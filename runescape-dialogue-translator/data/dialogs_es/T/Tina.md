# Tina

- **Original Wiki Page**: [Transcript:Tina](https://runescape.wiki/w/Transcript%3ATina)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Normalmente

- **Tina:** ¡Hola! ¿Qué puedo conseguirte?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Qué cervezas estás sirviendo?
    - **Player:** ¿Qué cervezas estás sirviendo?
    - **Tina:** Bueno, tenemos Asgarnian Ale, Wizard's Mind Bomb y Dwarven Stout, todas por solo 3 coins.
    - [Menu]: Selecciona una opción
      - [Choice]: Una cerveza asgarniana, por favor.
        - **Player:** Una cerveza Asgarnian, por favor.
        - (Condition: If the player does not have enough money:)
          - **Tina:** ¡Dije 3 coins! ¡No tienes 3 coins! {{anchor|isaid3coins}}
          - **Player:** Lo siento, volveré otro día.
        - (Condition: If the player has enough money:)
          - (removes=3 coins) (receives=Asgarnian ale)
          - **Player:** Gracias, Tina.
      - [Choice]: Probaré la bomba mental.
        - **Player:** Probaré la bomba mental.
        - (Condition: If the player does not have enough money:)
          - (above|isaid3coins)
        - (Condition: If the player has enough money:)
          - (removes=3 coins) (receives=Wizard's mind bomb)
          - **Player:** Gracias, Tina.
      - [Choice]: ¿Puedo tener una Dwarven Stout?
        - **Player:** ¿Puedo tener una Dwarven Stout?
        - (Condition: If the player does not have enough money:)
          - (above|isaid3coins)
        - (Condition: If the player has enough money:)
          - (removes=3 coins) (receives=Dwarven stout)
          - **Player:** Gracias, Tina.
      - [Choice]: No me siento como ninguno de esos.
        - **Player:** No me apetece nada de eso.
  - [Choice]: cond=After a certain point in Recipe for Disaster: Freeing the Mountain Dwarf|¿Qué puedes decirme sobre los enanos y la cerveza?
    - **Player:** ¿Qué puedes decirme sobre los enanos y la cerveza?
    - **Tina:** Oh, eres tú otra vez. ¿Ya olvidaste el secreto?
    - **Player:** No... Simplemente... lo perdí.
    - **Tina:** Mmmmm... el secreto está en el oro. Echa una moneda de oro en cerveza asgarniana y obtendrás esta extraña cerveza dorada que parece encantar a los enanos. Creo que se sienten atraídos genéticamente por el oro.
    - **Player:** Gracias, esta vez no lo olvidaré... err... extravío.

#### Con un barril de hidromiel antes de realizar una entrega a Rising Sun durante el evento The Need for Mead

- **Player:** Me preguntaba si podrías darnos algún comentario sobre este hidromiel.
- **Tina:** Reconocería esos viejos barriles en cualquier lugar.
- **Tina:** Me encantaría probar el próximo lote de hidromiel de Leslie.
- (removes=keg of mead) (receives=50 nectar)
- (ver|néctar)
- ((Shown in a pop-up:))
  - (Pop-up: You find 50 x Nectar as you hand over the keg of mead.|colour=#00FF00)
  - (continue)
- **Tina:** El hidromiel no es mi bebida favorita, pero es muy agradable.
- **Tina:** En realidad, ese puede ser el mejor hidromiel que he bebido.
- **Tina:** Los sabores son muy sutiles. Delicioso.
- **Player:** Fantástico, lo pasaré. ¡Gracias!

### Using coins on Tina

- **Tina:** ¡Gracias!
- (removes=one coin)
