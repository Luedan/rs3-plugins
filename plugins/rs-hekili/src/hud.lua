local Abilities = require("src/abilities")
local Engine = require("src/engine")
local Settings = require("src/settings")

local HUD = {}

local hudLayer = nil
local slots = {}

-- Configuración visual de las ranuras (Slot 1 grande, Slots 2 y 3 menores)
local SLOT_CONFIGS = {
    { size = 64, borderWidth = 2, borderColor = 0xFFD700FF, isNext = true },
    { size = 50, borderWidth = 1, borderColor = 0x64B5F6EE, isNext = false },
    { size = 42, borderWidth = 1, borderColor = 0x90A4AEEE, isNext = false },
}

local function colourToVec4(colour)
    local c = tonumber(colour) or 0xFFFFFFFF
    local r = (c >> 24) & 0xFF
    local g = (c >> 16) & 0xFF
    local b = (c >> 8) & 0xFF
    local a = c & 0xFF
    return Vector4.new(r / 255, g / 255, b / 255, a / 255)
end

--- Resuelve el recurso de imagen del icono con múltiples rutas y alias
local function getIconResource(iconFile)
    if not Plugin or not Plugin.resources then return nil end
    local res = Plugin.resources

    -- Alias comunes (ej: en la beta Magic Basic usa el mismo icono que antes se llamaba wrack)
    local checkFiles = { iconFile }
    if iconFile == "magic_basic" or iconFile == "magic" then
        table.insert(checkFiles, "magic_basic")
        table.insert(checkFiles, "magic")
        table.insert(checkFiles, "wrack")
    end

    for _, file in ipairs(checkFiles) do
        if res[file] then return res[file] end
        if res[file .. ".png"] then return res[file .. ".png"] end
        if res.icons then
            if res.icons[file] then return res.icons[file] end
            if res.icons[file .. ".png"] then return res.icons[file .. ".png"] end
        end
    end

    return nil
end

function HUD.Create(gameArea)
    if not gameArea then
        log("No se pudo obtener GAME_AREA para montar el HUD.")
        return false
    end

    if hudLayer then
        HUD.Destroy()
    end

    -- Obtener fuentes del motor
    local fontLarge = id and id.Font and id.Font.NOTO_SANS_13PT_BOLD_OUTLINE or 1
    local fontMedium = id and id.Font and id.Font.NOTO_SANS_11PT_BOLD_OUTLINE or 1

    -- Capa raíz posicionada en el MEDIO de la pantalla (50% X, 42% Y)
    local totalWidth = 64 + 10 + 50 + 10 + 42
    hudLayer = ui.Layer.new(gameArea)
    hudLayer:SetPos(Settings.data.posX, Settings.data.posY, 0.5, 0.42, -0.5, -0.5)
    hudLayer:SetSize(totalWidth, 80)

    slots = {}
    local currentX = 0

    for i = 1, #SLOT_CONFIGS do
        local cfg = SLOT_CONFIGS[i]
        local slotData = {}
        local yOffset = 64 - cfg.size -- Alinear por la parte inferior

        -- 1. Fondo oscuro
        slotData.bg = ui.Rectangle.new(hudLayer)
        slotData.bg:SetPos(currentX, yOffset)
        slotData.bg:SetSize(cfg.size, cfg.size)
        slotData.bg.colour = colourToVec4(0x0C121FEE)

        -- 2. Icono oficial de la habilidad (Sprite)
        slotData.iconSprite = ui.Sprite.new(hudLayer)
        slotData.iconSprite:SetPos(currentX + 2, yOffset + 2)
        slotData.iconSprite:SetSize(cfg.size - 4, cfg.size - 4)
        slotData.iconSprite.colour = colourToVec4(0xFFFFFFFF)

        -- 3. Texto alternativo con el nombre (en caso de que la imagen tarde en cargar)
        slotData.nameText = ui.Text.new(hudLayer)
        slotData.nameText:SetPos(currentX + 2, yOffset + (cfg.size / 2) - 8)
        slotData.nameText:SetSize(cfg.size - 4, 18)
        slotData.nameText.font = fontMedium
        slotData.nameText.colour = colourToVec4(0xFFFFFFFF)

        -- 4. Borde del recuadro
        slotData.border = ui.Rectangle.new(hudLayer)
        slotData.border:SetPos(currentX, yOffset)
        slotData.border:SetSize(cfg.size, cfg.size)
        slotData.border.colour = colourToVec4(cfg.borderColor)
        slotData.border.fill = false
        slotData.border.outlineThickness = -cfg.borderWidth

        -- 5. Placa de fondo para la tecla de atajo (esquina inferior derecha)
        local badgeW = 26
        local badgeH = 18
        slotData.keyBg = ui.Rectangle.new(hudLayer)
        slotData.keyBg:SetPos(currentX + cfg.size - badgeW, yOffset + cfg.size - badgeH)
        slotData.keyBg:SetSize(badgeW, badgeH)
        slotData.keyBg.colour = colourToVec4(0x000000EE)

        -- 6. Texto de la tecla asignada (con fuente oficial para que se vea claro)
        slotData.keyText = ui.Text.new(hudLayer)
        slotData.keyText:SetPos(currentX + cfg.size - badgeW + 2, yOffset + cfg.size - badgeH)
        slotData.keyText:SetSize(badgeW - 2, badgeH)
        slotData.keyText.font = fontLarge
        slotData.keyText.colour = colourToVec4(0xFFFF00FF) -- Amarillo brillante
        slotData.keyText.content = ""

        -- 7. Etiqueta "NEXT" sobre la ranura principal
        if cfg.isNext then
            slotData.nextBadge = ui.Text.new(hudLayer)
            slotData.nextBadge:SetPos(currentX, yOffset - 16)
            slotData.nextBadge:SetSize(cfg.size, 14)
            slotData.nextBadge.font = fontMedium
            slotData.nextBadge.colour = colourToVec4(0xFFD700FF)
            slotData.nextBadge.content = "NEXT"
        end

        -- Asegurar orden de renderizado
        slotData.iconSprite:MoveToFront()
        slotData.nameText:MoveToFront()
        slotData.border:MoveToFront()
        slotData.keyBg:MoveToFront()
        slotData.keyText:MoveToFront()
        if slotData.nextBadge then slotData.nextBadge:MoveToFront() end

        slots[i] = slotData
        currentX = currentX + cfg.size + 10
    end

    log("HUD de Hekili montado en pantalla [Centro X: 50%, Y: 42%].")
    return true
end

function HUD.Update()
    if not hudLayer then return end

    if Settings.data.hideOutOfCombat and not Engine.IsInCombat() then
        hudLayer.hidden = true
        return
    else
        hudLayer.hidden = false
    end

    local queue = Engine.CalculateQueue(#slots)

    for i = 1, #slots do
        local slot = slots[i]
        local ability = queue[i]

        if ability then
            -- Intentar asignar icono
            local iconRes = getIconResource(ability.iconFile)
            if iconRes then
                slot.iconSprite.sprite = iconRes
                slot.iconSprite.hidden = false
                slot.nameText.hidden = true
            else
                slot.iconSprite.hidden = true
                slot.nameText.content = ability.shortName or ability.name
                slot.nameText.hidden = false
            end

            -- Mostrar tecla de atajo
            local keybind = Settings.GetKeybind(ability.id)
            slot.keyText.content = keybind

            slot.bg.hidden = false
            slot.border.hidden = false
            slot.keyBg.hidden = false
            slot.keyText.hidden = false
            if slot.nextBadge then slot.nextBadge.hidden = false end
        else
            slot.bg.hidden = true
            slot.iconSprite.hidden = true
            slot.nameText.hidden = true
            slot.border.hidden = true
            slot.keyBg.hidden = true
            slot.keyText.hidden = true
            if slot.nextBadge then slot.nextBadge.hidden = true end
        end
    end
end

function HUD.Destroy()
    if hudLayer then
        pcall(function()
            hudLayer.hidden = true
        end)
        hudLayer = nil
        slots = {}
    end
end

return HUD
