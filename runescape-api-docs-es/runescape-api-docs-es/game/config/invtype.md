# InvType

## Descripción General

A `InvType` config contains the descriptive data necessary for the game to populate an Inventory.

These config types can be found within the `config.Inv` table:

```lua
config.Inv.AXESHOP
config.Inv["BANK"]
config.Inv.FromID(456) -- config.Inv.ROGUESDEN_SHOP_SKILLCAPE_TRIMMED
```

> **Información**
> An `InvType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `InvType` includes:

* Inventory size
* Stock Count
* TODO

## Ejemplos

```lua
-- Access an InvType config directly by using its name
local metalBankCfg = config.Inv.METAL_BANK
-- or by ID lookup
local metalBankCfg = config.Inv.FromID(id.Inv.METAL_BANK)

-- Retrieve the InvType(s) being used by an Inventory
-- TODO
```

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"METAL_BANK"`. |
| typeName | String | The type of this config. Will always be `"Inv"`. |
| size | Integer | The number of inventory slots in this config. |
| stockCount | Integer | The number of stock [ObjTypes](objtype.md) in this config. |