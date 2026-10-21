# Matrix33

## Descripción General

Matrix type representing a 3D rotation and/or scale operation, containing 3 rows and 3 columns.

## Métodos and Properties

### rotationY

```lua
function Matrix33.rotationY(rotationAmount : Float) -> Matrix33
```

Constructs a 3x3 rotation matrix representing a rotation around the y-axis.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| rotationAmount | Float | Amount to rotate the y-axis about, in radians. |

| Retorna | Descripción |
| --- | --- |
| Matrix33 | The resulting rotation matrix. |

> **Ejemplo**
> ```lua
> local mat = Matrix33.rotationY(0.3)
> ```

### fromQuaternion

```lua
function Matrix33.fromQuaternion(rotation : Quaternion) -> Matrix33
```

Constructs a 3x3 rotation matrix representing the provided quaternion.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| rotation | Quaternion | Rotation to convert. |

| Retorna | Descripción |
| --- | --- |
| Matrix33 | The provided rotation converted to a matrix. |

> **Ejemplo**
> ```lua
> local rotation = Quaternion.fromYawPitchRoll(0.3, 0.0, 2.0)
> local mat = Matrix33.fromQuaternion(rotation)
> ```