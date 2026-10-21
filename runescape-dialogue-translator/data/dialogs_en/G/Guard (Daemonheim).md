# Guard (Daemonheim)

- **Original Wiki Page**: [Transcript:Guard (Daemonheim)](https://runescape.wiki/w/Transcript%3AGuard%20%28Daemonheim%29)
- **Letter**: `G`

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Hello.
- **Guard:** Can we help you with anything?
- What would you like to say?{{anchor|init}}
  - Can I go through the gate?
    - **Player:** Can I go through the gate?
    - **Guard:** If you want, we will let you pass into the Wilderness. Be warned that other players might attack you there, and you won't be allowed through the gate while you're in combat.
    - What would you like to say?
      - I am not afraid.
        - **Player:** I am not afraid.
        - **Guard:** Your speech is brave. Travel south-west, and you should reach the city of Varrock, if you don't die first. Now, can we help you with anything else?
        - What would you like to say?{{anchor|second-opts}}
          - What are you doing here?
            - (below|role)
          - Is there any other way out of here?
            - **Player:** Is there any other way out of here?
            - **Guard:** Oh yes. Go back up the hill to the campsite, then head east to the docks. There is a ferry that will take you south to the so-called civilised lands. It's far safer than trying to walk through the Wilderness. Now, can we help you with anything else?
            - (initial|init)
          - No thanks.
            - **Player:** No thanks.
      - Forget it, I'm not going through there.
        - **Player:** Forget it, I'm not going through there.
        - **Guard:** That is wise. Now, can we help you with anything else?
        - (continuea|second-opts)
  - What are you doing here?{{anchor|role}}
    - **Player:** What are you doing here?
    - **Guard:** We are guarding this gateway against the vicious fighters who roam the Wilderness.
    - **Player:** Good luck with that.
    - **Guard:** Thank you. Now, can we help you with anything else?
    - (continuea|second-opts)
  - No thanks.
    - **Player:** No thanks.

### Attempting to enter the Wilderness

- **Guard:** You can enter the Wilderness, if you like, but you can't return this way if you're in combat.
- Proceed through the gate?
  - Yes, I understand the restrictions.
    - {{Qact|The player walks past the guard, into the Wilderness.}}
  - No, I'll stay here.
    - ((The player walks one square back.))
    - **Player:** No, I'll stay here.
