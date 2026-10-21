# ObjType

## Descripción General

A `ObjType` config contains the descriptive data necessary for the game to populate a `ObjStackEntity`.

These config types can be found within the `config.Obj` table:

```lua
config.Obj.LOGS
config.Obj["UNSTRUNG_MAGIC_SHORTBOW"]
config.Obj.FromID(456) -- config.Obj.SCORPIONCAGEEMPTY
```

> **Información**
> An `ObjType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `ObjType` includes:

* Display name
* ... TODO

## Ejemplos

```lua
-- Access an ObjType config directly by using its name
local steelBarCfg = config.Obj.STEEL_BAR
-- or by ID lookup
local steelBarCfg = config.Obj.FromID(id.Obj.STEEL_BAR)

-- Retrieve the ObjType(s) being used by an ObjStackEntity
-- TODO
```

## Enumeraciones

### ObjStackType

Determines how individual objects stack with objects of the same type.

| Name | Valor | Descripción |
| --- | --- | --- |
| SOMETIMES | 0 | Objects of this type will stack only in Inventories that allow stacking. |
| ALWAYS | 1 | Objects of this type stack at all times. |
| NEVER | 2 | Objects of this type can never be stacked.This type is always used for objects with ObjVars. |

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Métodos

### GetGroundOpCursor

```lua
function Obj:GetGroundOpCursor(opIndex : Integer) -> Cursor?
```

Returns the custom [CursorType](cursortype.md), if any, used for the given op index when the ObjType is on the ground.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Integer | The op index. |

| Retorna | Descripción |
| --- | --- |
| [CursorType](cursortype.md)? | The cursor type to display.Returns `nil` if no op exists for this index, or no custom [CursorType](cursortype.md) is set on an existing op. |

> **Ejemplo**
> ```lua
> -- Get the cursor
> local cursor = config.Obj.CABBAGE:GetGroundOpCursor(3) -- config.Cursor.CURSOR_TAKE(45)
> ```

### GetInterfaceOpCursor

```lua
function Obj:GetInterfaceOpCursor(opIndex : Integer) -> Cursor?
```

Returns the custom [CursorType](cursortype.md), if any, used for the given op index when the ObjType is shown in an interface component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Integer | The op index. |

| Retorna | Descripción |
| --- | --- |
| [CursorType](cursortype.md)? | The cursor type to display.Returns `nil` if no op exists for this index, or no custom [CursorType](cursortype.md) is set on an existing op. |

> **Ejemplo**
> ```lua
> -- Get the cursor
> local cursor = config.Obj.ELR1_TORTOISE_TRAP:GetInterfaceOpCursor(1) -- config.Cursor.CURSOR_HUNTER(167)
> ```

### GetParamValue

```lua
function Obj:GetParamValue(param : ParamType) -> ?
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
> local value = config.Obj.AIDE_SHORTSWORD:GetParamValue(config.Param.ATTACKRATE) -- 4
> ```

### HasParam

```lua
function Obj:HasParam(param : ParamType) -> Boolean
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
> if config.Obj.AIDE_SHORTSWORD:HasParam(config.Param.ATTACKRATE) then
>     -- Get the param value
>     local value = config.Obj.AIDE_SHORTSWORD:GetParamValue(config.Param.ATTACKRATE)
> end
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"STEEL_BAR"`. |
| typeName | String | The type of this config. Will always be `"Obj"`. |
| name | String | The display name of this config type. |
| isMembers | Boolean | Whether this object is for members. |
| category | Integer | The category type of this config.Returns `-1` if none is set.Category name is available using `id.Category.FromID()`. |
| teamID | Integer | Assigns this team ID to a [PlayerEntity](../entity/playerentity.md) if the object is worn. |
| cost | Integer | The 64-bit numeric value of this object. |
| stackType | [ObjStackType](#objstacktype) | The stacking behaviour of this config. |
| isStockmarket | Boolean | Whether this object can be traded on the Grand Exchange. |
| stockmarketBuyLimit | Integer | How many of this item can be bought on the Grand Exchage during a 4-hour period. |
| isTradeable | Boolean | Whether the object can be traded between players and to shops. |
| quests | [ [QuestType](questtype.md) ] | A list of all quests related to this config. |
| groundOpNames | [ String ] | A list of names displayed for the available ops when the object is shown on the ground.Use `pairs()` to iterate this list, which will provide both the op index and name as `opIndex,opName`. |
| interfaceOpNames | [ String ] | A list of names displayed for the available ops when the object is shown in an interface component.Use `pairs()` to iterate this list, which will provide both the op index and name as `opIndex,opName`. |
| stackCountAltObjs | [ [ Integer, [Obj](objtype.md) ] ] | A list of `[ count, config ]` pairs used to select which `ObjType` config is used to draw the current object.The list is iterated over, and selected the last pair the input `count` was `>=` to.This list will be empty if there are no alt configs. |
| params | [ [ParamType](paramtype.md) ] | Returns a list of all the [ParamTypes](paramtype.md) stored in this config. |