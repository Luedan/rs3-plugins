# Math

## Descripción General

The math module provides multiple primitives types such as [Vector](./vector.md) as well as various utility functions for calculating values.

## Funciones

### lerp

```lua
function lerp(start : Float, final : Float, t : Float) -> Float
function lerp(start : Vector2, final : Vector2, t : Float) -> Vector2
function lerp(start : Vector3, final : Vector3, t : Float) -> Vector3
function lerp(start : Vector4, final : Vector4, t : Float) -> Vector4
function lerp(start : Matrix33, final : Matrix33, t : Float) -> Matrix33
```

Calculates a linearly interpolated value based on starting and final values and an interpolation factor.

> **Advertencia**
> The interpolation factor used must be in a 0..1 range for this to yield a valid result.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| start | Float/Vector2/Vector3/Vector4/Matrix33 | Starting value used in interpolation. |
| final | Float/Vector2/Vector3/Vector4/Matrix33 | Final value used in interpolation. |
| t | Float | Interpolation percentage between start and end values. |

| Retorna | Descripción |
| --- | --- |
| Float/Vector2/Vector3/Vector4/Matrix33 | Resulting value from interpolating between start and end. |

> **Ejemplo**
> ```lua
> print(lerp(1.0, 5.0, 0.5)) -- 3.0
> ```
> ```lua
> local start = Vector2.new(0.3, 1.0)
> local final = Vector2.new(0.0, 5.0)
> print(lerp(start, final, 0.5)) -- 0.15, 3.0
> print(lerp(start, final, 1.0)) -- 0.0, 5.0
> ```

### slerp

```lua
function slerp(start : Vector3, final : Vector3, t : Float) -> Vector3
function slerp(start : Quaternion, final : Quaternion, t : Float) -> Quaternion
```

Calculates a spherically interpolated value based on starting and final values and an interpolation factor.

> **Información**
> This is generally used for rotations, where just using linear interpolation instead would yield non-normalised results, resulting in an invalid rotation value.

> **Advertencia**
> The interpolation factor used must be in a 0..1 range for this to yield a valid result.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| start | Vector3/Quaternion | Starting value used in interpolation. |
| final | Vector3/Quaternion | Final value used in interpolation. |
| t | Float | Interpolation percentage between start and end values. |

| Retorna | Descripción |
| --- | --- |
| Vector3/Quaternion | Resulting value from interpolating between start and end. |

> **Ejemplo**
> ```lua
> local target = Vector3.new(10, 0.0, 0.0)
> local origin = Vector3.new(0.0, 0.0, 10.0)
> local delta = target - origin
> 
> local originalDirection = Vector3.new(0.0, 0.0, 1.0)
> local targetDirection = delta:Normalise()
> 
> local interpolated = slerp(originalDirection, targetDirection, 0.3)
> ```

### clamp

```lua
function clamp(value : Float, min : Float, max : Float) -> Float
```

Limits a value to the provided range.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| value | Float | Value to clamp. |
| min | Float | Minimum value that can be returned. |
| max | Float | Maximum value that can be returned. |

| Retorna | Descripción |
| --- | --- |
| Float | The resulting value clamped to the provided min and max range. |

> **Ejemplo**
> ```lua
> print(clamp(0.3, 0.0, 1.0))     -- 0.3
> print(clamp(-0.3, 0.0, 1.0))    -- 0.0
> print(clamp(1.3, 0.0, 1.0))     -- 1.0
> ```

### random

```lua
function random(min : Float, max : Float) -> Float
```

Calculates a random value in the specified range.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| min | Float | Minimum value that can be returned. |
| max | Float | Maximum value that can be returned. |

| Retorna | Descripción |
| --- | --- |
| Float | The randomly calculated value within the specified range |

> **Ejemplo**
> ```lua
> print(random(0, 1)) -- 0.19
> print(random(0, 1)) -- 0.82
> print(random(0, 100)) -- 75.8
> print(random(0, 100)) -- 1.2
> ```