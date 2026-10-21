# Interface

## Descripción General

An interface is essentially a self-contained bundle of components created from packed game assets, and loaded on demand by the UI system. Only one top-level interface can be loaded at any one point, with additional sub-interfaces being loaded within components in the top-level interface.

It's through interfaces that plugins can access existing components and use them as a parent for plugin components, or scan the built-in UI for data that might not yet be exposed in an easier-to-access manner.

> **Información**
> Since plugins can't create new interfaces, they must instead use components in the appropriate interface as a parent for their components.
> Using the right interface is important since components only live for as long as their interface is loaded.

> **Advertencia**
> Although care is generally taken to avoid changes to built-in interfaces that would result in components being removed or changing to a different type over time, plugins should always check any components they obtain are valid and of the desired type prior to performing any actions on them.
> This is particularly important when a plugin is accessing or making use of components dynamically created by the built-in interfaces, since the IDs those components are associated with do not represent a static target, meaning the type of the component corresponding to those IDs could change over time, resulting in potential plugin errors if a specific type is assumed.

## Ejemplo

```lua
local nameLabelID = 62 -- Can use entry from id.Component instead

-- Get the actual component
local heroPanelIF = ui.Interfaces:GetInterface(id.Interface.TOPLEVEL_V2_PARENT_SUBOVERLAY_ADVENTURERS_LOG)
local heroPanelNameLabel = nil

if heroPanelIF ~= nil then
    heroPanelNameLabel = heroPanelIF:GetComponent(nameLabelID)
end
-- Or just use the Interfaces:GetComponent helper
local heroPanelNameLabel = ui.Interfaces:GetComponent(id.Interface.TOPLEVEL_V2_PARENT_SUBOVERLAY_ADVENTURERS_LOG, nameLabelID)

-- Extract data from this component
if (heroPanelNameLabel ~= nil) and (heroPanelNameLabel.type == ui.ComponentType.LABEL) then
    local playerName = heroPanelNameLabel.content
    print(playerName) -- George
else
    print("Unable to find the name label component")
end
```

## Métodos

### GetComponent

```lua
function ui.Interface:GetComponent(interfaceID : Int, staticID : Uint) -> ui.Component<T>?
function ui.Interface:GetComponent(interfaceID : Int, staticID : Uint, categoryID : Uint, dynamicID : Uint) -> ui.Component<T>?
```

Attempts to retrieve the component associated with the various provided IDs contained within this interface.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| staticID | Uint | ID value used to identify the static component that's being retrieved, or that contains the dynamic component that's being retrieved. |
| categoryID | Uint | Category ID value used to identify this dynamic component's category. |
| dynamicID | Uint | Dynamic ID value used to identify this dynamic component. |

| Retorna | Descripción |
| --- | --- |
| [ui.Component](./component.md)? | The component of the appropriate type associated with the specified interface and component IDs, or nil if there's no component with these IDs. |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | Uint | Unique numeric value used to identify this specific interface. |
| clientOnly | Bool | True if this interface is managed entirely by the client and doesn't interact with the server. |

## ui.Interfaces

The `ui.Interfaces` object provides helper methods for quickly retrieving loaded interfaces and their components.

### GetInterface

```lua
function ui.Interfaces:GetInterface(interfaceID : Int) -> ui.Interface?
```

Retrieves the loaded interface matching the specified ID.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| interfaceID | Int | ID value used to identify the interface containing the component that's being retrieved. |

| Retorna | Descripción |
| --- | --- |
| ui.Interface? | The interface associated with the specified ID, or nil if missing or not loaded. |

### GetComponent

```lua
function ui.Interfaces:GetComponent(combinedID : Uint) -> ui.Component<T>?
function ui.Interfaces:GetComponent(combinedID : Uint, categoryID : Uint, dynamicID : Uint) -> ui.Component<T>?
function ui.Interfaces:GetComponent(interfaceID : Int, staticID : Uint) -> ui.Component<T>?
function ui.Interfaces:GetComponent(interfaceID : Int, staticID : Uint, categoryID : Uint, dynamicID : Uint) -> ui.Component<T>?
```

Retrieves the loaded interface matching the specified ID, and searches within for a component associated with the various provided IDs.

> **Información**
> This is equivalent to retrieving an interface using `ui.Interfaces:GetInterface` and then calling `ui.Interface:GetComponent` on it if the interface isn't nil.
> Prefer using that method instead if the plugin needs to retrieve components from the same interface often, as it avoids redundant interface lookups.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| combinedID | Int | The combined ID ( `(interfaceID  << 16) \| staticID` ) used to identify the component that's being retrieved.Combined IDs are available via lookups such as `id.Component.TOPLEVEL_V2__GAME_AREA` where the double-underscore separates the interface name (`TOPLEVEL_V2`) and El nombre de component within it (`GAME_AREA`) |
| interfaceID | Int | ID value used to identify the interface containing the component that's being retrieved. |
| staticID | Uint | ID value used to identify the static component that's being retrieved, or that contains the dynamic component that's being retrieved. |
| categoryID | Uint | Category ID value used to identify this dynamic component's category. |
| dynamicID | Uint | Dynamic ID value used to identify this dynamic component. |

| Retorna | Descripción |
| --- | --- |
| [ui.Component](./component.md)? | The component of the appropriate type associated with the specified interface and component IDs, or nil if there's no component with these IDs or the interface isn't loaded. |