# Isma'il the Kebab seller

- **Original Wiki Page**: [Transcript:Isma'il the Kebab seller](https://runescape.wiki/w/Transcript%3AIsma%27il%20the%20Kebab%20seller)
- **Letter**: `I`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before The Feud

- **Player:** Hola.
- **Isma'il the Kebab seller:** Hola. ¿Qué puedo hacer por ti?
- **Player:** No sé, ¿qué puedes hacer por mí?
- **Isma'il the Kebab seller:** Bueno, eso depende.
- **Player:** ¿Depende de qué?
- **Isma'il the Kebab seller:** Depende de si te gustan los kebabs o no.
- **Player:** ¿Por qué?
- **Isma'il the Kebab seller:** Dado que estoy en la industria de la construcción de kebab, principalmente ayudo a las personas que necesitan un kebab.
- **Player:** Bueno, entonces, ¿qué tipo de kebabs construyes?
- **Isma'il the Kebab seller:** Ofrezco dos tipos diferentes de kebabs: el kebab común y corriente que se ve en Gielinor y que disfrutan muchos enanos ebrios, y mi especialidad, el kebab extra picante. Entonces ¿cuál será?
- **Isma'il the Kebab seller:** ¿O incluso se requieren mis servicios?
- [Menu]: Selecciona una opción
  - [Choice]: Quiero un kebab, por favor.
    - **Player:** Quiero un kebab, por favor.
    - **Isma'il the Kebab seller:** Serán tres gold coins, por favor.
    - (Condition: If the player does not have 3 coins:)
      - **Player:** Parece que no he traído suficiente dinero. Lo siento.
      - No puedes permitirte eso.
    - (Condition: If the player has 3 coins:)
      - (removes=3 coins) (receives=kebab)
      - **Isma'il the Kebab seller:** Aquí tienes.
      - **Player:** Gracias.
      - **Isma'il the Kebab seller:** ¿Hay algo más que pueda hacer por ti?
      - {{anchor|else}} [Menú]: seleccione una opción
        - [Choice]: Sí, gracias.
          - (initial)
        - [Choice]: No gracias, estoy bien.
          - **Player:**No, gracias, estoy bien.
          - **Isma'il the Kebab seller:** Vuelve pronto, me vendrían bien algunos clientes más.
  - [Choice]: ¿Podría darme un kebab extra caliente, por favor?
    - **Player:** ¿Podría darme uno de esos locos kebabs calientes tuyos?
    - **Isma'il the Kebab seller:** Un súper kebab, así es. Tenga cuidado, realmente son tan calientes como parecen.
    - **Player:** Claro, claro.
    - (Condition: If the player does not have 5 coins:)
      - **Player:** Parece que no he traído suficiente dinero. Lo siento.
      - No puedes permitirte eso.
    - (Condition: If the player has 5 coins:)
      - (removes=5 coins) (receives=super kebab)
      - **Isma'il the Kebab seller:** Aquí tienes.
      - **Player:** Gracias.
      - **Isma'il the Kebab seller:** ¿Hay algo más que pueda hacer por ti?
      - (continuea|else)
  - [Choice]: ¿Me venderías esa botella de salsa especial para kebab?
    - **Player:** ¿Me venderías esa botella de salsa especial para kebab?
    - **Isma'il the Kebab seller:** Bueno, eso depende de lo que tengas en mente.
    - **Player:** Tranquilízate, no tengo intención de montar una tienda de kebab rival.
    - **Isma'il the Kebab seller:** Pues bien, ¿para qué lo quieres?
    - **Player:** No lo sé, pero creo que podría divertirme un poco con ello.
    - **Isma'il the Kebab seller:** No lo vas a poner en la bebida de Jalal the Drunk, ¿verdad? Eso es lo que pasó la última vez que le di la salsa a alguien.
    - **Player:** No, eso sería un poco cliché. Creo que se me ocurrirá algo más original.
    - (Condition: If the player does not already have the red hot sauce in backpack or in bank:)
      - (receives=Red hot sauce)
      - **Isma'il the Kebab seller:** Solo ten cuidado con él, es lo suficientemente potente como para hacer correr a un camello.
      - **Player:** Muchas gracias.
      - **Isma'il the Kebab seller:** ¿Hay algo más que pueda hacer por ti?
      - (continuea|else)
    - (Condition: If the player already has the red hot sauce in backpack:)
      - **Isma'il the Kebab seller:** No creo que te lo regale, por el simple hecho de que ya tienes uno sobresaliendo de tu bolso. Tengo que administrar un negocio aquí.
      - **Isma'il the Kebab seller:** ¿Hay algo más que pueda hacer por ti?
      - (continuea|else)
    - (Condition: If the player already has the red hot sauce in bank:)
      - **Isma'il the Kebab seller:** ¿No te acabo de dar ya una botella de esto?
      - **Player:** Es posible que sí. ¿Alguna posibilidad de otro?
      - **Isma'il the Kebab seller:** Estoy tratando de administrar un negocio aquí, no una organización benéfica.
      - **Isma'il the Kebab seller:** ¿Hay algo más que pueda hacer por ti?
      - (continuea|else)
  - [Choice]: ¿Cuál es la diferencia entre el kebab estándar y el extra picante?
    - **Player:** ¿Cuál es la diferencia entre el kebab estándar y el extra picante?
    - **Isma'il the Kebab seller:** Si te dijera eso, tendría que matarte. La venta de kebab es una industria feroz. El kebab extra picante me da una ventaja competitiva sobre el resto y si tuviera que divulgar mis secretos a cada aventurero que pasa, pronto desaparecería.
    - **Player:** ¡Así que no hay diferencia excepto la salsa que usas entonces!
    - **Isma'il the Kebab seller:** ¡Shh! Mantén la voz baja. Deberías haberme dicho que eras del sindicato.
    - [Menu]: Selecciona una opción
      - [Choice]: Quiero un kebab, por favor.
        - (arriba)
      - [Choice]: ¿Podría darme un kebab extra caliente, por favor?
        - (arriba)
      - [Choice]: ¿Me venderías esa botella de salsa especial para kebab?
        - (arriba)
      - [Choice]: Escucha, tengo que correr. Te veré más tarde.
        - **Player:** Escucha, tengo que correr. Te veré más tarde.

### After The Feud

- **Player:** Hola.
- **Isma'il the Kebab seller:** Hola. ¿Qué puedo hacer por ti?
- [Menu]: Selecciona una opción
  - [Choice]: Quiero un kebab, por favor.
    - (arriba)
  - [Choice]: ¿Me podría dar un kebab extra caliente?
    - (arriba)
  - [Choice]: ¿Me venderías esa botella de salsa especial para kebab?
    - (arriba)
  - [Choice]: ¿Cuál es la diferencia entre el kebab estándar y el extra picante?
    - (arriba)
  - [Choice]: Necesito alguna información.
    - **Player:** Necesito información.
    - **Isma'il the Kebab seller:** Si lo que necesita es información, hay muchas personas mejores que yo para pedírsela y que podrían ayudarle. Uno de los pilluelos callejeros de la ciudad o quizás el borracho local. Puede que sea muchas cosas para muchas personas diferentes, pero no soy un chismoso.
    - **Isma'il the Kebab seller:** ¿Hay algo más que pueda hacer por ti?
    - {{anchor|else2}} [Menú]: seleccione una opción
      - [Choice]: Sí, gracias.
        - **Player:** Sí, gracias.
        - (initial)
      - [Choice]: No gracias, estoy bien.
        - **Player:**No, gracias, estoy bien.
