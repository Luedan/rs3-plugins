# NPCType

## Descripción General

An `NPCType` config contains the descriptive data necessary for the game to construct an [NPCEntity](../entity/npcentity.md).

These config types can be found within the `config.NPC` table:

```lua
config.NPC.RAT
config.NPC["QUEST_AMASCUT_ZEMOUREGAL_GUARD_1"]
config.NPC.FromID(456) -- config.NPC.FATHER_AERECK
```

> **Información**
> An `NPCType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `NPCType` includes:

* Display name
* References to Model IDs used for rendering
* Tile priority
* Custom picking bounds
* Background audio options
* MultiNPC configuration

## MultiNPC

MultiNPCs are special `NPCType` configs which allow an [NPCEntity](../entity/npcentity.md) to select one of many child `NPCTypes` based on a variable value.

For example, an [NPCEntity](../entity/npcentity.md) could swap between several `NPCTypes`, with different appearances and/or minimenu options, based on a variable value.
It could also be made invisible, if no `NPCType` is assigned to the current variable value.

## Ejemplos

```lua
-- Access an NPCType config directly by using its name
local hansCfg = config.NPC.HANS
-- or by ID lookup
local hansCfg = config.NPC.FromID(id.NPC.HANS)

-- Retrieve the NPCType being used by an NPCEntity
local allNPCs = NPCList.All()
for _,npcEntity in ipairs(allNPCs) do
    -- Directly
    local npcCfg = npcEntity.config
    -- Via ID
    local npcCfg = config.NPC.FromID(npcEntity.configID)
end
```

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Métodos

### GetOpCursor

```lua
function NPC:GetOpCursor(opIndex : Integer) -> Cursor?
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
> local cursor = config.NPC.FAI_LUMBRIDGE_GUARD_PEALE:GetOpCursor(1) -- config.Cursor.CURSOR_TALKTO(44)
> ```

### GetParamValue

```lua
function NPC:GetParamValue(param : ParamType) -> ?
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
> local value = config.NPC.BURTHORPE_MAN3:GetParamValue(config.Param.COMBATV2_NPC_ARMOUR) -- 130
> ```

### HasParam

```lua
function NPC:HasParam(param : ParamType) -> Boolean
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
> if config.NPC.BURTHORPE_MAN3:HasParam(config.Param.COMBATV2_NPC_ARMOUR) then
>     -- Get the param value
>     local value = config.NPC.BURTHORPE_MAN3:GetParamValue(config.Param.COMBATV2_NPC_ARMOUR)
> end
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"HANS"`. |
| typeName | String | The type of this config. Will always be `"NPC"`. |
| name | String | The display name of this config type. |
| attackOpPriority | Boolean | Whether the `Attack` op of an [NPCEntity](../entity/npcentity.md) using this config is given priority.Used in combination with `Player.GetAttackOpPriority`. |
| visibleCombatLevel | Integer | The combat level presented for an entity using this config. |
| castsShadows | Boolean | Whether an [NPCEntity](../entity/npcentity.md) using this config should cast a shadow. |
| overlayHeight | Integer | A custom override for how far above an NPCEntity to draw its overlays.Value is `-1` if unused. |
| walkSmoothing | Boolean | Whether an [NPCEntity](../entity/npcentity.md) using this config should follow walk routes smoothly.A smooth route uses bezier curves and acceleration.A non-smooth route travels linearly through tile centres. |
| isExamineOnly | Boolean | Shorthand check for whether this config type contains only an `Examine` op. |
| attackOpIndex | Integer | The op index for this configs `Attack` op.Returns `-1` if none is set. |
| examineOpIndex | Integer | The op index for this configs `Examine` op.Returns `-1` if none is set. |
| firstUniqueOpIndex | Integer | The op index where the first non-standard op begins.Returns `-1` if none is set. |
| opNames | [ String ] | A list of names shown for the available ops in this config.Use `pairs()` to iterate this list, which will provide both the op index and name as `opIndex,opName`. |
| bas | [BaseAnimSetType](baseanimsettype.md) | The animation set used by this config.Returns `nil` if none is set. |
| fastPicking | Boolean | Whether an [NPCEntity](../entity/npcentity.md) using this config uses a lower accuracy, but faster, picking test on triangles. |
| roughBounding | Integer | Whether an [NPCEntity](../entity/npcentity.md) using this config should skip triangle tests and stop at an earlier rectangular bounds test.`-1` = Only if `gridSize == 1``0` = Never`1` = Always |
| resize | Vector3 | A scaling transform applied to the body model(s) of an [NPCEntity](../entity/npcentity.md) using this config. |
| gridSize | Integer | The reported tile size of an [NPCEntity](../entity/npcentity.md) using this config.Used in various entity logic and priority checks. |
| turnSpeed | Integer | The turning speed of an [NPCEntity](../entity/npcentity.md) using this config.Affects facing and movement turn speeds. |
| wanderRange | Integer | The maximum tile distance an [NPCEntity](../entity/npcentity.md) will wander from its current coordinate when starting a new wander move. |
| maxRange | Integer | The maximum tile distance an [NPCEntity](../entity/npcentity.md) can move from its spawning coordinate.Also the maximum tile distance from its spawning coordinate at which it will pay attention to a [PlayerEntity](../entity/playerentity.md). |
| isActive | Boolean | Whether an [NPCEntity](../entity/npcentity.md) using this config is considered active.An inactive entity is not shown on the minimap and will not show in the minimenu. |
| isFamiliar | Boolean | Whether an [NPCEntity](../entity/npcentity.md) using this config is considered a familiar.Familiar-type NPCs have a lower draw order priority. |
| isAlwaysOnTop | Boolean | Greatly advances the draw order priority of an [NPCEntity](../entity/npcentity.md) using this config.Not guaranteed to be on top. |
| isAlwaysOnBottom | Boolean | Reduces the draw order priority of an [NPCEntity](../entity/npcentity.md) using this config.Not guaranteed to be at bottom. |
| priorityOffset | Integer | Adjusts the draw order priority of an [NPCEntity](../entity/npcentity.md) using this config.Can be positive or negative. |
| isOnMiniMap | Boolean | Whether an [NPCEntity](../entity/npcentity.md) using this config is shown on the minimap. |
| mapElement | [MapElementType](mapelementtype.md) | The map element to display for this config.Returns `nil` if none is set. |
| quests | [ [QuestType](questtype.md) ] | A list of all quests related to this config. |
| isMultiNPC | Boolean | Whether this config contains a sub-list of `NPCTypes` and a `multiVar` variable to use in selecting one.An [NPCEntity](../entity/npcentity.md) which uses a multiNPC config will expose it through [NPCEntity.parentConfig](../entity/npcentity.md#properties), while the selected `NPCType` sub-list config is exposed through [NPCEntity.config](../entity/npcentity.md#properties). |
| multiVar | [VarType](../config/vartype.md) | The variable which controls the currently displayed `NPCType`. |
| hasCustomBounding | Boolean | Whether an [NPCEntity](../entity/npcentity.md) using this config uses an overriding [AABB](../../math/aabb.md) bounds for picking tests.Often used by NPCs which have geometry or animations that make them tricky to click. |
| customBounding | [AABB](../../math/aabb.md)? | The [AABB](../../math/aabb.md) which describes this configs custom bounds.Returns `nil` if none is set. |
| hasBackgroundSound | Boolean | Whether an [NPCEntity](../entity/npcentity.md) using this config should play a sound depending on its animation state.Indicates that at least one of the ready/crawl/walk/run sounds is set. |
| backgroundSoundReady | Integer | TODO: Will become a config type |
| backgroundSoundCrawl | Integer | TODO: Will become a config type |
| backgroundSoundWalk | Integer | TODO: Will become a config type |
| backgroundSoundRun | Integer | TODO: Will become a config type |
| backgroundSoundRange | Integer | The maximum tile range, in `Grid units`, of any background sounds played by an [NPCEntity](../entity/npcentity.md) using this config.Distances above this range set volume to 0%. |
| backgroundSoundDropoffRange | Integer | The tile distance, in `Grid units`, at which background sounds in this config begin to drop off in volume.Distances below this range set volume to 100%. |
| backgroundSoundVolume | Integer | The base volume of any background sounds played by an [NPCEntity](../entity/npcentity.md) using this config. |
| params | [ [ParamType](paramtype.md) ] | Returns a list of all the [ParamTypes](paramtype.md) stored in this config. |