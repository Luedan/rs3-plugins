# GrandExchange

The GrandExchange table contains functions that enable read-only access to properties relevant to the Grand Exchange in the game.

## Enumeraciones

### GrandExchangeOfferType

Type of offer for a offer on the Grand Exchange.

| Name | Value |
| --- | --- |
| BUY | 0 |
| SELL | 1 |

### GrandExchangeOfferStage

Repesentation of a stage for a offer on the Grand Exchange.

| Name | Value |
| --- | --- |
| EMPTY | 0 |
| ADDING | 1 |
| ADDED | 2 |
| VERIFYING | 3 |
| ABORTING | 4 |
| FINISHED | 5 |

## GrandExchangeOffer

A representation of an offer on the Grand Exchange.

### Propiedades

| Property | Tipo | Descripción |
| --- | --- | --- |
| stage | [GrandExchangeOfferStage](#grandexchangeofferstage) | The stage the offer has reached. |
| type | [GrandExchangeOfferType](#grandexchangeoffertype) | The type of offer. |
| item | [ObjType](../game/config/objtype.md) | The item associated with the offer. |
| price | Integer | The gold price per individual item. |
| itemCount | Integer | Number of items in the offer. |
| soldCount | Integer | Number of items that have been sold in the offer. |
| goldFromSale | Integer | Amount of gold available after some items have been bought/sold. |

## Funciones

### GetOffer

```lua
GrandExchange.GetOffer(slot : Integer)
```

Returns the offer in the specified slot or nil if the slot can't be found.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| slot | - | 1-indexed slot number. |

| Retorna | Descripción |
| --- | --- |
| [GrandExchangeOffer](#grandexchangeoffer) | The offer in the specified slot. Is `nil` if the slot can't be found. |

> **Ejemplo**
> ```lua
> local offer = GrandExchange.GetOffer(1)
> -- Do something with the first offer
> ```

### MaxOffers

```lua
GrandExchange.MaxOffers()
```

Returns the maximum number of offers a player can have on the Grand Exchange.

| Retorna | Descripción |
| --- | --- |
| Integer | The maximum number of offers a player can have on the Grand Exchange. |

> **Ejemplo**
> ```lua
> local maxOffers = GrandExchange.MaxOffers()
> for slot = 1,maxOffers do
>     local offer = GrandExchange.GetOffer(slot)
>      -- Do something with each offer
> end
> ```