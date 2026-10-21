# Askeladden

- **Original Wiki Page**: [Transcript:Askeladden](https://runescape.wiki/w/Transcript%3AAskeladden)
- **Letter**: `A`

---

## Dialogue Transcript


### Rellekka


#### Talk-to


##### Before The Fremennik Trials

- **Player:** Hello there.
- **Askeladden:** Hey there, buddy. You're an outerlander, huh? I'm not really supposed to talk to you.
- **Player:** Why not?
- **Askeladden:** I dunno buddy. Some stupid tradition or other. We're always told not to talk to outerlanders unless the Chieftain has allowed it.
- **Player:** The Chieftain? Who is that?
- **Askeladden:** His names Brundt, buddy. He's a real boring guy. You can find him in the long hall there.
- **Player:** Can you take me to see him?
- **Askeladden:** Sorry buddy, I'm not allowed into the long hall. Don't worry, he's easy to spot. He's the one in the fancy helmet. Oh, and he only has one eye.
- **Player:** He's a cyclops?
- **Askeladden:** Nah, nah, nah... He just wears an eyepatch! Well, see ya around buddy!

##### After The Fremennik Trials

- **Player:** Hello again Askeladden.
- **Askeladden:** Hey buddy! That ain't my name no more! My new Fremennik name is Larravak! What's yours?
- **Player:** My Fremennik name is [Fremennik name].
- **Askeladden:** Ha! Ain't as good as my name buddy! So what can I do ya for?
- [Menu]: Choose an Option:
  - [Choice]: cond=After Hero's Welcome:|Ask about V
    - **Askeladden:** Yeah, sad that. I heard he's dead. Sounded like a good guy.
    - **Askeladden:** One day I'll be a hero just like him!
  - [Choice]: Ask about things to do
    - **Player:** So, Askeladd- sorry, Larravak; What is there to do around here now that we are both Fremenniks?
    - **Askeladden:** I guess you could do a bit of shopping. We got fresh fish at the docks, and some armour and weapons at Skulgrimen's place.
    - **Player:** Okay, thanks.
  - [Choice]: Ask for a new pet rock
    - **Player:** Can I have another pet rock? I lost mine...
    - **Askeladden:** Sure thing buddy! I'd say take better care of this one, but it's just a rock! I have hundreds of them! Go wild!

### Waterbirth Island


#### Talk-to


##### Before The Fremennik Trials

- **Player:** Hello there.
- **Askeladden:** Hey there, buddy.<br>You're an outerlander, huh?
- **Askeladden:** Didn't think old Jarvald would let an outerlander come kill daggermouths with him!
- **Player:** Well, obviously he did.<br>So what are you doing up here?
- **Askeladden:** Well buddy, let me tell you, killing those daggermouths is sure thirsty work!
- **Askeladden:** If you got a keg of beer on you I'll buy it off ya for 500 gold coins, buddy!
- **Askeladden:** Or if you got any animal parts, I'll trade ya something for 'em!
- (Condition: If the player does not have any kegs of beer nor any animal parts:)
  - **Player:** No... I don't have anything like that with me...
  - **Askeladden:** Well, I'm not going back down there until I get a drink buddy! Come see me if you find me a keg, I pay good money!
- (Condition: If the player has at least one keg of beer but no animal parts:)
  - **Askeladden:** Wanna sell me kegs of beer for 500 gold coins each outerlander?
  - **Player:** I don't know... Seems a little off to sell alcohol to a child...
  - **Askeladden:** Hey, don't judge our customs outerlander! Now do you want the cash or you want to bug me?
  - **Askeladden:** Now are ya gonna sell me some beer, or are you going to cry about it all day?
  - [Menu]: Would you like to sell your kegs of beer?
    - [Choice]: YES
      - **Askeladden:** You wanna sell me the lot buddy, or one at a time?
      - [Menu]: Select an Option
        - [Choice]: Sell all Kegs
          - (removes=all kegs of beer in backpack)
          - (receives=500 coins per keg of beer)
          - You sell Askeladden your Kegs of Beer.
        - [Choice]: Sell One Keg
          - (removes=keg of beer)
          - (receives=500 coins)
          - You sell Askeladden a Keg of Beer.
          - [Menu]: Sell another keg?
            - [Choice]: YES
              - (Condition: If the player does not have at least one keg of beer:)
                - **Player:** But I don't have any kegs of beer to sell...
              - (Condition: If the player has at least one keg of beer:)
                - (above|sell-one-keg1)
            - [Choice]: NO
              - (end)
    - [Choice]: NO
      - **Player:** No offence Askeladden, and it's not that I don't trust you...<br>Er, actually it is that I don't trust you.
      - **Askeladden:** Aw, buddy...<br>What did I ever do to you?
      - **Askeladden:** Well, if ya change your mind, I'm gonna be here waiting for a drink, buddy!
- (Condition: If the player has at least one animal part but no kegs of beer:)
  - **Askeladden:** I'll trade ya animal parts for cooked tuna, ya interested outerlander?
  - [Menu]: Would you like to trade animal parts for food?
    - [Choice]: YES
      - **Askeladden:** You wanna trade me the lot buddy, or just one type?
      - [Menu]: Select an Option
        - [Choice]: Trade all parts
          - (removes=all animal parts in backpack)
          - (receives=one tuna per animal part)
          - You trade Askeladden your animal parts for food.
        - [Choice]: Sell one type only
          - **Askeladden:** What ya selling buddy?
          - [Menu]: Select an Option
            - [Choice]: cond=If the player has at least one dagannoth hide:|Darkened Hides
              - (removes=all dagannoth hides in backpack)
              - (receives=one tuna per dagannoth hide)
              - You trade the parts for food.
            - [Choice]: cond=If the player has at least one fibula piece, ribcage piece, or skull piece:|Wallasalki Bones
              - (removes=all fibula pieces, ribcage pieces, and skull pieces in backpack)
              - (receives=one tuna per item)
              - You trade the parts for food.
            - [Choice]: cond=If the player has at least one circular hide, flattened hide, or stretched hide:|Lightened Hides
              - (removes=all circular hides, flattened hides, and stretched hides in backpack)
              - (receives=one tuna per item)
              - You trade the parts for food.
            - [Choice]: Nothing
              - (above|no-offence1)
    - [Choice]: NO
      - (above|no-offence1)
- (Condition: If the player has at least one keg of beer and at least one animal part:)
  - [Menu]: What would you like to trade?
    - [Choice]: Kegs for money
      - (above|sell-beer1)
    - [Choice]: Animal parts for food
      - (above|sell-hides1)
    - [Choice]: Nothing
      - (above|no-offence1)

##### After The Fremennik Trials

- **Askeladden:** Hi buddy! Or do ya want me to call ya [Fremennik name] now?
- [Menu]: Select an Option
  - [Choice]: Ask what Askeladden is doing here
    - **Player:** Askeladden, what on Gielinor are you doing up here? And by the way, the name is Player.
    - **Askeladden:** Sure thing, buddy!
    - **Askeladden:** I was down in that cave killing daggermouths! It was fun! But then I got thirsty, so came up here for a bit of a rest...
    - **Askeladden:** Hey buddy, I'll tell you what, if you got any kegs of beer on ya, I'll buy them off ya for 700 gold coins each!
    - **Askeladden:** If ya found any animal parts killing daggermouths I'll trade ya for them too!
    - (Condition: If the player does not have any kegs of beer nor any animal parts:)
      - **Player:** No... I don't have anything like that with me...
      - **Askeladden:** Well, I'm not going back down there until I get a drink buddy! Come see me if you find me a keg, I pay good money!
    - (Condition: If the player has at least one keg of beer but no animal parts:)
      - **Askeladden:** Wanna sell me kegs of beer for 700 gold coins each buddy?
      - **Player:** Um... Aren't you a little... ...young to be drinking so much?
      - **Askeladden:** Hey, don't talk to me like that buddy! I've done all the trials you have and I'm just as much a Fremennik as you are!
      - **Askeladden:** Now are ya gonna sell me some beer, or are you going to cry about it all day?
      - [Menu]: Would you like to sell your kegs of beer?
        - [Choice]: YES
          - **Askeladden:** You wanna sell me the lot buddy, or one at a time?
          - [Menu]: Select an Option
            - [Choice]: Sell all Kegs
              - (removes=all kegs of beer in backpack)
              - (receives=700 coins per keg of beer)
              - You sell Askeladden your Kegs of Beer.
            - [Choice]: Sell One Keg
              - (removes=keg of beer)
              - (receives=700 coins)
              - You sell Askeladden a Keg of Beer.
              - [Menu]: Sell another keg?
                - [Choice]: YES
                  - (Condition: If the player does not have at least one keg of beer:)
                    - **Player:** But I don't have any kegs of beer to sell...
                  - (Condition: If the player has at least one keg of beer:)
                    - (above|sell-one-keg)
                - [Choice]: NO
                  - (end)
        - [Choice]: NO
          - **Player:** No offence Askeladden, and it's not that I don't trust you... Er, actually it is that I don't trust you.
          - **Askeladden:** Aw, buddy... What did I ever do to you?
          - **Askeladden:** Well, if ya change your mind, I'm gonna be here waiting for a drink, buddy!
    - (Condition: If the player has at least one animal part but no kegs of beer:)
      - **Askeladden:** I'll trade ya animal parts for cooked lobsters if ya interested buddy!
      - [Menu]: Would you like to trade animal parts for food?
        - [Choice]: YES
          - **Askeladden:** You wanna trade me the lot buddy, or just one type?
          - [Menu]: Select an Option
            - [Choice]: Trade all parts
              - (removes=all animal parts in backpack)
              - (receives=one lobster per animal part)
              - You trade Askeladden your animal parts for food.
            - {{topt|Sell one type only}}
              - **Askeladden:** What ya selling buddy?
              - {{tselect|Select an Option}}
                - {{topt|cond=If the player has at least one dagannoth hide:|Darkened Hides}}
                  - (removes=all dagannoth hides in backpack)
                  - (receives=one lobster per dagannoth hide)
                  - You trade the parts for food.
                - [Choice]: cond=If the player has at least one fibula piece, ribcage piece, or skull piece:|Wallasalki Bones
                  - (removes=all fibula pieces, ribcage pieces, and skull pieces in backpack)
                  - (receives=one lobster per item)
                  - You trade the parts for food.
                - [Choice]: cond=If the player has at least one circular hide, flattened hide, or stretched hide:|Lightened Hides
                  - (removes=all circular hides, flattened hides, and stretched hides in backpack)
                  - (receives=one lobster per item)
                  - You trade the parts for food.
                - [Choice]: Nothing
                  - (above|no-offence)
        - [Choice]: NO
          - (above|no-offence)
    - (Condition: If the player has at least one keg of beer and at least one animal part:)
      - [Menu]: What would you like to trade?
        - [Choice]: Kegs for money
          - (above|sell-beer)
        - [Choice]: Animal parts for food
          - (above|sell-hides)
        - [Choice]: Nothing
          - (above|no-offence)
  - [Choice]: Ask for a new pet rock
    - **Player:** Can I have another pet rock? I lost mine...
    - (receives=pet rock)
    - **Askeladden:** Well it's sure a weird place to ask for it buddy, but I have hundreds of them! Go wild!
