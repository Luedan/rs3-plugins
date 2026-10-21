--- ============================================================================
--- Plugin: RS Hekili
--- Asistente de Rotación de Combate en Tiempo Real para RuneScape (EoC)
--- ============================================================================

local PLUGIN_TAG = "rs-hekili"
log(">>> Iniciando RS Hekili v1.0.0...")

local Engine = require("src/engine")
local HUD = require("src/hud")
local UI = require("src/ui")
local ActionBar = require("src/actionbar")

-- 1. Inicializar el motor APL de rotación y la interfaz de configuración
Engine.Init()
UI.Init()

-- 2. Escaneo de las barras de acción para detectar teclas reales y estados
ActionBar.ScanAllBars()

-- Diagnóstico de recursos cargados
if Plugin and Plugin.resources then
    local count = 0
    for k, _ in pairs(Plugin.resources) do
        count = count + 1
    end
    log(string.format("Recursos detectados en Plugin.resources: %d elementos", count))
else
    log("Aviso: Plugin.resources aún no está indexado por el cliente.")
end

-- 3. Montar el HUD en el área de juego
local gameArea = ui.Interfaces:GetComponent(id.Component.TOPLEVEL_V2__GAME_AREA)
if gameArea then
    HUD.Create(gameArea)
else
    log("Aviso: GAME_AREA no estaba disponible de inmediato; se reintentará en el primer tick.")
end

-- 4. Bucle de actualización en cada tick del juego (ServerLogic)
local UPDATE_KEY = "rs_hekili_update"
Event.ServerLogic.Subscribe(UPDATE_KEY, function()
    if not gameArea then
        gameArea = ui.Interfaces:GetComponent(id.Component.TOPLEVEL_V2__GAME_AREA)
        if gameArea then
            HUD.Create(gameArea)
        end
    end

    HUD.Update()
end)

log(string.format(">>> RS Hekili activo! Magia Nvl %d detectada.", Engine.GetMagicLevel()))

--- ============================================================================
--- Ciclo de Vida: Invocado al recargar (prl) o apagar (poff)
--- ============================================================================
function PluginShutdown()
    log(">>> Apagando RS Hekili...")
    pcall(function() Event.ServerLogic.Unsubscribe(UPDATE_KEY) end)
    HUD.Destroy()
    UI.Shutdown()
    Engine.Shutdown()
    log(">>> RS Hekili apagado limpiamente.")
end
