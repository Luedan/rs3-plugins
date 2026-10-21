local Abilities = require("src/abilities")
local Settings = require("src/settings")

local ActionBar = {}

ActionBar.detectedBarId = 1430
ActionBar.slots = {}     -- slotIndex (1..14) -> { key = "1", compId = ... }
ActionBar.radials = {}   -- list of radial progress components

--- Mapeo de ranuras de la barra principal a habilidades mágicas por defecto
--- En tu barra actual (Barra 3):
--- Ranura 1: Sonic Wave (Tecla "1")
--- Ranura 3: Magic Basic Attack (Tecla "3")
local DEFAULT_SLOT_MAPPING = {
    [1] = "sonic_wave",
    [3] = "magic_basic"
}

--- Escanea las barras de acción activas (1430 a 1435) y extrae las teclas/letras exactas
function ActionBar.ScanAllBars()
    log("=== [ActionBar Scan] Escaneando barras de acción en busca de teclas y habilidades... ===")

    local foundBars = {}

    for barId = 1430, 1435 do
        local iface = nil
        pcall(function()
            if ui and ui.Interfaces then
                iface = ui.Interfaces:GetInterface(barId)
            end
        end)

        if iface then
            table.insert(foundBars, barId)
            ActionBar.ScanInterface(barId)
        end
    end

    if #foundBars == 0 then
        -- Intentar búsqueda mediante componentes directos
        ActionBar.ScanComponentsDirectly()
    end
end

--- Inspecciona la interfaz de la barra de acción y extrae las letras exactas de cada botón
function ActionBar.ScanInterface(interfaceId)
    local labelsFound = {}
    local radialsFound = {}

    local function inspectComponent(comp, staticId)
        if not comp then return end

        local compType = comp.type

        -- Si es una etiqueta de texto con la letra/número del atajo
        if compType == ui.ComponentType.LABEL and comp.content and #comp.content > 0 then
            table.insert(labelsFound, {
                staticId = staticId,
                text = comp.content,
                x = comp.x or 0,
                y = comp.y or 0
            })
        end

        -- Si es el overlay de enfriamiento (RadialProgressOverlay)
        if compType == ui.ComponentType.RADIAL_PROGRESS_OVERLAY then
            table.insert(radialsFound, {
                staticId = staticId,
                comp = comp,
                progress = comp.progress or 0
            })
        end

        -- Explorar componentes dinámicos dentro de la ranura
        pcall(function()
            if comp.IterateDynamicComponents then
                comp:IterateDynamicComponents(function(child, visible)
                    if child then
                        if child.type == ui.ComponentType.LABEL and child.content and #child.content > 0 then
                            table.insert(labelsFound, {
                                staticId = staticId,
                                text = child.content,
                                isDynamic = true
                            })
                        elseif child.type == ui.ComponentType.RADIAL_PROGRESS_OVERLAY then
                            table.insert(radialsFound, {
                                staticId = staticId,
                                comp = child,
                                progress = child.progress or 0,
                                isDynamic = true
                            })
                        end
                    end
                    return false
                end)
            end
        end)
    end

    for staticId = 0, 200 do
        local comp = nil
        pcall(function()
            comp = ui.Interfaces:GetComponent(interfaceId, staticId)
        end)
        if comp then
            inspectComponent(comp, staticId)
        end
    end

    if #labelsFound > 0 then
        local labelSummary = {}
        for _, l in ipairs(labelsFound) do
            table.insert(labelSummary, string.format("[%d]='%s'", l.staticId, l.text))
        end
        log(string.format("[ActionBar %d] Teclas detectadas en la barra: %s",
            interfaceId, table.concat(labelSummary, ", ")))
    end

    if #radialsFound > 0 then
        ActionBar.radials = radialsFound
        log(string.format("[ActionBar %d] %d temporizadores de enfriamiento vinculados.",
            interfaceId, #radialsFound))
    end
end

function ActionBar.ScanComponentsDirectly()
    if not id or not id.Component then return end
    pcall(function()
        for k, v in pairs(id.Component) do
            local lk = string.lower(k)
            if string.find(lk, "action") or string.find(lk, "bar") then
                local comp = ui.Interfaces:GetComponent(v)
                if comp then
                    log(string.format("[ActionBar Direct] %s = %s", k, tostring(v)))
                end
            end
        end
    end)
end

--- Comprueba si algún RadialProgressOverlay tiene un enfriamiento activo (> 0 y < 1)
function ActionBar.IsSlotOnCooldown(staticId)
    if not ActionBar.radials then return false end
    for _, r in ipairs(ActionBar.radials) do
        if r.staticId == staticId then
            local p = 0
            pcall(function() p = r.comp.progress or 0 end)
            if p > 0 and p < 1 then
                return true
            end
        end
    end
    return false
end

return ActionBar
