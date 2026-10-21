# Auguste

- **Original Wiki Page**: [Transcript:Auguste](https://runescape.wiki/w/Transcript%3AAuguste)
- **Letter**: `A`

---

## Dialogue Transcript

{{transcript npc|Auguste}}

### Before Enlightened Journey

- {{tact|see|Enlightened Journey#Starting Out}}

### First time after completing Enlightened Journey

- **Auguste:** Hello, Player. It is good to see you again. My enterprise has grown since we last met. I've expanded all over Gielinor!
- **Auguste:** If you'd like to go to a new location, you will have to help fly the balloon again. Some of the routes are very dangerous!
- **Auguste:** But each route you complete will earn you Firemaking experience.
- **Auguste:** Once you've opened a route, it only costs 1 log of the corresponding type to travel there again, from any location you've already opened!
- **Auguste:** I have also hired assistants to watch over the balloons at each new location we go to. They will help you get where you want to go.
- **Auguste:** Do you want to use the balloon? Just so you know, some locations require special logs and high Firemaking skills.
- {{tact|continue}}

### Standard dialogue

- **Auguste:** Do you want to use the balloon? Just so you know, some locations require special logs and high Firemaking skills.
- {{tselect|Choose an option:}}
  - {{topt|Yes.}}
    - (opens=Balloon transport system)
  - {{topt|No.}}
    - **Player:** No.
  - {{topt|Could you tell me how to make an origami balloon?}}
    - **Player:** Could you tell me how to make an origami balloon?
    - **Auguste:** First, use the papyrus on the ball of wool. The papyrus is folded into an origami box and the yarn will support the heat source.
    - **Auguste:** Next, add the unlit candle to the balloon structure. It will act as the heat source.
    - **Auguste:** Now you have an origami balloon!
    - **Auguste:** If you use your origami balloon with any dye, you can change the colour.
    - **Auguste:** You can release the balloon and watch it float in the air, just use a tinderbox on it.
  - {{topt|cond=If the player has a bomber cap and gnome goggles in their backpack|Could you combine my cap and goggles?}}
    - (removes=bomber cap and gnome goggles)
    - (receives=cap and goggles)
    - **Auguste:** There you go! You look like a true airship pilot now.
  - {{topt|cond=If the player has lost their bomber cap or jacket|Could you replace some items for me?}}
    - (Condition: If the player still has their bomber cap:)
      - **Auguste:** You still seem to have your cap.
    - (Condition: If the player is missing their bomber cap:)
      - (receives=bomber cap)
      - **Auguste:** Here's your cap. Try to keep better track of it.
  - (Condition: If the player still has their bomber jacket:)
    - **Auguste:** You don't need a new jacket; you still have your original one.
  - (Condition: If the player is missing their bomber jacket:)
    - (receives=bomber jacket)
    - **Auguste:** Here's your jacket, to keep you warm during flight.

#### Store-logs option

- {{tselect|Give Auguste all your logs?}}
  - {{topt|Hand over your logs.}}
    - {{tcond|If the player has logs in backpack:}}
      - (removes=all logs in backpack)
      - **Auguste:** Thanks! You now have [number] charges.
    - {{tcond|If the player does not have logs in backpack:}}
      - **Auguste:** You don't have any logs that I can store. You currently have [number] charges.
  - {{topt|Cancel}}
    - {{tact|end}}

#### Fly option

- (opens=Balloon transport system)

#### Check charges option

- You have [number] charges.
