# Echo plinth

- **Original Wiki Page**: [Transcript:Echo plinth](https://runescape.wiki/w/Transcript%3AEcho%20plinth)
- **Letter**: `E`

---

## Dialogue Transcript


### Check

- (Condition: If the plinth is empty:)
  - {{tselect|ECHO SELECTION
    - Engrams must be charged and handed in to Orla before you can display their echo on a plinth.
    - Displaying echoes is not required for any passive beneficial effects.
    - Select an echo to display here:
    - *(12 engram boxes are shown. If the engram has been handed in the box contains its name and a checkbox. If the engram has already been placed on a plinth the box is greyed out and the checkbox is ticked. If the engram has not been handed in the box is greyed out, contains the text '[Uncharged]' and a checkbox that is filled with a '?'.)*}}
    - [Choice]: [Clicking any engram that isn't greyed out]
      - {{qact|An echo of the selected engram appears on the plinth as the player summons it with a Divination animation that lasts indefinitely.}}  <!-- echo colour is the highest unlocked -->
    - [Choice]: CANCEL
      - ((Interface closes.))
  - (Condition: Tooltip when hovering over an engram box:) <!-- in order of appearance in the interface -->
    - Naragi: {{Interface tooltip|Found within the memory of a long-dead world.}}
    - Elder Sword: {{Interface tooltip|Found on the docks of an island devoid of pests.}}
    - Fairy: {{Interface tooltip|Found where the Fairy Queen is seated.}}
    - Gnome: {{Interface tooltip|Found at a dead end in a maze of gnomes.}}
    - World Gate: {{Interface tooltip|Found near the Gate on this world.}}
    - Druid: {{Interface tooltip|Found where you can mix cakes near a stone circle.}}
    - Stone of Jas: {{Interface tooltip|Found where a bug guards the impact from a fist.}}{{fact|Is this different if Fiara dies during The World Wakes?}}
    - Sheep: {{Interface tooltip|Found in a pen protected by 'The Thing'.}}
    - Time: {{Interface tooltip|Found where an elven queen rests eternal.}}
    - Sword of Edicts: {{Interface tooltip|Found where a sharp reminder stands for all to see.}}
    - Guardians of Guthix: {{Interface tooltip|Found where stories hold back tears of loss.}}
    - Balance Elemental: {{Interface tooltip|Found among druidic standing stones.}}
- (Condition: If the plinth has en echo on it:)
  - [Menu]: What would you like to do?
    - [Choice]: Talk to the echo.
      - ((See the transcripts for Balance Elemental, Druid, Elder Sword, Fairy, Gnome, Guardian of Guthix, Naragi, Time, Sheep, Stone of Jas, Sword of Edicts, World Gate))
    - [Choice]: Recolour this echo.{{fact|Does this show before prestiging?}}
      - [Menu]: Which colour?
        - [Choice]: Blue.
          - {{qact|The echo turns blue.}}
        - [Choice]: Green.|cond=After prestige 1:
          - {{qact|The echo turns green.}}
        - [Choice]: Gold.|cond=After prestige 2:
          - {{qact|The echo turns gold.}}
    - [Choice]: Clear this plinth.
      - {{qact|The echo disappears from the plinth.}}
