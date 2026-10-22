local Translator = require("src/translator")
local DialogueLoader = require("src/dialogue_loader")
local QuestHighlighter = require("src/quest_highlighter")

local DialogueHook = {}

-- Modo depuración (desactivado para producción / juego silencioso)
local DEBUG = false

local function dlog(...)
    if DEBUG then log(...) end
end

-- Caché del último texto traducido por componente
local lastCompText = {}

--- Extrae una propiedad de una tabla o userdata C++ de forma segura
local function safeGet(tbl, key)
    if not tbl then return nil end
    local ok, res = pcall(function() return tbl[key] end)
    if ok and res ~= nil then return res end
    return nil
end

--- Extrae el texto legible de forma segura
local function getCompText(comp)
    if not comp then return nil, nil end
    local text, prop = nil, nil
    pcall(function()
        if comp.content and type(comp.content) == "string" and #comp.content > 0 then
            text = comp.content
            prop = "content"
        elseif comp.label and type(comp.label) == "string" and #comp.label > 0 then
            text = comp.label
            prop = "label"
        end
    end)
    return text, prop
end

--- Asigna el texto traducido al componente de forma limpia
local function setCompText(comp, text, prop)
    if not comp or not text then return false end
    local ok = false
    pcall(function()
        if prop == "content" then
            comp.content = text
            ok = true
        elseif prop == "label" then
            comp.label = text
            ok = true
        elseif comp.content ~= nil then
            comp.content = text
            ok = true
        elseif comp.label ~= nil then
            comp.label = text
            ok = true
        end
    end)
    return ok
end

--- Limpia y valida el nombre de un NPC a partir del texto del componente
local function cleanNpcName(raw)
    if not raw or type(raw) ~= "string" or #raw < 2 or #raw > 40 then return nil end
    local clean = string.gsub(raw, "<col=[%x]+>", "")
    clean = string.gsub(clean, "</col>", "")
    clean = string.gsub(clean, "%s*%(level%s*%-?%d+%)", "")
    clean = string.match(clean, "^%s*(.-)%s*$")
    if not clean or #clean < 2 or #clean > 40 then return nil end

    local lower = string.lower(clean)

    -- Descartar si coincide con el nombre del jugador
    local isPlayer = false
    pcall(function()
        if Player and Player.IsAvailable and Player.IsAvailable() then
            local pe = Player.GetEntity()
            if pe and pe.displayName and string.lower(pe.displayName) == lower then
                isPlayer = true
            end
        end
    end)
    if isPlayer then return nil end

    -- Descartar botones, preguntas o frases de control de interfaz
    if string.find(lower, "continue")
       or string.find(lower, "option")
       or string.find(lower, "select")
       or string.find(lower, "choose")
       or string.find(lower, "click")
       or string.find(lower, "please wait")
       or string.find(lower, "what would you like")
       or string.find(clean, "<p=")
       or string.find(clean, "[\r\n%?!;]") then
        return nil
    end

    return clean
end

--- Procesa un componente individual para traducir su texto limpiamente
local function processComponent(comp, ifaceId, compId)
    if not comp then return end

    local text, prop = getCompText(comp)
    if text and #text > 1 then
        local compKey = string.format("%s_%s", tostring(ifaceId), tostring(compId))

        -- Si el componente ya tiene la versión traducida o procesada aplicada, no reprocesar
        if lastCompText[compKey] == text then
            return
        end

        -- Si es el título/nombre del NPC en la interfaz de diálogo, actualizar NPC activo y no traducirlo
        local cleanName = cleanNpcName(text)
        if cleanName and (compId == 10 or compId == 11 or compId <= 8) and (ifaceId == 1184 or ifaceId == 1185 or ifaceId == 1189 or ifaceId == 1190) then
            DialogueLoader.SetActiveNPC(cleanName)
            lastCompText[compKey] = text
            return
        end

        -- Traducir texto informando el NPC activo actual si existe
        local activeNpc = DialogueLoader.GetActiveNPC()
        local trans = Translator.Translate(text, activeNpc)
        if trans and trans ~= text then
            local applied = setCompText(comp, trans, prop)
            if applied then
                lastCompText[compKey] = trans
                dlog(string.format(">>> [TRADUCIDO IF %s:%s] '%s' -> '%s'", tostring(ifaceId), tostring(compId), text, trans))
            else
                lastCompText[compKey] = text
            end
        else
            lastCompText[compKey] = text
        end
    end
end

--- Escaneo ultrarrápido en Event.Draw (justo antes de renderizar cada frame)
--- Elimina al 100% el flasheo en inglés traduciendo el texto antes de que toque la pantalla
local function scanFastDialogue()
    if not ui or not ui.Interfaces then return end

    pcall(function()
        -- 1. DETECCIÓN PRIORITARIA DEL NPC QUE HABLA Y DIÁLOGO ACTIVO
        -- Solo escanea si alguna interfaz de diálogo de NPC está realmente abierta
        for _, ifId in ipairs({ 1184, 1185, 1189, 1190 }) do
            local iface = nil
            pcall(function() iface = ui.Interfaces:GetInterface(ifId) end)
            if iface then
                -- Detección del nombre
                for sid = 0, 15 do
                    local titleComp = iface:GetComponent(sid)
                    if titleComp and (not titleComp.hidden and titleComp.visible ~= false) then
                        local name = getCompText(titleComp)
                        local clean = cleanNpcName(name)
                        if clean then
                            DialogueLoader.SetActiveNPC(clean)
                            break
                        end
                    end
                end
                -- Traducción del diálogo
                for sid = 0, 30 do
                    local c = iface:GetComponent(sid)
                    if c then processComponent(c, ifId, sid) end
                end
                break -- Solo una interfaz de diálogo de NPC está activa a la vez
            end
        end

        -- 2. RESALTADO CIAN NATIVO PARA QUEST HELPER Y TRADUCCIÓN DE OPCIONES (Interfaces 1188 y 720)
        local iface1188 = nil
        pcall(function() iface1188 = ui.Interfaces:GetInterface(1188) end)
        if iface1188 then
            QuestHighlighter.ScanAndHighlight(0.02)
            for sid = 0, 45 do
                local comp = iface1188:GetComponent(sid)
                if comp then processComponent(comp, 1188, sid) end
            end
        end

        local iface720 = nil
        pcall(function() iface720 = ui.Interfaces:GetInterface(720) end)
        if iface720 then
            QuestHighlighter.ScanAndHighlight(0.02)
            for sid = 0, 30 do
                local comp = iface720:GetComponent(sid)
                if comp then processComponent(comp, 720, sid) end
            end
        end

        -- 3. Componentes directos de diálogo (CHAT_V2_LEFT / RIGHT)
        local leftId = safeGet(id and id.Component, "CHAT_V2_LEFT__CHAT_TEXT")
        if leftId then
            local comp = ui.Interfaces:GetComponent(leftId)
            if comp then processComponent(comp, "direct", "CHAT_V2_LEFT__CHAT_TEXT") end
        end

        local rightId = safeGet(id and id.Component, "CHAT_V2_RIGHT__CHAT_TEXT")
        if rightId then
            local comp = ui.Interfaces:GetComponent(rightId)
            if comp then processComponent(comp, "direct", "CHAT_V2_RIGHT__CHAT_TEXT") end
        end

        -- 4. Interface 1191 (Jugador habla)
        local iface1191 = nil
        pcall(function() iface1191 = ui.Interfaces:GetInterface(1191) end)
        if iface1191 then
            for sid = 0, 30 do
                local c1191 = iface1191:GetComponent(sid)
                if c1191 then processComponent(c1191, 1191, sid) end
            end
        end

        -- 5. Interfaces de mensajes del sistema y popups (1186, 1187, 1192)
        for _, ifId in ipairs({ 1186, 1187, 1192 }) do
            local ifMsg = nil
            pcall(function() ifMsg = ui.Interfaces:GetInterface(ifId) end)
            if ifMsg then
                for sid = 0, 35 do
                    local c = ifMsg:GetComponent(sid)
                    if c then processComponent(c, ifId, sid) end
                end
            end
        end

        -- 6. Interface 1500 (QUEST_JOURNAL)
        local iface1500 = nil
        pcall(function() iface1500 = ui.Interfaces:GetInterface(1500) end)
        if iface1500 then
            for sid = 0, 40 do
                local c1500 = iface1500:GetComponent(sid)
                if c1500 then processComponent(c1500, 1500, sid) end
            end
            local cAccept = iface1500:GetComponent(409)
            if cAccept then processComponent(cAccept, 1500, 409) end
        end
    end)
end

--- Escaneo general de interfaces de diálogo (cada 5 ticks / 100ms en Logic)
function DialogueHook.ScanDialogueInterfaces()
    if not ui or not ui.Interfaces then return end

    -- 1. Ejecutar escaneo rápido prioritario
    scanFastDialogue()

    -- 2. Rango completo de diálogos y popups (1180 a 1205)
    -- Solo escanea componentes si la interfaz está cargada en el cliente
    for ifaceId = 1180, 1205 do
        local iface = nil
        pcall(function() iface = ui.Interfaces:GetInterface(ifaceId) end)
        if iface then
            for sid = 0, 35 do
                local comp = iface:GetComponent(sid)
                if comp then
                    processComponent(comp, ifaceId, sid)
                end
            end
        end
    end

    -- 3. Interfaces especiales (1501, 1243, 1177, 669 y 162)
    for _, ifId in ipairs({ 1501, 1243, 1177, 669, 162 }) do
        local iface = nil
        pcall(function() iface = ui.Interfaces:GetInterface(ifId) end)
        if iface then
            for sid = 0, 30 do
                local comp = iface:GetComponent(sid)
                if comp then processComponent(comp, ifId, sid) end
            end
        end
    end
end

function DialogueHook.Init()
    -- 1. Interceptar mensajes de chat del juego
    if Event.ChatMessage then
        Event.ChatMessage.Subscribe("rs_traductor_chat", function(event)
            if not event or not event.chatMessage then return end

            local raw = event.chatMessage
            local translated = Translator.Translate(raw)
            if translated and translated ~= raw then
                event.chatMessage = translated
                dlog(string.format("[Traductor Chat] '%s' -> '%s'", raw, translated))
            end
        end)
    end

    -- 2. ANTIFLASHEO en Event.Draw: se ejecuta ANTES de que el cliente pinte el frame en pantalla
    if Event.Draw then
        Event.Draw.Subscribe("rs_traductor_draw_instant", function()
            scanFastDialogue()
        end)
    end

    -- 3. Escáner de interfaces secundarias en Client Logic (cada 5 ticks, ~100ms)
    local logicCount = 0
    if Event.Logic then
        Event.Logic.Subscribe("rs_traductor_fast_scan", function()
            logicCount = logicCount + 1
            if logicCount % 5 == 0 then
                DialogueHook.ScanDialogueInterfaces()
            end
        end)
    end

    -- 4. Carga progresiva de diccionarios en segundo plano (ServerLogic ~600ms)
    if Event.ServerLogic then
        Event.ServerLogic.Subscribe("rs_traductor_ticks", function()
            DialogueLoader.TickBackgroundLoad()
            Translator.ClearNegativeCache()
        end)
    end

    log(">>> [RS Traductor] Escáner ACTIVO (Antiflasheo + Compatibilidad Quest Helper habilitados).")
end

function DialogueHook.Shutdown()
    pcall(function() Event.ChatMessage.Unsubscribe("rs_traductor_chat") end)
    pcall(function() Event.Draw.Unsubscribe("rs_traductor_draw_instant") end)
    pcall(function() Event.Logic.Unsubscribe("rs_traductor_fast_scan") end)
    pcall(function() Event.ServerLogic.Unsubscribe("rs_traductor_ticks") end)
    QuestHighlighter.ClearHighlight()
    lastCompText = {}
    log(">>> [RS Traductor] Gancho de diálogos apagado.")
end

return DialogueHook
