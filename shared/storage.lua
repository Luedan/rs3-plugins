---@class Storage
--- Envoltorio seguro para interactuar con PersistentDB con valores por defecto.
local Storage = {}

--- Crea un almacén persistente con prefijo de plugin.
---@param prefix string Prefijo para aislar claves (ej: "rs_test_")
---@return table
function Storage.new(prefix)
    local store = {
        prefix = prefix or "plugin_"
    }

    local function makeKey(key)
        return store.prefix .. key
    end

    --- Obtiene un booleano guardado o retorna el valor por defecto.
    ---@param key string
    ---@param defaultVal boolean
    ---@return boolean
    function store:GetBool(key, defaultVal)
        if not PersistentDB then return defaultVal end
        local ok, val = pcall(function() return PersistentDB:GetBool(makeKey(key)) end)
        if ok and val ~= nil then return val end
        return defaultVal
    end

    --- Guarda un valor booleano.
    ---@param key string
    ---@param val boolean
    function store:SetBool(key, val)
        if not PersistentDB then return false end
        return pcall(function() return PersistentDB:SetBool(makeKey(key), val) end)
    end

    --- Obtiene un entero guardado o retorna el valor por defecto.
    ---@param key string
    ---@param defaultVal integer
    ---@return integer
    function store:GetInt(key, defaultVal)
        if not PersistentDB then return defaultVal end
        local ok, val = pcall(function() return PersistentDB:GetInt(makeKey(key)) end)
        if ok and val ~= nil then return val end
        return defaultVal
    end

    --- Guarda un número entero.
    ---@param key string
    ---@param val integer
    function store:SetInt(key, val)
        if not PersistentDB then return false end
        return pcall(function() return PersistentDB:SetInt(makeKey(key), val) end)
    end

    --- Obtiene una cadena guardada o retorna el valor por defecto.
    ---@param key string
    ---@param defaultVal string
    ---@return string
    function store:GetString(key, defaultVal)
        if not PersistentDB then return defaultVal end
        local ok, val = pcall(function() return PersistentDB:GetString(makeKey(key)) end)
        if ok and val ~= nil then return val end
        return defaultVal
    end

    --- Guarda una cadena de texto.
    ---@param key string
    ---@param val string
    function store:SetString(key, val)
        if not PersistentDB then return false end
        return pcall(function() return PersistentDB:SetString(makeKey(key), val) end)
    end

    return store
end

return Storage
