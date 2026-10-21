# World

## Descripción General

The World table contains access to a variety of information about the current game world.

## Enumeraciones

### HeightOffsetType

Used with [World.GetGroundHeight()](#getgroundheight) to apply additional offsets to the ground height, depending on the type of [LocEntity](entity/locentity.md) placed at the sampled position.

| Name | Valor | Descripción |
| --- | --- | --- |
| NONE | 0 | Applies no offset to the ground height |
| GROUND_DECOR | 1 | Applies any offset from a [LocEntity](entity/locentity.md) using [LocShapeType.GROUNDDECOR](config/loctype.md#locshapetype), i.e. a rug.See [LocType.groundDecorOffset](config/loctype.md#properties). |
| LOCATION | 2 | Offsets the height by the total height of the [LocEntity](entity/locentity.md), i.e. a table. |

## Funciones

### IsAvailable

```lua
function World.IsAvailable() -> Boolean
```

Returns whether the world data can currently be accessed.

| Retorna | Descripción |
| --- | --- |
| Boolean | Indica si la información de the world data está disponible para lectura. |

> **Ejemplo**
> ```lua
> if World.IsAvailable() then
>     local coord = CoordGrid._0_50_50_32_32
>     local coordPos = coord:ToFine(true).position
>     local height = World.GetGroundHeight(coord.level, coordPos.x, coordPos.z)
> end
> ```

### IsMembers

```lua
function World.IsMembers() -> Boolean
```

Returns whether the currently connected world is a Member's world.

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the world is a Member's world. |

> **Ejemplo**
> ```lua
> if World.IsMembers() then
>     -- Do something with the value
> end
> ```

### GetPing

```lua
function World.GetPing() -> Integer
```

Returns the ping value to the current game world.

This function will return `-1` if there is no active connection to a game world.

> **Información**
> This function has an internal limit of 5 seconds per ping request.

| Retorna | Descripción |
| --- | --- |
| Integer | The ping value to the current game world. |

> **Ejemplo**
> ```lua
> local ping = World.GetPing()
> -- Do something with the value
> ```

### GetRebootTimer

```lua
function World.GetRebootTimer() -> Integer
```

Returns the number of logic ticks (50 per second) until the currently connected server reboots.

> **Información**
> This will return `0` if the world is unavailable or no reboot is currently scheduled.

| Retorna | Descripción |
| --- | --- |
| Integer | The number of logic ticks until a server reboot. |

> **Ejemplo**
> ```lua
> local rebootTicksRemaining = World.GetRebootTimer()
> if rebootTicksRemaining > 0 then
>     -- Do something with the value
> end
> ```

### IsRegion

```lua
function World.IsRegion() -> Boolean
```

Returns whether the current game world is a region or not.

> **Información**
> A region is a duplicated area outside of the main game world, typically to allow players to experience content alone or within a group.
> A `Region` is often known in game-terms as an `Instance`.
The term `region` is used to clearly differentiate this concept from other uses of `instance` in the API.

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the current game world is a region. |

> **Ejemplo**
> ```lua
> if World.IsRegion() then
>     -- Do something
> end
> ```

### GetRegionSourceForCoordGrid

```lua
function World.GetRegionSourceForCoordGrid(coord : CoordGrid) -> CoordGrid?
```

Returns the source coordinate for a given region [CoordGrid](coordgrid.md).

> **Información**
> Regions are constructed by referencing data from other parts of the game world.
> Referenced zones (8x8 tiles) and map squares (64x64 tiles) are copied into the target region to populate it.
> The input [CoordGrid](coordgrid.md) is used to find the source data which that coordinate was populated from.
> Once the source data is found, this method returns its bottom-left [CoordGrid](coordgrid.md).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| coord | [CoordGrid](coordgrid.md) | The input coordinate. |

| Retorna | Descripción |
| --- | --- |
| [CoordGrid](coordgrid.md)? | The bottom-left [CoordGrid](coordgrid.md) for the input coordinate's source data.Returns `nil` if the Player Character is not currently in a region, or the input coordinate was outside of the region bounds. |

> **Ejemplo**
> ```lua
> if World.IsRegion() then
>     local sourceCoord = World.GetRegionSourceForCoordGrid(Player.GetEntity().coordGrid)
> end
> ```

### GetMapSquareBounds

```lua
function World.GetMapSquareBounds() -> Rect?
```

Returns the map square bounds for the currently loaded game world.

> **Información**
> Values are in numbers of map squares. For example, when in a Dungeoneering region/instance this function returns:
> ```lua
> log(tostring(World.GetMapSquareBounds()))
> -- { x = 107, y = 1, w = 2, h = 2 }
> ```

| Retorna | Descripción |
| --- | --- |
| Rect? | The rectangle encompassing the current World's map square bounds. |

> **Ejemplo**
> ```lua
> -- Get the bounds of the game world
> local bounds = World.GetMapSquareBounds()
> if bounds ~= nil then
>     -- Use the config
> end
> ...
> ```

### GetGroundHeight

```lua
function World.GetGroundHeight(level : Integer, x : Integer, z : Integer, heightOffsetType? : HeightOffsetType) -> Integer,Boolean
```

Returns the height for the given level and position values, along with whether the height was available for that position.

All positional values are in fine units, where a tile dimension is `512` fine units.

> **Información**
> Valid height values are always positive.
A value of `-1` will be returned if the height could not be accessed.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| level | Integer | The coordinate level of height map data to read.The value of `level` must be between `0` and `3`. |
| x | Integer | The world-space X position, in fine units, to access the height value for. |
| z | Integer | The world-space Z position, in fine units, to access the height value for. |
| heightOffsetType? | [HeightOffsetType](#heightoffsettype) | An optional parameter, indicating what kind of height offset should be applied to the base ground height at the sampled position. |

| Retorna | Descripción |
| --- | --- |
| Integer,Boolean | The height and success pair for the input position values.Returns a height of `-1` on failure. |

> **Ejemplo**
> ```lua
> local coord = CoordGrid._0_50_50_32_32
> local coordPos = coord:ToFine(true).position
> -- Store both the height and whether it was successfully accessed
> local height,success = World.GetGroundHeight(coord.level, coordPos.x, coordPos.z)
> if success then
>     -- Do something with the valid height
> end
> ```

## RemoveRoof

### Descripción General

The Remove Roof system allows the client to hide upper levels of the game world in order to provide a clearer view to players.
Portions of the game world, such as the upper floors of a building, are grouped together and hidden as a whole when the system is told to 'reveal' a coordinate on a level underneath the group.

Some coordinates are marked in this way by default, such as:

* The Player Character's current coordinate, and
* All coordinates between the camera position and its focal target position.

The functions below allow plugins to add individual coordinates, and coordinate ranges, to further extend which parts of the game world should be hidden by this system.

> **Advertencia**
> These functions will only impact the Remove Roof system if the `Graphics` setting for `Remove Roofs` is set to `Selectively`.

> **Important**
> * A Remove Roof coordinate, or coordinate range, belongs to the plugin which registered it.
> * Different plugins may share the same registered name without clashing.
> * The coordinate, or coordinate range, will be removed when the plugin unloads.

### Funciones

#### Add(name, coord)

```lua
function World.RemoveRoof.Add(name : String, coord : CoordGrid)
```

Adds the given coordinate to the Remove Roof system, registering it by the given name.

If the name has already been registered then the existing coordinate, or coordinate range, is updated with the new coordinate.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | The name to register the coordinate with. |
| coord | [CoordGrid](coordgrid.md) | The coordinate to add to the Remove Roof system. |

> **Ejemplo**
> ```lua
> -- Add the mouse coord, and clear it if we couldn't get a mouse coord
> local coordGrid = ScreenConvert.ScreenToCoordGrid(Mouse.GetPosition())
> if coordGrid ~= nil then
>     World.RemoveRoof.Add("cursorTile", coordGrid)
> else
>     World.RemoveRoof.Remove("cursorTile")
> end
> ```

#### Add(name, coordRangeMin, coordRangeMax)

```lua
function World.RemoveRoof.Add(name : String, coordRangeMin : CoordGrid, coordRangeMax : CoordGrid)
```

Adds the given coordinate range to the Remove Roof system, registering it by the given name.

If the name has already been registered then the existing coordinate, or coordinate range, is updated with the new coordinate range.

> **Información**
> The coordinate range is applied as shown in this pseudocode example:
> ```text
> for (level = coordRangeMin.level; level <= coordRangeMax.level; level++)
>     for (x = coordRangeMin.x; x <= coordRangeMax.x; x++)
>         for (z = coordRangeMin.z; z <= coordRangeMax.z; z++)
>             ApplyCoordinate(level, x, z)
> ```

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | The name to register the coordinate with. |
| coordRangeMin | [CoordGrid](coordgrid.md) | The minimum coordinate of the range to add to the Remove Roof system. |
| coordRangeMax | [CoordGrid](coordgrid.md) | The maximum coordinate of the range to add to the Remove Roof system. |

> **Ejemplo**
> ```lua
> -- Add the mouse coord, with a 1-tile buffer around it
> local coordGrid = ScreenConvert.ScreenToCoordGrid(Mouse.GetPosition())
> if coordGrid ~= nil then
>     local coordGridMin = CoordGrid.new(coordGrid)
>     local coordGridMax = CoordGrid.new(coordGrid)
> 
>     coordGridMin.x = coordGridMin.x - 1
>     coordGridMin.z = coordGridMin.z - 1
> 
>     coordGridMax.x = coordGridMax.x + 1
>     coordGridMax.z = coordGridMax.z + 1
> 
>     World.RemoveRoof.Add("cursorTile", coordGridMin, coordGridMax)
> end
> ```

#### Remove

Removes the coordinate, or coordinate range, registered by the given name from the Remove Roof system.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | The registered name to remove. |

> **Ejemplo**
> ```lua
> -- Add the mouse coord, and clear it if we couldn't get a mouse coord
> local coordGrid = ScreenConvert.ScreenToCoordGrid(Mouse.GetPosition())
> if coordGrid ~= nil then
>     World.RemoveRoof.Add("cursorTile", coordGrid)
> else
>     World.RemoveRoof.Remove("cursorTile")
> end
> ```

#### Clear

Removes all Remove Roof coordinates registered by the current plugin.

> **Ejemplo**
> ```lua
> -- Clean up registered Remove Roof coordinates not holding shift
> if Keyboard.IsShiftDown() then
>     -- Do various Remove Roof things
> else
>     World.RemoveRoof.Clear()
> end
> ```