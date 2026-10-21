# Romily Weaklax

- **Original Wiki Page**: [Transcript:Romily Weaklax](https://runescape.wiki/w/Transcript%3ARomily%20Weaklax)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Romily Weaklax:** Hola y bienvenido a mi pastelería, ¿en qué puedo ayudarte?
- {{anchor|standard}} [Menú]: seleccione una opción
  - [Choice]: Me gustaría comprar algunas tartas.
    - (opens=Pie Shop)
  - [Choice]: cond=If the player does not have an active pie request|¿Necesitas ayuda?
    - **Player:** ¿Necesitas ayuda?
    - **Romily Weaklax:** En realidad podría, verás, me estoy quedando sin existencias y no tengo tiempo para hornear más pasteles. ¿Estarías dispuesto a hornearme algunos pasteles? Te pagaré bien por ellos.
    - [Menu]: Selecciona una opción
      - [Choice]: Claro, ¿qué necesitas?
        - **Player:** Claro, ¿qué necesitas?
        - **Romily Weaklax:** Genial, ¿puedes hornearme [número] [type of pie] por favor?
      - [Choice]: Lo siento, no puedo ayudarte.
        - **Player:** Lo siento, no puedo ayudarte.
  - [Choice]: cond=If the player has an active pie request|Tengo esos pasteles que querías.
    - **Player:** Tengo esos pasteles que querías.
    - (Condition: Si el player no tiene las tartas:)
      - **Romily Weaklax:** No parece que tengas ninguno de los [número] [type of pie] que solicité.
    - (Condition: Si el player tiene solo algunos de los pasteles solicitados:)
      - (removes=pies) (receives=coins)
      - **Romily Weaklax:** Gracias, si pudieras traerme el otro [remaining number], ¡sería genial!
    - (Condition: Si el player tiene todos los pasteles solicitados:)
      - (removes=pies) (receives=coins)
      - **Romily Weaklax:** ¡Muchas gracias!
  - [Choice]: Estoy bien gracias.
    - **Player:** Estoy bien, gracias.

### With a wild pie in inventory

- **Romily Weaklax:** Hola y bienvenido a mi pastelería. ¡Mi palabra! Qué pastel huele muy bien el que tienes. ¿Es para mí?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, lo es.
    - **Player:** Sí, lo es.
    - **Romily Weaklax:** ¡Oh, qué espléndido! Déjame quitarte eso entonces.
    - (removes=wild pie)
    - {{RSFontAchievement|Who Ate All the Pie?|Talk to Romily Weaklax and give him a wild pie.}}
    - **Romily Weaklax:** Ahora, ¿necesitabas algo más?
    - (continuea|standard)
  - [Choice]: No, es para... alguien más.
    - **Player:** No, es para... alguien más.
    - **Romily Weaklax:** Oh, ya veo. ¿Había algo más que necesitabas?
    - (continuea|standard)
