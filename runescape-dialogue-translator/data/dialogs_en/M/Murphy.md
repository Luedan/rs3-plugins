# Murphy

- **Original Wiki Page**: [Transcript:Murphy](https://runescape.wiki/w/Transcript%3AMurphy)
- **Letter**: `M`

---

## Dialogue Transcript


### Before playing Fishing Trawler

- **Player:** Good day to you Sir.
- **Murphy:** Well hello my brave adventurer.
- **Player:** What are you up to?
- **Murphy:** Getting ready to go fishing of course. There's no time to waste!
- **Murphy:** I've got all the supplies I need from the shop at the end of the pier. They sell good rope, although their bailing buckets aren't too effective.
- [Menu]: Choose an option:
  - [Choice]: What fish do you catch?
    - **Player:** What fish do you catch?
    - **Murphy:** I get all sorts, anything that lies on the sea bed, you never know what you're going to get until you pull up the net!
    - (other|initial-options)
  - [Choice]: Your boat doesn't look too safe.
    - **Player:** Your boat doesn't look too safe.
    - **Murphy:** That's because it's not, the darn thing's full of holes.
    - **Player:** Oh, so I suppose you can't go out for a while?
    - **Murphy:** Oh no, I don't let a few holes stop an experienced sailor like me. I could sail these seas in a barrel, I'll be going out soon enough.
    - (other|initial-options)
  - [Choice]: Could I help?
    - **Player:** Could I help?
    - **Murphy:** Well of course you can! I'll warn you though, the seas are merciless and without fishing experience you won't catch much.
    - **Murphy:** You need a fishing level of 15 or above to catch any fish on the trawler.
    - **Murphy:** On occasions the net rips, so you'll need some rope to repair it.
    - **Murphy:** Repairing the net is difficult in the harsh conditions so you'll find it easier with a higher Crafting level.
    - **Player:** Right...ok.
    - **Murphy:** There's also a slight problem with leaks.
    - **Player:** Leaks?!
    - **Murphy:** Nothing some swamp paste won't fix...
    - **Player:** Swamp paste?
    - **Murphy:** Oh, and one more thing... I hope you're a good swimmer?
    - [Menu]: Choose an option:
      - [Choice]: Actually, I think I'll leave it.
        - **Player:** Actually, I think I'll leave it.
        - **Murphy:** Bloomin' land lovers!!!
      - [Choice]: I'll be fine, let's go.
        - **Player:** I'll be fine, let's go.
        - **Murphy:** Aye aye! Meet me on board the trawler. I just need to get a few things together.
      - [Choice]: What's swamp paste?
        - **Player:** What's swamp paste?
        - **Murphy:** Swamp tar mixed with flour which is then heated over a fire.
        - **Player:** Where can I find swamp tar?
        - **Murphy:** Unfortunately the only supply of swamp tar is in the swamps below Lumbridge.

### After playing Fishing Trawler at least once


#### Before completing Recipe for Disaster:Freeing Pirate Pete

- **Player:** Hello again Murphy.
- **Murphy:** Good day to you land lover. Fancy hitting the high seas again?
- [Menu]: Select an Option
  - [Choice]: No thanks, I still feel ill from last time.
    - **Player:** No thanks, I still feel ill from last time.
    - **Murphy:** Hah! ...Softy.
  - [Choice]: We keep sinking! Can you give me some advice?
    - **Player:** We keep sinking! Can you give me some advice?
    - **Murphy:** Aye aye matey! We'll soon get you ship shape!
    - **Murphy:** You need a Fishing level of 15 or above to catch any fish on the trawler.
    - **Murphy:** On occasion the net rips, so you'll need some rope to repair it.
    - **Murphy:** Repairing the net is difficult in the harsh conditions so you'll find it easier with a higher Crafting level.
    - **Player:** Ah yes, got it.
    - **Murphy:** There's also a slight problem with leaks.
    - **Player:** Don't say!
    - **Murphy:** Nothing some swamp paste won't fix...
    - **Player:** Right so I need lots of swamp paste and plenty of rope. Thanks Murphy!
    - **Murphy:** If all else fails use a bailing bucket!
  - [Choice]: Yes, let's do it!
    - **Player:** Yes, let's do it!
    - (Condition: If the trawler is in port:)
      - **Murphy:** Aye aye! Meet me on board the trawler. I just need to get a few things together.
    - (Condition: If the trawler is at sea:)
      - **Murphy:** Aye aye! Meet me on board the trawler.
      - **Murphy:** Oh hang on. I'm already on a fishing trip with someone. You'll have to try back in a few minutes.
      - **Player:** How can you be here and on board the boat?!
      - **Murphy:** That's Game Magic son.
      - **Player:** What?!
      - **Murphy:** Never mind. Just try back later OK?

#### After completing Recipe for Disaster:Freeing Pirate Pete

- (Condition: If the player has lost their diving apparatus and fishbowl helmet:)
  - **Player:** Hello Murphy. Do you have a spare set of diving gear?
  - **Murphy:** Here you are. I'm sure the previous owner won't be needing this now, anyway.
  - (receives=diving apparatus and fishbowl helmet)
  - **Player:** Thanks!
  - **Player:** Wait... Why won't the previous owner be needing it?
  - **Murphy:** He... Erm...
  - **Murphy:** He's given up diving to follow his childhood dream of becoming a circus performer.
  - **Player:** That's it?
  - **Murphy:** Yep. He most definitely didn't die in a horrific diving incident whilst wearing that diving suit, anyway.
  - **Player:** ...
- (Condition: Otherwise:)
  - [Menu]: Select an Option
    - [Choice]: Go Diving.
      - (Condition: If the player has their diving apparatus and fishbowl helmet in bank:)
        - **Murphy:** Ahoy! Up for a dive today?
        - **Player:** Sadly no, I don't have my diving helmet or diving backpack with me.
        - **Murphy:** Ah well, can't be helped.
      - (Condition: If the player has their diving apparatus and fishbowl helmet in backpack:)
        - **Murphy:** Ahoy there! All set for a dive?
        - [Menu]: Select an Option
          - [Choice]: Yes, Let's go diving.
            - **Player:** Yes,  go diving.
            - (Condition: If a fishbowl helmet and diving apparatus are not equipped:)
              - **Murphy:** Well I can't take you out until you are properly geared up. We lost three diving parties that way!
              - **Player:** Ok, well I'll just put my diving helmet and diving backpack on.
            - (Condition: If the player's weight exceeds 27 kg:)
              - **Murphy:** Well that's the sort of spirit I like to see. However you are far too heavy to go diving right now.
              - **Player:** What do you mean?
              - **Murphy:** Well, I can't take you diving if you are carrying more than 27kg worth of equipment. We arrived at that number through trial and error, and the errors were not pretty let me assure you.
              - **Player:** So what can I do?
              - **Murphy:** Well, if you pop over to a bank and leave all your heavy equipment behind then I'll take you out. See you then!
            - (Condition: If the player has something equipped in the main- or off-hand slots and does not have at least two empty spaces in the backpack:)
              - **Murphy:** Well let's be...
              - **Murphy:** Err, how do you plan on swimming with your hands full?
              - **Player:** What do you mean?
              - **Murphy:** Well, when you hit the water you will start swimming. If you can't free up your hands by putting everything away then you will sink like a stone.
              - **Murphy:** All you have to do is have 2 spaces to store the items and you are good to go.
              - **Murphy:** Even if you aren't carrying a shield or weapon it's always handy to have some free space for an emergency.
              - **Murphy:** See you then!
            - (Condition: If the player is carrying a gnomeball:)
              - **Murphy:** Now, do you have a gnomeball on you?
              - **Player:** Yes, I do, why do you ask?
              - **Murphy:** Well you will need to leave them on the surface. They are so full of air that they will stop you diving properly.
              - **Player:** Right, I'll go put it in the bank.
            - (Condition: If the player has a pet cat following them:)
              - **Murphy:** You want that cat of yours to drown or something?
              - **Player:** You mean that you can't make them an adorable set of tiny diving gear?
              - **Murphy:** No. Just...no.
              - **Murphy:** I'm not taking you out for a dive with that cat following you.
              - **Murphy:** I'm not a cat person, and it'd have to stay on the ship while you were down.
            - (Condition: If the player has a pet cat in backpack:)
              - **Murphy:** You know, I can see your cat right there.
              - **Player:** What do you mean?
              - **Murphy:** I'm looking at it. See, it's just there in your bag!
              - **Murphy:** I'm not taking you out with that cat. I'm not some sort of cat-sitter, so go and put it somewhere safe, then come back.
              - **Player:** O'kay...
              - **Player:** I still think I should get some cat-sized diving gear...
            - (Condition: If the player has another pet or a familiar following them:)
              - **Murphy:** You seem to have something following you there, Player. I don't think they would react well to going underwater, so you'll have to leave them behind.
              - **Player:** Ok Murphy.
            - (Condition: If the player has another pet or a summoning pouch in backpack:)
              - **Murphy:** Ok, one last thing.
              - **Murphy:** Do you have any followers, familiars, Summoning Pouches or the like on you?
              - **Player:** Would that be a bad thing?
              - **Murphy:** Yes, those poor animals tend not to react well to water.
              - **Player:** Good point, I'll go drop them off where they can't be harmed.
            - (Condition: Otherwise:)
              - **Murphy:** Ok, let's be off then.
              - {{Qact|Screen fades out and then back in; Murphy and the player are on the deck of a ship.}}
              - **Player:** Ok, see you soon Murphy!
              - **Murphy:** Good luck, I'll weigh anchor. Climb up the chain to get aboard.
              - {{Qact|The player faces the railing and then jumps overboard. Screen fades out and then back in; the player is swimming underwater.}}
          - [Choice]: Not just yet.
            - **Player:** Not just yet.
            - **Murphy:** Ok, well I'll be here if you change your mind.
    - [Choice]: Talk about something else.
      - (above|Before completing Recipe for Disaster:Freeing Pirate Pete)

### Sextant dialogue

*After speaking with the Observatory professor about Treasure Trails*—*with a coordinate clue in inventory.*
- **Player:** Ahoy there!
- **Murphy:** Ahoy!
- **Player:** I'm trying to learn how to be a navigator.
- **Murphy:** Well, you've come to the right place, [my son/m'hearty]! What do you need to know?
- **Player:** The professor said that I need to have a sextant. Do you know where I can get one?
- **Murphy:** Hmm. I used to use a sextant when I was a young fella.
- **Player:** Do you still have it?
- **Murphy:** Aye.
- **Player:** Could I have it?
- **Murphy:** Aye.
- Murphy has given you his old sextant.
- **Player:** Don't you still need it?
- **Murphy:** I can tell from the taste of the sea spray where I am, [my son/m'hearty]!
- **Player:** Wow!
