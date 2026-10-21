# EnumType

## Descripción General

A `EnumType` config provides a key-value pair data structure.

Each enum has an input key [ValueType](vartype.md#valuetype) and an output value [ValueType](vartype.md#valuetype), alongside a fixed set of data values which can be accessed through a variety of methods.

These config types can be found within the `config.Enum` table:

```lua
config.Enum.CRAFTING_PLATINUM_TABLE
config.Enum["CRAFTING_PLATINUM_TABLE"]
config.Enum.FromID(0) -- config.Enum.CRAFTING_PLATINUM_TABLE
```

> **Información**
> An `EnumType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `EnumType` includes:

* Input and output [ValueTypes](vartype.md#valuetype)
* Key-value data pairs.

## Ejemplos

```lua
-- Access an EnumType config directly by using its name
local enumCfg = config.Enum.CRAFTING_PLATINUM_TABLE
-- or by ID lookup
local enumCfg = config.Enum.FromID(id.Enum.CRAFTING_PLATINUM_TABLE)

local inputValueType = config.Enum.CRAFTING_PLATINUM_TABLE.inputValueType -- ValueType.INTEGER
local outputValueType = config.Enum.CRAFTING_PLATINUM_TABLE.outputValueType -- ValueType.OBJ

-- Look for an object using the input key of 2
local obj = config.Enum.CRAFTING_PLATINUM_TABLE:GetOutputValue(2) -- config.Obj.PLATINUM_BRACELET

-- Iterate all data values
-- Values data is returned as an array of pairs, i.e. [ [inputValue, outputValue], [inputValue, outputValue], ... ]
local allValues = config.Enum.CRAFTING_PLATINUM_TABLE.values
for _,keyValuePair in ipairs(allValues) do
    local inputValue = keyValuePair[1] -- 2
    local outputValue = keyValuePair[2] -- config.Obj.PLATINUM_BRACELET
end
```

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Métodos

### GetOutputValue

```lua
function Enum:GetOutputValue(inputValue : ?) -> ?
```

Returns the corresponding output value for the given input value.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| inputValue | ? | The input data value.Data value type must match the [ValueType](vartype.md#valuetype) of property `inputValueType`. |

| Retorna | Descripción |
| --- | --- |
| ? | The corresponding output value.Returns `nil` if the input value is not found in the data structure. |

> **Ejemplo**
> ```lua
> -- Get the teleport animation for an urn
> local seq = config.Enum.URNS_TELE_ANIM:GetOutputValue(config.Obj.URNS_FISHING6_FULL)
> ```

### HasOutputValue

```lua
function Enum:HasOutputValue(outputValue : ?) -> Boolean
```

Returns the whether the given output value can be returned from this enum.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| outputValue | ? | The output data value.Data value type must match the [ValueType](vartype.md#valuetype) of property `outputValueType`. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Returns whether the given value was found in the list of potential output values. |

> **Ejemplo**
> ```lua
> -- Check whether a platinum anklet can be the output of this enum
> local exists = config.Enum.CRAFTING_PLATINUM_TABLE:HasOutputValue(config.Obj.PLATINUM_ANKLET)
> ```

### GetInputValues

```lua
function Enum:GetInputValues(outputValue : ?) -> [ ? ]
```

Returns all input values that will return the given output value from this enum.

In some enums, multiple input values can return the same output value.Use this method to gather those possible input values.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| outputValue | ? | The output data value.Data value type must match the [ValueType](vartype.md#valuetype) of property `outputValueType`. |

| Retorna | Descripción |
| --- | --- |
| [ ? ] | Returns an array of values which will result in the given output value.Returns an empty array if the output value is not found. |

> **Ejemplo**
> ```lua
> -- Return all numbers between 0-100 which end in 'st' when written as 1st, 2nd, 3rd, etc
> -- [ 1, 21, 32, ... ]
> local resultsArr = config.Enum.ORDINAL_ENGLISH:GetInputValues("st")
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"CRAFTING_PLATINUM_TABLE"`. |
| typeName | String | The type of this config. Will always be `"Enum"`. |
| valueCount | Integer | The total number of key-value pairs in this enum. |
| values | [ [ ?, ? ] ] | All data value pairs contained in this enum.Each pair in the array is a 2-element data array of `[ inputValueType, outputValueType ]`. |
| inputValueType | [ValueType](vartype.md#valuetype) | The expected type of data this enum expects as an input value. |
| outputValueType | [ValueType](vartype.md#valuetype) | The expected type of data this enum expects as an output value. |