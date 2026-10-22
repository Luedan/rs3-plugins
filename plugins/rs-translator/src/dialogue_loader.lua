--- ============================================================================
--- Módulo: DialogueLoader (Cargador Modular de Diálogos Offline)
--- Carga los diccionarios de diálogos por NPC desde los módulos generados (A-Z y NUM)
--- Soporta carga bajo demanda inmediata y precarga progresiva en segundo plano
--- ============================================================================

local DialogueLoader = {}

-- Almacén de letras cargadas en memoria RAM
local loadedLetters = {}
-- Puntero al NPC con el que el jugador interactúa actualmente
local currentActiveNPC = nil

-- Cola de letras para carga progresiva en segundo plano
local pendingLetters = {
    "E", "I", "J", "K", "L", "N", "O", "P", "Q", "R",
    "U", "V", "W", "X", "Y", "Z", "NUM"
}

local NPC_NAME_ALIASES = {
    ["lumbridge guide"] = "Lumbridge Sage",
    ["phileas"] = "Lumbridge Sage",
    ["sage"] = "Lumbridge Sage",
    ["donnie"] = "Donie",
    ["restless ghost"] = "Restless ghost",
    ["ghost"] = "Restless ghost",
    ["aereck"] = "Father Aereck",
    ["urhney"] = "Father Urhney",
    ["duke"] = "Duke Horacio",
    ["horacio"] = "Duke Horacio",
    ["cook"] = "Cook",
}

--- Carga una letra de diálogos si no está cargada
local function loadLetter(letter)
    if not letter or #letter == 0 then return nil end
    local cleanLetter = string.lower(letter)
    if NPC_NAME_ALIASES[cleanLetter] then
        cleanLetter = NPC_NAME_ALIASES[cleanLetter]
    end
    local upper = string.upper(cleanLetter)
    if upper ~= "NUM" then
        upper = string.sub(upper, 1, 1)
        if not string.match(upper, "^[A-Z]$") then
            upper = "NUM"
        end
    end

    if loadedLetters[upper] ~= nil then
        return loadedLetters[upper]
    end

    local path = "src/data/dialogues_" .. upper
    local ok, data = pcall(require, path)
    if ok and data and type(data) == "table" then
        loadedLetters[upper] = data
        return data
    else
        loadedLetters[upper] = false
        if not ok then
            log(string.format(">>> [DialogueLoader ERROR] Fallo al cargar %s: %s", path, tostring(data)))
        end
        return nil
    end
end

--- Inicializa los diccionarios base precargando las letras más frecuentes del juego
function DialogueLoader.Init()
    local fastLetters = { "H", "F", "D", "C", "A", "M", "S", "T", "G", "B" }
    for _, l in ipairs(fastLetters) do
        loadLetter(l)
    end
    log(">>> [DialogueLoader] Letras principales (H, F, D, C, A, M, S, T, G, B) precargadas en RAM.")
end

--- Tarea en segundo plano para cargar gradualmente las letras restantes
function DialogueLoader.TickBackgroundLoad()
    local count = 0
    while #pendingLetters > 0 and count < 2 do
        local nextLetter = table.remove(pendingLetters, 1)
        if loadedLetters[nextLetter] == nil then
            loadLetter(nextLetter)
            count = count + 1
        end
    end
end

--- Establece el NPC activo actual asegurando que sea un nombre válido y no el jugador
function DialogueLoader.SetActiveNPC(npcName)
    if not npcName or #npcName == 0 then return end

    -- Limpiar posibles etiquetas de color o niveles
    local clean = string.gsub(npcName, "<col=[%x]+>", "")
    clean = string.gsub(clean, "</col>", "")
    clean = string.gsub(clean, "%s*%(level%s*%-?%d+%)", "")
    clean = string.match(clean, "^%s*(.-)%s*$")
    if clean and #clean >= 2 and #clean <= 40 then
        local lower = string.lower(clean)

        -- Aplicar alias si coincide con algún nombre conocido
        if NPC_NAME_ALIASES[lower] then
            clean = NPC_NAME_ALIASES[lower]
            lower = string.lower(clean)
        end

        -- Descartar si coincide con el nombre de usuario del jugador
        local isPlayer = false
        pcall(function()
            if Player and Player.IsAvailable and Player.IsAvailable() then
                local pe = Player.GetEntity()
                if pe and pe.displayName and string.lower(pe.displayName) == lower then
                    isPlayer = true
                end
            end
        end)
        if isPlayer then return end

        -- Descartar frases de interfaz o botones de control
        if string.find(lower, "select") or string.find(lower, "choose")
           or string.find(lower, "continue") or string.find(lower, "click")
           or string.find(lower, "please wait") or string.find(lower, "option")
           or string.find(lower, "what would you like")
           or string.find(clean, "<p=") or string.find(clean, "[\r\n%?!;]") then
            return
        end

        -- Cargar la letra inmediatamente para este NPC
        local letterData = loadLetter(clean)
        if letterData and letterData.npcs then
            for realName, _ in pairs(letterData.npcs) do
                if string.lower(realName) == lower then
                    clean = realName
                    break
                end
            end
        end

        if currentActiveNPC ~= clean then
            currentActiveNPC = clean
        end
    end
end

--- Obtiene el NPC activo actual
function DialogueLoader.GetActiveNPC()
    return currentActiveNPC
end

--- Limpia el NPC activo actual
function DialogueLoader.ClearActiveNPC()
    currentActiveNPC = nil
end

local function normQuotes(s)
    if not s then return "" end
    return s:gsub("’", "'"):gsub("‘", "'"):gsub("“", '"'):gsub("”", '"'):gsub("…", "...")
end

--- Normaliza texto para comparación por tokens (elimina puntuación, minúsculas y normaliza plurales)
local function normTokens(s)
    if not s or #s == 0 then return "" end
    local q = normQuotes(s):lower()
    q = q:gsub("<[^>]*>", " ")
    q = q:gsub("[%.,!%?;:'\"…%-%–%—%(%)%[%]/\\|]", " ")
    local words = {}
    for w in q:gmatch("%S+") do
        if #w > 4 and w:sub(-2) == "es" then
            w = w:sub(1, -3)
        elseif #w > 4 and w:sub(-1) == "s" then
            w = w:sub(1, -2)
        end
        words[#words + 1] = w
    end
    return table.concat(words, " ")
end

--- Extrae un conjunto (set) de palabras para cálculo de similitud Jaccard
local function getWordSet(s)
    if not s or #s == 0 then return {}, 0 end
    local q = normQuotes(s):lower()
    q = q:gsub("<[^>]*>", " ")
    q = q:gsub("[%.,!%?;:'\"…%-%–%—%(%)%[%]/\\|]", " ")
    local set = {}
    local count = 0
    for w in q:gmatch("%S+") do
        if #w >= 3 then
            if not set[w] then
                set[w] = true
                count = count + 1
            end
        end
    end
    return set, count
end

--- Calcula la similitud Jaccard entre dos conjuntos de palabras
local function computeSimilarity(set1, count1, set2, count2)
    if count1 == 0 or count2 == 0 then return 0.0 end
    local inter = 0
    for w, _ in pairs(set1) do
        if set2[w] then
            inter = inter + 1
        end
    end
    local union = count1 + count2 - inter
    if union <= 0 then return 0.0 end
    return inter / union
end

local function lookupDirectOrPunct(tbl, str)
    if not tbl or not str then return nil end
    local qStr = normQuotes(str)
    if tbl[str] then return tbl[str] end
    if tbl[qStr] then return tbl[qStr] end

    -- Con o sin comillas al inicio y final
    local unquoted = string.match(qStr, "^[\"'](.-)[\"']$")
    if unquoted and (tbl[unquoted] or tbl[normQuotes(unquoted)]) then
        return tbl[unquoted] or tbl[normQuotes(unquoted)]
    end

    -- Con o sin punto final
    if string.sub(qStr, -1) == "." then
        local noDot = string.sub(qStr, 1, -2)
        if tbl[noDot] then return tbl[noDot] end
    else
        local withDot = qStr .. "."
        if tbl[withDot] then return tbl[withDot] end
    end

    -- Con o sin interrogación o exclamación
    if string.sub(qStr, -1) == "?" then
        local noQ = string.sub(qStr, 1, -2)
        if tbl[noQ] then return tbl[noQ] end
    end
    if string.sub(qStr, -1) == "!" then
        local noEx = string.sub(qStr, 1, -2)
        if tbl[noEx] then return tbl[noEx] end
    end

    -- Fallback si viene en mayúsculas completas (ej. títulos de interfaces)
    if #qStr >= 4 and qStr == string.upper(qStr) then
        local lower = string.lower(qStr)
        local title = lower:gsub("(%a)([%w_']*)", function(first, rest) return first:upper() .. rest:lower() end)
        if tbl[title] then return tbl[title] end
        if tbl[lower] then return tbl[lower] end
        if string.sub(title, -1) == "?" and tbl[string.sub(title, 1, -2)] then
            return tbl[string.sub(title, 1, -2)]
        end
    end

    return nil
end

--- Búsqueda inteligente por tokens y similitud semántica en la tabla del NPC
local function lookupNpcFuzzy(npcTable, text)
    if not npcTable or not text or #text < 4 then return nil end

    local nText = normTokens(text)
    if nText == "" then return nil end

    -- Nivel 1: Coincidencia normalizada de tokens y plurals (ej. hatchet == hatchets)
    for origText, transText in pairs(npcTable) do
        if normTokens(origText) == nText then
            return transText
        end
    end

    -- Nivel 2: Similitud por palabras para frases largas (>= 15 caracteres)
    if #text >= 15 then
        local targetSet, targetCount = getWordSet(text)
        if targetCount >= 3 then
            local bestMatch = nil
            local bestScore = 0.82 -- Umbral mínimo: 82% de palabras coincidentes

            for origText, transText in pairs(npcTable) do
                local lenDiff = math.abs(#origText - #text)
                if lenDiff < (#text * 0.40) then
                    local candSet, candCount = getWordSet(origText)
                    local sim = computeSimilarity(targetSet, targetCount, candSet, candCount)
                    if sim > bestScore then
                        bestScore = sim
                        bestMatch = transText
                    end
                end
            end

            if bestMatch then
                return bestMatch
            end
        end
    end

    return nil
end

--- Intenta buscar una traducción en una tabla con variaciones de puntuación, comillas y espacios
local function lookupWithVariations(tbl, text)
    if not tbl or not text then return nil end

    -- 1. Búsqueda directa o variación de comillas y puntuación
    local res = lookupDirectOrPunct(tbl, text)
    if res then return res end

    -- 2. Con saltos de línea, tags RS3 o múltiples espacios normalizados
    local norm = string.gsub(text, "<[^>]+>", " ")
    norm = string.gsub(norm, "\r?\n", " ")
    norm = string.gsub(norm, "%s+", " ")
    norm = string.match(norm, "^%s*(.-)%s*$")
    if norm and norm ~= text then
        res = lookupDirectOrPunct(tbl, norm)
        if res then return res end
    end

    return nil
end

--- Traduce un texto buscando primero en el NPC específico y luego en el almacén global
function DialogueLoader.Translate(text, overrideNPC)
    if not text or #text == 0 then return nil end

    local npcToQuery = overrideNPC or currentActiveNPC

    -- 1. Si conocemos el NPC, determinamos su letra correspondiente
    if npcToQuery and #npcToQuery > 0 then
        local letterData = loadLetter(npcToQuery)
        if letterData and letterData.npcs then
            -- A. Buscar en el NPC exacto
            local npcTable = letterData.npcs[npcToQuery]
            if not npcTable then
                -- B. Buscar si el nombre coincide ignorando mayúsculas/minúsculas
                local lowerNPC = string.lower(npcToQuery)
                for name, t in pairs(letterData.npcs) do
                    if string.lower(name) == lowerNPC then
                        npcTable = t
                        break
                    end
                end
            end

            if npcTable then
                -- Intento exacto / con puntuación
                local res = lookupWithVariations(npcTable, text)
                if res then return res end

                -- Intento fuzzy / tokens (elimina fallos por singular/plural o pequeñas erratas)
                res = lookupNpcFuzzy(npcTable, text)
                if res then return res end
            end
        end

        -- C. Si no se encontró en npcTable pero conocemos la letra, buscar en dialogues.all de esa letra
        if letterData and letterData.all then
            local res = lookupWithVariations(letterData.all, text)
            if res then return res end
        end
    end

    -- 2. Si no se encontró en el NPC o no sabemos el NPC (o es una opción de menú/respuesta),
    -- buscar en la lista global de todas las letras cargadas en memoria (búsqueda ultrarrápida O(1))
    for _, letterData in pairs(loadedLetters) do
        if letterData and letterData.all then
            local res = lookupWithVariations(letterData.all, text)
            if res then return res end
        end
    end

    return nil
end

return DialogueLoader
