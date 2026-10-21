# Benny

- **Original Wiki Page**: [Transcript:Benny](https://runescape.wiki/w/Transcript%3ABenny)
- **Letter**: `B`

---

## Dialogue Transcript


### In Varrock

- **Select an Option**
  - [Choice]: Can I have a newspaper, please?
    - **Player:** Can I have a newspaper, please?
    - **Benny:** Certainly, [Guv/Missus]. That'll be 50 gold pieces, please.
    - **Select an Option**
      - [Choice]: Sure, here you go. {{anchor|buy}}
        - (Condition: If the player does not have enough money:)
          - You can not afford that.
          - **Player:** Oh dear, I don't seem to have enough money with me.
          - **Benny:** Well, no cash, no paper. Live in ignorance.
        - (Condition: If the player has enough money:)
          - (removes=50 coins) (receives=newspaper)
          - {{RSFontAchievement|Read All About It}}
      - [Choice]: Uh, no thanks, I've changed my mind.
        - **Player:** No, thanks.
        - **Benny:** Ok, suit yourself. Plenty more fish in the sea.
  - [Choice]: How much does a paper cost?
    - **Player:** How much does a paper cost?
    - **Benny:** Just 50 gold pieces! An absolute bargain! Want one?
    - **Select an Option** {{anchor|yesno}}
      - [Choice]: Yes, please.
        - **Player:** Yes, please.
        - (continuea|buy)
      - [Choice]: No, thanks.
        - (above)
  - [Choice]: Varrock Herald? Never heard of it.
    - **Player:** Varrock Herald? Never heard of it.
    - **Benny:** For the illiterate amongst us, I shall elucidate. The Varrock Herald is a new newspaper. It is edited, printed and published by myself, Benny Gutenberg, and each edition promises to enthrall the reader with captivating
    - **Benny:** material! Now, can I interest you in buying one for a mere 50 gold ?
    - (continuea|yesno)
  - [Choice]: Anything interesting in there?
    - **Player:** Anything interesting in there?
    - **Benny:** Of course there is, mate. Packed full of thought provoking insights, contentious interviews and celebrity scandalmongering! An excellent read and all for just 50 coins! Want one?
    - (continuea|yesno)

#### Overhead dialogue

- **Benny:** {{RSChat|Varrock Herald, on sale here!}}
- **Benny:** {{RSChat|Get your Varrock Herald here!}}
- **Benny:** {{RSChat|Extra! Extra! Read all about it!}}

### In New Varrock

- **Select an Option**
  - [Choice]: Can I have a newspaper, please?
    - **Benny:**5 of your finest zemomarks.
    - **Select an Option**
      - [Choice]: Sure, here you go.
        - (Condition: If the player does not have five zemomarks:)
          - **Player:** I'm afraid I don't have enough money with me.
          - **Benny:** No cash, no herald! <br>I ain't handing out free fliers, guv.
          - (initial)
        - (Condition: If the player has five zemomarks:)
          - (removes=five zemomarks) (receives=Newspaper (New Varrock))
          - [Benny sells you a copy of the New Varrock Herald.]
          - (initial)
      - [Choice]: Uh, no thanks, I've changed my mind.
        - **Benny:**Suit yourself. Plenty more fish in the sea.
        - (initial)
  - [Choice]: How much does a paper cost?
    - **Benny:**Just 5 zemomarks! That wouldn't even get you a tongue-lolly nowadays. <br>Want one?
    - (initial)
  - [Choice]: New Varrock Herald? Never heard of it.
    - **Benny:** Allow me to elucidate, guv.
    - **Benny:**The New Varrock Herald is a new newspaper. It's edited, printed and published by myself, Benny Gutenburg...
    - **Benny:**...under the much appreciated guidance of the Zemouregal Publication & Corrections Commission.
    - **Benny:** Each edition promises to enthral{{Sic}} with captivating and educational material! <br>Now, can I interest you in one for a mere 5 zemomarks?
    - (initial)
  - [Choice]: Anything interesting in there?
    - **Benny:** Of course there is, mate. Packed full of thought-provoking insights, contentious interviews and celebrity scandalmongering!
    - **Benny:** A pageturner, all for just 5 zemomarks! Want one? Maybe two?
    - (initial)
  - [Choice]: Not interested.
    - **Benny:**Fine. Remain ignorant of current affairs. No skin off my nose.

#### Overhead dialogue

- **Benny:** {{RSChat|New Varrock Herald! Only 5 zemomarks!}}
- **Benny:** {{RSChat|Get your New Varrock Herald!}}
- **Benny:** {{RSChat|Selling V Herald 5zm!}}
- **Benny:** {{RSChat|Read all about it!}}
- **Benny:** {{RSChat|Come on guys, I'm on commission here!}}
