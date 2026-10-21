local UI = {}

local SETTINGS_KEY = "rs_traductor_settings"

--- Dibuja la ventana de configuración usando la API nativa de RuneScape
local function renderSettings(parent)
    if not parent then return end

    pcall(function()
        -- Título Principal
        local title = ui.Text.new(parent)
        title:SetPos(20, 20)
        title:SetSize(400, 25)
        title.content = "RS Traductor (Español)"
        title.colour = Vector4.new(1.0, 0.8, 0.2, 1.0)

        -- Descripción
        local desc = ui.Text.new(parent)
        desc:SetPos(20, 50)
        desc:SetSize(450, 40)
        desc.content = "Traducción offline de diálogos de NPCs y menú contextual.\nNombres de ítems, armas, NPCs y lugares en inglés original."
        desc.colour = Vector4.new(1.0, 1.0, 1.0, 1.0)

        -- Estado de la Base de Datos Local
        local dbStatus = ui.Text.new(parent)
        dbStatus:SetPos(20, 95)
        dbStatus:SetSize(450, 20)
        local pdbOk = (PersistentDB or (core and core.PersistentDB)) ~= nil
        dbStatus.content = string.format("Base de datos local (PersistentDB): %s", pdbOk and "ACTIVA" or "RAM")
        dbStatus.colour = Vector4.new(0.4, 1.0, 0.4, 1.0)

        -- Diccionarios cargados
        local dictStatus = ui.Text.new(parent)
        dictStatus:SetPos(20, 120)
        dictStatus:SetSize(450, 20)
        dictStatus.content = "Diálogos de NPCs: 3,350+ NPCs (Letras A-Z y #, 114,783 líneas)"
        dictStatus.colour = Vector4.new(0.3, 0.8, 1.0, 1.0)

        -- Información
        local info = ui.Text.new(parent)
        info:SetPos(20, 150)
        info:SetSize(450, 60)
        info.content = "Estado:\n* 100% Offline (Sin dependencia de HTTP, Cero Lag).\n* Al interactuar con cualquier NPC, sus diálogos y opciones se traducen automáticamente."
        info.colour = Vector4.new(0.8, 0.8, 0.8, 1.0)
    end)
end

function UI.Init()
    Event.SettingsLayerReady.Subscribe(SETTINGS_KEY, function(event)
        if event and event.component then
            renderSettings(event.component)
        end
    end)
end

function UI.Shutdown()
    pcall(function() Event.SettingsLayerReady.Unsubscribe(SETTINGS_KEY) end)
end

return UI
