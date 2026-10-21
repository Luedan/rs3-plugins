# Guthixian High Druid

- **Original Wiki Page**: [Transcript:Guthixian High Druid](https://runescape.wiki/w/Transcript%3AGuthixian%20High%20Druid)
- **Letter**: `G`

---

## Dialogue Transcript


### Standard dialogue

- **Guthixian High Druid:** Welcome. What can I aid you with?
- **CHOOSE AN OPTION:**
  - What is there to do here?
    - *If the player has not completed all activities in the main chamber:*
      - **Guthixian High Druid:** The shrine is a place of mourning. There are activities you can do to pay your respects, which you may find rewarding. We could also use your aid in a threat from the main chamber.
    - *If the player has completed all activities in the main chamber:*
      - **Guthixian High Druid:** You have paid your respects here. You need do no more. Of course, we could still use your aid in a threat from the main chamber.
    - **SELECT AN OPTION:**
      - *If the player has not lit the five torches:*
        - {{Transcript missing}}
      - *If the player has not paid respects on the monument:*
        - What can I do to pay my respects?
          - **Guthixian High Druid:** We are grateful to you for lighting the torches. We have also constructed a memorial to Guthix. Perhaps you would find it beneficial to contemplate his passing there.
      - What's happening in the main chamber?
        - **Guthixian High Druid:** There is an abundance of automatons loose in the chamber. Since Cres's death, they have become increasingly unstable.
        - **Guthixian High Druid:** Sad to say, without their master they are turning on anyone who enters.
        - **Guthixian High Druid:** If you are feeling up to it, we could use your help in thinning their numbers. After all, we need to preserve the sanctity of the shrine.
        - (continue|ask)
      - Do you think Guthix would approve of this shrine?
        - **Guthixian High Druid:** The importance here is learning from the events that happened.
        - **Guthixian High Druid:** With the knowledge we now have, we are trying to steer away from revering Guthix as a powerful god, but there will always be those who would praise him in this way.
        - **Guthixian High Druid:** Here in the shrine, we have the utmost respect for Guthix. In honour of his final words, we are trying only to continue our belief in balance and what Guthix taught, rather than Guthix himself.
        - **Guthixian High Druid:** We cannot ignore the importance of the events that have passed here, and this space provides us with an environment to reflect on them.
        - (continue|ask)
  - Can you teleport me to the main chamber?
    - *If the player does not meet the requirements for the additional rewards:*
      - **Guthixian High Druid:** Sadly, I do not believe you are experienced enough to face this threat at this time.
      - **Guthixian High Druid:** Please, train more and come back. We dearly need your help.
      - **{{anchor|ask}}SELECT AN OPTION**
        - Ask about something else.
          - (initial|initial-options)
        - That's all, thanks.
          - (end)
    - *If the player meets the requirements for the additional rewards:*
      - {{Qact|The Guthixian High Druid casts a spell on the player, who is teleported to the main chamber.}}
  - *If the player still has Azzanadra's/Juna's/Zilyana's Gift:*
    - I'd like to exchange my top.
      - **Guthixian High Druid:** If you have truly changed your mind, I will provide you with an alternative. Which would you like?
      - *(All the options except for the gift the player owns are shown:)*
        - **CHOOSE AN OPTION:**
          - Azzanadra's Gift
            - (continue)
          - Juna's Gift
            - (continue)
          - Zilyana's Gift
            - (continue)
      - (removes=current gift) (receives=chosen gift)
      - **Guthixian High Druid:** As you wish.
      - (continuea|ask)
  - *If the player has lost Azzanadra's/Juna's/Zilyana's Gift:*
    - I've lost some of my rewards.
      - **WHAT WOULD YOU LIKE TO RECLAIM?**
        - Ancient lamps
          - You receive an ancient lamp.
        - Sixth Age Circuit{{Sic}}
          - You receive a Sixth Age circuit{{Sic}}.
        - Static lamps
          - {{Transcript missing}}
        - Pale lamp
          - You receive a pale lamp.
        - Glossy lamp
          - You receive a glossy lamp.
        - [Azzanadra/Juna/Zilyana]'s Gift
          - (receives=gift)
          - You receive [Azzanadra/Juna/Zilyana]'s Gift.
      - **Guthixian High Druid:** It seems you have everything you need.
      - (initial|initial-options)
  - *If the player has not claimed the additional rewards:*
    - Am I eligible for any more rewards yet?
      - *If the player is not eligible to claim the additional rewards:*
        - **Guthixian High Druid:** I am afraid you are not yet strong enough to gain Guthix's full blessing. Have hope, adventurer.
        - (continuea|ask)
      - *If the player is eligible to claim the additional rewards:*
        - The Guthixian High-Druid{{Sic}} hands you a Sixth Age Circuit{{Sic}}.
        - {{Transcript missing}}

### Claim rewards option

- *If the player has rewards to reclaim:*
  - (above|reclaim-rewards)
- *If the player does not have rewards to reclaim:*
  - **Guthixian High Druid:** It seems you have all you need.
  - (initial|initial-options)

### Teleport option

- *If the player does not meet the requirements for the additional rewards:*
  - (above|teleport-fail)
- *If the player meets the requirements for the additional rewards:*
  - **THE REST OF THE CHAMBERS ARE DANGEROUS. ARE YOU SURE YOU WISH TO ENTER?**
    - Yes
      - {{Qact|The Guthixian High Druid casts a spell on the player, who is teleported to the main chamber.}}
    - Actually, no...
      - (end)

### Reminisce option

- **WHICH MEMORY WOULD YOU LIKE TO VIEW?**
  - Meeting Cres
    - {{Qact|Replays the cutscene.}}
  - Zilyana confronting Cres
    - {{Qact|Replays the cutscene.}}
  - Sliske dealing his final blow
    - {{Qact|Replays the cutscene.}}
  - Saradomin's return
    - {{Qact|Replays the cutscene.}}
  - I don't want to view a memory
    - (end)
