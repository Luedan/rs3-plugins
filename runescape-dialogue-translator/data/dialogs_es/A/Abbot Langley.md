# Abbot Langley

- **Original Wiki Page**: [Transcript:Abbot Langley](https://runescape.wiki/w/Transcript%3AAbbot%20Langley)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{dialogue|npc}}
{{transcript npc|Abbot Langley}}

### Standard dialogue

- **Abbot Langley:** Saludos viajero.
- [Menu]: Elige una opción:
  - [Choice]: ¿Puedes curarme? Estoy herido.
    - **Player:** ¿Puedes curarme? Estoy herido.
    - **Abbot Langley:** Vale.
    - Abbot Langley coloca sus manos sobre tu cabeza. Te sientes un poco mejor.
  - [Choice]: ¿No está este lugar construido un poco alejado?
    - **Player:** ¿No está este lugar construido un poco apartado?
    - **Abbot Langley:** ¡De hecho, nos gusta así! Nos molestamos menos. ¡Todavía recibimos una gran cantidad de viajeros que buscan santuario y curación aquí tal como está!
  - [Choice]: cond=If the player has not gained access to the upper level of the Monastery|¿Cómo puedo adentrarme más en el Monasterio?
    - **Player:** ¿Cómo puedo adentrarme más en el Monasterio?
    - **Abbot Langley:** Lo siento, pero solo los miembros de nuestra orden pueden ingresar al segundo nivel del monasterio.
    - [Menu]: Seleccione una opción|ancla=unirse
      - [Choice]: Bueno, ¿puedo unirme a tu pedido?
        - **Player:** Bueno, ¿puedo unirme a tu pedido?
        - (Condition: If the player is below level 31 Prayer:)
          - **Abbot Langley:** No. Lo siento, pero siento que no eres lo suficientemente devoto.
          - Necesitas un nivel de oración de 31 para unirte a la orden.
        - (Condition: If the player is level 31 Prayer or greater:)
          - **Abbot Langley:** Ok, veo que eres alguien adecuado para nuestro pedido. Puedes unirte.
      - [Choice]: Ah, lo siento.
        - **Player:** Oh, lo siento.

### Attempting to climb a ladder before joining the monastery


#### escalera oriental

- **Abbot Langley:** Sólo los miembros de nuestra orden pueden subir allí.
- (Action: continuar|unirse)

#### escalera occidental

- Un monje cercano te mira fijamente. Quizás deberías hablar con él antes de subir la escalera.

### Treasure Trails

- **Abbot Langley:** ¡Felicitaciones, viajero!
- (removes=the old clue scroll (hard))
- ((If the trail continues:))
  - (receives=a new clue scroll (hard))
  - {{tbox|pic=Clue scroll (hard) detail.png|Abbot Langley has given you another clue scroll.}}
- ((If the trail ends:))
  - (receives=reward casket (hard))
  - {{tbox|pic=Reward casket (hard) detail.png|You've found a casket!}}
