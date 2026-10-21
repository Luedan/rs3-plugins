# ui.Layer

## Descripción General

[ui.Component](./../component.md) -> [ui.ComponentCollection](./../component_collection.md) -> ui.Layer

The most basic layout component, supports arbitrary positioning and layout of child components on it.

## Ejemplo

```lua
-- Create a new layer
local myLayer = ui.Layer.new(parent)
myLayer:SetSize(200, 200)

-- Create an outline for the new layer
local outlineLayer = ui.Rectangle.new(myLayer)
outlineLayer:SetSize(0, 0, 1.0, 1.0)
outlineLayer.colour = Vector4.new(1.0)
```

## Métodos

### Constructor

```lua
function ui.Layer.new(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> Layer
```

Creates a new Layer on the specified parent.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this layer in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| Layer | The newly created layer.    The caller must set its layout and visual information afterwards. |