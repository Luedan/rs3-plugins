# Keyboard

## Descripción General

The Keyboard table contains functions which provide data belonging to the user's keyboard input.

This data includes:

* Keyboard availability (`false` on Mobile devices)
* Key pressed state

Keyboard information is also provided by:

* Events
[KeyUp](events.md#keyup)
[KeyDown](events.md#keydown)
[KeyTyped](events.md#keytyped)
* Hooks
[ONKEY](../ui/component.md#uihook)

> **Advertencia**
> Keyboard states, events and hooks are blocked when a [restricted component](../ui/component.md#restricted-components) is in focus, such as an [InputField](../ui/interactive_components/input_field.md) with hidden text.
Attempts to access key states via the Keyboard table when in a blocked state will return `false` for all states

## Key Codes

RuneScape has its own internal list of [game key codes](#gamekey) which it uses to trigger events.
These legacy key values differ from standard keyboard [system key codes](#systemkey).

Additionally, the available list of key codes is limited to keys which are guaranteed to exist across all desktop platforms.

A list of supported game keys, and their system key counterparts, is provided below.

## Ejemplos

```lua
if Keyboard.IsAvailable() and not Keyboard.IsBlocked() then
    -- Testing for a key combo
    local comboDown = Keyboard.IsShiftDown() and Keyboard.IsGameKeyDown(GameKey.P)
end
```

## Enumeraciones

### ModifierKey

Bitfield values for use in testing combined modifier values provided in key events:

* [KeyUp](events.md#keyup)
* [KeyDown](events.md#keydown)
* [KeyTyped](events.md#keytyped)

> **Advertencia**
> The `META` key is always excluded from the modifier list in the above events.

| Name | Value |
| --- | --- |
| SHIFT | 1 |
| CONTROL | 2 |
| ALT | 4 |
| META | 8 |
| ANY | 7 |
| ANY_INC_META | 15 |

### GameKey

| Name | Value |
| --- | --- |
| F1 | 1 |
| F2 | 2 |
| F3 | 3 |
| F4 | 4 |
| F5 | 5 |
| F6 | 6 |
| F7 | 7 |
| F8 | 8 |
| F9 | 9 |
| F10 | 10 |
| F11 | 11 |
| F12 | 12 |
| ESCAPE | 13 |
| _1 | 16 |
| _2 | 17 |
| _3 | 18 |
| _4 | 19 |
| _5 | 20 |
| _6 | 21 |
| _7 | 22 |
| _8 | 23 |
| _9 | 24 |
| _0 | 25 |
| MINUS | 26 |
| EQUALS | 27 |
| CONSOLE | 28 |
| Q | 32 |
| W | 33 |
| E | 34 |
| R | 35 |
| T | 36 |
| Y | 37 |
| U | 38 |
| I | 39 |
| O | 40 |
| P | 41 |
| LEFT_BRACKET | 42 |
| RIGHT_BRACKET | 43 |
| A | 48 |
| S | 49 |
| D | 50 |
| F | 51 |
| G | 52 |
| H | 53 |
| J | 54 |
| K | 55 |
| L | 56 |
| SEMICOLON | 57 |
| APOSTROPHE | 58 |
| HASH | 59 |
| Z | 64 |
| X | 65 |
| C | 66 |
| V | 67 |
| B | 68 |
| N | 69 |
| M | 70 |
| COMMA | 71 |
| FULLSTOP | 72 |
| SLASH | 73 |
| BACKSLASH | 74 |
| TAB | 80 |
| SHIFT | 81 |
| CONTROL | 82 |
| SPACE | 83 |
| ENTER | 84 |
| BACKSPACE | 85 |
| ALT | 86 |
| NUMPAD_ADD | 87 |
| NUMPAD_SUBTRACT | 88 |
| NUMPAD_MULTIPLY | 89 |
| NUMPAD_DIVIDE | 90 |
| CLEAR | 91 |
| LEFT | 96 |
| RIGHT | 97 |
| UP | 98 |
| DOWN | 99 |
| INSERT | 100 |
| DELETE | 101 |
| HOME | 102 |
| END | 103 |
| PAGE_UP | 104 |
| PAGE_DOWN | 105 |

### SystemKey

| Name | Value |
| --- | --- |
| BACKSPACE | 8 |
| TAB | 9 |
| CLEAR | 12 |
| RETURN | 13 |
| ENTER | 13 |
| SHIFT_LEFT | 16 |
| CONTROL_LEFT | 17 |
| ALT_LEFT | 18 |
| ESCAPE | 27 |
| SPACE | 32 |
| PAGE_UP | 33 |
| PAGE_DOWN | 34 |
| END | 35 |
| HOME | 36 |
| LEFT | 37 |
| UP | 38 |
| RIGHT | 39 |
| DOWN | 40 |
| INSERT | 45 |
| DELETE | 46 |
| _0 | 48 |
| _1 | 49 |
| _2 | 50 |
| _3 | 51 |
| _4 | 52 |
| _5 | 53 |
| _6 | 54 |
| _7 | 55 |
| _8 | 56 |
| _9 | 57 |
| A | 65 |
| B | 66 |
| C | 67 |
| D | 68 |
| E | 69 |
| F | 70 |
| G | 71 |
| H | 72 |
| I | 73 |
| J | 74 |
| K | 75 |
| L | 76 |
| M | 77 |
| N | 78 |
| O | 79 |
| P | 80 |
| Q | 81 |
| R | 82 |
| S | 83 |
| T | 84 |
| U | 85 |
| V | 86 |
| W | 87 |
| X | 88 |
| Y | 89 |
| Z | 90 |
| NUMPAD_MULTIPLY | 106 |
| NUMPAD_ADD | 107 |
| NUMPAD_SUBTRACT | 109 |
| NUMPAD_DECIMAL | 110 |
| NUMPAD_DIVIDE | 111 |
| F1 | 112 |
| F2 | 113 |
| F3 | 114 |
| F4 | 115 |
| F5 | 116 |
| F6 | 117 |
| F7 | 118 |
| F8 | 119 |
| F9 | 120 |
| F10 | 121 |
| F11 | 122 |
| F12 | 123 |
| SEMICOLON | 186 |
| EQUALS | 187 |
| COMMA | 188 |
| MINUS | 189 |
| FULLSTOP | 190 |
| SLASH | 191 |
| APOSTROPHE | 192 |
| LEFT_BRACKET | 219 |
| BACKSLASH | 220 |
| RIGHT_BRACKET | 221 |
| HASH | 222 |
| CONSOLE | 7331 |

## Funciones

### IsAvailable

```lua
function Keyboard.IsAvailable() -> Boolean
```

Returns whether keyboard data is available on the current platform.

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether keyboard data can be polled on the current platform.Returns `false` on Mobile devices, and `true` on all others. |

> **Ejemplo**
> ```lua
> if Keyboard.IsAvailable() then
>     local shiftDown = Keyboard.IsShiftDown()
> else
>     log("No keyboard data available")
> end
> ```

### IsBlocked

```lua
function Keyboard.IsBlocked() -> Boolean
```

Returns whether keyboard data is being blocked by the game for any reason.
This can occur when an [InputField](../ui/interactive_components/input_field.md) is set as restricted and is current in focus.

Any attempt to access key states while this method returns `true` will result in a return value of `false`.

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether accessing keyboard data is blocked at the current moment.Returns `true` when data is unavailable, and `false` when it is available. |

> **Ejemplo**
> ```lua
> if Keyboard.IsBlocked() then
>     -- Always returns false
>     local shiftDown = Keyboard.IsShiftDown()
>     local keyDown = Keyboard.IsGameKeyDown(GameKey.P)
>     -- Always returns an empty table
>     local allKeysDown = Keyboard.GetGameKeysDown()
> end
> ```

### IsShiftDown

```lua
function Keyboard.IsShiftDown() -> Boolean
```

Returns whether either shift key is currently down.

| Retorna | Descripción |
| --- | --- |
| Boolean | The current shift key down state.Returns `false` if keyboard data is [blocked](#isblocked). |

> **Ejemplo**
> ```lua
> local number = 0;
> if Keyboard.IsShiftDown() then
>     number = number + 5
> else
>     number = number + 1
> end
> ```

### IsControlDown

```lua
function Keyboard.IsControlDown() -> Boolean
```

Returns whether either control/ctrl key is currently down.

| Retorna | Descripción |
| --- | --- |
| Boolean | The current control key down state.Returns `false` if keyboard data is [blocked](#isblocked). |

> **Ejemplo**
> ```lua
> local number = 0;
> if Keyboard.IsControlDown() then
>     number = number + 5
> else
>     number = number + 1
> end
> ```

### IsAltDown

```lua
function Keyboard.IsAltDown() -> Boolean
```

Returns whether either alt key is currently down.

| Retorna | Descripción |
| --- | --- |
| Boolean | The current alt key down state.Returns `false` if keyboard data is [blocked](#isblocked). |

> **Información**
> In some cases, pressing the Alt-Gr key will trigger both an Alt and Control key event at the same time.

> **Ejemplo**
> ```lua
> local number = 0;
> if Keyboard.IsAltDown() then
>     number = number + 5
> else
>     number = number + 1
> end
> ```

### IsMetaDown

```lua
function Keyboard.IsMetaDown() -> Boolean
```

Returns whether either meta key is currently down.

The meta key for each platform is:

* Left Command or Right Command on Mac OSX
* Left Win or Right Win on Windows
* Left Meta or Right Meta on Linux

| Retorna | Descripción |
| --- | --- |
| Boolean | The current meta key down state.Returns `false` if keyboard data is [blocked](#isblocked). |

> **Ejemplo**
> ```lua
> local number = 0;
> if Keyboard.IsMetaDown() then
>     number = number + 5
> else
>     number = number + 1
> end
> ```

### IsGameKeyDown

```lua
function Keyboard.IsGameKeyDown(key : GameKey) -> Boolean
```

Returns whether the given [GameKey](#gamekey) `key` is currently down.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| key | GameKey | Integer enum value for the key being tested. |

| Retorna | Descripción |
| --- | --- |
| Boolean | The current key down state.Returns `false` if keyboard data is [blocked](#isblocked). |

> **Ejemplo**
> ```lua
> if Keyboard.IsGameKeyDown(GameKey.SPACE) then
>     log("Jump! Okay, maybe not")
> end
> ```

### GetGameKeysDown

```lua
function Keyboard.GetGameKeysDown() -> [ GameKey ]
```

Returns all currently pressed [GameKeys](#gamekey) in an array.

| Retorna | Descripción |
| --- | --- |
| [ [GameKey](#gamekey) ] | An array of [GameKeys](#gamekey). |

> **Ejemplo**
> ```lua
> local keysDown = Keyboard.GetGameKeysDown()
> for _,key in ipairs(keysDown) do
>     if key == GameKey.SHIFT then
>         log("Run!")
>     end
> end
> ```