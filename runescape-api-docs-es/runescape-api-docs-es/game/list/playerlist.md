# PlayerList

## Descripción General

An `PlayerList` provides access to all active [PlayerEntities](../entity/playerentity.md) in the game world, as well as several methods to search for entities.

> **Información**
> All methods, except [PlayerList.Self()](#self) return an array of [PlayerEntities](../entity/playerentity.md).

See each method for examples on how to use this list.

## Funciones

### Self

```lua
function PlayerList.Self() -> PlayerEntity
```

Returns the [PlayerEntity](../entity/playerentity.md) belonging to the currently logged in player character.

| Retorna | Descripción |
| --- | --- |
| [PlayerEntity](../entity/playerentity.md) | A [PlayerEntity](../entity/playerentity.md). |

> **Ejemplo**
> ```lua
> local self = PlayerList.Self()
> -- Another way to get the logged in playerEntity
> local self2 = Player.GetEntity()
> -- self == self2
> ```

### All

```lua
function PlayerList.All() -> [ PlayerEntity ]
```

Returns all active [PlayerEntities](../entity/playerentity.md) in the game world in an array.

| Retorna | Descripción |
| --- | --- |
| [ [PlayerEntity](../entity/playerentity.md) ] | An array of [PlayerEntities](../entity/playerentity.md). |

> **Ejemplo**
> ```lua
> local allPlayers = PlayerList.All()
> for _,playerEntity in ipairs(allPlayers) do
>     if playerEntity.coordGrid == CoordGrid._0_50_50_32_32 then
>         -- found a player at a specific coord
>     end
> end
> ```

### ByUID

```lua
function PlayerList.ByUID(uid : Integer) -> [ PlayerEntity ]
```

Returns the [PlayerEntity](../entity/playerentity.md) with the matching UID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| uid | Integer | A valid UID value. |

| Retorna | Descripción |
| --- | --- |
| [ [PlayerEntity](../entity/playerentity.md) ] | An array of [PlayerEntities](../entity/playerentity.md). |

> **Ejemplo**
> ```lua
> -- A UID obtained elsewhere
> local targetPlayerUID = ...
> local found = PlayerList.ByUID(targetPlayerUID)
> if #found > 0 then
>     -- Player was found
>     local playerEntity = found[1]
>     -- playerEntity.uid == targetPlayerUID
> end
> ```

### ByName

```lua
function PlayerList.ByName(name : String) -> [ PlayerEntity ]
```

Returns any [PlayerEntity](../entity/playerentity.md) with a display name matching the given `name` value.

String matches are case-insensitive.
Matches are exact unless wildcard characters `?` and/or `*` are provided.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | The string to match against `PlayerEntity.displayName`. |

| Retorna | Descripción |
| --- | --- |
| [ [PlayerEntity](../entity/playerentity.md) ] | An array of [PlayerEntities](../entity/playerentity.md). |

> **Ejemplo**
> ```lua
> found = PlayerList.ByName("Durial321")
> if #found > 0 then
>     -- Run for your life!
> end
> ```

### ByDistance

```lua
function PlayerList.ByDistance(coordGrid : CoordGrid, range : Integer) -> [ PlayerEntity ]
```

Returns any [PlayerEntity](../entity/playerentity.md) within `range` tiles of the given `coordGrid` value.

Exact coord matches should use a value of `0` for `range`.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordGrid | [CoordGrid](../coordgrid.md) | The coord at which to centre the distance search. |
| range | Integer | The maximum tile distance from the given coord which an [PlayerEntity](../entity/playerentity.md) must be. |

| Retorna | Descripción |
| --- | --- |
| [ [PlayerEntity](../entity/playerentity.md) ] | An array of [PlayerEntities](../entity/playerentity.md). |

> **Ejemplo**
> ```lua
> found = PlayerList.ByDistance(CoordGrid._0_50_50_34_30, 4)
> if #found > 0 then
>     -- Found a player nearby the target coord
> end
> ```

### Filter

```lua
function PlayerList.Filter(filterSet : Table) -> [ PlayerEntity ]
```

Returns any [PlayerEntity](../entity/playerentity.md) that matches all tests in the `filterSet` table.

Available tests are:

| Key | Tipo | Descripción |
| --- | --- | --- |
| uid | Integer | A valid entity UID.`{ uid = playerEntity.uid }`See [PlayerList.ByUID()](#byuid) |
| name | String | A name to match against `PlayerEntity.displayName`.`{ name = "*GIM*" }`See [PlayerList.ByName()](#byname) |
| coordGrid | [CoordGrid](../coordgrid.md) | A coord to test entity distance from.If `range` is not provided, the default value of `range` will be `0`.`{ coordGrid = CoordGrid._0_50_50_32_32 }`See [PlayerList.ByDistance()](#bydistance) |
| range | Integer | Ignored if `coordGrid` key is not provided.`{ range = 4 }`See [PlayerList.ByDistance()](#bydistance) |
| func | Function | A function which returns a boolean, and which takes a [PlayerEntity](../entity/playerentity.md) as its only parameter.This function is called for every entity, and any call that returns `true` will include that [PlayerEntity](../entity/playerentity.md) in the return array.`function eastFacingFinder(playerEntity) { return playerEntity.facing == 90 }``{ func = eastFacingFinder }` |

Tests can be combined as shown below:

```text
-- Return all players within 10 tiles of 0_50_50_32_32 that have "GIM" in their display name
found = PlayerList.Filter( { name = "*GIM*", coordGrid = CoordGrid._0_50_50_32_32, range = 10 } )
```

> **Información**
> Tests are inclusive.
All must pass in order for the [PlayerEntity](../entity/playerentity.md) to be included in the return array.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| filterSet | Table | A table of key-value pairs which describe individual tests to perform. |

| Retorna | Descripción |
| --- | --- |
| [ [PlayerEntity](../entity/playerentity.md) ] | An array of [PlayerEntities](../entity/playerentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> -- Filter all Players for the display names that include "GIM"
> local foundByFilterName = PlayerList.Filter( { name = "*GIM*" } )
> 
> function westFacingFinder(player)
>     return player.facing == 270
> end
> 
> -- Filter all Players for those that pass the func 'westFacingFinder'
> local foundByFilterFunc = PlayerList.Filter( { func = westFacingFinder } )
> 
> -- Filter all Players for those within 2 tiles of 0_50_50_32_32
> local foundByFilterCoord = PlayerList.Filter( { coordGrid = CoordGrid._0_50_50_32_32, range = 2 } )
> 
> -- Filter all Players for those within 3 tiles of 0_50_50_9_10 with a display name that starts with "GIM"
> local foundByFilterCoordAndName = NPCList.Filter( { coordGrid = CoordGrid._0_50_50_9_10, range = 3, name = "GIM*" } )
> ```