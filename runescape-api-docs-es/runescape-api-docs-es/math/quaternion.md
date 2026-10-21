# Quaternion

## Descripción General

Quaternions are 4-dimensional vectors that are used to represent rotations.

## Ejemplos

```lua
local rotation = Quaternion.fromYawPitchRoll(0.3, 0.0, 2.0)
local otherRotation = Quaternion.fromYawPitchRoll(0.0, 1.5, 0.0)
local finalRotation = rotation:RotateBy(otherRotation)
local v = Vector3.new(0.0, 1.0, 0.0)
local rotatedV = v:Rotate(finalRotation)
```

## Métodos and Properties

### fromYawPitchRoll

```lua
function Quaternion.fromYawPitchRoll(yaw : Float, pitch : Float, roll : Float) -> Quaternion
```

Constructs a quaternion from the provided yaw, pitch, and roll values.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| yaw | Float | Yaw rotation in radians. |
| pitch | Float | Pitch rotation in radians. |
| roll | Float | Roll rotation in radians. |

| Retorna | Descripción |
| --- | --- |
| Vector | Contains the absolute value representation of the provided vector. |

> **Ejemplo**
> ```lua
> local a = Quaternion.fromYawPitchRoll(0.3, 0.0, 2.0)
> ```

### fromMatrix

```lua
function Quaternion.fromMatrix(source : Matrix33) -> Quaternion
```

Constructs a quaternion from the provided rotation matrix.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| source | Matrix33 | Matrix containing the rotation to convert. |

| Retorna | Descripción |
| --- | --- |
| Quaternion | Quaternion representing the rotation contained in the provided matrix. |

> **Ejemplo**
> ```lua
> local mat = Matrix33.rotationY(2.0)
> local quaternion = Quaternion.fromMatrix(mat)
> ```

### rotateBy

```lua
function Quaternion:rotateBy(rotation : Quaternion) -> Quaternion
```

Constructs a quaternion representing the rotation of the source quaternion by the provided rotation quaternion.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| rotation | Quaternion | Represents the rotation to apply. |

| Retorna | Descripción |
| --- | --- |
| Quaternion | Result of rotating the current quaternion by the rotation quaternion. |

> **Ejemplo**
> ```lua
> local rotation = Quaternion.fromYawPitchRoll(0.3, 0.0, 2.0)
> local otherRotation = Quaternion.fromYawPitchRoll(0.0, 1.5, 0.0)
> local finalRotation = rotation:RotateBy(otherRotation)
> ```