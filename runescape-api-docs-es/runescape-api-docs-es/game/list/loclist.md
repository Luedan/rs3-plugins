# LocList

## Descripción General

An `LocList` provides access to all active [LocEntities](../entity/locentity.md) in the game world, as well as several methods to search for entities.

See each method for examples on how to use this list.

> **Important**
> Not all locations in the game are available as an entity.
Only locations which are considered `active` are accessible, such locations that animate, are interactable, or can be modified by the server or variable state.
> The remaining location are combined into larger static locations, to be rendered more optimally.

> **Información**
> All methods return an array of [LocEntities](../entity/locentity.md).

> **Advertencia**
> These functions can return a large number of results and may impact performance if called frequently.
> Prefer using methods where distance testing is available, such as [LocList.ByDistance](#bydistance) or [LocList.Filter](#filter) with `coordGrid` and `range` tests provided.

## Funciones

### All

```lua
function LocList.All() -> [ LocEntity ]
```

Returns all active [LocEntities](../entity/locentity.md) in the game world in an array.

| Retorna | Descripción |
| --- | --- |
| [ [LocEntity](../entity/locentity.md) ] | An array of [LocEntities](../entity/locentity.md). |

> **Ejemplo**
> ```lua
> local allLocs = LocList.All()
> for _,locEntity in ipairs(allLocs) do
>     if locEntity.config == config.Loc.FFH_WILLOW_TREE_TRUNK then
>         -- found a Willow tree
>     end
> end
> ```

### ByName

```lua
function LocList.ByName(name : String) -> [ LocEntity ]
```

Returns any [LocEntity](../entity/locentity.md) with a display name matching the given `name` value.

String matches are case-insensitive.
Matches are exact unless wildcard characters `?` and/or `*` are provided.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | The string to match against `LocEntity.displayName`. |

| Retorna | Descripción |
| --- | --- |
| [ [LocEntity](../entity/locentity.md) ] | An array of [LocEntities](../entity/locentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = LocList.ByName("*lumbridge*")
> -- Returns these entities:
> -- 1: Lumbridge farms (configID: 69782, coordGrid: 0,50,50,17,50)
> -- 2: Lumbridge Castle (configID: 69783, coordGrid: 0,50,50,17,48)
> -- 3: Lumbridge lodestone (configID: 69861, coordGrid: 0,50,50,32,21)
> -- 4: Lumbridge Castle (configID: 69787, coordGrid: 0,50,50,36,23)
> -- 5: Lumbridge farms (configID: 69788, coordGrid: 0,50,50,36,25)
> -- 6: Lumbridge Castle (configID: 69791, coordGrid: 0,50,50,60,30)
> -- 7: Lumbridge (configID: 69795, coordGrid: 0,51,50,15,26)
> 
> found = LocList.ByName("lumbridge lodestone")
> -- Returns these entities:
> -- 1: Lumbridge lodestone (configID: 69861, coordGrid: 0,50,50,32,21)
> 
> found = LocList.ByName("lodestone")
> -- Returns these entities:
> --  Empty
> 
> found = LocList.ByName("*lodestone")
> -- Returns these entities:
> -- 1: Lumbridge lodestone (configID: 69861, coordGrid: 0,50,50,32,21)
> -- 2: Al Kharid lodestone (configID: 69847, coordGrid: 0,51,49,32,48)
> ```

### ByDistance

```lua
function LocList.ByDistance(coordGrid : CoordGrid, range : Integer, sameLevel : Boolean) -> [ LocEntity ]
```

Returns any [LocEntity](../entity/locentity.md) within `range` tiles of the given `coordGrid` value.

Exact coord matches should use a value of `0` for `range`.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordGrid | [CoordGrid](../coordgrid.md) | The coordinate at which to centre the distance search. |
| range | Integer | The maximum tile distance from the given coord which an [LocEntity](../entity/locentity.md) must be.A value of `0` tests only the exact coordinate provided. |
| sameLevel | Boolean | Whether to only consider [LocEntities](../entity/locentity.md) on the same level as the given coordinate or [LocEntities](../entity/locentity.md) on all levels. |

| Retorna | Descripción |
| --- | --- |
| [ [LocEntity](../entity/locentity.md) ] | An array of [LocEntities](../entity/locentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> -- On the same level
> found = LocList.ByDistance(CoordGrid._0_50_50_34_30, 4, true)
> -- Returns these entities:
> -- 1: Crate (configID: 113566, coordGrid: 0,50,50,30,28)
> -- 2: Bush (configID: 119753, coordGrid: 0,50,50,37,28)
> -- 3: Buttercups (configID: 118880, coordGrid: 0,50,50,35,30)
> -- 4: Willow (configID: 38616, coordGrid: 0,50,50,35,32)
> -- 5: Bullrushes (configID: 5542, coordGrid: 0,50,50,38,32)
> -- 6: Fern (configID: 129454, coordGrid: 0,50,50,33,34)
> 
> -- On the all levels
> found = LocList.ByDistance(CoordGrid._0_50_50_34_30, 4, false)
> -- 1: Crate (configID: 113566, coordGrid: 0,50,50,30,28)
> -- 2: Bush (configID: 119753, coordGrid: 0,50,50,37,28)
> -- 3: Buttercups (configID: 118880, coordGrid: 0,50,50,35,30)
> -- 4: Willow (configID: 38717, coordGrid: 1,50,50,34,31)
> -- 5: Willow (configID: 38616, coordGrid: 0,50,50,35,32)
> -- 6:  (configID: 43520, coordGrid: 1,50,50,33,33)
> -- 7: Bullrushes (configID: 5542, coordGrid: 0,50,50,38,32)
> -- 8: Fern (configID: 129454, coordGrid: 0,50,50,33,34)
> ```

### ByConfig

```lua
function LocList.ByConfig(locType : LocType) -> [ LocEntity ]
```

Returns any [LocEntity](../entity/locentity.md) that uses the given [LocType](../config/loctype.md) config.

> **Información**
> If the [LocEntity](../entity/locentity.md) has a valid `LocEntity.config` then this will test against `LocEntity.config`.
If not, then the value for `LocEntity.parentConfig` will be tested against instead.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| locType | [LocType](../config/loctype.md) | The config to look for when testing [LocEntities](../entity/locentity.md). |

| Retorna | Descripción |
| --- | --- |
| [ [LocEntity](../entity/locentity.md) ] | An array of [LocEntities](../entity/locentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = LocList.ByConfig(config.Loc.FFH_WILLOW_TREE_TRUNK)
> -- Returns these entities:
> -- 1: Willow (configID: 38616, coordGrid: 0,49,51,26,6)
> -- 2: Willow (configID: 38616, coordGrid: 0,49,51,32,12)
> -- 3: Willow (configID: 38616, coordGrid: 0,49,51,40,1)
> -- 4: Willow (configID: 38616, coordGrid: 0,49,51,41,12)
> -- 5: Willow (configID: 38616, coordGrid: 0,50,50,35,32)
> -- 6: Willow (configID: 38616, coordGrid: 0,50,51,20,41)
> -- 7: Willow (configID: 38616, coordGrid: 0,50,51,20,45)
> -- 8: Willow (configID: 38616, coordGrid: 0,50,51,21,37)
> ```

### ByConfigID

```lua
function LocList.ByConfigID(locTypeID : Integer) -> [ LocEntity ]
```

> **Información**
> If the [LocEntity](../entity/locentity.md) has a valid `LocEntity.config` then this will test against `LocEntity.configID`.
If not, then the value for `LocEntity.parentConfigID` will be tested against instead.

> **Información**
> Only `LocEntity.configID` is tested, while `LocEntity.parentConfigID` is not tested against.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| locTypeID | Integer | The config ID to look for when testing [LocEntities](../entity/locentity.md). |

| Retorna | Descripción |
| --- | --- |
| [ [LocEntity](../entity/locentity.md) ] | An array of [LocEntities](../entity/locentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = LocList.ByConfigID(id.Loc.FFH_WILLOW_TREE_TRUNK)
> -- Returns these entities:
> -- 1: Willow (configID: 38616, coordGrid: 0,49,51,26,6)
> -- 2: Willow (configID: 38616, coordGrid: 0,49,51,32,12)
> -- 3: Willow (configID: 38616, coordGrid: 0,49,51,40,1)
> -- 4: Willow (configID: 38616, coordGrid: 0,49,51,41,12)
> -- 5: Willow (configID: 38616, coordGrid: 0,50,50,35,32)
> -- 6: Willow (configID: 38616, coordGrid: 0,50,51,20,41)
> -- 7: Willow (configID: 38616, coordGrid: 0,50,51,20,45)
> -- 8: Willow (configID: 38616, coordGrid: 0,50,51,21,37)
> ```

### ByParentConfig

```lua
function LocList.ByParentConfig(locType : LocType) -> [ LocEntity ]
```

Returns any [LocEntity](../entity/locentity.md) that uses the given [LocType](../config/loctype.md) config.

> **Información**
> Only `LocEntity.parentConfig` is tested, while `LocEntity.config` is not tested against.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| locType | [LocType](../config/loctype.md) | The config to look for when testing [LocEntities](../entity/locentity.md). |

| Retorna | Descripción |
| --- | --- |
| [ [LocEntity](../entity/locentity.md) ] | An array of [LocEntities](../entity/locentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = LocList.ByParentConfig(config.Loc.GARDEN_LUMBRIDGE_STATUE)
> -- Returns these entities:
> -- 1: Statue (configID: 36751, parentConfigID: 36755, coordGrid: 0,50,50,31,17)
> ```

### ByParentConfigID

```lua
function LocList.ByParentConfigID(locTypeID : Integer) -> [ LocEntity ]
```

Returns any [LocEntity](../entity/locentity.md) that uses the given [LocType](../config/loctype.md) config ID.

> **Información**
> Only `LocEntity.parentConfigID` is tested, while `LocEntity.configID` is not tested against.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| locTypeID | Integer | The config ID to look for when testing [LocEntities](../entity/locentity.md). |

| Retorna | Descripción |
| --- | --- |
| [ [LocEntity](../entity/locentity.md) ] | An array of [LocEntities](../entity/locentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = LocList.ByParentConfigID(id.Loc.GARDEN_LUMBRIDGE_STATUE)
> -- Returns these entities:
> -- 1: Statue (configID: 36751, parentConfigID: 36755, coordGrid: 0,50,50,31,17)
> ```

### Filter

```lua
function LocList.Filter(filterSet : Table) -> [ LocEntity ]
```

Returns any [LocEntity](../entity/locentity.md) that matches all tests in the `filterSet` table.

Available tests are:

| Key | Tipo | Descripción |
| --- | --- | --- |
| name | String | A name to match against `LocEntity.displayName`.`{ name = "*lumbridge*" }`See [LocList.ByName()](#byname) |
| coordGrid | [CoordGrid](../coordgrid.md) | A coordinate to test entity distance from.If `range` is not provided, the default value of `range` will be `0`.If `sameLevel` is not provided, the default value of `sameLevel` will be `false`.`{ coordGrid = CoordGrid._0_50_50_32_32 }`See [LocList.ByDistance()](#bydistance) |
| range | Integer | Ignored if `coordGrid` key is not provided.`{ range = 4 }`See [LocList.ByDistance()](#bydistance) |
| sameLevel | Boolean | Ignored if `coordGrid` key is not provided.`{ sameLevel = true }`See [LocList.ByDistance()](#bydistance) |
| config | [LocType](../config/loctype.md) | The config to match against `LocEntity.config`.`{ config = config.Loc.FFH_WILLOW_TREE_TRUNK }`See [LocList.ByConfig()](#byconfig) |
| configID | Integer | The config ID to match against `LocEntity.configID`.`{ configID = id.Loc.FFH_WILLOW_TREE_TRUNK }`See [LocList.ByConfigID()](#byconfigid) |
| parentConfig | [LocType](../config/loctype.md) | The config to match against `LocEntity.parentConfig`.`{ parentConfig = config.Loc.GARDEN_LUMBRIDGE_STATUE }`See [LocList.ByParentConfig()](#byparentconfig) |
| parentConfigID | Integer | The config ID to match against `LocEntity.parentConfigID`.`{ parentConfigID = id.Loc.GARDEN_LUMBRIDGE_STATUE }`See [LocList.ByParentConfigID()](#byparentconfigid) |
| func | Function | A function which returns a boolean, and which takes a [LocEntity](../entity/locentity.md) as its only parameter.This function is called for every entity, and any call that returns `true` will include that [LocEntity](../entity/locentity.md) in the return array.`function willowFinder(locEntity) { return locEntity.config == config.Loc.FFH_WILLOW_TREE_TRUNK }``{ func = willowFinder }` |

Tests can be combined as shown below:

```text
-- Return all willow tree trunks within 10 tiles of 0_50_50_32_32
found = LocList.Filter({ config = config.Loc.FFH_WILLOW_TREE_TRUNK, coordGrid = CoordGrid._0_50_50_32_32, range = 10 })
```

> **Información**
> Tests are inclusive.
All must pass in order for the [LocEntity](../entity/locentity.md) to be included in the return array.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| filterSet | Table | A table of key-value pairs which describe individual tests to perform. |

| Retorna | Descripción |
| --- | --- |
| [ [LocEntity](../entity/locentity.md) ] | An array of [LocEntities](../entity/locentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> -- Filter all Locs for config ID
> local foundByFilterConfigID = LocList.Filter({ configID = id.Loc.FFH_WILLOW_TREE_TRUNK })
> -- Returns these entities:
> -- 1: Willow (configID: 38616, coordGrid: 0,49,51,26,6)
> -- 2: Willow (configID: 38616, coordGrid: 0,49,51,32,12)
> -- 3: Willow (configID: 38616, coordGrid: 0,49,51,40,1)
> -- 4: Willow (configID: 38616, coordGrid: 0,49,51,41,12)
> -- 5: Willow (configID: 38616, coordGrid: 0,50,50,35,32)
> -- 6: Willow (configID: 38616, coordGrid: 0,50,51,20,41)
> -- 7: Willow (configID: 38616, coordGrid: 0,50,51,20,45)
> -- 8: Willow (configID: 38616, coordGrid: 0,50,51,21,37)
> 
> 
> -- Filter all Locs for a specific config
> local foundByFilterConfig = LocList.Filter({ config = config.Loc.FFH_WILLOW_TREE_TRUNK })
> -- Returns these entities:
> -- 1: Willow (configID: 38616, coordGrid: 0,49,51,26,6)
> -- 2: Willow (configID: 38616, coordGrid: 0,49,51,32,12)
> -- 3: Willow (configID: 38616, coordGrid: 0,49,51,40,1)
> -- 4: Willow (configID: 38616, coordGrid: 0,49,51,41,12)
> -- 5: Willow (configID: 38616, coordGrid: 0,50,50,35,32)
> -- 6: Willow (configID: 38616, coordGrid: 0,50,51,20,41)
> -- 7: Willow (configID: 38616, coordGrid: 0,50,51,20,45)
> -- 8: Willow (configID: 38616, coordGrid: 0,50,51,21,37)
> 
> 
> -- Filter all Locs for the exact display name "willow"
> local foundByFilterName = LocList.Filter({ name = "willow" })
> -- Returns these entities:
> -- 1: Willow (configID: 38616, coordGrid: 0,49,51,26,6)
> -- 2: Willow (configID: 38717, coordGrid: 1,49,51,25,5)
> -- 3: Willow (configID: 38717, coordGrid: 1,49,51,31,11)
> -- 4: Willow (configID: 38616, coordGrid: 0,49,51,32,12)
> -- 5: Willow (configID: 38616, coordGrid: 0,49,51,40,1)
> -- 6: Willow (configID: 38616, coordGrid: 0,49,51,41,12)
> -- 7: Willow (configID: 38717, coordGrid: 1,49,51,39,0)
> -- 8: Willow (configID: 38717, coordGrid: 1,49,51,40,11)
> -- 9: Willow (configID: 38717, coordGrid: 1,50,50,34,31)
> -- 10: Willow (configID: 38616, coordGrid: 0,50,50,35,32)
> -- 11: Willow (configID: 38616, coordGrid: 0,50,51,20,41)
> -- 12: Willow (configID: 38616, coordGrid: 0,50,51,20,45)
> -- 13: Willow (configID: 38616, coordGrid: 0,50,51,21,37)
> -- 14: Willow (configID: 38717, coordGrid: 1,50,51,19,40)
> -- 15: Willow (configID: 38717, coordGrid: 1,50,51,19,44)
> -- 16: Willow (configID: 38717, coordGrid: 1,50,51,20,36)
> 
> 
> function filterWillowLow(loc)
>     return loc.configID == id.Loc.FFH_WILLOW_TREE_TRUNK
> end
> 
> -- Filter all Locs for those that pass the func 'filterWillowLoc'
> local foundByFilterFunc = LocList.Filter({ func = filterWillowLoc })
> -- Returns these entities:
> -- 1: Willow (configID: 38616, coordGrid: 0,49,51,26,6)
> -- 2: Willow (configID: 38616, coordGrid: 0,49,51,32,12)
> -- 3: Willow (configID: 38616, coordGrid: 0,49,51,40,1)
> -- 4: Willow (configID: 38616, coordGrid: 0,49,51,41,12)
> -- 5: Willow (configID: 38616, coordGrid: 0,50,50,35,32)
> -- 6: Willow (configID: 38616, coordGrid: 0,50,51,20,41)
> -- 7: Willow (configID: 38616, coordGrid: 0,50,51,20,45)
> -- 8: Willow (configID: 38616, coordGrid: 0,50,51,21,37)
> 
> -- Filter all Locs for those within 2 tiles of 0_50_50_32_32
> local foundByFilterCoord = LocList.Filter({ coordGrid = CoordGrid._0_50_50_32_32, range = 2 })
> -- Returns these entities:
> -- 1: Willow (configID: 38717, coordGrid: 1,50,50,34,31)
> -- 2:  (configID: 43520, coordGrid: 1,50,50,33,33)
> -- 3: Fern (configID: 129454, coordGrid: 0,50,50,33,34)
> 
> 
> -- Filter all Locs for those of config type willow within 3 tiles of 0_50_50_32_32
> local foundByFilterConfigAndCoord = LocList.Filter({ coordGrid = CoordGrid._0_50_50_32_32, range = 3, config = config.Loc.FFH_WILLOW_TREE_TRUNK })
> -- Returns these entities:
> -- 1: Willow (configID: 38616, coordGrid: 0,50,50,35,32)
> ```