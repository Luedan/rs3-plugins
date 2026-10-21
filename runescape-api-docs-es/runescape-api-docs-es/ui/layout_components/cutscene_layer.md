# ui.CutsceneLayer

## Descripción General

[ui.Component](./../component.md) -> [ui.ComponentCollection](./../component_collection.md) -> [ui.Layer](./layer.md) -> ui.CutsceneLayer

Cutscene layers are layer-like components used for 2D cutscene playback.

> **Advertencia**
> Cutscenes aren't currently exposed to the plugin API, however existing cutscene layers can be accessed as regular layers.

## Enumeraciones

### ui.CutscenePlaybackEndReason

Identifies why a cutscene finished playing on a cutscene layer component.

| Valor | Descripción |
| --- | --- |
| FINISHED | The cutscene finished playing normally. |
| CANCELLED | Playback was manually cancelled by the user. |
| INTERRUPTED | The cutscene was interrupted by another cutscene. |
| INTERFACE_CLOSED | The cutscene's playback was interrupt due to the interface in which its layer resided being closed. |