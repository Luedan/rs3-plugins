local Abilities = require("src/abilities")
local Engine = require("src/engine")
local Settings = require("src/settings")

local UI = {}

local CONTENT_KEY = "rs_hekili_content"
local SETTINGS_KEY = "rs_hekili_settings"

local contentView = nil
local settingsView = nil

local function renderContent(parent)
    if contentView then
        pcall(function() contentView:Destroy() end)
        contentView = nil
    end

    if prettyui and prettyui.SimpleView then
        contentView = prettyui.SimpleView.new(parent, {
            width = parent.width,
            height = parent.height
        })

        contentView:AddTitle("RS Hekili - Asistente de Rotación")
        contentView:AddText(string.format("Nivel de Magia detectado: %d", Engine.GetMagicLevel()))
        contentView:AddDivider()

        contentView:AddTitle("Habilidades en tu Rotación Activa:")
        for _, id in ipairs(Abilities.PriorityOrder) do
            local ab = Abilities.List[id]
            if ab then
                local isEnabled = Settings.IsAbilityEnabled(id)
                local hasLevel = Engine.GetMagicLevel() >= ab.level
                local status = ""

                if isEnabled and hasLevel then
                    status = string.format("[EN ROTACIÓN] %s (Nvl %d) -> Tecla: [%s]", ab.name, ab.level, Settings.GetKeybind(ab.id))
                elseif isEnabled and not hasLevel then
                    status = string.format("[REQUIERE NIVEL] %s (Requiere Nivel %d)", ab.name, ab.level)
                else
                    status = string.format("[DESACTIVADA] %s (Tecla [%s])", ab.name, Settings.GetKeybind(ab.id))
                end
                contentView:AddText(status)
            end
        end

        contentView:AddDivider()
        contentView:AddText("El HUD muestra qué presionar según las habilidades que tengas en tu barra.")
        contentView:AddText("Activa o desactiva poderes en la pestaña 'Settings' del plugin.")
    end
end

local function renderSettings(parent)
    if settingsView then
        pcall(function() settingsView:Destroy() end)
        settingsView = nil
    end

    if prettyui and prettyui.SimpleView then
        settingsView = prettyui.SimpleView.new(parent, {
            width = parent.width,
            height = parent.height
        })

        settingsView:AddTitle("Configuración de RS Hekili")
        settingsView:AddText("Marca únicamente las habilidades que tienes colocadas en tu barra de poderes:")
        settingsView:AddDivider()

        -- Construir lista de checkboxes para cada habilidad
        local abilityOptions = {}
        for _, id in ipairs(Abilities.PriorityOrder) do
            local ab = Abilities.List[id]
            if ab then
                table.insert(abilityOptions, {
                    text = string.format("%s (Tecla [%s]) - Requiere Nvl %d", ab.name, Settings.GetKeybind(id), ab.level),
                    value = id,
                    selected = Settings.IsAbilityEnabled(id)
                })
            end
        end

        if settingsView.AddCheckboxButton then
            settingsView:AddCheckboxButton(abilityOptions, {
                onChange = function(_, _, abilityId, isSelected)
                    Settings.SetAbilityEnabled(abilityId, isSelected)
                    log(string.format("[RS Hekili] Habilidad '%s' cambiada a: %s", abilityId, tostring(isSelected)))
                end
            })

            settingsView:AddDivider()
            settingsView:AddCheckboxButton({
                {
                    text = "Ocultar HUD cuando estés fuera de combate",
                    value = "hide_ooc",
                    selected = Settings.data.hideOutOfCombat
                }
            }, {
                onChange = function(_, _, key, isSelected)
                    if key == "hide_ooc" then
                        Settings.SetHideOutOfCombat(isSelected)
                        log("[RS Hekili] Ocultar fuera de combate: " .. tostring(isSelected))
                    end
                end
            })
        end
    end
end

function UI.Init()
    Event.ContentLayerReady.Subscribe(CONTENT_KEY, function(event)
        if event and event.component then
            renderContent(event.component)
        end
    end)

    Event.SettingsLayerReady.Subscribe(SETTINGS_KEY, function(event)
        if event and event.component then
            renderSettings(event.component)
        end
    end)
end

function UI.Shutdown()
    pcall(function() Event.ContentLayerReady.Unsubscribe(CONTENT_KEY) end)
    pcall(function() Event.SettingsLayerReady.Unsubscribe(SETTINGS_KEY) end)

    if contentView then
        pcall(function() contentView:Destroy() end)
        contentView = nil
    end
    if settingsView then
        pcall(function() settingsView:Destroy() end)
        settingsView = nil
    end
end

return UI
