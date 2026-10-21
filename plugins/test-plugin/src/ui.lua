local Config = require("src/config")
local Monitor = require("src/monitor")

local UI = {}

local CONTENT_EVENT_KEY = "test_plugin_content_ready"
local SETTINGS_EVENT_KEY = "test_plugin_settings_ready"

local contentView = nil
local settingsView = nil
local statusTextComponent = nil
local counterTextComponent = nil

--- Renderiza la capa de contenido (Ventana Flotante del Listón / Ribbon)
local function renderContentLayer(parent)
    if contentView then
        pcall(function() contentView:Destroy() end)
        contentView = nil
    end

    if prettyui and prettyui.SimpleView then
        contentView = prettyui.SimpleView.new(parent, {
            width = parent.width,
            height = parent.height
        })

        contentView:AddTitle("RS Test Plugin")
        contentView:AddText("Estado del Entorno y API:")

        -- Estado de conexión y jugador
        local playerInfo = "Desconectado del juego"
        if Monitor.CurrentData.available then
            playerInfo = string.format("Jugador: %s | Nivel: %d | Run: %d%%",
                tostring(Monitor.CurrentData.name or "Jugador"),
                tonumber(Monitor.CurrentData.combatLevel) or 0,
                tonumber(Monitor.CurrentData.runEnergy) or 0)
        end
        statusTextComponent = contentView:AddText(playerInfo)
        contentView:AddText(string.format("Coordenadas: %s", tostring(Monitor.CurrentData.coordText or "N/A")))

        contentView:AddDivider()

        -- Contador persistente
        contentView:AddTitle("Prueba de Persistencia (PersistentDB)")
        counterTextComponent = contentView:AddText(string.format("Clics acumulados: %d", Config.Settings.testClicks))

        if contentView.AddSimpleButton then
            contentView:AddSimpleButton({
                text = "+1 Clic (Guardar en Disco)",
                onClick = function()
                    local nuevoTotal = Config.IncrementClicks()
                    if counterTextComponent and counterTextComponent.SetContent then
                        counterTextComponent:SetContent(string.format("Clics acumulados: %d", nuevoTotal))
                    elseif counterTextComponent and counterTextComponent.content then
                        counterTextComponent.content = string.format("Clics acumulados: %d", nuevoTotal)
                    end
                    log(string.format("Contador incrementado a: %d", nuevoTotal))
                end
            })
        end

        contentView:AddDivider()
        contentView:AddText("Abre 'Plugin Hub > Manage' para acceder a los ajustes.")
    else
        -- Fallback nativo utilizando componentes base ui.*
        local label = ui.Text.new(parent)
        label.content = "RS Test Plugin activo. (prettyui no detectado)"
        label:SetSize(parent.width, 30)
    end
end

--- Renderiza la capa de ajustes (Plugin Hub > Manage > RS Test Plugin)
local function renderSettingsLayer(parent)
    if settingsView then
        pcall(function() settingsView:Destroy() end)
        settingsView = nil
    end

    if prettyui and prettyui.SimpleView then
        settingsView = prettyui.SimpleView.new(parent, {
            width = parent.width,
            height = parent.height
        })

        settingsView:AddTitle("Configuración de RS Test Plugin")
        settingsView:AddText("Ajusta los parámetros del plugin:")

        if settingsView.AddCheckboxButton then
            settingsView:AddCheckboxButton({
                {
                    text = "Registrar ticks periódicos en consola",
                    value = "log_ticks",
                    selected = Config.Settings.logTicks
                },
                {
                    text = "Avisar en consola cuando energía sea < 20%",
                    value = "low_energy_alert",
                    selected = Config.Settings.lowEnergyAlert
                }
            }, {
                onChange = function(_, _, key, isSelected)
                    if key == "log_ticks" then
                        Config.SetLogTicks(isSelected)
                        log("Ajuste 'log_ticks' cambiado a: " .. tostring(isSelected))
                    elseif key == "low_energy_alert" then
                        Config.SetLowEnergyAlert(isSelected)
                        log("Ajuste 'low_energy_alert' cambiado a: " .. tostring(isSelected))
                    end
                end
            })
        end

        settingsView:AddDivider()
        settingsView:AddText("Los ajustes se guardan automáticamente con PersistentDB.")
    end
end

function UI.Init()
    -- Suscribirse al evento del icono del Ribbon
    Event.ContentLayerReady.Subscribe(CONTENT_EVENT_KEY, function(event)
        if event and event.component then
            renderContentLayer(event.component)
        end
    end)

    -- Suscribirse al evento de los ajustes en el Plugin Hub
    Event.SettingsLayerReady.Subscribe(SETTINGS_EVENT_KEY, function(event)
        if event and event.component then
            renderSettingsLayer(event.component)
        end
    end)

    log("Vistas de interfaz (UI) registradas con éxito.")
end

function UI.Shutdown()
    pcall(function() Event.ContentLayerReady.Unsubscribe(CONTENT_EVENT_KEY) end)
    pcall(function() Event.SettingsLayerReady.Unsubscribe(SETTINGS_EVENT_KEY) end)

    if contentView then
        pcall(function() contentView:Destroy() end)
        contentView = nil
    end

    if settingsView then
        pcall(function() settingsView:Destroy() end)
        settingsView = nil
    end

    log("Vistas de interfaz (UI) liberadas.")
end

return UI
