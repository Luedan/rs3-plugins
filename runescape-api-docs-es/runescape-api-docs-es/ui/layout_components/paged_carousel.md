# ui.PagedCarousel

## Descripción General

[ui.Component](./../component.md) -> [ui.ComponentCollection](./../component_collection.md) -> [ui.PagedLayer](./paged_layer.md) -> ui.PagedCarousel

These components are an extension of PagedLayer, with built-in controls for switching between the different pages, similarly to how a [ui.Carousel](./../interactive_components/carousel.md)'s buttons for switching between options.

PagedCarousels extend the concept of active/inactive pages, providing additional controls for inactive ones and allowing for multiple pages to be displayed simultaneously. These controls range from modifying the size to how much of an inactive page is visible, as well as transitions between active and inactive pages.

> **Información**
> Since paged carousels extend paged layers, they also support paged layer's header functionality, and page labels and icons can also be set even if those aren't displayed on the paged carousel instead.

## Ejemplo

```lua
-- Create a new paged carousel
local myPagedCarousel = ui.PagedCarousel.new(parent)
myPagedCarousel:SetSize(500, 500)
myPagedCarousel.stylesheetID = paged_carousel_full
myPagedCarousel.numPages = 3

-- We want only 50% of the inactive page contents to be visible, and for inactive pages to be 75% the size of the active one
myPagedCarousel.inactivePageVisibility = 0.5
myPagedCarousel.inactivePageScale = 0.75

-- Inactive pages can receive input
myPagedCarousel.inactivePageReceiveInput = false

myPagedCarousel.inactivePageFadeRegionSize = 20

myPagedCarousel:Subscribe(ui.Hook.ONSELECTIONCHANGED, function (comp, newPage) log("Switched to page", newPage) end)

-- Add a component to each page
for i=0,2 do
    -- Components are associated with the currently active page when created
    -- so we need to swap to the desired page first
    myPagedCarousel.activePage = i

    local c = ui.Rectangle.new(myPagedCarousel)
    c:SetSize(0, 0, 1.0, 1.0)
    c.colour = Vector4.new(1.0)
end
```

## Enumeraciones

### ui.CarouselButtonDisplayMode

Enumeration containing the various options for how the previous/next page carousel buttons should be displayed.

| Valor | Descripción |
| --- | --- |
| SIDES | Indicates the carousel's buttons should be displayed on its left and right sides. |

## Métodos

### Constructor

```lua
function ui.PagedCarousel.new(parent : ui.ComponentCollection, categoryID : Int?, dynamicID : Int?) -> PagedCarousel
```

Creates a new PagedCarousel on the specified parent.

> **Advertencia**
> Creating a component can fail if there's already a component on that parent with the same category ID and dynamic ID, or if those are omitted and the application is unable to generate a valid ID for the component.

| Parameter | Tipo | Descripción |
| --- | --- | --- |
| parent | [ui.ComponentCollection](./../component_collection.md) | Parent component to create this paged carousel in. |
| categoryID | Int? | Category ID used to identify this component.    Defaults to the parent's category ID if not specified. |
| dynamicID | Int? | Dynamic ID used to identify this component.    Defaults to auto-incrementing from the parent's dynamic ID if not specified. |

| Retorna | Descripción |
| --- | --- |
| PagedCarousel | The newly created paged carousel.    The caller must set its layout and visual information afterwards. |

## Propiedades

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| isSinglePageDisplay | Bool | **(Read-only)**   True if this paged carousel only displays one page at the time, with no others being partially visible. |
| numFullyVisiblePages | Int | **(Read-only)**   The number of pages that can be viewed in their entirety at the same time. |
| isSwitchingPages | Bool | ***(Read-only)**   True if a page switch animation is currently in progres. |
| pageSpacing | Int | Spacing in interface units between each displayed page. |
| inactivePageVisibility | Float | Indicates how many pages can be displayed besides the one currently in focus.   This value is symmetrical, so a value of 0.5 means 50% of the previous and 50% of the next page are visible.   Supports multiple pages, for example 1.5 results in one additional fully visible page to each side, followed by another 50% visible page on each side. |
| inactivePageScale | Float | Fractional height scaling used for inactive pages compared to the focused page.   Defaults to 1.0, the same size as the focused page.   Avoid using too high or too low values, as it may affect page contents negatively as well as cause issues with the transition animations. |
| inactivePageReceiveInput | Bool | Controls whether inactive pages can be interacted with.   Not recommended when `inactivePageVisibility` contains fractional values as it may be confusing to users. |
| inactivePageFadeRegionSize | Uint16 | Controls the width in interface units of the gradient fade on the left and right edges of the paged carousel.   Set to `0` to remove the fade effect. |
| buttonWidth | Uint16 | Width used for the previous/next page buttons. |
| buttonHeight | Uint16 | Height used for the previous/next page buttons. |
| buttonDisplayMode | [ui.CarouselButtonDisplayMode](#uicarouselbuttondisplaymode) | Controls how the previous/next buttons are displayed. |
| buttonSprite | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used for the previous/next buttons. |
| pageBackgroundSprite | [ui.SpriteData](./../common_types.md#uispritedata) | **(Modifiable Contents)**   Sprite properties used each page's background. |
| pageContentMargin | [ui.Margin](./../common_types.md#uimargin) | **(Modifiable Contents)**   Offsets used to determine the inner content area for each page. |