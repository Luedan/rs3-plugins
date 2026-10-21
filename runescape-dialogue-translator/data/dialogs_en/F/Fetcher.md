# Fetcher

- **Original Wiki Page**: [Transcript:Fetcher](https://runescape.wiki/w/Transcript%3AFetcher)
- **Letter**: `F`

---

## Dialogue Transcript

{{Outdated|Dailyscape overhaul that removed raid lockout mechanic}}

### Standard dialogue

- **Fetcher:** It is dangerous to go beyond this point human. Let me help you prepare yourself.
- [Menu]: Choose an option:
  - [Choice]: Can you fetch any loot I might've missed?
    - ((If the player has no loot to collect, Lil' Tuzzy to check, or hasn't previously done Raids:))
      - **Fetcher:** I'm sorry human, I couldn't find anything for you.
    - ((If the player has loot:))
      - ((If the loot hasn't been checked yet:))
        - **Fetcher:** I've found something for you!
        - (continue)
      - ((If the loot has been checked but not all of it has been dealt with yet:))
        - **Fetcher:** It looks like you didn't finish sorting through the last items I found you. Take a look.
        - (continue)
      - ((The following is shown in an interface titled "SELECT AN OPTION:))
        - What should I fetch?
          - ((Only with Beastmaster Durzag loot available:))
            - Collect Beastmaster Durzag loot.
              - (The Reward Chest interface opens.)
                - ((After closing the interface without having dealt with all the loot:))
                  - {{Contrast|c=#003366|t=WARNING:}} If you log out, items in the reward chest will be moved to your inventory or bank. If both of those places are full you will lose the items.
          - ((Only with Yakamaru loot available:))
            - Collect Yakamaru loot.
              - (The Reward Chest interface opens.)
                - ((After closing the interface without having dealt with all the loot:))
                  - {{Contrast|c=#003366|t=WARNING:}} If you log out, items in the reward chest will be moved to your inventory or bank. If both of those places are full you will lose the items.
          - I'll come back later.
            - {{Transcript missing}}
    - ((Failing to loot Lil' Tuzzy while on lockout:))
      - **Fetcher:** I'm sorry human, I couldn't find Lil' Tuzzy anywhere.
    - ((Successfully looting Lil' Tuzzy while on lockout:))
      - **Fetcher:** Hey, I found something for you.
    - ((Unknown trigger:))
      - **Fetcher:** I'll see if I can find some loot for you!
      - **Fetcher:** Nope. I couldn't find anything.
  - [Choice]: Show me my current raid lock.
    - (below|View lock)
  - [Choice]: Can you automatically reset my raid lockout?
    - **Fetcher:** That should be possible human.
    - (Condition: If Fetcher wasn't previously asked to automatically reset raids lockout:)
      - [Menu]: Automatically reset your raids lockout?
        - [Choice]: Yes
          - (end)
        - [Choice]: No
          - (end)
    - (Condition: If Fetcher was already automatically resetting raids lockout:)
      - **Fetcher:** It seems I'm already doing it for you human. Do you want me to stop?
      - [Menu]: Stop automatically {{Sic|reseting your raids lockout?}}
        - [Choice]: Yes
          - (end)
        - [Choice]: No
          - (end)
  - [Choice]: cond=If the player has the maximum goebie reputation and is carrying burial charms:|Would you pay any Teci for these burial charms?
    - **Fetcher:{{anchor|exchange}}** If you have no use for your charms, I'd be willing to exchange them for a small amount of Teci. Are you interested?
    - [Menu]: Exchange [#] charm[s] for [#] Teci?
      - [Choice]: Yes.
        - (removes=all burial charms)
        - (receives=the corresponding amount of Teci)
      - [Choice]: No.
        - **Fetcher:** Very well, human.
  - [Choice]: Goodbye.
    - (end)

### Using a burial charm on Fetcher


#### Without maximum reputation

- **Fetcher:** I can't do anything with that human. Maybe if you were a little bit more well known, I could make an exchange.

#### With maximum reputation

- (continuea|exchange)

### Collect loot

- (above|loot)

### View lock

- (An interface titled Mazcab Raid Lock opens, with "BEASTMASTER DURZAG" and "YAKAMARU" shown in either green or red background, depending whether loot is available or not. The button labelled "RESET" is either enabled or disabled.)
- ((Only if the reset is enabled:))
  - RESET
    - You can only reset the Mazcab raid once every 48 hours. Ensure you wish to reset your progress before you continue!
      - CANCEL
        - ((Returns to the Mazcab Raid Lock interface without changes.))
      - CONFIRM
        - Your raid progress has been reset.
        - ((Returns to the Mazcab Raid Lock interface with the backgrounds changed to green and reset button disabled.))
- ((When hovering over the disabled reset button:))
  - Boss progress can only be reset once every 48 hours.
