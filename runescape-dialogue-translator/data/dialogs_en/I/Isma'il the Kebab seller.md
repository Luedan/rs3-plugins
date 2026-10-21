# Isma'il the Kebab seller

- **Original Wiki Page**: [Transcript:Isma'il the Kebab seller](https://runescape.wiki/w/Transcript%3AIsma%27il%20the%20Kebab%20seller)
- **Letter**: `I`

---

## Dialogue Transcript


### Before The Feud

- **Player:** Hello.
- **Isma'il the Kebab seller:** Hello. What can I do for you?
- **Player:**  I don't know, what can you do for me?
- **Isma'il the Kebab seller:** Well, that depends.
- **Player:** Depends on what?
- **Isma'il the Kebab seller:** It depends on whether you like kebabs or not.
- **Player:** Why is that?
- **Isma'il the Kebab seller:** Seeing as I'm in the kebab construction industry, I mainly help people in need of a kebab.
- **Player:** Well then, what kind of kebabs do you, er, construct?
- **Isma'il the Kebab seller:** I offer two different types of kebabs: the standard run-of-the-mill kebab seen throughout Gielinor and enjoyed by many an intoxicated dwarf, and my speciality, the extra-hot kebab. So which shall it be?
- **Isma'il the Kebab seller:** Or are my services even required?
- [Menu]: Select an Option
  - [Choice]: I want a kebab, please.
    - **Player:**  I want a kebab, please.
    - **Isma'il the Kebab seller:** That will be three gold coins please.
    - (Condition: If the player does not have 3 coins:)
      - **Player:** I seem to have not brought enough money with me. Sorry.
      - You can not afford that.
    - (Condition: If the player has 3 coins:)
      - (removes=3 coins) (receives=kebab)
      - **Isma'il the Kebab seller:** Here you go.
      - **Player:** Thanks.
      - **Isma'il the Kebab seller:** Is there anything else I can do for you?
      - {{anchor|else}} [Menu]: Select an Option
        - [Choice]: Yes, thanks.
          - (initial)
        - [Choice]: No thanks, I'm good.
          - **Player:**No thanks, I'm good.
          - **Isma'il the Kebab seller:** Come back soon, I could do with a few more customers.
  - [Choice]: Could I have an extra-hot kebab please?
    - **Player:** Could I have one of those crazy hot kebabs of yours.
    - **Isma'il the Kebab seller:** A super kebab it is so. Be careful, they really are as hot as they're made out to be.
    - **Player:** Sure, sure.
    - (Condition: If the player does not have 5 coins:)
      - **Player:** I seem to have not brought enough money with me. Sorry.
      - You can not afford that.
    - (Condition: If the player has 5 coins:)
      - (removes=5 coins) (receives=super kebab)
      - **Isma'il the Kebab seller:** Here you go.
      - **Player:** Thanks.
      - **Isma'il the Kebab seller:** Is there anything else I can do for you?
      - (continuea|else)
  - [Choice]: Would you sell me that bottle of special kebab sauce?
    - **Player:** Would you sell me that bottle of special kebab sauce?
    - **Isma'il the Kebab seller:** Well, that depends on what you have in mind.
    - **Player:** Set yourself at ease, I have no intention of setting up a rival kebab shop.
    - **Isma'il the Kebab seller:** Well then, what do you want it for?
    - **Player:** I don't know, but I think I could have a little bit of fun with it.
    - **Isma'il the Kebab seller:** You're not going to put it in Jalal the Drunk's drink, are you? That's what happened the last time I gave someone the sauce.
    - **Player:** No, that would be a bit cliché. I think I'll come up with something more original.
    - (Condition: If the player does not already have the red hot sauce in backpack or in bank:)
      - (receives=Red hot sauce)
      - **Isma'il the Kebab seller:** Just be careful with it, it's potent enough to give a camel the runs.
      - **Player:** Thank you very much.
      - **Isma'il the Kebab seller:** Is there anything else I can do for you?
      - (continuea|else)
    - (Condition: If the player already has the red hot sauce in backpack:)
      - **Isma'il the Kebab seller:** I don't think I will give you it, for the simple fact that you already have one sticking out of your bag. I have to run a business here.
      - **Isma'il the Kebab seller:** Is there anything else I can do for you?
      - (continuea|else)
    - (Condition: If the player already has the red hot sauce in bank:)
      - **Isma'il the Kebab seller:** Didn't I just give you a bottle of this already?
      - **Player:** You might have. Any chance of another?
      - **Isma'il the Kebab seller:** I'm trying to run a business here, not a charity.
      - **Isma'il the Kebab seller:** Is there anything else I can do for you?
      - (continuea|else)
  - [Choice]: What is the difference between the standard and the extra-hot kebab?
    - **Player:** What is the difference between the standard and the extra-hot kebab?
    - **Isma'il the Kebab seller:** If I told you that I would have to kill you. Kebab sales is a cut-throat industry. The extra-hot kebab gives me the competitive edge on the rest and if I were to divulge my secrets to every passing adventurer, well it would soon disappear.
    - **Player:** So there's no difference except the sauce you use then!
    - **Isma'il the Kebab seller:** Shh! Keep your voice down. You should have told me you were from the union.
    - [Menu]: Select an Option
      - [Choice]: I want a kebab, please.
        - (above)
      - [Choice]: Could I have an extra-hot kebab please?
        - (above)
      - [Choice]: Would you sell me that bottle of special kebab sauce?
        - (above)
      - [Choice]: Listen I've got to run. I'll catch you later.
        - **Player:** Listen I've got to run. I'll catch you later.

### After The Feud

- **Player:** Hello.
- **Isma'il the Kebab seller:** Hello. What can I do for you?
- [Menu]: Select an Option
  - [Choice]: I want a kebab, please.
    - (above)
  - [Choice]: Could I have an extra-hot kebab?
    - (above)
  - [Choice]: Would you sell me that bottle of special kebab sauce?
    - (above)
  - [Choice]: What is the difference between the standard and the extra-hot kebab?
    - (above)
  - [Choice]: I need some information.
    - **Player:** I need some information.
    - **Isma'il the Kebab seller:** If information is what you need, there are many better people to ask than myself who could help you. One of the town's street urchins or perhaps the local drunk. I may be many things to many different people, but a gossip I am not.
    - **Isma'il the Kebab seller:** Is there anything else I can do for you?
    - {{anchor|else2}} [Menu]: Select an Option
      - [Choice]: Yes, thanks.
        - **Player:** Yes, thanks.
        - (initial)
      - [Choice]: No thanks, I'm good.
        - **Player:**No thanks, I'm good.
