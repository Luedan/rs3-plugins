# User Interfaces

## Descripción General

The plugin API can be used to create new interfaces and manipulate existing ones, ranging from changing colours and styles, to contents.

> **Default Property Values**
> Unless otherwise stated, values for certain UI properties present across multiple types in the interface system share the same default value, in particular:
> * Colours and tints - White (`Vector4.new(1.0)` or `0xFFFFFFFF`) by default
> * Alpha - Fully opaque (`1.0`) by default

## Componentes

A component represents a single element of the game interface, ranging from an input field, to a button, or a grid for example.

Components can be split into two categories:

* `Static` - hardcoded components defined via resource files
* `Dynamic` - components created at runtime via scripts

Both categories behave in the same way and support the exact same components, however they're identified slightly differently. `Dynamic` components are always created on a `static` parent component, and are associated with two IDs, a category ID and a dynamic ID, which combined represented a unique ID on the parent static component.

> **Información**
> Unlike dynamic components, static components cannot be removed at runtime.

The RuneScape Client API can only be used to create `Dynamic` components but can be used to access and modify both `Static` and `Dynamic` components.

> **Información**
> Multiple components can have the same category ID and dynamic ID as long as they're static parent differs

The following component types are available:

* Decorative: [Line](./decorative_components/line.md), [Rectangle](./decorative_components/rectangle.md), [Text](./decorative_components/text.md), [Sprite](./decorative_components/sprite.md), [Model](./decorative_components/model.md), [Model Group](./decorative_components/modelgroup.md)
* Interactive: [Button](./interactive_components/button.md), [Check](./interactive_components/check.md), [List](./interactive_components/list.md), [Input Field](./interactive_components/input_field.md), [Slider](./interactive_components/slider.md), [Combo Field](./interactive_components/combo_field.md), [Carousel](./interactive_components/carousel.md), [Radio Group](./interactive_components/radio_group.md)
* Layout: [Layer](./layout_components/layer.md), [Panel](./layout_components/panel.md), [Grid](./layout_components/grid.md) [Paged Layer](./layout_components/paged_layer.md), [Group Box](./layout_components/group_box.md), [Paged Carousel](./layout_components/paged_carousel.md)
* See also [Component](./component.md) and [Component Collection](./component_collection.md) for common methods and properties

## Interfaces

An interface represents a collection of static components, along with some additional information used for tracking their state. They're mainly an engine concept, and plugins simply use them as containers for their components.

See [here](./interface.md) for additional information on interfaces.

## Hojas de Estilo

Style sheets

See [here](./stylesheets.md) for additional information on style sheets as well as suggestions for what styles to use.