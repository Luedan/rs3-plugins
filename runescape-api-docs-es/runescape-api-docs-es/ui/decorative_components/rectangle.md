# ui.Rectangle

## Descripción General

[ui.Component](./../component.md) -> ui.Rectangle

Decorative component used to draw a block of a single colour, or an outline around an area.

## Ejemplo

```lua
-- Create a solid red rectangle
local solidRectangle = ui.Rectangle.new(parent)
solidRectangle:SetSize(200, 100)
solidRectangle.colour = Vector4.new(1.0, 0.0, 0.0, 1.0)

-- Create a blue outline around the previous rectangle
local outlineRectangle = ui.Rectangle.new(parent)
outlineRectangle:SetSize(200, 100)
outlineRectangle.colour = Vector4.new(0.0, 0.0, 1.0, 1.0)
outlineRectangle.fill = false
outlineRectangle.outlineThickness = -2
```

## Métodos

### Constructor

```lua
function ui.Rectangle.new(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> Rectangle
```

Creates a new rectangle on the specified parent.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this rectangle in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| Rectangle | The newly created rectangle.    The caller must set its layout and visual information afterwards. |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| fill | Bool | If true, this rectangle will be drawn as a single block, otherwise it will be drawn as an outline.   Defaults to false. |
| outlineThickness | Int | The pixel thickness of the outline drawn for this rectangle.   Defaults to 1.      Positive values will draw inwards, while negative values will draw outwards.   Outlines are clipped by parent containers, which will affect negative outlines when a rectangle fills its container space. |