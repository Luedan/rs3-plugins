# Leprechaun (Evil Tree)

- **Original Wiki Page**: [Transcript:Leprechaun (Evil Tree)](https://runescape.wiki/w/Transcript%3ALeprechaun%20%28Evil%20Tree%29)
- **Letter**: `L`

---

## Dialogue Transcript


### Strange sapling dialogue

- **Leprechaun:** 'Ello, 'ello, legs.
- [Menu]: Select an option{{anchor|init-sapling}}
  - [Choice]: Who are you?
    - **Player:**  Who are you?
    - **Leprechaun:** Me? Oo's askin'? I ain't nobody but a leprechaun, innit.
    - **Player:**  You sound a bit different from other leprechauns...
    - **Leprechaun:** That's bein' on account a' the fact I was raised by imps, innit. Luvverly chaps, imps. Right geezers.
    - **Leprechaun:** Anyways, if ya gimme a 'and, [lad/lass], I can return a favour.
    - **Leprechaun:** I come across this wild root on me wanderin', so I reckoned I'd stick about and get you geezers wif long legs to help nurture it.
    - **Leprechaun:** The wee thing's growin' fast, but ya'd speed up the process if ya gave it some encouragement.
    - (initial|init-sapling)
  - [Choice]: What's that thing growing nearby?
    - **Player:**  What's that thing growing nearby?
    - **Leprechaun:** That? That's...thats a...it's a rare...uh...innit.
    - **Player:**  You don't know what it is do you?
    - **Leprechaun:** No, not rightly...
    - **Leprechaun:** But all a' Mother Gielinor's creations is worth looking after. Giz us a hand and encourage the wee thing, won't ya? It's growin' fast!
    - (initial|init-sapling)
  - [Choice]: How do I nurture it?
    - **Player:**  How do I nurture it?
    - **Leprechaun:** That's easy, just interact with it, like ya would any Farming crop. That'll 'elp it to grow big and strong. Ya might even get yaself some Farming experience.
    - **Player:** How long does it take to nurture it?
    - (Condition: If the strange sapling hasn't transformed yet:)
      - **Leprechaun:** Not long at all. My experienced eye reckons e'll be fully grown in about [2/3/4/5] minutes. A' course, if you get some mates to help, the wee thing'll grow faster.
      - (initial|init-sapling)
    - (Condition: If the strange sapling is about to transform:)
      - **Leprechaun:** Not long at all. My experienced eye reckons e'll be fully grown in about 1 minute. A' course, if you get some mates to help, the wee thing'll grow faster.
      - (initial|init-sapling)
    - (Condition: If the strange sapling has already transformed into an Evil Tree:)
      - **Leprechaun:** Not long at all. My experienced eye reckons e'll be fully grown in about...
      - **Leprechaun:** Crickey! What's that!
  - [Choice]: Why should I help?
    - **Player:** Why should I help?
    - **Leprechaun:** There's 'uge rewards tendin' nature, 'elping weak things become strong. Ya might learn about Farming by helping this wee sapling grow into a tree.
    - (initial|init-sapling)
  - [Choice]: Goodbye
    - **Player:** Goodbye.
    - **Leprechaun:** See ya'!

### Evil Tree dialogue

- **Leprechaun:** Ain't you noticed the tree yet? Cut it down!
- [Menu]: Select an option{{anchor|init-options}}
  - [Choice]: Who are you?
    - **Player:**  Who are you?
    - **Leprechaun:** Me? Oo's askin'? I ain't nobody but a leprechaun, innit.
    - **Player:**  You sound a bit different from other leprechauns...
    - **Leprechaun:** That's bein' on account a' the fact I was raised by imps, innit. Luvverly chaps, imps. Right geezers.
    - **Leprechaun:** Anyways, I came across this 'ere root on me wanderin', so I got you geezers wif long legs to 'elp me out.
    - **Leprechaun:** Now look what I gots on me 'ands. Please, lad!
    - **Leprechaun:** If ya gimme a hand, I can return a favour.
    - (initial|init-options)
  - [Choice]: What is that thing?
    - **Player:**  What is that thing?
    - **Leprechaun:** That there is an evil tree, innit. The cunnin' geezer starts off lookin' like an innocent sapling.
    - **Leprechaun:** Later on, though, ooh! It grows into a frightenin' beast, all lashin' roots and 'Look at me nasty teef!'
    - **Leprechaun:** Some of 'em, I heard from a mate of a mate, are easier to kill than others.
    - (initial|init-options)
  - [Choice]: How can I help?
    - **Player:**  How can I help?
    - **Leprechaun:** You can't get near the tree while those roots are thrashin' about, so you'll have to cut them with a hatchet. Once they're gone, you can attack the tree itself. 'Cos it's a tree, it don't like hatchets or fire. Use any kindling you gets off the roots to set fires at the base of the tree. The fires will keep burning and doing damage to the tree while you whack it with a hatchet.
    - **Leprechaun:** Do ya need more information?
    - [Menu]: Select an option
      - [Choice]: Yes
        - **Player:**  Yes, I'd like some more information.
        - [Menu]: What do you want to know more about?{{anchor|knowmore}}
          - [Choice]: How do I cut the tree?
            - **Player:**  How do I cut the tree?
            - **Leprechaun:** Ya can only cut the tree when the roots are gone and if ya have a hatchet. The better the hatchet, the faster ya cut the tree.
            - **Leprechaun:{{anchor|hatchet}}** Do ya want a hatchet? I reckon I gots one in me loot-bag somewhere...
            - [Menu]: Select an option
              - [Choice]: Yes
                - **Leprechaun:** It looks like ya've already got a hatchet!
                - (initial|init-options)
              - [Choice]: No
                - **Player:** No, thanks.
                - **Leprechaun:** Suit yaself, [lad/lass].
                - (initial|init-options)
          - [Choice]: How do I light fires on the tree?
            - **Player:**  How do I light fires on the tree?
            - **Leprechaun:** Ya can only burn the tree when the roots are gone. When they've been cut back, use the kindling from the roots on the tree. You got to have a tinderbox to light the fires.
            - **Leprechaun:** Do ya need a tinderbox?
            - [Menu]: Select an option
              - [Choice]: Yes
                - (Condition: If the player does not have a tinderbox in inventory:)
                  - **Leprechaun:** Ya need a tinderbox? Here ya go, lad. Don't burn yaself!
                  - [He hands you a tinderbox.]
                  - (receives=tinderbox)
                  - (initial|init-options)
                - (Condition: If the player already has a tinderbox in inventory:)
                  - **Leprechaun:** It looks like ya've already got a tinderbox!
                  - (initial|init-options)
              - [Choice]: No
                - **Player:** No, thanks.
                - **Leprechaun:** Suit yaself, [lad/lass].
          - [Choice]: How do I deal with the roots?
            - **Player:**  How do I deal with the roots?
            - **Leprechaun:** Ya have to cut them down to get to the tree. A hatchet or machete should do the trick. The more people cutting them, the faster they'll come down. Ya can get kindling from them, which ya want to keep to light fires on the tree.
            - **Leprechaun:** Do ya want a hatchet? I reckon I gots one in me loot-bag somewhere...
            - (continuea|hatchet)
          - [Choice]: How do I know how much damage I'm doing to the tree?
            - **Player:**  How do I know how much damage I'm doing to the tree?
            - **Leprechaun:** If ya 'inspect' the tree, ya can find out how much damage you've done, as well as a few other bits of useful info.
            - **Leprechaun:** Ya should also see bark fly off as you cut it, and the fires will flare up when they do damage. Ya should see the tree look weaker the more damage you do. I'll let ya know how ya doin' as often as I can.
            - (initial|init-options)
          - [Choice]: How long will this take?
            - **Player:**  How long will this take?
            - (Condition: When the tree has less than 100% health remaining:)
              - **Leprechaun:** It's still big. I reckon it could be around for half an hour. If you get some mates to help, we can kill it faster!
              - (continue)
            - (Condition: When the tree has less than 50% health remaining:)
              - **Leprechaun:** It's gettin' weaker. I reckon it'll take less than twenty minutes. If you get some mates to help, we can kill it faster!
              - (continue)
            - (Condition: When the tree has less than 25% health remaining:)
              - **Leprechaun:** It's gettin' weak. I don't reckon it can last more than ten minutes. If you get some mates to help, we can kill it faster!
              - (continue)
            - (initial|init-options)
      - [Choice]: No
        - **Player:** No, thanks.
        - **Leprechaun:** Suit yaself, [lad/lass].
        - (initial|init-options)
      - [Choice]: Can I borrow some tools?
        - (below|borrow)
      - [Choice]: Why should I help you?
        - **Player:** Why should I help you?
        - **Leprechaun:** There's loads of loot in it for ya. Killing one of them will get ya logs, of course.
        - **Leprechaun:** But that ain't all! You might get seeds or nests, Treasure Trail clues, and maybe a few other surprises.
        - **Leprechaun:** Also, any logs ya get I'll teleport straight to ya bank. Honest, guv.
        - **Leprechaun:** I can also make you less likely to fell some trees while you're chopping them, but this'll only work on trees you haven't grown yourself.
        - **Leprechaun:** Do ya need more information?
        - (previous|knowmore)
  - [Choice]: Can I borrow some tools?
    - **Player:{{anchor|borrow}}** Can I borrow some tools?
    - **Leprechaun:** I reckon I can spare 'em for ya.
    - [Menu]: Select an option
      - [Choice]: Hatchet
        - **Leprechaun:** It looks like ya've already got a hatchet!
      - [Choice]: Tinderbox
        - (Condition: If the player does not have a tinderbox in inventory:)
          - **Leprechaun:** Ya need a tinderbox? Here ya go, lad. Don't burn yaself!
          - [He hands you a tinderbox.]
          - (receives=tinderbox)
          - (initial|init-options)
        - (Condition: If the player already has a tinderbox in inventory:)
          - **Leprechaun:** It looks like ya've already got a tinderbox!
          - (initial|init-options)
      - [Choice]: Both
        - **Leprechaun:** It looks like ya've already got a hatchet!
        - (Condition: If the player does not have a tinderbox in inventory:)
          - **Leprechaun:** Ya also need a tinderbox? Here ya go, lad. Don't burn yaself!
          - [He hands you a tinderbox.]
          - (receives=tinderbox)
          - (initial|init-options)
        - (Condition: If the player already has a tinderbox in inventory:)
          - **Leprechaun:** And it looks like ya've already got a tinderbox!
          - (initial|init-options)
      - [Choice]: Nothing
        - (initial|init-options)
  - [Choice]: Goodbye
    - **Player:** Goodbye.
    - **Leprechaun:** See ya'!

### If the tree is dead

- **Leprechaun:** Blimey! You gone an' done it!
- [Menu]: Select an option{{anchor|init-options-2}}
  - [Choice]: Who are you?
    - **Player:**  Who are you?
    - **Leprechaun:** Me? Oo's askin'? I ain't nobody but a leprechaun, innit.
    - **Player:**  You sound a bit different from other leprechauns...
    - **Leprechaun:** That's bein' on account a' the fact I was raised by imps, innit. Luvverly chaps, imps. Right geezers.
    - **Leprechaun:** Anyways, I came across this 'ere root on me wanderin', so I got you geezers wif long legs to 'elp me out.
    - **Leprechaun:** Turns out, I gots a wee bit a'bovver, though, on account of it has gnashin' teef and thrashin' roots!
    - **Leprechaun:** So I gots you lot to 'elp me out by choppin' and burnin' the arboreal nightmare down!
    - (initial|init-options-2)
  - [Choice]: What's that thing nearby?
    - **Player:** What's that thing nearby?
    - **Leprechaun:** That? That's an 'Evil Tree', matey.
    - **Leprechaun:** It's a cunnin' geezer, and starts out lookin' like an innocent sapling.
    - **Leprechaun:** Later on, though, ooh! It grows into a frightenin' beast, all lashin' roots and 'Look at me nasty teef!'
    - **Leprechaun:** Some of 'em, I heard from a mate of a mate, are easier to kill than others.
  - [Choice]: Will there be another Evil Tree?
    - **Leprechaun:** That's the funny thing. They seem to appear every coupla' hours all around the world. Strange, innit? The spirit trees know where they are; ask them if you're keen to help.

### After taking rewards from the Dead Evil Tree

- **Leprechaun:** Thanks for ya help, lad! For the next X  minutes (dependent on the type of evil tree felled) any regular oak, willow, maple, magic or elder logs ya get I'll teleport straight to ya bank. Honest, guv!
- **Leprechaun:** I'll also sort some magic out, makin' ya less likely to fell regular, oak, willow, maple, yew or magic trees, but this'll only work on some trees ya find on ya wanderin', not ones ya've grown yaself.
- **Player:** Thanks!

### Overhead dialogue

- (Condition: Upon the strange sapling turning into an Evil Tree:)
  - **Leprechaun:** {{RSChat|Crikey! What's that!}}
- (Condition: Upon the Evil Tree reaching 50% health:)
  - **Leprechaun:** {{RSChat|It's getting weaker!}}
- (Condition: Upon the Evil Tree dying:)
  - **Leprechaun:** {{RSChat|Hurrah! The Evil Tree is dead!}}

#### Historical overhead dialogue

- (Condition: When the health of the Evil Tree is above 25%, any of the following dialogue may occur:)
  - **Leprechaun:** {{RSChat|Why does this always 'appen to me?!}}
  - **Leprechaun:** {{RSChat|Ooh! 'E's a nasty one!}}
- (Condition: When the health of the Evil Tree is below 25%, any of the following dialogue may occur:)
  - **Leprechaun:** {{RSChat|Don't stop choppin'!}}
  - **Leprechaun:** {{RSChat|It's on its last legs! I mean... roots!}}
  - **Leprechaun:** {{RSChat|The end is nigh!}}
  - **Leprechaun:** {{RSChat|You can do it!}}
