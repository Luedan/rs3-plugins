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

-- Cola de letras para carga progresiva en segundo plano (para no congelar el juego al iniciar)
local pendingLetters = {
    "C", "B", "A", "D", "M", "S", "T", "W", "G", "F",
    "E", "I", "J", "K", "L", "N", "O", "P", "Q", "R",
    "U", "V", "X", "Y", "Z", "NUM"
}

--- Carga una letra de diálogos si no está cargada
local function loadLetter(letter)
    if not letter or #letter == 0 then return nil end
    local upper = string.upper(letter)
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

--- Inicializa los diccionarios base (comenzando por la letra H)
function DialogueLoader.Init()
    loadLetter("H")
    log(">>> [DialogueLoader] Inicializado con éxito. Diálogos de NPCs (A-Z y #) listos.")
end

--- Tarea en segundo plano para cargar gradualmente las letras restantes
function DialogueLoader.TickBackgroundLoad()
    while #pendingLetters > 0 do
        local nextLetter = table.remove(pendingLetters, 1)
        if loadedLetters[nextLetter] == nil then
            loadLetter(nextLetter)
            break
        end
    end
end

--- Establece el NPC activo actual
function DialogueLoader.SetActiveNPC(npcName)
    if not npcName or #npcName == 0 then return end
    -- Limpiar posibles etiquetas de color o niveles
    local clean = string.gsub(npcName, "<col=[%x]+>", "")
    clean = string.gsub(clean, "</col>", "")
    clean = string.gsub(clean, "%s*%(level%s*%-?%d+%)", "")
    clean = string.match(clean, "^%s*(.-)%s*$")
    if clean and #clean > 0 then
        local lower = string.lower(clean)
        -- Descartar frases de interfaz que no son nombres de NPCs
        if lower == "select an option" or lower == "choose an option"
           or lower == "please wait..." or lower == "please wait"
           or string.find(lower, "continue") or string.find(lower, "click") then
            return
        end
        if currentActiveNPC ~= clean then
            currentActiveNPC = clean
            -- Pre-cargar la letra inmediatamente para este NPC bajo demanda
            loadLetter(clean)
        end
    end
end

--- Obtiene el NPC activo actual
function DialogueLoader.GetActiveNPC()
    return currentActiveNPC
end

local function lookupDirectOrPunct(tbl, str)
    if not tbl or not str then return nil end
    if tbl[str] then return tbl[str] end

    -- Con o sin comillas al inicio y final
    local unquoted = string.match(str, "^[\"'](.-)[\"']$")
    if unquoted and tbl[unquoted] then return tbl[unquoted] end

    -- Con o sin punto final
    if string.sub(str, -1) == "." then
        local noDot = string.sub(str, 1, -2)
        if tbl[noDot] then return tbl[noDot] end
    else
        local withDot = str .. "."
        if tbl[withDot] then return tbl[withDot] end
    end

    -- Con o sin interrogación o exclamación
    if string.sub(str, -1) == "?" then
        local noQ = string.sub(str, 1, -2)
        if tbl[noQ] then return tbl[noQ] end
    end
    if string.sub(str, -1) == "!" then
        local noEx = string.sub(str, 1, -2)
        if tbl[noEx] then return tbl[noEx] end
    end

    return nil
end

--- Intenta buscar una traducción en una tabla con variaciones de puntuación y espacios
local function lookupWithVariations(tbl, text)
    if not tbl or not text then return nil end

    -- 1. Búsqueda directa o variación de puntuación
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
                local res = lookupWithVariations(npcTable, text)
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
    -- buscar en la lista global de todas las letras cargadas
    for _, letterData in pairs(loadedLetters) do
        if letterData and letterData.all then
            local res = lookupWithVariations(letterData.all, text)
            if res then return res end
        end
    end

    return nil
end

return DialogueLoader
