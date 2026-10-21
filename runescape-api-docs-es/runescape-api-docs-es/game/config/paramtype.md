# ParamType

## Descripción General

A `ParamType` config provides a way to retrieve named data from other data structures.

Params do not contain the value itself, only the default value to return when a data structure does not contain a value for that param.

For example, [ObjType](objtype.md) configs for armour items may contain data for `config.Param.DEFEND_SOUND_1`, with each config returning a different sound ID value to play.

Data structures that contain params, or provide methods using params, are:

* [StructType](structtype.md)
* [DBTableType](dbtabletype.md)
* [DBRowType](dbrowtype.md)
* [ObjType](objtype.md)
* [NPCType](npctype.md)
* [LocType](loctype.md)
* [SeqType](seqtype.md)

These config types can be found within the `config.Param` table:

```lua
config.Param.DEFEND_SOUND_1
config.Param["DEFEND_SOUND_1"]
config.Param.FromID(240) -- config.Param.DEFEND_SOUND_1
```

> **Información**
> An `ParamType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `ParamType` includes:

* [ValueType](vartype.md#valuetype)
* Default value

## Ejemplos

```lua
-- Access an ParamType config directly by using its name
local paramCfg = config.Param.DEFEND_SOUND_1
-- or by ID lookup
local paramCfg = config.Param.FromID(id.Param.DEFEND_SOUND_1)
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
| configName | String | The name of this config, i.e. `"DEFEND_SOUND_1"`. |
| typeName | String | The type of this config. Will always be `"Param"`. |
| valueType | [ValueType](vartype.md#valuetype) | The expected type of data this param will return. |
| defaultValue | ? | Returns the default value of this param config.The value data type [ValueType](vartype.md#valuetype) is provided by `valueType`.If the param does not exist within the data structure being used, this is the value which will be returned. |