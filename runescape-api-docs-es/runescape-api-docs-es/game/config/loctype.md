# LocType

## Descripción General

A `LocType` config contains the descriptive data necessary for the game to construct a `LocEntity`.

These config types can be found within the `config.Loc` table:

```lua
config.Loc.TRAWLER_GANGPLANK
config.Loc["PERCY_SACKS"]
config.Loc.FromID(456) -- config.Loc.BASALT_FLOOR_DETAIL_1
```

> **Información**
> A `LocType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `LocType` includes:

* Display name
* MultiLoc configuration

## MultiLoc

MultiLocs are special `LocType` configs which allow an [LocEntity](../entity/locentity.md) to select one of many child `LocTypes` based on a variable value.

For example, an [LocEntity](../entity/locentity.md) could swap between several `LocTypes`, with different appearances and/or minimenu options, based on a variable value.
It could also be made invisible, if no `LocType` is assigned to the current variable value.

## Ejemplos

```lua
-- Access a LocType config directly by using its name
local winchCfg = config.Loc.WINCHLADDER1
-- or by ID lookup
local winchCfg = config.Loc.FromID(id.Loc.WINCHLADDER1)
```

## Enumeraciones

### LocShapeType

A `LocShapeType` is a usage hint found in all `LocType` configs.
A config can have multiple of these `LocShapeTypes`, each of which having its own set of models to display.

Only one type can be active at a time in a [LocEntity](../entity/locentity.md), and the current `LocShapeType` being used is available through the property [LocEntity.shapeType](../entity/locentity.md#properties).

| Name | Value |
| --- | --- |
| WALL_STRAIGHT | 0 |
| WALL_DIAGONALCORNER | 1 |
| WALL_L | 2 |
| WALL_SQUARECORNER | 3 |
| WALLDECOR_STRAIGHT_NOOFFSET | 4 |
| WALLDECOR_STRAIGHT_OFFSET | 5 |
| WALLDECOR_DIAGONAL_OFFSET | 6 |
| WALLDECOR_DIAGONAL_NOOFFSET | 7 |
| WALLDECOR_DIAGONAL_BOTH | 8 |
| WALL_DIAGONAL | 9 |
| CENTREPIECE_STRAIGHT | 10 |
| CENTREPIECE_DIAGONAL | 11 |
| ROOF_STRAIGHT | 12 |
| ROOF_DIAGONAL_WITH_ROOFEDGE | 13 |
| ROOF_DIAGONAL | 14 |
| ROOF_L_CONCAVE | 15 |
| ROOF_L_CONVEX | 16 |
| ROOF_FLAT | 17 |
| ROOFEDGE_STRAIGHT | 18 |
| ROOFEDGE_DIAGONALCORNER | 19 |
| ROOFEDGE_L | 20 |
| ROOFEDGE_SQUARECORNER | 21 |
| GROUNDDECOR | 22 |
| WALL_L_ALT | 23 |
| WALLDECOR_DIAGONAL_BOTH_ALT | 24 |

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Métodos

### GetOpCursor

```lua
function Loc:GetOpCursor(opIndex : Integer) -> Cursor?
```

Returns the custom [CursorType](cursortype.md), if any, used for the given op index.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Integer | The op index.Valid values are `1` -> `6` |

| Retorna | Descripción |
| --- | --- |
| [CursorType](cursortype.md)? | The cursor type to display.Returns `nil` if no op exists for this index, or no custom [CursorType](cursortype.md) is set on an existing op. |

> **Ejemplo**
> ```lua
> -- Get the cursor
> local cursor = config.Loc.PLAYER_FORT_TOWNHALL_LVLMID_STAIRS_ORNATE:GetOpCursor(3) -- config.Cursor.CURSOR_CLIMB_DOWN(53)
> ```

### GetModelIDs

```lua
function Loc:GetModelIDs(locShapeType : LocShapeType) -> [ Integer ]
```

Returns the model IDs associated with the given [LocShapeType](#locshapetype).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| locShapeType | [LocShapeType](#locshapetype) | The [LocShapeType](#locshapetype) to gather model IDs with. |

| Retorna | Descripción |
| --- | --- |
| [ Integer ] | The list of model IDs.Returns an empty list if the [LocShapeType](#locshapetype) is not supported by this config. |

> **Ejemplo**
> ```lua
> -- Get the cursor
> local cursor = config.Loc.PLAYER_FORT_TOWNHALL_LVLMID_STAIRS_ORNATE:GetOpCursor(3) -- config.Cursor.CURSOR_CLIMB_DOWN(53)
> ```

### GetParamValue

```lua
function Loc:GetParamValue(param : ParamType) -> ?
```

Returns the corresponding output value for the given input [ParamType](paramtype.md).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| param | [ParamType](paramtype.md) | The input param value. |

| Retorna | Descripción |
| --- | --- |
| ? | The corresponding output value.Returns `param.defaultValue` if the param is not found in the data structure. |

> **Ejemplo**
> ```lua
> -- Get a value
> local value = config.Loc.ELR1_INTERACT_CONSTRUCTION:GetParamValue(config.Param.ELR1_NAME_PLURAL) -- "wooden tortems"
> ```

### HasParam

```lua
function Loc:HasParam(param : ParamType) -> Boolean
```

Returns whether this config contains output data for the given input [ParamType](paramtype.md).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| param | [ParamType](paramtype.md) | The input param value. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether a corresponding value exists in this config for [ParamType](paramtype.md). |

> **Ejemplo**
> ```lua
> -- Get a value, if a param for it exists
> if config.Loc.ELR1_INTERACT_CONSTRUCTION:HasParam(config.Param.ELR1_NAME_PLURAL) then
>     -- Get the param value
>     local value = config.Loc.ELR1_INTERACT_CONSTRUCTION:GetParamValue(config.Param.ELR1_NAME_PLURAL)
> end
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"WINCHLADDER1"`. |
| typeName | String | The type of this config. Will always be `"Loc"`. |
| name | String | The display name of this config type. |
| fastPicking | Boolean | Whether a `LocEntity` using this config uses a lower accuracy, but faster, picking test on triangles. |
| width | Integer | The width of this config on the X axis, in grid units. |
| length | Integer | The length of this config on the Z axis, in grid units. |
| modelOffset | [Vector3](../../math/vector.md#vector3) | A positional transform applied to the models of this config.This is applied before `modelScale`. |
| modelScale | [Vector3](../../math/vector.md#vector3) | A scaling transform applied to the models of this config.This is applied after `modelOffset` and before `modelPostOffset`. |
| modelPostOffset | [Vector3](../../math/vector.md#vector3) | A final positional transform applied to the models of this config.This is applied after `modelScale`. |
| groundDecorOffset | Integer | Returns the height offset applied to [World.GetGroundHeight()](../world.md#getgroundheight) by an entity using this config, if also using [LocShapeType.GROUNDDECOR](#locshapetype). |
| hasCustomBounding | Boolean | Whether a [LocEntity](../entity/locentity.md) using this config uses an overriding [AABB](../../math/aabb.md) bounds for picking tests.Often used by Locs which have geometry or animations that make them tricky to click. |
| customBounding | [AABB](../../math/aabb.md)? | The [AABB](../../math/aabb.md) which describes this configs custom bounds.Returns `nil` if none is set. |
| IsActive | Boolean | Indicates whether a [LocEntity](../entity/locentity.md) using this config can be modified by the server. |
| isExamineOnly | Boolean | Shorthand check for whether this config type contains only an `Examine` op. |
| opNames | [ String ] | A list of names shown for the available ops in this config.Use `pairs()` to iterate this list, which will provide both the op index and name as `opIndex,opName`. |
| blockWalk | Boolean | Whether a [LocEntity](../entity/locentity.md) using this config will block route pathing through the tile(s) it is placed on. |
| quests | [ [QuestType](questtype.md) ] | A list of all quests related to this config. |
| mapElement | [MapElementType](mapelementtype.md) | The map element to display for this config.Returns `nil` if none is set. |
| useRandomAnimationFrame | Boolean | Whether the animation played by [LocEntities](../entity/locentity.md) using this config should start on a random frame. |
| animations | [ [SeqType](seqtype.md) ] | A list of animations this config can play. |
| defaultAnimation | [SeqType](seqtype.md) | The default animation played by this config.Returns `nil` if none is set. |
| isMultiLoc | Boolean | Whether this config contains a sub-list of `LocTypes` and a `multiVar` variable to use in selecting one.An [LocEntity](../entity/locentity.md) which uses a multiLoc config will expose it through [LocEntity.parentConfig](../entity/locentity.md#properties), while the selected `LocType` sub-list config is exposed through [LocEntity.config](../entity/locentity.md#properties). |
| multiVar | [VarType](../config/vartype.md) | The variable which controls the currently displayed `LocType`. |
| locShapeTypes | [ [LocShapeType](#locshapetype) ] | Returns a list of all [LocShapeTypes](#locshapetype) supported by this config.Use these along with [Loc:GetModelIDs()](#getmodelids) to get the model IDs used by this config. |
| params | [ [ParamType](paramtype.md) ] | Returns a list of all the [ParamTypes](paramtype.md) stored in this config. |