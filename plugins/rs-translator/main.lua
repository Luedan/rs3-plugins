--- ============================================================================
--- Plugin: RS Traductor (ES)
--- Descripción: Traducción en tiempo real de diálogos, opciones, menú contextual
--- (clic derecho) y mensajes del juego sin traducir nombres de ítems ni NPCs.
--- ============================================================================

local PLUGIN_TAG = "rs-translator"
log("==================================================")
log(">>> [RS Traductor] Iniciando versión 1.0.0...")

-- Diagnóstico de entorno y APIs globales
pcall(function()
    local keys = {}
    for k, v in pairs(_G) do
        keys[#keys + 1] = tostring(k) .. ":" .. type(v)
    end
    table.sort(keys)
    local pdb = PersistentDB or (core and core.PersistentDB)
    if pdb and pdb.SetString then
        pdb:SetString("dbg_env", table.concat(keys, ";"))
    end
    if io and io.open then
        local f = io.open("D:/programacion/REPOS/rs-plugins/client_env_dump.txt", "w")
        if f then
            f:write("IO WORKS!\n" .. table.concat(keys, "\n"))
            f:close()
        end
    end
end)

local DialogueLoader = require("src/dialogue_loader")
local DialogueHook = require("src/dialogue_hook")
local MiniMenuHook = require("src/minimenu_hook")
local QuestHelperHook = require("src/quest_helper_hook")
local Translator = require("src/translator")
local UI = require("src/ui")

-- Inicializar subsistemas
DialogueLoader.Init()
DialogueHook.Init()
MiniMenuHook.Init()
QuestHelperHook.Init(Translator)
UI.Init()

-- Diagnóstico
local pdbAvailable = (PersistentDB or (core and core.PersistentDB)) ~= nil
log(string.format(">>> [RS Traductor] Base de Datos SQLite (PersistentDB): %s", tostring(pdbAvailable)))
log(">>> [RS Traductor] Plugin ACTIVO y listo para traducir.")
log("==================================================")

--- ============================================================================
--- Ciclo de Vida: Invocado al recargar (prl) o apagar (poff)
--- ============================================================================
function PluginShutdown()
    log(">>> Apagando RS Traductor...")
    UI.Shutdown()
    MiniMenuHook.Shutdown()
    DialogueHook.Shutdown()
    QuestHelperHook.Shutdown()
    log(">>> RS Traductor apagado limpiamente.")
end
