# QuestType

## Descripción General

A `QuestType` config contains data about one of the many quests in the game.

These config types can be found within the `config.Quest` table:

```lua
config.Quest.COOK_QUEST
config.Quest["QUEST_DUCK"]
config.Quest.FromID(456) -- config.Quest.ARCH_MONOLITH
```

> **Información**
> A `QuestType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `QuestType` includes:

* Display name
* Quest points rewarded
* Prerequisites

## Ejemplos

```lua
-- Access a QuestType config directly by using its name
local q200cfg = config.Quest.QUEST_200
-- or by ID lookup
local q200cfg = config.Quest.FromID(id.Quest.QUEST_200)
```

## MasterQuestVarPlayer

A container table holding data about a quest's progress tracking variable.
A quest will have only one of these.

> **Información**
> All properties are read-only.

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| varPlayer | [VarType](vartype.md) | The `var.VarPlayer` which holds the current progress value. |
| startState | Integer | The starting variable value for this quest.Values below this indicates that the quest has not been started. |
| endState | Integer | The completion value for this quest.Actual variable value may be greater than this, indicating post-completion progress. |

## QuestPreReqSkill

A container table holding data about a skill prerequisite.

> **Información**
> All properties are read-only.

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| skillType | [SkillType](../player.md#skilltype) | The skill type to check. |
| minimumLevel | Integer | The minimum skill level required by the Player Character to complete this prerequisite. |

## Enumeraciones

### QuestType

| Name | Value |
| --- | --- |
| NORMAL | 0 |
| SEASONAL | 1 |
| TUTORIAL | 2 |

### QuestDifficulty

| Name | Value |
| --- | --- |
| NOVICE | 0 |
| INTERMEDIATE | 1 |
| EXPERIENCED | 2 |
| MASTER | 3 |
| GRANDMASTER | 4 |
| MULTIDIFFICULTY | 5 |

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Métodos

### GetParamValue

```lua
function Quest:GetParamValue(param : ParamType) -> ?
```

Returns the corresponding output value for the given input [ParamType](paramtype.md).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| param | [ParamType](paramtype.md) | The input param value. |

| Retorna | Descripción |
| --- | --- |
| ? | The corresponding output value.Returns `param.defaultValue` if the param is not found in the data structure. |

> **Ejemplo**
> ```lua
> -- Get a value
> local value = config.Quest.ELEMENTAL_WORKSHOP_II:GetParamValue(config.Param.QUEST_RELEASE_YEAR) -- 2006
> ```

### HasParam

```lua
function Quest:HasParam(param : ParamType) -> Boolean
```

Returns whether this config contains output data for the given input [ParamType](paramtype.md).

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| param | [ParamType](paramtype.md) | The input param value. |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether a corresponding value exists in this config for [ParamType](paramtype.md). |

> **Ejemplo**
> ```lua
> -- Get a value, if a param for it exists
> if config.Quest.ELEMENTAL_WORKSHOP_II:HasParam(config.Param.QUEST_RELEASE_YEAR) then
>     -- Get the param value
>     local value = config.Quest.ELEMENTAL_WORKSHOP_II:GetParamValue(config.Param.QUEST_RELEASE_YEAR)
> end
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"QUEST_200"`. |
| typeName | String | The type of this config. Will always be `"Quest"`. |
| deprecated | Boolean | Whether this quest config has been deprecated.It has often been superseded by a different valid config.Deprecated quests are occasionally referenced in order to use their `iconID`. |
| name | String | The display name of this config type. |
| sortName | String | The string to use when sorting quest names alphabetically.For example, "Lost Tribe, The." |
| isMembers | Boolean | Whether this quest is for members. |
| questPoints | Integer | How many quest points are rewarded for completing this quest. |
| type | [QuestType](#questtype_1) | The type of quest. |
| difficulty | [QuestDifficulty](#questdifficulty) | The difficulty rating of this quest. |
| iconID | Integer | The sprite ID to display for this quest.This is shown on any [MiniMenuEntry](../minimenu.md#minimenuentry) related to this quest. |
| startCoordGrids | [ [CoordGrid](../coordgrid.md) ] | A list of [CoordGrids](../coordgrid.md) used to indicate where this quest can be started. |
| viaCoordGrid | [CoordGrid](../coordgrid.md) | An optional [CoordGrid](../coordgrid.md) to help navigate to one of the quest starting coordinates. |
| preReqQuestPoints | Integer | How many quest points the Player Character must have before starting this quest. |
| preReqQuests | [ [QuestType](questtype.md) ] | A list of quests the Player Character must have completed in order to start this quest. |
| preReqSkills | [ [QuestPreReqSkill](#questprereqskill) ] | A list of [SkillType](../player.md#skilltype) level requirement checks.Player Characters must meet all of the given requirements to start this quest. |
| completedPreReqQuestPoints | Boolean | Whether the Player Character has the required number of quest points to start this quest. |
| completedPreReqQuests | [ Boolean ] | Returns a list of boolean values for each prerequisite quest, indicating whether the Player Character has completed each of them. |
| completedPreReqSkills | [ Boolean ] | Returns a list of boolean values for each prerequisite skill level check, indicating whether the Player Character has completed each of them. |
| canStartQuest | Boolean | Whether the Player Character is able to start this quest.This returns `true` if all prerequisite checks are completed. |
| hasStartedQuest | Boolean | Whether the Player Character has started this quest. |
| hasFinishedQuest | Boolean | Whether the Player Character has completed this quest. |
| masterQuestVars | [ [MasterQuestVarPlayer](#masterquestvarplayer) ] | An array holding a list of [MasterQuestVarPlayer](#masterquestvarplayer) descriptors.There will always be one element in this array. |
| params | [ [ParamType](paramtype.md) ] | Returns a list of all the [ParamTypes](paramtype.md) stored in this config. |