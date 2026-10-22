# Gerrant

- **Original Wiki Page**: [Transcript:Gerrant](https://runescape.wiki/w/Transcript%3AGerrant)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Port Sarim

- **Gerrant:** ¡Bienvenido! Puedes comprar equipo de pesca en mi tienda. También compraremos cualquier cosa que te pillen.
- [Menu]: Elige una opción:
  - [Choice]: cond=After partial completion of Heroes' Quest|Quiero saber cómo pescar una anguila de lava.
    - **Gerrant:** Anguilas de lava, ¿eh? Esa es una pregunta complicada, claro está. Necesitarás una caña de pescar a prueba de lava. El método para hacer esto sería tomar una caña de pescar común y luego cubrirla con aceite ignífugo.
    - (Condition: After completion of Heroes' Quest:)
      - **Gerrant:** Por supuesto, eso ya lo sabías.
      - (continue)
    - **Player:** Entonces, ¿dónde puedo pescar anguilas de lava?
    - **Gerrant:** Mazmorra Taverley o laberinto de lava en Wilderness.
  - [Choice]: cond=If the player has lost their oily fishing rod|He perdido mi caña de pescar aceitosa.
    - [Gerrant reemplaza tu caña de pescar aceitosa.]
    - (receives=oily fishing rod)
  - [Choice]: Veamos qué tienes entonces.
    - **Player:** Veamos qué tienes entonces.
    - (opens=Gerrant's Fishy Business)
  - [Choice]: Lo siento, no estoy interesado.
    - **Player:** Lo siento, no estoy interesado.

### Treasure Trails

- **Gerrant:** ¡Lo has logrado!
- (removes=the old clue scroll (hard))
- ((If the trail continues:))
  - (receives=a new clue scroll (hard))
  - [¡Gerrant te ha dado otro pergamino de pistas!]
- ((If the trail ends:))
  - (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
