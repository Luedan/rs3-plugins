# Blurberry

- **Original Wiki Page**: [Transcript:Blurberry](https://runescape.wiki/w/Transcript%3ABlurberry)
- **Letter**: `B`

---

## Dialogue Transcript


### Cocktail training


#### Starting out

- **Player:** Hello.
- **Blurberry:** Well hello there traveller. If you're looking for a cocktail the barman will happily make you one.
- **Blurberry:** Or if you're looking for some training in cocktail making, then I'm your gnome! Aluft Gianne jnr. is looking for gnome cooks and bartenders to help in his new venture, so it's a useful skill to have.
- Select an option
  - No thanks, I prefer to stay this side of the bar.
    - **Player:** No thanks, I prefer to stay this side of the bar.
  - Ok then I'll give it a go.
    - **Player:** Ok then I'll give it a go.
    - **Blurberry:** Excellent. It's not an easy job, I'll have to try you out first. I'm sure you'll be great though.
    - (receives=cocktail guide)
    - **Blurberry:** Here, take this cocktail guide. The book tells you how to make all the cocktails we serve. I'll tell you what I need and you can make them.
    - **Player:** Sounds easy enough.
    - **Blurberry:** Take a look at the book then come and talk to me.

#### Fruit Blast

- **Player:** Hello Blurberry.
- **Blurberry:** Hi, are you ready to make your first cocktail?
- **Player:** Absolutely.
- *If the player doesn't have enough space in the inventory:*
  - **Blurberry:** Oh, you don't have enough space to take the items. Come back when you do.
- *If the player has enough space:*
  - **Blurberry:** Ok then, to start with make a Fruit Blast. Here, you'll need these ingredients, but I'm afraid I can't give you any more if you mess up.
  - (receives=two lemons, an orange, a pineapple, a cocktail glass, a knife and a cocktail shaker)
  - Blurberry gives you two lemons, one orange, one pineapple, a cocktail shaker, a glass and a knife.

#### Pineapple Punch

- **Blurberry:** So where's my Fruit Blast?
- *If the player doesn't have a cocktail shaker:*
  - (continue|get-shaker)
- *If the player doesn't have a Fruit Blast:*
  - **Blurberry:** I don't know what you have there but it's no Fruit Blast!
- *If the player has a Fruit Blast:*
  - **Player:** Here you go.
  - You give Blurberry the Fruit Blast. He takes a sip...
  - **Blurberry:** Hmmm... not bad, not bad at all.
  - *If the player doesn't have enough space in the inventory:*
    - **Blurberry:** We can continue your training when you have enough space to hold the ingredients for a Pineapple Punch!
  - *If the player has enough space:*
    - **Blurberry:** Now can you make me a Pineapple Punch? I can give you what you need, but again I won't be able to give you any more if you make a mistake.
    - (removes=Fruit Blast) (receives=a cocktail glass, three pineapples, a lemon, a lime and two oranges)
    - Blurberry gives you three pineapples, a pair of oranges, a lemon and a lime.
    - **Blurberry:** Let me know when it's done.

#### Wizard Blizzard

- **Player:** Hello Blurberry.
- **Blurberry:** How are you faring with the Pineapple Punch?
- *If the player doesn't have a cocktail shaker:*
  - (continue|get-shaker)
- *If the player doesn't have a Pineapple Punch:*
  - **Blurberry:** I don't know what you have there but it's no Pineapple Punch!
- *If the player has a Pineapple Punch:*
  - **Player:** Here you go.
  - You give Blurberry the Pineapple Punch. He takes a sip...
  - **Blurberry:** Not bad, not bad at all.... I can certainly sell drinks of that quality.
  - *If the player doesn't have enough space in the inventory:*
    - **Blurberry:** We can continue your training when you have enough space to hold the ingredients for a Wizard Blizzard!
  - *If the player has enough space:*
    - **Blurberry:** Okay then let's try something with some real booze in it! Make me a Wizard Blizzard.
    - (removes=Pineapple Punch) (receives=a cocktail glass, two vodka bottles, a bottle of gin, an orange, a pineapples, a lemon and two limes)
    - Blurberry gives you some vodka, gin, a lemon, a pineapple, a pair of limes and an orange.

#### Short Green Guy

- **Player:** Hello Blurberry.
- **Blurberry:** Hello, how did it go with the Wizard Blizzard.
- *If the player doesn't have a cocktail shaker:*
  - (continue|get-shaker)
- *If the player doesn't have a Wizard Blizzard:*
  - **Player:** I haven't managed to make it yet.
  - **Blurberry:** Ok, it's one Wizard Blizzard I need. done.
- *If the player has a Wizard Blizzard:*
  - **Player:** Here, try some.
  - You give Blurberry the Wizard Blizzard. He takes a sip...
  - **Blurberry:** Well that is both Wizardy and Blizzardy. You're quite a bartender. Okay, let's test you once more. Make me a SGG, then we'll see if you have what it takes.
  - **Player:** A what?
  - **Blurberry:** A Short Green Guy. I've got the ingredients here...
  - (removes=Wizard Blizzard) (receives=a cocktail glass, a bottle of vodka, four limes and equa leaves)
  - **Player:** Ok, I'll try my best.
  - **Blurberry:** I'm sure you'll make a great barman.

#### Finishing up

- **Player:** Hi Blurberry.
- **Blurberry:** So, have you got my Short Green Guy?
- *If the player doesn't have a cocktail shaker:*
  - (continue|get-shaker)
- *If the player doesn't have a Short Green Guy:*
  - **Blurberry:** I don't know what you have there but it's no SGG!
- *If the player has a Short Green Guy:*
  - **Player:** Here you go.
  - You give Blurberry the SGG. He takes a sip...
  - (removes=Short Green Guy)
  - **Blurberry:** Ooh, that's a frisky little number. Very tart, how it should be. Excellent. Well I'm happy to recommend you to the Giannes. You truly are a gnomish bartender now..
  - *If the player has not yet completed the Gnome cooking training with Aluft Gianne snr.:*
    - **Blurberry:{{anchor|training-halffinished}}** Well your training is over Player. Are you interested in some work?
    - **Player:** I may be...
    - **Blurberry:** I think you're almost ready to do some work for Aluft Gianne Jnr. He is in charge of a new family venture: Gnome Food Delivery. There are good tips to be made if you make and deliver gnome foods - though you may have to travel all over Gielinor to fulfill some of the other orders...
    - **Blurberry:** However, you'll need some basic gnome cooking training if you want to work for Lufty. Go and have a chat with his Dad, Aluft Gianne Snr. He'll tell you what you need to do.
    - **Player:** Thanks for your help!
  - *If the player has completed the Gnome cooking training with Aluft Gianne snr.:*
    - **Blurberry:{{anchor|training-finished}}** Aluft Gianne Snr. tells me that you have finished training with him, so I think you're ready to do some work for Aluft Gianne Jnr. He is in charge of the new Gnome Food Delivery service. I've heard there are good tips to be made if you make and deliver gnome foods - though you may have to travel all over Gielinor to fulfill some of the other orders...
    - **Player:** Sounds interesting....
    - **Blurberry:** Go and have a chat with my young Lufty Jnr. and he'll fill you in with details.

#### If the player loses the cocktail shaker

- Select an option{{anchor|get-shaker}}
  - I'm afraid I lost the cocktail shaker you gave to me.
    - **Player:** I'm afraid I lost the cocktail shaker you gave to me.
    - (receives=cocktail shaker)
    - **Blurberry:** I can see how that would make it hard to mix cocktails. I'll give you another one, but please try not lose any more.
  - I've not finished yet.
    - **Player:** I've not finished yet.
    - **Blurberry:** Ok, well let me know when you're done.

### After finishing cocktail training

- ''If you have not yet finished gnome cooking training
  - (above2|training-halffinished)
- ''If you have finished gnome cooking training
  - (above2|training-finished)

### During the advanced NovtumberFest Bar Crawl

- **Player:** I'm doing the NovtumberFest Bar crawl.
- **Blurberry:** Ah, you've come to the best stop on your list! The best drink that we have got; a drunk dragon! It'll cost you 10 coins.
- 10 coins have been removed from your money pouch.
- You buy a Drunk Dragon.
- Your mouth and throat burn as you gulp it down.
- You have completed one of the tasks on your bar crawl card!
