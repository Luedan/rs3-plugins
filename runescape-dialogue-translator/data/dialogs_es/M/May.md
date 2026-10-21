# May

- **Original Wiki Page**: [Transcript:May](https://runescape.wiki/w/Transcript%3AMay)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### When talked to

- **Mayo:** ¡Saludos [travelerZZCMD0ZZ/World Guardian]! ¿Qué puedo hacer por ti hoy?
- (Condition: Sólo en la primera conversación:)
  - **Player:** ¿Quién eres? ¿Qué es todo esto?
  - **May:** Bueno, soy May, y esto...
  - **Mayo:** ¡Este es mi último esfuerzo! ¡Quiero ayudar a aventureros como tú a convertirse en los héroes para los que están hechos!
  - **Player:** ¿Cómo puedes ayudarme?
  - **Mayo:** Bueno, tengo una variedad de artículos y beneficios para ayudarte a hacer tu vida un poco más fácil.
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: Abre la tienda.
    - (opens=May's Quest Caravan)
  - [Choice]: Reclaim items.|cond=Si hay artículos para reclamar:
    - (Condition: Si solo se pueden recuperar objetos que no sean de combate:)
      - (Condition: Sin suficiente espacio backpack:)
        - **Mayo:** No tienes suficiente espacio en el inventario para que te dé todo ahora mismo.
      - (Condition: Con suficiente espacio backpack:)
        - (receives=missing items)
        - **Mayo:** He colocado tus recompensas en tu inventario.
    - (Condition: Si solo se pueden recuperar objetos de combate:)
      - (Condition: Sin suficiente espacio backpack:)
        - (Condition: Si tan solo se pudiera recuperar Vanquish:)
          - **Mayo:** No tienes suficiente espacio libre para reclamar Vanquish.
        - (Condition: Si se pueden reclamar otros objetos además de Vanquish:)
          - **Mayo:** No tienes suficiente espacio libre para reclamar las piezas del Equipo de Pruebas que te faltan.
      - (Condition: Con suficiente espacio backpack:)
        - (Condition: Si tan solo se pudiera recuperar Vanquish:)
          - [pic=Coins 250 detail.png]
          - (continue)
        - (Condition: Si se pueden reclamar otros objetos además de Vanquish:)
          - [pic=Coins 250 detail.png]
          - (continue)
        - [Menu]: ¿Recuperar piezas faltantes para [100,000-1,000,000]?
          - [Choice]: Sí.
            - (removes=coins) (receives=missing Armour of Trials piece(s) y/o Vanquish (cuerpo a cuerpo))
            - (Condition: Aunque solo sea para recuperar Vanquish:)
              - [pic=Vencer detail.png]
            - (Condition: Si reclamas algo que no sea Vanquish:)
              - [pic=Helm of Trials detail.png]  <!-- image is independent of reclaimed piece -->
          - [Choice]: No.
            - (end)
    - (Condition: Si se pueden recuperar objetos tanto de combate como de no combate:)
      - [Menu]: Selecciona una opción
        - [Choice]: Recupera el atuendo de las pruebas.
          - (above|combat)
        - [Choice]: Reclama otros artículos.
          - (above|noncombat)
  - [Choice]: [Talk about rewards.]
    - [Menu]: Selecciona una opción
      - [Choice]: Háblame del Atuendo de Pruebas.
        - **May:** ¿No es glorioso? ¡Estoy realmente orgulloso de ello!
        - **Mayo:** Una vez conocí a una mujer llamada Xenia que me mostró un casco que inspiró el diseño de todo este conjunto.
        - **May:** No fue fácil, pero traté de encarnar lo que significa ser un aventurero con este conjunto. Está bien luchar, pero si te levantas y sigues adelante, ¡al final tendrás éxito!
        - **Mayo:** ¿Hay algo más en lo que pueda ayudarte?
        - (initial)
      - [Choice]: Cuéntame sobre tus mascotas.
        - **May:** Son maravillosos, ¿verdad? Los encontré cuando eran apenas cachorros, perdidos y solos. No tengo idea de dónde vinieron y desde ese día nunca he visto otro como ellos.
          - (Condition: Si el player no ha desbloqueado la mascota Lorehound:)
            - **May:** He entrenado a ambos para que sean útiles en una aventura, algo para lo que Didymus tenía un talento bastante natural.
            - **May:** Me entristecerá decirle adiós, pero a diferencia de Fenton, ¡él simplemente se muere por volver a la batalla con un héroe digno!
            - (continue)
        - (Condition: Si el player ha desbloqueado la mascota Lorehound:)
            - **Mayo:** Didymus parece estar pasando un buen rato aventurándose contigo, ¡espero que se porte tan bien como lo entrené!
            - (continue)
        - **Mayo:** ¿Hay algo más en lo que pueda ayudarte?
        - (initial)
      - [Choice]: Cuéntame sobre todo lo demás.
        - **Mayo:** Bueno, aquí hay muchas cosas que te ayudarán a medida que avanzas en tus aventuras. Hay una manera de unirte rápidamente a otros aventureros en su último esfuerzo y un título para mostrar tu destreza.
        - **Mayo:** Incluso guardaré algunas de las cosas variadas que seguramente recogerás mientras viajas por la tierra. ¡Tengo un cofre dedicado solo para eso!
        - **Mayo:** ¿Hay algo más en lo que pueda ayudarte?
        - (initial)
      - [Choice]: Adiós.
        - **Mayo:** ¡Mucha suerte en tus aventuras!
  - [Choice]: [Talk about something else.]
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué es todo esto?
        - **May:** Bueno, como puedes ver, no soy el más organizado, así que hay bastantes cosas de mis propias aventuras esparcidas por ahí.
        - **May:** Sin embargo, no todo es mío, también hay algunas partes que estoy siguiendo de cerca.
        - **May:** ¡Lo realmente importante es lo que tengo para ti! Estoy muy emocionado de mostrárselo todo.
        - **Mayo:** ¿Hay algo más en lo que pueda ayudarte?
        - (initial)
      - [Choice]: ¿Quién eres?
        - **May:** Mi nombre es May y solía ser una aventurera como tú.
        - **May:** ¡Siempre había soñado con hacerme un nombre y ser famoso en todo el mundo! ¡Durante un tiempo Dionisio incluso reconoció mis logros!
        - **May:** Me di cuenta de que ser la estrella del calzado es divertido, pero lo que realmente me importa es ayudar a la gente. Entonces, colgué mi capa y puse mis habilidades a trabajar para ayudar a otros aventureros.
        - **Mayo:** Me tomó un tiempo prepararme, pero ahora aquí estoy, ¡listo para ayudar a los aventureros en cualquier etapa de su viaje!
        - **Mayo:** ¿Hay algo más en lo que pueda ayudarte?
        - (initial)
      - [Choice]: Adiós.
        - **Mayo:** ¡Mucha suerte en tus aventuras!

### When attempting to use a locked feature

- **Mayo:** ¡Tendrás que desbloquearlo usando puntos de misión antes de poder usarlo!

### When reclaiming


#### Sin nada que reclamar

- **Mayo:** No tienes ningún artículo para reclamar en este momento.

#### Con artículos para reclamar


##### Sin suficiente espacio en backpack

- **Mayo:** No tienes suficiente espacio en el inventario para que te dé todo ahora mismo.

##### Con suficiente espacio en backpack

- **Mayo:** He colocado tus recompensas en tu inventario.

### When using the Armadyl's feather on her

- **Mayo:** Creo que esto puede ser útil o no en tus futuras aventuras.
- Has desbloqueado el título: {{Colour Player}}
