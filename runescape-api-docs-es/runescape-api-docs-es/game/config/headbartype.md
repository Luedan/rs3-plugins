# HeadbarType

## Descripción General

A `HeadbarType` config contains data about the various headbar overlays that can be drawn above an entity.

These config types can be found within the `config.Headbar` table:

```lua
config.Headbar.ADRENALINE_DEFAULT
config.Headbar["ADRENALINE_DEFAULT"]
config.Headbar.FromID(7) -- config.Headbar.ADRENALINE_DEFAULT
```

> **Información**
> A `HeadbarType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `HeadbarType` includes:

* The display order
* ... TODO

## Ejemplos

```lua
-- Access a HeadbarType config directly by using its name
local adrencfg = config.Headbar.ADRENALINE_DEFAULT
-- or by ID lookup
local adrencfg = config.Headbar.FromID(id.Headbar.ADRENALINE_DEFAULT)
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
| configName | String | The name of this config, i.e. `"ADRENALINE_DEFAULT"`. |
| typeName | String | The type of this config. Will always be `"Headbar"`. |
| displayOrder | Integer | The draw order of the headbar.Headbars are drawn from bottom-upwards. A higher value draws later. |