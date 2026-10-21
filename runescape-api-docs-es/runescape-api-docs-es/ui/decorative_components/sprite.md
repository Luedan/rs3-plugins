# ui.Sprite

## Descripción General

[ui.Component](./../component.md) -> ui.Sprite

Decorative component that simply draws an image onto the screen.

This is mostly an extension of [ui.SpriteData](./../common_types.md#uispritedata), with the only functionality besides what's provided by that and by `Component` being functionality to associate this component with an object, making it so the object's model is drawn instead of the normal component contents.

> **Advertencia**
> These components don't currently support segmented sprites, with the `visualMargin` property getting ignored.

## Ejemplo

```lua
local sprite = ui.Sprite.new(parent)
sprite:SetSize(100, 50)
sprite.sprite = Plugin.resources.my_sprite
-- or
sprite.sprite = builtin_sprite_id_to_use
sprite.colour = Vector4.new(1.0, 0.0, 1.0, 1.0)
```

## Enumeraciones

### ui.ObjectQuantityDisplayMode

Enumeration identifying how the quantity of an associated object should be displayed on a sprite with an associated object.

> **Información**
> The font used for the quantity indicator is currently hardcoded.

| Valor | Descripción |
| --- | --- |
| NEVER | The quantity indicator is never displayed. |
| ALWAYS | The quantity indicator is always displayed. |
| MULTIPLE | The quantity indicator is displayed if there's more than one object in the stack. |

## Métodos

### Constructor

```lua
function ui.Sprite.new(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> Sprite
```

Creates a new sprite component on the specified parent.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this sprite component in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| Sprite | The newly created sprite component.    The caller must set its layout and visual information afterwards. |

### SetAssociatedObject

```lua
function ui.Sprite:SetAssociatedObject(objectID : Int, quantity : Uint64?)
```

Associates an object with this component, making it use the object's name and optionally it's quantity as the displayed contents for this component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| objectID | Int | Numeric ID for the object to associate with this component. |
| quantity | Uint64? | The quantity for the object to associate with this component. |

### AlignTo

```lua
function ui.Sprite:AlignTo(alignment : ui.AlignMode)
function ui.Sprite:AlignTo(horizontalAlignment : ui.AlignMode, verticalAlignment : ui.AlignMode)
```

Sets the alignment for this sprite.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| alignment | [ui.AlignMode](./../common_types.md#uialignmode) | The alignment to set as both horizontal and vertical alignments. |
| horizontalAlignment | [ui.AlignMode](./../common_types.md#uialignmode) | The desired horizontal alignment. |
| verticalAlignment | [ui.AlignMode](./../common_types.md#uialignmode) | The desired vertical alignment. |

### SetConfig

```lua
function ui.Sprite:SetConfig(config : ui.SpriteDataConfig)
```

Sets this Sprite's properties based on the provided config values.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| config | ui.SpriteDataConfig | The config to source the various properties from. |

### GetConfigCopy

```lua
function ui.Sprite:GetConfigCopy() -> ui.SpriteDataConfig
```

Returns a copy of this Sprite's config, allowing it to be used elsewhere.

| Retorna | Descripción |
| --- | --- |
| ui.SpriteDataConfig | Config containing a copy of all properties set on this Sprite object, excluding non-config properties (eg. `content`) |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| associatedObjectID | Int | Numeric ID for the object associated with this component, or -1 if no associated object exists. |
| associatedObjectQuantity | Int | The quantity for the object associated with this component. |
| associatedObjectQuantityMode | [ui.ObjectQuantityDisplayMode](#uiobjectquantitydisplaymode) | Specifies when the label listing the quantity for the associated object should be displayed. |
| sprite | Int | [RuntimeSprite](./../common_types.md#runtimesprite) |
| spriteID | Int | Gets the built-in sprite ID to draw. |
| runtimeSprite | [RuntimeSprite](./../common_types.md#runtimesprite) | Gets the current runtime sprite to draw or nil if it doesn't exist. |
| visualMargins | [ui.Margin](./../common_types.md#uimargin) | **(Modifiable Contents)**   Offsets used to split this sprite's graphics into multiple segments for drawing. |
| outlineWidth | Uint8 | Thickness of the sprite's outline.   Only used when the containing component is associated with an object. |
| rotationDegrees | Float | Rotation of this sprite in degrees. |
| rotationRadians | Float | Rotation of this sprite in radians. |
| isFlippedHorizontally | Bool | Flag indicating whether or not this sprite is drawn mirrored horizontally. |
| isFlippedVertical | Bool | Flag indicating whether or not this sprite is drawn mirrored vertical. |
| isTiling | Bool | Flag indicating whether or not this sprite uses tiled visuals. |
| shadowColour | [Vector4](./../../math/vector.md) | Colour used when drawing this sprite's shadow.   If alpha is 0, no shadow will be drawn. |
| shadowRGBA | Uint | Hex-encoded red/green/blue/alpha colour code used when drawing this sprite.   If alpha is 0, no shadow will be drawn. |