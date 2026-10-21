# Client Options

## Descripción General

Client options represent configurable game client settings, ranging from graphical settings such as draw distance and ground decor, to audio volume levels, and accessibility options like cutscene subtitles and cursor scales.

> **Información**
> These represent the options available at the game client/engine-level, independent of actual game content, hence they do not include the various options listed in the ingame gameplay settings interface for example.

The various options are contained within the `game.options` table, with the following options being available:

## Ejemplo

```lua
-- Disable loginscreen music while this plugin is active
local originalLoginScreenVolume = game.options.VolumeLoginMusic.setting
game.options.VolumeLoginMusic.setting = 0

function PluginShutdown()
    game.options.VolumeLoginMusic.setting = originalLoginScreenVolume
end
```

```lua
function PrintOptionLabels(option)
    if option.hasLabels then
        for i=option.min, option.max do
            log("AmbientOcclusion option", i, "=", option:GetLabel(i))
        end
    else
        log("No labels for this option")
    end
end

PrintOptionLabels(game.options.AmbientOcclusion)
PrintOptionLabels(game.options.Language)
```

## Métodos

### Set

```lua
function game.options.<option name>:Set(setting : Int) -> Bool
```

Sets this option to the specified setting.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| setting | Int | The setting to set this option to. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if this option was successfully changed to the provided setting, false otherwise. |

### CheckIsValidSetting

```lua
function game.options.<option name>:CheckIsValidSetting(setting : Int) -> Bool
```

Checks if the specified setting is valid for this option.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| setting | Int | The setting to check for validity. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if this option supports being set to the provided setting, false otherwise. |

### GetLabel

```lua
function game.options.<option name>:GetLabel(setting : Int) -> String?
```

Gets the user-friendly text label associated with the provided setting for this option.

> **Advertencia**
> This function is non-localised currently, always returning english text.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| setting | Int | The setting to retrieve the text label for. |

| Retorna | Descripción |
| --- | --- |
| String? | The text label associated with the provided setting, or nil if the setting is invalid or has no associated text. |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| hasLabels | Bool | **(Read-only)**   True if there are text labels for this option's values, false otherwise. |
| isToggle | Bool | **(Read-only)**   True if this a on/off toggle setting instead of supporting arbitrary values. |
| isModifiable | Bool | **(Read-only)**   True if this option can be currently modified.   Some settings may not be modified in certain cases where there's a dependency on other settings.   For example, you can't change the shadow quality level if shadows are disabled. |
| setting | Int | The current setting for this option. |
| min | Int | **(Read-only)**   The minimum setting this option can be set to. |
| max | Int | **(Read-only)**   The maximum setting this option can be set to. |
| minMaxRange | (Int, Int) | **(Read-only)**   Returns the minimum and maximum values this option can be set to. |