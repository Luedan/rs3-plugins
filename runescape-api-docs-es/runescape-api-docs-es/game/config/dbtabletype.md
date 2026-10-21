# DBTableType

## Descripción General

A `DBTableType` config describes a table structure which [DBRow](dbrowtype.md) configs use to store values.

A DBTable has a number of columns, each of which is assigned one or more [ValueTypes](vartype.md#valuetype), for example:

```text
Column 1 = [ ValueType.INTEGER ]                -- A column with one value
    Column 2 = [ ValueType.NPC, ValueType.STRING ]  -- A column with two values
    Column 3 = [ ]                                  -- A server-only column with no values
```

Each column can also optionally provide a default value, such as:

```text
Column 1 = [ -1 ]                               -- A column with one default value
    Column 2 = [ nil, "Nothing" ]                   -- A column also with one default value
    Column 3 = [ ]                                  -- A server-only column with no default values
```

These config types can be found within the `config.DBTable` table:

```lua
config.DBTable.INVENT_PERK_TABLE
config.DBTable["INVENT_PERK_TABLE"]
config.DBTable.FromID(8) -- config.DBTable.INVENT_PERK_TABLE
```

> **Información**
> An `DBTableType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

## Ejemplos

```lua
-- Access a DBTable config directly by using its name
local dbTableCfg = config.DBTable.INVENT_PERK_TABLE
-- or by ID lookup
local dbTableCfg = config.DBTable.FromID(id.DBTable.INVENT_PERK_TABLE)
```

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Métodos

### GetColumnValueCount

```lua
function DBTable:GetColumnValueCount(columnIndex : Integer) -> Integer
```

Returns the number of values in the given column.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| columnIndex | Integer | The column index to check.Column index values are 1-indexed. |

| Retorna | Descripción |
| --- | --- |
| Integer | How many values are available for the given column index. |

> **Ejemplo**
> ```lua
> -- Get how many values the second column has
> local valueCount = config.DBTable.INVENT_PERK_TABLE:GetColumnValueCount(2)
> ```

### GetColumnValueTypes

```lua
function DBTable:GetColumnValueTypes(columnIndex : Integer) -> [ ValueType ]
```

Returns all [ValueTypes](vartype.md#valuetype) for each value in the given column.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| columnIndex | Integer | The column index to check.Column index values are 1-indexed. |

| Retorna | Descripción |
| --- | --- |
| [ [ValueType](vartype.md#valuetype) ] | An array containing a [ValueType](vartype.md#valuetype) for each value in the given column index. |

> **Ejemplo**
> ```lua
> -- Get all value types in the target column
> 
> -- [ ValueType.STRING ]
> local valueTypesCol2 = config.DBTable.INVENT_PERK_TABLE:GetColumnValueTypes(2)
> 
> -- [ ValueType.INTEGER, ValueType.INTEGER, ValueType.INTEGER, ValueType.INTEGER ]
> local valueTypesCol8 = config.DBTable.INVENT_PERK_TABLE:GetColumnValueTypes(8)
> ```

### GetColumnHasDefaultValues

```lua
function DBTable:GetColumnHasDefaultValues(columnIndex : Integer) -> Boolean
```

Returns whether a given column in the table has any default values.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| columnIndex | Integer | The column index to check.Column index values are 1-indexed. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the given column index can provide default values. |

> **Ejemplo**
> ```lua
> -- Check if the second column has any default values
> local hasDefaults = config.DBTable.INVENT_PERK_TABLE:GetColumnHasDefaultValues(2)
> ```

### GetColumnDefaultValues

```lua
function DBTable:GetColumnDefaultValues(columnIndex : Integer) -> [ ? ]
```

Returns all default values in the given column.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| columnIndex | Integer | The column index to check.Column index values are 1-indexed. |

| Retorna | Descripción |
| --- | --- |
| [ ? ] | An array containing each default value in the given column index.This array may be empty, or contain `nil` values.Use [GetColumnValueTypes](#getcolumnvaluetypes) to determine the types of the values returned by this method. |

> **Ejemplo**
> ```lua
> -- Get all default values in the target column
> 
> -- [ ]
> local defaultValuesCol2 = config.DBTable.INVENT_PERK_TABLE:GetColumnDefaultValues(2)
> 
> -- [ false ]
> local defaultValuesCol9 = config.DBTable.INVENT_PERK_TABLE:GetColumnDefaultValues(9)
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"INVENT_PERK_TABLE"`. |
| typeName | String | The type of this config. Will always be `"DBTable"`. |
| columnCount | Integer | The total number columns in this table. |