# MapElementType

## Descripción General

A `MapElementType` config contains the data required for the map to display information about an element of the world.

These config types are found within the `config.MapElement` table:

```lua
config.MapElement.DINO_GAME_ICON_1
config.MapElement["DINO_GAME_ICON_1"]
config.MapElement.FromID(id.MapElement.DINO_GAME_ICON_1) -- config.MapElement.DINO_GAME_ICON_1
```

> **Información**
> A `MapElementType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within a `MapElementType` includes:

* Text displayed for the config on the map
* References to sprite IDs for rendering on the map
* Text rendering properties
* Map element category
* Horizontal and vertical rendering alignment

## Ejemplos

```lua
-- Access a MapElementType config directly by using its name
local dinoGameIconCfg = config.MapElement.DINO_GAME_ICON_1
-- or by ID lookup
local dinoGameIconCfg = config.MapElement.FromID(id.MapElement.DINO_GAME_ICON_1)
```

## Enumeraciones

### MapElementHorizontalAlign

| Name | Valor | Descripción |
| --- | --- | --- |
| LEFT | 0 | Aligned to left-hand side. |
| CENTRE | 1 | Aligned to centre. |
| RIGHT | 2 | Aligned to right-hand side. |

### MapElementVerticalAlign

| Name | Valor | Descripción |
| --- | --- | --- |
| TOP | 0 | Aligned to top. |
| CENTRE | 1 | Aligned to top. |
| BOTTOM | 2 | Aligned to bottom. |

### MapElementTextSize

| Name | Valor | Descripción |
| --- | --- | --- |
| SMALL | 0 | Use small text size. |
| MEDIUM | 1 | Use medium text size. |
| LARGE | 2 | Use large text size. |

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Métodos

### GetParamValue

```lua
function MapElement:GetParamValue(param : ParamType) -> ?
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
> -- Get a value
> String value = config.MapElement.DINO_GAME_ICON_1:GetParamValue(config.Param.MEP_TOOLTIP) -- "Arcane apoterrasaur"
> ```

### HasParam

```lua
function MapElement:HasParam(param : ParamType) -> Boolean
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
> -- Get a value, if a param for it exists
> if config.MapElement.DINO_GAME_ICON_1:HasParam(config.Param.MEP_TOOLTIP) then
>     -- Get the param value
>     String value = config.MapElement.DINO_GAME_ICON_1:GetParamValue(config.Param.MEP_TOOLTIP)
> end
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"DINO_GAME_ICON_1"`. |
| typeName | String | The type of this config. Will always be `"MapElement"`. |
| listable | Boolean | Is this config listable. |
| spriteID | Integer | The ID of the sprite associated with the MapElement. |
| spriteMouseOverID | Integer | The ID of the sprite associated with the MapElement when a mouse hovers over it on the map. |
| text | String | The text displayed for this element on the map. |
| textColour | [Vector4](./../../math/vector.md) | The colour of the text displayed on the map. |
| textRGBA | Integer | The colour of the text displayed on the map as an integer. |
| textMouseOverColour | [Vector4](./../../math/vector.md) | The colour of the text displayed on the when a mouse hovers over it on the map. |
| textMouseOverRGBA | Integer | The colour of the text displayed on the when a mouse hovers over it on the map as an integer. |
| textSize | [MapElementTextSize](#mapelementtextsize) | The text size used to display the element's text on the map. |
| textOffsetX | Integer | The text offset on the X-axis used when displaying the element's text on the map. |
| textOffsetZ | Integer | The text offset on the Z-axis used when displaying the element's text on the map. |
| textBGFillColour | [Vector4](./../../math/vector.md) | The colour of the background for the text displayed on the map. |
| textBGFillRGBA | Integer | The colour of the background for the text displayed on the map as an integer. |
| textBGOutlineColour | [Vector4](./../../math/vector.md) | The colour of the background for the text displayed on the map. |
| textBGOutlineRGBA | Integer | The colour of the background outline for the text displayed on the when a mouse hovers over it on the map as an integer. |
| showOnMiniMap | Boolean | Is this config displayed on the minimap. |
| showOnMiniMap | Boolean | Is this config displayed on the world map. |
| category | Integer | The MapElement category this config is associated with. |
| subjectText | String | The text for the world map subject for the associated MapElement. |
| spriteID | Integer | The ID of the sprite associated with the MapElement when flashing on the map. |
| minimapIconScale | Integer | The icon scaling for the MapElement used when rendering it to the minimap. |
| alignHorizontal | [MapElementHorizontalAlign](#mapelementhorizontalalign) | The horizontal alignment of the MapElement. |
| alignVertical | [MapElementVerticalAlign](#mapelementverticalalign) | The vertical alignment of the MapElement. |
| isMultiMapElement | Boolean | Whether this config contains a sub-list of MapElementTypes, of which one is selected based on a variable check. |