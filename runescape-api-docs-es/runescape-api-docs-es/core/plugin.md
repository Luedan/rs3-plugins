# Plugin

## Descripción General

The plugin module allows users to access and query properties for the current plugin, as well as access plugin resources.

## Enumeraciones

### PluginPermissions

Contains all permissions a plugin may request.

| Valor | Descripción |
| --- | --- |
| httpAccess | Allows the use of [HTTP](./http.md)-related functionality if provided.   Makes use of base URLs specified in the plugin's manifest file. |
| chatAccess | Allows the use of [Chat](../game/chat.md)-related functionality if provided. |
| trackingAccess | Allows the use of [Tracking ID](../game/player.md#gettrackingid)-related functionality if provided. |

### urls

Table containing all URLs specified in the current plugin's metadata.

See [HTTP](./http.md) for more information on using these values along with examples.

> **Ejemplo**
> ```json
> "urls": { "wiki" : "http://www.runescape.wiki" },
> ```
> ```lua
> -- Accessed as follows
>     Plugin.urls.wiki
> ```

### Recursos Adicionales

Table containing all custom resources stored under the current plugin's `resources` folder, using their filenames as table keys. See [Plugin Resources](#plugin-resources) for information on how to use these.

> **Información**
> Nested folders are represented as sub-tables, so for example `resources/images/menu/background.png` can be accessed as `Plugin.resources.images.menu.background`.

## Métodos

### HasPermission

```lua
function Plugin.HasPermission(permission : PluginPermissions) -> Bool
```

Checks if the user has allowed the specified permission for the current plugin.

> **Información**
> Unless your plugin won't work at all without a specific permission, prefer marking permissions as optional in the manifest and using `HasPermission` to check whether or not to enable functionality that depends on that permission.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| permission | [PluginPermissions](#pluginpermissions) | The permission to check. |

| Retorna | Descripción |
| --- | --- |
| Bool | True if the specified permission has been given to this plugin, false otherwise. |

> **Ejemplo**
> ```lua
> if Plugin.HasPermission(PluginPermissions.httpAccess) then
>     -- Use functionality that require httpAccess
> end
> ```

## Plugin Resources

Custom resources provided by plugins can be used as a alternative for built-in ones in various methods, but also provide some additional functionality.

Resources are automatically loaded on demand, or can be loaded explicitly by plugins, which can be useful when dealing with larger resources, or to keep audio in memory to avoid any delays.

See [here](#resources) on information on how to access the resources provided by a plugin.

> **Información**
> Support for custom resources is currently limited to the following types and their associated formats:
> * Sprites ([`PluginResource`](#methods_1) -> `PluginImageResource`): Portable Network Graphics (.png)
> * Audio ([`PluginResource`](#methods_1) -> `PluginAudioResource`): Ogg Vorbis (.ogg)

> **Advertencia**
> Once loaded, a resource will remain loaded until either the plugin that owns it is unloaded and all references to it are freed, or until the user manually unloads it.

> **Advertencia**
> Image resources are limited to a maximum size of 1024x1024 pixels currently.

### Enumeraciones

#### PluginResourceLoadResult

| Valor | Descripción |
| --- | --- |
| success | The resource has been loaded successfully. |
| errorFilesystem | Failed to read the resource from disk. |
| errorDecode | Failed to decode the resource, it may be using an unsupported format. |
| errorExceedsLimits | Failed to load the resource as it exceeds limits. |
| errorConstruction | Failed to construct this resource even though loading succeeded.   This can occur when attempting to load a resource during shutdown for example. |

### Métodos

#### Load

```lua
function PluginResource<T>:Load() -> PluginResourceLoadResult
```

Attempts to load this resource, making it ready for immediate use afterwards if successful.

| Retorna | Descripción |
| --- | --- |
| PluginResourceLoadResult | Indicates whether loading succeeded, or the error in case it failed. |

#### Unload

```lua
function PluginResource<T>:Unload()
```

Attempts to unload this resource's data.

No data is actually freed until all references to it have been released, meaning that if it's being used for a sprite elsewhere, that sprite will remain valid until it is removed as well, even though the resource itself has been unloaded.

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| path | String | **(Read-only)**   The disk path to this resource. |
| loaded | Bool | **(Read-only)**   Whether the resource's data is currently loaded and ready to use. |
| inUse | Bool | **(Read-only)**   Whether or not the resource is being used anywhere currently. |