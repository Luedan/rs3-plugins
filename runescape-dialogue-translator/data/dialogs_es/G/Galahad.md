# Galahad

- **Original Wiki Page**: [Transcript:Galahad](https://runescape.wiki/w/Transcript%3AGalahad)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### Antes del Santo Grial

- **Galahad:** Bienvenido a mi casa. ¡Es raro para mí tener invitados! ¿Quieres una taza de té? Pondré la tetera a hervir.
- El hermano Galahad cuelga una tetera sobre el fuego.
- **Player:** ¿Te sientes solo aquí solo?
- **Galahad:** A veces sí, sí. Todavía no hay mucha gente que comparta mi solidaridad, ya que el Saradomin que conozco es muy diferente al que se adora aquí.
- **Galahad:** Medio momento, tu taza de té está lista.
- [El hermano Galahad te ofrece una taza de té.]
- (receives=cup of tea)
- (Condition: If the player is speaking to him for the first time:)
  - {{RSFontAchievement|Stir, Galahad|Have Sir Galahad make you a cup of tea.}}

#### Después del Santo Grial

- **Galahad:** ¡Bienvenido de nuevo! ¿Quieres una taza de té? Pondré la tetera a hervir.
- El hermano Galahad cuelga una tetera sobre el fuego.
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¡Le devolví el Santo Grial a Camelot!
    - **Player:** ¡Le devolví el Santo Grial a Camelot!
    - **Galahad:** ¡Estoy impresionado! Eso es algo que nunca pude hacer. Medio momento, tu taza de té está lista.
    - (Condition: If the player does not have at least one free backpack space:)
      - [El hermano Galahad te ofrece una taza de té.]
      - **Galahad:** Dios mío, no tienes espacio para guardarlo. <br/>Será mejor que no lo desperdicies...
      - (Action: Galahad bebe la taza de té.)
      - **Galahad:** {{RSChat|Aaah, nothing like a nice cuppa tea!}}
    - (Condition: If the player has at least one free backpack space:)
      - (receives=cup of tea)
      - [El hermano Galahad te ofrece una taza de té.]
  - [Choice]: cond=If the player lost the holy table napkin:|He perdido la santa servilleta.
    - **Player:** He perdido la servilleta sagrada.
    - (Condition: If the player does not have at least one free backpack space:)
      - **Galahad:** Dios mío. Pero no puedo darte otro a menos que liberes algo de espacio en el inventario.
      - **Galahad:** Los aventureros siempre tienen demasiadas posesiones; Me alegro de haber elegido una vida más sencilla. Ahora, veamos sobre ese té...
      - (continuea|receive-tea)
    - (Condition: If the player has at least one free backpack space:)
      - **Galahad:** Por suerte tuve más de uno, ¿eh?
      - [Galahad te da otra servilleta.<br/>Te guiña un ojo.]
      - **Galahad:** ¡Intenta no perder este!<br/>Oh, veo que tu taza de té está lista.
      - (continuea|receive-tea)
  - [Choice]: Es muy pacífico aquí.
    - **Player:** Es muy tranquilo aquí.
    - **Galahad:** Sí, creo que la tranquilidad me ayuda a acercarme cada vez más a comprender el verdadero significado de la vida.
    - **Player:** ¿El verdadero significado de la vida?<br/>¿Puedes decirme cuál es?
    - **Galahad:** Medio momento, tu taza de té está lista.
    - (continuea|receive-tea)
