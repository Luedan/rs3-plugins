# Farmer Blinkin

- **Original Wiki Page**: [Transcript:Farmer Blinkin](https://runescape.wiki/w/Transcript%3AFarmer%20Blinkin)
- **Letter**: `F`

---

## Dialogue Transcript

- **Farmer Blinkin:** 'Ello there! Welcome to Winkin's Farm. What can I do for ya?
- [Menu]: Select an option
  - [Choice]: What is this place?
    - **Player:** What is this place?
    - **Farmer Blinkin:** Ha! I told ya, it's Winkin's Farm. This is where we grow the magical ogleroots for the rest of the world.
    - **Player:** So, what can I do here?
    - **Farmer Blinkin:** Ya can improve yer Farming skill by getting some flags from me or Mrs. Winkin, inside. Then, head out to the fields and flag where ya think plants are, er, planted.
    - **Player:** Is that it?
    - **Farmer Blinkin:** Not at all! There's more. When ya've placed yar flags, the farmers will collect them up and give out points. Ya can trade these points for seeds or experience at the shop inside.
    - **Player:** Okay, that sounds great! I'll get planting, then.
    - **Farmer Blinkin:** Aye, but be careful where ya plant the flags. If there's no plant under yar flag, the farmer will keep it and they cost a pretty penny to buy more.
    - **Player:** I see. Thanks for the help.
    - **Farmer Blinkin:** Bye, for now. If I have to say 'flag' one more time, I tell ya...
  - [Choice]: Do you have any flags?
    - **Player:** Do you have any flags?
    - **Farmer Blinkin:** Let me check for ya.
    - (Condition: If it is the first time:)
      - **Farmer Blinkin:** Arr, a new'un, eh? Aye, it's always good to see a new face round these parts. Now, usually we charge for flags, since so many go missing - but ya can have yar first set for free.
      - **Player:** Wow, thanks!
      - **Farmer Blinkin:** Now, remember: if ya plant the flags in any old place that don't have seeds in it, ya'll lose yer flag - and they ain't cheap to buy back from me or Mrs. Winkin. Anyway, here's yer first lot.
      - (receives=10 flags)
      - **Player:** Thanks very much! I'll be off, then.
      - **Farmer Blinkin:** Bye now.
    - (Condition: If the player can claim free flags:)
      - **Farmer Blinkin:** Ah! First things first. One of the farm lads dropped off some flags for ya. Ya can have them back. Here ya go.
    - (Condition: If the player can buy flags:)
      - **Farmer Blinkin:** Righty-ho! Ya can have a total of 10 flags. To get yerself a full set of flags'll cost ya [number] gold pieces. Would ya like to buy these flags?
      - [Menu]: Select an option
        - [Choice]: Yes, please.
          - **Player:** Yes, please.
          - [number] coins have been removed from your money pouch.
          - **Farmer Blinkin:** Here ya go, then.
        - [Choice]: No, thanks.
          - **Player:** No, thanks.
          - **Farmer Blinkin:** Right y'are then! See ya.
    - (Condition: If the player has 10 flags (either before talking to Farmer Blinkin or by claiming/buying flags):)
      - **Farmer Blinkin:** It looks like ya got all the flags ya need right now. Ya don't need to buy any more.
  - [Choice]: Where is Mr. Winkin?
    - **Player:** Where is Mr. Winkin?
    - **Farmer Blinkin:** Farmer Winkin? Well, last I 'eard he was heading into market with a fresh load of Ogleroots.
    - **Player:** Ogleroots?
    - **Farmer Blinkin:** Aye! We get them growing a lot here in the farmyard. We dig 'em up and sell 'em to yar lot.
    - **Player:** My lot?
    - **Farmer Blinkin:** Aye! Humans.
    - **Player:** Oh, I see. Thanks!
    - **Farmer Blinkin:** Bye now!
