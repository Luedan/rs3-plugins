# NPCEntity

## Descripción General

An `NPCEntity` represents an instance of an [NPCType](../config/npctype.md) that is currently active in the game world.

See [NPCList](../list/npclist.md) for information on how to access `NPCEntities`.

> **Información**
> An `NPCEntity` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

> **Advertencia**
> Use `NPCEntity.isValid` to confirm that an entity still exists before trying to access its properties.
Entities can be removed from the client by the server for various reasons, i.e. due to moving beyond the player view distance or death.
When an entity is removed it will become invalid, and any copies of this usertype should be disposed of.
 If the same entity is re-added to the client by the server, such as walking back into visibility range, then a different *new* NPCEntity will be created.

Information available within an `NPCEntity` includes:

* [NPCType](../config/npctype.md)
* UID
* World position
* Facing direction
* TODO

## Ejemplos

```lua
-- Iterate all active NPCEntities
local allNPCs = NPCList.All()
for _,npcEntity in ipairs(allNPCs) do
    if npcEntity.config == config.NPC.HANS and npcEntity.coordGrid == CoordGrid._0_50_50_32_32 then
        -- Found Hans at a specific coord
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
| config | [NPCType](../config/npctype.md) | The config used by this entity. |
| parentConfig | [NPCType](../config/npctype.md) | The parent config used by this entity, if it is a [MultiNPC](../config/npctype.md#multinpc). |
| configID | Integer | The ID of the config used by this entity. |
| parentConfigID | Integer | The ID of the parent config used by this entity, if it is a [MultiNPC](../config/npctype.md#multinpc). |
| isMultiNPC | Boolean | Whether this `NPCEntity` is a [MultiNPC](../config/npctype.md#multinpc). |
| position | Vector3 | The world position of this `NPCEntity`. |
| coordGrid | CoordGrid | Returns the CoordGrid tile this `NPCEntity` is currently on. |
| aabb | [AABB](../../math/aabb.md) | Devuelve el/la bounding box for this `NPCEntity` actual. |
| facing | Integer | The current facing angle, in degrees, of this `NPCEntity`. |
| facingTarget | Integer | The target facing angle, in degrees, of this `NPCEntity`.The `NPCEntity` will be turning towards this angle, if different from `NPCEntity.facing`. |
| route | [ [CoordGrid](../coordgrid.md) ] | Returns a list of the current coordinates in the `NPCEntity`'s movement route.Devuelve el/la position coordinate if the `NPCEntity` is not moving actual. |
| routeEnd | [CoordGrid](../coordgrid.md)? | Returns the final coordinate in the `NPCEntity`'s movement route.Devuelve el/la position coordinate if the `NPCEntity` is not moving actual. |