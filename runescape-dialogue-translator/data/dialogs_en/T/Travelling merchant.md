# Travelling merchant

- **Original Wiki Page**: [Transcript:Travelling merchant](https://runescape.wiki/w/Transcript%3ATravelling%20merchant)
- **Letter**: `T`

---

## Dialogue Transcript


### Arriving

- The travelling merchant has arrived at the hub!

### Talk to normally

- The merchant is too busy to talk right now.

### Talk to with Travelling Merchant Coupon

- **Travelling merchant:** Ah, I see you've got one of my coupons. Hand it over and I can dig out some recent stock for you.
- The merchant only tracks their stock from the last 30 days. What runedate would you like to view the stock for?
- ([runedate 30 days ago]-[runedate yesterday])
- ((If a too early runedate is input:))
  - **Travelling merchant:** I don't keep track of my stock from a day that long ago, sorry.
- ((If a valid runedate is input:))
  - **CONFIRMATION**
  - You are about to change the available stock to runedate [runedate] which contains the following:
  - - Uncharted island map
  - - [Random item 1]
  - - [Random item 2]
  - - [Random item 3]
  - Do you wish to continue?
    - Cancel
      - (end)
    - OK
      - (A coupon is used and Travelling Merchant's Shop opens with the selected runedate.)
- ((If the current runedate is input:))
  - **Travelling merchant:** I'm already showing you the stock for that day.
- ((If a too late runedate is input:))
  - **Travelling merchant:** These coupons don't give you access to my future stock, sorry.

### Talk to after changing the stock with Travelling Merchant Coupon

- **Travelling merchant:** Got everything you need? Do you want to see today's stock again?
- {{Colour|#FF0000|Warning:}} This will revert the stock back to today's runedate. Viewing recent stock will require another coupon.
- **VIEW TODAY'S STOCK?**
  - Yes.
    - (Travelling Merchant's Shop opens with the current runedate.)
  - No.
    - (end)

### Using magical feather on them


#### Without ancient scroll

- **Travelling merchant:** Interesting... Throw that here and I'll give you something in return!
- The merchant takes the feather, and in exchange gives you an ancient scroll.
- **Travelling merchant:** Maybe you can make better use of this junk.

#### With ancient scroll

- **Travelling merchant:** I don't need another one of those right now.

### Leaving

- The travelling merchant has departed...
