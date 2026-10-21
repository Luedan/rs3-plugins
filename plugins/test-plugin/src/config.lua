local Config = {}

local DB_PREFIX = "test_plugin_"

--- Obtiene un valor booleano persistente con valor por defecto
function Config.GetBool(key, defaultVal)
    if not PersistentDB then return defaultVal end
    local ok, val = pcall(function() return PersistentDB:GetBool(DB_PREFIX .. key) end)
    if ok and val ~= nil then return val end
    return defaultVal
end

--- Guarda un valor booleano persistente
function Config.SetBool(key, value)
    if not PersistentDB then return false end
    return pcall(function() return PersistentDB:SetBool(DB_PREFIX .. key, value) end)
end

--- Obtiene un entero persistente con valor por defecto
function Config.GetInt(key, defaultVal)
    if not PersistentDB then return defaultVal end
    local ok, val = pcall(function() return PersistentDB:GetInt(DB_PREFIX .. key) end)
    if ok and val ~= nil then return val end
    return defaultVal
end

--- Guarda un entero persistente
function Config.SetInt(key, value)
    if not PersistentDB then return false end
    return pcall(function() return PersistentDB:SetInt(DB_PREFIX .. key, value) end)
end

--- Opciones por defecto del plugin de prueba
Config.Settings = {
    logTicks = Config.GetBool("log_ticks", false),
    lowEnergyAlert = Config.GetBool("low_energy_alert", true),
    testClicks = Config.GetInt("test_clicks", 0)
}

function Config.IncrementClicks()
    Config.Settings.testClicks = Config.Settings.testClicks + 1
    Config.SetInt("test_clicks", Config.Settings.testClicks)
    return Config.Settings.testClicks
end

function Config.SetLogTicks(enable)
    Config.Settings.logTicks = enable
    Config.SetBool("log_ticks", enable)
end

function Config.SetLowEnergyAlert(enable)
    Config.Settings.lowEnergyAlert = enable
    Config.SetBool("low_energy_alert", enable)
end

return Config
