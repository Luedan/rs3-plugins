# ui.RadioGroup

## Descripción General

[ui.Component](./../component.md) -> ui.RadioGroup

RadioGroup components are used to display a collection of options as a series of toggleable buttons.

They support an arbitrary minimum and maximum number of selected options, allowing for both the usual radio control's single selection behaviour, and for a more flexible selection limit, with selection changes triggering `ONSELECTIONCHANGED` events hooks.

They're ideal for situations where you have a set of mutually exclusive options, or want to allow users to mix and match multiple options (eg. category filters).

## Ejemplo

![A single-selection radiogroup, listing various options as separate selectable buttons](./../images/radiogroup_example_1.png)

```lua
local columns = 3
local spacing = 5
local buttonSize = 40
local buttonLabelSpacing = 10

local c = ui.RadioGroup.new(parent, categoryID)
c.stylesheetID = radiogroup_style
c:SetSize(400, 200)
c:SetVisualParams(columns, spacing, buttonSize, buttonLabelSpacing)
c:Subscribe(ui.Hook.ONSELECTIONCHANGED,
    function(component, id, selectionChange)
        print("Selection event=" ..  tostring(selectionChange) .. " id=" .. tostring(id))
    end)

-- Add options
c:Add(0, "Min");
c:Add(1, "Low");
c:Add(2, "Medium");
c:Add(3, "High");
c:Add(4, "Ultra");
```

![A multiple-selection radiogroup listing various options as separate selectable checkboxes](./../images/radiogroup_example_2.png)

```lua
local options = { Firemaking = 0, Woodcutting = 1, Runecrafting = 2, Smithing = 3 }

local columns = 2
local spacing = 5
local buttonSize = 20
local buttonLabelSpacing = 5

local c = ui.RadioGroup.new(parent)
c.stylesheetID = radiogroup_check_style
c:SetSize(300, 150)
c:SetVisualParams(columns, spacing, buttonSize, buttonLabelSpacing)
c:SetSelectionLimits(0, 3)
c:Subscribe(ui.Hook.ONSELECTIONCHANGED,
    function(component, id)
        print("Selection is now " .. tostring(id))
    end)

c:SetOptions(options)

-- Setup default selections
c:SetOptionSelected(options.Smithing, false, false)
c:SetOptionSelected(options.Firemaking, true, false)
c:SetOptionSelected(options.Woodcutting, true, false)
c:SetOptionSelected(options.Runecrafting, true, false)
```

## Métodos

### Constructor

```lua
function ui.RadioGroup.new(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> RadioGroup
```

Creates a new radiogroup on the specified parent.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this radiogroup in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| RadioGroup | The newly created radiogroup.    The caller must set its layout and visual information afterwards. |

### Add

```lua
function ui.RadioGroup:Add(id : Int, label : String) -> Bool
```

Adds an option to the radiogroup.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Unique value identifying this option. |
| label | String | Text to display for this option. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if successful, false if an option with that ID already exists. |

### Remove

```lua
function ui.RadioGroup:Remove(id : Int) -> Bool
```

Removes the option associated with this ID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Value used to identify the option to remove. |

| Retorna | Descripción |
| --- | --- |
| Bool | Indicates whether or not an option was successfully removed. |

### HasOption

```lua
function ui.RadioGroup:HasEntry(id : Int) -> Bool
```

Returns whether or not there's an option associated with the provided ID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Value associated with the option to check. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there is an option corresponding to the provided ID, false otherwise. |

### SetOptions

```lua
function ui.RadioGroup:SetEntries(entries : { String -> Int }) -> Bool
```

Clears existing options from the radiogroup and adds all options in the provided container to the radiogroup.

> **Advertencia**
> Entry IDs are expected to be unique, if the provided ID is already used by another option, this function will fail and return false.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| entries | { String -> Int } | Table containing a mapping between option names and their IDs to add to the radiogroup. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the provided options were valid and were successfully added to the radiogroup, false otherwise.   This function can fail and return false due to the provided ID already existing, or due to invalid/malformed data. |

> **Ejemplo**
> ```lua
> local c = ui.RadioGroup.new(parent)
> c:SetOptions({ A = 1, B = 2, C = 3, D = 10, E = 20, F = 50 })
> ```

### GetSelectedValue

```lua
function ui.RadioGroup:GetSelectedValue(selectionIndex : Uint8) -> Int
```

Gets the value/ID associated with the `selectionIndex` selected entry.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| selectionIndex | Uint8 | Index into the currently selected entries collection to access. |

| Retorna | Descripción |
| --- | --- |
| Int | The value/ID associated with the entry, or -1 if there are less than `selectionIndex` selected entries. |

### GetSelectedLabel

```lua
function ui.RadioGroup:GetSelectedLabel(selectionIndex : Uint8) -> String
```

Gets the text label associated with the `selectionIndex` selected entry.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| selectionIndex | Uint8 | Index into the currently selected entries collection to access. |

| Retorna | Descripción |
| --- | --- |
| String | The text label associated with the entry, or an empty string if there are less than `selectionIndex` selected entries. |

### GetOptionEnabled

```lua
function ui.RadioGroup:GetOptionEnabled(id : Int) -> Bool
```

Gets whether the option associated with the specified ID is enabled and can be selected by the user.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Value associated with the desired option. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the desired option exists and is enabled, false otherwise. |

### SetOptionEnabled

```lua
function ui.RadioGroup:SetOptionEnabled(id : Int, enabled : Bool) -> Bool
```

Sets whether the option associated with the specified ID is enabled and can be selected by the user.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Value associated with the desired option. |
| enabled | Bool | Whether or not the option should be enabled and selectable by the user. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the desired option exists, false otherwise. |

### GetOptionSelected

```lua
function ui.RadioGroup:GetOptionEnabled(id : Int) -> Bool
```

Gets whether the option associated with the specified ID is currently selected.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Value associated with the desired option. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the desired option exists and is selected, false otherwise. |

### SetOptionSelected

```lua
function ui.RadioGroup:SetOptionSelected(id : Int, selected : Bool, triggerEvents : Bool?) -> Bool
```

Sets whether the option associated with the specified ID is currently selected, optionally triggering selection events.

> **Información**
> This method obeys selection limits and will not make any changes if this would have resulted in the radiogroup being in an invalid state.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Value associated with the desired option. |
| selected | Bool? | Whether or not the option should be selected currently.   Defaults to false. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the desired option exists, false otherwise. |

### SetVisualParams

```lua
function ui.RadioGroup:SetVisualParams(numColumns : Uint8, spacing : Uint8, buttonSize : Uint8, buttonLabelSpacing : Uint8)
```

Sets the parameters used to position and layout the various options within this radiogroup.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| numColumns | Uint8 | Number of columns to split the various radiogroup contents over. |
| spacing | Uint8 | Desired horizontal and vertical spacing between each option. |
| buttonSize | Uint8 | Controls whether to display options as toggle buttons or as checks.   If set to `0`, options are displayed as toggle buttons, otherwise this controls the size of the checkbox for each option. |

### SetSelectionLimits

```lua
function ui.RadioGroup:SetSelectionLimits(minSelectedEntries : Uint8, maxSelectedEntries : Uint8) -> Bool
```

Changes the minimum and maximum number of selected options, without changing how many options are currently selected.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| minSelectedEntries | Uint8 | Minimum number of entries that can be selected at any one time. |
| maxSelectedEntries | Uint8 | Maximum number of entries that can be selected at any one time. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the `minSelectedEntries` and `maxSelectedEntries` form a valid range, where the minimum is less than or equal to maximum, and were set successfully, false otherwise. |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| numSelected | Uint8 | **(Read-only)**   The number of currently selected options. |
| selectedValues | `[Int]` | **(Read-only)**   Array containing the IDs or values of the currently selected entries. |
| selectedLabels | `[String]` | **(Read-only)**   Array containing the text labels of the currently selected entries. |
| entryMargin | [ui.Margin](./../common_types.md#uimargin) | **(Modifiable Contents)**   Offsets used to determine the inner content area within the regions for the individual options. |
| labelsText | [ui.TextData](./../common_types.md#uitextdata) | **(Modifiable Contents)**   Text properties used when displaying option text labels. |
| buttonSprite | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the radiogroup's buttons. |

## Custom Visuals

Radio groups can make use of the same sprites as check components since they're essentially identical in terms of functionality.

See [here](./check.md#custom-visuals) for information on how to create custom sprites that are usable by radio groups.