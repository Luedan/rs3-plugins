# Sistema de Eventos

## Descripción General

An event is a change within the RuneScape Client, such as a [NPC spawning](#npcentityadded), which can be reported to plugin functions that have *subscribed* to that change.

Functions are subscribed with a reference name, and can be unsubscribed with the same name.

A plugin can subscribed multiple functions to the same event, so long as their reference names are different.

> **Información**
> When an event is triggered, it will execute all functions subscribed to it *in the order they were subscribed*.

> **Ejemplo**
> ```lua
> -- Subscribes a function to an event
> Event.NPCEntityAdded.Subscribe("myRefName", function(npcAddedEvent) log("An NPC was added!") end)
> 
> -- Unsubscribes the previous function
> Event.NPCEntityAdded.Unsubscribe("myRefName")
> 
> -- Multiple functions can be subscribed to the same event
> Event.NPCEntityAdded.Subscribe("myRefName", function(npcAddedEvent) log("An NPC was added!") end)
> Event.NPCEntityAdded.Subscribe("aDifferentRefName", function(npcAddedEvent) log("I can't believe it.") end)
> Event.NPCEntityAdded.Subscribe("theThirdOne", function(npcAddedEvent) log("Just baffling stuff.") end)
> 
> -- Log output:
> -- An NPC was added!
> -- I can't believe it.
> -- Just baffling stuff.
> 
> -- Unsubscribe order doesn't matter
> Event.NPCEntityAdded.Unsubscribe("aDifferentRefName");
> Event.NPCEntityAdded.Unsubscribe("myRefName");
> Event.NPCEntityAdded.Unsubscribe("theThirdOne");
> ```

Re-using the same reference name in a plugin will overwrite the previously subscribed function, but only for that type of event.

> **Ejemplo**
> ```lua
> -- Subscribe first function
> Event.NPCEntityAdded.Subscribe("myRefName", function(npcAddedEvent) log("An NPC was added!") end)
> 
> -- Subscribe another for a different event, using the same reference name
> -- This doesn't overwrite the first function
> Event.NPCEntityRemoved.Subscribe("myRefName", function(npcRemovedEvent) log("An NPC was removed!") end)
> 
> -- Subscribe to the first event again
> -- This DOES overwrite the first function
> Event.NPCEntityAdded.Subscribe("myRefName", function(npcAddedEvent) log("An NPC was added, at coord " .. to_string(npcAddedEvent.npcEntity.coordGrid) .. "!") end)
> 
> -- Unsubscribes both functions
> Event.NPCEntityAdded.Unsubscribe("myRefName");
> Event.NPCEntityRemoved.Unsubscribe("myRefName");
> ```

Re-using the same reference name across multiple plugins will not overwrite existing subscribed functions made in other plugins.

> **Ejemplo**
> ```lua
> -- In plugin A
> Event.NPCEntityAdded.Subscribe("myRefName", function(npcAddedEvent) log("I'm called from Plugin A!") end)
> 
> -- In plugin B
> Event.NPCEntityAdded.Subscribe("myRefName", function(npcAddedEvent) log("I'm called from Plugin B!") end)
> 
> -- Log output:
> -- I'm called from Plugin A!
> -- I'm called from Plugin B!
> ```

## Event payloads

Most events provide Una tabla que contiene data related to the change which occurred.

In some cases, the payload data can be modified before it is further processed by the client.
These modifications are then passed to the next subscribed function.

> **Ejemplo**
> Here a chat message is passed to an event before being added to the chat window.
> ```lua
> function addHello(chatMessageEvent)
>     chatMessageEvent.chatMessage = chatMessageEvent.chatMessage ... " Hello!"
>     log(chatMessageEvent.chatMessage)
> end
> 
> function addGoodbye(chatMessageEvent)
>     chatMessageEvent.chatMessage = chatMessageEvent.chatMessage ... " Goodbye!"
>     log(chatMessageEvent.chatMessage)
> end
> 
> -- In plugin A
> Event.ChatMessage.Subscribe("hello", addHello)
> 
> -- In plugin B
> Event.ChatMessage.Subscribe("goodbye", addGoodbye)
> 
> -- For a new message received: "I'm a chat message."
> -- Log output:
> -- I'm a chat message. Hello!
> -- I'm a chat message. Hello! Goodbye!
> ```

## Enumeraciones

### EntityType

These are provided as part of the following event payloads:

* [PlayerEntityAdded](#playerentityadded)
* [PlayerEntityRemoved](#playerentityremoved)
* [NPCEntityAdded](#npcentityadded)
* [NPCEntityRemoved](#npcentityremoved)
* [ObjStackEntityAdded](#objstackentityadded)
* [ObjStackEntityRemoved](#objstackentityremoved)
* [ObjStackEntityChanged](#objstackentitychanged)
* [EntityDraw](#entitydraw)

| Name | Valor | Descripción |
| --- | --- | --- |
| LOCATION | 0 | A [LocEntity](../game/entity/locentity.md).These entities are the dynamic form of location, e.g. they animate or are a [MultiLoc](../game/config/loctype.md#multiloc), etc. |
| NPC | 1 | A [NPCEntity](../game/entity/npcentity.md). |
| PLAYER | 2 | A [PlayerEntity](../game/entity/playerentity.md). |
| OBJSTACK | 3 | An [ObjStackEntity](../game/entity/objstackentity.md). |
| COMBINED_LOCATION_SECTION | 12 | A [LocEntity](../game/entity/locentity.md).These entities are the static form of location, e.g. they are interactable but do not animate, etc. |

### GameState

These are provided as part of the [GameStateChanged](#gamestatechanged) event payload.

| Name | Value |
| --- | --- |
| BOOT | 0 |
| INIT | 1 |
| LOGINSCREEN | 10 |
| LOBBY | 20 |
| ACCOUNT_CREATE | 23 |
| GAME | 30 |
| RECONNECTING | 35 |
| RECONNECTING_FULL | 36 |
| SWITCH_WORLD | 37 |
| LOADING | 40 |

## Supported events

### Logic

Called each time the client begins a logic update.
The client runs at a fixed 50 logic ticks per second.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| logicTick | Integer |  | How many logic ticks have occurred since the client was started. |

> **Ejemplo**
> ```lua
> Event.Logic.Subscribe("myEvent", function(logicEvent) log("Client tick is currently " .. logicEvent.logicTick) end)
> ```

### ServerLogic

Called each time the client finishes processing a data packet sent from the server.
This is approximately synced with the server tick rate of 0.6 seconds (600ms) per tick.

> **Información**
> This event has no payload data.

> **Ejemplo**
> ```lua
> Event.ServerLogic.Subscribe("myEvent", function() log("Server tick has occurred") end)
> ```

### Draw

Called each time the client begins a draw update.
The interval between draw events is determined by the frame rate.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| timeDeltaSecs | Float |  | The time, in seconds, since the last draw event (often known as the delta). |

> **Ejemplo**
> ```lua
> Event.Draw.Subscribe("myEvent", function(drawEvent) log("My FPS is " .. (1.0 / drawEvent.timeDeltaSecs)) end)
> ```

### OptionalDependencyChanged

Called when an optional dependency plugin is enabled or disabled.

This event is only sent to plugins which have registered the changing plugin as an [optional dependency](../structure.md#external-plugin-dependencies).

This event is automatically created for plugins that use the built-in [PluginDependencyUpdate](../structure.md#dependency-updates) method.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| pluginIdentifier | String |  | The identifier name of the optional dependency plugin. |
| enabled | Boolean |  | Whether the optional dependency plugin is now enabled or disabled. |

> **Ejemplo**
> ```lua
> function depChanged(optionalDependencyChangedEvent)
>     log("Optional dependency", optionalDependencyChangedEvent.pluginIdentifier, "is now", optionalDependencyChangedEvent.enabled)
> end
> Event.OptionalDependencyChanged.Subscribe("myEvent", depChanged)
> ```

### OptionalPermissionChanged

Called when an optional [permission](plugin.md#pluginpermissions) is approved or revoked for a plugin.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| permissionName | String |  | El nombre de [permission](plugin.md#pluginpermissions). |
| enabled | Boolean |  | Whether the permission is now enabled or disabled. |

> **Ejemplo**
> ```lua
> function permChanged(optionalPermissionChangedEvent)
>     log("Optional permission", optionalPermissionChangedEvent.permissionName, "is now", optionalPermissionChangedEvent.enabled)
> end
> Event.OptionalPermissionChanged.Subscribe("myEvent", permChanged)
> ```

### KeyUp

Called when a [Keyboard](keyboard.md) key press is released.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| gameKey | [GameKey](keyboard.md#gamekey) |  | The game key which was released. |
| systemKey | [SystemKey](keyboard.md#systemkey) |  | The system key equivalent to `gameKey` which was released. |
| modifiers | Integer |  | A bitfield containing the [modifier keys](keyboard.ms#modifierkey) currently held. |
| timestamp | Integer |  | The time, in milliseconds, when the key was released. |

> **Ejemplo**
> ```lua
> Event.KeyUp.Subscribe("myEvent", function(keyUpEvent) log("I just released the " .. GameKey.FromID(keyUpEvent.gameKey) .. " key!") end)
> ```

### KeyDown

Called when a [Keyboard](keyboard.md) key press is first pressed, and when a key-repeat event is sent by the OS.

An equivalent [KeyTyped](#keytyped) event is always sent immediately after this event.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| isRepeat | Boolean |  | Whether the key press is a repeat or not.A value of `false` means the key has just been pressed.A value of `true` means the key was already pressed and the OS has re-sent the key event as a repeat. |
| gameKey | [GameKey](keyboard.md#gamekey) |  | The game key which was pressed. |
| systemKey | [SystemKey](keyboard.md#systemkey) |  | The system key equivalent to `gameKey` which was pressed. |
| modifiers | Integer |  | A bitfield containing the [modifier keys](keyboard.ms#modifierkey) currently held. |
| timestamp | Integer |  | The time, in milliseconds, when the key was first pressed, or the repeat event was sent. |

> **Ejemplo**
> ```lua
> function keyDownFunc(keyDownEvent)
>     if keyDownEvent.isRepeat then
>         log("The " .. GameKey.FromID(keyDownEvent.gameKey) .. " key was held down and repeated!")
>     else
>         log("I just pressed the " .. GameKey.FromID(keyDownEvent.gameKey) .. " key!")
>     end
> end
> Event.KeyDown.Subscribe("myEvent", keyDownFunc)
> ```

### KeyTyped

This event provides the string character generated by the combination of keys just pressed.

> **Nota**
> The character value provided may not be a printable one once converted to a string value.

This event always follows an equivalent [KeyDown](#keydown) event.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| char | Integer |  | The integer value of the character generated.This can be converted to a string value with:`local keyStr = string.char(keyTypedEvent.char)` |
| modifiers | Integer |  | A bitfield containing the [modifier keys](keyboard.ms#modifierkey) currently held. |
| timestamp | Integer |  | The time, in milliseconds, when the character was generated. |

> **Ejemplo**
> ```lua
> Event.KeyTyped.Subscribe("myEvent", function(keyTypedEvent) log("I just typed " .. string.char(keyTypedEvent.char)) end)
> ```

### VarTransmit

Called when a variable update is transmitted from the server to the client.
The variable is not guaranteed to have changed.

> **Información**
> This event is called immediately after the variable has been set.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| var | [VarType](../game/config/vartype.md) |  | The variable config that triggered the event. |
| oldValue | IntegerString |  | The previous value of the config.The return type is determined by the variable config. |
| newValue | IntegerString |  | The current value of the config.The return type is determined by the variable config. |

> **Ejemplo**
> ```lua
> function varTest(varTransmitEvent)
>     if varTransmitEvent.var == var.Player.COMBATV2_MELEE_DEFENCE then
>         log("Value change: " .. (varTransmitEvent.oldValue or "nil") .. " -> " .. (varTransmitEvent.newValue or "nil"))
>     end
> end
> Event.VarTransmit.Subscribe("myEvent", varTest)
> ```

### ChatMessage

Called each time the client receives a message from the server, or a local [Chat.AddMessage()](../game/chat.md#addmessage), that is intended for a chat window.

There are a variety of chat message types that can be received, see [ChatType](../game/chat.md#chattype).

> **Advertencia**
> A plugin will only receive these events if it has requested and been granted the [chatAccess](plugin.md#pluginpermissions) permission.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| chatMessage | String |  | The message received.Can be edited freely, and will be passed to any subsequent subscribed functions. |
| senderNameUnfiltered | String |  | An unfiltered version of a Player Character's name.Will be an empty string if no sender is attributed to the message. |
| senderNameFiltered | String |  | A filtered version of a Player Character's name intended for display, which may be altered depending on the current language context.This string may not be unique due to any filtering performed.Will be an empty string if no sender is attributed to the message. |
| senderNameSimple | String |  | A filtered version of a Player Character's name without any pre- or post-fixes.Will be an empty string if no sender is attributed to the message. |
| chatType | [ChatType](../game/chat.md#chattype) |  | The type of chat message. |
| timestamp | Integer |  | The time when the message was received.Timestamp is in seconds since Unix epoch. |

> **Ejemplo**
> ```lua
> function messageFunc(chatMessageEvent)
>     if chatMessageEvent.chatType == ChatType.PRIVATE_INCOMING then
>         -- Wrap message in a red colour tag
>         chatMessageEvent.chatMessage = "<col=FF0000>" .. chatMessageEvent.chatMessage .. "</col>"
>     end
> end
> Event.ChatMessage.Subscribe("myEvent", messageFunc)
> ```

### PlayerEntityAdded

Called when a player entity is added to the game world.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| playerEntity | [PlayerEntity](../game/entity/playerentity.md) |  | The player entity. |
| entityType | [EntityType](#entitytype) |  | The type of entity.This is always `EntityType.PLAYER`. |

> **Ejemplo**
> ```lua
> function playerFunc(playerEntityAddedEvent)
>     log("Player " .. playerEntityAddedEvent.playerEntity.displayName .. " has appeared!")
> end
> Event.PlayerEntityAdded.Subscribe("myEvent", playerFunc)
> ```

### PlayerEntityRemoved

Called when a player entity is removed from the game world.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| playerEntity | [PlayerEntity](../game/entity/playerentity.md) |  | The player entity. |
| entityType | [EntityType](#entitytype) |  | The type of entity.This is always `EntityType.PLAYER`. |

> **Ejemplo**
> ```lua
> function playerFunc(playerEntityRemovedEvent)
>     log("Player " .. playerEntityRemovedEvent.playerEntity.displayName .. " has departed.")
> end
> Event.PlayerEntityRemoved.Subscribe("myEvent", playerFunc)
> ```

### NPCEntityAdded

Called when an NPC entity is added to the game world.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| npcEntity | [NPCEntity](../game/entity/npcentity.md) |  | The NPC entity. |
| entityType | [EntityType](#entitytype) |  | The type of entity.This is always `EntityType.NPC`. |

> **Ejemplo**
> ```lua
> function npcFunc(npcEntityAddedEvent)
>     log("NPC " .. npcEntityAddedEvent.npcEntity.displayName .. " has appeared!")
> end
> Event.NPCEntityAdded.Subscribe("myEvent", npcFunc)
> ```

### NPCEntityRemoved

Called when an NPC entity is removed from the game world.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| npcEntity | [NPCEntity](../game/entity/npcentity.md) |  | The NPC entity. |
| entityType | [EntityType](#entitytype) |  | The type of entity.This is always `EntityType.NPC`. |

> **Ejemplo**
> ```lua
> function npcFunc(npcEntityRemovedEvent)
>     log("NPC " .. npcEntityRemovedEvent.npcEntity.displayName .. " has departed.")
> end
> Event.NPCEntityRemoved.Subscribe("myEvent", npcFunc)
> ```

### ObjStackEntityAdded

Called when an objStack entity is added to the game world.
This event provides the first object in the stack, with additional objects being provided by [ObjStackEntityChanged](#objstackentitychanged).

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| objStackEntity | [ObjStackEntity](../game/entity/objstackentity.md) |  | The objStack entity. |
| entityType | [EntityType](#entitytype) |  | The type of entity.This is always `EntityType.OBJSTACK`. |
| objType | [ObjType](../game/config/objtype.md) |  | The config type of the object that was added to the objStack. |
| count | Integer |  | How many of the object was added. |
| isOwner | Boolean |  | Whether the local player is the owner of the stack. |

> **Ejemplo**
> ```lua
> function objStackAddedFunc(objStackEntityAddedEvent)
>     log("An objStack has been added, " .. objStackEntityAddedEvent.count .. "x of " .. objStackEntityAddedEvent.objType.name)
> end
> Event.ObjStackEntityAdded.Subscribe("myEvent", objStackAddedFunc)
> ```

### ObjStackEntityRemoved

Called when an objStack entity is removed to the game world.
This event occurs when the final object in a stack is picked up, or the objStack goes out of view range.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| objStackEntity | [ObjStackEntity](../game/entity/objstackentity.md) |  | The objStack entity. |
| entityType | [EntityType](#entitytype) |  | The type of entity.This is always `EntityType.OBJSTACK`. |
| objType | [ObjType](../game/config/objtype.md) |  | The config type of the object that was removed from the objStack. |
| count | Integer |  | How many of the object was removed. |
| isOwner | Boolean |  | Whether the local player is the owner of the stack. |

> **Ejemplo**
> ```lua
> function objStackRemovedFunc(objStackEntityRemovedEvent)
>     log("An objStack has been removed, " .. objStackEntityRemovedEvent.count .. "x of " .. objStackEntityRemovedEvent.objType.name)
> end
> Event.ObjStackEntityRemoved.Subscribe("myEvent", objStackRemovedFunc)
> ```

### ObjStackEntityChanged

Called when an existing objStack entity has changed.
This event occurs when objects are added or removed from the tile the objStack is in.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| objStackEntity | [ObjStackEntity](../game/entity/objstackentity.md) |  | The objStack entity. |
| entityType | [EntityType](#entitytype) |  | The type of entity.This is always `EntityType.OBJSTACK`. |
| objType | [ObjType](../game/config/objtype.md) |  | The config type of the object that was added or removed from the objStack. |
| oldCount | Integer |  | The previous amount of the object. |
| newCount | Integer |  | The current amount of the object. |
| isOwner | Boolean |  | Whether the local player is the owner of the stack. |

> **Ejemplo**
> ```lua
> function objStackChangedFunc(objStackEntityChangedEvent)
>     log("An objStack has changed, " .. objStackEntityRemovedEvent.oldCount .. "x -> " .. objStackEntityRemovedEvent.newCount .. "x of " .. objStackEntityRemovedEvent.objType.name)
> end
> Event.ObjStackEntityChanged.Subscribe("myEvent", objStackChangedFunc)
> ```

### WindowFocusChanged

Called when the focus of the game window changes.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| hasFocus | Boolean |  | Whether the window has gained or lost focus. |

> **Ejemplo**
> ```lua
> function focusChangedFunc(windowFocusChangedEvent)
>     log("Window focus changed: " .. (windowFocusChangedEvent.hasFocus and "in focus" or "not in focus"))
> end
> Event.WindowFocusChanged.Subscribe("myEvent", focusChangedFunc)
> ```

### GameStateChanged

Called when the client's internal state changes.

See [GameState](#gamestate) for the list of possible states.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| oldState | [GameState](#gamestate) |  | The previous game state. |
| newState | [GameState](#gamestate) |  | The current game state. |

> **Ejemplo**
> ```lua
> function gameStateChangedFunc(gameStateChangedEvent)
>     log("Game state changed: " .. GameState.FromID(gameStateChangedEvent.oldState) .. " -> " .. GameState.FromID(gameStateChangedEvent.newState))
> end
> Event.GameStateChanged.Subscribe("myEvent", gameStateChangedFunc)
> ```

### EntityDraw

Called when an entity is about to be drawn.

> **Advertencia**
> This event requires a boolean return value to indicate whether the entity should continue drawing.
See below for an example.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| entityType | [EntityType](#entitytype) |  | The type of entity. |
| npcEntityplayerEntityobjStackEntity | [NPCEntity](../game/entity/npcentity.md)[PlayerEntity](../game/entity/playerentity.md)[ObjStackEntity](../game/entity/objstackentity.md) |  | The entity being drawn.Returns one of the listed entities, use `entityType` to select the correct one. |

> **Ejemplo**
> ```lua
> function hansHiderFunc(entityDrawEvent)
>     -- If the entity is an NPC and has the config belonging to Hans
>     if entityDrawEvent.entityType == EntityType.NPC and entityDrawEvent.npcEntity.configID == id.NPC.HANS
>         -- Returning false tells the entity to skip drawing
>         return false
>     end
>     -- Returning true tells the entity to continue drawing
>     return true
> end
> Event.EntityDraw.Subscribe("myEvent", hansHiderFunc)
> ```

### WindowSizeChanged

Called when the size of the game window changes.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| oldWidth | Integer |  | The old width of the window. |
| oldHeight | Integer |  | The old height of the window. |
| newWidth | Integer |  | The new width of the window. |
| newHeight | Integer |  | The new height of the window. |

> **Ejemplo**
> ```lua
> function windowSizeChangedFunc(windowSizeChangedEvent)
>     log("Window size changed: " .. windowSizeChangedEvent.oldWidth .. " x " .. windowSizeChangedEvent.oldHeight .. " -> " .. windowSizeChangedEvent.newWidth .. " x " .. windowSizeChangedEvent.newHeight)
> end
> Event.WindowSizeChanged.Subscribe("myEvent", windowSizeChangedFunc)
> ```

### SkillTransmit

Called when a player character's skill changes in value.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| skill | [SkillType](../game/player.md#skilltype) |  | The skill that has changed in value. |
| oldXP | Integer |  | The previous XP value for the skill. |
| newXP | Integer |  | The current XP value for the skill. |
| oldGameplayLevel | Integer |  | The previous gameplay level for the skill. |
| newGameplayLevel | Integer |  | The current gameplay level for the skill. |

> **Ejemplo**
> ```lua
> function skillTransmitFunc(skillTransmitEvent)
>     log("Skill transmit: (ID " .. skillTransmitEvent.skill .. " (" .. SkillType.FromID(skillTransmitEvent.skill) .. "), XP " .. skillTransmitEvent.oldXP .. " -> " .. skillTransmitEvent.newXP .. ", Gameplay Level " .. skillTransmitEvent.oldGameplayLevel .. " -> " .. skillTransmitEvent.newGameplayLevel)
> end
> Event.SkillTransmit.Subscribe("myEvent", skillTransmitFunc)
> ```

### RunEnergyTransmit

Called when the player character's run energy changes in value.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| oldRunEnergy | Integer |  | The player character's previous run energy value. |
| newRunEnergy | Integer |  | The player character's current run energy value. |

> **Ejemplo**
> ```lua
> function runEnergyTransmitFunc(runEnergyTransmitEvent)
>     log("Run energy: " .. runEnergyTransmitEvent.oldRunEnergy .. " -> " .. runEnergyTransmitEvent.newRunEnergy)
> end
> Event.RunEnergyTransmit.Subscribe("myEvent", runEnergyTransmitFunc)
> ```

### RunWeightTransmit

Called when the player character's weight changes in value.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| oldRunWeight | Integer |  | The player character's previous weight value. |
| newRunWeight | Integer |  | The player character's current weight value. |

> **Ejemplo**
> ```lua
> function runWeightTransmitFunc(runWeightTransmitEvent)
>     log("Weight: " .. runWeightTransmitEvent.oldRunWeight .. " -> " .. runWeightTransmitEvent.newRunWeight)
> end
> Event.RunWeightTransmit.Subscribe("myEvent", runWeightTransmitFunc)
> ```

### MiniMenuOpened

Called when the [MiniMenu](../game/minimenu.md) has been opened.

> **Información**
> Access to the MiniMenu's list of entries is available from this event's payload, but cannot be edited.
> Use [Event.MiniMenuReady](#minimenuready) to make changes to the list of entries.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| miniMenu | [MiniMenu](../game/minimenu.md#minimenu-properties) |  | The current MiniMenu and its list of entries. |

> **Ejemplo**
> ```lua
> function miniMenuOpenedFunc(miniMenuOpenedEvent)
>     log("Entry count: " .. miniMenuOpenedEvent.miniMenu.entryCount)
> end
> Event.MiniMenuOpened.Subscribe("myEvent", miniMenuOpenedFunc)
> ```

### MiniMenuClosed

Called when the [MiniMenu](../game/minimenu.md) has been closed.

This is called both when a [MiniMenuEntry](../game/minimenu.md#minimenuentry-properties) is selected and when the MiniMenu closes without selecting a [MiniMenuEntry](../game/minimenu.md#minimenuentry-properties).

> **Información**
> Access to the MiniMenu's list of entries is available from this event's payload, but cannot be edited.
> Use [Event.MiniMenuReady](#minimenuready) to make changes to the list of entries.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| miniMenu | [MiniMenu](../game/minimenu.md#minimenu-properties) |  | The current MiniMenu and its list of entries. |

> **Ejemplo**
> ```lua
> function miniMenuClosedFunc(miniMenuClosedEvent)
>     log("Entry count: " .. miniMenuClosedEvent.miniMenu.entryCount)
> end
> Event.MiniMenuClosed.Subscribe("myEvent", miniMenuClosedFunc)
> ```

### MiniMenuReady

Called when the [MiniMenu](../game/minimenu.md) has finished adding all entries for the current Logic tick and can now be altered.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| miniMenu | [MiniMenu](../game/minimenu.md#minimenu-properties) | Using [Swap()](../game/minimenu.md#swap) | The current MiniMenu and its list of entries. |

> **Ejemplo**
> ```lua
> function miniMenuReadyFunc(miniMenuReadyEvent)
>     -- Make changes to the minimenu
>     local count = miniMenuReadyEvent.miniMenu.entryCount
>     if count > 1 then
>         -- Swap the highest priority entries
>         miniMenuReadyEvent.miniMenu:Swap(count - 1, count)
>     end
> end
> Event.MiniMenuReady.Subscribe("myEvent", miniMenuReadyFunc)
> ```

### MiniMenuEntryAdded

Called when a [MiniMenuEntry](../game/minimenu.md#minimenuentry) has been added to the [MiniMenu](../game/minimenu.md).

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| entry | [MiniMenuEntry](../game/minimenu.md#minimenuentry-properties) |  | The MiniMenuEntry which has been added to the MiniMenu. |

> **Ejemplo**
> ```lua
> function miniMenuEntryAddedFunc(miniMenuEntryAddedEvent)
>     if miniMenuEntryAddedEvent.entry.actionEntryType == MiniMenuEntryType.NPC then
>         local npcEntity = miniMenuEntryAddedEvent.entry.npcData.entity
>         -- Do something with the NPC
>     end
> end
> Event.MiniMenuEntryAdded.Subscribe("myEvent", miniMenuEntryAddedFunc)
> ```

### MiniMenuEntrySelected

Called when a [MiniMenuEntry](../game/minimenu.md#minimenuentry) has been selected from the [MiniMenu](../game/minimenu.md).

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| entry | [MiniMenuEntry](../game/minimenu.md#minimenuentry-properties) |  | The MiniMenuEntry which has been selected  from the MiniMenu. |

> **Ejemplo**
> ```lua
> function miniMenuEntrySelectedFunc(miniMenuEntrySelectedEvent)
>     if miniMenuEntrySelectedEvent.entry.actionEntryType == MiniMenuEntryType.NPC then
>         local npcEntity = miniMenuEntrySelectedEvent.entry.npcData.entity
>         -- Do something with the NPC that was selected
>     end
> end
> Event.MiniMenuEntrySelected.Subscribe("myEvent", miniMenuEntrySelectedFunc)
> ```

### LocAdded

Called when a location is added to the game world, or changed from one location ito another, by the server.

A location will only be changed to another if the both `shapeType` and `coordGrid` match.

If a custom transform is not provided in the event, then the new location will inherit any pre-existing custom transform from any location it is changing.

> **Advertencia**
> If a location is changed via its MultiLoc variable state, then this event is **not** called.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| config | [LocType](../game/config/loctype.md) |  | The location config. |
| shapeType | [LocShapeType](../game/config/loctype.md#locshapetype) |  | The [LocShapeType](../game/config/loctype.md#locshapetype) of the location being added. |
| rotationType | [RotationType](../game/entity/locentity.md#rotationtype) |  | The 90-degree rotation type being used by this location. |
| coordGrid | [CoordGrid](../game/coordgrid.md) |  | The coordinate the location is being added to. |
| overrideTransform | Boolean |  | Whether an overriding transformation should be applied to this location. |
| transformTranslate | [Vector3](../math/vector.md#vector3) |  | The overriding translation transformation. |
| transformRotation | [Vector3](../math/vector.md#vector3) |  | The overriding rotation transformation. |
| transformScale | [Vector3](../math/vector.md#vector3) |  | The overriding scale transformation. |

> **Ejemplo**
> ```lua
> function locAddedFunc(locAddedEvent)
>     log("Location " .. locAddedEvent.config.configName .. " has been added to " .. tostring(locAddedEvent.coordGrid) .. "!")
> end
> Event.LocAdded.Subscribe("myEvent", locAddedFunc)
> ```

### LocRemoved

Called when a location is removed from the game world by the server.
No `config` is provided with this event, and only existing locations with a matching `shapeType` and `coordGrid` will be removed.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| shapeType | [LocShapeType](../game/config/loctype.md#locshapetype) |  | The [LocShapeType](../game/config/loctype.md#locshapetype) of the location being removed. |
| rotationType | [RotationType](../game/entity/locentity.md#rotationtype) |  | The 90-degree rotation type of the location being removed. |
| coordGrid | [CoordGrid](../game/coordgrid.md) |  | The coordinate the location is being removed from. |

> **Ejemplo**
> ```lua
> function locRemovedFunc(locRemovedEvent)
>     log("A location has been removed from " .. tostring(locRemovedEvent.coordGrid) .. "!")
> end
> Event.LocRemoved.Subscribe("myEvent", locRemovedFunc)
> ```

### LocCustomised

Called when an existing location has an appearance customisation applied to it by the server.
This event retains any existing custom transformation the location already has.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| config | [LocType](../game/config/loctype.md) |  | The location config. |
| shapeType | [LocShapeType](../game/config/loctype.md#locshapetype) |  | The [LocShapeType](../game/config/loctype.md#locshapetype) of the location being removed. |
| rotationType | [RotationType](../game/entity/locentity.md#rotationtype) |  | The 90-degree rotation type of the location being removed. |
| coordGrid | [CoordGrid](../game/coordgrid.md) |  | The coordinate the location is being removed from. |
| customModels | [ Integer ] |  | A list of model IDs to overwrite the base [LocType](../game/config/loctype.md) model IDs.Use `id.Model.FromID(id)` to see the overriding material. |
| customColours | [ Integer ] |  | A list of 16-bit HSL colours to overwrite the base [LocType](../game/config/loctype.md) HSL colours. |
| customMaterials | [ Integer ] |  | A list of material IDs to overwrite the base [LocType](../game/config/loctype.md) material IDs.Use `id.Material.FromID(id)` to see the overriding material. |

> **Ejemplo**
> ```lua
> function locRemovedFunc(locRemovedEvent)
>     log("A location has been removed from " .. tostring(locRemovedEvent.coordGrid) .. "!")
> end
> Event.LocRemoved.Subscribe("myEvent", locRemovedFunc)
> ```

### LocAnimation

Called when an animation [SeqType](../game/config/seqtype.md) is started on a location by the server.
No `config` is provided with this event, and only existing locations with a matching `shapeType` and `coordGrid` will be animated.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| shapeType | [LocShapeType](../game/config/loctype.md#locshapetype) |  | The [LocShapeType](../game/config/loctype.md#locshapetype) of the location being animated. |
| rotationType | [RotationType](../game/entity/locentity.md#rotationtype) |  | The 90-degree rotation type of the location being animated. |
| coordGrid | [CoordGrid](../game/coordgrid.md) |  | The coordinate the location being animated. |
| animation | [SeqType](../game/config/seqtype.md) |  | The animation to be played.Will be `nil` if an existing animation is being stopped by this event. |
| animationDelay | Integer |  | How many client logic ticks to wait before starting the animation.There are `50` logic ticks per second. |

> **Ejemplo**
> ```lua
> function locAnimationFunc(locAnimationEvent)
>     log("A location is now playing animation " .. tostring(locAnimationEvent.animation))
> end
> Event.LocRemoved.Subscribe("myEvent", locAnimationFunc)
> ```

### InventoryAdded

Called after an inventory and its contents have been populated by the server.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| inv | [InvTypeProxy](../game/config/invtype.md) |  | Config of the inventory added. |

> **Ejemplo**
> ```lua
> function onInventoryAdded(inventoryAddedEvent)
>     local addedInvID = inventoryAddedEvent.inv
>     -- Do something with the added inventory config
> end
> Event.InventoryAdded.Subscribe("myEvent", onInventoryAdded)
> ```

### InventoryUpdated

Called when an inventory and its contents have been updated by the server.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| inv | [InvTypeProxy](../game/config/invtype.md) |  | Config of the inventory updated. |
| slotsUpdated | [Integer] |  | List of slot ids that have been updated. |

> **Ejemplo**
> ```lua
> function onInventoryUpdated(inventoryUpdatedEvent)
>     local updatedInvID = inventoryUpdatedEvent.inv
>     -- Do something with the updated inventory config
>     for i,slot in ipairs(inventoryUpdatedEvent.slotsUpdated) do
>         -- Do something with the updated slots
>     end
> end
> Event.InventoryUpdated.Subscribe("myEvent", onInventoryUpdated)
> ```

### InventoryRemoved

Called when the server stops transmitting the inventory and its contents to the client, signalling its removal.After being removed, the inventory and its contents are no longer available to the client or the API.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| inv | [InvTypeProxy](../game/config/invtype.md) |  | Config of the inventory removed. |

> **Ejemplo**
> ```lua
> function onInventoryRemoved(inventoryRemovedEvent)
>     local removedInvID = inventoryRemovedEvent.inv
>     -- Do something with the removed inventory ID
> end
> Event.InventoryRemoved.Subscribe("myEvent", onInventoryRemoved)
> ```

### GrandExchangeOfferUpdated

Called when one of a player character's Grand Exchange trade offers receives an update from the server.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| slot | Integer |  | Number of the offer slot that has been updated. 1-indexed. |
| listing | [GrandExchangeOffer](../game/grandexchange.md#grandexchangeoffer) |  | The offer data. |

> **Ejemplo**
> ```lua
> function onGEOfferUpdated(slotUpdatedEvent)
>     local slot = slotUpdatedEvent.slot
>     -- Do something with the slot ID where applicable
> end
> Event.GrandExchangeOfferUpdated.Subscribe("myEvent", onGEOfferUpdated)
> ```

### WorldCreated

Called when a Player Character is moved to a new world area.

> **Información**
> A world area is a static part of the game world shared by all Player Characters.

Provides the minimum and maximum range of map squares that make up the current world area.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| mapSquareMinX | Integer |  | The minimum map square on the X axis. |
| mapSquareMinZ | Integer |  | The minimum map square on the Z axis. |
| mapSquareMaxX | Integer |  | The maximum map square on the X axis. |
| mapSquareMaxZ | Integer |  | The maximum map square on the Z axis. |

> **Ejemplo**
> ```lua
> function onWorldCreated(worldCreatedEvent)
>     local worldAreaWidth = worldCreatedEvent.mapSquareMaxX - worldCreatedEvent.mapSquareMinX + 1
>     local worldAreaLength = worldCreatedEvent.mapSquareMaxZ - worldCreatedEvent.mapSquareMinZ + 1
> end
> Event.WorldCreated.Subscribe("myEvent", onWorldCreated)
> ```

### WorldUpdated

Called when the current world area is updated, typically caused by player movement.

> **Información**
> This event has no payload

> **Ejemplo**
> ```lua
> function onWorldUpdated()
>     -- No payload
>     -- Act on world build changes
> end
> Event.WorldUpdated.Subscribe("myEvent", onWorldUpdated)
> ```

### RegionCreated

Called when a Player Character is moved to a new region.

> **Información**
> A region is a duplicated area outside of the main game world, typically to allow players to experience content alone or within a group.
> A `Region` is often known in game-terms as an `Instance`.
The term `region` is used to clearly differentiate this concept from other uses of `instance` in the API.

Provides the minimum and maximum range of map squares that make up the current region, as well as the bottom-left [CoordGrid](../game/coordgrid.md) tile, and region dimensions in grid units.

The region dimensions may not fully fill the map squares that make up the region, e.g. a 1x1 map square region may contain a region of 64x48 tiles.

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| mapSquareMinX | Integer |  | The minimum map square on the X axis. |
| mapSquareMinZ | Integer |  | The minimum map square on the Z axis. |
| mapSquareMaxX | Integer |  | The maximum map square on the X axis. |
| mapSquareMaxZ | Integer |  | The maximum map square on the Z axis. |
| regionGridCorner | [CoordGrid](../game/coordgrid.md) |  | The bottom-left coordinate of the region. |
| regionGridWidth | Integer |  | The width of the region in grid units. |
| regionGridLength | Integer |  | The length of the region in grid units. |

> **Ejemplo**
> ```lua
> function onRegionCreated(regionCreatedEvent)
>     --
> end
> Event.RegionCreated.Subscribe("myEvent", onRegionCreated)
> ```

### RegionUpdated

Called when the current region is updated, typically caused by the server adding new zones, e.g. when opening a Dungeoneering door.

> **Información**
> This event has no payload

> **Ejemplo**
> ```lua
> function onRegionUpdated()
>     -- No payload
>     -- Act on region build changes
> end
> Event.RegionUpdated.Subscribe("myEvent", onRegionUpdated)
> ```

### SettingsLayerReady

Called when the settings layer is presented for a given plugin.

> **Información**
> The settings layer is shown after selecting a `Settings Icon` in the `Manage` tab of the `Plugin Hub`.

Plugin developers are expected to populate this layer with UI elements for settings appropriate to their plugin.
The layer is cleared of pre-existing elements immediately before this event is called.

The `Settings Icon` is disabled by default, and can be enabled by adding the following to the plugin manifest:

```text
"hasSettingsIcon" : true
```

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| component | [Component](../ui/component.md) |  | An empty layer to be populated by UI elements. |

> **Ejemplo**
> ```lua
> function onSettingsLayerReady(settingsLayerReadyEvent)
>     local rootLayer = settingsLayerReadyEvent.component
>     -- Populate the root layer with settings
> end
> Event.SettingsLayerReady.Subscribe("myEvent", onSettingsLayerReady)
> ```

### ContentLayerReady

Called when the content layer is presented for a given plugin.

> **Información**
> The content layer is shown after selecting a `Ribbon Icon` in the `Plugins` floating UI window.

Plugin developers are expected to populate this layer with UI elements for content appropriate to their plugin.
The layer is cleared of pre-existing elements immediately before this event is called.

The `Ribbon Icon` is disabled by default, and can be enabled by adding the following to the plugin manifest:

```text
"hasRibbonIcon" : true
```

| Payload variable | Type | Writeable | Description |
| --- | --- | --- | --- |
| component | [Component](../ui/component.md) |  | An empty layer to be populated by UI elements. |

> **Ejemplo**
> ```lua
> function onContentLayerReady(contentLayerReadyEvent)
>     local rootLayer = contentLayerReadyEvent.component
>     -- Populate the root layer with settings
> end
> Event.ContentLayerReady.Subscribe("myEvent", onContentLayerReady)
> ```