local Translator = require("src/translator")
local DialogueLoader = require("src/dialogue_loader")

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

--- Asigna el texto traducido al componente
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

--- Procesa un componente individual para traducir su texto
local function processComponent(comp, ifaceId, compId)
    if not comp then return end

    local text, prop = getCompText(comp)
    if text and #text > 1 then
        local compKey = string.format("%s_%s", tostring(ifaceId), tostring(compId))

        -- Comprobar si parece el nombre de un NPC
        local clean = string.gsub(text, "<col=[%x]+>", "")
        clean = string.gsub(clean, "</col>", "")
        clean = string.gsub(clean, "%s*%(level%s*%-?%d+%)", "")
        clean = string.match(clean, "^%s*(.-)%s*$") or ""

        local isTitleComp = (ifaceId == 1184 or ifaceId == 1185 or ifaceId == 1186 or ifaceId == 1187 or ifaceId == 1191) and (compId == 10 or compId == 11)
        if isTitleComp and #clean >= 2 and #clean <= 40 then
            DialogueLoader.SetActiveNPC(clean)
        elseif #clean >= 2 and #clean <= 30 and not string.find(clean, "[\r\n%?!;]") and not string.find(clean, "<p=") then
            DialogueLoader.SetActiveNPC(clean)
        end

        if lastCompText[compKey] ~= text then
            local trans = Translator.Translate(text)
            if trans and trans ~= text then
                local applied = setCompText(comp, trans, prop)
                if applied then
                    lastCompText[compKey] = trans
                    dlog(string.format(">>> [TRADUCIDO IF %s:%s] '%s' -> '%s'", tostring(ifaceId), tostring(compId), text, trans))
                end
            else
                lastCompText[compKey] = text
            end
        end
    end
end

--- Escaneo ultrarrápido en Event.Draw (justo antes de renderizar cada frame)
--- Elimina al 100% el flasheo en inglés traduciendo el texto antes de que toque la pantalla
local function scanFastDialogue()
    if not ui or not ui.Interfaces then return end

    pcall(function()
        -- 1. Componentes directos de diálogo
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

        -- 2. Diálogo NPC en pantalla (1184, 1185, 1186, 1187, 1191)
        for sid = 8, 14 do
            local c1184 = ui.Interfaces:GetComponent(1184, sid)
            if c1184 then processComponent(c1184, 1184, sid) end

            local c1185 = ui.Interfaces:GetComponent(1185, sid)
            if c1185 then processComponent(c1185, 1185, sid) end

            local c1186 = ui.Interfaces:GetComponent(1186, sid)
            if c1186 then processComponent(c1186, 1186, sid) end

            local c1187 = ui.Interfaces:GetComponent(1187, sid)
            if c1187 then processComponent(c1187, 1187, sid) end

            local c1191 = ui.Interfaces:GetComponent(1191, sid)
            if c1191 then processComponent(c1191, 1191, sid) end
        end

        -- 3. Opciones de respuesta activas (1188)
        for sid = 5, 10 do
            local c1188 = ui.Interfaces:GetComponent(1188, sid)
            if c1188 then processComponent(c1188, 1188, sid) end
        end
        for sid = 30, 42 do
            local c1188 = ui.Interfaces:GetComponent(1188, sid)
            if c1188 then processComponent(c1188, 1188, sid) end
        end
    end)
end

--- Escaneo general de interfaces de diálogo (cada 2 ticks / 40ms en Logic)
function DialogueHook.ScanDialogueInterfaces()
    if not ui or not ui.Interfaces then return end

    -- 1. Ejecutar escaneo rápido prioritario
    scanFastDialogue()

    -- 2. Rango completo de diálogos y popups (1180 a 1205)
    for ifaceId = 1180, 1205 do
        for sid = 0, 35 do
            pcall(function()
                local comp = ui.Interfaces:GetComponent(ifaceId, sid)
                if comp then
                    processComponent(comp, ifaceId, sid)
                end
            end)
        end
    end

    -- 3. Interfaces especiales (669 y 162)
    for sid = 0, 15 do
        pcall(function()
            local c669 = ui.Interfaces:GetComponent(669, sid)
            if c669 then processComponent(c669, 669, sid) end

            local c162 = ui.Interfaces:GetComponent(162, sid)
            if c162 then processComponent(c162, 162, sid) end
        end)
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

    -- 3. Escáner rápido en Client Logic (cada 2 ticks, ~40ms)
    local logicCount = 0
    if Event.Logic then
        Event.Logic.Subscribe("rs_traductor_fast_scan", function()
            logicCount = logicCount + 1
            if logicCount % 2 == 0 then
                DialogueHook.ScanDialogueInterfaces()
            end
        end)
    end

    -- 4. Escáner de respaldo y carga progresiva en ServerLogic (cada tick del servidor, ~600ms)
    if Event.ServerLogic then
        Event.ServerLogic.Subscribe("rs_traductor_ticks", function()
            DialogueHook.ScanDialogueInterfaces()
            DialogueLoader.TickBackgroundLoad()
        end)
    end

    log(">>> [RS Traductor] Escáner ACTIVO (Antiflasheo habilitado).")
end

function DialogueHook.Shutdown()
    pcall(function() Event.ChatMessage.Unsubscribe("rs_traductor_chat") end)
    pcall(function() Event.Draw.Unsubscribe("rs_traductor_draw_instant") end)
    pcall(function() Event.Logic.Unsubscribe("rs_traductor_fast_scan") end)
    pcall(function() Event.ServerLogic.Unsubscribe("rs_traductor_ticks") end)
    lastCompText = {}
    log(">>> [RS Traductor] Gancho de diálogos apagado.")
end

return DialogueHook
