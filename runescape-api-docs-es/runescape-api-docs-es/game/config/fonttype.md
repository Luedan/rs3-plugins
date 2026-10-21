# FontType

## Descripción General

A `FontType` config contains information about one of available fonts used by the game.

Font configs are referenced by [Components](../../ui/component.md) to render text, such as:

* [Button](../../ui/interactive_components/button.md)
* [Canvas](../../ui/decorative_components/canvas.md)
* [Carousel](../../ui/interactive_components/carousel.md)
* [Check](../../ui/interactive_components/check.md)
* [ComboField](../../ui/interactive_components/combo_field.md)
* [GroupBox](../../ui/layout_components/group_box.md)
* [InputField](../../ui/interactive_components/input_field.md)
* [List](../../ui/interactive_components/list.md)
* [PagedLayerHeader](../../ui/layout_components/paged_layer.md)
* [RadioGroup](../../ui/interactive_components/radio_group.md)
* [Slider](../../ui/interactive_components/slider.md)
* [Text](../../ui/decorative_components/text.md)

These config types can be found within the `config.Font` table:

```lua
config.Font.MUSEO_SANS_15PT_REGULAR
config.Font["MUSEO_SANS_15PT_REGULAR"]
config.Font.FromID(30) -- config.Font.MUSEO_SANS_15PT_REGULAR
```

> **Información**
> A `FontType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

## Common Modfiers

Font configs also provide methods to calculate the dimensions of strings drawn using that font, which can be used to help position surrounding [Components](../../ui/component.md).

There are three commonly used optional modifiers used in the methods provided:

* `ignoreTags`
`true` - Tags are treated as literal characters and included in the width calculation.
`false` - Tags are skipped over and not included in the width calculation.
* `noWordWrapping`
`true` - Word wrapping occurs on any character.
`false` - Word wrapping occurs only on spaces and hyphens.
* `noTrimEdges` -
`true` - Trailing spaces are not removed from wrapped lines before width calculation.
`false` - Trailing spaces are removed from wrapped lines before width calculation.

## Ejemplos

```lua
-- Calculate the width of a string
local myText = "This is a test string which is long enough to wrap into multiple lines when drawn."
local textWidth = config.Font.MUSEO_SANS_15PT_REGULAR:GetStringWidth(myText)
-- The largest width of all lines when wrapped inside fixed bounds width
local fixedBoundsWidth = 200
local textWidthMax = config.Font.MUSEO_SANS_15PT_REGULAR:GetStringWidthMultiline(myText, fixedBoundsWidth)
```

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Métodos

### GetStringWidth

```lua
function Font:GetStringWidth(text : String, ignoreTags : Boolean?) -> Integer
```

Returns the pixel width of a string drawn with this font.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| text | String |  | The text to calculate the total pixel width for. |
| ignoreTags | Boolean |  | See [Common Modifiers](#common-modfiers). |

| Retorna | Descripción |
| --- | --- |
| Integer | The total pixel width of the given string when drawn with this font. |

> **Ejemplo**
> ```lua
> -- Find the width of a string drawn with a specific font
> local pixelWidth = config.Font.MUSEO_SANS_15PT_REGULAR:GetStringWidth("How long this a piece of string?")
> 
> -- Find the width of a string with text tags inside it
> local tagText = "This is <col=FF0000>red text</col>"
> 
> -- Shorter - calculated as "This is red text"
> local width = config.Font.MUSEO_SANS_15PT_REGULAR:GetStringWidth(tagText, false)
> 
> -- Longer - calculated as "This is <col=FF0000>red text</col>"
> local widthIgnoreTags = config.Font.MUSEO_SANS_15PT_REGULAR:GetStringWidth(tagText, true)
> ```

### GetStringWidthMultiline

```lua
function Font:GetStringWidthMultiline(text : String, wrapWidth : Integer, ignoreTags : Boolean?, noWordWrapping : Boolean?, noTrimEdges : Boolean?) -> Integer
```

Returns the pixel width of a wrapped multiline string drawn with this font.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| text | String |  | The text to calculate the pixel width for. |
| wrapWidth | Integer |  | The pixel width limit at which the string should wrap. |
| ignoreTags | Boolean |  | See [Common Modifiers](#common-modfiers). |
| noWordWrapping | Boolean |  | See [Common Modifiers](#common-modfiers). |
| noTrimEdges | Boolean |  | See [Common Modifiers](#common-modfiers). |

| Retorna | Descripción |
| --- | --- |
| Integer | The total pixel width of the longest line after wrapping this given string into multiple lines. |

> **Ejemplo**
> ```lua
> -- Find the width of a multiline string drawn with a specific font
> -- This splits the string into multiple lines and returns the width on the longest line
> local pixelWidth = config.Font.MUSEO_SANS_15PT_REGULAR:GetStringWidthMultiline("How long this a piece of string?", 100)
> ```

### GetStringLineCount

```lua
function Font:GetStringLineCount(text : String, wrapWidth : Integer, ignoreTags : Boolean?, noWordWrapping : Boolean?, noTrimEdges : Boolean?) -> Integer
```

Returns how many lines the given string will be become when wrapped using this font.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| text | String |  | The text to calculate the line count for. |
| wrapWidth | Integer |  | The pixel width limit at which the string should wrap. |
| ignoreTags | Boolean |  | See [Common Modifiers](#common-modfiers). |
| noWordWrapping | Boolean |  | See [Common Modifiers](#common-modfiers). |
| noTrimEdges | Boolean |  | See [Common Modifiers](#common-modfiers). |

| Retorna | Descripción |
| --- | --- |
| Integer | The total number of lines resulting after wrapping the given string using this font. |

> **Ejemplo**
> ```lua
> -- How many lines a multiline string will return when wrapped with a specific font
> local lineCount = config.Font.MUSEO_SANS_15PT_REGULAR:GetStringLineCount("How long this a piece of string?", 100)
> ```

### GetStringHeightAndLineCount

```lua
function Font:GetStringHeightAndLineCount(text : String, wrapWidth : Integer, lineSpacing : Integer, ignoreTags : Boolean?, noWordWrapping : Boolean?, noTrimEdges : Boolean?) -> Integer, Integer
```

Returns the total pixel height of a string wrapped using this font and how many lines the text was wrapped into.

The resulting height is `(lineCount * lineSpacing) + fontMaxAscent + fontMaxDescent`.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| text | String |  | The text to calculate the height and line count for. |
| wrapWidth | Integer |  | The pixel width limit at which the string should wrap. |
| lineSpacing | Integer |  | The pixel spacing between each line.This is the distance between the baselines of each line. |
| ignoreTags | Boolean |  | See [Common Modifiers](#common-modfiers). |
| noWordWrapping | Boolean |  | See [Common Modifiers](#common-modfiers). |
| noTrimEdges | Boolean |  | See [Common Modifiers](#common-modfiers). |

| Retorna | Descripción |
| --- | --- |
| Integer | The total pixel height after wrapping this given string into multiple lines. |
| Integer | The total number of lines resulting after wrapping the given string using this font. |

> **Ejemplo**
> ```lua
> -- The total pixel height and how many lines a multiline string will return when wrapped with a specific font
> local pixelHeight,lineCount = config.Font.MUSEO_SANS_15PT_REGULAR:GetStringHeightAndLineCount("How long this a piece of string?", 100)
> ```

### SplitString

```lua
function Font:SplitString(text : String, wrapWidth : Integer, ignoreTags : Boolean?, noWordWrapping : Boolean?, noTrimEdges : Boolean?) -> [ String ]
```

Splits the given string using the given pixel wrap distance and returns the resulting strings.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| text | String |  | The text to split. |
| wrapWidth | Integer |  | The pixel width limit at which the string should split. |
| ignoreTags | Boolean |  | See [Common Modifiers](#common-modfiers). |
| noWordWrapping | Boolean |  | See [Common Modifiers](#common-modfiers). |
| noTrimEdges | Boolean |  | See [Common Modifiers](#common-modfiers). |

| Retorna | Descripción |
| --- | --- |
| [ String ] | The resulting strings after spliting the given string. |

> **Ejemplo**
> ```lua
> -- The resulting lines a multiline string will return when wrapped and split with a specific font
> local allLines = config.Font.MUSEO_SANS_15PT_REGULAR:SplitString("How long this a piece of string?", 100)
> 
> for i,line in ipairs(allLines) do
>     -- Do something with each line
> end
> ```

### GetSplitStringLine

```lua
function Font:GetSplitStringLine(text : String, lineIndex : Integer, wrapWidth : Integer, ignoreTags : Boolean?, noWordWrapping : Boolean?, noTrimEdges : Boolean?) -> String
```

Splits the given string using the given pixel wrap distance and returns the specific line requested.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| text | String |  | The text to split. |
| lineIndex | Integer |  | The index of the requested line.Line numbers are 1-indexed.Requesting a line index greater than available will return an empty string. |
| wrapWidth | Integer |  | The pixel width limit at which the string should split. |
| ignoreTags | Boolean |  | See [Common Modifiers](#common-modfiers). |
| noWordWrapping | Boolean |  | See [Common Modifiers](#common-modfiers). |
| noTrimEdges | Boolean |  | See [Common Modifiers](#common-modfiers). |

| Retorna | Descripción |
| --- | --- |
| String | The requested line after spliting the given string. |

> **Ejemplo**
> ```lua
> -- The second line of a multiline string after being wrapped and split with a specific font
> local secondLine = config.Font.MUSEO_SANS_15PT_REGULAR:GetSplitStringLine("How long this a piece of string?", 100, 2)
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"MUSEO_SANS_15PT_REGULAR"`. |
| typeName | String | The type of this config. Will always be `"Font"`. |
| baseline | Integer | The baseline distance of the font.This is also the vertical spacing between lines. |
| upperCaseAscent | Integer | The distance above the baseline for the uppercase 'X' glyph in the font. |
| lowerCaseAscent | Integer | The distance above the baseline for the lowercase 'x' glyph in the font. |
| maxAscent | Integer | The maximum distance above the baseline for the tallest glyph in the font. |
| maxDescent | Integer | The maximum distance below the baseline for the lowest glyph in the font. |