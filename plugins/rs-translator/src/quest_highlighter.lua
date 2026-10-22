--- ============================================================================
--- Módulo: QuestHighlighter (Resaltado Cian de Opciones de Misión)
--- Detecta opciones de misión (en inglés o español) y dibuja el rectángulo cian
--- idéntico al de Quest Helper (categoría 224, pulsante, nativo y limpio).
--- Funciona independientemente de si Quest Helper está activo o no, sin alterar texto.
--- ============================================================================

local QuestSteps = require("src/data/quest_dialogue_steps")

local QuestHighlighter = {}

local HIGHLIGHT_CATEGORY = 224
local CREATE_CAP = 32
local activeHighlights = {}
local animTime = 0

--- Función de llamada protegida que devuelve el resultado o nil
local function safe(fn)
    local ok, v = pcall(fn)
    if ok then return v end
    return nil
end

--- Normaliza una cadena para comparaciones seguras
local function norm(s)
    if not s then return "" end
    s = tostring(s):gsub("<[^>]*>", " ")
    s = s:gsub("%s+", " "):gsub("^%s+", ""):gsub("%s+$", ""):lower()
    return s
end

--- Elimina signos de apertura y puntuación final
local function stripPunct(s)
    if not s then return "" end
    s = s:gsub("^[¡¿]", ""):gsub("[%!%?%.;,:]$", ""):gsub("^%s+", ""):gsub("%s+$", "")
    return s
end

--- Extrae la parte de texto eliminando prefijos de numeración como "1. ", "2: ", "[3] "
local function stripNumberPrefix(s)
    if not s then return "" end
    local clean = s:gsub("<[^>]*>", "")
    local bare = clean:match("^%d+[%.:%-]?%s*(.*)$") or clean:match("^%[%d+%]%s*(.*)$") or clean
    return bare:match("^%s*(.-)%s*$") or bare
end

local cachedActiveQuest = nil
local lastDbCheckTime = 0

--- Obtiene la misión activa actualmente en Quest Helper desde PluginData.db
function QuestHighlighter.GetActiveQuest()
    local now = 0
    if os and os.clock then
        now = os.clock()
    end

    if now - lastDbCheckTime < 0.5 and lastDbCheckTime > 0 then
        return cachedActiveQuest
    end
    lastDbCheckTime = now

    if not io or not io.open then
        return nil
    end

    local ok, questName = pcall(function()
        local f = io.open("C:/ProgramData/Jagex/RuneScape-BETA/plugins/PluginData.db", "rb")
        if not f then return nil end
        local size = f:seek("end") or 0
        local readSize = math.min(size, 65536)
        f:seek("set", math.max(0, size - readSize))
        local data = f:read("*a")
        f:close()
        if not data then return nil end

        local last = nil
        for q in data:gmatch("Quest HelperactiveEntry[^\x00]*[\x01-\x05]([^\x00\r\n]+)%z") do
            last = q
        end
        return last
    end)

    if ok and questName and type(questName) == "string" and #questName > 0 then
        cachedActiveQuest = norm(questName)
    else
        cachedActiveQuest = nil
    end

    return cachedActiveQuest
end

--- Comprueba si una opción de diálogo (en inglés o español) es un paso de misión
--- Garantiza CERO falsos positivos: sólo coincidencias exactas, nunca búsqueda por subcadena
function QuestHighlighter.MatchesQuestStep(text)
    if not text or #text == 0 then return false end

    local clean = stripNumberPrefix(text)
    local nClean = norm(clean)
    if nClean == "" then return false end
    local bare = stripPunct(nClean)

    -- 1. Pasos universales de inicio de misión (sólo coincidencias exactas, ej. "I'm looking for a quest!")
    if QuestSteps.universal then
        if QuestSteps.universal[nClean] or (bare ~= "" and QuestSteps.universal[bare]) then
            return true
        end
    end

    -- 2. Pasos de la misión actualmente activa en Quest Helper (si hay una activa)
    local activeQuest = QuestHighlighter.GetActiveQuest()
    if activeQuest and QuestSteps.byQuest then
        local qSteps = QuestSteps.byQuest[activeQuest]
        if qSteps then
            if qSteps[nClean] or (bare ~= "" and qSteps[bare]) then
                return true
            end
        end
    end

    -- 3. Respaldo general: SÓLO pasos largos inequívocos (>= 15 caracteres) con coincidencia exacta
    -- NUNCA pasos cortos genéricos ("yes", "no", "si", "chat")
    if not activeQuest and QuestSteps.longSteps and #bare >= 15 then
        if QuestSteps.longSteps[nClean] or QuestSteps.longSteps[bare] then
            return true
        end
    end

    return false
end

--- Recorrido recursivo de componentes de interfaz (compatible con RS3 Beta)
local function recurseWalk(node, visit, depth, budget)
    if node == nil or depth > budget.maxDepth or budget.n <= 0 then return end
    for _, method in ipairs({ "IterateDynamicComponents", "IterateStaticComponents" }) do
        pcall(function()
            if node[method] then
                node[method](node, function(child, visible)
                    if budget.n <= 0 then return true end
                    budget.n = budget.n - 1
                    visit(child, node, visible, depth)
                    recurseWalk(child, visit, depth + 1, budget)
                    return budget.n <= 0
                end)
            end
        end)
    end
end

local function ifaceWalk(ifaceId, visit, opts)
    opts = opts or {}
    local iface = safe(function() return ui.Interfaces:GetInterface(ifaceId) end)
    if iface == nil then return false end
    local budget = { n = opts.maxComps or 600, maxDepth = opts.maxDepth or 8 }
    local maxStatic = opts.maxStatic or 300
    for sid = 0, maxStatic do
        if budget.n <= 0 then break end
        local comp = safe(function() return iface:GetComponent(sid) end)
        if comp ~= nil then
            budget.n = budget.n - 1
            visit(comp, nil, true, 0)
            recurseWalk(comp, visit, 1, budget)
        end
    end
    return true
end

--- Clave única de componente
local function keyOf(comp)
    if not comp then return "" end
    return table.concat({
        tostring(comp.interfaceID or 0),
        tostring(comp.staticID or 0),
        tostring(comp.categoryID or 0),
        tostring(comp.dynamicID or 0)
    }, ":")
end

--- Busca un rectángulo existente por dynamicId en el padre
local function findHl(parent, slot)
    if not parent or not ui or not ui.Interfaces or not ui.Interfaces.GetComponent then return nil end
    return safe(function()
        return ui.Interfaces:GetComponent(parent.interfaceID, parent.staticID, HIGHLIGHT_CATEGORY, slot)
    end)
end

--- Asegura que un rectángulo cian esté dibujado y posicionado sobre un target { parent, x, y, w, h }
local function ensureHl(target, key)
    local parent = target.parent
    if not parent then return nil end

    local rec = activeHighlights[key]
    if rec and (rec.interfaceId ~= parent.interfaceID or rec.staticId ~= parent.staticID) then
        local oldHl = findHl({ interfaceID = rec.interfaceId, staticID = rec.staticId }, rec.dynamicId)
        if oldHl and oldHl.Destroy then pcall(function() oldHl:Destroy() end) end
        activeHighlights[key] = nil
        rec = nil
    end

    if not rec then
        local used = {}
        for _, entry in pairs(activeHighlights) do
            used[entry.dynamicId] = true
        end
        local slot = 0
        while used[slot] do slot = slot + 1 end
        if slot >= CREATE_CAP then return nil end

        rec = { interfaceId = parent.interfaceID, staticId = parent.staticID, dynamicId = slot }
        activeHighlights[key] = rec
    end

    local hl = findHl(parent, rec.dynamicId)
    if not hl then
        if ui and ui.Rectangle and ui.Rectangle.new then
            hl = safe(function() return ui.Rectangle.new(parent, HIGHLIGHT_CATEGORY, rec.dynamicId) end)
        end
        if not hl then
            activeHighlights[key] = nil
            return nil
        end
        hl.fill = true
        hl.clickthrough = true
        if hl.MoveToFront then hl:MoveToFront() end
    end

    if hl.x ~= target.x or hl.y ~= target.y then
        if hl.SetPos then hl:SetPos(target.x, target.y) end
    end
    if hl.width ~= target.w or hl.height ~= target.h then
        if hl.SetSize then hl:SetSize(target.w, target.h) end
    end

    return hl
end

--- Escanea una interfaz de opciones (1188 o 720) y localiza las filas de opciones que deben resaltarse
local function scanInterfaceForTargets(ifaceId, out)
    local nodes, byComponent = {}, {}
    local walked = ifaceWalk(ifaceId, function(comp, parent)
        local node = byComponent[comp]
        if node then
            if parent then node.parent = parent end
            return
        end
        local text = comp.content or comp.label or ""
        local matches = false
        if #text > 1 then
            matches = QuestHighlighter.MatchesQuestStep(text)
        end
        node = {
            comp = comp,
            parent = parent,
            visible = comp.visible,
            match = matches,
        }
        byComponent[comp] = node
        nodes[#nodes + 1] = node
    end, { maxComps = 600, maxStatic = 250 })

    if not walked then return end

    local function isVisible(node)
        while node do
            if node.visible == false then return false end
            node = byComponent[node.parent]
        end
        return true
    end

    local picked = {}
    for _, node in ipairs(nodes) do
        if node.match and isVisible(node) then
            local current = node
            while current do
                local comp = current.comp
                local height = comp.height or 0
                if current.visible ~= false
                   and current.parent
                   and (height >= 8 and height <= 45 and (comp.x or 0) >= 0) then
                    if not picked[comp] then
                        picked[comp] = true
                        out[#out + 1] = {
                            comp = comp,
                            parent = current.parent,
                            x = comp.x or 0,
                            y = comp.y or 0,
                            w = comp.width or 0,
                            h = height
                        }
                    end
                    break
                end
                current = byComponent[current.parent]
            end
        end
    end
end

--- Escanea las interfaces de diálogo de misiones y aplica el resaltado cian
function QuestHighlighter.ScanAndHighlight(dt)
    animTime = animTime + (dt or 0.02)
    local p = 0.5 + 0.5 * math.sin(animTime * 5)
    local alpha = 0.22 + 0.30 * p

    local targets = {}

    -- 1. Interface 1188 (CHOICE_V2 - opciones de respuesta habituales)
    scanInterfaceForTargets(1188, targets)

    -- 2. Interface 720 (MODAL_CHOICE - opciones emergentes)
    scanInterfaceForTargets(720, targets)

    -- 3. Interface 1500 (QUEST_JOURNAL / Resumen de misión - Botón Aceptar Misión)
    pcall(function()
        if ui and ui.Interfaces then
            local acceptBtn = ui.Interfaces:GetComponent(1500, 409)
            if acceptBtn and (not acceptBtn.hidden and acceptBtn.visible ~= false) and acceptBtn.parent then
                targets[#targets + 1] = {
                    comp = acceptBtn,
                    parent = acceptBtn.parent,
                    x = acceptBtn.x or 0,
                    y = acceptBtn.y or 0,
                    w = acceptBtn.width or 0,
                    h = acceptBtn.height or 0
                }
            end
        end
    end)

    -- Si no hay opciones coincidentes, limpiar cualquier rectángulo previo
    if #targets == 0 then
        QuestHighlighter.ClearHighlight()
        return 0
    end

    -- Actualizar o crear rectángulos cian para los objetivos encontrados
    local wanted = {}
    local shown = 0

    for _, t in ipairs(targets) do
        local key = keyOf(t.comp)
        wanted[key] = true
        local hl = ensureHl(t, key)
        if hl then
            if Vector4 and Vector4.new then
                hl.colour = Vector4.new(0, 0.8, 0.8, alpha)
            end
            hl.hidden = false
            shown = shown + 1
        end
    end

    -- Eliminar rectángulos de opciones que ya no son válidas
    for key, rec in pairs(activeHighlights) do
        if not wanted[key] then
            local oldHl = findHl({ interfaceID = rec.interfaceId, staticID = rec.staticId }, rec.dynamicId)
            if oldHl and oldHl.Destroy then pcall(function() oldHl:Destroy() end) end
            activeHighlights[key] = nil
        end
    end

    return shown
end

--- Elimina todos los rectángulos de resaltado
function QuestHighlighter.ClearHighlight()
    for key, rec in pairs(activeHighlights) do
        pcall(function()
            local oldHl = findHl({ interfaceID = rec.interfaceId, staticID = rec.staticId }, rec.dynamicId)
            if oldHl and oldHl.Destroy then
                oldHl:Destroy()
            elseif oldHl and oldHl.hidden ~= nil then
                oldHl.hidden = true
            end
        end)
    end
    activeHighlights = {}
end

return QuestHighlighter
