# Mouse

## Descripción General

The Mouse table contains functions which provide data belonging to the user's mouse input.

This data includes:

* Mouse availability (`false` on Mobile devices)
* Mouse position
* TODO position with UI scaling applied
* TODO mouse button states

> **Información**
> The mouse position:
> * is relative to the top-left of the game window, and
> * updates only when the mouse is within the bounds of the game window.

## Ejemplos

```lua
if Mouse.IsAvailable() then
    -- A Vector2 containing the mouse X & Y position
    local xy = Mouse.GetPosition()
    -- Or separately
    local x = Mouse.GetX()
    local y = Mouse.GetY()
end
```

## Funciones

### IsAvailable

```lua
function Mouse.IsAvailable() -> Boolean
```

Returns whether mouse data is available on the current platform.

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether mouse data can be polled on the current platform.Returns `false` on Mobile devices, and `true` on all others. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local mousePositionXY = Mouse.GetPosition()
> else
>     log("No mouse data available")
> end
> ```

### GetPosition

```lua
function Mouse.GetPosition() -> Vector2?
```

Devuelve el/la mouse X & Y position, if available actual.

| Retorna | Descripción |
| --- | --- |
| Vector2? | The current mouse position.Returns `nil` on Mobile devices. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local mousePositionXY = Mouse.GetPosition()
> end
> ```

### GetX

```lua
function Mouse.GetX() -> Integer?
```

Devuelve el/la mouse X position, if available actual.

| Retorna | Descripción |
| --- | --- |
| Integer? | The current X position of the mouse.Returns `nil` on Mobile devices. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local mousePositionX = Mouse.GetX()
> end
> ```

### GetY

```lua
function Mouse.GetY() -> Integer?
```

Devuelve el/la mouse Y position, if available actual.

| Retorna | Descripción |
| --- | --- |
| Integer? | The current Y position of the mouse.Returns `nil` on Mobile devices. |

> **Ejemplo**
> ```lua
> if Mouse.IsAvailable() then
>     local mousePositionY = Mouse.GetY()
> end
> ```