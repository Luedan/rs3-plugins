# BaseAnimSetType

## Descripción General

A `BaseAnimSetType` config contains data about animation sets that are used by entities.

It is a collection of various animation [Seqs](seqtype.md), and additional data, for use when an entity performs common animations like walking or running.

These config types can be found within the `config.BaseAnimSet` table:

```lua
config.BaseAnimSet.HUMAN_WALK_ROPEBALANCE
config.BaseAnimSet["HUMAN_WALK_ROPEBALANCE"]
config.BaseAnimSet.FromID(1957) -- config.BaseAnimSet.HUMAN_WALK_ROPEBALANCE
```

> **Información**
> A `BaseAnimSetType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `BaseAnimSetType` includes:

* Overlay height offset
* [Seqs](seqtype.md) to use for various animations
* ... TODO

## Ejemplos

```lua
-- Access a BaseAnimSetType config directly by using its name
local balancecfg = config.BaseAnimSet.HUMAN_WALK_ROPEBALANCE
-- or by ID lookup
local balancecfg = config.BaseAnimSet.FromID(id.BaseAnimSet.HUMAN_WALK_ROPEBALANCE)
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
| configName | String | The name of this config, i.e. `"HUMAN_WALK_ROPEBALANCE"`. |
| typeName | String | The type of this config. Will always be `"BaseAnimSet"`. |
| overlayHeight | Integer | The height above the owning entity, in fine units, at which entity overlays like [Headbars](headbartype.md) and [Hitmarks](hitmarktype.md) are drawn. |