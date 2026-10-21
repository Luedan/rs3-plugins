# Rect

## Descripción General

`Rects` are used to represent an X and Y position with accompanying width and height dimensions.

> **Información**
> The X and Y positions are the Left and Top of the rectangle respectively.

## Ejemplos

```lua
-- A rectangle with the bottom left corner at 20,15 and
-- with a width of 100 and a height of 45
local rect = Rect.new(20, 15, 100, 45)
-- Another rectangle
local otherRect = Rect.new(50, 40, 20, 30)

-- Test intersections
local intersects = rect:Intersects(otherRect)
local containsPosition = rect:Contains(40, 30)

-- Modify
rect:Shrink(5)
rect:Grow(10, 15)
```

## Constructors

```lua
function Rect.new() -> Rect
function Rect.new(x : Float, y : Float, width : Float, height : Float) -> Rect
```

Creates and returns a rectangle with the provided values, or with all elements set to 0 if no arguments were provided.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| x | Float | Value to set the X element of the newly created rectangle to. |
| y | Float | Value to set the Y element of the newly created rectangle to. |
| width | Float | Value to set the width element of the newly created rectangle to. |
| height | Float | Value to set the height element of the newly created rectangle to. |

| Retorna | Descripción |
| --- | --- |
| `Rect` | The newly created rectangle |

## Métodos

### Translate

```lua
function Rect:Translate(offsetX : Float, offsetY : Float)
```

Moves the rectangle's X and Y elements by the given input values.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| offsetX | Float | The offset applied to the X element. |
| offsetY | Float | The offset applied to the Y element. |

> **Ejemplo**
> ```lua
> local rect = Rect.new(10, 20, 40, 30)
> rect:Translate(15, 100)
> -- { 25, 120, 40, 30 }
> ```

### Grow

```lua
function Rect:Grow(horizontal : Float, vertical : Float)
```

Increases **each edge** of the rectangle by the given horizontal and vertical values.

> **Información**
> The calculation for this method is:
> ```text
> rect.x -= horizontal
> rect.y -= vertical
> rect.width += horizontal * 2
> rect.height += vertical * 2
> ```

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| horizontal | Float | The expansion applied to the left and right edges of the rectangle. |
| vertical | Float | The expansion applied to the top and bottom edges of the rectangle. |

> **Ejemplo**
> ```lua
> local rect = Rect.new(10, 20, 40, 30)
> rect:Grow(10, 15)
> -- { 0, 5, 60, 60 }
> ```

### Shrink

```lua
function Rect:Shrink(horizontal : Float, vertical : Float)
```

Decreases **each edge** of the rectangle by the given horizontal and vertical values.

> **Información**
> The calculation for this method is:
> ```text
> rect.x += horizontal
> rect.y += vertical
> rect.width -= horizontal * 2
> rect.height -= vertical * 2
> ```

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| horizontal | Float | The reduction applied to the left and right edges of the rectangle. |
| vertical | Float | The reduction applied to the top and bottom edges of the rectangle. |

> **Ejemplo**
> ```lua
> local rect = Rect.new(40, 80, 50, 60)
> rect:Shrink(10, 15)
> -- { 50, 95, 30, 30 }
> ```

### Scale

```lua
function Rect:Scale(scale : Float)
```

Scales the rectangle about 0,0 by the given amount.

> **Información**
> The calculation for this method is:
> ```text
> rect.x *= scale
> rect.y *= scale
> rect.width *= scale
> rect.height *= scale
> ```

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| scale | Float | The scaling value to apply to all elements in the rectangle. |

> **Ejemplo**
> ```lua
> local rect = Rect.new(40, 80, 50, 60)
> rect:Scale(0.5)
> -- { 20, 40, 25, 30 }
> ```

### Contains(x, y)

```lua
function Rect:Contains(x : Float, y : Float) -> Boolean
```

Returns whether the given X and Y position is within this rectangle

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| x | Float | The X position to test. |
| y | Float | The Y position to test. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the given position is within this rectangle. |

> **Ejemplo**
> ```lua
> local rect = Rect.new(40, 80, 50, 60)
> rect:Contains(50, 100)
> -- true
> rect:Contains(30, 100)
> -- false
> ```

### Contains(rect)

```lua
function Rect:Contains(rect : Rect) -> Boolean
```

Returns whether the given other rectangle is entirely contained within this rectangle.

> **Información**
> This test fails if any element of the input rectangle lies outside the bounds of this rectangle.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| rect | [Rect](#rect) | The rectangle to test. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the given rectangle is within this rectangle. |

> **Ejemplo**
> ```lua
> local rect = Rect.new(40, 80, 50, 60)
> local smallerRect = Rect.new(50, 100, 20, 30)
> local overlappingRect = Rect.new(50, 60, 20, 30)
> local matchingRect = Rect.new(40, 80, 50, 60)
> rect:Contains(smallerRect)
> -- true
> rect:Contains(overlappingRect)
> -- false
> rect:Contains(matchingRect)
> -- true
> ```

### Intersects

```lua
function Rect:Intersects(rect : Rect) -> Boolean
```

Returns whether the given other rectangle intersects with this rectangle.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| rect | [Rect](#rect) | The rectangle to test. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the given rectangle intersects with this rectangle. |

> **Ejemplo**
> ```lua
> local rect = Rect.new(40, 80, 50, 60)
> local smallerRect = Rect.new(50, 100, 20, 30)
> local overlappingRect = Rect.new(50, 60, 20, 30)
> local separateRect = Rect.new(20, 80, 10, 60)
> rect:Intersects(smallerRect)
> -- true
> rect:Intersects(overlappingRect)
> -- true
> rect:Intersects(separateRect)
> -- false
> ```

### GetIntersection

```lua
function Rect:GetIntersection(rect : Rect) -> Rect?
```

Returns a rectangle which covers where the given rectangle and this rectangle intersect.

If there is no intersection, then `nil` is returned.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| rect | [Rect](#rect) | The rectangle to intersect with. |

| Retorna | Descripción |
| --- | --- |
| [Rect](#rect)? | The intersection rectangle.Returns `nil` if there is no intersection. |

> **Ejemplo**
> ```lua
> local rect = Rect.new(40, 80, 50, 60)
> local overlappingRect = Rect.new(50, 60, 20, 30)
> local separateRect = Rect.new(20, 80, 10, 60)
> rect:GetIntersection(overlappingRect)
> -- { 50, 80, 20, 10 }
> rect:GetIntersection(separateRect)
> -- nil
> ```

### GetUnion(rect)

```lua
function Rect:GetUnion(rect : Rect) -> Rect
```

Returns a rectangle which encompasses both the given rectangle and this rectangle.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| rect | [Rect](#rect) | The rectangle to union with. |

| Retorna | Descripción |
| --- | --- |
| [Rect](#rect) | The encompassing rectangle. |

> **Ejemplo**
> ```lua
> local rect = Rect.new(40, 80, 50, 60)
> local overlappingRect = Rect.new(50, 60, 20, 30)
> local separateRect = Rect.new(20, 80, 10, 60)
> rect:GetUnion(overlappingRect)
> -- { 40, 60, 50, 80 }
> rect:GetUnion(separateRect)
> -- { 20, 80, 70, 60 }
> ```

### GetUnion(x, y)

```lua
function Rect:GetUnion(x : Float, y : Float) -> Rect
```

Returns a rectangle which encompasses both the given X and Y position and this rectangle.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| x | Float | The X position to union with. |
| y | Float | The Y position to union with. |

| Retorna | Descripción |
| --- | --- |
| [Rect](#rect) | The encompassing rectangle. |

> **Ejemplo**
> ```lua
> local rect = Rect.new(40, 80, 50, 60)
> rect:GetUnion(0, 0)
> -- { 0, 0, 90, 140 }
> rect:GetUnion(60, 300)
> -- { 40, 80, 50, 220 }
> ```

## Propiedades

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| x | Float |  | The X position of the rectangle. |
| y | Float |  | The Y position of the rectangle. |
| width | Float |  | The width of the rectangle. |
| height | Float |  | The height of the rectangle. |
| left | Float |  | The left edge of the rectangle.`left = x` |
| top | Float |  | The upper edge of the rectangle.`top = y` |
| right | Float |  | The right edge of the rectangle.`right = x + width` |
| bottom | Float |  | The lower edge of the rectangle.`bottom = y + height` |
| centreX | Float |  | The X position of the centre point of the rectangle.`centreX = x + (width / 2)` |
| centreY | Float |  | The Y position of the centre point of the rectangle.`centreY = y + (height / 2)` |