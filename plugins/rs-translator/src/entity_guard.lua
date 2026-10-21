local EntityGuard = {}

-- Palabras comunes al inicio de una oración en inglés que NO son entidades
local SENTENCE_STARTERS = {
    ["The"] = true, ["A"] = true, ["An"] = true, ["You"] = true,
    ["Your"] = true, ["I"] = true, ["My"] = true, ["We"] = true,
    ["Our"] = true, ["He"] = true, ["His"] = true, ["She"] = true,
    ["Her"] = true, ["They"] = true, ["Their"] = true, ["It"] = true,
    ["Its"] = true, ["This"] = true, ["That"] = true, ["These"] = true,
    ["Those"] = true, ["There"] = true, ["Here"] = true, ["What"] = true,
    ["Where"] = true, ["When"] = true, ["Why"] = true, ["How"] = true,
    ["Who"] = true, ["Which"] = true, ["If"] = true, ["As"] = true,
    ["Do"] = true, ["Does"] = true, ["Did"] = true, ["Are"] = true,
    ["Is"] = true, ["Was"] = true, ["Were"] = true, ["Have"] = true,
    ["Has"] = true, ["Had"] = true, ["Can"] = true, ["Could"] = true,
    ["Would"] = true, ["Should"] = true, ["May"] = true, ["Might"] = true,
    ["Must"] = true, ["Please"] = true, ["Hello"] = true, ["Greetings"] = true,
    ["Yes"] = true, ["No"] = true, ["Well"] = true, ["Now"] = true,
    ["Welcome"] = true, ["Thank"] = true, ["Thanks"] = true
}

-- Prefijos característicos de ítems y materiales de RuneScape
local RS_ITEM_PREFIXES = {
    "Bronze", "Iron", "Steel", "Mithril", "Adamant", "Rune", "Dragon",
    "Orikalkum", "Necronium", "Bane", "Elder Rune", "Abyssal", "Armadyl",
    "Bandos", "Saradomin", "Zamorak", "Zaros", "Seren", "Sliske",
    "Fractured", "Noxious", "Shadow", "Cryptbloom", "Tectonic", "Sirenic",
    "Malevolent", "First Necromancer", "Ghostly", "Death lotus", "Seasinger"
}

--- Extrae y protege nombres propios, ítems, armas, lugares y personajes con tokens
function EntityGuard.Protect(text)
    if not text or #text == 0 then return text, {} end

    local entities = {}
    local counter = 0

    local function addEntity(match)
        table.insert(entities, match)
        local token = string.format("__E%d__", counter)
        counter = counter + 1
        return token
    end

    local masked = text

    -- 1. Proteger frases compuestas con "of" (ej: "Fractured Staff of Armadyl", "Eye of Newt", "Shield of Arrav")
    masked = string.gsub(masked, "([%u][%w'%-_]+%s+of%s+[%u][%w'%-_]+)", function(m)
        return addEntity(m)
    end)
    masked = string.gsub(masked, "([%u][%w'%-_]+%s+of%s+the%s+[%u][%w'%-_]+)", function(m)
        return addEntity(m)
    end)

    -- 2. Proteger secuencias de dos o tres palabras capitalizadas (ej: "Duke Horacio", "Lumbridge Sage", "Grand Exchange")
    masked = string.gsub(masked, "(%s)([%u][%w'%-_]+%s+[%u][%w'%-_]+%s+[%u][%w'%-_]+)", function(space, m)
        return space .. addEntity(m)
    end)
    masked = string.gsub(masked, "(%s)([%u][%w'%-_]+%s+[%u][%w'%-_]+)", function(space, m)
        return space .. addEntity(m)
    end)

    -- 3. Proteger palabras capitalizadas individuales dentro de la oración (no al principio de la frase)
    masked = string.gsub(masked, "(%s)([%u][%w'%-_]+)", function(space, word)
        if not SENTENCE_STARTERS[word] then
            return space .. addEntity(word)
        end
        return space .. word
    end)

    -- 4. Proteger ítems con prefijos conocidos de RuneScape aunque estén en minúsculas
    for _, prefix in ipairs(RS_ITEM_PREFIXES) do
        local pat = "(%f[%a]" .. prefix .. "%s+[%a]+%f[%A])"
        masked = string.gsub(masked, pat, function(m)
            return addEntity(m)
        end)
    end

    return masked, entities
end

--- Restaura los nombres originales en inglés en las posiciones de los tokens
function EntityGuard.Restore(maskedText, entities)
    if not maskedText or not entities or #entities == 0 then
        return maskedText
    end

    local restored = maskedText
    for i, orig in ipairs(entities) do
        local token = string.format("__E%d__", i - 1)
        restored = string.gsub(restored, token, orig)
    end

    return restored
end

return EntityGuard
