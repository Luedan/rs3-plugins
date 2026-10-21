# CursorType

## Descripción General

A `CursorType` config contains information about one of custom cursor used by the game.

These config types can be found within the `config.Cursor` table:

```lua
config.Cursor.CURSOR_INCITE_FEAR
config.Cursor["CURSOR_READ"]
config.Cursor.FromID(123) -- config.Cursor.CURSOR_SMOKE_BARRAGE
```

> **Información**
> A `CursorType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `CursorType` includes:

* Hotspot X & Y
* Sprite ID

> **Información**
> A cursor hotspot is the pixel inside the source sprite where the 'click' happens.This is usually aligned to the tip of a finger or arrow, etc.

## Ejemplos

```lua
-- Access a CursorType config directly by using its name
local unlockCfg = config.Cursor.CURSOR_UNLOCK
-- or by ID lookup
local unlockCfg = config.Cursor.FromID(id.Cursor.CURSOR_UNLOCK)

-- Discover the sprite name using
local spriteName = id.Sprite.FromID(unlockCfg.spriteID)
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
| configName | String | The name of this config, i.e. `"CURSOR_UNLOCK"`. |
| typeName | String | The type of this config. Will always be `"Cursor"`. |
| hotspotX | Integer | The horizontal pixel inside the source sprite where clicks are centred. |
| hotspotY | Integer | The vertical pixel inside the source sprite where clicks are centred. |
| spriteID | Integer | The ID of the source sprite. |