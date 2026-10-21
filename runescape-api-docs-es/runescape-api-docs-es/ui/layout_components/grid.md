# ui.Grid

## Descripción General

[ui.Component](./../component.md) -> [ui.ComponentCollection](./../component_collection.md) -> ui.Grid

Grids subdivide an area into multiple same-size cells which can each contain a child component, with components being assigned to cells in the order they're created, from left to right and top to bottom.

> **Información**
> Although each cell can only have one component, this can be of any type, even including other grids.

Grid layouts can be configured in one of two modes:

* Fixed number of columns and rows - Results in cell width and height varying based on the grid's size.
* Fixed cell width and height - Results in the number of columns and rows varying based on the grid's size.

> **Advertencia**
> If the number of child components on a grid exceeds the number of cells, any additional components will ignore the grid layout and end up at position 0,0 with a size of 100x100 interface units, indicating a failed layout operation.

## Ejemplo

![A grid containing 5 rows and 5 columns, with each cell containing a solid coloured rectangle](./../images/grid_example.png)

```lua
-- Create a new 5x5 grid
local myGrid = ui.Grid.new(parent)
myGrid:SetSize(200, 200)
myGrid:SetColumnRows(5, 5)

-- Fill each grid cell with a solid colour
local maxRect = grid.columns * grid.rows - 1
for i=0,maxRect do
    local rect = ui.Rectangle.new(grid)
    rect.colour = Vector4.new(i / maxRect, 0.0, 0.0, 1.0)
    rect.fill = true

    -- Have the rectangle occupy the entire cell
    rect:SetSize(0, 0, 1.0, 1.0)
end
```

## Métodos

### Constructor

```lua
function ui.Grid.new(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> Grid
```

Creates a new Grid on the specified parent.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this grid in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| Grid | The newly created grid.    The caller must set its layout and visual information afterwards. |

### SetColumnRows

```lua
function ui.Grid:SetColumnRows(columns : Int, rows : Int)
```

Makes the grid use a fixed number of columns and rows, and dynamically scales cell sizes based on that and the grid's dimensions.

> **Advertencia**
> Ideally this should only be called on empty grids, as calling this will request layout operations for all child components present on the grid.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| columns | Int | The desired number of columns to use for this grid. |
| rows | Int | The desired number of rows to use for this grid. |

> **Ejemplo**
> ```lua
> myGrid:SetSize(200, 50)
> myGrid:SetColumnRows(5, 2)
> log("w=", myGrid.cellWidth, "h=", myGrid.cellHeight)    -- w=40 h=25
> log("c=", myGrid.columns, "r=", myGrid.rows)            -- c=5 r=2
> ```

### SetCellSize

```lua
function ui.Grid:SetCellSize(width : Int, height : Int)
```

Makes the grid use fixed cell dimensions, and dynamically scales the number of columns and rows available based on that and the grid's dimensions.

> **Advertencia**
> Ideally this should only be called on empty grids, as calling this will request layout operations for all child components present on the grid.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| width | Int | The desired width of each cell to use for this grid. |
| height | Int | The desired height of each cell to use for this grid. |

> **Ejemplo**
> ```lua
> myGrid:SetSize(200, 50)
> myGrid:SetCellSize(50, 10)
> log("w=", myGrid.cellWidth, "h=", myGrid.cellHeight)    -- w=50 h=10
> log("c=", myGrid.columns, "r=", myGrid.rows)            -- c=4 r=5
> ```

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| cellWidth | Int | **(Read-only)** The width of each cell in this grid. |
| cellHeight | Int | **(Read-only)** The height of each cell in this grid. |
| columns | Int | **(Read-only)** The number of columns in this grid. |
| rows | Int | **(Read-only)** The number of rows in this grid. |
| hasFixedCellSizes | Bool | **(Read-only)** Indicates whether the cell size for this grid has been explicitly set via `SetCellSize`, resulting in dynamically calculated `columns` and `rows` values based on the grid's dimensions.   Otherwise it's `cellWidth` and `cellHeight` that are dynamically calculated. |
| spacing | Int | The spacing in interface units between grid cells, both horizontal and vertical. |