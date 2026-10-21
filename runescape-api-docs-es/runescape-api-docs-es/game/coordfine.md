# CoordFine

## Descripción General

A CoordFine represents a 3D world position within the game world, in *Fine units*, as opposed to the tile position found in CoordGrid, which is in *Grid units*.

An important distinction is that a CoordFine also includes a vertical Y position, whereas a CoordGrid does not.

## Ejemplos

```lua
-- CoordGrid position
local coordGrid = CoordGrid._0_50_50_32_32
-- CoordFine equivalent; each tile contains 512 Fine units
local pos = Vector3.new( (50 * 64 + 32) * 512, 0.0, (50 * 64 + 32) * 512 )
local coordFine = CoordFine.new(0, pos)
```

## Constructors

### CoordFine(level, x, z)

```lua
function CoordFine.new(level : Integer, x : Float, z : Float) -> CoordFine
```

Constructs a CoordFine from the provided level and X & Z world positions.

Set the Y world position to a default of 0.0.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| level | Integer | The level of the coord (0-3). |
| x | Float | The X world position of the coord, in *Fine units*. |
| z | Float | The Z world position of the coord, in *Fine units*. |

> **Ejemplo**
> ```lua
> local worldX = ((50.0 * 64.0) + 32.0) * 512.0
> local worldZ = ((50.0 * 64.0) + 32.0) * 512.0
> local coordFine = CoordFine.new(0, worldX, worldZ)
> 
> -- Equivalent position vector
> local worldVec = Vector3.new(worldX, 0.0, worldZ)
> -- coordFine.position == worldVec
> 
> -- Equivalent CoordGrid
> local coordGrid = CoordGrid._0_50_50_32_32
> local coordFine2 = coordGrid.ToCoordFine(false)
> -- coordFine == coordFine2
> ```

### CoordFine(level, x, y, z)

```lua
function CoordFine.new(level : Integer, x : Float, y : Float, z : Float) -> CoordFine
```

Constructs a CoordFine from the provided level and X, Y & Z world positions.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| level | Integer | The level of the coord (0-3). |
| x | Float | The X world position of the coord, in *Fine units*. |
| y | Float | The Y world position of the coord, in *Fine units*. |
| z | Float | The Z world position of the coord, in *Fine units*. |

> **Ejemplo**
> ```lua
> local worldX = ((50.0 * 64.0) + 32.0) * 512.0
> local worldY = 2048.0
> local worldZ = ((50.0 * 64.0) + 32.0) * 512.0
> local coordFine = CoordFine.new(0, worldX, worldY, worldZ)
> 
> -- Equivalent position vector
> local worldVec = Vector3.new(worldX, worldY, worldZ)
> -- coordFine.position == worldVec
> 
> -- Converting to a CoordGrid and back to a CoordFine will lose the Y position
> local coordGrid = coordFine:ToCoordGrid()
> local coordFine2 = CoordFine.FromCoordGrid(coordGrid, false)
> -- coordFine != coordFine2
> ```

### CoordFine(level, position)

```lua
function CoordFine.new(level : Integer, position : Vector3) -> CoordFine
```

Constructs a CoordFine from the provided level and world position vector.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| level | Integer | The level of the coord (0-3). |
| position | Vector3 | The world position of the coord, in *Fine units*. |

> **Ejemplo**
> ```lua
> local worldX = ((50.0 * 64.0) + 32.0) * 512.0
> local worldY = 2048.0
> local worldZ = ((50.0 * 64.0) + 32.0) * 512.0
> local worldVec = Vector3.new(worldX, worldY, worldZ)
> local coordFine = CoordFine.new(0, worldVec)
> -- coordFine.position == worldVec
> 
> -- Converting to a CoordGrid and back to a CoordFine will lose the Y position
> local coordGrid = coordFine:ToCoordGrid()
> local coordFine2 = CoordFine.FromCoordGrid(coordGrid, false)
> -- coordFine != coordFine2
> ```

### CoordFine(coordGrid, fromCentre)

```lua
function CoordFine.new(coordGrid : CoordGrid, fromCentre : Boolean) -> CoordFine
```

Constructs a CoordFine from the provided CoordGrid.

Use `fromCentre` to indicate whether the resulting CoordFine `position` is:

* From the bottom-left of the tile, when `fromCentre = false`
* From the centre of the tile, when `fromCentre = true`

> **Información**
> The centre of a tile is 256 fine units from the bottom-left corner.

For example:

```text
-- Non-centred
local fineX = ((coordGrid.mapsquareX * 64) + coordGrid.localTileX) * 512
-- Centred
local fineX = (((coordGrid.mapsquareX * 64) + coordGrid.localTileX) * 512) + 256
```

Also see [CoordGrid:ToCoordFine](coordgrid.md#tocoordfine) and [CoordFine.FromCoordGrid](coordfine.md#fromcoordgrid)

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordGrid | CoordGrid | A coord grid position. |
| fromCentre | Boolean | Boolean value which indicates where to centre the constructed CoordFine. |

> **Ejemplo**
> ```lua
> local coordGrid0 = CoordGrid._0_50_50_32_32
> local coordFine1 = CoordFine.new(coordGrid0, false)
> local coordFine2 = CoordFine.new(coordGrid0, true)
> -- coordFine1.position != coordFine2.position
> 
> local coordGrid1 = coordFine1:ToCoordGrid()
> local coordGrid2 = coordFine2:ToCoordGrid()
> -- coordGrid0 == coordGrid1 == coordGrid2
> ```

### CoordFine(coordFine)

```lua
function CoordFine.new(coordFine : CoordFine) -> CoordFine
```

Constructs a CoordFine from the provided CoordFine.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordFine | CoordFine | A CoordFine position. |

> **Ejemplo**
> ```lua
> local coord1 = CoordFine.new(0, 2000.0, 100.0, 5000.0)
> local coord2 = CoordFine.new(coord1)
> -- coord1 == coord2
> ```

## Funciones

### FromCoordGrid

```lua
function CoordFine.FromCoordGrid(coordGrid : CoordGrid, fromCentre : Boolean) -> CoordFine
```

Returns a CoordFine constructed from the provided CoordGrid.

Use `fromCentre` to indicate whether the resulting CoordFine `position` is:

* From the bottom-left of the tile, when `fromCentre = false`
* From the centre of the tile, when `fromCentre = true`

> **Información**
> The centre of a tile is 256 fine units from the bottom-left corner.

For example:

```text
-- Non-centred
local fineX = ((coordGrid.mapsquareX * 64) + coordGrid.localTileX) * 512
-- Centred
local fineX = (((coordGrid.mapsquareX * 64) + coordGrid.localTileX) * 512) + 256
```

Also see [CoordGrid:ToCoordFine](coordgrid.md#tocoordfine) and [CoordFine(coordGrid, fromCentre)](coordfine.md#coordfinecoordgrid-fromcentre)

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordGrid | CoordGrid | A CoordGrid position. |
| fromCentre | Boolean | Boolean value which indicates where to centre the output CoordFine. |

| Retorna | Descripción |
| --- | --- |
| CoordFine | A CoordFine position. |

> **Ejemplo**
> ```lua
> local coordGrid0 = CoordGrid._0_50_50_32_32
> local coordFine1 = CoordFine.FromCoordGrid(coordGrid0, false)
> local coordFine2 = CoordFine.FromCoordGrid(coordGrid0, true)
> -- coordFine1.position != coordFine2.position
> 
> local coordGrid1 = coordFine1:ToCoordGrid()
> local coordGrid2 = coordFine2:ToCoordGrid()
> -- coordGrid0 == coordGrid1 == coordGrid2
> ```

## Métodos

### ToCoordGrid

```lua
function CoordFine:ToCoordGrid() -> CoordGrid
```

Returns a CoordGrid using the current CoordFine as a base.

The value of `level` is copied directly.  

The values of `position.x` and `position.z` are converted to *Grid Units*.  

The value of `position.y` is discarded.  

The Fine->Grid unit conversion is as follows:

```text
x = (int)(position.x / 512.0)
```

Also see [CoordGrid.FromCoordFine](coordgrid.md#fromcoordfine) and [CoordGrid(coordFine)](coordgrid.md#coordgridcoordfine)

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordFine | CoordFine | A CoordFine position. |

| Retorna | Descripción |
| --- | --- |
| CoordGrid | A CoordGrid position. |

> **Ejemplo**
> ```lua
> local worldX = ((50.0 * 64.0) + 32.0) * 512.0
> local worldZ = ((50.0 * 64.0) + 32.0) * 512.0
> local coordFine = CoordFine.new(0, worldX, worldZ)
> local coordGrid1 = coordFine:ToCoordGrid()
> local coordGrid2 = CoordGrid._0_50_50_32_32
> -- coordGrid1 == coordGrid2
> ```

## Propiedades

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| level | Integer |  | The level of this CoordFine. Valid range is 0-3. |
| x | Float |  | The world position X of this CoordFine, in *Fine units*. |
| y | Float |  | The world position Y of this CoordFine, in *Fine units*. |
| z | Float |  | The world position Z of this CoordFine, in *Fine units*. |
| position | Vector3 |  | The world position of this CoordFine, in *Fine units*. |
| mapSquareX | Integer |  | The mapsquare X of this CoordFine, in *Grid units*. Valid range is 0-199. |
| mapSquareZ | Integer |  | The mapsquare Z of this CoordFine, in *Grid units*. Valid range is 0-199. |
| localX | Integer |  | The local tile X of this CoordFine, in *Grid units*. Valid range is 0-63. |
| localZ | Integer |  | The local tile Z of this CoordFine, in *Grid units*. Valid range is 0-63. |