--- ============================================================================
--- Módulo: QuestHelperHook (Compatibilidad Total con Quest Helper)
--- Permite que Quest Helper resalte las opciones de diálogo en azul/cian
--- incluso cuando RS Traductor ha traducido el texto al español.
--- ============================================================================

local QuestHelperHook = {}

-- Mapa bidireccional de textos traducidos en tiempo real
local originalEnglishBySpanish = {}
local spanishByEnglish = {}

local isHooked = false
local origMatchesAny = nil

--- Normaliza texto para comparaciones seguras
local function norm(s)
    if not s then return "" end
    s = tostring(s):gsub("<[^>]*>", " ")
    s = s:gsub("%s+", " "):gsub("^%s+", ""):gsub("%s+$", ""):lower()
    return s
end

--- Limpia signos de apertura españoles (¡, ¿) y puntuación común
local function stripInverted(s)
    if not s then return "" end
    s = s:gsub("^[¡¿]", ""):gsub("[%!%?%.]$", ""):gsub("^%s+", ""):gsub("%s+$", "")
    return s
end

--- Extrae la parte de texto eliminando prefijos de numeración como "1. ", "2: ", "[3] "
local function stripNumberPrefix(s)
    if not s then return "" end
    local clean = s:gsub("<[^>]*>", "")
    local bare = clean:match("^%d+[%.:]%s*(.*)$") or clean:match("^%[%d+%]%s*(.*)$") or clean
    return bare:match("^%s*(.-)%s*$") or bare
end

--- Registra un par de traducción (Inglés -> Español)
function QuestHelperHook.RegisterTranslation(english, spanish)
    if not english or not spanish or english == spanish then return end

    local nEs = norm(spanish)
    local nEn = norm(english)
    originalEnglishBySpanish[nEs] = english
    spanishByEnglish[nEn] = spanish

    -- También sin prefijo numérico
    local bareEs = norm(stripNumberPrefix(spanish))
    local bareEn = norm(stripNumberPrefix(english))
    if bareEs ~= nEs then
        originalEnglishBySpanish[bareEs] = stripNumberPrefix(english)
    end
    if bareEn ~= nEn then
        spanishByEnglish[bareEn] = stripNumberPrefix(spanish)
    end
end

--- Obtiene el texto original en inglés para un texto en español dado
function QuestHelperHook.GetOriginalEnglish(spanishText)
    if not spanishText then return nil end
    local n = norm(spanishText)
    if originalEnglishBySpanish[n] then
        return originalEnglishBySpanish[n]
    end
    local bare = norm(stripNumberPrefix(spanishText))
    if originalEnglishBySpanish[bare] then
        return originalEnglishBySpanish[bare]
    end
    return nil
end

--- Intercepta WidgetHighlight de Quest Helper
local function applyHookToWidgetHighlight(WidgetHighlight, Translator)
    if not WidgetHighlight or isHooked then return end
    if type(WidgetHighlight) ~= "table" or not WidgetHighlight.matchesAny then return end

    origMatchesAny = WidgetHighlight.matchesAny

    WidgetHighlight.matchesAny = function(content, texts)
        if not content or not texts or #texts == 0 then
            return false
        end

        -- 1. Intentar coincidencia nativa original (por si el texto aún está en inglés)
        if origMatchesAny(content, texts) then
            return true
        end

        -- 2. Si el texto en pantalla está en español, buscar su versión original en inglés
        local origEng = QuestHelperHook.GetOriginalEnglish(content)
        if origEng and origMatchesAny(origEng, texts) then
            return true
        end

        -- Si tiene número (ej. "3.   ¡Estoy buscando una misión!"), probar solo con la parte sin número
        local bareContent = stripNumberPrefix(content)
        local bareOrigEng = QuestHelperHook.GetOriginalEnglish(bareContent)
        if bareOrigEng and origMatchesAny(bareOrigEng, texts) then
            return true
        end

        -- 3. Traducir cada opción objetivo de Quest Helper al español y probar
        local translatedTargets = {}
        for _, t in ipairs(texts) do
            local trans = nil
            if Translator and Translator.Translate then
                trans = Translator.Translate(t)
            end
            if not trans then
                trans = spanishByEnglish[norm(t)]
            end

            if trans and trans ~= t then
                table.insert(translatedTargets, trans)
                local noPunct = stripInverted(trans)
                if noPunct ~= trans then
                    table.insert(translatedTargets, noPunct)
                end
            end
        end

        if #translatedTargets > 0 and origMatchesAny(content, translatedTargets) then
            return true
        end

        return false
    end

    isHooked = true
    log(">>> [RS Traductor] ¡Compatibilidad con Quest Helper ACTIVADA! (Resaltado azul garantizado)")
end

--- Intenta enganchar WidgetHighlight si ya está cargado en package.loaded
function QuestHelperHook.CheckAndHook(Translator)
    if isHooked then return true end

    if package and package.loaded then
        local wh = package.loaded["src/render/widgethighlight"]
        if wh then
            applyHookToWidgetHighlight(wh, Translator)
            return true
        end
    end
    return false
end

--- Comprobación pública exportada para otros plugins o hooks globales
function QuestHelperHook.MatchesAny(content, texts)
    if not content or not texts or #texts == 0 then return false end

    -- 1. Si el texto en pantalla coincide con el inglés original
    local origEng = QuestHelperHook.GetOriginalEnglish(content)
    if origEng then
        local nOrig = norm(origEng)
        for _, t in ipairs(texts) do
            local nt = norm(t)
            if nt ~= "" and nOrig:find(nt, 1, true) then return true end
        end
    end

    -- 2. Probar sin prefijos numéricos
    local bare = stripNumberPrefix(content)
    local bareEng = QuestHelperHook.GetOriginalEnglish(bare)
    if bareEng then
        local nBare = norm(bareEng)
        for _, t in ipairs(texts) do
            local nt = norm(t)
            if nt ~= "" and nBare:find(nt, 1, true) then return true end
        end
    end

    -- 3. Comprobar si content coincide con las traducciones de texts
    local nContent = norm(content)
    for _, t in ipairs(texts) do
        local es = spanishByEnglish[norm(t)]
        if es then
            local nes = norm(es)
            if nes ~= "" and nContent:find(nes, 1, true) then return true end
            local bareEs = nes:gsub("^[¡¿]", ""):gsub("[%!%?%.]$", "")
            if bareEs ~= "" and nContent:find(bareEs, 1, true) then return true end
        end
    end

    return false
end

function QuestHelperHook.Init(Translator)
    -- Exponer gancho global para cualquier plugin (como Quest Helper)
    if _G then
        _G.RSTranslatorHook = QuestHelperHook
    end

    -- 1. Probar si ya está cargado
    QuestHelperHook.CheckAndHook(Translator)

    -- 2. Interceptar _G.require para enganchar en el instante exacto en que Quest Helper lo requiera
    if not isHooked and _G and _G.require then
        local oldRequire = _G.require
        _G.require = function(modname)
            local res = oldRequire(modname)
            if (modname == "src/render/widgethighlight" or modname:find("widgethighlight")) and type(res) == "table" and res.matchesAny then
                applyHookToWidgetHighlight(res, Translator)
            end
            return res
        end
    end
end

function QuestHelperHook.Shutdown()
    if _G and _G.RSTranslatorHook == QuestHelperHook then
        _G.RSTranslatorHook = nil
    end
    if isHooked and origMatchesAny and package and package.loaded then
        local wh = package.loaded["src/render/widgethighlight"]
        if wh then
            wh.matchesAny = origMatchesAny
        end
    end
    isHooked = false
    origMatchesAny = nil
    originalEnglishBySpanish = {}
    spanishByEnglish = {}
end

return QuestHelperHook
