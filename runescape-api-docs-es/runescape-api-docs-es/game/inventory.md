# Inventory

## Descripción General

La tabla `Inventory` proporciona acceso a [Inv](#inv) objects.

## Funciones

### Find(InvType)

```lua
function Inventory.Find(config : InvType) -> Inv
```

Returns the [Inv](#inv) associated with the supplied [InvType](config/invtype.md).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| config | [InvType](config/invtype.md) | A valid InvType. |

| Retorna | Descripción |
| --- | --- |
| [Inv](#inv) | The inventory container for a list of objects. |

> **Ejemplo**
> ```lua
> local inv = Inventory.Find(config.Inv.INV)
> -- Do something with the inventory
> ```

### Find(Integer)

```lua
function Inventory.Find(id : Integer) -> Inv
```

Returns the [Inv](#inv) associated with the matching ID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | A valid ID value. |

| Retorna | Descripción |
| --- | --- |
| [Inv](#inv) | The inventory container for a list of objects. |

> **Ejemplo**
> ```lua
> local targetInvID = ...
> local inv = Inventory.Find(targetInvID)
> -- Do something with the inventory
> ```

## Inv

### Descripción General

An inventory provides access to a list of [InvSlot](#invslot) entries, each of which contains information about the [ObjType](config/objtype.md) contained within it.  

Inventories are of a fixed size, and their slots may or may not be populated by an [InvSlot](#invslot).

> **Información**
> An `Inv` object is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

> **Advertencia**
> Use `Inv.isValid` to confirm that an inventory still exists before trying to access its properties.
**Inventories can be added or removed from the client by the server for a variety of reasons e.g. the player closes a shop interface.**
When an inventory's data is removed it will become invalid, and any copies of this usertype should be disposed of.
 If the same inventory data is re-added to the client by the server, such as walking back into visibility range, then a different *new* Inv object will be created.

### Métodos

#### GetSlot

```lua
function Inv:GetSlot(index : Integer) -> InvSlot
```

Returns the [InvSlot](#invslot) at the specified index.

> **Advertencia**
> This function returns a copy of the data in the specified slot at the time of execution.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| index | Integer | A valid slot index.Index values are 1-indexed. |

| Retorna | Descripción |
| --- | --- |
| [InvSlot](#invslot) | An object representing the inventory slot specified.   Returns `nil` on failure. |

> **Ejemplo**
> ```lua
> local inv = Inventory.Find(config.Inv.INV)
> local firstSlot = inv:GetSlot(1)
> -- Do something with the slot data
> ```

#### GetSlots

```lua
function Inv:GetSlots() -> [ InvSlot ]
```

Devuelve el/la data associated for all slots in the inventory actual.

> **Advertencia**
> This function returns a copy of the data in the specified slot at the time of execution.

| Retorna | Descripción |
| --- | --- |
| [[InvSlot]](#invslot) | An table of objects representing the inventory slot specified.   Returns `nil` on failure. |

> **Ejemplo**
> ```lua
> local inv = Inventory.Find(config.Inv.INV)
> local slots = inv:GetSlots()
> for i,slot in ipairs(slots) do
>     -- Do something with the slots here
> end
> ```

#### GetTotal(ObjType)

```lua
function Inv:GetTotal(objType : ObjType) -> Integer
```

Returns the number of objects matching a valid [ObjType](config/objtype.md) specified in the associated inventory.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| objType | [ObjType](config/objtype.md) | A valid [ObjType](config/objtype.md). |

| Retorna | Descripción |
| --- | --- |
| Integer | The number of objects matching the specified [ObjType](config/objtype.md). |

> **Ejemplo**
> ```lua
> local inv = Inventory.Find(config.Inv.INV)
> local steelBarTotal = inv:GetTotal(config.Obj.STEEL_BAR)
> ```

#### GetTotal(Integer)

```lua
function Inv:GetTotal(id : Integer) -> Integer
```

Returns the number of objects matching a valid [ObjType](config/objtype.md) ID specified in the associated inventory.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | A valid [ObjType](config/objtype.md) ID. |

| Retorna | Descripción |
| --- | --- |
| Integer | The number of objects matching the id. |

> **Ejemplo**
> ```lua
> local inv = Inventory.Find(config.Inv.INV)
> local id = config.Obj["STEEL_BAR"].id
> local steelBarTotal = inv:GetTotal(id)
> ```

#### GetCategoryTotal

```lua
function Inv:GetCategoryTotal(category : Integer) -> Integer
```

Returns the number of objects in the inventory that are in the category specified.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| category | Integer | A valid category of object. |

| Retorna | Descripción |
| --- | --- |
| Integer | The number of objects matching the specified category. |

> **Ejemplo**
> ```lua
> local inv = Inventory.Find(config.Inv.INV)
> local categoryTotal = inv:GetCategoryTotal(config.Obj.STEEL_BAR.category)
> ```

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | Unique ID associated with the inventory. |
| config | [InvType](config/invtype.md) | [InvType](config/invtype.md) config used to construct the inventory. |
| isValid | Boolean | Is the inventory object valid. |
| slotCount | Integer | Total number of slots. |
| usedSlotCount | Integer | Number of non-empty slots. |
| freeSlotCount | Integer | Number of empty slots. |

## InvSlot

### Descripción General

A representation of an individual inventory slot.

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| obj | [ObjType](./config/objtype.md) | Unique ID associated with the inventory. |
| count | Integer | Number of objects in the slot. |