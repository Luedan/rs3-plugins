# Audio

## Descripción General

The audio system allows plugins to create sound instances for builtin sound resources or for their [custom audio resources](./../core/plugin.md#plugin-resources), and control their playback.

## Ejemplo

```lua
local curSound = audio.Play(Plugin.resources.click_long)

curSound:Pause()
print(curSound.isPaused, curSound.isPlaying)
curSound:Resume()
print(curSound.isPaused, curSound.isPlaying)

curSound:Stop()
```

```lua
local soundParams = audio.SoundPlaybackParams.new()
soundParams.type = audio.SoundType.SCRIPT
soundParams.audioBus = audio.AudioBus.SFX
soundParams.volume = 0.5 -- 50%
soundParams.numLoops = 2
soundParams.delayTick = 0
soundParams.samplingRate = 100 -- Default = 256, which is also used when samplingRate is 0

-- Disable spatial audio with audio.EmitterShape.NONE
-- Using audio.EmitterShapes.SPHERE/BOX/SPHERE_NO_PANNING/BOX_NO_PANNING enables that instead
soundParams.emitterShape = audio.EmitterShape.NONE

-- These are only relevant for spatial audio sounds
soundParams.origin = Vector3.new(0.0)
soundParams.minDistance = 0.0
soundParams.maxDistance = 1.0
soundParams.level = -1

audio.Play(Plugin.resources.click, soundParams)

-- Sound parameters are reusable
audio.Play(Plugin.resources.click_long, soundParams)
```

## Enumeraciones

### audio.SoundType

Identifies the type of sound associated with a [SoundInstance](#audiosoundinstance)'s playback.Unless otherwise stated, these are just used to categorise sounds and don't affect playback.

| Name | Valor | Descripción |
| --- | --- | --- |
| INVALID | 255 |  |
| ENTITY | 0 |  |
| LOCATION | 1 |  |
| LOCATION_RANDOM | 2 |  |
| GENERAL_ANIMATION | 3 |  |
| LOCATION_ANIMATION | 4 |  |
| ENTITY_ANIMATION | 5 |  |
| SPOT_ANIMATION | 6 |  |
| SCRIPT | 7 |  |
| SERVER_TRIGGERED | 8 |  |
| MUSIC | 9 | Identifies a sound meant to be played as music.   Playback for audio of this type cannot be manually stopped. |
| JINGLE | 10 | Identifies a sound meant to be played as a short jingle.   Playback for audio of this type cannot be manually stopped. |
| ENTITY_MOVEMENT | 11 |  |
| INTERFACE_ANIMATION | 12 |  |

### audio.AudioBus

Identifies the audio bus a sound instance is playing into, used by the audio mixer system.These are used to identify certain elements used during audio playback, such as the desired volume based on game settings.

| Name | Value |
| --- | --- |
| MASTER | 0 |
| SFX | 1 |
| MUSIC | 2 |
| MUSIC_LOGIC | 3 |
| AMBIENT | 4 |
| VOICEOVER | 5 |
| SFX_SUB | 6 |
| MUSIC_SUB | 7 |
| DIALOG_SUB | 8 |
| PLAYER_ANIMATION_SUB | 9 |
| NPC_ANIMATION_SUB | 10 |
| LOCATION_ANIMATION_SUB | 11 |
| GENERAL_ANIMATION_SUB | 12 |
| LOCATIONS_SUB | 13 |
| LOCATION_RANDOM_SUB | 14 |
| LOCATION_GENERIC_SUB | 15 |

### audio.EmitterShape

Controls how spatial audio applies to this sound instance.

| Name | Valor | Descripción |
| --- | --- | --- |
| SPHERE | 0 | The sound's volume scales based on distance between the emitter and the listener, and takes into account the angle between them.   Represents a spherical volume. |
| BOX | 1 | The sound's volume scales based on distance between the emitter and the listener, and takes into account the angle between them.   Represents a box volume. |
| SPHERE_NO_PANNING | 2 | The sound's volume scales based on distance between the emitter and the listener, ignoring the angle between them.   Represents a spherical volume. |
| BOX_NO_PANNING | 3 | The sound's volume scales based on distance between the emitter and the listener, ignoring the angle between them.   Represents a box volume. |
| NONE | 4 | The emitter doesn't use spatial audio. |

## Tipos

### audio.SoundInstance

SoundInstances represent a single playable sound. By default they're created dormant, and a plugin must then manually call `Play` on them for playback to start.

SoundInstances can also expire naturally (via shutdown of the plugin they were created in, or by being played and finishing), or through script requests (via `Stop`).

#### Métodos

##### Start

```lua
function audio.SoundInstance:Start(ticksDelay : Int?)
```

Starts playing this sound instance, or requests playback to start in the specified number of logic ticks.

Does nothing if this sound has already expired.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| ticksDelay | Int? | Optional, indicates how many logic ticks to wait for before this sound starts playing. |

##### Stop

```lua
function audio.SoundInstance:Stop()
```

Stops playing this sound instance immediately.

Does nothing if this sound has already expired.

##### Pause

```lua
function audio.SoundInstance:Pause()
```

Pauses playback for this sound instance immediately.

Does nothing if this sound has already been paused or has expired.

> **Advertencia**
> Avoid having a large amount of sounds paused, while the added overhead is minimal, in some cases it could prevent other audio from playing due to limitations on the number of live sound instances present in the audio mixer system.

##### Resume

```lua
function audio.SoundInstance:Resume()
```

Resumes playback for this sound instance immediately.

Does nothing if this sound isn't paused or has expired.

#### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| isPlaying | Bool | True if this sound is currently playing, false otherwise. |
| isPaused | True if this sound is currently paused. |  |
| id | Numeric ID used to uniquely identify this sound instance. |  |

### audio.SoundPlaybackParams

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| type | [audio.SoundType](#audiosoundtype) | The type of this sound.   Defaults to `audio.SoundType.Script`. |
| numLoops | Int | How many times this sound should loop for.   Defaults to 0, indicating a one-shot sound. |
| volume | Float | Volume for this sound's playback relative to its audio bus volume.   Defaults to 1.0, representing 100% volume. |
| audioBus | [audio.AudioBus](#audioaudiobus) | The audio bus associated with this sound.   Defaults to `audio.AudioBus.SFX`. |
| emitterShape | [audio.EmitterShape](#audioemittershape) | The shape used for this sound's spatial audio.   Defaults to `audio.EmitterShape.none`, representing non-spatial audio. |
| minDistance | Float | Minimum distance in world units for this sound to be audible.   Only relevant for spatial audio.   Defaults to 0. |
| maxDistance | Float | Maximum distance in world units for this sound to be audible.   Only relevant for spatial audio.   Defaults to 0. |
| origin | [Vector3](./../math/vector.md) | Origin in world units for this sound's emitter.   Only relevant for spatial audio.   Defaults to 0,0,0. |
| level | Int | Height level where this sound's playing from.   Only relevant for spatial audio.   Defaults to -1. |
| samplingRate | Uint | Rate at which this audio is sampled.   Affects pitch and playback speed.   Defaults to 0, indicating the default sample rate (256) should be used instead. |
| delayTick | Int | The number of logic ticks to delay playback for.   Defaults to 0, indicating immediate playback. |

## Funciones

### audio.Play

```lua
function audio.Play(resource : PluginAudioResource, params : audio.SoundPlaybackParams?) -> audio.SoundInstance?
function audio.Play(builtinResourceID : Int, params : audio.SoundPlaybackParams?) -> audio.SoundInstance?
```

Creates an instance for an audio resource that can then be played back.

> **Información**
> The resulting instance starts playing immediately if you omit playback parameters or they have a delay of `0`. You can defer playback by specifying parameters with a large delay (eg. `100000`), and then manually calling `Play` on the created sound instance.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| resource | [PluginAudioResource](./../core/plugin.md#plugin-resources) | The plugin-provided audio resource to create a sound instance for. |
| builtinResourceID | Int | Numeric ID for the built-in audio resource to create a sound instance for. |
| params | [audio.SoundPlaybackParams](#audiosoundplaybackparams)? | Parameters used to configure the sound instance.   Will use default parameter values if not provided. |

| Retorna | Descripción |
| --- | --- |
| audio.SoundInstance? | The newly created sound instance, or nil if resource loading or we were already at the maximum number of live sound instances. |

### audio.Stop

```lua
function audio.Stop(soundInstanceID : Int)
```

Immediately stops playback for the sound instance associated with the provided ID if it exists and is live.

> **Información**
> Prefer using `audio.SoundInstance:Stop` instead whenever possible. The one advantage of using this function is it won't trigger an error if the sound instance is already defunct, so it can be useful if you're passing sound instances to other plugins.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| soundInstanceID | Int | Unique numeric value used to identify the sound instance we're looking to stop playback. |

### audio.StopSoundsUsingResource

```lua
function audio.StopSoundsUsingResource(resource : PluginAudioResource)
function audio.StopSoundsUsingResource(builtinResourceID : Int)
```

Stops playback for **all** sound instances currently using the provided resource.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| resource | [PluginAudioResource](./../core/plugin.md#plugin-resources) | The plugin-provided audio resource to stop playback for. |
| builtinResourceID | Int | Numeric ID for the built-in audio resource to stop playback for. |