# ShapeList

## Descripción General

This page provides information on the available methods and properties for drawing 3D shapes in the game world.

For a general introduction, see the [Shapes](../shapes.md) page.

## Enumeraciones

### ShapeEntityAlignType

Used by the [ShapeEntity](#properties_2) property `alignType`.

| Name | Valor | Descripción |
| --- | --- | --- |
| NONE | 0 | No rotational alignment. |
| OBJECT | 1 | The shape rotates to align with the average slope of the ground. |
| MODEL | 2 | Each separate position in the shape is translated vertically to align with the ground, for a closer fit. |

## ShapeData

The `ShapeData` table provides a way to store data like positions, colours and triangle and line indices in one object.

It also allows those objects to be registered by name and re-used across a variety of drawing operations by object or name.

### Constructors

```lua
function ShapeData.new() -> ShapeData
```

Creates and returns an empty `ShapeData` object.

| Retorna | Descripción |
| --- | --- |
| [ShapeData](#shapedata) | The newly created data object. |

### Funciones

#### GetAllRegistered

```lua
function ShapeData.GetAllRegistered() -> [ String ]
```

Returns the names of all registered [ShapeData](#shapedata) that are available to the current plugin.

| Retorna | Descripción |
| --- | --- |
| [ String ] | An array of registered [ShapeData](#shapedata) names. |

> **Ejemplo**
> ```lua
> log("ShapeData names available:")
> for _,name in ipairs(ShapeData.GetAllRegistered()) do
>     log("    " .. name)
> end
> ```

#### IsRegistered

```lua
function ShapeData.IsRegistered(name : String) -> Boolean
```

Returns whether a [ShapeData](#shapedata) is registered with the given name.

> **Información**
> String matches are case-sensitive.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | The string to match against each registered [ShapeData](#shapedata) name. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the name has been registered. |

> **Ejemplo**
> ```lua
> -- Check if the shape exists already
> if not ShapeData.IsRegistered("myExampleShape") then
>     -- It doesn't, so create and register it
>     local shape = ShapeData.new()
>     shape.positions = { ... }
>     shape.lines = { ... }
>     local success = ShapeData.Register("myExampleShape", shape)
> end
> ```

#### Register

```lua
function ShapeData.Register(name : String, shapeData : ShapeData) -> Boolean
```

Registers [ShapeData](#shapedata) with the given name, and returning whether the registration was successful.

> **Información**
> [ShapeData](#shapedata) objects are copied when registered.
This means that changes made to the object after registration do not affect the newly registered object data.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | The string to register as the [ShapeData](#shapedata) name. |
| shapeData | [ShapeData](#shapedata) | The data to register. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the [ShapeData](#shapedata) was successfully registered. |

> **Ejemplo**
> ```lua
> -- Create the shape data first
> local shape = ShapeData.new()
> shape.positions = { ... }
> shape.rgba = { ... }
> shape.lines = { ... }
> 
> -- Then register it with the desired name
> local success = ShapeData.Register("myExampleShape", shape
> ```

#### Unregister

```lua
function ShapeData.Unregister(name : String) -> Boolean
```

Attempts to unregister a [ShapeData](#shapedata) which is registered with the given name.

> **Información**
> String matches are case-sensitive.

> **Advertencia**
> When a `ShapeData` is unregistered, any [ShapeInstance](#shapeinstance) or [ShapeEntity](#shapeentity) which uses that data **will be automatically destroyed**.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | The string to match against each registered [ShapeData](#shapedata) name. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the [ShapeData](#shapedata) was successfully unregistered. |

> **Ejemplo**
> ```lua
> local success = ShapeData.Unregister("myExampleShape")
> 
> -- Alternatively
> if ShapeData.IsRegistered("myExampleShape") then
> 
>     -- Do some clean-up work
>     ...
> 
>     -- Then finally unregister
>     ShapeData.Unregister("myExampleShape")
> end
> ```

### Propiedades

Also see [Shapes](../shapes.md#shapes) for addition information on this data.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| positions | [ [Vector3](../../math/vector.md#vector3) ] | A list of 3D positions. |
| rgba | [ Integer ] | A list of 32-bit colours. The number of colours in this array must match the number of positions, or be empty.If empty, the default colour value is `0xFFFFFFFF`. |
| tris | [ Integer ] | A list of position index triplets which represent a single triangle.**Indices are 0-indexed.** |
| lines | [ Integer ] | A list of position index pairs which represent a single line.**Indices are 0-indexed.** |

## ShapeList

The `ShapeList` table allows plugins to draw shape data arrays and [ShapeData](#shapedata) objects in the game world.

It also manages the creation and destruction of [ShapeInstances](#shapeinstance) and [ShapeEntities](#shapeentity), which in turn draw themselves to the game world.

### Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

### Funciones

#### Draw

```lua
function ShapeList.Draw(settings : Table)
```

Draws a shape in the game world using the provided `settings` table of values.

Supported values for the `settings` table are:

| Key | Type | Default Value | Description |
| --- | --- | --- | --- |
| shapeDataName | String | - | The name of a registered [ShapeData](#shapedata) to draw. |
| shapeData | [ShapeData](#shapedata) | - | The [ShapeData](#shapedata) to draw directly. |
| shapePositions | [ [Vector3](../../math/vector.md#vector3) ] | - | The raw shape data positions to draw. |
| shapeRGBA | [ Integer ] | - | The raw shape data colours to draw. |
| shapeTris | [ Integer ] | - | The raw shape data triangle indices to draw. |
| shapeLines | [ Integer ] | - | The raw shape data line indices to draw. |
| translation | [Vector3](../../math/vector.md#vector3) | `0,0,0` | A positional offset transform applied to the shape when it is drawn.Allows shape data constructed in local-space to be drawn in world-space. |
| rotation | [Vector3](../../math/vector.md#vector3) | `0,0,0` | A rotational transform applied to the shape when it is drawn.`X = Yaw, Y = Pitch, Z = Roll` |
| scale | [Vector3](../../math/vector.md#vector3) | `1,1,1` | A scaling transform applied to the shape when it is drawn. |
| ignoreDepth | Boolean | `false` | Controls how the shape handles depth testing when drawing:`true` - Always draws on top of world geometry`false` - Draws behind occluding world geometry. |
| colour | Integer | `0xFFFFFFFF` | A 32-bit colour which is multiplied against the RGBA data of the shape being drawn. |
| lineWidth | Float | `2.0` | The drawn thickness of any lines defined by the shape data.Maximum value is `10.0`. |
| asBillboard | Boolean | `false` | Whether the shape should always rotate to face the camera.This rotation is applied around the centre of final AABB of the drawn shape. |

Shape data can be provided via settings in the following priority order:

* `shapeDataName`
* `shapeData`
* Raw data buffers `shapePositions`, `shapeRGBA`, `shapeTris` and `shapeLines`

Only the highest priority setting with valid data is drawn; any lower priority settings with data are ignored.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| settings | Table | A table of key-value pairs which describe the settings for the draw operation. |

> **Ejemplo**
> ```lua
> -- Draw a rotating tile shape on the tile the mouse cursor is pointing at
> 
> -- A basic tile shape
> local tileShape = ShapeData.new()
> tileShape.positions = {
>     Vector3.new(-250, 0, -250),
>     Vector3.new(250, 0, -250),
>     Vector3.new(250, 0, 250),
>     Vector3.new(-250, 0, 250)
> }
> tileShape.lines = { 0, 1, 1, 2, 2, 3, 3, 0 }
> 
> -- Track the time elapsed
> elapsedTime = 0.0
> 
> -- ShapeList.Draw() only works within draw events
> Event.Draw.Subscribe("myEvent", function (drawEvent)
> 
>     -- Update the time
>     elapsedTime = elapsedTime + drawEvent.timeDeltaSecs
> 
>     -- Get the coordinate under the mouse cursor
>     local coordGrid = ScreenConvert.ScreenToCoordGrid(Mouse.GetPosition())
>     if coordGrid ~= nil then
> 
>         -- Rotate once every 4 seconds
>         local interval = 4.0
>         local yaw = 360 * (math.fmod(elapsedTime, interval) / interval)
> 
>         -- Get the tile centre
>         local tilePos = coordGrid:ToCoordFine(true).position
>         -- Find the ground height
>         tilePos.y = World.GetGroundHeight(coordGrid.level, tilePos.x, tilePos.z)
>         -- Move vertically up to reduce clipping
>         tilePos.y = tilePos.y + 100.0
> 
>         -- Draw the shape
>         ShapeList.Draw( {
>             shapeData = tileShape,
>             translation = tilePos,
>             rotation = Vector3.new(yaw, 0, 0),
>             colour = 0xFF8800FF
>         } )
> 
>     end
> end)
> ```

#### DrawLine

```lua
function ShapeList.DrawLine(settings : Table)
```

Draws a segmented line in the game world using the provided `settings` table of values.

This method does not require line indices, like those found in a [ShapeData](#shapedata).
Instead, it draws a line from each provided position to the next.

Supported values for the `settings` table are:

| Key | Type | Default Value | Description |
| --- | --- | --- | --- |
| positions | [ [Vector3](../../math/vector.md#vector3) ] | - | The list of positions to draw lines between. |
| translation | [Vector3](../../math/vector.md#vector3) | `0,0,0` | A positional offset transform applied to the lines when they are drawn.Allows positions constructed in local-space to be drawn in world-space. |
| rotation | [Vector3](../../math/vector.md#vector3) | `0,0,0` | A rotational transform applied to the lines when they are drawn.`X = Yaw, Y = Pitch, Z = Roll` |
| scale | [Vector3](../../math/vector.md#vector3) | `1,1,1` | A scaling transform applied to the lines when they are drawn. |
| ignoreDepth | Boolean | `false` | Controls how the lines handle depth testing when drawing:`true` - Always draws on top of world geometry`false` - Draws behind occluding world geometry. |
| colour | Integer | `0xFFFFFFFF` | The 32-bit colour to use as the line colour. |
| lineWidth | Float | `2.0` | The drawn thickness of the lines.Maximum value is `10.0`. |

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| settings | Table | A table of key-value pairs which describe the settings for the draw operation. |

> **Ejemplo**
> ```lua
> -- Draw an orange line showing the player's movement history
> 
> -- Small wrapping buffer to hold player coordinates
> playerHistoryCoords = {}
> playerHistoryMax = 10
> function addPlayerCoord(coord)
>     if lastCoord == nil or lastCoord ~= coord then
>         lastCoord = coord
>         local count = #(playerHistoryCoords)
>         if count < playerHistoryMax then
>             playerHistoryCoords[count + 1] = coord
>         else
>             for i=1,(playerHistoryMax-1) do
>                 playerHistoryCoords[i] = playerHistoryCoords[i + 1]
>             end
>             playerHistoryCoords[playerHistoryMax] = coord
>         end
>     end
> end
> 
> -- ShapeList.DrawLine() only works within draw events
> Event.Draw.Subscribe("myEvent", function (drawEvent)
> 
>     -- Add the current player coordinate to the list
>     local playerEntity = Player.GetEntity()
>     if playerEntity ~= nil then
>         addPlayerCoord(playerEntity.coordGrid)
>     end
> 
>     -- ShapeList.DrawLine{} requires at least two positions
>     if #(playerHistoryCoords) >= 2 then
> 
>         -- Build a line of positions from the coords
>         local linePositions = {}
>         for i,coord in ipairs(playerHistoryCoords) do
>             local pos = coord:ToCoordFine(true).position
>             pos.y = World.GetGroundHeight(coord.level, pos.x, pos.z) + 50.0
>             linePositions[i] = pos
>         end
> 
>         -- Draw the line of positions
>         -- Positions are already in world-space so no need to use the translation setting
>         ShapeList.DrawLine( {
>             positions = linePositions,
>             colour = 0xFF8800FF,
>             lineWidth = 6.0
>         } )
> 
>     end
> end)
> ```

#### CreateInstance

```lua
function ShapeList.CreateInstance(name : String) -> ShapeInstance?
```

Creates a new [ShapeInstance](#shapeinstance) with the given name.
Returns `nil` if an instance already exists with that name.

> **Información**
> Only one instance can exist with the same name in each plugin.
However, separate plugins can have an instance with the same name, as shown below:
> ```lua
> -- Plugin A
> local pluginA_Instance1 = ShapeList.CreateInstance("myInstance") -- success
> local pluginA_Instance2 = ShapeList.CreateInstance("myInstance") -- fail
> 
> -- Plugin B
> local pluginB_Instance = ShapeList.CreateInstance("myInstance") -- success
> ```

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | El nombre de instance. |

| Retorna | Descripción |
| --- | --- |
| [ShapeInstance](#shapeinstance)? | The created [ShapeInstance](#shapeinstance).Returns `nil` if the instance could not be created. |

> **Ejemplo**
> ```lua
> -- Create an empty instance
> local instance = ShapeList.CreateInstance("myInstance");
> if instance ~= nil then
>     -- Populate with shape data
>     instance:SetShapeDataName("myShape")
>     -- Move into position, 100 fine units above the ground
>     instance.translation = CoordGrid._0_50_50_32_32:ToFine(true).position  + Vector3.new(0, 100, 0)
> end
> ```

#### GetInstance

```lua
function ShapeList.GetInstance(name : String) -> ShapeInstance?
```

Returns an existing [ShapeInstance](#shapeinstance) with the given name.
Returns `nil` if no instance exists with that name.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | El nombre de instance. |

| Retorna | Descripción |
| --- | --- |
| [ShapeInstance](#shapeinstance)? | The [ShapeInstance](#shapeinstance) which was found.Returns `nil` if no instance was found. |

> **Ejemplo**
> ```lua
> -- Create an instance and set it up
> local tmpInstance = ShapeList.CreateInstance("myInstance");
> ...
> 
> -- Get the instance inside the logic event
> Event.Logic.Subscribe("myEvent", function (logicEvent)
>     local logicInstance = ShapeList.GetInstance("myInstance");
>     if logicInstance ~= nil then
>         -- Make changes
>     end
> end)
> ```

#### GetAllInstances

```lua
function ShapeList.GetAllInstances() -> [ ShapeInstance ]
```

Returns a list of all existing [ShapeInstances](#shapeinstance) created by the plugin.

| Retorna | Descripción |
| --- | --- |
| [ [ShapeInstance](#shapeinstance) ] | All existing [ShapeInstances](#shapeinstance). |

> **Ejemplo**
> ```lua
> -- Print every instance name
> local allInstances = ShapeList.GetAllInstances()
> log("There are " .. #(allInstances) .. " ShapeInstances")
> for _,instance in ipair(allInstances) do
>     log(instance.name)
> end
> ```

#### DestroyInstance(instance)

```lua
function ShapeList.DestroyInstance(instance : ShapeInstance) -> Boolean
```

Attempts to destroy the given [ShapeInstance](#shapeinstance) and returns whether it was successful.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| instance | [ShapeInstance](#shapeinstance) | The [ShapeInstance](#shapeinstance) object. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the [ShapeInstance](#shapeinstance) was successfully destroyed. |

> **Ejemplo**
> ```lua
> -- Destroy every instance (by object)
> local allInstances = ShapeList.GetAllInstances()
> log("Destroying " .. #(allInstances) .. " ShapeInstances")
> for _,instance in ipair(allInstances) do
>     ShapeList.DestroyInstance(instance)
> end
> ```

#### DestroyInstance(name)

```lua
function ShapeList.DestroyInstance(name : String) -> Boolean
```

Attempts to destroy the [ShapeInstance](#shapeinstance) with the given name and returns whether it was successful.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | El nombre de [ShapeInstance](#shapeinstance) object. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the [ShapeInstance](#shapeinstance) was successfully destroyed. |

> **Ejemplo**
> ```lua
> -- Destroy every instance (by name)
> local allInstances = ShapeList.GetAllInstances()
> log("Destroying " .. #(allInstances) .. " ShapeInstances")
> for _,instance in ipair(allInstances) do
>     ShapeList.DestroyInstance(instance.name)
> end
> ```

#### CreateEntity

```lua
function ShapeList.CreateEntity(name : String) -> ShapeEntity?
```

Creates a new [ShapeEntity](#shapeentity) with the given name.
Returns `nil` if an entity already exists with that name.

> **Información**
> Only one entity can exist with the same name in each plugin.
However, separate plugins can have an entity with the same name, as shown below:
> ```lua
> -- Plugin A
> local pluginA_Entity1 = ShapeList.CreateEntity("myEntity") -- success
> local pluginA_Entity2 = ShapeList.CreateEntity("myEntity") -- fail
> 
> -- Plugin B
> local pluginB_Entity = ShapeList.CreateEntity("myEntity") -- success
> ```

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | El nombre de entity. |

| Retorna | Descripción |
| --- | --- |
| [ShapeEntity](#shapeentity)? | The created [ShapeEntity](#shapeentity).Returns `nil` if the entity could not be created. |

> **Ejemplo**
> ```lua
> -- Create an empty entity
> local entity = ShapeList.CreateEntity("myEntity");
> if entity ~= nil then
>     -- Populate with shape data
>     entity:SetShapeDataName("myShape")
>     -- Move into position, 100 fine units above the ground
>     entity.coordGrid = CoordGrid._0_50_50_32_32
>     entity.heightOffset = 100
> end
> ```

#### GetEntity

```lua
function ShapeList.GetEntity(name : String) -> ShapeInstance?
```

Returns an existing [ShapeEntity](#shapeentity) with the given name.
Returns `nil` if no entity exists with that name.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | El nombre de entity. |

| Retorna | Descripción |
| --- | --- |
| [ShapeEntity](#shapeentity)? | The [ShapeEntity](#shapeentity) which was found.Returns `nil` if no entity was found. |

> **Ejemplo**
> ```lua
> -- Create an entity and set it up
> local tmpEntity = ShapeList.CreateEntity("myEntity");
> ...
> 
> -- Get the entity inside the logic event
> Event.Logic.Subscribe("myEvent", function (logicEvent)
>     local logicEntity = ShapeList.GetEntity("myEntity");
>     if logicEntity ~= nil then
>         -- Make changes
>     end
> end)
> ```

#### GetAllEntities

```lua
function ShapeList.GetAllEntities() -> [ ShapeEntity ]
```

Returns a list of all existing [ShapeEntities](#shapeentity) created by the plugin.

| Retorna | Descripción |
| --- | --- |
| [ [ShapeEntity](#shapeentity) ] | All existing [ShapeEntities](#shapeentity). |

> **Ejemplo**
> ```lua
> -- Print every entity name
> local allEntities = ShapeList.GetAllEntities()
> log("There are " .. #(allEntities) .. " ShapeEntities")
> for _,entity in ipair(allEntities) do
>     log(entity.name)
> end
> ```

#### DestroyEntity(entity)

```lua
function ShapeList.DestroyEntity(entity : ShapeEntity) -> Boolean
```

Attempts to destroy the given [ShapeEntity](#shapeentity) and returns whether it was successful.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| entity | [ShapeEntity](#shapeentity) | The [ShapeEntity](#shapeentity) object. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the [ShapeEntity](#shapeentity) was successfully destroyed. |

> **Ejemplo**
> ```lua
> -- Destroy every entity (by object)
> local allEntities = ShapeList.GetAllEntities()
> log("Destroying " .. #(allEntities) .. " ShapeEntities")
> for _,entity in ipair(allEntities) do
>     ShapeList.DestroyEntity(entity)
> end
> ```

#### DestroyEntity(name)

```lua
function ShapeList.DestroyEntity(name : String) -> Boolean
```

Attempts to destroy the [ShapeEntity](#shapeentity) with the given name and returns whether it was successful.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| name | String | El nombre de [ShapeEntity](#shapeentity) object. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the [ShapeEntity](#shapeentity) was successfully destroyed. |

> **Ejemplo**
> ```lua
> -- Destroy every entity (by name)
> local allEntities = ShapeList.GetAllEntities()
> log("Destroying " .. #(allEntities) .. " ShapeEntities")
> for _,entity in ipair(allEntities) do
>     ShapeList.DestroyEntity(entity.name)
> end
> ```

## ShapeInstance

A `ShapeInstance` is a dynamic object which contains some [ShapeData](#shapedata) and automatically handles drawing itself in the game world.

See [Shape Instance](../shapes.md#shape-instance) for additional information on this object.

### Constructors

> **Información**
> This usertype has no constructor, use [ShapeList.CreateInstance()](#createinstance) to create one.

### Métodos

#### SetShapeData

```lua
function ShapeInstance:SetShapeData(shapeData : ShapeData) -> Boolean
```

Assigns a copy of the given shape data to the instance and returns whether the data was valid and successfully set.

This method also clears any value set by [SetShapeDataName](#setshapedataname).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| shapeData | [ShapeData](#shapedata) | The shape data to copy to the instance. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the shape data was successfully set on the instance. |

> **Ejemplo**
> ```lua
> -- Create some data
> local data = ShapeData.new()
> data.positions = { ... }
> data.lines = { ... }
> 
> -- Create an instance
> local instance = ShapeList.CreateInstance("myInstance")
> if instance ~= nil then
>     -- Assign the data, and log if there was a problem
>     if not instance:SetShapeData(data) then
>         log("Failed to set instance shape data")
>         instance:Destroy()
>     else
>         -- Set up the rest of the instance
>         instance.translation = ...
>     end
> end
> ```

#### SetShapeDataName

```lua
function ShapeInstance:SetShapeDataName(shapeName : String) -> Boolean
```

Assigns the name of a registered [ShapeData](#shapedata) to the instance and returns whether the registered name exists and was successfully set.

This method also clears any value set by [SetShapeData](#setshapedata).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| shapeName | String | The name of a registered shape data [ShapeData](#shapedata). |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the shape name was successfully set on the instance. |

> **Ejemplo**
> ```lua
> -- Create some data
> local data = ShapeData.new()
> data.positions = { ... }
> data.lines = { ... }
> 
> -- Register the shape
> local success = ShapeData.Register("myShape", data)
> 
> if success then
>     -- Create an instance
>     local instance = ShapeList.CreateInstance("myInstance")
>     if instance ~= nil then
>         -- Assign the shape name
>         if not instance:SetShapeDataName("myShape") then
>             log("Failed to set instance shape name")
>             instance:Destroy()
>         else
>             -- Set up the rest of the instance
>             instance.translation = ...
>         end
>     end
> end
> ```

#### Destroy

```lua
function ShapeInstance:Destroy() -> Boolean
```

Attempts to destroy the instance. Returns `false` if the entity does not exist, otherwise `true`.

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the instance was successfully destroyed. |

> **Ejemplo**
> ```lua
> -- Create an instance and set it up
> local tmpInstance = ShapeList.CreateInstance("myInstance")
> ...
> 
> -- Set a lifetime for the instance
> tickLifetime = 100
> 
> Event.Logic.Subscribe("myEvent", function(logicEvent)
> 
>     -- Decrease the lifetime
>     tickLifetime = tickLifetime - 1
> 
>     -- Destroy the instance when the lifetime reaches 0
>     if tickLifetime == 0 then
>         local instance = ShapeList.GetInstance("myInstance")
>         if instance ~= nil then
>             instance:Destroy()
>         end
>     end
> end)
> ```

### Propiedades

| Name | Type | Default Value | Writeable | Description |
| --- | --- | --- | --- | --- |
| isValid | Boolean | `-` |  | Whether this instance still exists. Dispose of this usertype object when invalid. |
| name | String | `-` |  | The name the instance was created with. |
| hasData | Boolean | `-` |  | Whether this instance has valid [ShapeData](#shapedata) or a registered shape name assigned to it. |
| translation | [Vector3](../../math/vector.md#vector3) | `0,0,0` |  | A positional offset transform applied to the shape when it is drawn.Allows shape data constructed in local-space to be drawn in world-space. |
| rotation | [Vector3](../../math/vector.md#vector3) | `0,0,0` |  | A rotational transform applied to the shape when it is drawn.`X = Yaw, Y = Pitch, Z = Roll` |
| scale | [Vector3](../../math/vector.md#vector3) | `1,1,1` |  | A scaling transform applied to the shape when it is drawn. |
| visible | Boolean | `true` |  | Whether the instance should be drawn. |
| ignoreDepth | Boolean | `false` |  | Controls how the instance handles depth testing when drawing:`true` - Always draws on top of world geometry`false` - Draws behind occluding world geometry. |
| colour | Integer | `0xFFFFFFFF` |  | A 32-bit colour which is multiplied against the RGBA data of the ShapeData being drawn. |
| lineWidth | Float | `2.0` |  | The drawn thickness of any lines defined by the instance's [ShapeData](#shapedata).Maximum value is `10.0`. |
| asBillboard | Boolean | `false` |  | Whether the shape should always rotate to face the camera.This rotation is applied around the centre of final AABB of the drawn shape. |

## ShapeEntity

A `ShapeEntity` is an object which contains some [ShapeData](#shapedata), is often placed at a fixed coordinate, and automatically handles drawing itself in the game world.

See [Shape Entity](../shapes.md#shape-entity) for additional information on this object.

### Constructors

> **Información**
> This usertype has no constructor, use [ShapeList.CreateEntity()](#createentity) to create one.

### Métodos

#### SetShapeData

```lua
function ShapeEntity:SetShapeData(shapeData : ShapeData) -> Boolean
```

Assigns a copy of the given shape data to the entity and returns whether the data was valid and successfully set.

This method also clears any value set by [SetShapeDataName](#setshapedataname_1).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| shapeData | [ShapeData](#shapedata) | The shape data to copy to the entity. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the shape data was successfully set on the entity. |

> **Ejemplo**
> ```lua
> -- Create some data
> local data = ShapeData.new()
> data.positions = { ... }
> data.lines = { ... }
> 
> -- Create an entity
> local entity = ShapeList.CreateEntity("myEntity")
> if entity ~= nil then
>     -- Assign the data, and log if there was a problem
>     if not entity:SetShapeData(data) then
>         log("Failed to set entity shape data")
>         entity:Destroy()
>     else
>         -- Set up the rest of the entity
>         entity.coordGrid = ...
>     end
> end
> ```

#### SetShapeDataName

```lua
function ShapeEntity:SetShapeDataName(shapeName : String) -> Boolean
```

Assigns the name of a registered [ShapeData](#shapedata) to the entity and returns whether the registered name exists and was successfully set.

This method also clears any value set by [SetShapeData](#setshapedata_1).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| shapeName | String | The name of a registered shape data [ShapeData](#shapedata). |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the shape name was successfully set on the entity. |

> **Ejemplo**
> ```lua
> -- Create some data
> local data = ShapeData.new()
> data.positions = { ... }
> data.lines = { ... }
> 
> -- Register the shape
> local success = ShapeData.Register("myShape", data)
> 
> if success then
>     -- Create an entity
>     local entity = ShapeList.CreateEntity("myEntity")
>     if entity ~= nil then
>         -- Assign the shape name
>         if not entity:SetShapeDataName("myShape") then
>             log("Failed to set entity shape name")
>             entity:Destroy()
>         else
>             -- Set up the rest of the entity
>             entity.coordGrid = ...
>         end
>     end
> end
> ```

#### SetDrawDistance(distance)

```lua
function ShapeEntity:SetDrawDistance(distance : Float)
```

Sets the draw distance, in fine units, for the [ShapeEntity](#shapeentity).

If the distance between the Player Character and the [ShapeEntity](#shapeentity) is greater than `distance` then the entity will not be drawn.

The tested distance is the horizontal measurement between the Player Character's world position and the closest point on the [ShapeEntity's](#shapeentity) bounding box.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| distance | Float | The distance, in fine units, from the Player Character at which the entity will stop drawing. |

> **Ejemplo**
> ```lua
> -- Create an entity
> local entity = ShapeList.CreateEntity("myEntity")
> entity:SetShapeDataName("myShape")
> entity.coordGrid = CoordGrid._0_50_50_32_32
> 
> -- Set the entity to stop drawing when more than 20 tiles from the player
> entity:SetDrawDistance(20 * 512) -- 20 tiles, each at 512 fine units
> ```

#### SetDrawDistance(nearDistance, farDistance)

```lua
function ShapeEntity:SetDrawDistance(nearDistance : Float, farDistance : Float)
```

Sets the draw distance range, in fine units, for the [ShapeEntity](#shapeentity), allowing the entity to fade out gradually over distance.

If the distance between the Player Character and the [ShapeEntity](#shapeentity) is greater than `farDistance` then the entity will not be drawn.

If the distance is between `nearDistance` and `farDistance` then the transparency of the entity is scaled from `x1.0` at `nearDistance` to `x0.0` at `farDistance`, and linearly interpolating between those two scaling values.
For example, if the distance is halfway between `nearDistance` and `farDistance` then the transparency is scaled by `x0.5`.

The tested distance is the horizontal measurement between the Player Character's world position and the closest point on the [ShapeEntity's](#shapeentity) bounding box.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| nearDistance | Float | The near draw distance, in fine units. |
| farDistance | Float | The far draw distance, in fine units. |

> **Ejemplo**
> ```lua
> -- Create an entity
> local entity = ShapeList.CreateEntity("myEntity")
> entity:SetShapeDataName("myShape")
> entity.coordGrid = CoordGrid._0_50_50_32_32
> 
> -- Set the entity to start fading out at 16 tiles from the player, and
> -- have faded out completely at 20 tiles from the player
> entity:SetDrawDistance(16 * 512, 20 * 512)
> ```

#### Destroy

```lua
function ShapeEntity:Destroy() -> Boolean
```

Attempts to destroy the entity. Returns `false` if the entity does not exist, otherwise `true`.

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the entity was successfully destroyed. |

> **Ejemplo**
> ```lua
> -- Create an entity and set it up
> local tmpEntity = ShapeList.CreateEntity("myEntity")
> ...
> 
> -- Set a lifetime for the entity
> tickLifetime = 100
> 
> Event.Logic.Subscribe("myEvent", function(logicEvent)
> 
>     -- Decrease the lifetime
>     tickLifetime = tickLifetime - 1
> 
>     -- Destroy the entity when the lifetime reaches 0
>     if tickLifetime == 0 then
>         local entity = ShapeList.GetEntity("myEntity")
>         if entity ~= nil then
>             entity:Destroy()
>         end
>     end
> end)
> ```

### Propiedades

| Name | Type | Default Value | Writeable | Description |
| --- | --- | --- | --- | --- |
| isValid | Boolean | `-` |  | Whether this entity still exists. Dispose of this usertype object when invalid. |
| name | String | `-` |  | The name the entity was created with. |
| hasData | Boolean | `-` |  | Whether this entity has valid [ShapeData](#shapedata) or a registered shape name assigned to it. |
| drawDistances | Integer,Integer | `10240`,`12288` |  | Returns the near and far draw distances for the entity as a value pair.Use [SetDrawDistance()](#setdrawdistancedistance) to set these value(s). |
| coordGrid | [CoordGrid](../coordgrid.md) | `-` |  | The coordinate at which the entity is placed.The entity will be placed at the centre of the coordinate, and automatically sets its height to align with the ground.Replaces any value set for `coordFine`. |
| coordFine | [CoordFine](../coordfine.md) | `-` |  | The coordinate at which the entity is placed.Automatically sets its height to align with the ground.Replaces any value set for `coordGrid`. |
| visible | Boolean | `true` |  | Whether the entity should be drawn. |
| ignoreDepth | Boolean | `false` |  | Controls how the entity handles depth testing when drawing:`true` - Always draws on top of world geometry`false` - Draws behind occluding world geometry. |
| colour | Integer | `0xFFFFFFFF` |  | A 32-bit colour which is multiplied against the RGBA data of the ShapeData being drawn. |
| lineWidth | Float | `2.0` |  | The drawn thickness of any lines defined by the entity's [ShapeData](#shapedata).Maximum value is `10.0`. |
| alignType | [ShapeEntityAlignType](#shapeentityaligntype) | `NONE` |  | How the entity's shape data should align with the ground.See [ShapeEntityAlignType](#shapeentityaligntype). |
| heightOffset | Float | `0.0` |  | How high above the ground level the entity should be drawn. |
| rotation | Float | `0.0` |  | The starting rotation of the entity.Rotation occurs around the vertical Y axis.Units are in degrees. |
| rotationSpeed | Float | `0.0` |  | How far the entity rotates in a clockwise direction in one second.Rotation occurs around the vertical Y axis.Units are in degrees. |
| asBillboard | Boolean | `false` |  | Whether the shape should always rotate to face the camera.This rotation is applied around the centre of final AABB of the drawn shape.This setting often conflicts with `alignType` - it is recommended to use `ShapeEntityAlignType.NONE` when drawing a shape entity as a billboard. |