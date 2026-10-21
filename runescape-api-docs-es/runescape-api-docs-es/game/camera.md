# Camera

## Descripción General

La tabla `Camera` proporciona acceso a a game world's active camera.

## Funciones

### IsAvailable

```lua
function Camera.IsAvailable() -> Boolean
```

Indica si camera information está actualmente disponible.

| Retorna | Descripción |
| --- | --- |
| Boolean | Indica si la información de camera information está disponible para lectura. |

> **Ejemplo**
> ```lua
> if Camera.IsAvailable() then
>     local cameraPos = Camera.GetPosition()
>     ...
> end
> ```

### GetPosition

```lua
function Camera.GetPosition() -> Vector3
```

Devuelve la posición actual de the game world's camera.

El valor de retorno será `{0, 0, 0}` si la cámara no está disponible.

| Retorna | Descripción |
| --- | --- |
| [Vector3](../math/vector.md#vector3) | La posición de the camera, en unidades finas (fine units). |

> **Ejemplo**
> ```lua
> if Camera.IsAvailable() then
>     local cameraPos = Camera.GetPosition()
>     ...
> end
> ```

### GetFocusPosition

```lua
function Camera.GetFocusPosition() -> Vector3
```

Devuelve el/la focus position of the game world's camera actual.
This is typically the waist position of the Player Character during normal gameplay.

El valor de retorno será `{0, 0, 0}` si la cámara no está disponible.

| Retorna | Descripción |
| --- | --- |
| [Vector3](../math/vector.md#vector3) | The focus position of the camera, in fine units. |

> **Ejemplo**
> ```lua
> if Camera.IsAvailable() then
>     local cameraFocusPos = Camera.GetFocusPosition()
>     ...
> end
> ```