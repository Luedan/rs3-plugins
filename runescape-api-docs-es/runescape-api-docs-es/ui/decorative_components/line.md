# ui.Line

## Descripción General

[ui.Component](./../component.md) -> ui.Line

Decorative component responsible for drawing a line from the component's origin to its bottom-right point, taking into account the component's width and height.

> **Información**
> If you just want to create an outline, prefer using [Rectangle](./rectangle.md) since it has built-in support.

## Ejemplo

```lua
-- Create a thick horizontal green line with some transparency
local horizontalLine = ui.Line.new(parent)
horizontalLine:SetSize(200, 1)
horizontalLine.width = 10
horizontalLine.colour = Vector4.new(0.0, 1.0, 0.0, 0.7)
-- Create a thin vertical line
local verticalLine = ui.Line.new(parent)
verticalLine:SetSize(1, 200)
verticalLine.width = 2
-- Create a diagonal line going from 0,0 to 50,200
ui.Line.new(parent):SetSize(50, 200)
-- Create a diagonal line going from 0,200 to 0,0
local invertedDiagonalLine = ui.Line.new(parent)
invertedDiagonalLine:SetSize(50, 200)
invertedDiagonalLine.invert = true
```

## Métodos

### Constructor

```lua
function ui.Line.new(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> Line
```

Creates a new line on the specified parent.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this line in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| Line | The newly created line.    The caller must set its layout and visual information afterwards. |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| invert | Bool | If true, inverts diagonal lines vertically.   Defaults to false. |
| width | Uint | Width used for this line in interface units.   May differ from actual visible width due to anti-aliasing.   Defaults to `1`. |