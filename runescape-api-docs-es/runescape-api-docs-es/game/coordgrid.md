# CoordGrid

## Descripción General

A CoordGrid represents a position within the game world's tile system, in *Grid units*, as opposed to the 3D world position found in CoordFine, which is in *Fine units*.

## Ejemplos

```lua
-- Absolute coord position
-- Level (0-3), Mapsquare X (0-199), Mapsquare Z (0-199), Local Tile X (0-63), Local Tile Z (0-63)
local coord = CoordGrid.new(0, 49, 52, 17, 8)

-- Centre of a mapsquare
-- Equivalent to CoordGrid.new(0, 49, 52, 32, 32)
local centreCoord = CoordGrid.new(0, 49, 52)

-- Utility shorthand for the previous examples
local coordAlt = CoordGrid._0_49_52_17_8
local centreCoordAlt = CoordGrid._0_49_52
```

## Constructors

### CoordGrid(bitPacked)

```lua
function CoordGrid.new(bitPacked : Integer) -> CoordGrid
```

Constructs a CoordGrid from the provided numeric value.

This value is a packed representation of the coordinate, useful for storing as a single 32-bit integer.  

The coordinate data is packed as follows:
`(level << 28) |  (x << 14) | (z)`

Also see [CoordGrid:ToPacked](coordgrid.md#topacked)

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| bitPacked | Integer | The packed representation of a CoordGrid. |

> **Ejemplo**
> ```lua
> local coord1 = CoordGrid._50_50_32_32
> local packedCoord = coord1:ToPacked()
> local coord2 = CoordGrid.new(packedCoord)
> -- coord1 == coord2
> ```

### CoordGrid(level, mapSquareX, mapSquareZ)

```lua
function CoordGrid.new(level : Integer, mapSquareX : Integer, mapSquareZ : Integer) -> CoordGrid
```

Constructs a CoordGrid from the provided level and mapsquare X & Z values.

This constructor auto-fills the local tile X & Z values to be the centre of the mapsquare:

```text
CoordGrid.new(1, 43, 56) == CoordGrid.new(1, 43, 56, 32, 32)
```

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| level | Integer | The level of the coord (0-3). |
| mapSquareX | Integer | The mapsquare X-dimension of the coord (0-199). |
| mapSquareZ | Integer | The mapsquare Z-dimension of the coord (0-199). |

> **Ejemplo**
> ```lua
> local coord1 = CoordGrid._0_50_50_32_32
> local coord2 = CoordGrid.new(0, 50, 50)
> -- coord1 == coord2
> ```

### CoordGrid(level, mapSquareX, mapSquareZ, localTileX, localTileZ)

```lua
function CoordGrid.new(level : Integer, mapSquareX : Integer, mapSquareZ : Integer, localTileX : Integer, localTileZ : Integer) -> CoordGrid
```

Constructs a CoordGrid from the provided level, mapsquare and tile X & Z values.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| level | Integer | The level of the coord (0-3). |
| mapSquareX | Integer | The mapsquare X-dimension of the coord (0-199). |
| mapSquareZ | Integer | The mapsquare Z-dimension of the coord (0-199). |
| localTileX | Integer | The local tile X-dimension of the coord (0-63). |
| localTileZ | Integer | The local tile Z-dimension of the coord (0-63). |

> **Ejemplo**
> ```lua
> local coord1 = CoordGrid._0_4_21_44_12
> local coord2 = CoordGrid.new(0, 4, 21, 44, 12)
> -- coord1 == coord2
> ```

### CoordGrid(level, position)

```lua
function CoordGrid.new(level : Integer, position : Vector3) -> CoordGrid
```

Constructs a CoordGrid from the provided level and 3D world position.

The values of `position.x` and `position.z` should be in *Fine units* and will be converted to *Grid units* by the constructor.  

The value of `position.y` is discarded.  

The Fine->Grid unit conversion is as follows:

```text
x = (int)(position.x / 512.0)
```

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| level | Integer | The level of the coord (0-3). |
| position | Vector3 | A 3D world position in Fine units. |

> **Ejemplo**
> ```lua
> local coord1 = CoordGrid._0_51_42_10_24
> -- X & Z are in Fine units: ((mapSquare * 64) + localTile) * 512
> local worldPos = Vector3.new( ((51 * 64) + 10) * 512, 0.0, ((42 * 64) + 24) * 512 )
> local coord2 = CoordGrid.new(0, worldPos)
> -- coord1 == coord2
> ```

### CoordGrid(coordFine)

```lua
function CoordGrid.new(coordFine : CoordFine) -> CoordGrid
```

Constructs a CoordGrid from the provided CoordFine.

The value of `coordFine.level` is copied directly.  

The values of `coordFine.position.x` and `coordFine.position.z` are converted to *Grid Units*.  

The value of `coordFine.position.y` is discarded.  

The Fine->Grid unit conversion is as follows:

```text
x = (int)(position.x / 512.0)
```

Also see [CoordFine:ToCoordGrid](coordfine.md#tocoordgrid) and [CoordGrid.FromCoordFine](coordgrid.md#fromcoordfine)

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordFine | CoordFine | A CoordFine position. |

> **Ejemplo**
> ```lua
> local coord1 = CoordGrid._0_50_50_32_32
> local coordFine = coord1:ToCoordFine(false)
> local coord2 = CoordGrid.new(coordFine)
> -- coord1 == coord2
> ```

### CoordGrid(coordGrid)

```lua
function CoordGrid.new(coordGrid : CoordGrid) -> CoordGrid
```

Constructs a CoordGrid from the provided CoordGrid.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordGrid | CoordGrid | A CoordGrid position. |

> **Ejemplo**
> ```lua
> local coord1 = CoordGrid._0_50_50_32_32
> local coord2 = CoordGrid.new(coord1)
> -- coord1 == coord2
> ```

## Funciones

### FromCoordFine

```lua
function CoordGrid.FromCoordFine(coordFine : CoordFine) -> CoordGrid
```

Returns a CoordGrid constructed from the provided CoordFine.

The value of `coordFine.level` is copied directly.  

The values of `coordFine.position.x` and `coordFine.position.z` are converted to *Grid Units*.  

The value of `coordFine.position.y` is discarded.  

The Fine->Grid unit conversion is as follows:

```text
x = (int)(position.x / 512.0)
```

Also see [CoordFine:ToCoordGrid](coordfine.md#tocoordgrid) and [CoordGrid(coordFine)](coordgrid.md#coordgridcoordfine)

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordFine | CoordFine | A CoordFine position. |

| Retorna | Descripción |
| --- | --- |
| CoordGrid | A CoordGrid position. |

> **Ejemplo**
> ```lua
> local coord1 = CoordGrid._0_50_50_32_32
> local coordFine = coord1:ToCoordFine(false)
> local coord2 = CoordGrid.FromCoordFine(coordFine)
> -- coord1 == coord2
> ```

## Métodos

### ToPacked

```lua
function CoordGrid:ToPacked() -> Integer
```

Returns a numeric value which is a packed representation of the coordinate, useful for storing as a single 32-bit integer.  

The coordinate data is packed as follows:
`(level << 28) |  (x << 14) | (z)`

| Retorna | Descripción |
| --- | --- |
| Integer | The numeric value representing a CoordGrid. |

> **Ejemplo**
> ```lua
> local coord1 = CoordGrid._0_50_50_32_32
> local packedCoord = coord1:ToPacked()
> local coord2 = CoordGrid.new(packedCoord)
> -- coord1 == coord2
> ```

### ToCoordFine

```lua
function CoordGrid:ToCoordFine(fromCentre : Boolean) -> CoordFine
```

Returns a CoordFine using the current CoordGrid as a base.

Use `fromCentre` to indicate whether the CoordFine `position` is:

* From the bottom-left of the tile, when `fromCentre = false`
* From the centre of the tile, when `fromCentre = true`

> **Información**
> The centre of a tile is 256 fine units from the bottom-left corner.

For example:

```text
-- Non-centred
local fineX = ((mapsquareX * 64) + localTileX) * 512
-- Centred
local fineX = (((mapsquareX * 64) + localTileX) * 512) + 256
```

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| fromCentre | Boolean | Boolean value which indicates where to centre the output CoordFine. |

| Retorna | Descripción |
| --- | --- |
| CoordFine | A CoordFine position. |

> **Ejemplo**
> ```lua
> local coord1 = CoordGrid._0_50_50_32_32
> local coordFine = coord1:ToCoordFine(false)
> local coordFineCentred = coord1:ToCoordFine(true)
> 
> -- Both CoordFines will output the same CoordGrid after being converted from Fine units to Grid units
> local coord2 = CoordGrid.new(coordFine)
> local coord3 = CoordGrid.new(coordFineCentred)
> -- coord1 == coord2 == coord3
> ```

## Propiedades

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| level | Integer |  | The level of this CoordGrid. Valid range is 0-3. |
| x | Integer |  | The world tile X of this CoordGrid, in *Grid units*. Valid range is 0-12799. |
| z | Integer |  | The world tile Z of this CoordGrid, in *Grid units*. Valid range is 0-12799. |
| mapSquareX | Integer |  | The mapsquare X of this CoordGrid, in *Grid units*. Valid range is 0-199. |
| mapSquareZ | Integer |  | The mapsquare Z of this CoordGrid, in *Grid units*. Valid range is 0-199. |
| localX | Integer |  | The local tile X of this CoordGrid, in *Grid units*. Valid range is 0-63. |
| localZ | Integer |  | The local tile Z of this CoordGrid, in *Grid units*. Valid range is 0-63. |