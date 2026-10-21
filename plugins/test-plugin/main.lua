--- ============================================================================
--- Plugin: RS Test Plugin
--- Descripción: Plugin de prueba para validar eventos, datos del jugador, UI y persistencia.
--- ============================================================================

local PLUGIN_TAG = "test-plugin"
log(">>> Iniciando RS Test Plugin v1.0.0...")

local Config = require("src/config")
local Monitor = require("src/monitor")
local UI = require("src/ui")

-- Inicializar subsistemas
Monitor.Init()
UI.Init()

log(string.format("RS Test Plugin listo. Clics previos en BD: %d", Config.Settings.testClicks))

--- ============================================================================
--- CICLO DE VIDA (Llamado por el cliente de RuneScape al recargar o apagar)
--- ============================================================================
function PluginShutdown()
    log(">>> Apagando RS Test Plugin...")
    UI.Shutdown()
    Monitor.Shutdown()
    log(">>> RS Test Plugin finalizado correctamente.")
end
