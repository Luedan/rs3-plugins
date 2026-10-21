local DialogueLoader = require("src/dialogue_loader")

local MiniMenuHook = {}

-- Diccionario maestro de verbos de interacción del segundo clic (clic derecho)
local VERB_TRANSLATIONS = {
    -- Interacciones con NPCs
    ["Talk-to"] = "Hablar con",
    ["Talk to"] = "Hablar con",
    ["Talk"] = "Hablar con",
    ["Examine"] = "Examinar",
    ["Attack"] = "Atacar",
    ["Trade"] = "Comerciar con",
    ["Trade with"] = "Comerciar con",
    ["Pickpocket"] = "Robar a",
    ["Bank"] = "Banco",
    ["Collect"] = "Recoger de",
    ["Claim"] = "Reclamar de",
    ["Reward"] = "Recompensa de",
    ["Follow"] = "Seguir a",
    ["Lookup"] = "Consultar",
    ["Report"] = "Reportar",
    ["Add friend"] = "Añadir amigo",
    ["Add ignore"] = "Añadir ignorado",

    -- Navegación y entorno
    ["Walk here"] = "Caminar aquí",
    ["Cancel"] = "Cancelar",
    ["Search"] = "Registrar",
    ["Open"] = "Abrir",
    ["Close"] = "Cerrar",
    ["Climb-up"] = "Subir por",
    ["Climb-down"] = "Bajar por",
    ["Climb"] = "Escalar",
    ["Cross"] = "Cruzar",
    ["Jump"] = "Saltar",
    ["Enter"] = "Entrar a",
    ["Leave"] = "Salir de",
    ["Pass-through"] = "Atravesar",
    ["Pass through"] = "Atravesar",
    ["Pray-at"] = "Rezar en",
    ["Pray at"] = "Rezar en",
    ["Recharge"] = "Recargar en",
    ["Recharge at"] = "Recargar en",
    ["Quick-teleport"] = "Teletransporte rápido",
    ["Teleport to"] = "Teletransportarse a",

    -- Habilidades y recursos
    ["Chop down"] = "Talar",
    ["Chop"] = "Talar",
    ["Mine"] = "Minar",
    ["Prospect"] = "Inspeccionar",
    ["Fish"] = "Pescar",
    ["Bait"] = "Pescar con cebo",
    ["Net"] = "Pescar con red",
    ["Cage"] = "Pescar con jaula",
    ["Harpoon"] = "Pescar con arpón",
    ["Catch"] = "Atrapar",
    ["Cook"] = "Cocinar",
    ["Light"] = "Encender",
    ["Burn"] = "Quemar",
    ["Craft"] = "Fabricar",
    ["Smelt"] = "Fundir",
    ["Smith"] = "Forjar",
    ["Fletch"] = "Hacer flechas",
    ["String"] = "Encordar",
    ["Loot"] = "Saquear",
    ["Pick"] = "Recoger",

    -- Inventario y equipo
    ["Take"] = "Tomar",
    ["Drop"] = "Tirar",
    ["Destroy"] = "Destruir",
    ["Wield"] = "Empuñar",
    ["Wear"] = "Vestir",
    ["Equip"] = "Equipar",
    ["Remove"] = "Quitar",
    ["Eat"] = "Comer",
    ["Drink"] = "Beber",
    ["Use"] = "Usar",
    ["Check"] = "Revisar",
    ["Inspect"] = "Inspeccionar",
    ["Read"] = "Leer",
    ["Cast"] = "Lanzar",
    ["Teleport"] = "Teletransportar",
    ["Activate"] = "Activar",
    ["Deactivate"] = "Desactivar",
    ["Configure"] = "Configurar",
    ["Rub"] = "Frotar",
    ["Store"] = "Guardar",
    ["Withdraw"] = "Retirar",
    ["Deposit"] = "Depositar",
    ["Empty"] = "Vaciar",
    ["Fill"] = "Llenar",
    ["Buy"] = "Comprar",
    ["Sell"] = "Vender"
}

--- Limpia códigos de color y formato
local function cleanTag(str)
    if not str then return "" end
    str = string.gsub(str, "<col=[%x]+>", "")
    str = string.gsub(str, "</col>", "")
    str = string.gsub(str, "<shad=[%x]+>", "")
    str = string.gsub(str, "</shad>", "")
    local trimmed = string.match(str, "^%s*(.-)%s*$")
    return trimmed or str
end

--- Traduce una entrada individual del menú del segundo clic manteniendo intacto el nombre
local function translateEntry(entry)
    if not entry then return end

    -- Si ya fue sobreescrita por nosotros, ignorar
    if entry.overrideText and #entry.overrideText > 0 then
        return
    end

    local verb = entry.verbText
    local transVerb = nil

    if verb and #verb > 0 then
        local cVerb = cleanTag(verb)
        transVerb = VERB_TRANSLATIONS[cVerb]

        if not transVerb then
            for eng, es in pairs(VERB_TRANSLATIONS) do
                if string.find(cVerb, "^" .. eng .. "$") or string.find(cVerb, eng, 1, true) then
                    transVerb = string.gsub(cVerb, eng, es)
                    break
                end
            end
        end
    end

    -- Si no pudimos por verbText, intentar analizando fullText directamente
    if not transVerb and entry.fullText and #entry.fullText > 0 then
        local cFull = cleanTag(entry.fullText)
        for eng, es in pairs(VERB_TRANSLATIONS) do
            if string.find(cFull, "^" .. eng .. "%s+") then
                local subject = string.sub(cFull, #eng + 2)
                entry.overrideText = es .. " " .. subject
                return
            elseif cFull == eng then
                entry.overrideText = es
                return
            end
        end
    end

    if transVerb then
        local subject = entry.subjectText or ""
        local extra = entry.extraText or ""

        if #subject > 0 then
            if #extra > 0 then
                entry.overrideText = string.format("%s %s %s", transVerb, subject, extra)
            else
                entry.overrideText = string.format("%s %s", transVerb, subject)
            end
        else
            if #extra > 0 then
                entry.overrideText = string.format("%s %s", transVerb, extra)
            else
                entry.overrideText = transVerb
            end
        end
    end
end

local function checkAndRecordNPC(entry)
    if not entry then return end
    local verb = cleanTag(entry.verbText or "")
    local subject = cleanTag(entry.subjectText or "")

    if (verb == "Talk-to" or verb == "Talk to" or verb == "Talk" or string.find(verb, "Talk")) and #subject > 0 then
        DialogueLoader.SetActiveNPC(subject)
    elseif entry.actionEntryType and MiniMenuEntryType and entry.actionEntryType == MiniMenuEntryType.NPC then
        if #subject > 0 then
            DialogueLoader.SetActiveNPC(subject)
        end
    end
end

function MiniMenuHook.Init()
    -- 1. Cuando se añade una entrada individual al menú
    if Event.MiniMenuEntryAdded then
        Event.MiniMenuEntryAdded.Subscribe("rs_traductor_minimenu_add", function(event)
            if event and event.entry then
                translateEntry(event.entry)
                checkAndRecordNPC(event.entry)
            end
        end)
    end

    -- 2. Cuando el menú de clic derecho está listo y completo para mostrarse
    if Event.MiniMenuReady then
        Event.MiniMenuReady.Subscribe("rs_traductor_minimenu_ready", function(event)
            if not event or not event.miniMenu then return end
            local entries = event.miniMenu.entries
            if entries then
                for _, entry in ipairs(entries) do
                    translateEntry(entry)
                end
            end
        end)
    end

    -- 3. Cuando el jugador selecciona una opción del menú (o clic directo)
    if Event.MiniMenuEntrySelected then
        Event.MiniMenuEntrySelected.Subscribe("rs_traductor_minimenu_select", function(event)
            if event and event.entry then
                checkAndRecordNPC(event.entry)
            end
        end)
    end

    log(">>> [RS Traductor] Gancho de Menú de Clic Derecho (MiniMenu) ACTIVADO.")
end

function MiniMenuHook.Shutdown()
    pcall(function() Event.MiniMenuEntryAdded.Unsubscribe("rs_traductor_minimenu_add") end)
    pcall(function() Event.MiniMenuReady.Unsubscribe("rs_traductor_minimenu_ready") end)
    pcall(function() Event.MiniMenuEntrySelected.Unsubscribe("rs_traductor_minimenu_select") end)
end

return MiniMenuHook
