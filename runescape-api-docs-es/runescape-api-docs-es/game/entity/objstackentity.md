# ObjStackEntity

## ObjStackEntity

### Descripción General

An `ObjStackEntity` represents an collection of individual [ObjEntry](#objentry) instances that are currently on a tile in the game world.

See [ObjStackList](../list/objstacklist.md) for information on how to access `ObjStackEntities`.

> **Información**
> An `ObjStackEntity` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

> **Advertencia**
> Use `ObjStackEntity.isValid` to confirm that an entity still exists before trying to access its properties.
Entities can be removed from the client by the server for various reasons, i.e. due to moving beyond the player view distance or death.
When an entity is removed it will become invalid, and any copies of this usertype should be disposed of.
 If the same entity is re-added to the client by the server, such as walking back into visibility range, then a different *new* ObjStackEntity will be created.

Information available within an `ObjStackEntity` includes:

* [ObjEntries](#objentry)
* World position

### Ejemplos

```lua
-- Iterate all active ObjStackEntities
local allObjStacks = ObjStackList.All()
for _,objStackEntity in ipairs(allObjStacks) do
    for i = 1,objStackEntity.stackSize do
        local entry = objStackEntity:GetEntry(i)
        if entry.config == config.Obj.LOGS then
            -- ObjStack has a log in it
        end
    end
end
```

### Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

### Métodos

#### GetEntry

```lua
function ObjStackEntity:GetEntry(index : Integer) -> ObjEntry
```

Returns the [ObjEntry](#objentry) at the given `index`.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| index | Integer | The index of the [ObjEntry](#objentry) to return.The value of `index` starts at `1`.Returns `nil` if no entry is found at the given index. |

| Retorna | Descripción |
| --- | --- |
| [ObjEntry](#objentry) | An [ObjEntry](#objentry) within an [ObjStackEntity](#objstackentity). |

> **Ejemplo**
> ```lua
> -- Find all objStacks with logs in them
> local found = ObjList.ByConfig(config.Obj.LOGS);
> for _,objStackEntity in ipairs(found) do
>     for i=1,objStackEntity.stackSize do
>         -- Get each entry in turn
>         local entry = objStackEntity:GetEntry(i)
>         if entry.config == config.Obj.LOGS then
>             -- Found a logs entry within the stack
>         end
>     end
> end
> ```

#### HasObj

```lua
function ObjStackEntity:HasObj(objType : ObjType) -> Boolean
```

Returns whether an [ObjStackEntity](#objstackentity) contains an [ObjEntry](#objentry) referencing the given [ObjType](../config/objtype.md).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| objType | [ObjType](../config/objtype.md) | The [ObjType](../config/objtype.md) to search for. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the [ObjType](../config/objtype.md) was found. |

> **Ejemplo**
> ```lua
> -- Gather all objStacks
> local found = ObjList.All(config.Obj.LOGS);
> for _,objStackEntity in ipairs(found) do
>     -- Check for logs
>     if objStackEntity:HasObj(config.Obj.LOGS) then
>         -- This objStack contains logs
>     end
> end
> ```

#### HasObjID

```lua
function ObjStackEntity:HasObjID(objTypeID : Integer) -> Boolean
```

Returns whether an [ObjStackEntity](#objstackentity) contains an [ObjEntry](#objentry) referencing the given [ObjType](../config/objtype.md) ID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| objTypeID | Integer | The ID of [ObjType](../config/objtype.md) to search for. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the [ObjType](../config/objtype.md) was found. |

> **Ejemplo**
> ```lua
> -- Gather all objStacks
> local found = ObjList.All(config.Obj.LOGS);
> for _,objStackEntity in ipairs(found) do
>     -- Check for logs
>     if objStackEntity:HasObjID(id.Obj.LOGS) then
>         -- This objStack contains logs
>     end
> end
> ```

### Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| isValid | Boolean | Whether this entity still exists. Dispose of this usertype object when invalid. |
| position | Vector3 | The world position of this `ObjStackEntity`. |
| coordGrid | CoordGrid | Returns the CoordGrid tile this `ObjStackEntity` is currently on. |
| aabb | [AABB](../../math/aabb.md) | Devuelve el/la bounding box for this `ObjStackEntity` actual. |
| stackSize | Integer | The number of [ObjEntries](#objentry) in this `ObjStackEntity`. |

## ObjEntry

### Descripción General

Every `ObjStackEntity` contains one or more instances of `ObjEntry`.
Each `ObjEntry` references a single [ObjType](../config/objtype.md) config and a count of how many there are.

> **Información**
> For objects that cannot stack, like logs, there will be a separate entry for each one.
For stackable objects, like arrowheads, there will be a single entry with a total count of how many there are.
 *Stackable objects do not merge*.
If another object of the same stackable type was dropped into the stack, it will remain a separate object.

### Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

### Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| config | [ObjType](../config/objtype.md) | The config that describes this entry. |
| configID | Integer | The config ID that describes this entry. |
| count | Integer | How many of this object are in this specific entry.This will always be `1` for [ObjTypes](../config/objtype.md) that cannot stack. |