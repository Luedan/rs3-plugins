# Tindel Marchant

- **Original Wiki Page**: [Transcript:Tindel Marchant](https://runescape.wiki/w/Transcript%3ATindel%20Marchant)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue


#### Hablando con él

- **Tindel Marchant:{{anchor|start}}** ¡Hola! Bienvenidos a mi boutique especial de antigüedades.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué haces aquí?
    - **Player:** ¿Qué haces aquí?
    - **Tindel Marchant:** Soy un especialista en identificar armas exóticas y antiguas, específicamente espadas, pero planeo expandirme. Si tienes armas viejas y oxidadas que quieres que revise, enséñamelas, págame 100 de oro y veré si tienes una antigüedad en tus manos. También puedo reparar algunas armas y armaduras antiguas, solo muéstrame el artículo y te diré si puedo repararlo y por cuánto.
    - (Condition: If the 'They're Long and Pointy' achievement hasn't been completed:)
      - {{RSFontAchievement|They're Long and Pointy}}
      - (continue)
    - (initial|init)
  - [Choice]: ¿Qué implica?
    - **Player:** ¿Qué implica?
    - **Tindel Marchant:** Bueno, págame 100 de oro y veré si alguna espada oxidada que hayas encontrado realmente vale algo. ¡Algunos de ellos podrían valer algo de dinero! Sin embargo, si se trata de un artículo antiguo, me reservo el derecho de comprarlo inmediatamente para agregarlo a mi colección personal. Te daré un precio justo por ello.
    - (initial|init)
  - [Choice]: ¿Qué obtengo de esto?
    - **Player:** ¿Qué obtengo de esto?
    - **Tindel Marchant:** Si puedo recuperar la espada con mis propias habilidades especializadas, te la devolveré en óptimas condiciones. Si es una antigüedad, te daré lo que creo que vale y, en general, pago bastante bien. Sin embargo, si es sólo un pedazo de basura, simplemente te daré las malas noticias y me desharé del artículo por ti.
    - (initial|init)
  - [Choice]: Ok, ¡lo intentaré!
    - **Player:** Ok, ¡lo intentaré!
    - (Condición: Si el player no tiene espadas oxidadas en el inventario:) {{anchor|identify}}
      - **Tindel Marchant:** Lo siento, amigo mío, pero parece que no tienes ninguna espada que deba identificarse.
    - (Condition: If the player has a rusty sword in the inventory:)
      - (removes=100 coins)
      - [Le entregas a Tindel 100 coins más la espada oxidada.]
      - (removes=rusty sword) (receives=a sword of a random metal)
      - **Tindel Marchant:** Ahí tienes amigo, resultó ser un <sword name>.
      - [Tindel te regala un <sword name>.]
  - [Choice]: Bien, gracias.
    - **Player:** Vale, gracias.

#### Opción Dar-Espada

- (arriba2|identificar)

#### Opción de reparar todo

- **Tindel Marchant:** Reparar o recargar artículos degradables cuesta dinero. Si desea que repare todos sus artículos, tomaré la tarifa correcta de su inventario o bolsa de dinero.
- [Menu]: ¿Reparar o recargar todos tus artículos?
  - [Choice]: Sí {{anchor|repair}}
    - (Condition: If the player has no items that can be repaired:)
      - **Tindel Marchant:** No tienes ningún artículo que pueda repararse o recargarse.
    - (Condition: If the player has items that can be repaired:)
      - **Tindel Marchant:** ¡Todo listo! Eso te costó <amount> coins.
      - Todos sus elementos han sido reparados para <amount> coins.
  - [Choice]: No
    - (end)
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (above|repair)

### Ring-bell option of the Antiques Shop Stall

- [Llamas para llamar la atención.]
- (continuea|start)
