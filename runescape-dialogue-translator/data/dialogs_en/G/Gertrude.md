# Gertrude

- **Original Wiki Page**: [Transcript:Gertrude](https://runescape.wiki/w/Transcript%3AGertrude)
- **Letter**: `G`

---

## Dialogue Transcript


### West of Varrock


#### Normally

- [Menu]: Choose an option:
  - [Choice]: Do you have any more kittens?
    - **Player:** Do you have any more kittens?
    - (Condition: If the player already has a kitten:)
      - **Gertrude:** Aren't you still raising that other kitten? Only once it's fully grown and it no longer needs your attention will I let you have another kitten.
    - (Condition: If the player doesn't have a kitten:)
      - **Gertrude:** Indeed I have. They are 100 coins each, do you want one?
      - (Condition: If the player doesn't have 100 coins:)
        - **Player:** Oops, looks like I'm a bit short. I'll come back later.
      - (Condition: If the player has 100 coins:)
        - [Menu]: Select an Option
          - [Choice]: Accept the offered kitten.
            - (removes=100 coins)
            - (receives=pet kitten)
            - Gertrude gives you another kitten.
          - [Choice]: Don't buy a kitten.
            - **Player:** No thanks.
          - [Choice]: cond=With a ring of charos (a) equipped|[Charm] Ask to choose your own kitten.
            - **Gertrude:** Well okay, but they're all just as cuddly as each other.
            - (opens=Cat#Gallery{{!)Kitten selection}}
            - (removes=100 coins)
            - (receives=pet kitten)
            - Gertrude gives you another kitten.
  - [Choice]: Can you tell me how to look after my cat?
    - **Player:** Can you tell me how to look after my cat?
    - **Gertrude:** I'm so glad you asked. What is it you need to know?
    - [Menu]: Select an Option
      - [Choice]: What should I feed my cat?{{anchor|cat-food}}
        - **Player:** What should I feed my cat?
        - **Gertrude:** You'll find that most sorts of fish will help keep your cat growing and happy, although I don't think Fluffs liked eels much. As for drink, buckets of milk are the best. Remember, if you don't feed your cat, it is likely to run away - understandable, really.
        - **Player:** Thanks for the advice.
        - **Gertrude:** Is there anything more you need to know?
        - [Menu]: Select an Option
          - [Choice]: No, thank you. I'll be off now.{{anchor|im-off}}
            - **Player:** No, thank you. I'll be off now.
          - [Choice]: How can I keep my cat happy?
            - (below|happy-cat)
          - [Choice]: What sorts of cat are there?
            - (below|cat-types)
      - [Choice]: How can I keep my cat happy?{{anchor|happy-cat}}
        - **Player:** How can I keep my cat happy?
        - **Gertrude:** You can stroke it, of course. All cats like to be stroked. If you are feeling a bit more energetic you can play with balls of yarn; cats enjoy playing with those.
        - **Gertrude:** I've also heard that skilled craftsmen can make clockwork mice as cat toys. <br>If this all seems a bit too much like effort, remember that a bored cat will run away in search of adventure.
        - **Player:** Thanks for the advice.
        - **Gertrude:** Is there anything more you need to know?
        - [Menu]: Select an Option
          - [Choice]: No, thank you. I'll be off now.
            - (above|im-off)
          - [Choice]: What should I feed my cat?
            - (above|cat-food)
          - [Choice]: What sorts of cat are there?
            - (below|cat-types)
      - [Choice]: What sorts of cat are there?{{anchor|cat-types}}
        - **Player:** What sorts of cat are there?
        - **Gertrude:** Well, you know that a kitten will grow into a cat if you feed and treat it well. You can, however, go a bit far and end up with an overgrown cat.
        - **Gertrude:** I've heard that there are secret methods for training an overgrown cat into a wily cat. You have to keep wily cats on their toes, though, or they can easily become lazy cats. Even more extreme are hellcats; if your cat eats too many hellrats then they turn into one! Luckily, a drink of milk sorts this out.
        - **Player:** Thanks for the advice.
        - **Gertrude:** Is there anything more you need to know?
        - [Menu]: Select an Option
          - [Choice]: No, thank you. I'll be off now.
            - (above|im-off)
          - [Choice]: How can I keep my cat happy?
            - (above|happy-cat)
          - [Choice]: What should I feed my cat on?
            - (above|cat-food)
  - [Choice]: cond=After catching 100 rats and without a cat training medal:|Tell Gertrude your cat has caught 100 rats.
    - **Player:** Hello again Gertrude!
    - **Gertrude:** Well, hello adventurer! How are you?
    - **Player:** My cat has caught 100 rats!
    - **Gertrude:** Well well! You are good with cats!
    - **Gertrude:** Here, I have a little present for you.
    - (receives=Cat training medal)
    - Gertrude hands you a small medal.
    - (Condition: If this is the first time claiming the medal:)
      - {{RSFontAchievement|Faster, Pussycat! Kill! Kill!}}
      - (continue)
    - **Player:** Hey thanks Gertrude.
  - [Choice]: cond=With a hellcat out:|What's happened to my cat?
    - **Player:** What's happened to my cat?
    - **Gertrude:** Oh, deary me. You've been letting it eat demonic beings, haven't you? Don't worry, just give it a drink of milk and it'll be right as rain.
  - [Choice]: cond=After Ratcatchers:|Talk about the 'Ratcatchers' quest.
    - **Gertrude:** Did you ever talk to those people I told you about?
    - **Player:** Yes, strange people. But interesting nonetheless.

#### During the 25th Anniversary celebrations task with a cat follower

- **Gertrude:** I hope you're taking good care of this little cute baby.
- **Player:** I sure am!
- **Gertrude:** I was talking to your cat.
- **Player:** Oh, right.
- {{RSFontAchievement|Gertrude's Cat|Talk to Gertrude while you have a cat follower.}}
- ((Shown in a task completion pop-up:))
  - {{Colour|#F0BE79|&nbsp;25TH ANNIVERSARY TASK&nbsp;|#181513}}
  - Gertrude's Cat
  - Talk to Gertrude while you have a cat follower.
  - (continue)
- **Player:** I can assure you that I am well fed and get lots of attention.
- (Condition: If all the tasks have been completed:)
  - **Player:** Looks like I've completed everything. I'd better go and see Hans about that reward!

### In New Varrock


#### Before Mummy Returns

- **Gertrude:** I've lost them.<br>I've lost all of them!
- [Menu]: Choose an option:
  - [Choice]: Who have you lost?
    - **Gertrude:** First it was Fluffs, my beloved feline friend. She'd been purring by my side for almost a decade.
    - **Gertrude:** There was nobody here to help, so I sent my eldest sons, Wilough and Shilop, out to search for her.
    - **Gertrude:** That was the day the demon came...my poor boys. When the red terror burst up through the floor of the square, they were the first to be taken.
    - **Gertrude:**After the...the funeral, I was very upset. I shouldn't have gone into the city, not with the demon still about, but I was so lonely.
    - **Gertrude:** I only left the house for a short while. I made sure that my children Philop and Kanel were well fed, and the door was securely locked.
    - **Gertrude:** I'd barely stepped foot in the square when the dead marched on Varrock. The city guard sealed the gates to try to keep them out.
    - **Gertrude:** They wouldn't let me go back for my little Philop and Kanel. By the time the gates fell and the battle was over, it was already too late.
    - **Gertrude:** My home was a smoking ruin, and my boys were nowhere to be found.
    - **Gertrude:** After the necromancer took over, I moved into this building, since I had nowhere else to stay. I adopted one of the stray dogs, trying to fill the emptiness in my soul.
    - **Gertrude:** I've loved him and petted him, but he's changed, bless him. He tries to bite me, and only eats raw meat.
    - (Condition: If the player has already taken Dimies the sardine:)
      - **Gertrude:** And now my pet fish, my poor little Dimies, has gone missing too! It's heartbreaking...
      - (continue)
    - **Gertrude:** Oh but I don't want to bother you with the troubles of a silly old spinster and her tragic past. It's not like there's anything you can do to help. <br>What is it you were wanting?
    - (initial)
  - [Choice]: Are you selling anything?
    - **Gertrude:** Selling?<br>Well, I could offer you a warm meal, or some nice, yummy chocolate cake. <br>Cooking's how I keep myself occupied nowadays...
    - (opens=Gertrude's Food)
  - [Choice]: Goodbye.
    - **Gertrude:** Oh...you're leaving so soon?<br>I do love a bit of company. I've been so lonely...

#### After Mummy Returns

- **Gertrude:** Thank you for returning Fluffs home - she told me everything!
- [Menu]: Choose an option:
  - [Choice]: Who have you lost?
    - **Gertrude:** First it was Fluffs, my beloved feline friend. She'd been purring by my side for almost a decade.
    - **Gertrude:** There was nobody here to help, so I sent my eldest sons, Wilough and Shilop, out to search for her.
    - **Gertrude:** That was the day the demon came...my poor boys. When the red terror burst up through the floor of the square, they were the first to be taken.
    - **Gertrude:**After the...the funeral, I was very upset. I shouldn't have gone into the city, not with the demon still about, but I was so lonely.
    - **Gertrude:** I only left the house for a short while. I made sure that my children Philop and Kanel were well fed, and the door was securely locked.
    - **Gertrude:** I'd barely stepped foot in the square when the dead marched on Varrock. The city guard sealed the gates to try to keep them out.
    - **Gertrude:** They wouldn't let me go back for my little Philop and Kanel. By the time the gates fell and the battle was over, it was already too late.
    - **Gertrude:** My home was a smoking ruin, and my boys were nowhere to be found.
    - **Gertrude:** After the necromancer took over, I moved into this building, since I had nowhere else to stay. I adopted one of the stray dogs, trying to fill the emptiness in my soul.
    - **Gertrude:** I've loved him and petted him, but he's changed, bless him. He tries to bite me, and only eats raw meat.
    - **Gertrude:** And now my pet fish, my poor little Dimies, has gone missing too! It's heartbreaking...
    - **Gertrude:** Oh but I don't want to bother you with the troubles of a silly old spinster and her tragic past. Fluffs is home now, and that's cheered me right up.
    - (initial)
  - [Choice]: How is Fluffs?
    - **Gertrude:** Oh, it's just like old times!<br>We'll be together for decades to come!
    - **Gertrude:** Though she does say the strangest things sometimes - devouring souls and such, but...
    - **Gertrude:** She brought home her kittens too! They've been living stray in Varrock and I never knew. They're all upstairs.
    - **Gertrude:** Someone did take my fish - my poor little sardine - Dimies. Another tragic loss...
    - **Gertrude:** It's just as well, though. The cats would have eaten him by now anyway.
    - **Gertrude:** And one of the kittens gave me this strange book about cats. It's very interesting...
    - (initial)
  - [Choice]: Are you selling anything?
    - (above)
  - [Choice]: Goodbye.
    - **Gertrude:** Come back soon!
