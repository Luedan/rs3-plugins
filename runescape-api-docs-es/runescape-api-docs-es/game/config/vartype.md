# VarType

## Descripción General

A `VarType` config contains information about one of variables used by the game.

Variables belong to one of several different domains, such as:

| Domain | Description |
| --- | --- |
| VarClient | Exists on the local game client, although the server is able to set its value remotely. |
| VarPlayer | Variables which are stored in the player character's savegame. |
| VarPlayerGroup | Currently unavailable |
| VarClan | Currently unavailable |
| VarClanSettings | Currently unavailable |
| VarNPC | TODO |
| VarObj | TODO |

All domain types other than `VarClient` exist on the server.

> **Información**
> A server variable may optionally transmit its value to the client, allowing the API to access it.
As a result, not all variables (or their names) are available to the API.

Variables can be one of many different value types:

* Integer (32-bit)
* Long (64-bit)
* String
* [CoordGrid](../coordgrid.md)
* [NPCType](npctype.md), [LocType](loctype.md), etc config
* and more

See [ValueType](#valuetype) for a full list of all supported types.

These config types can be found within the `var` table, and then further within the domain sub-table:

```lua
var.VarClient.TOOLTIP_TIME
var.VarPlayer["COMBATV2_MELEE_DEFENCE"]
var.VarPlayer.FromID(456) -- var.VarPlayer.OPTION_CHAT
```

> **Información**
> A `VarType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

## VarBit

The default data type for a variable is a 32-bit Integer, which allows for values from -2147483648 to 2147483647.
Some variables do not need this much value range, meaning that much of the underlying data space is wasted.

To improve efficiency, several `VarBits` can share one variable data space.
A `VarBit` reserves a sub-section of its base variable, using only the data it needs.

Below is an example of several `VarBits` sharing one base variable.

| BaseVar |  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VarBit1 |  | x | x | x | x | x | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| VarBit2 |  |  |  |  |  |  |  |  |  | x | x | x | x | x |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| VarBit3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | x | x | x | x | x | x | x | x | x | x |  |  |

*VarBit1* uses 8 bits (`varBitMask = 255, 0xFF, 0b11111111`), making its value range 0 -> 255
*VarBit2* uses 5 bits (`varBitMask = 7936, 0x1F00, 0b1111100000000`), making its value range 0 -> 31
*VarBit3* uses 12 bits (`varBitMask = 1073479680, 0x3FFC0000, 0b111111111111000000000000000000`), making its value range 0 -> 4095

`VarBit` values can **only** be positive (unsigned) Integers.
As shown, `VarBits` do not need to be contiguous, i.e. gaps can be left between the bits they use.

When a `VarBit` value is changed, it changes the data in the underlying base variable.
Additionally, when the base variable is changed, it can change the value of any `VarBits` that use it. This is often used to reset a number of `VarBits` at the same time.

> **Información**
> The property `VarType.isVarBit` can be used to determine whether a variable is a `VarBit`.
`VarBit` IDs are also negative:
> ```lua
> id.VarPlayer.OPTION_TOGGLE1 -- ID: 5967
>     id.VarPlayer.FRIEND_SORT_MODE -- ID: -30174, uses bits 3-5 of VarPlayer.OPTION_TOGGLE1
> ```

## Enumeraciones

### ValueType

A list of all the possible value types and the data type they correspond to.

| Name | Value | Value Data Type |
| --- | --- | --- |
| UNSUPPORTED | -1 | nil |
| ACHIEVEMENT | 131 | [AchievementType](achievementtype.md) |
| AREA | 16 | TODO |
| BASEANIMSET | 44 | [BasAnimSetType](baseanimsettype.md) |
| BOOLEAN | 1 | Boolean |
| CATEGORY | 41 | Integer |
| CHAR | 42 | Integer |
| CHATCAT | 29 | Integer |
| CHATPHRASE | 24 | Integer |
| COMPONENT | 9 | [Component](../../ui/component.md) |
| COORDGRID | 22 | [CoordGrid](../coordgrid.md) |
| CURSOR | 5 | [CursorType](cursortype.md) |
| CUTSCENE2D | 138 | Integer |
| DBTABLE | 129 | [DBTable](dbtabletype.md) |
| DBROW | 74 | [DBRow](dbrowtype.md) |
| ENUM | 26 | [EnumType](enumtype.md) |
| FONT | 25 | [Font](fonttype.md) |
| HITMARK | 62 | [HitmarkType](hitmarktype.md) |
| IDKIT | 10 | Integer |
| INTEGER | 0 | Integer |
| INV | 39 | [InvType](invtype.md) |
| LOC | 30 | [LocType](loctype.md) |
| LONG | 110 | Long |
| MAPELEMENT | 59 | Integer |
| MATERIAL | 102 | Integer |
| MODEL | 31 | Integer |
| NPC | 32 | [NPCType](npctype.md) |
| NPC_UID | 38 | Integer |
| OBJ | 33 | [ObjType](objtype.md) |
| OVERLAYINTERFACE | 99 | Integer |
| PLAYER_UID | 34 | Integer |
| QUEST | 3 | [QuestType](questtype.md) |
| SEQ | 6 | Integer |
| SPOTANIM | 37 | [SpotAnimType](spotanimtype.md) |
| SKILL | 17 | [SkillType](../player.md#skilltype) |
| SPRITE | 23 | Integer |
| STRING | 36 | String |
| STRUCT | 73 | [StructType](structtype.md) |
| SYNTH | 14 | Integer |
| VAR_INT | 209 | Integer |
| VORBIS | 57 | Integer |

## Ejemplos

```lua
-- Access a VarType directly by using its name
local sortVar = var.VarPlayer.FRIEND_SORT_MODE
-- or by ID lookup
local sortVar = var.VarPlayer.FromID(id.VarPlayer.FRIEND_SORT_MODE)

-- Obtain the value and value type using
local sortValueType = sortVar.valueType
local sortMode = sortVar.value
-- or
local sortValueType = var.VarPlayer.FRIEND_SORT_MODE.valueType
local sortMode = var.VarPlayer.FRIEND_SORT_MODE.value
```

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"FRIEND_SORT_MODE"`. |
| typeName | String | The type of this config. Will one of `"VarClient"`, `"VarPlayer"`, `"VarPlayerGroup"`, `"VarClan"`, `"VarClanSettings"`, `"VarNPC"` or `"VarObj"`. |
| value | ? | Devuelve el/la value of this variable config actual.The value data type [ValueType](#valuetype) is provided by `valueType`. |
| valueType | [ValueType](#valuetype) | The expected type of data this variable will return. |
| isVarBit | Boolean | Whether this config type is a `VarBit`. |
| baseVar | `VarType` | Returns the base `VarType`, if this config is a `VarBit`.Otherwise returns `nil`. |
| varBitMask | Integer | Returns a bitmask showing the range of bits used, if this config is a `VarBit`.Otherwise returns `nil`.A `VarBit` using bits 3-5 would return a value of `56` (`0x38`, `0b111000`). |