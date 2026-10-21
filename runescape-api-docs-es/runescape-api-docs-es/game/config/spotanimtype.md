# SpotAnimType

## Descripción General

An `SpotAnimType` config contains the descriptive data necessary for the game to construct a `SpotAnimEntity`.

These config types can be found within the `config.SpotAnim` table:

```lua
config.SpotAnim.TELEGRAB_IMPACT
config.SpotAnim["TELEGRAB_IMPACT"]
config.SpotAnim.FromID(144) -- config.SpotAnim.TELEGRAB_IMPACT
```

> **Información**
> A `SpotAnimType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `SpotAnimType` includes:

* The animation [SeqType](seqtype.md) to play
* ... TODO

## Ejemplos

```lua
-- Access a SpotAnimType config directly by using its name
local spotcfg = config.SpotAnim.TELEGRAB_IMPACT
-- or by ID lookup
local spotcfg = config.SpotAnim.FromID(id.SpotAnim.TELEGRAB_IMPACT)
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
| configName | String | The name of this config, i.e. `"TELEGRAB_IMPACT"`. |
| typeName | String | The type of this config. Will always be `"SpotAnim"`. |
| seqID | Integer | The ID of the [SeqType](seqtype.md) to play with this spotanim. |