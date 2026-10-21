# Vector

## Descripción General

Vectors are used to represent positional and colour data, and can contain between 2, 3, or 4 float values.

## Ejemplos

```lua
local v = Vector2.new(0.3, 10.0)
v = v + Vector.new(5.0, 0.1)
print(v.x, v.y) -- 5.3, 10.1

print(v:Dot(Vector2.new(1.0, 0.0))) -- 5.3
```

```lua
local v = Vector3.new(5.0)
print(v.x, v.y, v.z) -- 5.0, 5.0, 5.0

v.y = -3.1
v.z = v.z - 9.5
print(v.x, v.y, v.z) -- 5.0, -3.1, -4.5

v = v:Abs()
print(v.x, v.y, v.z) -- 5.0, 3.1, 4.5
```

```lua
local colour = Vector4.new(1.0, 0.5, 0.0, 1.0)
colour = colour * Vector4.new(1.0, 0.0, 0.0, 1.0)
print(colour.x, colour.y, colour.z, colour.w) -- 1.0, 0.0, 0.0, 1.0
print(colour.r, colour.g, colour.b, colour.a) -- 1.0, 0.0, 0.0, 1.0

local rgbOnly = colour.rgb
rgbOnly = rgbOnly + Vector3.new(0.0, 0.3, 0.7)
print(rgbOnly.x, rgbOnly.y, rgbOnly.z) -- 1.0, 0.3, 0.7
print(rgbOnly.r, rgbOnly.g, rgbOnly.b) -- 1.0, 0.3, 0.7
```

## Common Methods and Properties

The methods/properties listed under this section are available on vectors regardless of their size.

> **Información**
> Whenever the Vector type appears as a parameter/return type, unless otherwise stated this represents a vector of the same size as the object that function was called on.

### Abs

```lua
function Vector:Abs() -> Vector
```

Computes the absolute value representation for the provided vector and returns it.

| Retorna | Descripción |
| --- | --- |
| Vector | Contains the absolute value representation of the provided vector. |

> **Ejemplo**
> ```lua
> local a = Vector2.new(1.4, -5.8)
> a = Vector2:Abs()
> print(a.x, a.y) -- 1.4, 5.8
> ```

### Ceil

```lua
function Vector:Ceil() -> Vector
```

Returns a vector where each element is the smallest integer that's greater than the original element.

| Retorna | Descripción |
| --- | --- |
| Vector | Contains the result from ceil'ing each of the original vector's elements. |

> **Ejemplo**
> ```lua
> local a = Vector2.new(1.4, -5.8)
> a = Vector2:Ceil()
> print(a.x, a.y) -- 2.0, -5.0
> ```

### Floor

```lua
function Vector:Floor() -> Vector
```

Returns a vector where each element is the largest integer that's not greater than the original element.

| Retorna | Descripción |
| --- | --- |
| Vector | Contains the result from floor'ing each of the original vector's elements. |

> **Ejemplo**
> ```lua
> local a = Vector2.new(1.4, -5.8)
> a = Vector2:Floor()
> print(a.x, a.y) -- 1.0, -6.0
> ```

### Dot

```lua
function Vector:Dot(other : Vector) -> Float
```

Returns the dot-product of two vectors.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| other | Vector | Vector to compare elements to. |

| Retorna | Descripción |
| --- | --- |
| Vector | Contains the maximum elements of both vectors. |

> **Ejemplo**
> ```lua
> local a = Vector2.new(1, 5)
> local b = Vector2.new (-2, 10)
> print(a:Dot(b)) -- 48
> ```
> ```lua
> local a = Vector3.new(0.5, -50, 10)
> local b = Vector3.new (5, 0, -40)
> print(a:Dot(b)) -- -397.5
> ```

### Max

```lua
function Vector:Max(other : Vector) -> Vector
```

Returns an element-wise maximum between two vectors.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| other | Vector | Vector to compare elements to. |

| Retorna | Descripción |
| --- | --- |
| Vector | Contains the maximum elements of both vectors. |

> **Ejemplo**
> ```lua
> local a = Vector3.new(0.5, -50, 10)
> local b = Vector3.new (5, 0, -40)
> local c = a:Max(b)
> print(c.x, c.y, c.z) -- 5, 0, 10
> ```

### Min

```lua
function Vector:Min(other : Vector) -> Vector
```

Returns an element-wise minimum between two vectors.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| other | Vector | Vector to compare elements to. |

| Retorna | Descripción |
| --- | --- |
| Vector | Contains the minimum elements of both vectors. |

> **Ejemplo**
> ```lua
> local a = Vector3.new(0.5, -50, 10)
> local b = Vector3.new (5, 0, -40)
> local c = a:Min(b)
> print(c.x, c.y, c.z) -- 0.5, -50, -40
> ```

### Normalise

```lua
function Vector:Normalise()
```

Normalises the current vector, rescaling its elements so it becomes a vector of length 1.
Does nothing if all elements of the vector are 0.

> **Ejemplo**
> ```lua
> local v = Vector2.new(5, -2)
> v:Normalise()
> print(v.x, v.y) -- 0.93, -0.37
> ```
> ```lua
> local v = Vector3.new(1.0, 0.5, 0.5)
> v:Normalise()
> print(v.x, v.y, v.z) -- 0.82, 0.41, 0.41
> ```
> ```lua
> local v = Vector4.new(0.0)
> v:Normalise()
> print(v.x, v.y, v.z, v.w) -- 0.0, 0.0, 0.0, 0.0
> ```

### NormaliseSafe

```lua
function Vector:Normalise(fallback : Vector) -> Vector
```

Returns a normalised version of the provided vector, with its elements rescaled so it becomes a vector of length 1.

If all of the provided vector's elements are 0, returns the fallback vector instead.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| fallback | Vector | Value to return if all elements on the vector this was called on are 0. |

| Retorna | Descripción |
| --- | --- |
| Vector | Normalised version of the caller or the fallback if the caller had length 0 |

> **Ejemplo**
> ```lua
> local target = Vector3.new(10, 0.0, 0.0)
> local origin = Vector3.new(0.0, 0.0, 10.0)
> local delta = target - origin
> 
> local direction = delta:NormaliseSafe(Vector3.new(0.0, 0.0, 1.0))
> -- Always safe to use direction vector regardless of whether delta's length was 0 or not
> ```

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| isNormal | Bool | **(Read-only)** True if this is a unit-length vector. |
| length | Float | **(Read-only)** Length value for this vector. |
| lengthSq | Float | **(Read-only)** Squared length value for this vector. Faster to calculate than length. |
| invLength | Float | **(Read-only)** Inverse of the length value for this vector, equivalent to 1.0 / length. |

## Vector2

Additional properties and methods provided for Vector2 types.

### Constructors

```lua
function Vector2.new() -> Vector2
function Vector2.new(v : Float) -> Vector2
function Vector2.new(x : Float, y : Float) -> Vector2
```

Creates and returns a vector with the provided values, or with all elements set to 0 if no arguments were provided.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| v | Float | Value to set all elements of the newly created vector to. |
| x | Float | Value to set the first element of the newly created vector to. |
| y | Float | Value to set the second element of the newly created vector to. |

| Retorna | Descripción |
| --- | --- |
| Vector2 | The newly created element |

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| x | Float | First element in this vector. |
| y | Float | Second element in this vector. |
| u | Float | First element in this vector, aliasing x. |
| v | Float | Second element in this vector, aliasing y. |

> **Información**
> The following aliases are supported:
> * u/v -> x/y

## Vector3

Additional properties and methods provided for Vector3 types.

### Constructors

```lua
function Vector3.new() -> Vector3
function Vector3.new(v : Float) -> Vector3
function Vector3.new(x : Float, y : Float, z : Float) -> Vector3
```

Creates and returns a vector with the provided values, or with all elements set to 0 if no arguments were provided.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| v | Float | Value to set all elements of the newly created vector to. |
| x | Float | Value to set the first element of the newly created vector to. |
| y | Float | Value to set the second element of the newly created vector to. |
| z | Float | Value to set the third element of the newly created vector to. |

| Retorna | Descripción |
| --- | --- |
| Vector3 | The newly created element |

### Cross

```lua
function Vector3:Cross(other : Vector3) -> Vector3
```

Returns the cross-product of two 3D vectors.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| other | Vector3 | Vector to calculate the cross-product against. |

| Retorna | Descripción |
| --- | --- |
| Vector3 | Contains the maximum elements of both vectors. |

> **Ejemplo**
> ```lua
> local a = Vector3.new(0.5, -50, 10)
> local b = Vector3.new (5, 0, -40)
> local c = a:Cross(b)
> print(c.x, c.y, c.z) -- 2000, 70, 250
> ```

### Reflect

```lua
function Vector3:Cross(normal : Vector3) -> Vector3
```

Calculates the reflection of the current vector along the provided normal.

> **Advertencia**
> Both vectors should be normalised prior to calling this method to ensure a sane value is returned.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| normal | Vector3 | Vector treated as the normal for the surface to calculate the reflection on. |

| Retorna | Descripción |
| --- | --- |
| Vector3 | Contains the reflection of the source vector on the provided surface normal. |

> **Ejemplo**
> ```lua
> local a = Vector3.new(0.5, -50, 10):Normalise()
> local b = Vector3.new(5, 0, -40):Normalise()
> local c = a:Reflect(b)
> ```

### Rotate

```lua
function Vector3:Rotate(rotation : Quaternion) -> Vector3
```

Calculates the result of rotating this vector by the provided quaternion.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| rotation | [Quaternion](./quaternion.md) | Quaternion describing the rotation to apply. |

| Retorna | Descripción |
| --- | --- |
| Vector3 | Contains the result of rotating the source vector by the provided quaternion. |

> **Ejemplo**
> ```lua
> local v = Vector3.new(1.0, 0.0, 0.0)
> local rotation = Quaternion.fromYawPitchRoll(160.0, 0.0, 0.0)
> v = v:Rotate(rotation)
> ```

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| x | Float | First element in this vector. |
| y | Float | Second element in this vector. |
| z | Float | Third element in this vector. |

> **Información**
> The following aliases are supported:
> * r/g/b -> x/y/z

## Vector4

Additional properties and methods provided for Vector4 types.

### Constructors

```lua
function Vector4.new() -> Vector4
function Vector4.new(v : Float) -> Vector4
function Vector4.new(x : Float, y : Float, z : Float, w : Float) -> Vector4
function Vector4.new(xy : Vector2, zw : Vector2) -> Vector4
```

Creates and returns a vector with the provided values, or with all elements set to 0 if no arguments were provided.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| v | Float | Value to set all elements of the newly created vector to. |
| x | Float | Value to set the first element of the newly created vector to. |
| y | Float | Value to set the second element of the newly created vector to. |
| z | Float | Value to set the third element of the newly created vector to. |
| w | Float | Value to set the fourth element of the newly created vector to. |
| xy | Vector2 | Value to set the first and second elements of the newly created vector to. |
| zw | Vector2 | Value to set the third and fourth elements of the newly created vector to. |

| Retorna | Descripción |
| --- | --- |
| Vector4 | The newly created element |

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| x | Float | First element in this vector. |
| y | Float | Second element in this vector. |
| z | Float | Third element in this vector. |
| w | Float | Fourth element in this vector. |
| xyz | Vector3 | **(Read-only)** Returns x, y, and z as a separate vector. |
| xy | Vector2 | **(Read-only)** Returns x and y as a separate vector. |
| zw | Vector2 | **(Read-only)** Returns z and w as a separate vector. |

> **Información**
> The following aliases are supported:
> * r/g/b/a -> x/y/z/w
> * rgb -> xyz