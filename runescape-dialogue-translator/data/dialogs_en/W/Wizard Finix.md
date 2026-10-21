# Wizard Finix

- **Original Wiki Page**: [Transcript:Wizard Finix](https://runescape.wiki/w/Transcript%3AWizard%20Finix)
- **Letter**: `W`

---

## Dialogue Transcript


### At the [[Wizards' Tower]]


#### Talking to Wizard Finix

- **Wizard Finix:** I hope they let me into the Runecrafting Guild soon. It's cold up here on the roof!
- [Menu]: Select an option:{{anchor|init-tower}}
  - [Choice]: What do you do in the Wizards' Tower?
    - **Wizard Finix:** I'm a student at the Wizards' Tower. I'm here to see Wizard Elriss in the Runecrafting Guild about the thesis I wrote on Runecrafting.
    - [Menu]: Select an Option
      - [Choice]: What was the thesis about?
        - **Wizard Finix:** Well, it explains my theory that the runecrafting altars are not everlasting. They are vast stores for runic energy, but one day they will run out!
        - **Wizard Finix:** I believe that's why Wizard Elriss wants to see me. The Runecrafting Guild wizards cannot disprove my theories and I think it's worrying them!
        - **Wizard Finix:** Luckily I believe I've found an alternative method of making runes: runic energy  in the Runespan!
        - [Menu]: Select an Option
          - [Choice]: Runic energy siphoning?{{anchor|siphoning}}
            - **Wizard Finix:** Yes! It's a way to take the energy out of the world around us and place it into rune essence, which in turn makes runes.
            - **Wizard Finix:** It's still a theory, and most of the Runecrafting Guild wizards think it can never be done, but Wizard Elriss thinks that the Runespan might help my studies.
            - **Wizard Finix:** We will see what Wizard Elriss says, I suppose.
            - [Menu]: Select an Option
              - [Choice]: The Runespan?
                - (below|runespan)
              - [Choice]: Other questions...
                - (initial|init-tower)
          - [Choice]: The Runespan?{{anchor|runespan}}
            - **Wizard Finix:** The Runespan is the plane in which the Runecrafting Guild was built. It's a chaotic place with runic energy flying around unbound to anything.
            - **Wizard Finix:** You can visit the Runespan by going through this portal next to me. The wizards have been observing it from the Runecrafting Guild for years, but it's only recently that they've been exploring it.
            - **Wizard Finix:** Silly old wizards. They spend far too much time arguing and not enough time going out and researching into all these theories they come up with.
            - [Choice]: Select an Option
              - [Choice]: Runic energy siphoning?
                - (above|siphoning)
              - [Choice]: Other questions...
                - (initial|init-tower)
          - [Choice]: Other questions...
            - (initial|init-tower)
      - [Choice]: Other questions...
        - (initial|init-tower)
  - [Choice]: What do you sell?
    - **Wizard Finix:** You can buy wicked robes from me. The hood will give you runes and rune essence and even teleport you to the runecrafting altars. The rest of the robes will improve the hood and make you ligher.
    - **Wizard Finix:** I can also re-colour these robes for you and provide you with an esteem icon for them to show off how much you've trained energy siphoning.
    - **Wizard Finix:** I can also provide you with staves made of rune essence. They are ineffective as melee weapons, but they can store the charges for spells which only cost runes, and are good at defending against magical attacks.
    - **Wizard Finix:** Lastly, I can sell you a rune essence pouch that is much bigger than any you would find elsewhere. This pouch will not degrade as quickly as other pouches, but once it has degraded it will turn to dust.
    - (initial|init-tower)
  - [Choice]: Can I see your shop?
    - (opens=Wizard Finix's Runecrafting Shop)
  - [Choice]: Goodbye.
    - (end)

#### Shopping with Wizard Finix

- (opens=Wizard Finix's Runecrafting Shop)
  - (Condition: If something is purchased:)
    - **Wizard Finix:** Enjoy!
    - (opens=Wizard Finix's Runecrafting Shop)
  - (Condition: If esteem is purchased:)
    - **Wizard Finix:** Congratulations! In recognition of your work siphoning runic energy, you have attained rank [number] Esteem.
    - (opens=Wizard Finix's Runecrafting Shop)

### At the [[Runespan]]


#### Talking to Wizard Finix

- **Wizard Finix:** Hello. How can I help you?
  - Hello. Who are you?
    - **Wizard Finix:** I'm Wizard Finix. I am a student of runecrafting.
    - **Player:** Ah, pleased to meet you, Wizard Finix. I'm Player. What are you doing here?
    - **Wizard Finix:** I'm creating runes by siphoning energy out of the Runespan.
    - **Player:** Creating runes by siphoning?
    - **Wizard Finix:** Yes, it's a new way to make runes. I discovered it, actually!
    - Select an option
      - Why don't you just use the altars?{{anchor|runespan-altars}}
        - **Wizard Finix:** That is another one of my discoveries! Runecrafting altars will not last forever. One day, the altars will run out!
        - **Player:** Run out?
        - **Wizard Finix:** Yes - of course, it is still only a theory. The Runecrafting Guild wizards are still sceptical, but they cannot prove me wrong.
        - **Player:** How will humans perform magic if they cannot make runes?
        - **Wizard Finix:** Exactly. That is why learning to siphon energy from the world around us is important.
        - **Player:** You mean I could create runes by pulling energy from Gielinor itself?
        - **Wizard Finix:** Theoretically, yes, but there is no runecrafter skilled enough to do this yet. In theory, runecrafting and magic should be a self-supporting cycle.
        - **Player:** So how can I learn to siphon energy if it is so difficult?
        - **Wizard Finix:** That is why we are in this area. In the Runespan, energy is still in a very raw state and is not tightly bound to matter, as it is in Gielinor. The wizards of the Runecrafting Guild have been using their tower to study runic energy in the Runespan for years.
        - **Player:** So that means...
        - **Wizard Finix:** ...we are outside the Runecrafting Guild - yes!
        - Select an option
          - So, how do you make runes by siphoning?
            - (continue|finix-warning)
          - Can you teleport me back to the Wizards' Tower?
            - (below|teleport-to-tower)
      - How do you make runes by siphoning?
        - (continue|finix-warning)
      - Can you teleport me back to the Wizards' Tower?
        - (below|teleport-to-tower)
  - What can I do here?
    - **Wizard Finix:** I can show you around, or I can just explain it to you. Which would you prefer?
    - Select an option
      - Show me
        - *(Runespan tutorial begins)*
      - Tell me
        - **Wizard Finix:** This is the Runespan. You can train runecrafting by siphoning energy from here into rune essence.
        - **Player:** How do you make runes by siphoning?
        - **Wizard Finix:{{anchor|finix-warning}}** Well, firstly, I have to warn you that any runes you make here are taken by the Runecrafting Guild when you leave. They discovered the portal to this plane, and have laid claim to it as their own. Don't worry too much about that, though. Any runes you do make will award you points to spend at my shop in the Wizards' Tower. You will learn to become a better runecrafter faster here, too.
        - Select an option{{anchor|runespan-opts-3}}
          - How do I get rune essence?
            - **Wizard Finix:** Firstly, you can only train runecrafting here with rune essence found on this plane.
            - **Player:** So how do I get rune essence?
            - **Wizard Finix:** There are two ways to get rune essence. If you have no rune essence, then you can use the floating essence to collect a small amount. If you do have some essence then the best way to get more is to siphon from the creatures that are walking around.
            - **Player:** Siphon from the creatures?
            - **Wizard Finix:** Yes. The creatures that you can find here are made up of rune essence that is bound together with runic energy. If you take away all that energy, then you are just left with rune essence. If you are in a hurry and don't want to siphon from the creatures then you can chip some of their rune essence away from them using your runes. I would advise against doing it to the same creature twice, though.
            - (previous|runespan-opts-3)
          - How do I make runes?
            - **Wizard Finix:** Once you have rune essence from this plane, you can siphon energy from the creatures and pockets of energy that appear randomly on islands in this area. The energy in the creatures is not as dense as it is in the pockets of energy, so they will give you a small amount of runes and not much experience. The pockets of energy are the best way to train. These can be easily spotted because, when one appears, the runecrafting wizards will mark the floor around it to display when energy can be siphoned from it. The pockets of energy appear in random places and you can find yourself on an island where there are none. The best way for you to train is to find the most complex type of energy you can siphon, and siphon from that.
            - (previous|runespan-opts-3)
          - How do I get around?
            - **Wizard Finix:** Getting around this plane can be tricky as it is made up of floating islands. Fortunately, the Runecrafting Guild wizards have installed crossing points. For the cost of a few runes, you can activate these points which will enchant you and take you to another island. Since these are made by wizards, it is not as simple as hopping from island to island, though. The type of runes required are shown on the crossing point. As you approach a crossing point, the far side will glow to show where it goes to. If you have the runes to use the crossing point, the near side will glow as well. Not all the crossing points will charge you. If you try to go from a small island to a big island, then the crossing point is free. This is to prevent you from becoming stranded.
            - (previous|runespan-opts-3)
          - Is there anything else to do here?
            - **Wizard Finix:** Yes, there are a couple of things you can do here as well. The wizards have a tendency to get themselves stuck on islands, and once in a while you will hear one of them calling to you. If you find and help the wizard, he will share some of his runecrafting knowledge with you. There is also a rare chance that a runesphere will form. This is a complex, multi-layered ball of rune essence. Each layer of the runesphere is aligned to a specific runic type and you need to siphon away all layers of the runesphere. This will give you rune dust and impart further runecrafting knowledge to you. The runesphere only appears for a while before it disappears. If you can siphon away all of its layers before it disappears, then you can hand in the rune dust you gathered from siphoning away the layers to the pure energy inside. This will grant you yet more runecrafting knowledge.
            - (previous|runespan-opts-3)
          - Why don't you just use the altars?
            - (above|runespan-altars)
  - Can I have some runes?
    - (continue|Buying runes from Wizard Finix)
  - Can you help me find something?
    - **Wizard Finix:** Sure, what would you like me to help you find?
    - Select an option
      - Can you help me find a wizard in yellow robes?
        - **Wizard Finix:** Sure, I've seen him. I will point you in the right direction for a while.
      - Can you help me find the runesphere?
        - *If the runesphere is not currently active:*
          - **Wizard Finix:** I don't feel the runesphere's influence at this time.
        - *If the runesphere is active:*
          - *If the runesphere is on an above floor:*
            - **Wizard Finix:** I feel the runesphere's influence above me.
          - *If the runesphere is on the current floor:*
            - **Wizard Finix:** I feel the runesphere's influence towards the <cardinal direction> of me.
  - Can you teleport me back to the Wizards' Tower?{{anchor|teleport-to-tower}}
    - **Wizard Finix:** Sure.
    - (continue|Teleporting with Wizard Finix)

#### Teleporting with Wizard Finix

- All your runes will be converted into points when you leave.
- Teleport to the Wizards' Tower?
  - Yes
    - {{Qact|Wizard Finix teleports the player to the top of the Wizards' Tower.}}
  - No
  - (end)

#### Buying runes from Wizard Finix

- *If the player has not yet bought runes:*
  - **Wizard Finix:** I can give you 10 of each rune that you can siphon for a cost of <number> reward points.
  - Do you want to buy some runes?
    - Yes
      - (receives=10 of each rune that the player can siphon)
    - No
      - (end)
- *If the player has already bought runes:*
  - **Wizard Finix:** You have already bought a starter pack. You can only buy one per trip into the Runespan.
