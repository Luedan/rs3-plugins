# ui.Carousel

## Descripción General

[ui.Component](./../component.md) -> ui.Carousel

Carousels contain a series of entries, and only display one at a time, allowing the user to switch between them via buttons to the left and right of the carousel's contents.

They're ideal for situations where you have a limited set of options that relate to eachother, such as game settings.

Entries can be displayed as either an icon, or as a text label, with support for mixing and matching within the same carousel.

## Ejemplo

![A carousel with the "Ultra" option selected and the cursor hovering the left button](./../images/carousel_example_1.png)

```lua
local c = ui.Carousel.new(parent)
c.stylesheetID = carousel_default
c:SetSize(200, 50)
c:Subscribe(ui.Hook.ONSELECTIONCHANGED,
    function(component, id, selectionChange)
        print("Selection event=" ..  tostring(selectionChange) .. " id=" .. tostring(id))
    end)

-- Add entries
c:Add(0, "Min");
c:Add(1, "Low");
c:Add(2, "Medium");
c:Add(3, "High");
c:Add(4, "Ultra");
```

## Métodos

### Constructor

```lua
function ui.Carousel.new(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> Carousel
```

Creates a new carousel on the specified parent.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this carousel in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| Carousel | The newly created carousel.    The caller must set its layout and visual information afterwards. |

### Add

```lua
function ui.Carousel:Add(id : Int, label : String) -> Bool
function ui.Carousel:Add(id : Int, iconSpriteID : Int) -> Bool
```

Adds an entry to the carousel.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Unique numeric value identifying this entry. |
| label | String | Text to display for this entry. |
| iconSpriteID | Int | ID for the sprite to use as an icon for this entry. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if successful, false if an entry with that ID already exists. |

### Clear

```lua
function ui.Carousel:Clear()
```

Removes all entries from the carousel.

### HasEntry

```lua
function ui.Carousel:HasEntry(id : Int) -> Bool
```

Returns whether or not there's an entry associated with the provided ID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to check. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there is an entry corresponding to the provided ID, false otherwise. |

### SetEntryEnabled

```lua
function ui.Carousel:SetEntryEnabled(id : Int, enabled : Bool) -> Bool
```

Sets whether or not the entry associated with the provided ID is enabled and can be selected.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to modify. |
| enabled | Bool | Whether or not the entry should be enabled and selectable. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there was an entry corresponding to the provided ID, false otherwise. |

### GetEntryEnabled

```lua
function ui.Carousel:GetEntryEnabled(id : Int) -> Bool
```

Returns whether or not the entry associated with the provided ID is enabled and selectable.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to access. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there was an entry corresponding to the provided ID and it was enabled, false otherwise. |

### Select

```lua
function ui.ComboField:Select(id : Int, triggerEvents : Bool?) -> Bool
```

Selects the entry associated with the provided ID, and optionally triggers the corresponding `ONSELECTIONCHANGED` events.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to select. |
| triggerEvents | Bool? | Whether or not to emit `ONSELECTIONCHANGED` events for this change.   Defaults to false. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there was an entry corresponding to the provided ID, false otherwise. |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| selectedID | Int | **(Read-only)**   The numeric ID for the currently selected entry, or -1 if there is no selection. |
| buttonWidth | Uint16 | Width for the carousel's buttons in interface units. |
| buttonHeight | Uint16 | Height for the carousel's buttons in interface units. |
| buttonOffset | Uint16 | Offset in interface units from the left/right edges applied when positioning the carousel's buttons. |
| contentMargin | [ui.Margin](./../common_types.md#uimargin) | **(Modifiable Contents)**   Offsets used to determine the inner content area for this component. |
| entryText | [ui.TextData](./../common_types.md#uitextdata) | **(Modifiable Contents)**   Text properties used when displaying entry text labels. |
| buttonSprite | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the carousel's buttons. |
| backgroundSprite | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the background. |

## Custom Visuals

Using custom or plugin-provided sprites is supported, however the provided sprite must represent a spritesheet containing all of the potential states in a vertical layout using the following order - `default`, `mouseover`, `pressed`, `disabled`.

![Image containing the following button states from top to bottom: default, mouseover, pressed, disabled](./../images/carousel_custom_layout.png)