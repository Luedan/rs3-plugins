# Fancy-dress shop owner

- **Original Wiki Page**: [Transcript:Fancy-dress shop owner](https://runescape.wiki/w/Transcript%3AFancy-dress%20shop%20owner)
- **Letter**: `F`

---

## Dialogue Transcript


### Standard dialogue

- **Fancy-dress shop owner:** Now you look like someone who goes to a lot of fancy dress parties.
- **Player:** Errr...what are you saying exactly?
- **Fancy-dress shop owner:** I'm just saying that perhaps you would like to peruse my selection of garments.
- **Fancy-dress shop owner:** Or, if that doesn't interest you, then maybe you have something else to offer? I'm always on the lookout for interesting or unusual new materials.
- [Menu]: Select an option
  - [Choice]: Okay, let's see what you've got, then.
    - **Player:** Okay, let's see what you've got, then.
    - (opens=Fancy Clothes Store)
  - [Choice]:  *(After Eagles' Peak:)* Could you make another bird costume for me?
    - **Player:** Could you make another eagle costume for me?
    - **Fancy-dress shop owner:** Certainly, if you can supply the materials. I'll need appropriate feathers, swamp tar and some yellow dye. It'll also cost you 25 gold pieces.
    - (Condition: If the player does not have the required items:)
      - **Player:** I'll see what I can do.
    - (Condition: If the player has the required items:)
      - [Menu]: Select an option
        - [Choice]: Okay, here are the materials. Eagle me up.
          - **Player:** Okay, here are the materials. Eagle me up.
          - (Condition: If the player has less than 25 coins:)
            - **Player:** I'm afraid I don't have that much money with me.
            - You can not afford that.
          - (Condition: If the player has 25 coins:)
            - (removes=10 eagle feathers, yellow dye, swamp tar and 25 coins) (receives=eagle cape and fake beak)
            - **Fancy-dress shop owner:** There we go, one eagle costume. You should be the envy of the entire party wearing that.
            - **Player:**  Thanks.
        - [Choice]: On second thoughts, that's too expensive.
          - **Player:** On second thoughts, that's too expensive.
          - **Fancy-dress shop owner:** Well, feel free to come back if you change your mind.
  - [Choice]: I think I might just leave the perusing for now thanks.
    - **Player:** I think I might just leave the perusing for now, thanks.
  - [Choice]: *(If you do not have suitable fur in your inventory:)* Can you make clothing suitable for hunting in?
    - **Player:** Can you make clothing suitable for hunting?
    - **Fancy-dress shop owner:** Certainly. Take a look at my range of made-to-order items. If you can supply the furs, I'll gladly make any of these for you.
    - (opens=Custom Fur Clothing)
  - [Choice]: *(If you have fur in your inventory:)* Could you make anything out of this fur that I got from hunting?
    - **Player:** Could you make anything out of this fur that I got from hunting?
    - **Fancy-dress shop owner:** Certainly. Take a look at my range of made-to-order items. If you can supply the furs, I'll gladly make any of these for you.
    - (opens=Custom Fur Clothing)
  - [Choice]: What sort of unusual materials did you have in mind?
    - **Player:** What sort of unusual materials did you have in mind?
    - **Fancy-dress shop owner:** Well, some more colourful feathers might be useful. For some surreal reason, all I normally seem to get offered are large quantities of rather beaten-up looking chicken feathers.
    - **Fancy-dress shop owner:** People must have some very strange pastimes around these parts, that's all I can say.
    - **Player:** Ok, let's see what you've got then.
    - (opens=Fancy Clothes Store)
