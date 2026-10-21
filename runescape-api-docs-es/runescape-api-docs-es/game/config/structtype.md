# StructType

## Descripción General

A `StructType` config provides a collection of data values, accessible by [ParamTypes](paramtype.md).

Each struct contains data where each separate input key is a [ParamType](paramtype.md) and the corresponding output value is a [ValueType](vartype.md#valuetype) matching that of the given param.

Input keys are unique within the config - the same [ParamType](paramtype.md) cannot exist in the same struct multiple times.

These config types can be found within the `config.Struct` table:

```lua
config.Struct.BOSS_INSTANCE_STALKER_BOSS
config.Struct["BOSS_INSTANCE_STALKER_BOSS"]
config.Struct.FromID(922) -- config.Struct.BOSS_INSTANCE_STALKER_BOSS
```

> **Información**
> An `StructType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `StructType` includes:

* [Param](paramtype.md) data stored

## Ejemplos

```lua
-- Access a StructType config directly by using its name
local bossCfg = config.Struct.BOSS_INSTANCE_STALKER_BOSS
-- or by ID lookup
local bossCfg = config.Struct.FromID(id.Struct.BOSS_INSTANCE_STALKER_BOSS)

-- Get values for some params contained in the struct
local bossName = config.Struct.BOSS_INSTANCE_STALKER_BOSS:GetParamValue(config.Param.BOSS_INSTANCE_BOSS_NAME) -- "Flesh-hatcher Mhekarnahz"
local bossNPC = config.Struct.BOSS_INSTANCE_STALKER_BOSS:GetParamValue(config.Param.BOSS_INSTANCE_BOSS_NPC) -- config.NPC.STALKER_BOSS

-- Iterate all data values
-- Values data is returned as an array of pairs, i.e. [ [ParamType, dataValue], [ParamType, dataValue], ... ]
local allParams = config.Struct.BOSS_INSTANCE_STALKER_BOSS.paramValues
for _,keyValuePair in ipairs(allParams) do
    local paramType = keyValuePair[1] -- config.Param.BOSS_INSTANCE_BOSS_NPC
    local paramValue = keyValuePair[2] -- config.NPC.STALKER_BOSS
end
```

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Métodos

### GetParamValue

```lua
function Struct:GetParamValue(param : ParamType) -> ?
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
> -- Get a boss name
> local name = config.Struct.BOSS_INSTANCE_STALKER_BOSS:GetParamValue(config.Param.BOSS_INSTANCE_BOSS_NAME) -- "Flesh-hatcher Mhekarnahz"
> -- And another few boss names in different structs using the same param
> local name2 = config.Struct.BOSS_INSTANCE_DINO_BOSS:GetParamValue(config.Param.BOSS_INSTANCE_BOSS_NAME) -- "Raksha"
> local name3 = config.Struct.BOSS_INSTANCE_GWD2_ZAROS:GetParamValue(config.Param.BOSS_INSTANCE_BOSS_NAME) -- "Vindicta & Gorvek"
> ```

### HasParam

```lua
function Struct:HasParam(param : ParamType) -> Boolean
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
> -- Get a boss name, if a param for it exists
> if config.Struct.BOSS_INSTANCE_STALKER_BOSS:HasParam(config.Param.BOSS_INSTANCE_BOSS_NAME) then
>     -- Get the param value
>     local name = config.Struct.BOSS_INSTANCE_STALKER_BOSS:GetParamValue(config.Param.BOSS_INSTANCE_BOSS_NAME)
> end
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"BOSS_INSTANCE_STALKER_BOSS"`. |
| typeName | String | The type of this config. Will always be `"Struct"`. |
| params | [ [ParamType](paramtype.md) ] | Returns a list of all the [ParamTypes](paramtype.md) stored in this config. |