# AABB

## Descripción General

An `AABB` (Axis-Aligned Bounding Box) is used to represent a 3D region in the world, which is aligned to the X, Y and Z axes.

They are constructed from two 3D positions in the world, which represent the minimum value corner and the maximum value corner.

## Ejemplos

```lua
-- An AABB which is
--  X: 0 -> 10
--  Y: -20 -> 100
--  Z: 40 -> 50
-- Minimum corner = (0, -20, 40)
-- Maximum corner = (10, 100, 50)
local aabb = AABB.new(Vector3.new(0, -20, 40), Vector3.new(10, 100, 50))
-- Another AABB
local otherAABB = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))

-- Test intersections
local intersects = aabb:Intersects(otherAABB)
local containsPosition = aabb:IsInside(Vector3.new(4, 70, 42))

-- Modify
aabb:ScaleFromCentre(Vector3.new(0.5, 0.5, 0.5))
aabb:AddPoint(Vector3.new(40, 200, 90))
```

## Enumeraciones

### BoxCornerType

Used with [AABB:GetCorner()](#getcorner) to select the position of a specific corner of an `AABB`.

> **Axis Terminology**
> Axis directions use the following terms:

| Name | Value |
| --- | --- |
| LEFT_TOP_NEAR | 0 |
| RIGHT_TOP_NEAR | 1 |
| LEFT_BOTTOM_NEAR | 2 |
| RIGHT_BOTTOM_NEAR | 3 |
| LEFT_TOP_FAR | 4 |
| RIGHT_TOP_FAR | 5 |
| LEFT_BOTTOM_FAR | 6 |
| RIGHT_BOTTOM_FAR | 7 |

## Constructors

```lua
function AABB.new(minimum : Vector3, maximum : Vector3) -> AABB
```

Creates and returns an `AABB` with the provided values.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| minimum | [Vector3](vector.md#vector3) | The minimum value on each axis. |
| maximum | [Vector3](vector.md#vector3) | The maximum value on each axis. |

| Retorna | Descripción |
| --- | --- |
| `AABB` | The newly created `AABB` |

## Métodos

### GetCorner

```lua
function AABB:GetCorner(corner : BoxCornerType) -> Boolean
```

Returns the position of the given corner type in this AABB.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| corner | [BoxCornerType](#boxcornertype) | The corner type. |

| Retorna | Descripción |
| --- | --- |
| [Vector3](vector.md#vector3) | The position of the corner. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:GetCorner(BoxCornerType.RIGHT_TOP_NEAR)
> -- { x = 45, y = 60, z = 10 }
> aabb:GetCorner(BoxCornerType.LEFT_BOTTOM_FAR)
> -- { x = 5, y = 50, z = 45 }
> ```

### IsInside(Vector3)

```lua
function AABB:IsInside(position : Vector3) -> Boolean
```

Returns whether the position is within the AABB

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| position | [Vector3](vector.md#vector3) | The position to test. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the given position is within this AABB. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:IsInside(Vector3.new(30, 55, 25))
> -- true
> aabb:IsInside(Vector3.new(0, 55, 25))
> -- false
> ```

### IsInside(AABB)

```lua
function AABB:IsInside(otherAABB : AABB) -> Boolean
```

Returns whether the given other AABB entirely encompasses this AABB.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| otherAABB | [AABB](aabb.md) | The AABB to test. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether this AABB is entirely with the given AABB. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:IsInside(AABB.new(Vector3.new(0, 40, 5), Vector3.new(50, 60, 60)))
> -- true
> aabb:IsInside(AABB.new(Vector3.new(6, 40, 5), Vector3.new(50, 60, 60)))
> -- false
> ```

### Intersects(Vector3, Vector3)

```lua
function AABB:Intersects(fromPosition : Vector3, toPosition : Vector3) -> Boolean
```

Returns whether the given line segment intersects with this AABB at any point.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| fromPosition | [Vector3](vector.md#vector3) | The line segment start position to test. |
| toPosition | [Vector3](vector.md#vector3) | The line segment end position to test. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether an intersection occurs. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:Intersects(Vector3.new(0, 0, 0), Vector3.new(100, 100, 100))
> -- false
> aabb:Intersects(Vector3.new(35, 40, 0), Vector3.new(20, 70, 60))
> -- true
> ```

### Intersects(AABB)

```lua
function AABB:Intersects(otherAABB : AABB) -> Boolean
```

Returns whether the given AABB intersects with this AABB at any point.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| otherAABB | [AABB](aabb.md) | The AABB to test. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether an intersection occurs. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:Intersects(AABB.new(Vector3.new(0, 0, 0), Vector3.new(100, 100, 100)))
> -- true
> aabb:Intersects(Vector3.new(10, 20, 30), Vector3.new(30, 70, 35))
> -- true
> aabb:Intersects(Vector3.new(10, 20, 30), Vector3.new(30, 40, 35))
> -- false
> ```

### GetClosestPosition

```lua
function AABB:GetClosestPosition(position : Vector3) -> Vector3
```

Returns the position on the AABB surface which is closest to the given position.
If the position is inside the AABB then the given position will be returned.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| position | [Vector3](vector.md#vector3) | The position to test. |

| Retorna | Descripción |
| --- | --- |
| [Vector3](vector.md#vector3) | The closest AABB surface position, or the given position if it is inside the AABB. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:GetClosestPosition(Vector3.new(10, 55, 30)) -- Inside the AABB
> -- { x = 10, y = 55, z = 30 }
> aabb:GetClosestPosition(Vector3.new(90, 80, 0)) -- Outside the AABB
> -- { x = 45, y = 60, z = 10 }
> ```

### GetFurthestPosition

```lua
function AABB:GetFurthestPosition(position : Vector3) -> Vector3
```

Returns the position on the AABB surface which is furthest to the given position.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| position | [Vector3](vector.md#vector3) | The position to test. |

| Retorna | Descripción |
| --- | --- |
| [Vector3](vector.md#vector3) | The furthest AABB surface position. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:GetFurthestPosition(Vector3.new(10, 55, 30)) -- Inside the AABB
> -- { x = 45, y = 60, z = 10 }
> aabb:GetFurthestPosition(Vector3.new(90, 80, 0)) -- Outside the AABB
> -- { x = 5, y = 50, z = 45 }
> ```

### GetDistanceToPosition

```lua
function AABB:GetDistanceToPosition(position : Vector3) -> Float
```

Returns the shortest distance from the given position to this AABB.
Will return `0.0` if the position is inside the AABB.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| position | [Vector3](vector.md#vector3) | The position to test. |

| Retorna | Descripción |
| --- | --- |
| Float | The closest distance from the position to the AABB, or `0` if the position is inside the AABB. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:GetDistanceToPosition(Vector3.new(10, 55, 30)) -- Inside the AABB
> -- 0.0
> aabb:GetDistanceToPosition(Vector3.new(90, 80, 0)) -- Outside the AABB
> -- 50.2493
> ```

### Translate

```lua
function AABB:Translate(offset : Vector3)
```

Moves the AABB's minimum and maximum elements by the given offset value.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| offset | [Vector3](vector.md#vector3) | The offset applied to the AABB. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:Translate(Vector3.new(10, 20, 30))
> -- { min = { 15, 70, 40 }, max = { 55, 80, 75 } }
> ```

### Scale

```lua
function AABB:Scale(scale : Vector3)
```

Scales the AABB about 0,0,0 by the given amount.

> **Información**
> The calculation for this method is:
> ```text
> aabb.minimum *= scale
> aabb.maximum *= scale
> ```

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| scale | [Vector3](vector.md#vector3) | The scaling value to apply to the AABB. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:Scale(Vector3.new(1.5, 2.0, 2.5))
> -- { min = { 7.5, 100, 25 }, max = { 67.5, 120, 112.5 } }
> ```

### ScaleFromCentre

```lua
function AABB:ScaleFromCentre(scale : Vector3)
```

Scales the AABB about the centre of the AABB by the given amount.

> **Información**
> The calculation for this method is:
> ```text
> aabb.minimum = (aabb.minimum - aabb.centre) * scale + aabb.centre
> aabb.maximum = (aabb.maximum - aabb.centre) * scale + aabb.centre
> ```

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| scale | [Vector3](vector.md#vector3) | The scaling value to apply to the AABB. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:ScaleFromCentre(Vector3.new(1.5, 2.0, 2.5))
> -- { min = { -5, 45, -16.25 }, max = { 55, 65, 71.25 } }
> ```

### AddPoint

```lua
function AABB:AddPosition(position : Vector3)
```

Expands this AABB to encompass the given position.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| position | [Vector3](vector.md#vector3) | The position to encompass. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:AddPosition(Vector3.new(-10, 20, 35))
> -- { min = { -10, 20, 10 }, max = { 45, 60, 45 } }
> ```

### AddAABB

```lua
function AABB:AddAABB(otherAABB : AABB)
```

Expands this AABB to encompass the given AABB.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| otherAABB | [AABB](aabb.md) | The AABB to encompass. |

> **Ejemplo**
> ```lua
> local aabb = AABB.new(Vector3.new(5, 50, 10), Vector3.new(45, 60, 45))
> aabb:AddAABB(AABB.new(Vector3.new(20, 45, 5), Vector3.new(55, 55, 35)))
> -- { min = { 5, 45, 5 }, max = { 55, 60, 45 } }
> ```

## Propiedades

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| minimum | [Vector3](vector.md#vector3) |  | The minimum values of each axis. |
| maximum | [Vector3](vector.md#vector3) |  | The maximum values of each axis. |
| dimensions | [Vector3](vector.md#vector3) |  | The width, height, and length values of the AABB. |
| centre | [Vector3](vector.md#vector3) |  | The centre position of the AABB. |
| minX | Float |  | The minimum value of the X axis. |
| minY | Float |  | The minimum value of the Y axis. |
| minZ | Float |  | The minimum value of the Z axis. |
| maxX | Float |  | The maximum value of the X axis. |
| maxY | Float |  | The maximum value of the Y axis. |
| maxZ | Float |  | The maximum value of the Z axis. |
| width | Float |  | The width of the AABB. |
| height | Float |  | The height of the AABB. |
| length | Float |  | The length of the AABB. |
| radiusMinimum | Float |  | The radius of a sphere centered inside the AABB that wholly contains the AABB at any orientation |
| radiusMinimumSq | Float |  | The squared radius of a sphere centered inside the AABB that wholly contains the AABB at any orientation |
| radiusMaximum | Float |  | The radius of a sphere centered inside the AABB that is the largest sphere that can fit inside this AABB |
| radiusMaximumSq | Float |  | The squared radius of a sphere centered inside the AABB that is the largest sphere that can fit inside this AABB |