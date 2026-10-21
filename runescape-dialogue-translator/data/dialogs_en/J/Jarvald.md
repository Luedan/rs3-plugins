# Jarvald

- **Original Wiki Page**: [Transcript:Jarvald](https://runescape.wiki/w/Transcript%3AJarvald)
- **Letter**: `J`

---

## Dialogue Transcript


### Before The Fremennik Trials


#### In Rellekka


##### Talk-to

- **Jarvald:** What do you want from me outerlander? It is our policy not to associate with those not of our tribe.
- [Menu]: What would you like to ask about?
  - [Choice]: Where is your chieftain?
    - **Player:** Where is your chieftain? I find it highly discriminatory to refuse to talk to someone on the grounds that they are not part of your tribe.
    - **Jarvald:** I don't rightly understand your speech outerlander, but my loyalty is with Chieftain Brundt. He resides in our long hall; it is the large building over there, you should speak to him for he speaks for us all.
  - [Choice]: What Jarvald is doing.
    - **Player:** So what are you doing here?
    - **Jarvald:** This should not concern you, outerlander. I am awaiting other Fremenniks to join me on an expedition to Waterbirth Island.
    - [Menu]: Select an Option
      - [Choice]: Waterbirth Island?
        - **Jarvald:** It is a small crescent-shaped island just north-west of here, outerlander. We have many legends about it, such as the tale of the broken sky, and the day of the green seas. The reason I am travelling there is more serious Fremennik business, however. I doubt an outerlander would be interested.
      - [Choice]: Can I come?
        - (Condition: First time choosing this option:)
          - **Player:** Hey, scary barbarian type guy, think I can join you on this expedition?
          - **Jarvald:** An outerlander join us on an honoured hunt??? Well.... I guess... I might be able to allow you to join us, although it is a breach of many of our customs...
          - **Player:** Oh, pleeeeease? I really LOVE killing stuff!
          - **Jarvald:** Well... I remain unconvinced that it would be wise to allow an outerlander to join us in such dangerous battle, but your enthusiasm seems genuine enough... I will allow you to escort us, but you must pay me a sum of money first.
          - **Player:** What? That's outrageous, why charge me money? And, uh, how much does it cost me?
          - **Jarvald:** Ah, the outerlanders have stolen from my people for many years, in this way you can help my community with a small amount of money... Let us say... 1000 coins. Payable in advance, of course. For this I will take you to Waterbirth Island on my boat, and will bring you back here when you have had your fill of the hunt. Assuming you are still alive to wish to leave, of course.
        - {{anchor|pay-trip}}**Jarvald:** So do you have the 1000 coins for my service, and are you ready to leave now?
        - [Menu]: Select an Option
          - [Choice]: YES
            - (Condition: If the player does not have enough coins:)
              - You can not afford that.
              - **Jarvald:** Ah, outerlander... I go beyond my duty to allow you to accompany me, and you attempt to swindle me out of a reasonable fee? This is no way even for an outerlander to behave...
            - (Condition: If the player has enough coins:)
              - (removes=1,000 coins)
              - {{anchor|back-to-waterbirth}}Leaving Rellekka for Waterbirth Island.
              - {{qact|Screen fades out and then fades in. The player appears at Waterbirth Island, by the northeastern coast.}}
              - (Condition: First time travelling to Waterbirth Island:)
                - (Condition: If the player has not completed The Fremennik Trials:)}
                  - **Jarvald:** I suggest you head to the cave with some urgency outerlander, the cold air out here might be too much for the likes of you...
                - (Condition: If the player has completed The Fremennik Trials:)
                  - **Jarvald:** I would head straight for the cave and not tarry too long [Fremennik name], the cold winds on this island can cut right through you should you spend too long in them.
          - [Choice]: NO
            - {{anchor|decline-travel-waterbirth}}**Player:** No, actually I have some stuff to do here first.
            - **Jarvald:** As you wish. Come and see me when your bloodlust needs sating.
      - [Choice]: Nice hat!
        - **Player:** Hey, I have to say, that's a fine looking hat you are wearing there.
        - **Jarvald:** It is actually a helm, outerlander, but the sentiment is appreciated nonetheless.
      - [Choice]: Ok, 'bye.
        - {{anchor|know-how-to-party}}**Player:** Wow, you Fremenniks sure know how to party. Well, see ya around.
  - [Choice]: Nothing
    - {{anchor|nothing}}**Player:** Actually, I don't think I have anything to speak to you about...

##### Travel-Waterbirth


##### Before asking to travel to Waterbirth Island

- **Jarvald:** No, outerlander I am not taking you there.

##### After asking to travel to Waterbirth Island

- (above2|pay-trip)

#### On Waterbirth Island


##### Talk-to

- **Jarvald:** Ah, you live yet, outerlander! Have you had your fill of the hunt and wish to return, or are you still feeling the joy of the cull?
- {{anchor|leave-waterbirth}}[Menu]: Leave island?
  - [Choice]: Yes
    - **Jarvald:** Then let us away; There will be death to bring here another day!
    - {{anchor|back-to-rellekka}}Leaving Waterbirth Island for Rellekka.
    - {{qact|Screen fades out and then fades in. The player appears at Rellekka, by the northwesternmost dock.}}
  - [Choice]: No
    - **Jarvald:** Ha Ha Ha! A true huntsman at heart!
    - **Jarvald:** I myself have killed over a hundred of the daggermouths, and did not think it too many!

##### Travel-Rellekka

- (above2|back-to-rellekka)

### After The Fremennik Trials


#### In Rellekka


##### Talk-to

- **Jarvald:** Greetings, [Fremennik name]!
- (Condition: If the player's Fremennik name is Jarvald:)
  - **Jarvald:** Ah, and what a glorious name that is! Worthy of only the finest warriors!
  - **Player:** Heh. Yup, you're right there.
- **Jarvald:** So what brings you back to fair Rellekka? It has been too long since you have drunk in the long hall with us and sang of your battles!
- [Menu]: What would you like to ask about?
  - [Choice]: What Jarvald is doing.
    - **Player:** So what are you doing here?
    - **Jarvald:** You have not heard, [Fremennik name]? I am leading an expedition to Waterbirth Island!
    - {{anchor|expedition-options}}[Menu]: Select an Option
      - [Choice]: Waterbirth Island?
        - **Jarvald:** You have not ever travelled to Waterbirth Island, [Fremennik name]? I am surprised, it is a place of outstanding natural beauty.
        - **Jarvald:** Or at least it used to be! But things have now changed...
        - **Player:** Changed? How do you mean, changed?
        - **Jarvald:** It seems as though the sea-beasts known to us as the daggermouths have begun their hatching once again... And there may be others of their ilk there too.
        - **Player:** Daggermouths?
        - **Jarvald:** Aye, the daggermouths! The vile creatures lived near here once, but we had thought them all driven back to the ocean depths many moons past.
        - **Jarvald:** I can only imagine a daggermouth queen has nested somewhere nearby, and spawned her foul brood under the sea once more, and some of them have migrated to fair Waterbirth Island.
        - **Player:** So you're scared they might attack Rellekka?
        - **Jarvald:** Scared? Ha ha ha!
        - **Jarvald:** You wound us with your questioning, [Fremennik name]!
        - **Jarvald:** We are glad the daggermouths have returned to these shores, for it means we will get the chance to hunt them once again as our ancestors did!
        - **Jarvald:** When treated in the correct manner, the creatures' remains can be used to make fine battleworthy armour!
        - (other|expedition-options)
      - [Choice]: Can I come?
        - **Player:** Can I come?
        - **Jarvald:** Of course, [Fremennik name]! Your presence is more than welcome on this cull! You wish to leave now?
        - [Menu]: Select an Option
          - [Choice]: YES
            - (continuea|back-to-waterbirth)
          - [Choice]: NO
            - (continuea|decline-travel-waterbirth)
      - [Choice]: Nice hat!
        - **Player:** Hey, I have to say, that's a fine looking hat you are wearing there.
        - **Jarvald:** Aye, that it is [Fremennik name]! Skulgrimen fashioned it for me from the carcass of one of the monsters on Waterbirth Island after our last hunt! I hope to kill enough creatures to fashion some fine armour as well when next we leave!
        - (other|expedition-options)
      - [Choice]: Ok, 'bye.
        - (continuea|know-how-to-party)
  - [Choice]: Nothing
    - (continuea|nothing)

##### Travel-Waterbirth

- (above|back-to-waterbirth)

#### On Waterbirth Island


##### Talk-to

- **Jarvald:** Ah, [Fremennik name]! Such glorious battle makes you feel glad of life, does it not?
- **Jarvald:** So what say you, stay here for the hunt, or return home to sweet Rellekka to feast and drink with your tribe?
- (continuea|leave-waterbirth)

##### Travel-Rellekka

- (above|back-to-rellekka)
