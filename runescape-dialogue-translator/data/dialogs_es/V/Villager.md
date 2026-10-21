# Villager

- **Original Wiki Page**: [Transcript:Villager](https://runescape.wiki/w/Transcript%3AVillager)
- **Letter**: `V`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to

- {{trandom}}
  - (Condition: Diálogo 1:)
    - **Player:** Hola, ¿cómo te va?
    - **Player:** ¿Deseas comerciar? {{anchor|one}}
    - **Villager:** No, no tengo nada de lo que desee deshacerme. Si desea comerciar, hay muchas tiendas y puestos de mercado alrededor.
  - (Condition: Diálogo 2:)
    - **Player:** Hola, ¿cómo te va?
    - **Player:** Estoy buscando una misión. {{anchor|two}}
    - **Villager:** Lamento no poder ayudarte en eso.
  - (Condition: Diálogo 3:)
    - **Player:** Hola, ¿cómo te va?
    - **Player:** Estoy en busca de enemigos para matar. {{anchor|three}}
    - **Villager:** Bueno, siempre están esos Ugthanki salvajes, serpientes y lobos que matar en las afueras de la ciudad.
  - (Condition: Diálogo 4:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** Ya sabes, incluso un reloj parado marca la hora correcta dos veces al día.
    - **Player:** ¿De qué estás hablando?
    - **Villager:** ¡Tonto sin educación! ¡Morirá, morirá!
    - **Player:** Ohhh kaaay, entonces te dejo con eso.
  - (Condition: Diálogo 5:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** Estoy ocupado ahora mismo.
  - (Condition: Diálogo 6:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** Estoy muy bien gracias.
  - (Condition: Diálogo 7:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** ¡Apártate de mi camino, tengo prisa!
  - (Condition: Diálogo 8:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** Estoy bien, ¿cómo estás tú?
    - **Player:** Muy bien, gracias.
  - (Condition: Diálogo 9:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** ¿Te conozco? ¡Tengo prisa!
  - (Condition: Diálogo 10:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** ¡Hola! Buen tiempo que hemos estado teniendo.
  - (Condition: Diálogo 11:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** No está mal, gracias.
  - (Condition: Diálogo 12:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** No es asunto tuyo.
  - (Condition: Diálogo 13:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** Creo que necesitamos un nuevo alcalde. El que tenemos no es muy bueno.
  - (Condition: Diálogo 14:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** Esa es información clasificada.
  - (Condition: Diálogo 15:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** Aquí aquí aquí.
    - **Player:** ¿De qué estás hablando?
    - **Villager:** ¡Tonto sin educación! ¡Morirá, morirá!
    - **Player:** Ohhh kaaay, entonces te dejo con eso.
  - (Condition: Diálogo 16:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** ¿Quién eres?
    - **Player:** Soy un aventurero audaz.
    - **Villager:** Ah, una profesión muy noble.
  - (Condition: Diálogo 17:)
    - **Player:** Hola, ¿cómo te va?
    - **Villager:** ¿Cómo puedo ayudarte?
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Desea negociar?
        - (above|one)
      - [Choice]: Estoy en busca de una misión.
        - (above|two)
      - [Choice]: Estoy en busca de enemigos para matar.
        - (above|three)

### Pickpocket


#### Si el aldeano está consciente{{anchor|thief}}

- {{trandom}}
  - (Condition: Diálogo 1:)
    - **Villager:** {{RSChat|What do you think you're doing?}}
    - No logras robarle el bolsillo al aldeano.
    - Has quedado atónito.
  - (Condition: Diálogo 2:)
    - **Villager:** {{RSChat|Thief! Thief! Get away from me.}}
    - No logras robarle el bolsillo al aldeano.
    - Has quedado atónito.

#### Si el aldeano está inconsciente.

- (receives=5 coins)

### Lure

- **Player:** Psst. Ven aquí. Quiero mostrarte algo.
- **Villager:** ¿Qué es?
- **Player:** ¡Es una sorpresa! Sígueme.

### Knock-Out


#### Si hay otros NPC alrededor

- Quizás no debería hacer esto todavía. Creo que alguien me verá.

#### Si el player no tiene un blackjack equipado

- Necesito un arma diferente para hacer esto, quiero noquearlos, no matarlos.

#### Si el player tiene un blackjack equipado

- (Action: el player golpea al aldeano en la cabeza con la cachiporra. El aldeano cae al suelo.)
- Golpeas al aldeano en la cabeza y lo dejas inconsciente.
- **Villager:** {{RSChat|Zzzzzz}}
- (Action: El aldeano se levanta.)
- **Villager:** {{RSChat|Aghh, my head.}}
- (Condition: Si el player hubiera robado al aldeano:)
  - (continuea|thief)
