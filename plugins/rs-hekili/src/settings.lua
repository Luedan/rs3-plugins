local Abilities = require("src/abilities")

local Settings = {}

-- Prefijo v4 para la migración limpia con la batería moderna de habilidades
local DB_PREFIX = "rs_hekili_v4_"

local function dbGet(key, defaultVal)
    if not PersistentDB then return defaultVal end
    local ok, val = pcall(function() return PersistentDB:Get(DB_PREFIX .. key) end)
    if ok and val ~= nil then return val end
    return defaultVal
end

local function dbSet(key, val)
    if not PersistentDB then return false end
    return pcall(function() return PersistentDB:Set(DB_PREFIX .. key, val) end)
end

-- Configuración por defecto basada en tu barra de acción actual:
-- Ranura 1: Sonic Wave (Tecla [1])
-- Ranura 3: Magic (Ataque Básico, Tecla [3])
local DEFAULT_ENABLED = {
    sonic_wave = true,
    magic_basic = true,
    concentrated_blast = false,
    dragon_breath = false,
    combust = false,
    chain = false,
    wild_magic = false,
    asphyxiate = false,
    omnipower = false,
    sunshine = false
}

Settings.data = {
    posX = dbGet("pos_x", 0),
    posY = dbGet("pos_y", -60),
    hideOutOfCombat = dbGet("hide_ooc", false),
    queueSize = dbGet("queue_size", 3),
    enabledAbilities = {},
    keybinds = {}
}

-- Inicializar estado y atajos
for id, ability in pairs(Abilities.List) do
    local defaultEnable = DEFAULT_ENABLED[id] or ability.enabledByDefault or false
    local savedEnabled = dbGet("enabled_" .. id, defaultEnable)
    Settings.data.enabledAbilities[id] = savedEnabled

    local savedKey = dbGet("key_" .. id, ability.defaultKey)
    Settings.data.keybinds[id] = savedKey
end

function Settings.IsAbilityEnabled(abilityId)
    if Settings.data.enabledAbilities[abilityId] ~= nil then
        return Settings.data.enabledAbilities[abilityId]
    end
    return DEFAULT_ENABLED[abilityId] or false
end

function Settings.SetAbilityEnabled(abilityId, isEnabled)
    Settings.data.enabledAbilities[abilityId] = isEnabled
    dbSet("enabled_" .. abilityId, isEnabled)
end

function Settings.GetKeybind(abilityId)
    return Settings.data.keybinds[abilityId] or "?"
end

function Settings.SetKeybind(abilityId, keyText)
    Settings.data.keybinds[abilityId] = keyText
    dbSet("key_" .. abilityId, keyText)
end

function Settings.SetPosition(x, y)
    Settings.data.posX = x
    Settings.data.posY = y
    dbSet("pos_x", x)
    dbSet("pos_y", y)
end

function Settings.SetHideOutOfCombat(enable)
    Settings.data.hideOutOfCombat = enable
    dbSet("hide_ooc", enable)
end

return Settings
