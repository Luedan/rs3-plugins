# ui.Text

## Descripción General

[ui.Component](./../component.md) -> ui.Text

Decorative component that simply draws a text string onto the screen.

This is mostly an extension of [ui.TextData](./../common_types.md#uitextdata), with the only functionality besides what's provided by that and by `Component` being functionality to associate this component with an object, making it so the object's name is drawn instead of the normal component contents.

## Ejemplo

```lua
local label = ui.Text.new(parent)
label:AlignTo(ui.AlignMode.CENTRE)
label:SetSize(100, 50)
label.content = "Hello World"
label.font = my_font_id
label.colour = Vector4.new(1.0, 0.0, 1.0, 1.0)
```

## Métodos

### Constructor

```lua
function ui.Text.new(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> Text
```

Creates a new text component on the specified parent.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this text component in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| Text | The newly created text component.    The caller must set its layout and visual information afterwards. |

### SetAssociatedObject

```lua
function ui.Text:SetAssociatedObject(objectID : Int, quantity : Uint64?)
```

Associates an object with this component, making it use the object's name and optionally it's quantity as the displayed contents for this component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| objectID | Int | Numeric ID for the object to associate with this component. |
| quantity | Uint64? | The quantity for the object to associate with this component. |

### AlignTo

```lua
function ui.Text:AlignTo(alignment : ui.AlignMode)
function ui.Text:AlignTo(horizontalAlignment : ui.AlignMode, verticalAlignment : ui.AlignMode)
```

Sets the alignment for this text.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| alignment | [ui.AlignMode](./../common_types.md#uialignmode) | The alignment to set as both horizontal and vertical alignments. |
| horizontalAlignment | [ui.AlignMode](./../common_types.md#uialignmode) | The desired horizontal alignment. |
| verticalAlignment | [ui.AlignMode](./../common_types.md#uialignmode) | The desired vertical alignment. |

### SetConfig

```lua
function ui.Text:SetConfig(config : ui.TextDataConfig)
```

Sets this Text's properties based on the provided config values.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| config | ui.TextDataConfig | The config to source the various properties from. |

### GetConfigCopy

```lua
function ui.Text:GetConfigCopy() -> ui.TextDataConfig
```

Returns a copy of this Text's config, allowing it to be used elsewhere.

| Retorna | Descripción |
| --- | --- |
| ui.TextDataConfig | Config containing a copy of all properties set on this Text object, excluding non-config properties (eg. `content`) |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| associatedObjectID | Int | Numeric ID for the object associated with this component, or -1 if no associated object exists. |
| associatedObjectQuantity | Int | The quantity for the object associated with this component. |
| content | String | The text to draw. |
| font | Int | The font to use when drawing this text. |
| lineSpacing | Uint8 | Spacing between text lines in interface units.   Defaults to the font's spacing if set to zero. |
| alignHorizontal | [ui.AlignMode](./../common_types.md#uialignmode) | Horizontal alignment for this text. |
| alignVertical | [ui.AlignMode](./../common_types.md#uialignmode) | Vertical alignment for this text. |
| maxLines | Uint8 | Maximum number of lines to display.   Can be set to 0 to allow an unlimited number of lines. |
| shadowColour | [Vector4](./../../math/vector.md) | Colour used when drawing this text's shadow if enabled. |
| shadowRGBA | Uint | Hex-encoded red/green/blue/alpha colour code used when drawing this text's shadow if enabled. |
| isShadowed | Bool | Whether or not to draw this text with a shadow effect for better legibility.   Defaults to false. |