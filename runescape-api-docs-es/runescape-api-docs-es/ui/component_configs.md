# Component Configs

## Descripción General

The types listed here represent optional configuration data available to components.

## Tipos

### ui.OpNameFilter

Helper type containing information used to filter what ops should be available on a component.

#### Métodos

##### Constructor

```lua
function ui.OpNameFilter.new() -> ui.OpNameFilter
function ui.OpNameFilter.new(filterString : String, exactMatch : Bool, invertFilter : Bool) -> ui.OpNameFilter
```

Creates a new op name filter object.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| filterString | String | Filtering string to compare against op names. |
| exactMatch | Bool | Whether the filter string must be an exact match to the op name, otherwise the filter string is a substring. |
| invertFilter | Bool | Inverts the filter results, ie. op names that don't match the filter string return true. |

| Retorna | Descripción |
| --- | --- |
| ui.OpNameFilter | The newly created filter, default initialized, or setup with the provided filter string and options. |

##### Test

```lua
function ui.OpNameFilter:Test(testString : String) -> Bool
```

Checks if the provided string passes this filter.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| testString | String | String to test this filter against. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the provided string would pass this filter, false otherwise. |

#### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| filterString | String | Filtering string to compare against op names. |
| exactMatch | Bool | Whether the filter string must be an exact match to the op name, otherwise the filter string is a substring. |
| invertFilter | Bool | Inverts the filter results, ie. op names that don't match the filter string return true. |

### ui.ComponentOpConfig

Config type containing the ingame actions available for the player to perform when interacting with this config's UI component.

Supports filtering ops based on their ID and/or name, as well as marking visible ops as high priority based on their ID and/or name.

#### Métodos

##### GetOpName

```lua
function ui.ComponentOpConfig:GetOpName(opIndex : Int) -> String
```

Retrieves El nombre de op at the specified index.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Int | Index of the op that will be accessed. |

| Retorna | Descripción |
| --- | --- |
| String | El nombre de specified op, or an empty string if missing. |

##### ClearOpNames

```lua
function ui.ComponentOpConfig:ClearOpNames()
```

Resets the names of all previously defined ops.

> **Advertencia**
> This doesn't affect cursors for the ops, those must be cleared using [ClearOpCursors](#clearopcursors).

##### GetOpCursor

```lua
function ui.ComponentOpConfig:GetOpCursor(opIndex : Int) -> Int
```

Retrieves the cursor ID of the op at the specified index.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Int | Index of the op that will be accessed. |

| Retorna | Descripción |
| --- | --- |
| Int | The cursor ID of the specified op, or `-1` if missing. |

##### SetOpCursor

```lua
function ui.ComponentOpConfig:SetOpCursor(opIndex : Int, cursorID : Int)
```

Sets the cursor ID of the op at the specified index.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Int | Index of the op that will be accessed. |
| cursorID | Int | ID of the cursor to use for this op. |

##### ClearOpCursors

```lua
function ui.ComponentOpConfig:ClearOpCursors()
```

Resets the cursors of all previously defined ops.

> **Advertencia**
> This doesn't affect names for the ops, those must be cleared using [ClearOpNames](#clearopnames).

##### HasHiddenTests

```lua
function ui.ComponentOpConfig:HasHiddenTests() -> Bool
```

Checks whether or not [SetOpIDHidden](#setopidhidden) or [SetOpNameHidden](#setopnamehidden) have been called previously, resulting in active filters for visible ops.

| Retorna | Descripción |
| --- | --- |
| Bool | True if there are any active visible op filters, false otherwise. |

##### TestOpIsHidden

```lua
function ui.ComponentOpConfig:TestOpIsHidden(opIndex : Int) -> Bool
```

Tests whether the op at the specified index is hidden or not.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Int | Index of the op that will be accessed. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if this op exists and is hidden, false otherwise. |

##### ClearHiddenOps

```lua
function ui.ComponentOpConfig:ClearHiddenOps()
```

Resets both the op name hidden filters and op ID hidden by default settings.

##### SetOpIDHidden

```lua
function ui.ComponentOpConfig:SetOpIDHidden(opIndex : Int, hidden : Bool)
```

Controls whether the op at the specified index is hidden or not by default.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Int | Index of the op that will be accessed. |
| hidden | Bool | Whether this op should be hidden by default or not. |

##### GetOpIDHidden

```lua
function ui.ComponentOpConfig:GetOpIDHidden(opIndex : Int) -> Bool
```

Retrieves whether the op at the specified index is hidden or not by default.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Int | Index of the op that will be accessed. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if this op exists and is hidden by default, false otherwise. |

##### SetOpNameHidden

```lua
function ui.ComponentOpConfig:SetOpNameHidden(filter : ui.OpNameFilter)
```

Sets the filter used to determine if an op is hidden or not based on its name.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| filter | [ui.OpNameFilter](#uiopnamefilter) | Filter used to determine whether an op should be hidden or not based on its name. |

##### GetOpNameHidden

```lua
function ui.ComponentOpConfig:GetOpNameHidden() -> ui.OpNameFilter
```

Gets the filter used to determine if an op is hidden or not based on its name.

| Retorna | Descripción |
| --- | --- |
| [ui.OpNameFilter](#uiopnamefilter) | Currently active filter used to determine whether an op should be hidden or not based on its name.   If not set previously, this will represent an always-pass filter. |

##### HasHighPriorityTests

```lua
function ui.ComponentOpConfig:HasHighPriorityTests() -> Bool
```

Checks whether or not [SetOpIDHighPriority](#setopidhighpriority) or [SetOpNameHighPriority](#setopnamehighpriority) have been called previously, resulting in active filters for high priority ops.

| Retorna | Descripción |
| --- | --- |
| Bool | True if there are any active high priority op filters, false otherwise. |

##### TestOpIsHighPriority

```lua
function ui.ComponentOpConfig:TestOpIsHighPriority(opIndex : Int) -> Bool
```

Tests whether the op at the specified index is shown higher on the op list or not.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Int | Index of the op that will be accessed. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if this op exists and is shown higher on the op list, false otherwise. |

##### ClearHighPriorityOps

```lua
function ui.ComponentOpConfig:ClearHighPriorityOps()
```

Resets both the op name high priority filters and op ID high priority by default settings.

##### SetOpIDHighPriority

```lua
function ui.ComponentOpConfig:SetOpIDHighPriority(opIndex : Int, highPriority : Bool)
```

Controls whether the op at the specified index is shown higher on the op list or not by default.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Int | Index of the op that will be accessed. |
| highPriority | Bool | Whether this op should be shown higher on the op list by default or not. |

##### GetOpIDHighPriority

```lua
function ui.ComponentOpConfig:GetOpIDHighPriority(opIndex : Int) -> Bool
```

Retrieves whether the op at the specified index is shown higher on the op list or not by default.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| opIndex | Int | Index of the op that will be accessed. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if this op exists and is shown higher on the op list by default, false otherwise. |

##### SetOpNameHighPriority

```lua
function ui.ComponentOpConfig:SetOpNameHighPriority(filter : ui.OpNameFilter)
```

Sets the filter used to determine if an op should be shown higher on the op list or not based on its name.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| filter | [ui.OpNameFilter](#uiopnamefilter) | Filter used to determine whether an op should be shown higher on the op list or not based on its name. |

##### GetOpNameHighPriority

```lua
function ui.ComponentOpConfig:GetOpNameHighPriority() -> ui.OpNameFilter
```

Gets the filter used to determine if an op should be shown higher on the op list or not based on its name.

| Retorna | Descripción |
| --- | --- |
| [ui.OpNameFilter](#uiopnamefilter) | Currently active filter used to determine whether an op should be shown higher on the op list or not based on its name.   If not set previously, this will represent an always-fail filter. |

#### Propiedades

| Property | Tipo | Descripción |
| --- | --- | --- |
| pauseText | String | Text to display for this component when an interface pause is triggered by the server.   Only affects text and button components. |
| opWikiText | String | Text to display for this component's Wiki op entry in the right-click menu. |
| numOpNames | Uint | **(Read-only)**   Number of ops defined for this component. |
| numOpCursors | Uint | **(Read-only)**   Number of cursors defined for this component's ops. |
| opNames | `[String]` | **(Read-only)**   Names for the ops available for this component. |
| opBaseName | String | **(Read-only)**   Suffix used for ops for this component.   Commonly used to identify the target of an op. |
| opCursors | `[Int]` | **(Read-only)**   IDs for the cursors available for this component's ops. |
| targetOpVerb | String | **(Read-only)**   Prefix used for ops for this component when in target mode.   Commonly used to identify the action to perform with something. |
| targetOpCursor | Int | ID for the cursor to use when in target mode for this component. |

### ui.ComponentSwipeConfig

Configuration paremeters used for swipe gesture handling on components.

#### Métodos

##### SetDeadZone

```lua
function ui.ComponentSwipeConfig:SetDeadZone(horizontal : Uint8, vertical : Uint8)
```

Sets the minimum travel distance for horizontal and vertical inputs before being treated as a swipe gesture.

#### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| directionMask | Uint8 | Combination of [ui.SwipeDirectionBit](#uiswipedirectionbit), determines the direction used to detect swipe gestures. |
| deadZoneHorizontal | Uint8 | Minimum horizontal travel distance before an input is treated as a swipe gesture. |
| deadZoneVertical | Uint8 | Minimum vertical travel distance before an input is treated as a swipe gesture. |
| deceleration | Uint8 | Determines how far a swipe gesture drifts based on previous motion.   Ranges from `1` to `100`, representing `1%`-`100%` deceleration.   A value of `100` results in no swipe drift being applied. |
| stopExponent | Uint8 | Exponent applied to the threshold value at which we stop drifting.   A value of `1` indicates drifting stops at drift speeds below `0.1`, while `2` results in stopping below `0.01`.   Should generally be left at the default value of `8` for consistency. |

### ui.ComponentDragConfig

Configuration parameters used for drag gestures handling on components.

| Property | Tipo | Descripción |
| --- | --- | --- |
| draggedComponent | Component | The component that's being actively dragged. |
| renderBehaviour | [DragRenderBehaviour](#uidragrenderbehaviour) | Indicates how the component should be rendered while it's being dragged. |
| dragDelayTicks | Uint8 | How long the user must be attempting a drag action for on a component in logic ticks, before the action actually starts. |
| deadZone | Uint8 | Minimum distance in interface units before a drag gesture is triggered, assuming `dragDelayTicks` has been exceeded. |

### ui.ComponentPinchConfig

Configuration parameters used for pinch gestures handling on components.

| Property | Tipo | Descripción |
| --- | --- | --- |
| directionMask | Uint8 | Combination of [ui.SwipeDirectionBit](#uiswipedirectionbit), determines the direction used to detect pinch gestures. |
| threshold | Uint8 | Minimum distance in interface units before a pinch gesture is triggered. |

### ui.ComponentCursorConfig

Configuration parameters used for cursors associated with this component.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| mouseOverCursor | Int | The ID of the cursor to display when the mouse is over this component.   A value of `-1` indicates no cursor is set. |
| targetValidCursor | Int | The ID of the cursor to display when in target mode for this component and the cursor is over a valid target.   A value of `-1` indicates no cursor is |
| targetInvalidCursor | Int | The ID of the cursor to display when in target mode for this component and the cursor is over an invalid target.   A value of `-1` indicates no cursor is |

### ui.ComponentParamsConfig

Contains arbitrary parameter data associated with the component.

> **Advertencia**
> This config type is meant for interop with the game's legacy scripting system and should generally be avoided as it may be removed in the future.

#### Métodos

##### Get

```lua
function ui.ComponentParamsConfig:Get(paramID : Int) -> Int? | String?
```

Retrieves the value for the parameter associated with the provided ID.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| paramID | Int | Numeric ID associated with the parameter to retrieve. |

| Retorna | Descripción |
| --- | --- |
| Int? | String? |

##### CheckExists

```lua
function ui.ComponentParamsConfig:CheckExists(paramID : Int) -> Bool
```

Checks if there's a parameter associated with the provided ID.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| paramID | Int | Numeric ID associated with the parameter to check. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if a parameter with the specified ID exists, false otherwise. |

#### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| valid | Bool | **(Read-only)**   True if there are any parameters set on this component. |

## Enumeraciones

### ui.DragRenderBehaviour

Enumeration identifying how a component that is actively being dragged by the user should be rendered.

| Valor | Descripción |
| --- | --- |
| TRANSPARENT_OVERLAY | The dragged component will be rendered as semi-translucent and over other components. |
| OPAQUE | The dragged component will be drawn as normal. |
| OPAQUE_OVERLAY | The dragged component will be drawn as normal and over other components. |
| INVISIBLE | The dragged component won't be drawn. |

### ui.PlayerOpType

Identifies the type of player that's been associated with a component.

| Valor | Descripción |
| --- | --- |
| NONE | No player is currently associated with this component. |
| FRIEND | A player in the local player's friend list is currently associated with this component. |
| GROUP_MEMBER | A player in the local player's group list is currently associated with this component. |
| GROUP_BANNED | A player in the local player's group ban list is currently associated with this component. |
| CLAN_MEMBER | A player in the local player's clan is currently associated with this component. |
| CLAN_GUEST | A guest player in the local player's clan is currently associated with this component. |
| FRIEND_CHAT | A player in the local player's friend chat is currently associated with this component. |

### ui.PinchAxisBit

Bitmasks for the available pinch axii, can be added together to combine them.

| Valor | Descripción |
| --- | --- |
| HORIZONTAL | Allows horizontal pinch gestures. |
| VERTICAL | Allows vertical pinch gestures. |

### ui.SwipeDirectionBit

Bitmasks for the available swipe directions, can be added together to combine them.

| Valor | Descripción |
| --- | --- |
| LEFT | Allows swipe left gestures. |
| RIGHT | Allows swipe right gestures. |
| UP | Allows swipe up gestures. |
| DOWN | Allows swipe down gestures. |