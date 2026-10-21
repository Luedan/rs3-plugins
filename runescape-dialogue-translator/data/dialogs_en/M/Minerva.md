# Minerva

- **Original Wiki Page**: [Transcript:Minerva](https://runescape.wiki/w/Transcript%3AMinerva)
- **Letter**: `M`

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Whose tomb is this? It must have been someone special for the city of Falador to honour them with such a resting place.
- **Minerva:** My family's history is deeply rooted in the very foundations of Falador, long before a castle even existed.
- **Minerva:** She served King Raddallin faithfully, and travelled to every corner of each kingdom to help with the unification of what then became the Kingdom of Asgarnia.
- **Minerva:** During her travels, she learned everything she could from the various tribes and villages she passed through, mastering everything she was taught.
- **Minerva:** As Asgarnia flourished, she continued to serve her king before eventually passing unto the light of Saradomin. Forever to be remembered.
- **Player:** What was her name?
- **Minerva:** Her name was Meira.
- **Minerva:** Before she passed, to mark her place in history and as a gesture of all she did for the king, she was honoured with a cape made of the most magical thread.
- **Minerva:** The cape was enchanted by someone lost to the history books. However, the enchantment they cast prevents unworthy individuals from wearing the cape.
- **Player:** But you can wear it?
- **Minerva:** Meira's mastery over all the skills of the world became somewhat of a creed for our family, so we've continued her legacy by passing on what she started.
- **Minerva:** Then came a time where we'd honour those outside our family with such a blessing.
- (Condition: If asking about the grave after having inserted the keystone:)
  - (continue|After inserting the blurite keystone)
- **Player:** If I master all skills, can I wear the cape?
- **Minerva:** If you master all skills and are able to craft a keystone made of rubies, emeralds and sapphires set into some blurite, then place said keystone into that slot you see there on the tomb.
- **Minerva:** The tomb itself will decide if you're worthy. Then - and only then - will I offer you the chance to wear the cape.
- **Player:** I'll try that!
- **Minerva:** Oh, and there is one condition.
- **Player:** Hmm?
- **Minerva:** If one day you do manage to earn the cape. You're not to sell it or donate it to the Varrock Museum. They've been trying to get their hands on this for a while. It's not a garment to lay unworn and gathering dust.
- [A blurite keystone can be smelted in a furnace using blurite, sapphires, rubies and emeralds.]

### After inserting the blurite keystone

- [Menu]: What would you like to say?
  - [Choice]: What's your name?
    - **Minerva:** My name is Minerva. Pleasure to finally meet you, Player.
    - **Player:** But I didn't tell you my name.
    - **Minerva:** You've gained quite the reputation and word tends to travel swiftly around these parts.
    - **Player:** Just doing what I do! Good to meet you.
    - (previous)
  - [Choice]: Am I worthy enough to buy that cape?
    - **Minerva:** Thank you! It was a long path, but that's because I want to take in everything there is to know.
    - **Player:** I've mastered all skills!
    - **Minerva:** So you have, Player. This incredible achievement means you're worthy of wearing the cape. Though the craftsmanship of such a cape requires time and effort, so it'll come at a cost.
    - **Minerva:** It seems fair to offer you the cape for {{fe|{{globals|total skills}} * 120000}} coins - 120,000 for each skill you have mastered.
    - [Menu]: Pay {{fe|{{globals|total skills * 120000}} coins for a true mastery cape?}}
      - [Choice]: Sure!
        - **Player:** That'd be great, thank you.
        - (removes={{fe|{{globals|total skills) * 120000}} coins}} (receives=a master max cape and hood)
        - **Minerva:** Here you go! Enjoy and please, look after it.
        - **Minerva:** Don't go selling it to Varrock museum!
      - [Choice]: No, thanks.
        - **Player:** I'll have to pass up on that offer for now. Thank you, though!
  - [Choice]: What is this grave?
    - (above|Standard dialogue)
  - [Choice]: What is the symbol on the top of the grave?
    - **Minerva:** It's a very simple keystone you crafted to prove you've mastered all of RuneScape's skills.
    - **Player:** But it was really easy to make. Just a chunk of metal and a handful of gems. Anyone with a blunt hammer and dull chisel could have made that.
    - **Minerva:** All this time spent skilling and you still don't believe in magic, eh?
    - **Player:** I suppose. It didn't feel very magical, though.
    - **Minerva:** That is because the magic is in you, Player. You said it yourself, it's just a chunk of metal and a few gems. But YOU were the one who made it.
    - (previous)
