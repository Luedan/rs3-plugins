# MiniMenu

## Descripción General

The MiniMenu is the primary mechanism for interacting with the game.

Each element in the game, whether a 2D Interface Component or a 3D game world NPC Entity, will add [MiniMenuEntries](#minimenuentry) to the MiniMenu when the cursor, or a tap, is positioned over them.
These entries are recalculated on every Client Logic tick, so long as the MiniMenu remains closed.

When the MiniMenu is opened, by right-click or long-press, the current list of available entries is shown.
The list is sorted by priority, with the higher priority entries shown at the top.

> **Información**
> When accessing the MiniMenu via the API, higher priority entries are instead at the **end** of the list.

The highest priority entry in the list is activated when you left-click or tap while the MiniMenu is closed.
This is also the entry which interface tooltips are generated for, and which affects the current [Cursor](config/cursortype.md) sprite.

## Accessing the MiniMenu

As the MiniMenu's list of [MiniMenuEntries](#minimenuentry) is in constant flux, access and making changes to the MiniMenu is restricted to within specific [Events](../core/events.md).

The principal event for managing the MiniMenu is [Event.MiniMenuReady](../core/events.md#minimenuready).
This event provides access to the full list of entries, as well as the ability to [Swap](#swap) entries.

Additional events [Event.MiniMenuOpened](../core/events.md#minimenuopened) and [Event.MiniMenuClosed](../core/events.md#minimenuclosed) provide **read-only** access to the presented list of entries.

[Event.MiniMenuEntryAdded](../core/events.md#minimenuentryadded) is called when each new entry is added, providing access only to that entry.

[Event.MiniMenuEntrySelected](../core/events.md#minimenuentryselected) is called when a MiniMenu entry is chosen.
This can be from a left-click or tap on a game element, or from selecting an entry from the open MiniMenu.

The only MiniMenu state available outside of these events is [MiniMenu.IsOpen()](#isopen).

## MiniMenuEntry

A MiniMenuEntry contains information about a specific **action** from a specific **source**, which should occur when the entry is selected.

The entry source, like an NPC entity or Interface Component, is indicated by [MiniMenuEntryType](#minimenuentrytype), which covers all the places where actions can be gathered.

Entries also provide additional data, depending on the [MiniMenuEntryType](#minimenuentrytype).
This can be things like access to a source [NPCEntity](entity/npcentity.md) or a ground [CoordGrid](coordgrid.md).

See [MiniMenuEntry properties](#minimenuentry-properties) for additional information.

### Actions and Ops

There is a fixed number of possible actions available, shown in [MiniMenuActionType](#minimenuactiontype).
These actions can be handled by the Client, sent to the Server, or both at the same time.

The legacy name for these actions is called an **Op**.
Each source, like an NPC or Component, has a set of numbered Ops which are individually referred to as Op1, Op2, etc.

Each type also has a Target Op, referred to as OpT.
This is used to apply one entity to another - such as a Spell or Ability to an in-game NPC.

### Verbs and Subjects

Most entries have a **Verb**, like "Chop down", and a **Subject**, like "Oak Tree".
Some simpler entries have only a **Verb**, such as "Walk" or "Cancel".

There are a few common verb types, shown in [MiniMenuActionVerbType](#minimenuactiontype).
These are used to present display strings for common Ops like `MiniMenuActionVerbType.ATTACK` or `MiniMenuActionVerbType.EXAMINE`, while `MiniMenuActionVerbType.OP` covers all custom Ops.

Custom Ops are found in entity configs, or are manually defined in [Component OP configs](../ui/component_configs.md#uicomponentopconfig).

For entities, the Subject display **string** comes from the entity config's `displayName` while the Verb **string** depends on each individual Op found in the entity config.

### Sorting

Entries are sorted within the MiniMenu in the following order:

* Entity distance to camera
* Subject, which groups entries belonging to the same entity or Component
* Action Priority

## Enumeraciones

### MiniMenuEntryType

A list of all the possible source types for each MiniMenuEntry.

| Name | Value |
| --- | --- |
| NONE | 0 |
| INTERFACE | 1 |
| OBJ | 2 |
| LOC | 3 |
| NPC | 4 |
| OTHER | 5 |
| MINIMENU | 6 |
| PLAYER | 7 |
| SELF | 8 |
| MAP | 9 |
| PLUGIN | 10 |

### MiniMenuActionVerbType

The type of action for each entry.
`MiniMenuActionVerbType.OP` is the most common.

| Name | Value |
| --- | --- |
| ATTACK | 0 |
| EXAMINE | 1 |
| OP | 2 |
| UNSPECIFIED | 3 |

### MiniMenuActionType

All available types of action that can be found in a [MiniMenuEntry](#minimenuentry).

Entity sources have individual actions for each numbered Op, such as `OP_LOC1` or `OP_OBJ6`.

Component Ops use `IF_BUTTONX1` and `IF_BUTTONX2` with the Op number found in `MiniMenuEntry.componentData.opIndex`.

The entry source type, and the related property data for the source, are also provided.

| Name | Value | [MiniMenuEntryType](#minimenuentrytype) | Data Property |
| --- | --- | --- | --- |
| TGT_LOC | 2 | LOC | [LocData](#locdata-properties) |
| OP_LOC1 | 3 | LOC | [LocData](#locdata-properties) |
| OP_LOC2 | 4 | LOC | [LocData](#locdata-properties) |
| OP_LOC3 | 5 | LOC | [LocData](#locdata-properties) |
| OP_LOC4 | 6 | LOC | [LocData](#locdata-properties) |
| TGT_NPC | 8 | NPC | [NPCData](#npcdata-properties) |
| OP_NPC1 | 9 | NPC | [NPCData](#npcdata-properties) |
| OP_NPC2 | 10 | NPC | [NPCData](#npcdata-properties) |
| OP_NPC3 | 11 | NPC | [NPCData](#npcdata-properties) |
| OP_NPC4 | 12 | NPC | [NPCData](#npcdata-properties) |
| OP_NPC5 | 13 | NPC | [NPCData](#npcdata-properties) |
| TGT_PLAYER | 15 | PLAYER | [PlayerData](#playerdata-properties) |
| TGT_SELF | 16 | SELF | [PlayerData](#playerdata-properties) |
| TGT_OBJ | 17 | OBJ | [ObjData](#objdata-properties) |
| OP_OBJ1 | 18 | OBJ | [ObjData](#objdata-properties) |
| OP_OBJ2 | 19 | OBJ | [ObjData](#objdata-properties) |
| OP_OBJ3 | 20 | OBJ | [ObjData](#objdata-properties) |
| OP_OBJ4 | 21 | OBJ | [ObjData](#objdata-properties) |
| OP_OBJ5 | 22 | OBJ | [ObjData](#objdata-properties) |
| WALK | 23 | NONE | [GroundData](#grounddata-properties) |
| TGT_BUTTON | 25 | INTERFACE | [ComponentData](#componentdata-properties) |
| PAUSE_BUTTON | 30 | INTERFACE | [ComponentData](#componentdata-properties) |
| OP_PLAYER1 | 44 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER2 | 45 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER3 | 46 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER4 | 47 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER5 | 48 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER6 | 49 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER7 | 50 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER8 | 51 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER9 | 52 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER10 | 53 | PLAYER | [PlayerData](#playerdata-properties) |
| IF_BUTTONX1 | 57 | INTERFACE | [ComponentData](#componentdata-properties) |
| IF_BUTTONT | 58 | INTERFACE | [ComponentData](#componentdata-properties) |
| TGT_GROUND | 59 | NONE | [GroundData](#grounddata-properties) |
| FACE_SQUARE | 60 | NONE | [GroundData](#grounddata-properties) |
| OP_LOC5 | 1001 | LOC | [LocData](#locdata-properties) |
| OP_LOC6 | 1002 | LOC | [LocData](#locdata-properties) |
| OP_NPC6 | 1003 | LOC | [NPCData](#npcdata-properties) |
| OP_OBJ6 | 1004 | LOC | [ObjData](#objdata-properties) |
| WIKI | 1005 | NONE | Unsupported |
| CANCEL | 1006 | NONE | None |
| IF_BUTTONX2 | 1007 | INTERFACE | [ComponentData](#componentdata-properties) |
| OP_MAPELEMENT1 | 1008 | MAP | [MapElementData](#mapelementdata-properties) |
| OP_MAPELEMENT2 | 1009 | MAP | [MapElementData](#mapelementdata-properties) |
| OP_MAPELEMENT3 | 1010 | MAP | [MapElementData](#mapelementdata-properties) |
| OP_MAPELEMENT4 | 1011 | MAP | [MapElementData](#mapelementdata-properties) |
| OP_MAPELEMENT5 | 1012 | MAP | [MapElementData](#mapelementdata-properties) |
| OP_NPC1_LOWPRIORITY | 2009 | NPC | [NPCData](#npcdata-properties) |
| OP_NPC2_LOWPRIORITY | 2010 | NPC | [NPCData](#npcdata-properties) |
| OP_NPC3_LOWPRIORITY | 2011 | NPC | [NPCData](#npcdata-properties) |
| OP_NPC4_LOWPRIORITY | 2012 | NPC | [NPCData](#npcdata-properties) |
| OP_NPC5_LOWPRIORITY | 2013 | NPC | [NPCData](#npcdata-properties) |
| OP_PLAYER1_LOWPRIORITY | 2044 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER2_LOWPRIORITY | 2045 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER3_LOWPRIORITY | 2046 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER4_LOWPRIORITY | 2047 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER5_LOWPRIORITY | 2048 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER6_LOWPRIORITY | 2049 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER7_LOWPRIORITY | 2050 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER8_LOWPRIORITY | 2051 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER9_LOWPRIORITY | 2052 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_PLAYER10_LOWPRIORITY | 2053 | PLAYER | [PlayerData](#playerdata-properties) |
| OP_NPC6_LOWPRIORITY | 3003 | NPC | [NPCData](#npcdata-properties) |

## MiniMenu Functions

### IsOpen

```lua
function MiniMenu.IsOpen() -> Boolean
```

Returns whether the MiniMenu is currently open.
This static method be called at any time.

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the MiniMenu is currently open. |

> **Ejemplo**
> ```lua
> -- Skip some processing if the minimenu is open
> if not MiniMenu.IsOpen() then
>     ...
> end
> ```

## MiniMenu Methods

### Add

```lua
function MiniMenu:Add(label : String, action : Function, ...)
```

Adds a [MiniMenuEntry](#minimenuentry) to the end of the current list of minimenu entries.  
 
It will be displayed with the label specified and call the Lua function specified, with any additional arguments provided in order.

> **Advertencia**
> This method is only available during [Event.MiniMenuEntryAdded](../core/events.md#minimenuentryadded) and [Event.MiniMenuReady](../core/events.md#minimenuready).
> When called during [Event.MiniMenuEntryAdded](../core/events.md#minimenuentryadded) the new entry will be added immediately after the current entry.
> When called during [Event.MiniMenuReady](../core/events.md#minimenuready) the new entry will be added at the bottom of `MiniMenu.entries`.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| label | String | The text displayed for the entry in the minimenu. |
| action | Function | A Lua function that can take any number of arguments, including none. |
| ... | Args | A comma-separated list of arguments that will be passed to the function specified in the action parameter. |

> **Ejemplo**
> ```lua
> function logAdd(a,b)
>     log(a .. " + " .. b .. " = " .. a+b)
> end
> 
> function miniMenuEntryAddedEvent(addedEvent)
>     miniMenuEvent.miniMenu:Add("Log Add (3 + 5)", logAdd, 3, 5)
> end
> 
> Event.MiniMenuReady.Subscribe("miniMenuEntryAddedEvent", miniMenuEntryAddedEvent)
> ```

### Swap

```lua
function MiniMenu:Swap(indexA : Integer, indexB : Integer)
```

Swaps [MiniMenuEntries](#minimenuentry-properties) found at the two provided indices of `MiniMenu.entries`.

> **Información**
> The index values are 1-based.

> **Advertencia**
> This method is only available during [Event.MiniMenuReady](../core/events.md#minimenuready).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| indexA | Integer | The index of the first [MiniMenuEntry](#minimenuentry-properties) in `MiniMenu.entries`. |
| indexB | Integer | The index of the second [MiniMenuEntry](#minimenuentry-properties) in `MiniMenu.entries`. |

> **Ejemplo**
> ```lua
> function onMiniMenuReady(miniMenuEvent)
>     -- Get the available entries
>     local entries = miniMenuEvent.miniMenu.entries
> 
>     -- Store the index of entries we find
>     local idxA = 0
>     local idxB = 0
> 
>     -- Loop all the entries
>     for i,entry in ipairs(entries) do
> 
>         -- If we find the Lumbridge Market bank chest, make a note of the Op indices
>         -- NOTE: The tile coords in entry.locData should ideally be compared here, to make sure the entities match
> 
>         if entry.actionType == MiniMenuActionType.OP_LOC2 and entry.locData.config == config.Loc.CBTV2CA_DEPOSIT_BOX then
>             idxA = i
>         elseif entry.actionType == MiniMenuActionType.OP_LOC4 and entry.locData.config == config.Loc.CBTV2CA_DEPOSIT_BOX then
>             idxB = i
>         end
>     end
> 
>     -- If we found a bank chest, and stored the indices, swap them
>     if idxA ~= 0 and idxB ~= 0 then
>         miniMenuEvent.miniMenu:Swap(idxA, idxB)
>     end
> end
> 
> Event.MiniMenuReady.Subscribe("myEvent", onMiniMenuReady)
> ```

## MiniMenu Properties

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| isOpen | Boolean |  | Whether the MiniMenu is currently open. |
| entryCount | Integer |  | How many entries are in the MiniMenu. |
| entries | [ [MiniMenuEntry](#minimenuentry-properties) ] |  | A list of current entries available in the MiniMenu. |

## MiniMenuEntry Properties

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| actionType | [MiniMenuActionType](#minimenuactiontype) |  | The action type of this entry. |
| actionEntryType | [MiniMenuEntryType](#minimenuentrytype) |  | The entry source type of this entry. |
| actionVerbType | [MiniMenuActionVerbType](#minimenuactionverbtype) |  | The verb type of this entry. |
| verbText | String |  | The verb name of the entry. |
| subjectText | String |  | The subject name of the entry. |
| extraText | String |  | An additional string appended to the entry. |
| fullText | String |  | The full text displayed when the entry is shown in the MiniMenu if `overrideText` has not been set.Combines `verbText`, `subjectText` and `extraText` in that order. |
| overrideText | String |  | Override text for an entry supplied by a plugin. This is displayed in place of an entry's `fullText` if set. |
| cursorID | Integer |  | The Cursor config ID shown when this entry is active.Use `config.Cursor.FromID(cursorID)` to obtain the config. |
| iconSpriteIDs | [ Integer ] |  | An array of sprite IDs which are drawn next to the entry text.Empty if none are drawn. |
| subjectOnOtherLevel | Boolean |  | Whether the source entity is on a different level from the Player Character.NOTE: Not always correct. |
| subjectHash | Integer |  | A (sort of) unique identifier for the entry.This identifier is only unique for entries that share the same `actionEntryType`. |
| npcData? | [NPCData](#npcdata-properties) |  | A collection of data related to this entry.Will be `nil` if unavailable. |
| locData? | [LocData](#locdata-properties) |  | A collection of data related to this entry.Will be `nil` if unavailable. |
| objData? | [ObjData](#objdata-properties) |  | A collection of data related to this entry.Will be `nil` if unavailable. |
| playerData? | [PlayerData](#playerdata-properties) |  | A collection of data related to this entry.Will be `nil` if unavailable. |
| groundData? | [GroundData](#grounddata-properties) |  | A collection of data related to this entry.Will be `nil` if unavailable. |
| mapElementData? | [MapElementData](#mapelementdata-properties) |  | A collection of data related to this entry.Will be `nil` if unavailable. |
| componentData? | [ComponentData](#componentdata-properties) |  | A collection of data related to this entry.Will be `nil` if unavailable. |

### NPCData Properties

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| entity | [NPCEntity](entity/npcentity.md) |  | The NPC entity source for this entry. |

### LocData Properties

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| coordGridX | Integer |  | The south-west tile X coordinate the Loc entity is positioned at. |
| coordGridZ | Integer |  | The south-west tile Z coordinate the Loc entity is positioned at. |
| config | [LocType](config/loctype.md) |  | The config for the Loc entity. |

### ObjData Properties

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| entity | [ObjStackEntity](entity/objstackentity.md) |  | The ObjStack entity source for this entry. |
| stackIndex | Integer |  | The specific object within the source ObjStackEntity that this MiniMenuEntry relates to.Use this with [ObjStackEntity:GetEntry()](entity/objstackentity.md#getentry). |
| config | [ObjType](config/objtype.md) |  | The config for the specific object that this MiniMenuEntry relates to. |

### PlayerData Properties

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| entity | [PlayerEntity](entity/playerentity.md) |  | The Player entity source for this entry. |

### GroundData Properties

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| coordGridX | Integer |  | The tile X coordinate this entry is focused at. |
| coordGridZ | Integer |  | The tile Z coordinate this entry is focused at. |
| fromMiniMap | Boolean |  | `true` if this entry was created from the MiniMap.`false` if this entry was created from the 3D world view. |

### MapElementData Properties

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| mapElementID | Integer |  | The MapElement config ID shown when this entry is active.Use `config.MapElement.FromID(mapElementID)` to obtain the config.TODO: `MapElement` configs are not available yet. |
| categoryID | Integer |  | The Category ID belonging to this map element. |

### ComponentData Properties

| Name | Type | Writeable | Description |
| --- | --- | --- | --- |
| opIndex | Integer |  | The op index for this entry.Valid values are `1` -> `10`. |
| objConfig? | [ObjType](config/objtype.md) |  | Some [Components](../ui/component.md) allow [ObjType](config/objtype.md) IDs to be assigned to them, such as [Sprites](../ui/decorative_components/sprite.md#setassociatedobject) and [Models](../ui/decorative_components/model.md#setassociatedobject).This property provides the config, if set on the source Component.Will be `nil` if unavailable. |
| component | [Component](../ui/component.md) |  | The [Component](../ui/component.md) source for this entry. |