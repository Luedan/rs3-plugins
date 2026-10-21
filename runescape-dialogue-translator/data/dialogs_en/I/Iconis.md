# Iconis

- **Original Wiki Page**: [Transcript:Iconis](https://runescape.wiki/w/Transcript%3AIconis)
- **Letter**: `I`

---

## Dialogue Transcript


### On free-to-play worlds

- **Iconis:** Good day! I'm afraid you can't use the booth's services on a non-members world. Film costs a lot you know!

### On members' worlds

- **Iconis:** Good day! Would you like to have your picture taken?
- [Menu]: Select an Option
  - [Choice]: Yes, please!
    - **Player:** Yes please!
    - (Condition: If the player hasn't taken a picture in the last two hours:)
      - **Iconis:** Just enter the tent, adjust your clothing and press the 'Take picture' button when you're ready!
      - **Player:** Thank you!
      - {{Qact|The player enters the photo booth.}}
    - (Condition: If the player has taken a picture in the last two hours:)
      - **Iconis:** Sorry, you've only recently had your picture taken. You'll be able to have it taken again in [time remaining].
  - [Choice]: No, thank you.
    - **Player:** No, thank you.
    - **Iconis:** As you wish.
  - [Choice]: What are the pictures for?
    - **Player:** What are the pictures for?
    - **Iconis:** The imp sends them to a mysterious web that can be found beyond this material plane. From there, they can be viewed by other adventurers to put a face to the name.
    - **Iconis:** For example, they'll be used to display the faces of adventurers with high skill training accomplishments.
    - [Menu]: Select an Option
      - [Choice]: How does it work?
        - (below|work)
      - [Choice]: Is it safe?
        - (below|safe)
  - [Choice]: How does it work?
    - {{anchor|work}} **Player:** How does it work?
    - **Iconis:** There's an imp in there who uses a spell to take your picture. He can only do it once every 2 hours at the moment, though, and it will take some time to process the picture. There's a lot of demand, you see.
    - [Menu]: Select an Option
      - [Choice]: Why an imp?
        - **Player:** Why an imp?
        - **Iconis:** Ah, good question! See, I've experimented with lots of ways of making accurate visual representations of things in a magical way. Most recently, I've been trying to modify scrying orbs to get a still picture.
        - **Iconis:** Because of their shape, though, they always made the subject look fat! So I came up with a scrying cube, but that made things look even worse!
        - **Player:** So what did you do?
        - **Iconis:** I tweaked and tweaked the shape until I got a decent picture - took me weeks to make - but then this imp just teleported in from out of nowhere right next to it. My scrying device fell on the floor and smashed.
        - [Menu]: Select an Option
          - [Choice]: Oh, no!
            - **Player:** Oh, no!
            - {{anchor|ohno}} **Iconis:** Indeed. I caught the culprit in a magic imp box and had a word with him. He seemed rather confused that I was using orbs to take pictures. Apparently, imps have a rather handy spell for that, so I hired him!
            - **Player:** Imps take pictures?
            - **Iconis:** Yes. He wouldn't reveal the exact working of the spell to me, or even why they do it, but the result is very convincing.
            - [Menu]: Select an Option
              - [Choice]: Is it safe?
                - (below|safe)
              - [Choice]: What are the pictures for?
                - (above|pictures)
              - [Choice]: That's all, thank you.
                - (below)
          - [Choice]: That's unfortunate.
            - **Player:** That's unfortunate.
            - (above2|ohno)
  - [Choice]: Is it safe?
    - {{anchor|safe}} **Iconis:** Oh, absolutely! I've tried the procedure myself thousands of times to make sure it's safe and that there are no side effects.
    - **Player:** But are my belongings safe?
    - **Iconis:** Totally! I've got a few runes, orbs and trinkets in there to ensure of that.
  - [Choice]: That's all, thank you.
    - **Player:** That's all, thank you.
    - **Iconis:** You're welcome!
