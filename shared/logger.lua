---@class Logger
local Logger = {}

--- Crea un nuevo logger prefijado para un plugin específico.
---@param prefix string
---@return table
function Logger.new(prefix)
    local logObj = {}
    local tag = "[" .. tostring(prefix) .. "]"

    function logObj:info(...)
        print(tag, "[INFO]", ...)
    end

    function logObj:warn(...)
        print(tag, "[WARN]", ...)
    end

    function logObj:error(...)
        print(tag, "[ERROR]", ...)
    end

    function logObj:debug(...)
        print(tag, "[DEBUG]", ...)
    end

    return logObj
end

return Logger
