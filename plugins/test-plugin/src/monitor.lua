local Config = require("src/config")

local Monitor = {}

local EVENT_KEY = "rs_test_plugin_tick"
local tickCount = 0

Monitor.CurrentData = {
    available = false,
    name = "Desconectado",
    combatLevel = 0,
    runEnergy = 0,
    coordText = "N/A",
    tickCount = 0
}

function Monitor.Init()
    tickCount = 0

    -- Event.ServerLogic se dispara en cada tick del servidor (~600ms)
    Event.ServerLogic.Subscribe(EVENT_KEY, function()
        tickCount = tickCount + 1
        Monitor.CurrentData.tickCount = tickCount

        if not Player.IsAvailable() then
            Monitor.CurrentData.available = false
            return
        end

        Monitor.CurrentData.available = true

        -- Leer información dinámica del jugador
        local playerEntity = Player.GetEntity()
        if playerEntity and playerEntity.isValid then
            Monitor.CurrentData.name = playerEntity.displayName or "Jugador"
            local coords = playerEntity.coordGrid
            if coords then
                local cx = coords.x or 0
                local cz = coords.z or coords.y or 0
                local cl = coords.level or coords.plane or 0
                Monitor.CurrentData.coordText = string.format("[%d, %d, piso %d]", cx, cz, cl)
            end
        end

        Monitor.CurrentData.combatLevel = Player.GetCombatLevel() or 0
        Monitor.CurrentData.runEnergy = Player.GetRunEnergy() or 0

        -- Alerta de energía baja si está configurada
        if Config.Settings.lowEnergyAlert and Monitor.CurrentData.runEnergy > 0 and Monitor.CurrentData.runEnergy < 20 then
            -- Solo advertir cada ~50 ticks para no saturar la consola
            if tickCount % 50 == 0 then
                log(string.format("¡Atención! Energía de correr baja (%d%%)", Monitor.CurrentData.runEnergy))
            end
        end

        -- Registro opcional de ticks
        if Config.Settings.logTicks and tickCount % 10 == 0 then
            log(string.format("Tick #%d | %s | HP/Stats activos", tickCount, Monitor.CurrentData.name))
        end
    end)

    log("Monitor de eventos iniciado correctamente (ServerLogic).")
end

function Monitor.Shutdown()
    pcall(function()
        Event.ServerLogic.Unsubscribe(EVENT_KEY)
    end)
    log("Monitor de eventos detenido.")
end

return Monitor
