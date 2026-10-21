# ObjStackList

## Descripción General

An `ObjStackList` provides access to all active [ObjStackEntities](../entity/objstackentity.md) in the game world, as well as several methods to search for entities.

> **Información**
> All methods return an array of [ObjStackEntities](../entity/objstackentity.md).

See each method for examples on how to use this list.

## Funciones

### All

```lua
function ObjStackList.All() -> [ ObjStackEntity ]
```

Returns all active [ObjStackEntities](../entity/objstackentity.md) in the game world in an array.

| Retorna | Descripción |
| --- | --- |
| [ [ObjStackEntity](../entity/objstackentity.md) ] | An array of [ObjStackEntities](../entity/objstackentity.md). |

> **Ejemplo**
> ```lua
> local allObjStacks = ObjStackList.All()
> for _,objStackEntity in ipairs(allObjStacks) do
>     if objStackEntity:HasObj(config.Obj.LOGS) then
>         -- found some logs
>     end
> end
> ```

### ByName

```lua
function ObjStackList.ByName(name : String) -> [ ObjStackEntity ]
```

Returns any [ObjStackEntity](../entity/objstackentity.md) which contains an [ObjEntry](../entity/objstackentity.md#objentry) with a display name matching the given `name` value.

String matches are case-insensitive.
Matches are exact unless wildcard characters `?` and/or `*` are provided.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | The string to match against `ObjType.name`. |

| Retorna | Descripción |
| --- | --- |
| [ [ObjStackEntity](../entity/objstackentity.md) ] | An array of [ObjStackEntities](../entity/objstackentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = ObjStackList.ByName("*logs*")
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 2,50,50,5,24)
> --      1: Logs (count: 1, configID: 1511)
> --  2: (stackSize: 1, coordGrid: 2,50,50,5,26)
> --      1: Logs (count: 1, configID: 1511)
> --  3: (stackSize: 1, coordGrid: 2,50,50,8,25)
> --      1: Logs (count: 1, configID: 1511)
> --  4: (stackSize: 1, coordGrid: 2,50,50,9,24)
> --      1: Logs (count: 1, configID: 1511)
> 
> found = ObjStackCList.ByName("mind rune")
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 0,50,50,6,8)
> --      1: Mind rune (count: 1, configID: 558)
> 
> found = ObjStackList.ByName("rune")
> -- Returns these entities:
> --  Empty
> 
> found = ObjStackList.ByName("*rune")
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 0,50,50,6,8)
> --      1: Mind rune (count: 1, configID: 558)
> ```

### ByDistance

```lua
function ObjStackList.ByDistance(coordGrid : CoordGrid, range : Integer) -> [ ObjStackEntity ]
```

Returns any [ObjStackEntity](../entity/objstackentity.md) within `range` tiles of the given `coordGrid` value.

Exact coord matches should use a value of `0` for `range`.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordGrid | [CoordGrid](../coordgrid.md) | The coord at which to centre the distance search. |
| range | Integer | The maximum tile distance from the given coord which an [ObjStackEntity](../entity/objstackentity.md) must be. |

| Retorna | Descripción |
| --- | --- |
| [ [ObjStackEntity](../entity/objstackentity.md) ] | An array of [ObjStackEntities](../entity/objstackentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = ObjStackList.ByDistance(CoordGrid._0_50_50_10_10, 6)
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 0,50,50,5,12)
> --      1: Knife (count: 1, configID: 946)
> --  2: (stackSize: 1, coordGrid: 0,50,50,6,8)
> --      1: Mind rune (count: 1, configID: 558)
> --  3: (stackSize: 1, coordGrid: 0,50,50,8,14)
> --      1: Bowl (count: 1, configID: 1923)
> --  4: (stackSize: 1, coordGrid: 0,50,50,9,14)
> --      1: Empty pot (count: 1, configID: 1931)
> --  5: (stackSize: 1, coordGrid: 0,50,50,11,12)
> --      1: Jug (count: 1, configID: 1935)
> ```

### ByConfig

```lua
function ObjStackList.ByConfig(objType : ObjType) -> [ ObjStackEntity ]
```

Returns any [ObjStackEntity](../entity/objstackentity.md) that contains a [ObjEntry](../entity/objstackentity.md#objentry) referencing the given [ObjType](../config/objtype.md) config.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| objType | [ObjType](../config/objtype.md) | The config to look for when testing [ObjStackEntities](../entity/objstackentity.md). |

| Retorna | Descripción |
| --- | --- |
| [ [ObjStackEntity](../entity/objstackentity.md) ] | An array of [ObjStackEntities](../entity/objstackentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = ObjStackList.ByConfig(config.Obj.BOWL_EMPTY)
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 0,50,50,8,14)
> --      1: Bowl (count: 1, configID: 1923)
> ```

### ByConfigID

```lua
function ObjStackList.ByConfigID(objTypeID : Integer) -> [ ObjStackEntity ]
```

Returns any [ObjStackEntity](../entity/objstackentity.md) that contains a [ObjEntry](../entity/objstackentity.md#objentry) referencing the given [ObjType](../config/objtype.md) config ID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| objTypeID | Integer | The config ID to look for when testing [ObjStackEntities](../entity/objstackentity.md). |

| Retorna | Descripción |
| --- | --- |
| [ [ObjStackEntity](../entity/objstackentity.md) ] | An array of [ObjStackEntities](../entity/objstackentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = ObjStackList.ByConfigID(id.Obj.BOWL_EMPTY)
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 0,50,50,8,14)
> --      1: Bowl (count: 1, configID: 1923)
> ```

### Filter

```lua
function ObjStackList.Filter(filterSet : Table) -> [ ObjStackEntity ]
```

Returns any [ObjStackEntity](../entity/objstackentity.md) that matches all tests in the `filterSet` table.

Available tests are:

| Key | Tipo | Descripción |
| --- | --- | --- |
| name | String | A name to match against `ObjType.name`.`{ name = "*logs*" }`See [ObjStackList.ByName()](#byname) |
| coordGrid | [CoordGrid](../coordgrid.md) | A coord to test entity distance from.If `range` is not provided, the default value of `range` will be `0`.`{ coordGrid = CoordGrid._0_50_50_32_32 }`See [ObjStackList.ByDistance()](#bydistance) |
| range | Integer | Ignored if `coordGrid` key is not provided.`{ range = 4 }`See [ObjStackList.ByDistance()](#bydistance) |
| config | [ObjType](../config/objtype.md) | The config to match against entries of `ObjEntry.config`.`{ config = config.Obj.LOGS }`See [ObjStackList.ByConfig()](#byconfig) |
| configID | Integer | The config ID to match against entries of `ObjEntry.configID`.`{ configID = id.Obj.LOGS }`See [ObjStackList.ByConfigID()](#byconfigid) |
| func | Function | A function which returns a boolean, and which takes an [ObjStackEntity](../entity/objstackentity.md) as its only parameter.This function is called for every entity, and any call that returns `true` will include that [ObjStackEntity](../entity/objstackentity.md) in the return array.`function logFinder(objStackEntity) { return objStackEntity:HasObj(config.Obj.LOGS) }``{ func = logFinder }` |

Tests can be combined as shown below:

```text
-- Return all objStacks containing logs within 3 tiles of 0_50_50_4_24
found = ObjStackList.Filter({ config = config.Obj.LOGS, coordGrid = CoordGrid._0_50_50_4_24, range = 3 })
```

> **Información**
> Tests are inclusive.
All must pass in order for the [ObjStackEntity](../entity/objstackentity.md) to be included in the return array.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| filterSet | Table | A table of key-value pairs which describe individual tests to perform. |

| Retorna | Descripción |
| --- | --- |
| [ [ObjStackEntity](../entity/objstackentity.md) ] | An array of [ObjStackEntities](../entity/objstackentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> -- Filter all objStacks for config ID
> local foundByFilterConfigID = ObjStackList.Filter({ configID = id.Obj.LOGS })
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 2,50,50,5,24)
> --      1: Logs (count: 1, configID: 1511)
> --  2: (stackSize: 1, coordGrid: 2,50,50,5,26)
> --      1: Logs (count: 1, configID: 1511)
> --  3: (stackSize: 1, coordGrid: 2,50,50,8,25)
> --      1: Logs (count: 1, configID: 1511)
> --  4: (stackSize: 1, coordGrid: 2,50,50,9,24)
> --      1: Logs (count: 1, configID: 1511)
> 
> 
> 
> -- Filter all objStacks for a specific config
> local foundByFilterConfig = ObjStackList.Filter({ config = config.Obj.LOGS })
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 2,50,50,5,24)
> --      1: Logs (count: 1, configID: 1511)
> ...
> --  4: (stackSize: 1, coordGrid: 2,50,50,9,24)
> --      1: Logs (count: 1, configID: 1511)
> 
> -- Filter all objStacks for the exact display name "logs"
> local foundByFilterName = ObjStackList.Filter({ name = "logs" })
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 2,50,50,5,24)
> --      1: Logs (count: 1, configID: 1511)
> ...
> --  4: (stackSize: 1, coordGrid: 2,50,50,9,24)
> --      1: Logs (count: 1, configID: 1511)
> 
> function filterLogsObj(objStack)
>     return objStack:HasObjID(id.Obj.LOGS)
> end
> 
> -- Filter all objStacks for those that pass the func 'filterLogsObj'
> local foundByFilterFunc = ObjStackList.Filter({ func = filterLogsObj })
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 2,50,50,5,24)
> --      1: Logs (count: 1, configID: 1511)
> ...
> --  4: (stackSize: 1, coordGrid: 2,50,50,9,24)
> --      1: Logs (count: 1, configID: 1511)
> 
> -- Filter all objStacks for those within 10 tiles of 0_50_50_32_32
> local foundByFilterCoord = ObjStackList.Filter({ coordGrid = CoordGrid._0_50_50_32_32, range = 10 })
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 2,50,50,29,23)
> --      1: Bronze pickaxe (count: 1, configID: 1265)
> 
> -- Filter all objStacks for those of config type LOGS within 3 tiles of 0_50_50_4_24
> local foundByFilterConfigAndCoord = ObjStackList.Filter({ coordGrid = CoordGrid._0_50_50_4_24, range = 3, config = config.Obj.LOGS })
> -- Returns these entities:
> --  1: (stackSize: 1, coordGrid: 2,50,50,5,24)
> --      1: Logs (count: 1, configID: 1511)
> --  2: (stackSize: 1, coordGrid: 2,50,50,5,26)
> --      1: Logs (count: 1, configID: 1511)
> ```