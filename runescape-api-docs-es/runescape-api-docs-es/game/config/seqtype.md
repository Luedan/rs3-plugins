# SeqType

## Descripción General

A `SeqType` config contains the playback data properties associated with a given animation's frames.

These config types can be found within the `config.Seq` table:

```lua
config.Seq.ARDRAGON_DRAGON_BASIC_ICE_ATTACK
config.Seq["ARDRAGON_DRAGON_BASIC_ICE_ATTACK"]
config.Seq.FromID(id.Seq.ARDRAGON_DRAGON_BASIC_ICE_ATTACK)
```

> **Información**
> A `SeqType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `SeqType` includes:

* Pre-animation and post-animation moves
* Frame, extras and delay data
* Length and loop properties

```lua
-- Access a SeqType config directly by using its name
local iceAtkCfg = config.Seq.ARDRAGON_DRAGON_BASIC_ICE_ATTACK
-- or by ID lookup
local iceAtkCfg = config.Seq.FromID(id.Seq.ARDRAGON_DRAGON_BASIC_ICE_ATTACK)
```

## Enumeraciones

### PreAnimMove

| Name | Value |
| --- | --- |
| DELAY_MOVE | 0 |
| DELAY_ANIMATION | 1 |
| MOVE_MERGE | 2 |
| ABORT_ANIMATION | 3 |
| DEFAULT | 4 |

### PostAnimMove

| Name | Value |
| --- | --- |
| DELAY_MOVE | 0 |
| ABORT_ANIMATION | 1 |
| MOVE_MERGE | 2 |
| DEFAULT | 3 |

### AnimationDuplicateBehaviour

| Name | Value |
| --- | --- |
| CONTINUE | 0 |
| RESET | 1 |
| LOOP_RESET | 2 |

## Métodos

### GetParamValue

```lua
function Seq:GetParamValue(param : ParamType) -> ?
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
> Seqal value = config.Seq.ARDRAGON_DRAGON_BASIC_ICE_ATTACK:GetParamValue(config.Param.ELR1_NAME_PLURAL) -- "wooden tortems"
> ```

### HasParam

```lua
function Seq:HasParam(param : ParamType) -> Boolean
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
> if config.Seq.ARDRAGON_DRAGON_BASIC_ICE_ATTACK:HasParam(config.Param.PROJECTILE_START_TIME) then
>     -- Get the param value
>     Integer value = config.Seq.ARDRAGON_DRAGON_BASIC_ICE_ATTACK:GetParamValue(config.Param.PROJECTILE_START_TIME)
> end
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"ARDRAGON_DRAGON_BASIC_ICE_ATTACK"`. |
| typeName | String | The type of this config. Will always be `"Seq"`. |
| preAnimMove | [PreAnimMove](#preanimmove) | Behaviour of the animation if the entity is moving when it starts playing. |
| postAnimMove | [PostAnimMove](#postanimmove) | Behaviour of the animation if the entity is wants to move after it starts playing. |
| length | Integer | Number of client ticks the associated animation will run for. |
| loop | Integer | How many more loops the animation will run for. |
| priority | Integer | Priority of the animation. Higher is more important. |
| replaceHeldLeft | [Obj](objtype.md) | Object of what to replace the entity's left hand is holding with. |
| replaceHeldRight | [Obj](objtype.md) | Object of what to replace the entity's right hand is holding with. |
| maxLoop | Integer | Maximum number of loops this animation can run for. |
| animDuplicateBehaviour | [AnimationDuplicateBehaviour](#animationduplicatebehaviour) | Determines what happens if the same animation is requested to be played while it is already being played. |