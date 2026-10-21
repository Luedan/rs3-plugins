local Abilities = {}

--- Batería completa de habilidades mágicas de RuneScape 3 (Modern Combat Beta)
Abilities.List = {
    magic_basic = {
        id = "magic_basic",
        name = "Magic",
        shortName = "MAGIC",
        level = 1,
        type = "basic_attack",
        cooldownTicks = 0,      -- Ataque básico sin cooldown (activado automáticamente)
        adrenalineGain = 9,     -- Genera 9% de adrenalina
        description = "Ataque Básico: 90%-110% daño mágico. Genera 9% Adrenalina.",
        color = 0x00E5FFFF,
        bgColour = 0x0D2B45EE,
        defaultKey = "3",       -- Ranura 3 en tu barra de poderes
        iconFile = "magic_basic",
        enabledByDefault = true,
    },
    sonic_wave = {
        id = "sonic_wave",
        name = "Sonic Wave",
        shortName = "SONIC",
        level = 12,
        type = "basic",
        weaponReq = "2h",       -- Requiere bastón de 2 manos (el que tienes equipado)
        cooldownTicks = 8,      -- 5 segundos (~8 ticks)
        adrenalineGain = 8,
        description = "Básico (2H Staff): Daño 100% y reduce el coste de adrenalina de la siguiente habilidad.",
        color = 0x1E88E5FF,
        bgColour = 0x003B46EE,
        defaultKey = "1",       -- Ranura 1 en tu barra
        iconFile = "sonic_wave",
        enabledByDefault = true,
    },
    concentrated_blast = {
        id = "concentrated_blast",
        name = "Concentrated Blast",
        shortName = "C-BLAST",
        level = 12,
        type = "basic",
        weaponReq = "dual",     -- Requiere Varita + Orbe (Dual Wield). Bloqueada con bastón 2H
        cooldownTicks = 8,
        adrenalineGain = 8,
        description = "Básico (Dual Wield): Requiere Varita + Orbe. Bloqueada si usas bastón 2H.",
        color = 0x7E57C2FF,
        bgColour = 0x2B1A4DEE,
        defaultKey = "2",       -- Ranura 2 en tu barra
        iconFile = "concentrated_blast",
        enabledByDefault = false,
    },
    dragon_breath = {
        id = "dragon_breath",
        name = "Dragon Breath",
        shortName = "D-BREATH",
        level = 18,
        type = "basic",
        cooldownTicks = 17,     -- 10 segundos (~17 ticks)
        adrenalineGain = 8,
        description = "Básico: Fuego en cono AoE de gran impacto. (¡Se desbloquea a nivel 18!)",
        color = 0xFF5722FF,
        bgColour = 0x4D1A0DEE,
        defaultKey = "4",       -- Ranura 4 en tu barra
        iconFile = "dragon_breath",
        enabledByDefault = false,
    },
    combust = {
        id = "combust",
        name = "Combust",
        shortName = "COMBUST",
        level = 34,
        type = "basic",
        cooldownTicks = 25,     -- 15 segundos
        adrenalineGain = 8,
        description = "Básico DoT: Sangrado continuo por 6s (doble si el objetivo camina).",
        color = 0xFFB300FF,
        bgColour = 0x4D3600EE,
        defaultKey = "5",
        iconFile = "combust",
        enabledByDefault = false,
    },
    chain = {
        id = "chain",
        name = "Chain",
        shortName = "CHAIN",
        level = 45,
        type = "basic",
        cooldownTicks = 17,
        adrenalineGain = 8,
        description = "Básico AoE: Golpea y encadena relámpagos a 2 enemigos cercanos.",
        color = 0x26C6DAFF,
        bgColour = 0x0A373DEE,
        defaultKey = "6",
        iconFile = "chain",
        enabledByDefault = false,
    },
    wild_magic = {
        id = "wild_magic",
        name = "Wild Magic",
        shortName = "W-MAGIC",
        level = 55,
        type = "threshold",
        cooldownTicks = 33,     -- 20 segundos
        adrenalineReq = 50,
        adrenalineCost = 15,
        description = "Umbral: 2 impactos devastadores de magia pura.",
        color = 0xEC407AFF,
        bgColour = 0x4D0D2DEE,
        defaultKey = "E",
        iconFile = "wild_magic",
        enabledByDefault = false,
    },
    asphyxiate = {
        id = "asphyxiate",
        name = "Asphyxiate",
        shortName = "ASPHYX",
        level = 65,
        type = "threshold",
        cooldownTicks = 33,     -- 20 segundos
        adrenalineReq = 50,
        adrenalineCost = 15,
        stuns = true,
        stunDurationTicks = 6,
        description = "Umbral: Canaliza 4 golpes fuertes y aturde.",
        color = 0x9C27B0FF,
        bgColour = 0x3E1B4DEE,
        defaultKey = "Q",
        iconFile = "asphyxiate",
        enabledByDefault = false,
    },
    omnipower = {
        id = "omnipower",
        name = "Omnipower",
        shortName = "OMNI",
        level = 66,
        type = "ultimate",
        cooldownTicks = 50,     -- 30 segundos
        adrenalineReq = 100,
        adrenalineCost = 100,
        description = "Definitiva: Disparo monumental de daño de todos los elementos.",
        color = 0xFFD700FF,
        bgColour = 0x4D3F00EE,
        defaultKey = "R",
        iconFile = "omnipower",
        enabledByDefault = false,
    },
    sunshine = {
        id = "sunshine",
        name = "Sunshine",
        shortName = "SUNSHINE",
        level = 85,
        type = "ultimate",
        cooldownTicks = 100,    -- 60 segundos
        adrenalineReq = 100,
        adrenalineCost = 100,
        description = "Definitiva: Área ardiente que incrementa todo tu daño mágico un 50%.",
        color = 0xFFEB3BFF,
        bgColour = 0x554400EE,
        defaultKey = "F",
        iconFile = "sunshine",
        enabledByDefault = false,
    }
}

--- Orden de prioridad para la toma de decisiones APL
Abilities.PriorityOrder = {
    "sunshine",             -- Definitiva máxima
    "omnipower",            -- Definitiva de burst
    "wild_magic",           -- Umbral principal
    "asphyxiate",           -- Umbral con aturdimiento
    "dragon_breath",        -- Básico fuerte AoE
    "combust",              -- Básico DoT
    "sonic_wave",           -- Básico constructor (2H)
    "concentrated_blast",   -- Básico constructor (Dual Wield)
    "chain",                -- Básico AoE
    "magic_basic",          -- Ataque básico / Relleno continuo (Tecla [3])
}

return Abilities
