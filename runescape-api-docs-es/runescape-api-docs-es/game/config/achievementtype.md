# AchievementType

## Descripción General

A `AchievementType` config contains data about one of the many achievements in the game.

These config types can be found within the `config.Achievement` table:

```lua
config.Achievement.CHEEVO_GODWARS_SOULSTONES
config.Achievement["CHEEVO_GODWARS_SOULSTONES"]
config.Achievement.FromID(1618) -- config.Achievement.CHEEVO_GODWARS_SOULSTONES
```

> **Información**
> A `AchievementType` is a Proxy usertype, which means it is safe to copy and store in your scripts.
It cannot, however, be used with any persistent storage.

Information available within an `AchievementType` includes:

* Display name
* Rewards
* Prerequisites
* Requirements

## Ejemplos

```lua
-- Access a AchievementType config directly by using its name
local cheevocfg = config.Achievement.CHEEVO_GODWARS_SOULSTONES
-- or by ID lookup
local cheevocfg = config.Achievement.FromID(id.Achievement.CHEEVO_GODWARS_SOULSTONES)
```

## Prerequisites and Requirements

Achievement configs contain one or more tests, each which can be one of several different test types:

| Nombre | Descripción |
| --- | --- |
| [AchievementTestSkill](#achievementtestskill) | Tests if skill(s) have met a certain level threshold. |
| [AchievementTestQuest](#achievementtestquest) | Tests if quest(s) are completed. |
| [AchievementTestAchievement](#achievementtestachievement) | Tests if achievement(s) are completed. |
| [AchievementTestVarTotal](#achievementtestvartotal) | Tests if variable(s) have met a certain value threshold. |
| [AchievementTestVarTestBit](#achievementtestvartestbit) | Test if variable bit(s) have been set to a certain value. |

These test types are further split into two different collections:

| Name | Property | Description |
| --- | --- | --- |
| Prerequisites | `AchievementType.prereqs` | Controls how an achievement is presented, such as being hidden until prerequisites have been met. |
| Requirements | `AchievementType.requirements` | Controls the actual completion of the achievement. |

An example would be an achievement with:

* Prerequisite
Skill Test - Smithing >= 20
* Requirement
Crafted Tally - Crafting items that require at least level 20 in Smithing to craft

This example could hide the achievement until Smithing is at level 20, revealing it only when the Player Character is able to craft items that meet the requirement.

More information about each of the types of test is shown below.

### AchievementTestSkill

This test collects Player Character's levels in the given [SkillTypes](../player.md#skilltype) into one cumulative total, and compares it against the target total level.

Typically this test will contain only one skill, but is able to support more.

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| group | Integer | The group ID of this test. |
| skillTypes | [ [SkillType](../player.md#skilltype) ] | All skill types to be tested.The levels of each skill type are added together. |
| totalLevels | Integer | The target total skill levels which must be achieved. |
| description | String | The description for this test, if supplied. |
| isComplete | Boolean | Whether the Player Character has completed this test. |

### AchievementTestQuest

This test checks whether the Player Character has completed the given quest.

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| group | Integer | The group ID of this test. |
| quest | [QuestType](questtype.md) | The quest config to test for completion. |
| description | String | The description for this test, if supplied. |
| isComplete | Boolean | Whether the Player Character has completed this test. |

### AchievementTestAchievement

This test checks whether the Player Character has completed the given achievement.

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| group | Integer | The group ID of this test. |
| achievement | [AchievementType](achievementtype.md) | The achievement config to test for completion. |
| description | String | The description for this test, if supplied. |
| isComplete | Boolean | Whether the Player Character has completed this test. |

### AchievementTestVarTotal

This test checks whether the cumulative total of a given list of [VarPlayers](vartype.md) values meets or exceeds a given total value.

An example would be a test for '50 bosses killed' that accumulates the values of many separate [VarPlayers](vartype.md) which individually track kills for a specific boss.

A more basic example would be '20 oak logs chopped' where only one [VarPlayer](vartype.md) value is compared to the total.

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| group | Integer | The group ID of this test. |
| vars | [ [VarPlayer](vartype.md) ] | The list of VarPlayer variables to accumulate the values of. |
| totalValue | Integer | The target value which must be met or exceeded. |
| description | String | The description for this test, if supplied. |
| isComplete | Boolean | Whether the Player Character has completed this test. |

### AchievementTestVarTestBit

This test checks whether a specific bit in a [VarPlayer](vartype.md) value matches a given value of `0` or `1`.

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| group | Integer | The group ID of this test. |
| var | [VarPlayer](vartype.md) | The VarPlayer variable holding the value which is tested. |
| bitIndex | Integer | The bit index of the tested value.**bitIndex is 0-indexed.** |
| bitValue | Integer | The target value which must be matched.This is typically always `1`. |
| description | String | The description for this test, if supplied. |
| isComplete | Boolean | Whether the Player Character has completed this test. |

## Enumeraciones

### AchievementProgressType

Achievement progress is provided by the `AchievementType.progress` property.

A positive value indicates that the achievement has partial completion, while a 0 or negative value indicates one of the enumerations below.

| Name | Value |
| --- | --- |
| READY | 0 |
| LOCKED | -1 |
| COMPLETE | -2 |
| GRACE | -3 |
| DEPRECATED | -4 |

### AchievementDescriptionType

Alternate achievement descriptions are available for various game modes.

These types are provided along with the relevant string by the `AcheivementType.descriptions` property.

| Name | Value |
| --- | --- |
| DEFAULT | 0 |
| IRONMAN | 1 |
| GROUP_IRONMAN_SIZE_2 | 2 |
| GROUP_IRONMAN_SIZE_3 | 3 |
| GROUP_IRONMAN_SIZE_4 | 4 |
| GROUP_IRONMAN_SIZE_5 | 5 |

### AchievementHiddenType

An achievement's display behaviour is controlled by this enumeration, and is provided by the `AchievementType.hiddenType` property.

| Name | Valor | Descripción |
| --- | --- | --- |
| NEVER | 0 | Achievement is always displayed |
| IF_LOCKED | 1 | Achievement is hidden if any **prerequisites** are incomplete. |
| UNTIL_COMPLETE | 2 | Achievement is hidden until all **requirements** are completed. |

## Constructors

> **Información**
> This usertype has no constructor, and you cannot create your own.

## Métodos

### GetPrereqGroupComplete

```lua
function Achievement:GetPrereqGroupComplete(group : Integer) -> Boolean
```

Returns whether the given prerequisite group is considered complete.

Depending on the value of [GetSubItemCompletionCountForPrereqGroup()](#getsubitemcompletioncountforprereqgroup), this can mean all or only some of the individual prerequisites have actually been completed.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| group | Integer | The group ID to be tested for completion.**`group` is 0-indexed.** |

| Retorna | Descripción |
| --- | --- |
| Boolean | Whether the prerequisite group is considered complete. |

> **Ejemplo**
> ```lua
> local cfg = config.Achievement.LEAGUE_TASK_EQUIP_MASTERWORK_ARMOUR_SET
> -- Check how many prerequisite groups are completed
> local totalGroupsCompleted = 0
> 
> -- 3 groups of prerequisites in this config
> for i=1,cfg.prereqGroupCount do
>     local groupIsCompleted = cfg:GetPrereqGroupComplete(i - 1) -- Group starts at 0
>     if groupIsCompleted then
>         totalGroupsCompleted = totalGroupsCompleted + 1
>     end
> end
> 
> -- Set if prereqs are considered to be completed
> local prereqsAreCompleted = totalGroupsCompleted >= cfg.completionCountForPrereqGroups
> 
> -- The above can also be achieved with only
> local prereqsAreCompleted = cfg.prereqsComplete
> ```

### GetSubItemCompletionCountForPrereqGroup

```lua
function Achievement:GetSubItemCompletionCountForPrereqGroup(group : Integer) -> Boolean
```

Returns how many individual prerequisites, each with the same group, must be completed for that group to be considered complete.

For example, if there were three prerequisites with group 0, and `GetSubItemCompletionCountForPrereqGroup(0)` returned a value of 1, then only one of the three prerequisites will need to be completed.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| group | Integer | The group ID to be checked.**`group` is 0-indexed.** |

| Retorna | Descripción |
| --- | --- |
| Integer | How many items in the prerequisite group need to be completed for the entire group to be considered complete. |

> **Ejemplo**
> ```lua
> local cfg = config.Achievement.LEAGUE_TASK_EQUIP_MASTERWORK_ARMOUR_SET
> 
> -- Gather how many prereqs of group 0 are completed
> local totalCompleted = 0;
> local testGroup = 0;
> 
> -- Loop through all types of prereq
> for k,v in pairs(cfg.prereqs) do
>     -- k will be 'skills', 'quests', 'achievements', 'varTotals' or 'varTestBits'
>     -- v will be a list of all the prereqs of that type
>     for _,req in ipairs(v) do
>         if req.group == testGroup and req.isComplete then
>             totalCompleted = totalCompleted + 1
>         end
>     end
> end
> 
> -- How many of group 0 must be completed
> local completeNeeded = cfg:GetSubItemCompletionCountForPrereqGroup(0)
> 
> -- Set if the group has been completed
> local groupIsCompleted = totalCompleted >= completeNeeded
> 
> -- The above can also be achieved with only
> local groupIsCompleted = cfg:GetPrereqGroupComplete(0)
> ```

### GetSubItemCompletionCountForRequirementGroup

```lua
function Achievement:GetSubItemCompletionCountForRequirementGroup(group : Integer) -> Boolean
```

Returns how many individual requirements, each with the same group, must be completed for that group to be considered complete.

For example, if there were three requirements with group 0, and `GetSubItemCompletionCountForRequirementGroup(0)` returned a value of 1, then only one of the three requirements will need to be completed.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| group | Integer | The group ID to be checked.**`group` is 0-indexed.** |

| Retorna | Descripción |
| --- | --- |
| Integer | How many items in the requirement group need to be completed for the entire group to be considered complete. |

> **Ejemplo**
> ```lua
> local cfg = config.Achievement.CHEEVO_MENAPHOS_SLAYER_MOBS_I
> 
> -- Gather how many requirements of group 0 are completed
> local totalCompleted = 0;
> local testGroup = 0;
> 
> -- Loop through all types of prereq
> for k,v in pairs(cfg.requirements) do
>     -- k will be 'skills', 'quests', 'achievements', 'varTotals' or 'varTestBits'
>     -- v will be a list of all the requirements of that type
>     for _,req in ipairs(v) do
>         if req.group == testGroup and req.isComplete then
>             totalCompleted = totalCompleted + 1
>         end
>     end
> end
> 
> -- How many of group 0 must be completed
> local completeNeeded = cfg:GetSubItemCompletionCountForRequirementGroup(0)
> 
> -- Set if the group has been completed
> local groupIsCompleted = totalCompleted >= completeNeeded
> ```

## Propiedades

> **Información**
> All properties are read-only.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Integer | The ID of this config type. |
| configName | String | The name of this config, i.e. `"CHEEVO_GODWARS_SOULSTONES"`. |
| typeName | String | The type of this config. Will always be `"Achievement"`. |
| name | String | The display name of this config type. |
| reward | String | A string containing any rewards for this achievement.Multiple rewards are delimited by "<br>". |
| isMembers | Boolean | Whether this achievement is for members. |
| category | Integer | The category type of this config.Returns `-1` if none is set.Category name is available using `id.Category.FromID()`. |
| subCategory | Integer | The sub-category type of this config.Returns `-1` if none is set.Category name is available using `id.Category.FromID()`. |
| spriteID | Integer | The ID of any sprite shown for this achievement.Returns `-1` if not set. |
| runeScore | Integer | The RuneScore value of the achievement.Returns `0` if not set. |
| hiddenType | [AchievementHiddenType](#achievementhiddentype) | The visibility behaviour of this achievement if its **prerequisites** are incomplete. |
| graceExpiryRunedate | Integer | The RuneDay when the grace period for this achievement expires.Before this, the achievement is always considered complete for the purpose of meta-achievements (e.g. Completion Cape).Returns -1 if not set. |
| hasRequirementDescriptions | Boolean | Whether any of the achievement requirements contains a description. |
| totalPrereqCount | Integer | How many total prerequisites this achievement contains. |
| totalRequirementCount | Integer | How many total requirements this achievement contains. |
| dbRowConfig | [DBRow](dbrowtype.md) | Any associated [DBRow](dbrowtype.md) for this achievement.Returns `nil` if not set. |
| tallyTarget | Integer | For achievements with a tally (such as killing 100 monsters), this returns what the target value is.Each achievement can have only one tally.Returns `-1` if not set. |
| tallyProgress | Integer | For achievements with a tally, this Devuelve el/la progression count actual.Returns `-1` if not set. |
| descriptions | [ Table ] | Returns a list of entries, each of which contain a [AchievementDescriptionType](#achievementdescriptiontype) and the text for the description, i.e.[    {        "type" : [AchievementDescriptionType](#achievementdescriptiontype),        "text" : "Description..."    },    ...] |
| prereqs | Table | Returns all prerequisites for this achievement, separated into sub-lists of requirement type, i.e.{    "skills" : [ [AchievementTestSkill](#achievementtestskill), ... ],    "quests" : [ [AchievementTestQuest](#achievementtestquest), ... ],    "achievements" : [ [AchievementTestAchievement](#achievementtestachievement), ... ],    "varTotals" : [ [AchievementTestVarTotal](#achievementtestvartotal), ... ],    "varTestBits" : [ [AchievementTestVarTestBit](#achievementtestvartestbit), ... ],} |
| achievements | Table | Returns all requirements for this achievement, separated into sub-lists of requirement type, i.e.{    "skills" : [ [AchievementTestSkill](#achievementtestskill), ... ],    "quests" : [ [AchievementTestQuest](#achievementtestquest), ... ],    "achievements" : [ [AchievementTestAchievement](#achievementtestachievement), ... ],    "varTotals" : [ [AchievementTestVarTotal](#achievementtestvartotal), ... ],    "varTestBits" : [ [AchievementTestVarTestBit](#achievementtestvartestbit), ... ],} |
| progress | Integer | Returns a progression value for this achievement.If the value is 0 or less, then it will be a [AchievementProgressType](#achievementprogresstype).Use `AchievementProgressType.FromID(config.progress)` to view the type name.If the value is greater than 0 then it indicates the current completion progress, where `10000` is the maximum value.For example:`local percentComplete = config.progress / 100` |
| prereqsComplete | Boolean | Whether prerequisites are regarded as completed.This is impacted by `completionCountForPrereqGroups` and [GetSubItemCompletionCountForPrereqGroup()](#getsubitemcompletioncountforprereqgroup) whereby not every test needs to be completed for this property to return `true`. |
| prereqGroupCount | Integer | How many separate groups of prerequisite tests exist. |
| completionCountForPrereqGroups | Integer | How many prerequisite groups need to be complete in order to consider all prerequisites as completed.For example, if `prereqGroupCount == 2` and `completionCountForPrereqGroups == 1` then only one of the two groups needs to be completed. |
| requirementGroupCount | Integer | How many separate groups of requirement tests exist. |
| completionCountForRequirementGroups | Integer | How many requirement groups need to be complete in order to consider all requirements as completed.For example, if `requirementGroupCount == 2` and `completionCountForRequirementGroups == 1` then only one of the two groups needs to be completed. |