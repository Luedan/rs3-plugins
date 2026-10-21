# ui.Component

## Descripción General

Base type common to all user interface elements. The following components inherit from this:

* Decorative: [Line](./decorative_components/line.md), [Rectangle](./decorative_components/rectangle.md), [Text](./decorative_components/text.md), [Sprite](./decorative_components/sprite.md), [Model](./decorative_components/model.md), [Model Group](./decorative_components/modelgroup.md)
* Interactive: [Button](./interactive_components/button.md), [Check](./interactive_components/check.md), [List](./interactive_components/list.md), [Input Field](./interactive_components/input_field.md), [Slider](./interactive_components/slider.md), [Combo Field](./interactive_components/combo_field.md), [Carousel](./interactive_components/carousel.md), [Radio Group](./interactive_components/radio_group.md)
* Layout: [Layer](./layout_components/layer.md), [Panel](./layout_components/panel.md), [Grid](./layout_components/grid.md) [Paged Layer](./layout_components/paged_layer.md), [Group Box](./layout_components/group_box.md), [Paged Carousel](./layout_components/paged_carousel.md)
See also [Component Collection](./component_collection.md) for methods and properties shared by these components

## Ejemplos

```lua
-- Resize a component to 100x200 interface units and move it to 50 units from the top left of its parent
component:SetPos(50, 50)
component:SetSize(100, 200)

-- Centre the component on its parent and resize it to 300x150 interface units
component:SetPos(0, 0, 0.5, 0.5, -0.5, -0.5)
component:SetSize(300, 150)

-- Resize a component to 30% of the parent's width and 100% of the height, and place it in the centre
component:SetPos(0, 0, 0.3, 1.0, -0.5, 0.0)
component:SetSize(0, 0, 0.3, 1.0)
```

```lua
-- Use a specific style
component.stylesheetID = myStyleID
-- Change the colour to red with a slight transparency
component.colour = Vector4.new(1.0, 0.0, 0.0, 0.7)
-- Make it more transparent
component.alpha = component.alpha - 50
-- Set the colour to blue using a hex colour code
component.rgba = 0x0000FF77
```

## Positioning and Layout

### Métodos

#### SetX/SetY/SetPos

```lua
function Component:SetX(x : Int, parentPercentageX : Float?, selfPercentageX : Float?)
function Component:SetY(y : Int, parentPercentageY : Float?, selfPercentageY : Float?)

function Component:SetPos(
    x : Int, y : Int,
    parentPercentageX : Float?, parentPercentageY : Float?,
    selfPercentageX : Float?, selfPercentageY : Float?)
```

Moves this component's origin to the provided coordinates, optionally taking into account the parent's dimensions, and this component's own dimensions.

> **Información**
> `SetPos` should be preferred over using SetX and SetY separately as it involves less layout operations.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| x | Int | Absolute horizontal coordinate to move this component to in interface units |
| y | Int | Absolute vertical coordinate to move this component to in interface units |
| parentPercentageX | Float? | If specified, offsets this component's horizontal origin based on a percentage of its parent's width. |
| parentPercentageY | Float? | If specified, offsets this component's vertical origin based on a percentage of its parent's height. |
| selfPercentageX | Float? | If specified, offsets this component's horizontal origin based on a percentage of its width. |
| selfPercentageY | Float? | If specified, offsets this component's vertical origin based on a percentage of its height. |

> **Ejemplo**
> ```lua
> -- Move the component to 100 units from the left and 50 units from the top
> component:SetX(100)
> component:SetY(50)
> 
> -- Place the component's origin on the parent's center and offset it 50 units to the left
> component:SetX(-50, 0.5)
> component:SetY(0, 0.5)
> 
> -- Right-align the component on its parent, assuming it has a width of 125
> component:SetX(-125, 1.0)
> 
> -- Right-align the component on its parent, taking into account its actual width
> component:SetX(0, 1.0, -1.0)
> 
> -- Center the component on its parent
> component:SetX(0, 0.5, -0.5)
> component:SetY(0, 0.5, -0.5)
> 
> -- Right-align the component to the parent's center
> component:SetX(0, 0.5, -1.0)
> component:SetY(0, 0.5, -0.5)
> ```

#### SetWidth/SetHeight/SetSize

```lua
function Component:SetWidth(x : Int, parentPercentageX : Float?)
function Component:SetHeight(y : Int, parentPercentageY : Float?)
function Component:SetSize(x : Int, y : Int, parentPercentageX : Float?, parentPercentageY : Float?)
```

Sets the width/height for this component, optionally taking into account the parent's dimensions.

> **Información**
> `SetSize` should be preferred over using SetX and SetY separately as it involves less layout operations.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| x | Int | Absolute width in interface units to resize this component to. |
| y | Int | Absolute height in interface units to resize this component to. |
| parentPercentageX | Float? | If specified, offsets this component's width based on a percentage of its parent's width. |
| parentPercentageY | Float? | If specified, offsets this component's height based on a percentage of its parent's height. |

> **Ejemplo**
> ```lua
> -- Resize this component to 100x50
> component:SetWidth(100)
> component:SetHeight(50)
> -- or
> component:SetSize(-50, 50)
> 
> -- Resize this component to 50% of the parent's dimensions, but make it 50 interface units narrower
> component:SetWidth(-50, 0.5)
> component:SetHeight(0, 0.5)
> -- or
> component:SetSize(-50, 0, 0.5, 0.5)
> ```

#### SetAspectRatio

```lua
function Component:SetAspectRatio(widthRatio : Int, heightRatio : Int, mode : ui.AspectRatioMode)
```

Sets the target aspect ratio the component should follow, and how it should be applied. Can also be used to disable aspect ratio scaling.

> **Información**
> Invalid width and height ratio values will be replaced with `1` when calling this function.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| widthRatio | Int | Target width aspect ratio |
| heightRatio | Int | Target height aspect ratio |
| mode | [ui.AspectRatioMode](./common_types.md#uiaspectratiomode) | Indicates how the component scales based on its target aspect ratio |

> **Ejemplo**
> ```lua
> -- Set the component to a standard 16:9 aspect ratio, scaling its width
> component:SetAspectRatio(16, 9, ui.AspectRatioMode.SCALE_WIDTH)
> 
> -- Disable aspect ratio scaling
> component:SetAspectRatio(1, 1, ui.AspectRatioMode.NONE)
> ```

#### Destroy

```lua
function Component:Destroy()
```

Destroys this component, along with any other components that might have been attached to it.

> **Nota**
> Plugins can't delete components belonging to other plugins.

#### MoveToFront/MoveToBack

```lua
function Component:MoveToFront()
function Component:MoveToBack()
```

Moves this component to the front/back of the render order, causing it to draw on top/below of components that have the same parent.

#### UpdateLayout

```lua
function Component:UpdateLayout()
```

Triggers a layout update on this component.

> **Información**
> You should generally never need to call this directly, as it is automatically called whenever a layout modifying operation (eg. `SetSize`) occurs on a component.

### Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| position | [ui.Pos](./common_types.md#uipos) | Gets or sets this component's origin. |
| size | [ui.Size](./common_types.md#uisize) | Gets or sets the dimensions for this component. |
| isSafeAreaRelative | Bool | Whether or not layout operations involving this component take into account the device's safe areas. |
| x | Int | **(Read-only)** Current horizontal position for this component relative to its parent. |
| y | Int | **(Read-only)** Current vertical position for this component relative to its parent. |
| width | Int | **(Read-only)** Current width for this component. |
| height | Int | **(Read-only)** Current height for this component. |
| xyLocal | [Vector2](../math/vector.md#vector2) | **(Read-only)** Current XY position for this component relative to its parent. |
| xyGlobal | [Vector2](../math/vector.md#vector2) | **(Read-only)** Current absolute XY position for this component. |

## Handling Events

Components can set as listeners for certain events, allowing developers to trigger actions in response. These range from events triggered on that component, such as mouse clicks, to global events, such as variable transmissions.

### ui.Hook

The `ui.Hook` table contains a list of all potential event hooks that can be attached to a component.

### Subscribe

```lua
function Component:Subscribe(hook : ui.Hook, callback : function (...) -> Bool?)
function Component:Subscribe(hook : ui.Hook, id : String, callback : function (...) -> Bool?)
```

Subscribes a listener for an event hook, setting a callback to be triggered whenever this event occurs, and optionally assigning it an ID allowing it to be referenced to in the future.

> **Información**
> IDs are specific to an event hook type, the component they're attached to, and the current plugin, so the same ID can be used across different components or events, and doesn't need to be unique per plugin as well.

> **Limitations**
> * Calling `Subscribe` multiple times using the same event hook type and ID will instead replace the existing callback.
> * Plugins can't remove/replace callbacks subscribed by other plugins.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| hook | ui.Hook | The event hook to listen for. |
| callback | function (...) -> Bool? | The callback to trigger on this event, with parameters varying based on the event hook type.   Can return a boolean indicating whether or not to continue processing listeners afterwards. If omitted, the callback is treated as if it returned true, resulting in other listeners still getting triggered. |
| id | String | Name used to refer to this listener.   Used when attempting to remove a listener by its ID via `Unsubscribe`. |

> **Ejemplo**
> ```lua
> local myComponent = ...
> myComponent:Subscribe(ui.Hook.ONCLICK, "a", function () log("Hello") return true end)
> -- Or
> myComponent:Subscribe(ui.Hook.ONCLICK, "b", function () log("World") return true end)
> 
> -- Clicks yield "Hello World"
> ```
> ```lua
> local myComponent = ...
> myComponent:Subscribe(ui.Hook.ONCLICK, "a", function () log("Hello") return true end)
> -- Or
> myComponent:Subscribe(ui.Hook.ONCLICK, "a", function () log("World") return true end)
> 
> -- Clicks yield "World"
> ```
> ```lua
> local myComponent = ...
> myComponent:Subscribe(ui.Hook.ONCLICK, "a", function () log("Hello") return false end)
> -- Or
> myComponent:Subscribe(ui.Hook.ONCLICK, "b", function () log("World") return true end)
> 
> -- Clicks yield "Hello"
> ```

### Unsubscribe

```lua
function Component:Unsubscribe(hook : ui.Hook)
function Component:Unsubscribe(hook : ui.Hook, id : String)
```

Removes the listener set for the specified hook with the provided ID, or the default listener for that hook if omitted, from that component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| hook | ui.Hook | The event hook to listen for. |
| id | String | Name used to refer to this listener.   Used when attempting to remove a listener by its ID via `Unsubscribe`. |

> **Ejemplo**
> ```lua
> local myComponent = ...
> myComponent:Subscribe(ui.Hook.ONCLICK, "myHookName", function () log("Hello World") end)
> -- Later on
> myComponent:Unsubscribe(ui.Hook.ONCLICK, "myHookName")
> ```

### UnsubscribeAll

```lua
function Component:UnsubscribeAll(hook : ui.Hook)
```

Removes all event listeners of the specified type from this component associated with the current plugin.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| hook | ui.Hook | The event hook to clear the listeners for. |

## Visual Properties

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| alpha | Float | Controls how opaque this component appears, ranges from 0 (fully transparent) to 1 (opaque). |
| rgb | Uint | Hexadecimal colour code representing the Red, Green, and Blue tints for this component. |
| rgba | Uint | Hexadecimal colour code representing the Red, Green, Blue, And Alpha tints for this component. |
| colour | [Vector4](./../../math/vector.md) | Red, Green, Blue, and Alpha tints represented as a 4-channel vector, with each channel limited to a 0..1 range.   On assignment, values outside of this range will be clamped. |
| hidden | Bool | Controls whether this component is visible.    This only applies to Lua-side visibility, and cannot be used to force built-in UI components to become visible. |
| visible | Bool | **(Read-only)** Indicates whether this component is visible or not.   This state refers only to the internal state of this component. For the global visibility state see `visibleGlobal`.   Differs from `hidden` in that this also takes into account built-in UI component visibility. |
| visibleGlobal | Bool | **(Read-only)** Indicates whether this component is visible within the UI component tree.   For example, will return `false` if any parent of this component is not visible. |
| stylesheetID | Int | ID for the StyleSheet currently in use by this component, or -1 if no StyleSheet is active. |
| aspectRatioProportion | Float | **(Read-only)**   The aspect ratio width value divided by the height value.   For example, a `16:10` ratio resolves to a proportion of `1.6`. |
| aspectRatioWidth | Int | **(Read-only)**   The target width value used for aspect ratio calculations.   Note this value is always `1` or higher, even when aspect ratio scaling is disabled. |
| aspectRatioHeight | Int | **(Read-only)**   The target height value used for aspect ratio calculations.   Note this value is always `1` or higher, even when aspect ratio scaling is disabled. |
| aspectRatioMode | [ui.AspectRatioMode](./common_types.md#uiaspectratiomode) | **(Read-only)**   Mode used when determining how the aspect ratio should be applied to this component, if at all. |

## State Properties

The following properties relate to how the user interacts with the component and how the component reacts to said interactions.

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| enabled | Bool | Controls whether this component responds to inputs and events. |
| clickthrough | Bool | Controls whether mouse interactions on this component block interactions on components below it. |
| isMouseOver | Bool | **(Read-only)** Whether the cursor is currently over this component or not. |
| isClicked | Bool | **(Read-only)** Whether the user has clicked on this component recently or not. |
| opConfig | [ui.ComponentOpConfig](./component_configs.md#uicomponentopconfig) | Identifies the action to perform when the component is interacted with. |
| dragConfig | [ui.ComponentDragConfig](./component_configs.md#uicomponentdragconfig) | Determines how the component reacts to drag actions. |
| swipeConfig | [ui.ComponentSwipeConfig](./component_configs.md#uicomponentswipeconfig) | Determines how the component reacts to swipe gestures. |
| pinchConfig | [ui.ComponentPinchConfig](./component_configs.md#uicomponentpinchconfig) | Determines how the component reacts to pinch gestures. |
| cursorConfig | [ui.ComponentCursorConfig](./component_configs.md#uicomponentcursorconfig) | Specifies which cursors to use, if any, when interacting with this component. |
| paramsConfig | [ui.ComponentParamsConfig](./component_configs.md#uicomponentparamsconfig) | Additional parameters attached to this component. |

## Interface Properties

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| type | [ui.ComponentType](./common_types#uicomponenttype) | **(Read-only)** ID identifying the type of this component. |
| parent | ui.Component? | **(Read-Only)** The immediate parent of this component within the UI component tree.Returns `nil` if there is no parent. |
| parentStatic | ui.Component? | **(Read-Only)** The static parent of this component within the UI component tree.Returns `nil` if there is no static parent. |
| parentInterface | [Interface](./interface.md) | **(Read-Only)** Interface in which this component resides. |
| interfaceID | Int | **(Read-only)** ID identifying the interface in which this component resides. |
| staticID | Int | **(Read-only)** ID identifying the static component on which this component resides. |
| categoryID | Int | **(Read-only)** ID identifying the dynamic ID category this component's using, or -1 if this is a static component. |
| dynamicID | Int | **(Read-only)** ID identifying the dynamic ID category this component's using, or -1 if this is a static component. |

## Restricted Components

In some cases, components may be flagged as restricted, preventing certain operations from working from the Lua-side, or resulting in them yielding default values instead.

Components can be intentionally tagged as restricted through the `Component:FlagRestricted()` function, with the restricted status being verifiable via `component.isRestricted`.

> **Advertencia**
> Once restricted, a component cannot become unrestricted afterwards.

> **Advertencia**
> Flagging a component as restricted is only possible if the current plugin is its creator.

> **Limitations on restricted components**
> * Attempting to retrieve the content of `InputField` and `Label` components returns an empty string.
> * `InputField:Setup` cannot be called on a restricted component