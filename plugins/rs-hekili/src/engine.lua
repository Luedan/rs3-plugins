local Abilities = require("src/abilities")
local Settings = require("src/settings")
local ActionBar = require("src/actionbar")

local Engine = {}

local cooldowns = {}        -- abilityId -> ticksRestantes
local stunTicksRemaining = 0
local targetInCombat = false
local currentMagicLevel = 1
local currentAdrenaline = 0 -- 0 a 100
local gcdTicks = 0          -- Global Cooldown (3 ticks = 1.8s)

local function queryPlayerMagicLevel()
    if not Player or not Player.IsAvailable or not Player.IsAvailable() then
        return 1
    end
    local level = nil
    pcall(function()
        if SkillType and SkillType.MAGIC then
            level = Player.GetLevelGameplay(SkillType.MAGIC)
        end
    end)
    if not level then
        pcall(function() level = Player.GetLevelGameplay(6) end)
    end
    if not level then
        pcall(function() level = Player.GetLevelUncapped(6) end)
    end
    return level or 1
end

--- Comprueba si una habilidad puede ser lanzada según nivel, cooldown y adrenalina
local function canCast(id, simCds)
    local ab = Abilities.List[id]
    if not ab then return false end
    if not Settings.IsAbilityEnabled(id) then return false end
    if currentMagicLevel < ab.level then return false end
    if (simCds[id] or 0) > 0 then return false end
    if ab.type == "threshold" and currentAdrenaline < (ab.adrenalineReq or 50) then return false end
    if ab.type == "ultimate" and currentAdrenaline < (ab.adrenalineReq or 100) then return false end
    return true
end

--- Registra la ejecución real de una habilidad en combate y aplica su cooldown
function Engine.OnAbilityFired(abilityId)
    local ab = Abilities.List[abilityId]
    if not ab then return end

    if ab.cooldownTicks and ab.cooldownTicks > 0 then
        cooldowns[abilityId] = ab.cooldownTicks
    end
    gcdTicks = 3 -- 1 GCD (1.8s)

    if ab.stuns then
        stunTicksRemaining = ab.stunDurationTicks or 3
    end

    log(string.format("[Hekili] Habilidad TIRADA: %s (Tecla [%s]). CD: %d ticks",
        ab.name, Settings.GetKeybind(abilityId), ab.cooldownTicks or 0))
end

function Engine.Init()
    cooldowns = {}
    stunTicksRemaining = 0
    targetInCombat = false
    gcdTicks = 0
    currentMagicLevel = queryPlayerMagicLevel()

    -- 1. Bucle de Ticks del Servidor (~600ms)
    Event.ServerLogic.Subscribe("rs_hekili_ticks", function()
        -- Actualizar nivel
        local lvl = queryPlayerMagicLevel()
        if lvl and lvl > 0 then currentMagicLevel = lvl end

        -- Decrementar cooldowns activos
        for id, ticks in pairs(cooldowns) do
            if ticks > 0 then
                cooldowns[id] = ticks - 1
            else
                cooldowns[id] = 0
            end
        end

        -- Decrementar GCD y aturdimientos
        if gcdTicks > 0 then gcdTicks = gcdTicks - 1 end
        if stunTicksRemaining > 0 then stunTicksRemaining = stunTicksRemaining - 1 end

        -- Comprobar si el objetivo está en combate
        if var and var.VarClient and var.VarClient["COMBATV2_TARGET_SIDE_PANEL_HEALTH"] then
            local hp = var.VarClient["COMBATV2_TARGET_SIDE_PANEL_HEALTH"].value or 0
            targetInCombat = (hp > 0)
        else
            targetInCombat = true
        end

        -- 2. SIMULACIÓN DE REVOLUTION / COMBATE EN TIEMPO REAL:
        -- Cuando el GCD llega a 0 en combate, el juego lanza la siguiente habilidad lista
        if targetInCombat and gcdTicks <= 0 then
            local nextToFire = nil

            -- Prioridad 1: Definitivas / Umbrales si hay adrenalina
            if canCast("sunshine", cooldowns) then
                nextToFire = "sunshine"
            elseif canCast("omnipower", cooldowns) then
                nextToFire = "omnipower"
            elseif canCast("wild_magic", cooldowns) then
                nextToFire = "wild_magic"
            elseif canCast("asphyxiate", cooldowns) then
                nextToFire = "asphyxiate"
            -- Prioridad 2: Dragon Breath (Nvl 18+)
            elseif canCast("dragon_breath", cooldowns) then
                nextToFire = "dragon_breath"
            -- Prioridad 3: Combust (Nvl 34+)
            elseif canCast("combust", cooldowns) then
                nextToFire = "combust"
            -- Prioridad 4: Sonic Wave (Nvl 12+, Ranura 1)
            elseif canCast("sonic_wave", cooldowns) then
                nextToFire = "sonic_wave"
            -- Prioridad 5: Magic Basic Attack (Ranura 3, relleno sin cooldown)
            elseif canCast("magic_basic", cooldowns) then
                nextToFire = "magic_basic"
            end

            if nextToFire then
                Engine.OnAbilityFired(nextToFire)
            end
        end
    end)

    -- 2. Escuchar variables transmitidas para sincronizar lanzamientos
    if Event.VarTransmit then
        Event.VarTransmit.Subscribe("rs_hekili_vars", function(event)
            if not event or not event.var then return end
            local configName = event.var.configName or ""

            if string.find(configName, "SONIC") and event.newValue ~= event.oldValue then
                Engine.OnAbilityFired("sonic_wave")
            elseif string.find(configName, "DRAGON") and event.newValue ~= event.oldValue then
                Engine.OnAbilityFired("dragon_breath")
            elseif string.find(configName, "COMBUST") and event.newValue ~= event.oldValue then
                Engine.OnAbilityFired("combust")
            end
        end)
    end

    log(string.format("Motor APL Hekili iniciado. Nivel Magia: %d", currentMagicLevel))
end

function Engine.GetMagicLevel()
    return currentMagicLevel
end

function Engine.IsInCombat()
    return targetInCombat
end

function Engine.IsAvailable(abilityId)
    return canCast(abilityId, cooldowns)
end

--- Calcula la cola de próximas habilidades recomendadas (1..maxCount)
function Engine.CalculateQueue(maxCount)
    maxCount = maxCount or 3
    local queue = {}

    local simCds = {}
    for k, v in pairs(cooldowns) do
        simCds[k] = v
    end

    for step = 1, maxCount do
        local chosen = nil

        -- REGLA 1: Definitivas
        if canCast("sunshine", simCds) then
            chosen = Abilities.List.sunshine
        elseif not chosen and canCast("omnipower", simCds) then
            chosen = Abilities.List.omnipower
        end

        -- REGLA 2: Umbrales
        if not chosen and canCast("wild_magic", simCds) then
            chosen = Abilities.List.wild_magic
        elseif not chosen and canCast("asphyxiate", simCds) then
            chosen = Abilities.List.asphyxiate
        end

        -- REGLA 3: Dragon Breath (Nvl 18+)
        if not chosen and canCast("dragon_breath", simCds) then
            chosen = Abilities.List.dragon_breath
        end

        -- REGLA 4: Combust (Nvl 34+)
        if not chosen and canCast("combust", simCds) then
            chosen = Abilities.List.combust
        end

        -- REGLA 5: Sonic Wave (Nvl 12+, Tecla [1])
        if not chosen and canCast("sonic_wave", simCds) then
            chosen = Abilities.List.sonic_wave
        end

        -- REGLA 6: Concentrated Blast (Dual Wield)
        if not chosen and canCast("concentrated_blast", simCds) then
            chosen = Abilities.List.concentrated_blast
        end

        -- REGLA 7: Chain (Nvl 45+)
        if not chosen and canCast("chain", simCds) then
            chosen = Abilities.List.chain
        end

        -- REGLA 8: Magic - Ataque Básico (Relleno continuo, Tecla [3])
        if not chosen and canCast("magic_basic", simCds) then
            chosen = Abilities.List.magic_basic
        end

        if chosen then
            table.insert(queue, chosen)
            -- Avanzar cooldown en la simulación
            simCds[chosen.id] = chosen.cooldownTicks or 0
            -- Avanzar 1 GCD (3 ticks)
            for k, cd in pairs(simCds) do
                simCds[k] = math.max(0, cd - 3)
            end
        else
            break
        end
    end

    return queue
end

function Engine.Shutdown()
    pcall(function() Event.ServerLogic.Unsubscribe("rs_hekili_ticks") end)
    pcall(function() Event.VarTransmit.Unsubscribe("rs_hekili_vars") end)
end

return Engine
