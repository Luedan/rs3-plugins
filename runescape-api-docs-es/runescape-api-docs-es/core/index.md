# Core

## Descripción General

This module provides functionality core to the plugin system and the application itself.

## Funciones

### print

```lua
function print(args : ...)
```

Outputs a message containing the contents of the provided arguments separated by a space to the Lua console.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| args | ... | Values to format. |

> **Ejemplo**
> ```text
> print("hello", "world")                     -- hello world
> print(10, "+", 5, "=", 15)                  -- 10 + 5 = 15
> print({ hello = true, world = { 10, 50 }})  -- { hello = true, world = { 10, 50 } }
> ```

### log

```lua
function log(format : String, args : ...)
```

Outputs a plugin-associated message containing the contents of the provided arguments separated by a space to the Lua console.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| args | ... | Values to log. |

> **Ejemplo**
> ```text
> log("hello", "world")                     -- MyPlugin: hello world
> log(10, "+", 5, "=", 15)                  -- MyPlugin: 10 + 5 = 15
> log({ hello = true, world = { 10, 50 }})  -- MyPlugin: { hello = true, world = { 10, 50 } }
> ```

### ExecuteConsoleCommand

```lua
function ExecuteConsoleCommand(command : String)
```

Executes the provided string as a ingame console command.

> **Información**
> The list of available commands can be obtained by using the `help` command on the ingame console.

> **Advertencia**
> The console isn't available on mobile platforms.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| args | String | Contains the command to be executed and any arguments that it might require. |