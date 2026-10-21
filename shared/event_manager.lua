---@class EventManager
--- Administrador centralizado de eventos para registrar y limpiar suscripciones fácilmente.
local EventManager = {}

--- Crea una nueva instancia del gestor de eventos para un plugin.
---@param pluginTag string Identificador único del plugin (ej: "test-plugin")
---@return table
function EventManager.new(pluginTag)
    local manager = {
        pluginTag = pluginTag,
        subscriptions = {} -- Lista de { channel = Event.X, key = string, eventName = string }
    }

    --- Suscribe una función a un canal de eventos de forma segura.
    ---@param eventChannel table Canal de Event (ej: Event.PlayerTick)
    ---@param eventName string Nombre identificativo del evento
    ---@param callback fun(event: any) Función que recibe el payload
    function manager:Subscribe(eventChannel, eventName, callback)
        local key = string.format("%s_%s", self.pluginTag, eventName)
        
        local success, err = pcall(function()
            eventChannel.Subscribe(key, function(eventData)
                local ok, runErr = pcall(callback, eventData)
                if not ok then
                    print(string.format("[%s] ERROR en evento '%s': %s", self.pluginTag, eventName, tostring(runErr)))
                end
            end)
        end)

        if success then
            table.insert(self.subscriptions, {
                channel = eventChannel,
                key = key,
                name = eventName
            })
        else
            print(string.format("[%s] Error al suscribirse a '%s': %s", self.pluginTag, eventName, tostring(err)))
        end
    end

    --- Cancela todas las suscripciones registradas. Llamar en PluginShutdown().
    function manager:UnsubscribeAll()
        for _, sub in ipairs(self.subscriptions) do
            pcall(function()
                sub.channel.Unsubscribe(sub.key)
            end)
        end
        self.subscriptions = {}
    end

    return manager
end

return EventManager
