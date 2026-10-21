# Common Types

## Descripción General

The types listed here represent core types used throughout the UI system.

## Tipos

### ui.Pos

Used to represent positions, taking into account absolute horizontal and vertical offsets, as well as a specific percent of an arbitrary parent component's width and height, and a component's own width and height.

Since position objects just store offsets and percentages, it's only when associated with a component that they can be used to calculate a *final* position value.

> **Información**
> The resulting position is calculated as `position = x/y + xParentPc/yParentPc * <parentWidth>/<parentHeight> + xSelfPc/ySelfPc * <selfWidth>/<selfHeight>`

> **Ejemplo**
> ```lua
> -- Initialised to zeros
> local zero = ui.Pos.new()
> 
> -- Set to 50,-20
> local offsets = ui.Pos.new(50, -20)
> 
> -- Centred on the parent, with a 50,-20 offset
> local mixed = ui.Pos.new(50, -20, 0.5, 0.5)
> 
> -- Right-aligned on the parent, and centred vertically on itself
> local rightAligned = ui.Pos.new(0, 0, 1.0, 0.0, -1.0, 0.5)
> ```

#### Constructor

```lua
function ui.Pos.new() -> Pos
function ui.Pos.new(other : Pos) -> Pos
function ui.Pos.new(x : Int, y : Int) -> Pos
function ui.Pos.new(x : Int, y : Int, xParentPc : Float, yParentPc : Float) -> Pos
function ui.Pos.new(x : Int, y : Int, xParentPc : Float, yParentPc : Float, xSelfPc : Float, ySelfPc : Float) -> Pos
```

Creates a new position object.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| other | Pos | Position object to copy values from. |
| x | Int | Horizontal offset in interface units. |
| y | Int | Vertical offset in interface units. |
| xParentPc | Float | Percentage of the parent component's width to take into account for positioning. |
| yParentPc | Float | Percentage of the parent component's height to take into account for positioning. |
| xSelfPc | Float | Percentage of the component's width to take into account for positioning. |
| ySelfPc | Float | Percentage of the component's height to take into account for positioning. |

| Retorna | Descripción |
| --- | --- |
| Pos | The newly created position object. |

#### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| x | Int | Horizontal offset in interface units. |
| y | Int | Vertical offset in interface units. |
| xParentPc | Float | Percentage of the parent component's width to take into account for positioning. |
| yParentPc | Float | Percentage of the parent component's height to take into account for positioning. |
| xSelfPc | Float | Percentage of the component's width to take into account for positioning. |
| ySelfPc | Float | Percentage of the component's height to take into account for positioning. |

### ui.Size

Used to represent sizes, taking into account absolute horizontal and vertical offsets, as well as a specific percent of an arbitrary parent component's width and height, as well of a component's own width and height.

Since size objects just store offsets and percentages, it's only when associated with a component that they can be used to calculate a *final* size value.

> **Información**
> The resulting size is calculated as `size = width/height + widthParentPc/heightParentPc * <parentWidth>/<parentHeight>`

> **Ejemplo**
> ```lua
> -- Initialised to zeros
> local zero = ui.SizePos.new()
> 
> -- Set to 50,20
> local offsets = ui.Size.new(50, 20)
> 
> -- Covering 50% of the parent's area, plus 50 units horizontally, and shrunk vertically by 20 units
> local mixed = ui.Size.new(50, -20, 0.5, 0.5)
> 
> -- Spans the entire parent horizontally, with a 50 interface unit height
> local spanHorizontal = ui.Size.new(0, 50, 1.0, 0.0)
> ```

#### Constructor

```lua
function ui.Size.new() -> Size
function ui.Size.new(other : Size) -> Size
function ui.Size.new(width : Int, height : Int) -> Size
function ui.Size.new(width : Int, height : Int, widthParentPc : Float, heightParentPc : Float) -> Size
```

Creates a new position object.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| other | Pos | Size object to copy values from. |
| width | Int | Width offset in interface units. |
| height | Int | Height offset in interface units. |
| widthParentPc | Float | Percentage of the parent component's width to take into account for sizing. |
| heightParentPc | Float | Percentage of the parent component's height to take into account for sizing. |

| Retorna | Descripción |
| --- | --- |
| Size | The newly created size object. |

#### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| width | Int | Width offset in interface units. |
| height | Int | Height offset in interface units. |
| widthParentPc | Float | Percentage of the parent component's width to take into account for sizing. |
| heightParentPc | Float | Percentage of the parent component's height to take into account for sizing. |

### ui.TextData

Used to represent a text element within a UI component. These contain properties necessary for drawing text, as well as the actual text to draw.

#### ui.TextDataConfig

TextDataConfigs are simplified versions of TextData, containing only the properties necessary for drawing text, allowing them to be initialised separately and shared across components.

Essentially they contain all of the same properties and data, except the `content` property is omitted and no methods are available.

> **Ejemplo**
> ```lua
> local reusableTextCfg = ui.TextDataConfig.new()
> reusableTextCfg.font = museo_sans_15pt_regular
> reusableTextCfg.alignHorizontal = ui.AlignMode.CENTRE
> reusableTextCfg.alignVertical = ui.AlignMode.CENTRE
> reusableTextCfg.colour = Vector4.new(0.0, 1.0, 0.7, 1.0)
> 
> aComponent.text:SetConfig(reusableTextCfg)
> anotherComponent.text:SetConfig(reusableTextCfg)
> ```

#### Métodos

##### AlignTo

```lua
function ui.TextData:AlignTo(alignment : ui.AlignMode)
function ui.TextData:AlignTo(horizontalAlignment : ui.AlignMode, verticalAlignment : ui.AlignMode)
```

Sets the alignment for this text.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| alignment | [ui.AlignMode](#uialignmode) | The alignment to set as both horizontal and vertical alignments. |
| horizontalAlignment | [ui.AlignMode](#uialignmode) | The desired horizontal alignment. |
| verticalAlignment | [ui.AlignMode](#uialignmode) | The desired vertical alignment. |

##### SetConfig

```lua
function ui.TextData:SetConfig(config : ui.TextDataConfig)
```

Sets this TextData's properties based on the provided config values.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| config | ui.TextDataConfig | The config to source the various properties from. |

##### GetConfigCopy

```lua
function ui.TextData:GetConfigCopy() -> ui.TextDataConfig
```

Returns a copy of this TextData's config, allowing it to be used elsewhere.

| Retorna | Descripción |
| --- | --- |
| ui.TextDataConfig | Config containing a copy of all properties set on this TextData object, excluding non-config properties (eg. `content`) |

#### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| content | String | The text to draw. |
| font | Int | The font to use when drawing this text. |
| lineSpacing | Uint8 | Spacing between text lines in interface units.   Defaults to the font's spacing if set to zero. |
| alignHorizontal | [ui.AlignMode](#uialignmode) | Horizontal alignment for this text. |
| alignVertical | [ui.AlignMode](#uialignmode) | Vertical alignment for this text. |
| maxLines | Uint8 | Maximum number of lines to display.   Can be set to 0 to allow an unlimited number of lines. |
| alpha | Float | Visibility for this text, ranging from 0 (fully transparent) to 1 (opaque). |
| colour | [Vector4](./../../math/vector.md) | Colour used when drawing this text. |
| rgba | Uint | Hex-encoded red/green/blue/alpha colour code used when drawing this text. |
| shadowColour | [Vector4](./../../math/vector.md) | Colour used when drawing this text's shadow if enabled. |
| shadowRGBA | Uint | Hex-encoded red/green/blue/alpha colour code used when drawing this text's shadow if enabled. |
| isShadowed | Bool | Whether or not to draw this text with a shadow effect for better legibility.   Defaults to false. |

### ui.SpriteData

Used to represent a sprite element within a UI component. These contain properties necessary for drawing sprite, as well as the actual sprite resource to draw.

Sprite resources can contained tiled visuals, or be split into multiple segments, up to a 3x3 segmented sprite, containing segments for the four sides, the 4 corners, and the centre region.

> **Información**
> Unless they're tiled, sprite visuals will be stretched to occupy the region provided by the component containing that sprite.
> This is particularly important when using segmented sprites, since for a 3x3 sprite the corners don't get stretched at all, the edges get stretched in one direction only (for example, left and right edges stretch vertically), and the centre segment stretches as normal.

> **Información**
> Prefer using segmented sprites and tiling for sprites used for functional elements such as buttons, and limiting non-tiled and non-segmented sprites to decorative elements.

#### ui.SpriteDataConfig

SpriteDataConfigs are simplified versions of SpriteData, containing only the properties necessary for drawing a sprite, allowing them to be initialised separately and shared across components.

Essentially they contain all of the same properties and data, except the `sprite`, `spriteID`, and `runtimeSprite` properties are omitted and no methods are available.

#### RuntimeSprite

An opaque object representing a sprite generated at runtime.

These are generally sprites representing objects associated with the containing components, such as those used for inventory icons.

#### Image Layout

Sprites can be split into segments via the `visualMargin` property.

For example by specifying left and right margins you obtain a 3x1 segments sprite, with the left and right segments having a fixed width and stretching vertically, while the middle one stretches horizontally and vertically:

![A sprite sliced into three segments horizontally](images/sprite_slice_example_1.png)

While by specifying top and bottom margins you obtain a 1x3 segments sprite, with the top and bottom segments having a fixed height and stretch horizontally, while the middle one stretches horizontally and vertically:

![A sprite sliced into three segments vertically](images/sprite_slice_example_2.png)

Or you can specify all margins, resulting in a 3x3 segments sprite, where the corners don't stretch at all, and the edges stretch only in one direction, while the middle segment stretches horizontally and vertically:

![A sprite sliced into a 3x3 collection of segments](images/sprite_slice_example_3.png)

#### Métodos

##### SetConfig

```lua
function ui.SpriteData:SetConfig(config : ui.SpriteDataConfig)
```

Sets this SpriteData's properties based on the provided config values.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| config | ui.SpriteDataConfig | The config to source the various properties from. |

##### GetConfigCopy

```lua
function ui.SpriteData:GetConfigCopy() -> ui.SpriteDataConfig
```

Returns a copy of this SpriteData's config, allowing it to be used elsewhere.

| Retorna | Descripción |
| --- | --- |
| ui.SpriteDataConfig | Config containing a copy of all properties set on this SpriteData object, excluding non-config properties (eg. `content`) |

#### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| sprite | Int | [RuntimeSprite](#runtimesprite) |
| spriteID | Int | Gets the built-in sprite ID to draw. |
| runtimeSprite | [RuntimeSprite](#runtimesprite) | Gets the current runtime sprite to draw or nil if it doesn't exist. |
| visualMargins | [ui.Margin](#uimargin) | **(Modifiable Contents)**   Offsets used to split this sprite's graphics into multiple segments for drawing.   See [image layout](#image-layout) for information on how they're used. |
| outlineWidth | Uint8 | Thickness of the sprite's outline.   Only used when the containing component is associated with an object. |
| rotationRadians | Float | Rotation of this sprite in radians. |
| rotationDegrees | Float | Rotation of this sprite in degrees. |
| alpha | Float | Visibility for this sprite, ranging from 0 (fully transparent) to 1 (opaque). |
| colour | [Vector4](./../../math/vector.md) | Colour used when drawing this sprite. |
| rgba | Uint | Hex-encoded red/green/blue/alpha colour code used when drawing this sprite. |
| shadowColour | [Vector4](./../../math/vector.md) | Colour used when drawing this sprite's shadow.   If alpha is 0, no shadow will be drawn. |
| shadowRGBA | Uint | Hex-encoded red/green/blue/alpha colour code used when drawing this sprite.   If alpha is 0, no shadow will be drawn. |
| isFlippedHorizontally | Bool | Flag indicating whether or not this sprite is drawn mirrored horizontally. |
| isFlippedVertical | Bool | Flag indicating whether or not this sprite is drawn mirrored vertical. |
| isTiling | Bool | Flag indicating whether or not this sprite uses tiled visuals. |

### ui.Margin

Margins are used to represent distances from the sides of a region.

They're commonly used when defining slices for 3x3 sprites, or specifying the content regions for UI components.

#### Constructors

```lua
function ui.Margin.new() -> Margin
function ui.Margin.new(allSides : uint8) -> Margin
function ui.Margin.new(left : uint8, top : uint8, right : uint8, bottom : uint8) -> Margin
```

Constructs a new margin object with the provided values, or with all sides initialised to zero if omitted.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| allSides | Uint8 | Distance in interface units to set for all edges. |
| left | Uint8 | Distance from the left edge in interface units for this margin. |
| top | Uint8 | Distance from the top edge in interface units for this margin. |
| right | Uint8 | Distance from the right edge in interface units for this margin. |
| bottom | Uint8 | Distance from the bottom edge in interface units for this margin. |

| Retorna | Descripción |
| --- | --- |
| Margin | Resulting margin object. |

#### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| left | Uint8 | Distance from the left edge in interface units for this margin. |
| top | Uint8 | Distance from the top edge in interface units for this margin. |
| right | Uint8 | Distance from the right edge in interface units for this margin. |
| bottom | Uint8 | Distance from the bottom edge in interface units for this margin. |

### ui.ScrollBar

Provides controls for scrolling a component's contents.

> **Información**
> Custom sprites are supported, however note that for `handleSprite` and `backgroundSprite`, you must supply a sprite containing the following visual states in a vertical layout - `default/idle`, `mouseover`, `pressed`, `disabled`.

#### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| size | Uint8 | The scrollbar's size, representing width or height depending on whether it's a vertical or a horizontal scrollbar, respectively. |
| visible | Bool | Controls whether the scrollbar is visible or not.   Defaults to true. |
| autohide | Bool | Controls whether the scrollbar only appears to the user when required by the component where the scrollbar resides.   For example, an input field may hide the scrollbar until the contents exceed the input field's visible region.   Note this doesn't affect the value of `visible`, as that controls whether the scrollbar can ever appear to the user.   Defaults to true. |
| buttonLength | Uint8 | The length of the scrollbar's buttons, representing height or width depending on whether it's a vertical or a horizontal scrollbar.   Can be set to `0` to remove the buttons. |
| backgroundSprite | [ui.SpriteData](#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the background. |
| buttonSprite | [ui.SpriteData](#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the scrollbar's buttons. |
| handleSprite | [ui.SpriteData](#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the scrollbar's draggable handle. |

## Enumeraciones

### ui.ComponentType

Enumeration representing a component's type.

| Valor | Descripción |
| --- | --- |
| LINE | A line component. |
| RECTANGLE | A rectangle component. |
| LABEL | A text component. |
| SPRITE | A sprite component. |
| MODEL | A model component. |
| MODEL_GROUP | A model group component. |
| RADIAL_PROGRESS_OVERLAY | A radial progress overlay component. |
| CUTSCENE_LAYER | A cutscene layer component. |
| CANVAS | A canvas component. |
| BUTTON | A button component. |
| CHECK | A check component. |
| LIST | A list component. |
| INPUTFIELD | An input field component. |
| SLIDER | A slider component. |
| COMBO | A combo field component. |
| PAGED_LAYER_HEADER | A paged layer header component. |
| CAROUSEL | A carousel component. |
| PAGED_CAROUSEL | A paged carousel component. |
| RADIO_GROUP | A radio group component. |
| LAYER | A layer component. |
| PANEL | A panel component. |
| GRID | A grid component. |
| PAGED_LAYER | A paged layer component. |
| GROUP_BOX | A groupbox component. |

### ui.AlignMode

Enumeration identifying how an element should be aligned.

| Valor | Descripción |
| --- | --- |
| TOPLEFT | This element will be aligned to the top-left corner. |
| CENTRE | This element will be aligned to the centre. |
| BOTTOMRIGHT | This element will be aligned to the bottom-right corner. |
| JUSTIFY | This element will be aligned to the top-left corner, and justified so as to occupy the full width if possible. |

### ui.AspectRatioMode

Enumeration identifying how an element should be scaled based on its aspect ratio.

| Valor | Descripción |
| --- | --- |
| NO_SCALING | This element will ignore aspect ratio settings. |
| SCALE_WIDTH | This element will stretch horizontally so it matches its target aspect ratio. |
| SCALE_HEIGHT | This element will stretch vertically so it matches its target aspect ratio. |