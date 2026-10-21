# DBRowType

## Descripción General

A `DBRowType` config contains data that is partitioned into columns.

Each column is assigned one or more [ValueTypes](vartype.md#valuetype), for example:

```text
Column 1 = [ ValueType.INTEGER ]                -- A column with one value
    Column 2 = [ ValueType.NPC, ValueType.STRING ]  -- A column with two values
    Column 3 = [ ]                                  -- A server-only column with no values
```

A DBRow may not provide values for all columns.In this case, its parent [DBTable](dbtabletype.md) is referenced to provide any default values for those that are missing.

These config types can be found within the `config.DBRow` table:

```lua
config.DBRow.INVENT_PERK_LOOTING
config.DBRow["INVENT_PERK_LOOTING"]
config.DBRow.FromID(487) -- config.DBRow.INVENT_PERK_LOOTING
```

> **Información**
> An `DBRowType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

## Ejemplos

```lua
-- Access a DBRowType config directly by using its name
local dbRowCfg = config.DBRow.INVENT_PERK_LOOTING
-- or by ID lookup
local dbRowCfg = config.DBRow.FromID(id.DBRow.INVENT_PERK_LOOTING)
```

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Métodos

### GetColumnValueCount

```lua
function DBRow:GetColumnValueCount(columnIndex : Integer) -> Integer
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
> local valueCount = config.DBRow.INVENT_PERK_LOOTING:GetColumnValueCount(2)
> ```

### GetColumnValueTypes

```lua
function DBRow:GetColumnValueTypes(columnIndex : Integer) -> [ ValueType ]
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
> local valueTypesCol2 = config.DBRow.INVENT_PERK_LOOTING:GetColumnValueTypes(2)
> 
> -- [ ValueType.INTEGER, ValueType.INTEGER, ValueType.INTEGER, ValueType.INTEGER ]
> local valueTypesCol8 = config.DBRow.INVENT_PERK_LOOTING:GetColumnValueTypes(8)
> ```

### GetColumnValues

```lua
function DBRow:GetColumnValues(columnIndex : Integer) -> [ ? ]
```

Returns all values in the given column.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| columnIndex | Integer | The column index to check.Column index values are 1-indexed. |

| Retorna | Descripción |
| --- | --- |
| [ ? ] | An array containing each value in the given column index.This array may be empty, or contain `nil` values.Use [GetColumnValueTypes](#getcolumnvaluetypes) to determine the types of the values returned by this method. |

> **Ejemplo**
> ```lua
> -- Get all values in the target column
> 
> -- [ "Looting" ]
> local valuesCol2 = config.DBRow.INVENT_PERK_LOOTING:GetColumnValues(2)
> 
> -- [ false ]
> -- This value is not defined in the DBRow config and is returning the default value
> local valuesCol9 = config.DBRow.INVENT_PERK_LOOTING:GetColumnValues(9)
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"INVENT_PERK_LOOTING"`. |
| typeName | String | The type of this config. Will always be `"DBRow"`. |
| columnCount | Integer | The total number columns in this table. |
| ownerDBTable | [DBTable](dbtabletype.md) | The parent table config for this row config. |