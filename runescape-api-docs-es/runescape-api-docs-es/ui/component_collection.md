# ui.ComponentCollection

## Descripción General

[ui.Component](./component.md) -> ui.ComponentCollection

Base type common to all user interface layout components.

The following layout component types are available:

* [Layer](./layout_components/layer.md) - Simple component that allows arbitrary positioning/sizing of child components
* [Panel](./layout_components/panel.md) - Automatically positions/resizes components along the panel's direction (either horizontal or vertical), taking into account total component sizes across that dimension.
* [Grid](./layout_components/grid.md) - Organises components in a grid. Supports using either fixed-size grid cells, resulting in dynamic rows and columns, or a fixed number of rows and columns, which results in dynamic grid cell sizes
* [Paged Layer](./layout_components/paged_layer.md) - A tabbed version of the layer component, and containing functionality for creating tab headers.
* [Paged Carousel](./layout_components/paged_carousel.md) - A variant of `Paged Layer` that has built-in functionality for switching between pages, and supports displaying the contents of multiple pages at a time as part of a horizontal carousel.
* [Group Box](./layout_components/group_box.md) - Similar to `Layer` in that it allows arbitrary positioning/sizing of child components, but additionally encloses them in a box with an optional header label.

## Métodos

### IterateStaticComponents/IterateDynamicComponents

```lua
function ComponentCollection:IterateStaticComponents(callback : function (component : ui.Component, visible : Bool) -> Bool)
function ComponentCollection:IterateDynamicComponents(callback : function (component : ui.Component, visible : Bool) -> Bool)
```

Iterates over statically defined components contained in this collection, executing the provided callback once for each component, optionally stopping based on the callback's return value.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| callback | function (component : ui.Component, visible : Bool) -> Bool | Callback to execute for each component, receiving the component and its visibility status.     If it returns true, iteration will stop |

> **Ejemplo**
> ```lua
> -- Report the dynamic ID and visible status
> collection:IterateDynamicComponents(
>     function (component, visible)
>         log("Found component", component.dynamicID, " visible=", visible)
>         return false -- Keep iterating
>     end)
> ```

### GetChild

```lua
function ComponentCollection:GetChild(staticID : Int) -> Component<T>?
function ComponentCollection:GetChild(categoryID : Int, dynamicID : Int) -> Component<T>?
```

Attempts to retrieve the static or dynamic child component corresponding to the provided IDs, returning nil if missing.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| staticID | Int | Value used to identify a static component. |
| categoryID | Int | Value used to identify the category associated with a component. |
| dynamicID | Int | Value used to identify the in-category ID associated with a component. |

| Retorna | Descripción |
| --- | --- |
| Component? | The existing component if found, or nil if missing |

> **Ejemplo**
> ```lua
> local static = collection:GetChild(100)
> if static ~= nil then
>     local dyn = static:GetChild(0, 1)
> 
>     if dyn ~= nil then
>         print("Found dynamic component on static parent with ID 100")
>     end
> end
> ```

### Delete

```lua
function ComponentCollection:Delete(categoryID : Int, dynamicID : Int) -> Bool
```

Attempts to delete the dynamic child component corresponding to the provided IDs, returning true if successful.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| categoryID | Int | Value used to identify the category associated with a component. |
| dynamicID | Int | Value used to identify the in-category ID associated with a component. |

| Retorna | Descripción |
| --- | --- |
| Bool | Indicates whether or not a component was deleted. |

> **Ejemplo**
> ```lua
> local static = collection:GetChild(100)
> if static ~= nil then
>     if static:Delete(0, 1) then
>         print("Successfully deleted the dynamic component")
>     end
> end
> ```

## DeleteAll

```lua
function ComponentCollection:DeleteAll()
```

Deletes all dynamically created child components contained in the current collection.

> **Información**
> Individual components can be deleted by using `Component:Destroy` or `ComponentCollection:Delete` instead

### SetScrollPos

```lua
function ComponentCollection:SetScrollPos(x : Int, y : Int)
```

Sets the origin of this component's scroll region, if it supports scrolling.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| x | Int | Horizontal origin for this component's scroll region. |
| y | Int | Vertical origin for this component's scroll region. |

### SetScrollSize

```lua
function ComponentCollection:SetScrollSize(width : Int, height : Int)
```

Sets the size of this component's scroll region, if it supports scrolling.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| width | Int | Target width for this component's scroll region. |
| height | Int | Target height for this component's scroll region. |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| scrollable | bool | **(Read-only)** Indicates whether this component can be scrolled. |
| scrollX | number | **(Read-only)** Current horizontal origin for this component's scroll region. |
| scrollY | number | **(Read-only)** Current vertical origin for this component's scroll region. |
| scrollWidth | number | **(Read-only)** Width of this component's scroll region. |
| scrollHeight | number | **(Read-only)** Height of this component's scroll region. |