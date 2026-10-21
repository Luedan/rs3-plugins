# LocEntity

## Descripción General

An `LocEntity` represents an instance of an [LocType](../config/loctype.md) that is currently active in the game world.

See [LocList](../list/loclist.md) for information on how to access `LocEntities`.

> **Información**
> An `LocEntity` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

> **Advertencia**
> Use `LocEntity.isValid` to confirm that an entity still exists before trying to access its properties.
Entities can be removed from the client by the server for various reasons, i.e. due to moving beyond the player view distance or being deleted by the server.
When an entity is removed it will become invalid, and any copies of this usertype should be disposed of.
 If the same entity is re-created on the client, such as walking back into visibility range, then a different *new* LocEntity will be created.

Information available within an `LocEntity` includes:

* [LocType](../config/loctype.md)
* World position
* Rotation type
* Visibility status

## Enumeraciones

### RotationType

Indicates the 90-degree rotation type a `LocEntity` is using.
Also see [LocEntity.rotationType](#properties).

| Name | Value |
| --- | --- |
| ZERO | 0 |
| NINETY | 1 |
| ONEEIGHTY | 2 |
| TWOSEVENTY | 3 |

## Ejemplos

```lua
-- Iterate all available LocEntities
local allLocs = LocList.All()
for _,locEntity in ipairs(allLocs) do
    if locEntity.config == config.Loc.FFH_WILLOW_TREE_TRUNK and locEntity.coordGrid == CoordGrid._0_50_50_35_32 then
        -- Found the willow tree next to the Lumbridge Bridge
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
| displayName | String | The display name of this entity. |
| config | [LocType](../config/loctype.md) | The config used by this entity. |
| parentConfig | [LocType](../config/loctype.md) | The parent config used by this entity, if it is a [MultiLoc](../config/loctype.md#multiloc). |
| configID | Integer | The ID of the config used by this entity. |
| parentConfigID | Integer | The ID of the parent config used by this entity, if it is a [MultiLoc](../config/loctype.md#multiloc). |
| isMultiLoc | Boolean | Whether this entity is a [MultiLoc](../config/loctype.md#multiloc). |
| position | Vector3 | The world position of this entity. |
| coordGrid | CoordGrid | Returns the CoordGrid tile this entity is currently on. |
| shapeType | [LocShapeType](../config/loctype.md#locshapetype) | The [LocShapeType](../config/loctype.md#locshapetype) being used by this entity. |
| rotationType | [RotationType](#rotationtype) | The 90-degree rotation type being used by this entity. |
| width | Integer | The width of this entity on the X axis, in grid units.This taken from entity's [LocType](../config/loctype.md) config after being rotated by `rotationType`. |
| length | Integer | The length of this entity on the Z axis, in grid units.This taken from entity's [LocType](../config/loctype.md) config after being rotated by `rotationType`. |
| isHidden | Boolean | Whether this entity has been hidden by game logic. |
| isRoofRemoved | Boolean | Whether this entity has been hidden by the [Remove Roof](../world.md#removeroof) system. |
| currentAnimation | [SeqType](../config/seqtype.md) | The current animation being played by this entity.Returns `nil` if none is set. |