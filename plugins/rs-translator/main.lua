--- ============================================================================
--- Plugin: RS Traductor (ES)
--- Descripción: Traducción en tiempo real de diálogos, opciones, menú contextual
--- (clic derecho) y mensajes del juego sin traducir nombres de ítems ni NPCs.
--- ============================================================================

local PLUGIN_TAG = "rs-translator"
log("==================================================")
log(">>> [RS Traductor] Iniciando versión 1.0.0...")

local DialogueLoader = require("src/dialogue_loader")
local DialogueHook = require("src/dialogue_hook")
local MiniMenuHook = require("src/minimenu_hook")
local UI = require("src/ui")

-- Inicializar subsistemas
DialogueLoader.Init()
DialogueHook.Init()
MiniMenuHook.Init()
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
    log(">>> RS Traductor apagado limpiamente.")
end
