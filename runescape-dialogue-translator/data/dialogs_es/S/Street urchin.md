# Street urchin

- **Original Wiki Page**: [Transcript:Street urchin](https://runescape.wiki/w/Transcript%3AStreet%20urchin)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before The Feud

- **Player:** Hola, pequeño.
- **Street urchin:** No soy pequeño y si vuelves a decir eso te destriparé.
- **Player:** Tranquilo, no quise ofender.
- **Street urchin:** Te dejaré ir por esta vez. Bueno, ¿qué quieres? ¿Información?
- **Player:** Sí, cuéntame sobre...
- [Menu]: Selecciona una opción
  - [Choice]: Los menafitas
    - **Player:** Háblame de los menafitas.
    - **Street urchin:** Son un grupo malo, siempre inician peleas en Asp y Snake. Se dice en la calle que están dirigidos por algún sacerdote trastornado. Aunque nadie puede verlo mientras negocia a través de Rashid the Operator. Están planeando algo, pero son un grupo tan unido que nunca se les escapa nada.
    - **Street urchin:** Bueno, ¿entonces necesitas alguna otra información?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, cuéntame sobre...
        - **Player:** Sí, cuéntame sobre...
        - (initial|initial-options)
      - [Choice]: No gracias.
        - **Player:** No, gracias{{Sic}}
        - **Street urchin:** Vuelve si necesitas información sobre algo en la ciudad.
        - **Player:** Lo haré, gracias.
  - [Choice]: los bandidos
    - **Player:** Háblame de los bandidos.
    - **Street urchin:** Realmente no hay mucho que decir sobre ellos, son solo un grupo de matones locales liderados por el más grande de ellos. No albergan las ambiciones de los menafitas.
    - **Street urchin:** Bueno, ¿entonces necesitas alguna otra información?
    - (continuea|other-info)
  - [Choice]: el alcalde
    - **Player:** Háblame del alcalde.
    - **Street urchin:** El alcalde es un cobarde sin carácter. El estado actual del pueblo es todo culpa suya. No se enfrentó a los menafitas cuando llegaron por primera vez a la ciudad. Cuando finalmente se dio cuenta de su error, contrató a un grupo de matones para intentar deshacerse de ellos.
    - **Street urchin:** Cuando descubrieron que era débil, también se volvieron contra él. Provocando así un desastre aún mayor.
    - **Street urchin:** Bueno, ¿entonces necesitas alguna otra información?
    - (continuea|other-info)
  - [Choice]: la ciudad
    - **Player:** Cuéntame sobre la ciudad.
    - **Street urchin:** No hay mucho que decir al respecto. Pollivneach es una pequeña ciudad situada entre Al Kharid y Menaphos y tiene un problema de delincuencia especialmente grave. Además de eso, aquí no pasa mucho.
    - **Street urchin:** Bueno, ¿entonces necesitas alguna otra información?
    - (continuea|other-info)

### After partial completion of The Feud


#### Diálogo por primera vez

- **Player:** ¡Hola!
- **Street urchin:** ¿Viste la forma en que distraí a ese tipo? ¡Hombre, soy un operador suave!
- **Player:** Estuviste bien, ¿verdad?
- **Street urchin:** Entonces, ¿dónde está mi dinero?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué dinero?
    - **Player:** ¿Qué dinero?
    - **Street urchin:** No te hagas el estúpido conmigo, soy mejor en eso. ¿Dónde está mi dinero?
    - **Player:** ¡Oh, ese dinero! ¡No creo que te lo merezcas!
    - **Street urchin:** ¡Mentiroso, ladrón!
    - **Player:** ¡Qué observador de tu parte!
    - **Street urchin:** ¡Dame mi dinero!
    - **Player:** ¡Hazme!
    - **Street urchin:** ¡Te arrepentirás!
  - [Choice]: Aquí tienes, gracias.
    - **Player:** Aquí tienes, gracias.
    - (Condition: Sin al menos 10 coins:)
      - color=#EB2F2F
      - (Condition: Repetido en una ventana emergente:)
        - (Ventana emergente: No puedes permitirte eso.|advertencia=yes)
        - (continue)
      - **Street urchin:**¿Aquí voy, qué? ¡No tienes dinero!
      - **Player:** ¿Qué dinero?
      - (continuea|what-money)
    - (Condition: Con al menos 10 coins:)
      - (removes=10 coins)
      - **Street urchin:** Gracias [sir/ma'am], no pensé que cumplirías tu parte del trato. No hay mucho honor entre los ladrones, ¿sabes?
      - **Street urchin:** Bueno, ¿entonces necesitas alguna otra información?
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, cuéntame sobre....
          - **Player:** Sí, cuéntame sobre...
          - [Menu]: Selecciona una opción
            - [Choice]: Los menafitas
              - **Player:** Háblame de los menafitas.
              - **Street urchin:** Son un grupo malo, siempre inician peleas en Asp y Snake. Se dice en la calle que están dirigidos por algún sacerdote trastornado. Aunque nadie puede verlo mientras negocia a través de Rashid the Operator. Están planeando algo, pero son un grupo tan unido que nunca se les escapa nada.
            - [Choice]: los bandidos
              - **Player:** Háblame de los bandidos.
              - **Street urchin:** Realmente no hay mucho que decir sobre ellos, son solo un grupo de matones locales liderados por el más grande de ellos. No albergan las ambiciones de los menafitas.
            - [Choice]: el alcalde
              - **Player:** Háblame del alcalde.
              - **Street urchin:** El alcalde es un cobarde sin carácter. El estado actual del pueblo es todo culpa suya. No se enfrentó a los menafitas cuando llegaron por primera vez a la ciudad. Cuando finalmente se dio cuenta de su error, contrató a un grupo de matones para intentar deshacerse de ellos.
              - **Street urchin:** Cuando descubrieron que era débil, también se volvieron contra él. Provocando así un desastre aún mayor.
            - [Choice]: sobrino de Ali Morrisane
              - **Player:** Háblame del sobrino de Ali Morrisane.
              - **Street urchin:** Estaba bien, aunque solía patearnos cuando nos pillaba robando en su puesto.
              - **Player:** ¿Sabes dónde está ahora?
              - **Street urchin:** Desapareció hace aproximadamente una semana, estuvo involucrado en algún negocio dudoso con ambas pandillas. Creo que los estafó. No sé si se salió con la suya o si lo atraparon, pero creo que si te ganaste la confianza de alguna de las pandillas, es posible que te den más información.
            - [Choice]: la ciudad
              - **Player:** Cuéntame sobre la ciudad.
              - **Street urchin:** Realmente no hay mucho que decir al respecto. Pollnivneach es una pequeña ciudad ubicada entre Al Kharid y Menaphos y tiene un problema de delincuencia particularmente grave. Además de eso, aquí no pasa mucho.
            - (continuea|info)
        - [Choice]: No gracias.
          - **Player:** No, gracias{{Sic}}
          - **Street urchin:** Vuelve si necesitas información sobre algo en la ciudad.
          - **Player:** Lo haré, gracias.

#### Después de negarse a pagar el street urchin

- **Player:** ¡Hola!
- **Street urchin:** ¡Ladrón! ¡Ladrón!
- **Player:** ¡Cállate! No provoques más problemas o te arrepentirás.
- **Street urchin:** ¡Dame el doble y me callaré!
- (Condition: Si el player no tiene al menos 20 coins:)
  - color=#EB2F2F
  - (Condition: Repetido en una ventana emergente:)
    - (Ventana emergente: No puedes permitirte eso.|advertencia=yes)
    - (continue)
  - **Player:** Lo siento, no tengo suficiente dinero encima, te lo daré la próxima vez que nos veamos.
  - **Street urchin:** Ya había oído eso antes. Si no me das el dinero, lo lamentarás.
- (Condition: Si el player tiene al menos 20 coins:)
  - **Player:** Ok, aquí tienes, ladrón.
  - (removes=20 coins)
  - **Street urchin:** ¡Qué observador de tu parte!

#### Después de pagar el street urchin

- **Player:** ¡Hola!
- **Street urchin:** ¡Hola! ¿Quieres ir a robar a más personas? Me vendría bien algo más de dinero.
- **Player:** Ok, hagámoslo de nuevo.
- (Condition: Si no hay aldeanos cerca:)
  - **Street urchin:** No parece haber nadie cerca a quien robar en este momento. Quizás podamos volver a intentarlo más tarde.
- (Condition: Si hay un aldeano cerca:)
  - **Street urchin:** {{RSChat|Hey you, camel features! Come here.}}
  - **Villager:** {{RSChat|I know your game guttersnipe.}}
  - **Street urchin:** {{RSChat|???}}
  - **Villager:** {{RSChat|You wont{{Sic}} vuelve a engañar a cualquiera con ese truco.}}
  - **Player:** ¡No creo que ese truco vuelva a funcionar aquí! Es un pueblo pequeño y la gente habla.
  - **Street urchin:** Bueno, ¿entonces necesitas alguna información?
  - **Player:** No, gracias. Creo que tengo una idea bastante clara de lo que está pasando en la ciudad ahora.

#### Después de ayudar nuevamente al street urchin

- **Player:** ¡Hola!
- **Street urchin:** ¡Hola! ¿Quieres ir a robar a más personas? Me vendría bien algo más de dinero.
- **Player:** ¡No creo que ese truco vuelva a funcionar aquí! Es un pueblo pequeño y la gente habla.
- **Street urchin:** Bueno, ¿entonces necesitas alguna información?
- **Player:** No, gracias. Creo que tengo una idea bastante clara de lo que está pasando en la ciudad ahora.
