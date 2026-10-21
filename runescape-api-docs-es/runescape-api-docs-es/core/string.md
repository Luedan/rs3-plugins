# String Utils

## Funciones

### formatStr

```lua
function formatStr(format : String, args : ...) -> String
```

Creates a string containing the provided arguments based on the specified format string.

> **Format String**
> Formatting a value is done by specifying `{}` as part of the format string, or `{<options>}` where `<options>` varies based on the type being formatted.
> Positional argument formatting can also be done via `{<argument number>}` where `{0}` represents the first argument, `{1}` the second and so on.

> **Advertencia**
> Only elementary types (numbers, strings, booleans, and nil) are supported.
> Other types, such as tables and functions, get formatted as the underlying type name where available.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| format | String | String representing the desired output format. |
| args | ... | Values to format. |

| Retorna | Descripción |
| --- | --- |
| String | Formatted output obtained based on the provided format string and arguments. |

> **Ejemplo**
> ```text
> local a = formatStr("hello {}", "world")                       -- hello world
> local b = formatStr("{1} is {0}? {2}", "Loud", "George", true) -- George is Loud? True
> local c = formatStr("{} + {} = {}", 10, 5, 15)                 -- 10 + 5 = 15
> ```