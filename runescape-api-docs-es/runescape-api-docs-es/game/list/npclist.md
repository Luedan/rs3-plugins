# NPCList

## Descripción General

An `NPCList` provides access to all active [NPCEntities](../entity/npcentity.md) in the game world, as well as several methods to search for entities.

> **Información**
> All methods return an array of [NPCEntities](../entity/npcentity.md).

See each method for examples on how to use this list.

## Funciones

### All

```lua
function NPCList.All() -> [ NPCEntity ]
```

Returns all active [NPCEntities](../entity/npcentity.md) in the game world in an array.

| Retorna | Descripción |
| --- | --- |
| [ [NPCEntity](../entity/npcentity.md) ] | An array of [NPCEntities](../entity/npcentity.md). |

> **Ejemplo**
> ```lua
> local allNPCs = NPCList.All()
> for _,npcEntity in ipairs(allNPCs) do
>     if npcEntity.config == config.NPC.HANS then
>         -- found Hans
>     end
> end
> ```

### ByUID

```lua
function NPCList.ByUID(uid : Integer) -> [ NPCEntity ]
```

Returns the [NPCEntity](../entity/npcentity.md) with the matching UID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| uid | Integer | A valid UID value. |

| Retorna | Descripción |
| --- | --- |
| [ [NPCEntity](../entity/npcentity.md) ] | An array of [NPCEntities](../entity/npcentity.md). |

> **Ejemplo**
> ```lua
> -- A UID obtained elsewhere
> local targetNPCUID = ...
> local found = NPCList.ByUID(targetNPCUID)
> if #found > 0 then
>     -- NPC was found
>     local npcEntity = found[1]
>     -- npcEntity.uid == targetNPCUID
> end
> ```

### ByName

```lua
function NPCList.ByName(name : String) -> [ NPCEntity ]
```

Returns any [NPCEntity](../entity/npcentity.md) with a display name matching the given `name` value.

String matches are case-insensitive.
Matches are exact unless wildcard characters `?` and/or `*` are provided.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | The string to match against `NPCEntity.displayName`. |

| Retorna | Descripción |
| --- | --- |
| [ [NPCEntity](../entity/npcentity.md) ] | An array of [NPCEntities](../entity/npcentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = NPCList.ByName("*lumbridge*")
> -- Returns these entities:
> --  1: Lumbridge guardsman (uid: 88197, configID: 9213, coordGrid: 0,50,50,4,59)
> --  2: Lumbridge guardsman (uid: 88228, configID: 32428, coordGrid: 0,50,50,19,51)
> --  3: Lumbridge guard dog (uid: 88232, configID: 14937, coordGrid: 0,50,50,35,28)
> --  4: Lumbridge guardsman (uid: 88234, configID: 14936, coordGrid: 0,50,50,36,28)
> --  5: Lumbridge Sage (uid: 88235, configID: 2244, coordGrid: 0,50,50,38,19)
> --  6: Lumbridge guardsman (uid: 88262, configID: 32429, coordGrid: 0,50,50,52,24)
> --  7: Lumbridge guardsman (uid: 88263, configID: 32429, coordGrid: 0,50,50,52,27)
> --  8: Lumbridge guardsman (uid: 88191, configID: 9213, coordGrid: 0,50,50,3,57)
> 
> found = NPCList.ByName("lumbridge sage")
> -- Returns these entities:
> --  1: Lumbridge Sage (uid: 88235, configID: 2244, coordGrid: 0,50,50,38,19)
> 
> found = NPCList.ByName("sage")
> -- Returns these entities:
> --  Empty
> 
> found = NPCList.ByName("*sage")
> -- Returns these entities:
> --  1: Lumbridge Sage (uid: 88235, configID: 2244, coordGrid: 0,50,50,38,19)
> ```

### ByDistance

```lua
function NPCList.ByDistance(coordGrid : CoordGrid, range : Integer) -> [ NPCEntity ]
```

Returns any [NPCEntity](../entity/npcentity.md) within `range` tiles of the given `coordGrid` value.

Exact coord matches should use a value of `0` for `range`.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordGrid | [CoordGrid](../coordgrid.md) | The coord at which to centre the distance search. |
| range | Integer | The maximum tile distance from the given coord which an [NPCEntity](../entity/npcentity.md) must be. |

| Retorna | Descripción |
| --- | --- |
| [ [NPCEntity](../entity/npcentity.md) ] | An array of [NPCEntities](../entity/npcentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = NPCList.ByDistance(CoordGrid._0_50_50_34_30, 4)
> -- Returns these entities:
> --  1: Lumbridge guard dog (uid: 88232, configID: 14937, coordGrid: 0,50,50,35,28)
> --  2: Lumbridge guardsman (uid: 88234, configID: 14936, coordGrid: 0,50,50,36,28)
> --  3: Musician (uid: 88231, configID: 29, coordGrid: 0,50,50,33,33)
> ```

### ByConfig

```lua
function NPCList.ByConfig(npcType : NPCType) -> [ NPCEntity ]
```

Returns any [NPCEntity](../entity/npcentity.md) that uses the given [NPCType](../config/npctype.md) config.

> **Información**
> If the [NPCEntity](../entity/npcentity.md) has a valid `NPCEntity.config` then this will test against `NPCEntity.config`.
If not, then the value for `NPCEntity.parentConfig` will be tested against instead.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| npcType | [NPCType](../config/npctype.md) | The config to look for when testing [NPCEntities](../entity/npcentity.md). |

| Retorna | Descripción |
| --- | --- |
| [ [NPCEntity](../entity/npcentity.md) ] | An array of [NPCEntities](../entity/npcentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = NPCList.ByConfig(config.NPC.HANS)
> -- Returns these entities:
> --  1: Hans (uid: 88220, configID: 0, coordGrid: 0,50,50,13,30)
> ```

### ByConfigID

```lua
function NPCList.ByConfigID(npcTypeID : Integer) -> [ NPCEntity ]
```

Returns any [NPCEntity](../entity/npcentity.md) that uses the given [NPCType](../config/npctype.md) config ID.

> **Información**
> If the [NPCEntity](../entity/npcentity.md) has a valid `NPCEntity.config` then this will test against `NPCEntity.configID`.
If not, then the value for `NPCEntity.parentConfigID` will be tested against instead.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| npcTypeID | Integer | The config ID to look for when testing [NPCEntities](../entity/npcentity.md). |

| Retorna | Descripción |
| --- | --- |
| [ [NPCEntity](../entity/npcentity.md) ] | An array of [NPCEntities](../entity/npcentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = NPCList.ByConfigID(id.NPC.HANS)
> -- Returns these entities:
> --  1: Hans (uid: 88220, configID: 0, coordGrid: 0,50,50,10,30)
> ```

### ByParentConfig

```lua
function NPCList.ByParentConfig(npcType : NPCType) -> [ NPCEntity ]
```

Returns any [NPCEntity](../entity/npcentity.md) that uses the given [NPCType](../config/npctype.md) config as its `parentConfig`.

> **Información**
> Only `NPCEntity.parentConfig` is tested, while `NPCEntity.config` is not tested against.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| npcType | [NPCType](../config/npctype.md) | The config to look for when testing [NPCEntities](../entity/npcentity.md). |

| Retorna | Descripción |
| --- | --- |
| [ [NPCEntity](../entity/npcentity.md) ] | An array of [NPCEntities](../entity/npcentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = NPCList.ByParentConfig(config.NPC.THIGUI_ROBIN_MULTI)
> -- Returns these entities:
> --  1:  (uid: 88238, configID: 11268, parentConfigID: 11268, coordGrid: 0,50,50,12,8)
> ```

### ByParentConfigID

```lua
function NPCList.ByParentConfigID(npcTypeID : Integer) -> [ NPCEntity ]
```

Returns any [NPCEntity](../entity/npcentity.md) that uses the given [NPCType](../config/npctype.md) parent config ID.

> **Información**
> Only `NPCEntity.parentConfigID` is tested, while `NPCEntity.configID` is not tested against.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| npcTypeID | Integer | The config ID to look for when testing [NPCEntities](../entity/npcentity.md). |

| Retorna | Descripción |
| --- | --- |
| [ [NPCEntity](../entity/npcentity.md) ] | An array of [NPCEntities](../entity/npcentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> found = NPCList.ByParentConfigID(id.NPC.THIGUI_ROBIN_MULTI)
> -- Returns these entities:
> --  1:  (uid: 88238, configID: 11268, parentConfigID: 11268, coordGrid: 0,50,50,12,8)
> ```

### Filter

```lua
function NPCList.Filter(filterSet : Table) -> [ NPCEntity ]
```

Returns any [NPCEntity](../entity/npcentity.md) that matches all tests in the `filterSet` table.

Available tests are:

| Key | Tipo | Descripción |
| --- | --- | --- |
| uid | Integer | A valid entity UID.`{ uid = npcEntity.uid }`See [NPCList.ByUID()](#byuid) |
| name | String | A name to match against `NPCEntity.displayName`.`{ name = "*lumbridge*" }`See [NPCList.ByName()](#byname) |
| coordGrid | [CoordGrid](../coordgrid.md) | A coord to test entity distance from.If `range` is not provided, the default value of `range` will be `0`.`{ coordGrid = CoordGrid._0_50_50_32_32 }`See [NPCList.ByDistance()](#bydistance) |
| range | Integer | Ignored if `coordGrid` key is not provided.`{ range = 4 }`See [NPCList.ByDistance()](#bydistance) |
| config | [NPCType](../config/npctype.md) | The config to match against `NPCEntity.config`.`{ config = config.NPC.HANS }`See [NPCList.ByConfig()](#byconfig) |
| configID | Integer | The config ID to match against `NPCEntity.configID`.`{ configID = id.NPC.HANS }`See [NPCList.ByConfigID()](#byconfigid) |
| parentConfig | [NPCType](../config/npctype.md) | The config to match against `NPCEntity.parentConfig`.`{ parentConfig = config.NPC.THIGUI_ROBIN_MULTI }`See [NPCList.ByParentConfig()](#byparentconfig) |
| parentConfigID | Integer | The config ID to match against `NPCEntity.parentConfigID`.`{ parentConfigID = id.NPC.THIGUI_ROBIN_MULTI }`See [NPCList.ByParentConfigID()](#byparentconfigid) |
| func | Function | A function which returns a boolean, and which takes an [NPCEntity](../entity/npcentity.md) as its only parameter.This function is called for every entity, and any call that returns `true` will include that [NPCEntity](../entity/npcentity.md) in the return array.`function ratFinder(npcEntity) { return npcEntity.config == config.NPC.RAT }``{ func = ratFinder }` |

Tests can be combined as shown below:

```text
-- Return all rats within 10 tiles of 0_50_50_32_32
found = NPCList.Filter( { config = config.NPC.RAT, coordGrid = CoordGrid._0_50_50_32_32, range = 10 } )
```

> **Información**
> Tests are inclusive.
All must pass in order for the [NPCEntity](../entity/npcentity.md) to be included in the return array.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| filterSet | Table | A table of key-value pairs which describe individual tests to perform. |

| Retorna | Descripción |
| --- | --- |
| [ [NPCEntity](../entity/npcentity.md) ] | An array of [NPCEntities](../entity/npcentity.md). |

> **Ejemplo**
> ```lua
> -- At coord 0_50_50_32_32
> 
> -- Filter all NPCs for config ID
> local foundByFilterConfigID = NPCList.Filter( { configID = id.NPC.RAT } )
> -- Returns these entities:
> --  1: Rat (uid: 88198, configID: 47, coordGrid: 0,50,50,7,6)
> --  2: Rat (uid: 88203, configID: 47, coordGrid: 0,50,50,5,9)
> --  3: Rat (uid: 88195, configID: 47, coordGrid: 0,50,50,7,9)
> --  4: Rat (uid: 88194, configID: 47, coordGrid: 0,50,50,9,10)
> --  5: Rat (uid: 88199, configID: 47, coordGrid: 0,50,50,6,8)
> --  6: Rat (uid: 88196, configID: 47, coordGrid: 0,50,50,13,8)
> --  7: Rat (uid: 88201, configID: 47, coordGrid: 0,50,50,6,9)
> --  8: Rat (uid: 88200, configID: 47, coordGrid: 0,50,50,0,14)
> 
> -- Filter all NPCs for a specific config
> local foundByFilterConfig = NPCList.Filter( { config = config.NPC.RAT } )
> -- Returns these entities:
> --  1: Rat (uid: 88198, configID: 47, coordGrid: 0,50,50,8,9)
> --  2: Rat (uid: 88203, configID: 47, coordGrid: 0,50,50,5,9)
> -- ...
> --  8: Rat (uid: 88200, configID: 47, coordGrid: 0,50,50,2,1)
> 
> -- Filter all NPCs for the exact display name "rat"
> local foundByFilterName = NPCList.Filter( { name = "rat" } )
> -- Returns these entities:
> --  1: Rat (uid: 88198, configID: 47, coordGrid: 0,50,50,6,8)
> --  2: Rat (uid: 88203, configID: 47, coordGrid: 0,50,50,14,9)
> -- ...
> --  8: Rat (uid: 88200, configID: 47, coordGrid: 0,50,50,14,1)
> 
> function filterRatNPC(npc)
>     return npc.configID == id.NPC.RAT
> end
> 
> -- Filter all NPCs for those that pass the func 'filterRatNPC'
> local foundByFilterFunc = NPCList.Filter( { func = filterRatNPC } )
> -- Returns these entities:
> --  1: Rat (uid: 88198, configID: 47, coordGrid: 0,50,50,9,12)
> --  2: Rat (uid: 88203, configID: 47, coordGrid: 0,50,50,5,9)
> -- ...
> --  8: Rat (uid: 88200, configID: 47, coordGrid: 0,50,50,2,0)
> 
> -- Filter all NPCs for those within 2 tiles of 0_50_50_32_32
> local foundByFilterCoord = NPCList.Filter( { coordGrid = CoordGrid._0_50_50_32_32, range = 2 } )
> -- Returns these entities:
> --  1: Doomsayer (uid: 88225, configID: 3777, coordGrid: 0,50,50,30,28)
> --  2: Musician (uid: 88231, configID: 29, coordGrid: 0,50,50,33,33)
> 
> -- Filter all NPCs for those of config type Rat within 3 tiles of 0_50_50_9_10
> local foundByFilterConfigAndCoord = NPCList.Filter( { coordGrid = CoordGrid._0_50_50_9_10, range = 3, config = config.NPC.RAT } )
> -- Returns these entities:
> --  1: Rat (uid: 88203, configID: 47, coordGrid: 0,50,50,8,9)
> --  2: Rat (uid: 88201, configID: 47, coordGrid: 0,50,50,10,11)
> ```