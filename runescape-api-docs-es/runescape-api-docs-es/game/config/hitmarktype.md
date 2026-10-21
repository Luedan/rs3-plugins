# HitmarkType

## Descripción General

A `HitmarkType` config contains data about the various hitmark overlays that can be drawn above an entity.

These config types can be found within the `config.Hitmark` table:

```lua
config.Hitmark.MAGIC_DAMAGE
config.Hitmark["MAGIC_DAMAGE"]
config.Hitmark.FromID(2) -- config.Hitmark.MAGIC_DAMAGE
```

> **Información**
> A `HitmarkType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `HitmarkType` includes:

* Visibility duration
* ... TODO

## Ejemplos

```lua
-- Access a HitmarkType config directly by using its name
local splatcfg = config.Hitmark.MAGIC_DAMAGE
-- or by ID lookup
local splatcfg = config.Hitmark.FromID(id.Hitmark.MAGIC_DAMAGE)
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
| configName | String | The name of this config, i.e. `"MAGIC_DAMAGE"`. |
| typeName | String | The type of this config. Will always be `"Hitmark"`. |
| duration | Integer | How long, in client ticks, the hitmark will display for. |