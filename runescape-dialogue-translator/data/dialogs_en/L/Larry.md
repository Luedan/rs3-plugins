# Larry

- **Original Wiki Page**: [Transcript:Larry](https://runescape.wiki/w/Transcript%3ALarry)
- **Letter**: `L`

---

## Dialogue Transcript


### In Ardougne Zoo


#### Before talking to Larry about Penguin Hide and Seek

- [Menu]: I want to speak to Larry about:
  - [Choice]: Cold War
    - (Condition: Without level 10 Hunter:)
      - [You need to be level 10 Hunter to start this quest.]
    - (Condition: With level 10 Hunter:)
      - [You need to be level 30 Agility to start this quest.]
      - **Larry:** I'm looking for an experienced adventurer and you're not it. Come back when you are more capable.
    - (Condition: With level 30 Agility:)
      - [You need to be level 34 Construction to start this quest.]
      - **Larry:** I'm looking for an experienced adventurer and you're not it. Come back when you are more capable.
  - [Choice]: Penguin Hide and Seek
    - **Larry:** What do you want?
    - **Player:** Uh, I just wanted to as-
    - **Larry:** SHHHHHH! They're listening. Keep your voice down.
    - **Player:** *whispers* Who's listening?
    - **Larry:** Never mind.
    - **Larry:** Are you the inquisitive sort? Are you willing to go on an expedition for me?
    - **Player:** What would I need to do on this expedition?
    - **Larry:** The zoo has granted me permission to study penguins abroad. It's my, er...understanding that there are many penguins located around the world.
    - **Player:** Why do you want to find penguins around the world?
    - **Larry:** I need to see if they're organis-, I mean, if they're migrating or something like that.
    - **Player:** You think they're organised? They're just penguins!
    - **Larry:** Do not underestimate them! They're clever and tricky and LISTENING! I know they're up to something.
    - **Larry:** That's why I'm recruiting brave adventurers to find these penguins and tell me of their locations.
    - **Player:** Well, I don't think they're organised, but I do travel all over the world. I could give you a hand finding them. What do I need to do?
    - **Larry:** Whenever you spot a penguin, spy on it. They're well trained and will change their positions every week, so keep your eyes peeled.
    - **Larry:** I'll give you a device that can track the penguin spies and offer you hints on their locations. Penguins are worth between 1 and 3 Penguin Points depending how difficult they are to find.
    - **Larry:** Report back here and I will reward you for your efforts.
    - **Player:** Great, I'll get started right away.
    - (Condition: Without space in backpack:)
      - **Larry:** I need to give you a device but you don't have any space. Come and talk to me once you have made space, or you can claim one from the shop.
    - (Condition: With space in backpack:)
      - **Larry:** Hold on, there. Take this device.
      - (receives=penguin spy device)
      - [Larry hands you a penguin spy device.]
      - **Larry:** You should take this device for spying on the penguins. It should come in handy as it has a number of useful functions that will help you on your mission.
      - **Larry:** First, it will provide hints to all the penguin locations. It can't get an exact lock on, but it should give you the general area to begin your search.
      - **Larry:** Once you're in the area, you can start a scan which will search your immediate vicinity and identify any penguins nearby.
      - **Larry:** As you spot more penguins, I will be offer an upgrade to the scan range and a new zap function which will freeze any penguins in place.

#### After talking to Larry about Penguin Hide and Seek

- [Menu]: I want to speak to Larry about:
  - [Choice]: Cold War
    - (above)
  - [Choice]: Penguin Hide and Seek
    - **Larry:** Do you have news? Have you found more?
    - (Condition: If the player is receiving the penguin spy device for the first time:)
      - **Larry:** You should take this device for spying on the penguins. It should come in handy as it has a number of useful functions that will help you on your mission.
      - **Larry:** First, it will provide hints to all the penguin locations. It can't get an exact lock on, but it should give you the general area to begin your search.
      - **Larry:** Once you're in the area, you can start a scan which will search your immediate vicinity and identify any penguins nearby.
      - **Larry:** As you spot more penguins, I will be offer an upgrade to the scan range and a new zap function which will freeze any penguins in place.
      - (Condition: Without space in backpack:)
        - **Larry:** It looks like your backpack is full. Don't worry, I'll hold on to this for you. After all, you never know where the next penguin could come from!
        - (continue|standard)
      - (Condition: With space in backpack:)
        - (receives=penguin spy device)
        - [Larry hands you a penguin spy device.]
        - (continue|standard)
    - (Condition: If the player has lost the penguin spy device:)
      - **Larry:** Wait! Where if your spy device? Did it fall into enemy hands?
      - **Player:** I only turned around for a second...
      - **Larry:** You're lucky these as easy to make. Just a bit of tin foil and we're ready to go.
      - (Condition: Without space in backpack:)
        - **Larry:** It looks like your backpack is full. Don't worry, I'll hold on to this for you. After all, you never know where the next penguin could come from!
        - (continue|standard)
      - (Condition: With space in backpack:)
        - (receives=penguin spy device)
        - [Larry hands you a penguin spy device.]
        - (continue|standard)
    - [Menu]: Select an Option
      - [Choice]: I've found more penguins.
        - **Player:** I've found more penguins.
        - **Larry:** More? They're spreading so quickly.
        - (Condition: First time after spying on a penguin:)
          - **Player:** That's not all! I discovered there are secret agent penguins that have started to appear across Gielinor as well!
          - **Larry:** Prawn crackers! Surely not? I heard the whispers but I never believed they would have reached this stage already.
          - **Player:** What should we do about them?
          - **Larry:** Let's just keep tracking them for now. They have to slip up eventually.
          - **Player:** Because of the ice, right?
          - **Larry:** This isn't a laughing matter, Player! Pay attention or who knows what may happen to you!
          - **Player:** Sorry. Full focus from now on.
          - (continue)
        - **Player:** I've found [number] penguin[s] this week.
        - (Condition: With points to spend:)
          - **Larry:** Great! You have [number] points to spend. Perhaps you should think about claiming your reward.
          - (continue)
        - (Condition: Without points to spend:)
          - **Larry:** You've found a lot of spies. But, you have no penguin points saved up. Keep looking!
          - (continue)
        - [Menu]: Select an Option
          - [Choice]: I'm having trouble finding the penguins, can I have a hint?
            - (below|hint)
          - [Choice]: What do I need to do again?
            - (below|explain-again)
          - [Choice]: Never mind.
            - (below|nevermind)
      - [Choice]: I'm having trouble finding the penguins; can I have a hint?{{anchor|hint}}
        - **Player:** I'm having trouble finding the penguins; can I have a hint?
        - ((One of the following is shown, depending on the location of the penguins:))
          - **Larry:** I've heard there's a penguin located around a village between a great tower and a vampyre's manor.
          - **Larry:** I've heard there's a penguin located around Ardougne.
          - **Larry:** I've heard there's a penguin located around Feldip Hills, near Gu'Tanoth.
          - **Larry:** I've heard there's a penguin located around the Al Kharid region, north of Shantay Pass.
          - **Larry:** I've heard there's a penguin located around the Ice Mountain region.
          - **Larry:** I've heard there's a penguin located between the Fremenniks and the Barbarians.
          - **Larry:** I've heard there's a penguin located deep in the jungle.
          - **Larry:** I've heard there's a penguin located east of the Mage Training Arena.
          - **Larry:** I've heard there's a penguin located in a city of plagues within the desert.
          - **Larry:** I've heard there's a penguin located in a town of druids.
          - **Larry:** I've heard there's a penguin located in or around Falador.
          - **Larry:** I've heard there's a penguin located in the east of the kingdom of Kandarin.
          - **Larry:** I've heard there's a penguin located in the fairy realm.
          - **Larry:** I've heard there's a penguin located in the frozen wastes.
          - **Larry:** I've heard there's a penguin located in the north of the kingdom of Misthalin.
          - **Larry:** I've heard there's a penguin located in the south of the kingdom of Misthalin.
          - **Larry:** I've heard there's a penguin located in the north of the Kharidian desert.
          - **Larry:** I've heard there's a penguin located in the south of the Kharidian desert.
          - **Larry:** I've heard there's a penguin located in the west of the kingdom of Kandarin.
          - **Larry:** I've heard there's a penguin located in the wilderness.
          - **Larry:** I've heard there's a penguin located near a big tree surrounded by short people.
          - **Larry:** I've heard there's a penguin located near a mountain of wolves.
          - **Larry:** I've heard there's a penguin located near a tainted swamp.
          - **Larry:** I've heard there's a penguin located near a town of werewolves.
          - **Larry:** I've heard there's a penguin located near some ogres in South Feldip Hills.
          - **Larry:** I've heard there's a penguin located near the Barbarian Outpost.
          - **Larry:** I've heard there's a penguin located near the bees and flax.
          - **Larry:** I've heard there's a penguin located near the Castle of Arthur.
          - **Larry:** I've heard there's a penguin located near the city of ghosts.
          - **Larry:** I've heard there's a penguin located near the coast, east of Ardougne.
          - **Larry:** I've heard there's a penguin located near the island of Dragontooth.
          - **Larry:** I've heard there's a penguin located near the pointy-eared ones.
          - **Larry:** I've heard there's a penguin located near Port Sarim.
          - **Larry:** I've heard there's a penguin located near the mudskippers.
          - **Larry:** I've heard there's a penguin located north of Ardougne.
          - **Larry:** I've heard there's a penguin located on a large crescent island.
          - **Larry:** I've heard there's a penguin located on an island, etc.
          - **Larry:** I've heard there's a penguin located on islands where brothers quarrel.
          - **Larry:** I've heard there's a penguin located somewhere beyond detection.
          - **Larry:** I've heard there's a penguin located somewhere in Gielinor.
          - **Larry:** I've heard there's a penguin located south of Ardougne.
          - **Larry:** I've heard there's a penguin located west of Ardougne, in the hills.
          - **Larry:** I've heard there's a penguin located west of Varrock.
          - **Larry:** I've heard there's a penguin located where banana smugglers dwell.
          - **Larry:** I've heard there's a penguin located where bloodsuckers rule.
          - **Larry:** I've heard there's a penguin located where eagles fly.
          - **Larry:** I've heard there's a penguin located where fishers colonise.
          - **Larry:** I've heard there's a penguin located where monkeys rule.
          - **Larry:** I've heard there's a penguin located where no weapons may go.
          - **Larry:** I've heard there's a penguin located where pirates feel mostly harmless.
          - **Larry:** I've heard there's a penguin located where the big-eyed goblins dwell.
          - **Larry:** I've heard there's a penguin located where the dwarves dig deep.
          - **Larry:** I've heard there's a penguin located where the Fremennik 'heim' and seek.
          - **Larry:** I've heard there's a penguin located where the Imperial Guard train.
          - **Larry:** I've heard there's a penguin located where wizards study.
      - [Choice]: I want to claim my reward.
        - (opens=Spy Club)
      - [Choice]: What do I need to do again?{{anchor|explain-again}}
        - **Player:** What do I need to do again?
        - **Larry:** Weren't you listening the first time? Fine, I'll explain it again, but pay attention this time.
        - **Larry:** There are spies everywhere. I'm recruiting brave adventurers to find these penguins and tell me of their locations.
        - **Larry:** Whenever you spot a penguin, spy on it. They're well trained and will change their positions every week, so keep your eyes peeled.
        - **Larry:** I gave you a device that can track the penguin spies and offer you hints on their locations. Penguins are worth between 1 and 3 Penguin Points depending how difficult they are to find.
        - **Larry:** Report back here and I will reward you for your efforts.
        - (Condition: If Lunar Diplomacy is not completed:)
          - **Larry:** One last thing. If you ever discover a place called Lunar Isle, you might gain access to a spell that will help you get in touch with me from anywhere in the world. I can't say any more that that, there may be spies nearby.
      - [Choice]: Never mind.{{anchor|nevermind}}
        - **Player:** Never mind.
        - **Larry:** FINE. Be that way.

#### Tuxedo-time


##### Before Cold War

- **Larry:** I can't talk about that right now.

##### After Cold War

- **Larry:** I can't do that right now.

#### Hide-n-Seek


##### Before talking to Larry about Penguin Hide and Seek

- **Larry:** What do you want?
- (above|shhhh)

##### After talking to Larry about Penguin Hide and Seek

- ((Spy Club reward interface opens.))
