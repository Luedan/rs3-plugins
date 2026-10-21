# ui.PagedLayer

## Descripción General

[ui.Component](./../component.md) -> [ui.ComponentCollection](./../component_collection.md) -> ui.PagedLayer

Similarly to [Layer](./layer.md), paged layers supports arbitrary positioning and layout of child components on them, however they also provide functionality to switch between different pages (or tabs as they're often called), allowing different sets of components to reside in each page.

The individual pages can have icons and labels defined for them, which are used by [PagedLayerHeader](#uipagedlayerheader) components to provide a basic page selection UI.

## Ejemplo

```lua
-- Create a new layer
local myLayer = ui.PagedLayer.new(parent)
myLayer:SetSize(200, 200)
myLayer.numPages = 3

-- Add a component to each page
for i=0,2 do
    -- Components are associated with the currently active page when created
    -- so we need to swap to the desired page first
    myLayer.activePage = i

    local c = ui.Rectangle.new(myLayer)
    c:SetSize(0, 0, 1.0, 1.0)
    c.colour = Vector4.new(1.0)
end

-- Optional - add some labels for the pages and a header
myLayer:SetPageLabel(0, "A")
myLayer:SetPageLabel(1, "B")
myLayer:SetPageLabel(2, "C")

local header = c:AddHeader(myLayer)
header:SetSize(200, 50)

myLayer:SetPos(0, 60)
```

## Métodos

### Constructor

```lua
function ui.PagedLayer.new(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> PagedLayer
```

Creates a new PagedLayer on the specified parent.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this paged layer in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| PagedLayer | The newly created paged layer.    The caller must set its layout and visual information afterwards. |

### SetPageEnabled

```lua
function ui.PagedLayer:SetPageEnabled(pageIndex : Uint8, enabled : Bool)
```

Sets whether the user can switch to the specified page through a [paged layer header](#uipagedlayerheader).

Disabling a page doesn't prevent it from being switched to via scripts using the `activePage` property.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| pageIndex | Uint8 | Index for the page to access. |
| enabled | Bool | Controls whether or not the user can switch to that page manually. |

### GetPageEnabled

```lua
function ui.PagedLayer:GetPageEnabled(pageIndex : Uint8) -> Bool
```

Gets whether the user can switch to the specified page through a [paged layer header](#uipagedlayerheader).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| pageIndex | Uint8 | Index for the page to access. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the page exists and is enabled, false otherwise. |

### SetPageLabel

```lua
function ui.PagedLayer:SetPageLabel(pageIndex : Uint8, label : String)
```

Sets the text label displayed for the specified page in a [paged layer header](#uipagedlayerheader).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| pageIndex | Uint8 | Index for the page to access. |
| label | String | Text to display for this page in a paged layer header. |

### GetPageLabel

```lua
function ui.PagedLayer:GetPageLabel(pageIndex : Uint8) -> String
```

Gets the text label displayed for the specified page in a [paged layer header](#uipagedlayerheader).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| pageIndex | Uint8 | Index for the page to access. |

| Retorna | Descripción |
| --- | --- |
| String | Text to display for this page in a paged layer header, or an empty string if not specified or if the page is missing. |

### SetPageIcon

```lua
function ui.PagedLayer:SetPageIcon(pageIndex : Uint8, iconSpriteID : Int)
```

Sets the ID for the sprite to display as an icon for the specified page in a [paged layer header](#uipagedlayerheader).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| pageIndex | Uint8 | Index for the page to access. |
| iconSpriteID | Int | ID for the sprite to use as an icon for this page. |

### GetPageIcon

```lua
function ui.PagedLayer:GetPageIcon(pageIndex : Uint8) -> Int
```

Gets the ID for the sprite to display as an icon for the specified page in a [paged layer header](#uipagedlayerheader).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| pageIndex | Uint8 | Index for the page to access. |

| Retorna | Descripción |
| --- | --- |
| Int | ID for the sprite to use as an icon for this page, or -1 if not specified or if the page is missing. |

### AddHeader

```lua
function ui.PagedLayer:AddHeader(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> PagedLayerHeader
```

Creates a new [PagedLayerHeader](#uipagedlayerheader) on the specified parent, and associates it with this paged layer, allowing it to retrieve labels and icons for the available pages.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this paged layer header in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| PagedLayerHeader | The newly created paged layer header associated with this paged layer.    The caller must set its layout and visual information afterwards. |
| ``` |  |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| activePage | Uint8 | The currently active page, displayed to the user. |
| numPages | Uint8 |  |
| numBuiltinPages | Uint8 | **(Read-only)**   The number of statically built-in pages on this paged layer.   Always zero for dynamically created paged layers. |
| contentMargin | [ui.Margin](./../common_types.md#uimargin) | **(Modifiable Contents)**   Offsets used to determine the inner content area for this component. |
| backgroundSprite | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the background. |

## ui.PagedLayerHeader

These components are directly associated with an individual PagedLayer, and provide a basic UI to allow the user to switch between the various pages.

Page information is retrieved from the associated PagedLayer, with labels and icons being displayed in page index order on this header. Optionally, in addition to that, an icon can also be displayed for disabled pages to indicate their status.

> **Advertencia**
> Although a paged layer can be associated with any number of headers, you should avoid doing so as there's no benefit to it at the moment and support for that may be removed in the future.

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| target | ui.PagedLayer | The paged layer associated with this header, and where page information is being sourced retrieved from. |
| isHorizontal | Bool | Controls whether this header uses a horizontal or vertical layout. |
| contentMargin | [ui.Margin](./../common_types.md#uimargin) | **(Modifiable Contents)**   Offsets used to determine the inner content area for this component. |
| pageHeaderMargin | [ui.Margin](./../common_types.md#uimargin) | **(Modifiable Contents)**   Offsets used to determine the inner content area for each page element. |
| entryText | [ui.TextData](./../common_types.md#uitextdata) | **(Modifiable Contents)**   Text properties used when displaying entries for this combo. |
| backgroundSprite | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the background. |
| disabledPageIcon | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the icon displayed on disabled pages. |
| pageHeaderSprite | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the the individual page elements. |