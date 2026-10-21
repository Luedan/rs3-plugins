# Hojas de Estilo

## Descripción General

Style sheets bundle together multiple visual parameters for various component types in a single reusable object.

You can use style sheets to achieve a consistent visual across your plugin and the game, while also simplifying interface creation since you can just specify the style sheet to use instead of the individual sprites, margins, colours, etc, for each component.

## Usage

It's straightforward to access or create stylesheets, only requiring the user to index into `ui.StyleSheets` with the ID of an built-in stylesheet (obtainable from `id.StyleSheet`), or with a new ID.

Once a stylesheet has been retrieved, you then use an entry from the `ui.StyleValue` table, which contains all of the currently available style properties, as an index into the stylesheet to retrieve or modify the value for that property.

> **Información**
> Currently style sheets can only be assigned integer properties.

> **Advertencia**
> While you can access/store properties other than those contained in the `ui.StyleValue` table, it is not recommended as those properties may clash with future additions to `ui.StyleValue`.

> **Ejemplo**
> ```lua
> myButtonComponent.stylesheetID = id.StyleSheet.BUTTON_DEFAULT
> ```
> ```lua
> local buttonTint = ui.StyleSheets[id.StyleSheet.BUTTON_DEFAULT][ui.StyleValue.button.tint.rgb]
> print("Default button tint =", buttonTint)
> ```
> ```lua
> -- StyleSheet IDs are unique
> local myStyleSheetID = 10000
> ui.StyleSheets[myStyleSheetID][ui.StyleValue.button.tint.rgb] = 0xFF0000
> ui.StyleSheets[myStyleSheetID][ui.StyleValue.button.tint.alpha] = 100
> 
> -- Can set parents dynamically, allowing a stylesheet to "inherit" properties
> ui.StyleSheets[myStyleSheetID].parent = ui.StyleSheets[id.StyleSheet.BUTTON_DEFAULT]
> 
> -- Can then set the style on a component
> component.stylesheetID = myStyleSheetID
> 
> -- Can also access style data manually and use it
> local buttonTint = ui.StyleSheets[myStyleSheetID][ui.StyleValue.button.tint.rgb]
> component.rgb = buttonTint
> ```

## ui.StyleSheet

### Métodos

#### Index

```lua
ui.StyleSheet[property : Uint] -> Int?
ui.StyleSheet[property : Uint] = value : Int
```

Gets or sets the value for the specified property in this stylesheet.

> **Información**
> When retrieving the value for a missing entry, the entire parent hierarchy gets checked for that same property until it is found or there are no more parents.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| property | Uint | Number representing the style property to search for.   Can be an arbitrary number but prefer using a property listed in the `ui.StyleValue` table for consistency and safety, as the underlying property IDs may change in the future. |
| value | Int | The value to set for that property. |

| Getter Returns | Description |
| --- | --- |
| Int? | The value of the specified property, or nil if not found. |

#### GetValue

```lua
function ui.StyleSheet:GetValue(property : Uint) -> Int?
```

Attempts to retrieve the value for the specified property from this stylesheet, or if missing, from its parent.

> **Información**
> If an entry is missing, the entire parent hierarchy gets checked for that same property until it is found or there are no more parents.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| property | Uint | Number representing the style property to search for.   Can be an arbitrary number but prefer using a property listed in the `ui.StyleValue` table for consistency and safety, as the underlying property IDs may change in the future. |

| Retorna | Descripción |
| --- | --- |
| Int? | The value of the specified property, or nil if not found. |

#### SetValue

```lua
function ui.StyleSheet:SetValue(property : Uint, value : Int)
```

Sets the value for the specified property on this stylesheet.

> **Advertencia**
> Currently, changing a property value will not update that stylesheet's users, and instead you must re-assign the stylesheet to trigger an update.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| property | Uint | Number representing the style property to search for.   Can be an arbitrary number but prefer using a property listed in the `ui.StyleValue` table for consistency and safety, as the underlying property IDs may change in the future. |
| value | Int | The value to set for that property. |

#### HasValue

```lua
function ui.StyleSheet:HasValue(property : Uint) -> Bool
```

Checks if the specified property exists on this stylesheet or its parents.

> **Información**
> If an entry is missing, the entire parent hierarchy gets checked for that same property until it is found or there are no more parents.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| property | Uint | Number representing the style property to search for.   Can be an arbitrary number but prefer using a property listed in the `ui.StyleValue` table for consistency and safety, as the underlying property IDs may change in the future. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the property exists, false otherwise. |

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric ID associated with this stylesheet. |
| parent | ui.StyleSheet | Parent stylesheet for this. |
| parentID | Int | Numeric ID associated with the parent for this stylesheet, or `-1` if no parent is specified. |

## ui.StyleSheets

The container of all available stylesheets, can be indexed into using IDs to retrieve existing stylesheets or create new ones.

### Métodos

#### Index

```lua
ui.StyleSheets[styleSheetID : Int] -> ui.StyleSheet
```

Retrieves the existing stylesheet associated with the provided ID, or creates a new one if missing.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| styleSheetID | Int | Numeric ID associated with the stylesheet to be retrieved. |

| Retorna | Descripción |
| --- | --- |
| [ui.StyleSheet](#uistylesheet) | The existing or newly created stylesheet, associated with the provided ID. |

#### Find

```lua
function ui.StyleSheets:Find(styleSheetID : Int) -> ui.StyleSheet?
```

Attempts to retrieve the existing stylesheet associated with the provided ID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| styleSheetID | Int | Numeric ID associated with the stylesheet to be retrieved. |

| Retorna | Descripción |
| --- | --- |
| [ui.StyleSheet](#uistylesheet) | The stylesheet associated with the provided ID, or nil if missing. |

#### Contains

```lua
ui.function StyleSheets:Contains(styleSheetID : Int) -> Bool
```

Checks whether a stylesheet associated with the provided ID already exists.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| styleSheetID | Int | Numeric ID associated with the stylesheet to check. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there's already a stylesheet with the provided ID, false otherwise. |

## Recommend Built-in Styles

While there are a large number of styles available which can be accessed through the *id.StyleSheet* table, the following represent good defaults for plugins to use:

| Component Type | Recommended Style | Alternative Styles |
| --- | --- | --- |
| Button | id.StyleSheet.BUTTON_DEFAULT | id.StyleSheet.BUTTON_CORNERED_BOLD_NEUTRAL   id.StyleSheet.BUTTON_CORNERED_BOLD_POSITIVE   id.StyleSheet.BUTTON_CORNERED_BOLD_NEGATIVE |
| Check | id.StyleSheet.CHECKBOX_DEFAULT | id.StyleSheet.CHECKBOX_DEFAULT_LEFT_ALIGNED   id.StyleSheet.CHECKBOX_DEFAULT_RIGHT_ALIGNED |
| InputField | id.StyleSheet.INPUT_DEFAULT | - |
| RadioGroup | id.StyleSheet.RADIO_DEFAULT | - |
| List | id.StyleSheet.DROPDOWN_DEFAULT[1](#fn:1) | - |
| ComboField | id.StyleSheet.COMBO_DEFAULT | - |
| GroupBox | id.StyleSheet.GROUPBOX_DEFAULT | - |
| Carousel | id.StyleSheet.CAROUSEL_DEFAULT | - |
| PagedCarousel | id.StyleSheet.PAGED_CAROUSEL_DEFAULT | id.StyleSheet.PAGED_CAROUSEL_FULL   id.StyleSheet.PAGED_CAROUSEL_SINGLE   id.StyleSheet.PAGED_CAROUSEL_TRIPLE |
| PagedLayer | id.StyleSheet.PAGED_LAYER_DEFAULT | - |
| RadialProgressOverlay | id.StyleSheet.RADIAL_DEFAULT | id.StyleSheet.RADIAL_CIRCLE   id.StyleSheet.RADIAL_SQUARE |
| Slider | id.StyleSheet.SLIDER_DEFAULT | id.StyleSheet.SLIDER_WIDE |