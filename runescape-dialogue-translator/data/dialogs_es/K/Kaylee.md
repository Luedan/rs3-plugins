# Kaylee

- **Original Wiki Page**: [Transcript:Kaylee](https://runescape.wiki/w/Transcript%3AKaylee)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### Normalmente

- **Kaylee:** ¡Hola! ¿Qué puedo conseguirte?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Qué cervezas estás sirviendo?
    - **Player:** ¿Qué cervezas estás sirviendo?
    - **Kaylee:** Bueno, tenemos Asgarnian Ale, Wizard's Mind Bomb y Dwarven Stout, todas por solo 3 coins.
    - [Menu]: Selecciona una opción
      - [Choice]: Una cerveza asgarniana, por favor.
        - **Player:** Una cerveza Asgarnian, por favor.
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Kaylee:** ¡Dije 3 coins! ¡No tienes 3 coins! {{anchor|isaid3coins}}
          - **Player:** Lo siento, volveré otro día.
        - (Condition: Si el player tiene suficiente dinero:)
          - (removes=3 coins) (receives=Asgarnian ale)
          - **Player:** Gracias, Kaylee.
      - [Choice]: Probaré la bomba mental.
        - **Player:** Probaré la bomba mental.
        - (Condition: Si el player no tiene suficiente dinero:)
          - (above|isaid3coins)
        - (Condition: Si el player tiene suficiente dinero:)
          - (removes=3 coins) (receives=Wizard's mind bomb)
          - **Player:** Gracias, Kaylee.
      - [Choice]: ¿Puedo tener una Dwarven Stout?
        - **Player:** ¿Puedo tener una Dwarven Stout?
        - (Condition: Si el player no tiene suficiente dinero:)
          - (above|isaid3coins)
        - (Condition: Si el player tiene suficiente dinero:)
          - (removes=3 coins) (receives=Dwarven stout)
          - **Player:** Gracias, Kaylee.
      - [Choice]: No me siento como ninguno de esos.
        - **Player:** No me apetece nada de eso.
  - [Choice]: cond=After a certain point in Recipe for Disaster: Freeing the Mountain Dwarf|¿Qué puedes decirme sobre los enanos y la cerveza?
    - **Player:** ¿Qué puedes decirme sobre los enanos y la cerveza?
    - **Kaylee:** Oh, eres tú otra vez. ¿Ya olvidaste el secreto?
    - **Player:** No... Simplemente... lo perdí.
    - **Kaylee:** Mmmmm... el secreto está en el oro. Echa una moneda de oro en cerveza asgarniana y obtendrás esta extraña cerveza dorada que parece encantar a los enanos. Creo que se sienten atraídos genéticamente por el oro.
    - **Player:** Gracias, esta vez no lo olvidaré... err... extravío.

#### Con un barril de hidromiel antes de realizar una entrega a Rising Sun durante el evento The Need for Mead

- **Player:** Me preguntaba si podrías darnos algún comentario sobre este hidromiel.
- **Kaylee:** Reconocería esos viejos barriles en cualquier lugar.
- **Kaylee:** Me encantaría probar el próximo lote de hidromiel de Leslie.
- (removes=keg of mead) (receives=50 nectar)
- (ver|néctar)
- ((Se muestra en una ventana emergente:))
  - (Ventana emergente: encontrarás 50 x néctar cuando entregas el barril de hidromiel.|color=#00FF00)
  - (continue)
- **Kaylee:** El hidromiel no es mi bebida favorita, pero es muy agradable.
- **Kaylee:** En realidad, ese puede ser el mejor hidromiel que he bebido.
- **Kaylee:** Los sabores son muy sutiles. Delicioso.
- **Player:** Fantástico, lo pasaré. ¡Gracias!

### Using coins on Kaylee

- **Kaylee:** ¡Gracias!
- (removes=one coin)
