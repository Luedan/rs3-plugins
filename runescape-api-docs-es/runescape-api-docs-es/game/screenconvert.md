# ScreenConvert

## Descripción General

The ScreenConvert table contains functions which will convert to and from screen positions and in-game coordinate positions.

> **Información**
> Conversions from a screen position into a [CoordGrid](coordgrid.md) or [CoordFine](coordfine.md) without supplying a `level` will output at the same level as the active player character.

## Ejemplos

```lua
-- The screen position at the feet of the player entity
local playerScreenPos = ScreenConvert.Vector3ToScreen(Player.GetEntity().position)

-- The tile currently under the mouse cursor
-- Outputs a tile at the same level as the player character
local coordGrid = ScreenConvert.ScreenToCoordGrid(Mouse.GetPosition())
-- This outputs a tile at the specified level instead
local coordGrid = ScreenConvert.ScreenToCoordGrid(Mouse.GetPosition(), 3)
```

## Funciones

### ScreenToCoordGrid(position)

```lua
function ScreenConvert.ScreenToCoordGrid(position : Vector2) -> CoordGrid?
```

Returns the [CoordGrid](coordgrid.md) under the given screen position.
Resulting coord will be on the same `level` as the player character.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| position | [Vector2](../math/vector.md#vector2) | The XY screen position to convert. |

| Retorna | Descripción |
| --- | --- |
| [CoordGrid](coordgrid.md)? | The tile coordinate to return.Returns `nil` if the active player or game world is unavailable, or if there is no tile beneath the given screen position. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local coordGrid = ScreenConvert.ScreenToCoordGrid(Mouse.GetPosition())
> end
> ```

### ScreenToCoordGrid(position, level)

```lua
function ScreenConvert.ScreenToCoordGrid(position : Vector2, level : Integer) -> CoordGrid?
```

Returns the [CoordGrid](coordgrid.md) for the specified level under the given screen position.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| position | [Vector2](../math/vector.md#vector2) | The XY screen position to convert. |
| level | Integer | The level to output the coordinate for.The value of `level` must be between `0` and `3`. |

| Retorna | Descripción |
| --- | --- |
| [CoordGrid](coordgrid.md)? | The tile coordinate to return.Returns `nil` if the game world is unavailable, the value of `level` is invalid, or if there is no tile beneath the given screen position. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local coordGrid = ScreenConvert.ScreenToCoordGrid(Mouse.GetPosition(), 3)
> end
> ```

### ScreenToCoordGrid(x, y)

```lua
function ScreenConvert.ScreenToCoordGrid(x : Integer, y : Integer) -> CoordGrid?
```

Returns the [CoordGrid](coordgrid.md) under the given screen X & Y positions.
Resulting coord will be on the same `level` as the player character.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| x | Integer | The X screen position to convert. |
| y | Integer | The Y screen position to convert. |

| Retorna | Descripción |
| --- | --- |
| [CoordGrid](coordgrid.md)? | The tile coordinate to return.Returns `nil` if the active player or game world is unavailable, or if there is no tile beneath the given screen position. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local coordGrid = ScreenConvert.ScreenToCoordGrid(Mouse.GetX(), Mouse.GetY())
> end
> ```

### ScreenToCoordGrid(x, y, level)

```lua
function ScreenConvert.ScreenToCoordGrid(x : Integer, y : Integer, level : Integer) -> CoordGrid?
```

Returns the [CoordGrid](coordgrid.md) for the specified level under the given screen X & Y positions.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| x | Integer | The X screen position to convert. |
| y | Integer | The Y screen position to convert. |
| level | Integer | The level to output the coordinate for.The value of `level` must be between `0` and `3`. |

| Retorna | Descripción |
| --- | --- |
| [CoordGrid](coordgrid.md)? | The tile coordinate to return.Returns `nil` if the game world is unavailable, the value of `level` is invalid, or if there is no tile beneath the given screen position. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local coordGrid = ScreenConvert.ScreenToCoordGrid(Mouse.GetX(), Mouse.GetY(), 3)
> end
> ```

### ScreenToCoordFine(position)

```lua
function ScreenConvert.ScreenToCoordFine(position : Vector2) -> CoordFine?
```

Returns the [CoordFine](coordfine.md) under the given screen position.
Resulting coord will be on the same `level` as the player character.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| position | [Vector2](../math/vector.md#vector2) | The XY screen position to convert. |

| Retorna | Descripción |
| --- | --- |
| [CoordFine](coordfine.md)? | The tile coordinate to return.Returns `nil` if the active player or game world is unavailable, or if there is no tile beneath the given screen position. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local coordFine = ScreenConvert.ScreenToCoordFine(Mouse.GetPosition())
> end
> ```

### ScreenToCoordFine(position, level)

```lua
function ScreenConvert.ScreenToCoordFine(position : Vector2, level : Integer) -> CoordFine?
```

Returns the [CoordFine](coordfine.md) for the specified level under the given screen position.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| position | [Vector2](../math/vector.md#vector2) | The XY screen position to convert. |
| level | Integer | The level to output the coordinate for.The value of `level` must be between `0` and `3`. |

| Retorna | Descripción |
| --- | --- |
| [CoordFine](coordfine.md)? | The tile coordinate to return.Returns `nil` if the game world is unavailable, the value of `level` is invalid, or if there is no tile beneath the given screen position. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local coordFine = ScreenConvert.ScreenToCoordFine(Mouse.GetPosition(), 3)
> end
> ```

### ScreenToCoordFine(x, y)

```lua
function ScreenConvert.ScreenToCoordFine(x : Integer, y : Integer) -> CoordFine?
```

Returns the [CoordFine](coordfine.md) under the given screen X & Y positions.
Resulting coord will be on the same `level` as the player character.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| x | Integer | The X screen position to convert. |
| y | Integer | The Y screen position to convert. |

| Retorna | Descripción |
| --- | --- |
| [CoordFine](coordfine.md)? | The tile coordinate to return.Returns `nil` if the active player or game world is unavailable, or if there is no tile beneath the given screen position. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local coordFine = ScreenConvert.ScreenToCoordFine(Mouse.GetX(), Mouse.GetY())
> end
> ```

### ScreenToCoordFine(x, y, level)

```lua
function ScreenConvert.ScreenToCoordFine(x : Integer, y : Integer, level : Integer) -> CoordFine?
```

Returns the [CoordFine](coordfine.md) for the specified level under the given screen X & Y positions.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| x | Integer | The X screen position to convert. |
| y | Integer | The Y screen position to convert. |
| level | Integer | The level to output the coordinate for.The value of `level` must be between `0` and `3`. |

| Retorna | Descripción |
| --- | --- |
| [CoordFine](coordfine.md)? | The tile coordinate to return.Returns `nil` if the game world is unavailable, the value of `level` is invalid, or if there is no tile beneath the given screen position. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local coordFine = ScreenConvert.ScreenToCoordFine(Mouse.GetX(), Mouse.GetY(), 3)
> end
> ```

### CoordGridToScreen

```lua
function ScreenConvert.CoordGridToScreen(coordGrid : CoordGrid, heightAboveGround : Integer) -> Vector2?
```

Returns the screen XY position, as a [Vector2](../math/vector.md#vector2), of the given [CoordGrid](coordgrid.md).
The position is calculated from the centre of the coordinate tile.
An optional in-game vertical offset `heightAboveGround`, which in *Fine units*, can be applied to the coordinate.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordGrid | [CoordGrid](coordgrid.md) | The tile coordinate to convert to a screen position.Calculations are made from the centre of the tile. |
| heightAboveGround | Integer | An additional vertical offset, in *Fine units*, to add to the tile position before converting. |

| Retorna | Descripción |
| --- | --- |
| Vector2? | The resulting screen XY position.Returns `nil` if the game world or ground data for the given coordinate is unavailable. |

> **Ejemplo**
> ```lua
> local screenPos = ScreenConvert.CoordGridToScreen(Player.GetEntity().coordGrid, 1024)
> if screenPos ~= nil then
>     -- A valid screen position above the player character's head
> end
> ```

### CoordFineToScreen

```lua
function ScreenConvert.CoordFineToScreen(coordFine : CoordFine, heightAboveGround : Integer) -> Vector2?
```

Returns the screen XY position, as a [Vector2](../math/vector.md#vector2), of the given [CoordFine](coordfine.md).
An optional in-game vertical offset `heightAboveGround`, which in *Fine units*, can be applied to the coordinate.

> **Información**
> The vertical component of `CoordFine.position.y` is ignored.
Only `CoordFine.position.x` and `CoordFine.position.z` are used to calculate the ground height at `CoordFine.level`.
The value of `heightAboveGround` is then added to the ground height before converting.

If you need to convert a position with an explicit vertical component, use [ScreenConvert.Vector3ToScreen](#vector3toscreen).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coordFine | [CoordFine](coordfine.md) | The tile coordinate to convert to a screen position.The vertical position component is ignored (see above). |
| heightAboveGround | Integer | An additional vertical offset, in *Fine units*, to add to the tile position before converting. |

| Retorna | Descripción |
| --- | --- |
| Vector2? | The resulting screen XY position.Returns `nil` if the game world or ground data for the given coordinate is unavailable. |

> **Ejemplo**
> ```lua
> local screenPos = ScreenConvert.CoordFineToScreen(Player.GetEntity().coordGrid:ToCoordFine(true), 1024)
> if screenPos ~= nil then
>     -- A valid screen position above the player character's head
> end
> ```

### Vector3ToScreen

```lua
function ScreenConvert.Vector3ToScreen(vec3 : Vector3) -> Vector2?
```

Returns the screen XY position, as a [Vector2](../math/vector.md#vector2), of the given [Vector3](../math/vector.md#vector3), in *Fine units*.

> **Información**
> This method does not perform a ground height look-up, and so will perform better than coordinate-to-screen conversions.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| vec3 | [Vector3](../math/vector.md#vector3) | The world position, in *Fine units*, to convert to a screen position. |

| Retorna | Descripción |
| --- | --- |
| Vector2? | The resulting screen XY position.Returns `nil` if the game world is unavailable. |

> **Ejemplo**
> ```lua
> local screenPos = ScreenConvert.Vector3ToScreen(Player.GetEntity().position + Vector3.new(0, 1024, 0))
> if screenPos ~= nil then
>     -- A valid screen position above the player character's head
> end
> ```