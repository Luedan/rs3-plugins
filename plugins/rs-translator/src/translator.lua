local EntityGuard = require("src/entity_guard")
local Dictionary = require("src/dictionary")
local DialogueLoader = require("src/dialogue_loader")

local Translator = {}

local DB_CACHE_PREFIX = "rs_tr_cache_"
local memoryCache = {}

local function getPDB()
    return PersistentDB or (core and core.PersistentDB)
end

--- Obtiene una traducción previa desde memoria RAM o la base de datos local SQLite (PersistentDB)
local function getCached(hash)
    if memoryCache[hash] then
        return memoryCache[hash]
    end

    local pdb = getPDB()
    if not pdb then return nil end

    local ok, res = pcall(function()
        if pdb.GetString then
            return pdb:GetString(DB_CACHE_PREFIX .. hash)
        elseif pdb.Get then
            return pdb:Get(DB_CACHE_PREFIX .. hash)
        end
    end)

    if ok and res and type(res) == "string" and #res > 0 then
        memoryCache[hash] = res
        return res
    end
    return nil
end

--- Guarda una traducción permanentemente en memoria y en la base de datos local SQLite
local function setCached(hash, val)
    if not val or #val == 0 then return end
    memoryCache[hash] = val

    local pdb = getPDB()
    if not pdb then return end

    pcall(function()
        if pdb.SetString then
            pdb:SetString(DB_CACHE_PREFIX .. hash, val)
        elseif pdb.Set then
            pdb:Set(DB_CACHE_PREFIX .. hash, val)
        end
    end)
end

local function simpleHash(str)
    local h = 5381
    for i = 1, #str do
        h = ((h << 5) + h) + string.byte(str, i)
        h = h & 0x7FFFFFFF
    end
    return tostring(h)
end

--- Extrae etiquetas de formato de RuneScape (<p=...>, <col=...>, </col>, <shad=...>, </shad>)
local function stripFormatting(text)
    if not text then return "", "", "" end
    local prefix = ""
    local suffix = ""
    local clean = text

    -- Extraer todas las etiquetas iniciales (<p=2>, <col=ffffff>, etc.)
    while true do
        local tagStart, tagEnd, tag = string.find(clean, "^(<[^>]+>)")
        if tag then
            prefix = prefix .. tag
            clean = string.sub(clean, tagEnd + 1)
        else
            break
        end
    end

    -- Extraer todas las etiquetas finales (</col>, </p>, etc.)
    while true do
        local tagStart, tagEnd, tag = string.find(clean, "(<[^>]+>)$")
        if tag then
            suffix = tag .. suffix
            clean = string.sub(clean, 1, tagStart - 1)
        else
            break
        end
    end

    -- Limpiar espacios en blanco al inicio y final
    local trimmed = string.match(clean, "^%s*(.-)%s*$")
    if trimmed then clean = trimmed end

    return clean, prefix, suffix
end

--- Traduce una frase respetando la base de datos local, diccionarios de NPCs y entidades en inglés
function Translator.Translate(text, optNPC)
    if not text or #text == 0 then return text end

    -- Ignorar comandos de consola o cadenas puramente numéricas
    if string.find(text, "^%d+$") or string.find(text, "^[/%~]") then
        return text
    end

    -- 1. Separar etiquetas de formato (color, sombra)
    local cleanText, prefix, suffix = stripFormatting(text)
    if #cleanText == 0 then return text end

    -- Extraer numeración de opción si la tiene (ej. "1. ", "2. ", "1: ", "[1] ")
    local optNum = string.match(cleanText, "^(%d+[%.:]%s+)") or string.match(cleanText, "^(%[%d+%]%s+)")
    if optNum then
        prefix = prefix .. optNum
        cleanText = string.sub(cleanText, #optNum + 1)
        cleanText = string.match(cleanText, "^%s*(.-)%s*$") or cleanText
    end

    -- 2. PRIORIDAD 1: Diálogos pretraducidos de NPCs y opciones (offline en memoria RAM)
    local npcTrans = DialogueLoader.Translate(cleanText, optNPC)
    if npcTrans and npcTrans ~= cleanText then
        return prefix .. npcTrans .. suffix
    end

    -- 3. PRIORIDAD 2: Diccionario de frases fijas del juego y botones
    local dictRes = Dictionary.exact[cleanText]
    if not dictRes and string.sub(cleanText, -1) == "?" then
        dictRes = Dictionary.exact[string.sub(cleanText, 1, -2)]
    end
    if not dictRes and string.sub(cleanText, -1) == "." then
        dictRes = Dictionary.exact[string.sub(cleanText, 1, -2)]
    end
    if dictRes then
        return prefix .. dictRes .. suffix
    end

    -- 4. PRIORIDAD 3: Patrones dinámicos offline con protección de entidades
    local masked, entities = EntityGuard.Protect(cleanText)
    local translatedMasked = nil
    if Dictionary.exact[masked] then
        translatedMasked = Dictionary.exact[masked]
    else
        for _, rule in ipairs(Dictionary.patterns) do
            if string.find(masked, rule.pat) then
                translatedMasked = string.gsub(masked, rule.pat, rule.rep)
                break
            end
        end
    end

    -- 5. PRIORIDAD 4: Reglas gramaticales rápidas
    if not translatedMasked then
        local temp = masked
        temp = string.gsub(temp, "^You are in (.-)%.$", "Estás en %1.")
        temp = string.gsub(temp, "^You're in (.-)%.$", "Estás en %1.")
        temp = string.gsub(temp, "^You are at (.-)%.$", "Estás en %1.")
        temp = string.gsub(temp, "^This is (.-)%.$", "Este es %1.")
        temp = string.gsub(temp, "^I am (.-)%.$", "Soy %1.")
        temp = string.gsub(temp, "^I'm (.-)%.$", "Soy %1.")
        temp = string.gsub(temp, "^You don't have ", "No tienes ")
        temp = string.gsub(temp, "^You do not have ", "No tienes ")
        temp = string.gsub(temp, "^You cannot ", "No puedes ")
        temp = string.gsub(temp, "^You can't ", "No puedes ")
        temp = string.gsub(temp, "^You need to ", "Necesitas ")
        temp = string.gsub(temp, "^You must ", "Debes ")
        temp = string.gsub(temp, "^You talk to ", "Hablas con ")

        if temp ~= masked then
            translatedMasked = temp
        end
    end

    -- 6. Si hubo coincidencia con entidades restauradas, retornar
    if translatedMasked then
        local finalRes = EntityGuard.Restore(translatedMasked, entities)
        return prefix .. finalRes .. suffix
    end

    -- 7. Consultar SQLite cache solo para cadenas previamente procesadas
    local h = simpleHash(cleanText)
    local cached = getCached(h)
    if cached and cached ~= cleanText then
        return prefix .. cached .. suffix
    end

    return text
end

return Translator
