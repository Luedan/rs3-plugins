# Player

## Descripción General

The Player table contains functions which provide data belonging to the currently logged in Player Character.

This data includes:

* Skills Levels & XP
* Run Energy
* Self Player Entity

## Ejemplos

```lua
-- The % of run energy remaining
local runEnergy = Player.GetRunEnergy()

-- The current gameplay level of a Skill (including bonuses and penalties)
local levelAttack = Player.GetLevelGameplay(SkillType.Attack)

-- The XP of a Skill, capped by a Free/Members world check
local cappedXPMagic = Player.GetXPCapped(SkillType.Magic)
```

## Enumeraciones

### SkillType

An enum for all Skills in the game.

| Name | Value |
| --- | --- |
| ATTACK | 0 |
| DEFENCE | 1 |
| STRENGTH | 2 |
| HITPOINTS | 3 |
| RANGED | 4 |
| PRAYER | 5 |
| MAGIC | 6 |
| COOKING | 7 |
| WOODCUTTING | 8 |
| FLETCHING | 9 |
| FISHING | 10 |
| FIREMAKING | 11 |
| CRAFTING | 12 |
| SMITHING | 13 |
| MINING | 14 |
| HERBLORE | 15 |
| AGILITY | 16 |
| THIEVING | 17 |
| SLAYER | 18 |
| FARMING | 19 |
| RUNECRAFTING | 20 |
| HUNTER | 21 |
| CONSTRUCTION | 22 |
| SUMMONING | 23 |
| DUNGEONEERING | 24 |
| DIVINATION | 25 |
| INVENTION | 26 |
| ARCHAEOLOGY | 27 |
| NECROMANCY | 28 |

## Funciones

### IsAvailable

```lua
function Player.IsAvailable() -> Boolean
```

Returns whether a Player Character is logged in and exists in a game world.

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether Player data is available to access. |

> **Ejemplo**
> ```lua
> if Player.IsAvailable() then
>     local attackLevel = Player.GetLevelGameplay(SkillType.ATTACK)
> end
> ```

### GetTrackingID

```lua
function Player.GetTrackingID() -> Long?
```

Returns a unique 64-bit tracking value for the Player Character.

> **Advertencia**
> This value is available to a plugin only if it has requested and been granted the [trackingAccess](../core/plugin.md#pluginpermissions) permission.

> **Información**
> This value is transmitted to the client on login, and several seconds may pass before it becomes available.
The function will return `nil` if the value is unavailable, or permission has not been granted.

| Retorna | Descripción |
| --- | --- |
| Long? | The 64-bit tracking value.Returns `nil` if unavailable due to login transmission delay, or missing permissions. |

> **Ejemplo**
> ```lua
> local trackingID = Player.GetTrackingID()
> if trackingID ~= nil then
>     -- Make use of the value
> end
> ```

### GetLevelGameplay

```lua
function Player.GetLevelGameplay(skill : SkillType) -> Integer
```

Devuelve el/la level for the given skill actual.
This includes all skill bonuses and penalties.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| skill | [SkillType](#skilltype) | The skill to return the gameplay level for. |

| Retorna | Descripción |
| --- | --- |
| Integer | The current gameplay level of the given skill. |

> **Ejemplo**
> ```lua
> if Player.GetLevelGameplay(SkillType.MAGIC) < Player.GetLevelCapped(SkillType.MAGIC) then
>     -- Player has a Magic debuff
> end
> ```

### GetLevelCapped

```lua
function Player.GetLevelCapped(skill : SkillType) -> Integer
```

Devuelve el/la level for the given skill based on XP actual.
This level is additionally capped by any Free/Member world limits on skill levels.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| skill | [SkillType](#skilltype) | The skill to return the capped level for. |

| Retorna | Descripción |
| --- | --- |
| Integer | The current capped level of the given skill. |

> **Ejemplo**
> ```lua
> if Player.GetLevelGameplay(SkillType.MAGIC) < Player.GetLevelCapped(SkillType.MAGIC) then
>     -- Player has a Magic debuff
> end
> ```

### GetLevelUncapped

```lua
function Player.GetLevelUncapped(skill : SkillType) -> Integer
```

Devuelve el/la level for the given skill based on XP actual.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| skill | [SkillType](#skilltype) | The skill to return the level for. |

| Retorna | Descripción |
| --- | --- |
| Integer | The current level of the given skill. |

> **Ejemplo**
> ```lua
> -- While on a Free world
> local gameplayLevel = Player.GetLevelGameplay(SkillType.AGILITY)
> local freeWorldLevel = Player.GetLevelCapped(SkillType.AGILITY)
> local actualLevel = Player.GetLevelUncapped(SkillType.AGILITY)
> ```

### GetXPCapped

```lua
function Player.GetXPCapped(skill : SkillType) -> Integer
```

Devuelve el/la XP for the given skill actual.
This XP value is additionally capped by any Free/Member world limits on skill levels.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| skill | [SkillType](#skilltype) | The skill to return the capped XP for. |

| Retorna | Descripción |
| --- | --- |
| Integer | The current capped XP of the given skill. |

> **Ejemplo**
> ```lua
> -- While on a Free world
> local freeWorldXP = Player.GetXPCapped(SkillType.AGILITY)
> local actualXP = Player.GetXPUncapped(SkillType.AGILITY)
> ```

### GetXPUncapped

```lua
function Player.GetXPUncapped(skill : SkillType) -> Integer
```

Devuelve el/la XP for the given skill actual.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| skill | [SkillType](#skilltype) | The skill to return the XP for. |

| Retorna | Descripción |
| --- | --- |
| Integer | The current XP of the given skill. |

> **Ejemplo**
> ```lua
> -- While on a Free world
> local freeWorldXP = Player.GetXPCapped(SkillType.AGILITY)
> local actualXP = Player.GetXPUncapped(SkillType.AGILITY)
> ```

### GetRunEnergy

```lua
function Player.GetRunEnergy() -> Integer
```

Devuelve el/la run energy for the Player Character actual.
This value is a percentage.

| Retorna | Descripción |
| --- | --- |
| Integer | The current run energy. |

> **Ejemplo**
> ```lua
> local runEnergy = Player.GetRunEnergy()
> if runEnergy < 20 then
>     -- could do with a rest
> end
> ```

### GetWeight

```lua
function Player.GetWeight() -> Integer
```

Devuelve el/la weight of the Player Character actual.
This value is in kilograms.

| Retorna | Descripción |
| --- | --- |
| Integer | The current weight. |

> **Ejemplo**
> ```lua
> local weight = Player.GetWeight()
> ```

### GetCombatLevel

```lua
function Player.GetCombatLevel() -> Integer
```

Devuelve el/la combat level of the Player Character actual.

| Retorna | Descripción |
| --- | --- |
| Integer | The current combat level. |

> **Ejemplo**
> ```lua
> local combatLevel = Player.GetCombatLevel()
> ```

### GetEntity

```lua
function Player.GetEntity() -> PlayerEntity
```

Returns the [PlayerEntity](entity/playerentity.md) belonging to the currently logged in Player Character.

| Retorna | Descripción |
| --- | --- |
| [PlayerEntity](entity/playerentity.md) | A [PlayerEntity](entity/playerentity.md). |

> **Ejemplo**
> ```lua
> local self = Player.GetEntity()
> -- Another way to get the logged in playerEntity
> local self2 = PlayerList.Self()
> -- self == self2
> ```