# ui.List

## Descripción General

[ui.Component](./../component.md) -> ui.List

These components allow users to select between various options, supporting single or multiple selection, and can be displayed as either a regular list, or as a dropdown list. `ONSELECTIONCHANGED` event are then triggered for any selection changes.

## Ejemplo

![A multiple selection list with entries B and E selected, and the cursor over the G entry](./../images/list_example_1.png)

```lua
-- Callback for selection events
local selectionChangeReportPrint = function(component, entryID, selected)
        if selected == 1 then
            log("Selected entry", entryID)
        else
            log("Deselected entry", entryID)
        end

        log("Selection is now")
        for k, v in pairs(component.selectedEntries) do
            log(formatStr("[{}] = {}", k, v))
        end
    end

-- Regular multi-selection list
local list = ui.List.new(container, categoryID, 1)
list:SetSize(100, 300)
list.stylesheetID = list_style

-- Force this to be a regular list, even if the previous style defines it to be a dropdown
list.dropdownMaxVisibleEntries = 0

list.maxSelected = 3
list:Subscribe(ui.Hook.ONSELECTIONCHANGED, selectionChangeReportPrint)

local entries = { "A", "B", "C", "D", "E", "F", "G" }

for i,v in ipairs(entries) do
    list:Add(v, i)
end
-- Or list:SetEntries(entries)
```

![Two dropdown lists, with the second one active and displaying its contents](./../images/list_example_2.png)

```lua
-- Basic Dropdown
local dropdownList = ui.List.new(container, categoryID)
dropdownList:SetPos(0, 0)
dropdownList:SetSize(100, 50)
dropdownList.stylesheetID = list_style
dropdownList.dropdownMaxVisibleEntries = 3
dropdownList:Subscribe(ui.Hook.ONSELECTIONCHANGED, selectionChangeReportPrint)
dropdownList:SetEntries(entries)

-- Can also be explicit about IDs on entries
local dropdownList = ui.List.new(container, categoryID)
dropdownList:SetPos(0, 60)
dropdownList:SetSize(100, 50)
dropdownList.stylesheetID = list_style
dropdownList.dropdownMaxVisibleEntries = 3
dropdownList:Subscribe(ui.Hook.ONSELECTIONCHANGED, selectionChangeReportPrint)
dropdownList:SetEntries({ A = 10, B = 20, C = 30, D = 40 }, 30)
```

## List Entry

In most cases, entries must be modified through methods on the list itself, however you can also iterate through the list contents via the `entries` property, which returns a collection of entries. These are fairly limited and mostly provide an easy way to read the various properties for the various entries.

| Property | Tipo | Descripción |
| --- | --- | --- |
| text | String | The label for this entry. |
| id | Int | **(Read-only)**   The value for this entry. |
| enabled | Bool | **(Read-only)**   Whether this entry can be selected. |
| visible | Bool | **(Read-only)**   Whether this entry is currently hidden. |
| selected | Bool | **(Read-only)**   Whether this entry is currently selected. |

## Métodos

### Constructor

```lua
function ui.List.new(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> List
```

Creates a new list on the specified parent.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this list in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| List | The newly created list.    The caller must set its layout and visual information afterwards. |

### Add

```lua
function ui.List:Add(label : String, id : Int) -> Bool
```

Adds an entry to this list with the provided label and ID.

> **Advertencia**
> Entry IDs are expected to be unique, if the provided ID is already used by another entry, this function will fail and return false.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| label | String | The text to display for this entry. |
| id | Int | Unique value used to identify this entry. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the entry was added successfully, false otherwise.   This function can fail and return false due to the provided ID already existing. |

### SetEntries

```lua
function ui.List:SetEntries(entries : [String], selectedID : Int?) -> Bool
function ui.List:SetEntries(entriesMap : { String -> Int }, selectedID : Int?) -> Bool
```

Clears existing entries from the list and adds all entries in the provided container to the list, optionally selecting the one with the provided ID.

> **Advertencia**
> Entry IDs are expected to be unique, if the provided ID is already used by another entry, this function will fail and return false.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| entries | `[String]` | Array of entry names to add to this list. Their respective IDs are autogenerated using an auto-incrementing integer. |
| entriesMap | `{ String -> Int }` | Table containing a mapping between entry names and their IDs to add to the list. |
| selectedID | Int? | ID for the entry to be selected afterwards.   If this is an invalid ID or not specified, the first entry will be selected instead for lists that always require at least one selected entry (dropdowns for example). |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the provided entries were valid and were successfully added to the list, false otherwise.   This function can fail and return false due to the provided ID already existing, or due to invalid/malformed data. |

### Clear

```lua
function ui.List:Clear()
```

Removes all entries from this list.

### UnselectAll

```lua
function ui.List:UnselectAll()
```

Deselects all currently selected entries in a multiple selection list (defined via the `maxSelected` property).  
Does nothing for single selection lists.

### SetEntryEnabled

```lua
function ui.List:SetEntryEnabled(id : Int, enabled : Bool) -> Bool
```

Sets whether or not the entry associated with the provided ID is enabled and can be selected.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to modify. |
| enabled | Bool | Whether or not the entry should be enabled and selectable. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there was an entry corresponding to the provided ID, false otherwise. |

### SetEntryVisible

```lua
function ui.List:SetEntryVisible(id : Int, visible : Bool) -> Bool
```

Sets whether or not the entry associated with the provided ID is visible to the user.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to modify. |
| visible | Bool | Whether or not the entry should be enabled visible to the user. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there was an entry corresponding to the provided ID, false otherwise. |

### SetEntrySelected

```lua
function ui.List:SetEntrySelected(id : Int, selected : Bool, triggerEvents : Bool?) -> Bool
```

Sets whether or not the entry associated with the provided ID is selected, and optionally triggers the corresponding `ONSELECTIONCHANGED` events.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to modify. |
| selected | Bool | Whether or not the entry should be selected. |
| triggerEvents | Bool? | Whether or not to emit `ONSELECTIONCHANGED` events for this change.   Defaults to false. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there was an entry corresponding to the provided ID, false otherwise. |

### SetEntryIcon

```lua
function ui.List:SetEntryIcon(id : Int, spriteID : Int) -> Bool
```

Sets the icon for the entry associated with the provided ID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to modify. |
| spriteID | Int | Numeric ID associated with the sprite to use as an icon for this entry. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there was an entry corresponding to the provided ID, false otherwise. |

### GetEntryEnabled

```lua
function ui.List:GetEntryEnabled(id : Int) -> Bool
```

Returns whether or not the entry associated with the provided ID is enabled and selectable.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to access. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there was an entry corresponding to the provided ID and it was enabled, false otherwise. |

### GetEntryVisible

```lua
function ui.List:GetEntryVisible(id : Int) -> Bool
```

Returns whether or not the entry associated with the provided ID is visible to the user.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to access. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there was an entry corresponding to the provided ID and it was visible, false otherwise. |

### GetEntrySelected

```lua
function ui.List:GetEntrySelected(id : Int) -> Bool
```

Returns whether or not the entry associated with the provided ID is selected.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to access. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there was an entry corresponding to the provided ID and it was selected, false otherwise. |

### HasEntry

```lua
function ui.List:HasEntry(id : Int) -> Bool
```

Returns whether or not there's an entry associated with the provided ID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Int | Numeric value associated with the entry to check. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if there is an entry corresponding to the provided ID, false otherwise. |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| numSelectedEntries | Int | **(Read-only)**   How many entries are currently selected on this list. |
| selectedEntries | [[List Entry]](#list-entry) | **(Read-only)**   Array containing the entries selected on this list. |
| entryHeight | Uint8 | Height for each displayed entry in interface units. |
| entryIconScale | Uint8 | Scaling factor applied to icons for entries, where `1` represents `1%`.   Defaults to `100`. |
| dropdownButtonOffset | Uint8 | Horizontal offset applied to this list's dropdown button.   Only used by dropdown lists. |
| dropdownButtonSize | Uint8 | Dimensions used for the dropdown button.   Only used by dropdown lists. |
| dropdownMaxVisibleEntries | Uint8 | How many entries can be displayed on the dropdown.   Controls whether the list is displayed as a dropdown or not - if it's a non-zero value, the list is displayed as a dropdown. |
| isDropdown | Bool | **(Read-only)**   Whether the list is displayed as a dropdown. |
| maxSelected | Uint8 | Sets the maximum number of selected entries at any one time.   Does not affect dropdowns.   May deselect entries to ensure the current selection does not exceed the new limit. |
| entries | [[List Entry]](#list-entry) | **(Read-only)**   Array containing all entries on this list. |
| contentMargin | [ui.Margin](./../common_types.md#uimargin) | **(Modifiable Contents)**   Offsets used to determine the inner content area for this component. |
| headerMargin | [ui.Margin](./../common_types.md#uimargin) | **(Modifiable Contents)**   Offsets used to determine the inner content area for this component's dropdown header.   Only used by dropdown lists. |
| scrollbar | [ui.ScrollBar](./../common_types.md#uiscrollbar) | **(Modifiable Contents)**   Scroll bar proprties used when vertical scrolling is required. |
| entryText | [ui.TextData](./../common_types.md#uitextdata) | **(Modifiable Contents)**   Text properties used when displaying entries for this list. |
| entrySprite | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the background. |
| buttonSprite | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the dropdown's button.   Only used by dropdown lists. |
| headerSprite | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the dropdown's header.   Only used by dropdown lists. |

## Custom Visuals

Using custom or plugin-provided sprites is supported, however the provided sprites used for the header and button must represent a spritesheet containing all of the potential states in a vertical layout using the following order - `default`, `mouseover`, `dropdown open`, `disabled`.