# PlayerEntity

## Descripción General

An `PlayerEntity` represents a player that is currently active in the game world.

See [PlayerList](../list/playerlist.md) for information on how to access `PlayerEntities`.

> **Información**
> A `PlayerEntity` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

> **Advertencia**
> Use `PlayerEntity.isValid` to confirm that an entity still exists before trying to access its properties.
Entities can be removed from the client by the server for various reasons, i.e. due to moving beyond the player view distance or teleporting.
When an entity is removed it will become invalid, and any copies of this usertype should be disposed of.
 If the same entity is re-added to the client by the server, such as walking back into visibility range, then a different *new* PlayerEntity will be created.

Information available within an `PlayerEntity` includes:

* UID
* World position
* Facing direction

## Ejemplos

```lua
-- Iterate all active PlayerEntities
local allPlayers = PlayerList.All()
for _,playerEntity in ipairs(allPlayers) do
    if playerEntity.coordGrid == CoordGrid._0_50_50_32_32 then
        -- Found a player at a specific coord
    end
end
```

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| isValid | Boolean | Whether this entity still exists. Dispose of this usertype object when invalid. |
| uid | Integer | The unique ID (UID) of this entity. |
| displayName | String | The display name of this entity. |
| position | Vector3 | The world position of this `PlayerEntity`. |
| coordGrid | [CoordGrid](../coordgrid.md) | Returns the [CoordGrid](../coordgrid.md) tile this `PlayerEntity` is currently on. |
| aabb | [AABB](../../math/aabb.md) | Devuelve el/la bounding box for this `PlayerEntity` actual. |
| facing | Integer | The current facing angle, in degrees, of this `PlayerEntity`. |
| facingTarget | Integer | The target facing angle, in degrees, of this `PlayerEntity`.The `PlayerEntity` will be turning towards this angle, if different from `PlayerEntity.facing`. |
| route | [ [CoordGrid](../coordgrid.md) ] | Returns a list of the current coordinates in the `PlayerEntity`'s movement route.Devuelve el/la position coordinate if the `PlayerEntity` is not moving actual. |
| routeEnd | [CoordGrid](../coordgrid.md)? | Returns the final coordinate in the `PlayerEntity`'s movement route.Devuelve el/la position coordinate if the `PlayerEntity` is not moving actual. |