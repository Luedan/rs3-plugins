# PersistentDB

## Descripción General

The persistent DB system provides a way for plugins to store runtime data and preserve it across game sessions, making it ideal for storing user-facing plugin settings.

Records are isolated per plugin, preventing plugins from accessing or modifying eachother's data.

## Ejemplos

```lua
-- On plugin shutdown
PersistentDB:Set("meowEnabled", true)
PersistentDB:Set("meowName", "George")
PersistentDB:Set("meowLoudness", 4.3)
PersistentDB:Set("meowProperties", { colour = "orange", speed = 1000 })
-- Or
PersistentDB:SetBool("meowEnabled", true)
PersistentDB:SetString("meowName", "George")
PersistentDB:SetFloat("meowLoudness", 4.3)
PersistentDB:SetStructuredData("meowProperties", { colour = "orange", speed = 1000 })
```

```lua
-- On plugin startup
local enabled = PersistentDB:Get("meowEnabled")
local name = PersistentDB:Get("meowName")
local loudnesss = PersistentDB:Get("meowLoudness")
local properties = PersistentDB:Get("meowProperties")
-- Or
local enabled = PersistentDB:GetBool("meowEnabled")
local name = PersistentDB:GetString("meowName")
local loudnesss = PersistentDB:GetFloat("meowLoudness")
local properties = PersistentDB:GetStructuredData("meowProperties")
```

## Enumeraciones

### PersistentDBType

Enumeration representing the type of the an entry in the persistent DB.

| Name | Valor | Descripción |
| --- | --- | --- |
| BOOL | 0 | True/false entry |
| INT | 1 | Integer entry |
| FLOAT | 2 | Floating point entry |
| STRING | 3 | Text-based entry |
| STRUCTURED_DATA | 4 | Entry that gets serialized directly to/from Lua tables |

## Funciones

### Get

```lua
function PersistentDB:Get(key : String) -> Bool/Int/Float/String/Table?
```

Retrieves the entry associated with the provided key and the current plugin from the persistent DB, returning its value.

> **Explicit Data Types**
> You can explicitly request data of a certain type by using the following aliases:
> ```lua
> function PersistentDB:GetBool(key : String) -> Bool?
> function PersistentDB:GetInt(key : String) -> Int?
> function PersistentDB:GetFloat(key : String) -> Float?
> function PersistentDB:GetString(key : String) -> String?
> function PersistentDB:GetStructuredData(key : String) -> Table?
> ```
> These function the same as the general `Get` function, however they also check the data type, returning nil if there's a type mismatch.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| key | String | The name associated with a persistent DB entry. |

| Retorna | Descripción |
| --- | --- |
| Bool/Int/Float/String/Table? | Value associated with the entry matching the provided key, or nil if there is no such entry.    The returned type matches the type originally used when storing that entry. |

### Set

```lua
function PersistentDB:Set(key : String, value : Bool/Int/Float/String/Table) -> Bool
```

Stores the provided value in the persistent DB, associating it with the specified key and the current plugin.

> **Explicit Data Types**
> You can explicitly set data of a certain type by using the following aliases:
> ```lua
> function PersistentDB:SetBool(key : String, value : Bool) -> Bool
> function PersistentDB:SetInt(key : String, value : Int) -> Bool
> function PersistentDB:SetFloat(key : String, value : Float) -> Bool
> function PersistentDB:SetString(key : String, value : String) -> Bool
> function PersistentDB:SetStructuredData(key : String, value : Table) -> Bool
> ```
> These function the same as the general `Get` function, however they also check the data type, returning nil if there's a type mismatch.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| key | String | The name associated with a persistent DB entry. |

| Retorna | Descripción |
| --- | --- |
| Bool/Int/Float/String/Table? | Value associated with the entry matching the provided key, or nil if there is no such entry.    The returned type matches the type originally used when storing that entry.      Note when using tables, fields with types other than the ones allowed by this function will be ignored. |

### CheckExists

```lua
function PersistentDB:CheckExists(key : String) -> Bool
```

Checks if an entry exists in the persistent DB with the specified key for the current plugin.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| key | String | The name associated with a persistent DB entry. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if an entry with the provided key exists, false otherwise. |

### CheckExistsTyped

```lua
function PersistentDB:CheckExistsTyped(key : String, type : PersistentDBType) -> Bool
```

Checks if an entry exists in the persistent DB with the specified key and is of the specified type.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| key | String | The name associated with a persistent DB entry. |
| type | [PersistentDBType](#persistentdbtype) | The type we're expecting for this entry. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if an entry with the provided key exists with the provided type, false otherwise. |

### IterateEntries

```lua
function PersistentDB:IterateEntries(callback : function (key : String, value : Bool/Int/Float/String/Table) -> Bool) -> Int
```

Calls the provided callback once per persistent DB entry associated with this plugin.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| callback | function (key : String, value : Bool/Int/Float/String/Table) -> Bool | Function called once for each persistent DB entry for this plugin.    Iteration is stopped if it returns true, and continues otherwise. |

| Retorna | Descripción |
| --- | --- |
| Int | The number of entries iterated on |

> **Ejemplo**
> ```lua
> -- Print all persistent DB entries for this plugin
> local numEntries = PersistentDB:IterateEntries(
>     function (k, v)
>         print(k, "=", v)
>         return false -- Keep iterating
>     end)
> 
> print(numEntries, "entries found")
> ```

### Delete

```lua
function PersistentDB:Delete(key : String) -> Bool
```

Removes an entry associated with the current plugin and matching the provided key from the persistent DB.

> **Información**
> If you just want to replace an existing entry, use `Set` or one of its aliases instead, there's no need to delete an entry before updating it, even if the new data has a different type.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| key | String | The name associated with a persistent DB entry. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if this operation completed successfully, false otherwise. |

### Clear

```lua
function PersistentDB:Clear() -> Bool
```

Clears all persistent DB entries associated with this plugin.

> **Advertencia**
> You may want to prompt the user before deleting data in this manner.

| Retorna | Descripción |
| --- | --- |
| Bool | True if this operation completed successfully, false otherwise. |