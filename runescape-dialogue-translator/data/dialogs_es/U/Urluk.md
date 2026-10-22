# Urluk

- **Original Wiki Page**: [Transcript:Urluk](https://runescape.wiki/w/Transcript%3AUrluk)
- **Letter**: `U`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Antes de la jota de espadas

- **Urluk:** Oye, Hassan y los líderes te estaban buscando. Será mejor que hables con ellos primero.
- Completa la misión Jack of Spades para obtener acceso a Urluk.

#### Después de la jota de espadas

- (Condition: Only on first time:)
  - **Urluk:** Intento brindar ayuda e indicaciones a la gente por aquí.
  - **Urluk:** Aunque la gente simplemente se burla de mí.
  - **Player:** ¿De qué estás hablando? ¿Por qué me burlaría de ti?
  - **Urluk:** Bueno, si te dijera que te burlarías de mí...
  - **Urluk:** Todo el mundo siempre se burla de mí a mis espaldas, pero los camellos tienen un oído brillante, ¿sabes?
  - **Player:** Creo que estoy empezando a ver el problema aquí, continuaré.
  - **Urluk:** ¡No, espera! Se burlan de mí porque no me he movido en cincuenta años humanos. Sólo me gusta sentarme aquí y fumar cincho.
  - **Player:** ¿Cómo te has mantenido en comida y agua? Ni siquiera estoy enojado, estoy impresionado.
  - **Urluk:** No voy a mentir; Lo guardo en mis jorobas. No he necesitado comer durante décadas. Pareces agradable. ¿Necesitas algún consejo sobre qué hacer por aquí?
  - (continue|initial-options)
- [Menu]: Elige una opción: {{anchor|initial-options}}
  - [Choice]: ¿Qué puedo hacer aquí?
    - (Condition: Responses cycle through the following:)
      - (Condition: Woodcutting:)
        - **Urluk:** Deberías intentar cortar árboles de Acadia. Los encontrarás en la meseta elevada del Distrito Imperial, ¡pregúntale a un guardia si te pierdes!
        - **Urluk:** Esta es una excelente manera de hacer crecer tu reputación con la facción que elijas.
        - (initial|initial-options)
      - (Condition: Thieving:)
        - **Urluk:** Deberías probar algo de Thieving en el mercado junto a nosotros.
        - **Urluk:** Es posible que ganes reputación por hacerlo.
        - (initial|initial-options)
      - (Condition: Fishing:)
        - **Urluk:** Deberías intentar pescar algunos Beltfish en el distrito portuario.
        - **Urluk:** Esta es una excelente manera de hacer crecer tu reputación con la facción que elijas.
        - (initial|initial-options)
      - (Condition: Hunter:)
        - **Urluk:** Deberías ir a cazar algunos chorlitos al otro lado del río en Sophanem.
        - **Urluk:** Esta es una excelente manera de hacer crecer tu reputación con la facción que elijas.
        - (initial|initial-options)
      - (Condition: Shifting Tombs:)
        - **Urluk:** Deberías hacer algunas Tumbas Móviles en cualquiera de los cuatro distritos. Busque la aguja.
        - **Urluk:** Esta es una excelente manera de hacer crecer tu reputación con la facción que elijas.
        - (initial|initial-options)
      - (Condition: City Quests:)
        - (Condition: If a City Quest is active:)
          - **Urluk:** Alguien en la ciudad estaba buscando ayuda. No recuerdo el nombre... ¿[NPC] tal vez?
          - (initial|initial-options)
        - (Condition: If a City Quest isn't active:)
          - **Urluk:** Deberías realizar una de las misiones de la ciudad. Pruebe con un ciudadano que necesita hablar.
          - (initial|initial-options)
      - (Condition: Slayer:)
        - **Urluk:** Deberías ir a hacer algo de Slayer en la mazmorra Sophanem Slayer. Asegúrate de recoger algunas plumas de Ma'at del general store.
        - **Urluk:** Esta es una excelente manera de hacer crecer tu reputación con la facción que elijas.
        - (initial|initial-options)
      - (Condition: Divination:)
        - **Urluk:** Deberías hacer algo de Divination en Sophanem, busca los Luminous Wisps cerca del río.
        - (initial|initial-options)
      - (Condition: Crafting:)
        - **Urluk:** Deberías intentar entrenar a tu Crafting en la rueca en el distrito portuario.
        - (initial|initial-options)
      - (Condition: Smithing:)
        - **Urluk:** Deberías intentar entrenar a tu Smithing en el horno y el yunque en los distritos de trabajadores o portuarios.
        - (initial|initial-options)
      - (Condition: Cooking and Firemaking:)
        - **Urluk:** Deberías intentar entrenar tu Cooking o Firemaking en la fogata del Distrito de los Trabajadores.
        - (initial|initial-options)
  - [Choice]: ¿A qué debo aspirar?
    - (Condition: Responses cycle through the following:)
      - (Condition: Quest:)
        - (Condition: If the player is between 1 and 2 city reputation:)
          - **Urluk:** Podrías hacer una misión. Sin embargo, no eres lo suficientemente conocido en estos lugares como para ser elegible para uno.
          - Se requiere reputación de nivel 3 para 'Crocodile Tears'.
          - (initial|initial-options)
      - (Condition: No quest:)
        - **Urluk:** No se me ocurre nada más ahora, ¡háblame en un segundo!
        - Se requiere reputación de nivel 3 para 'Crocodile Tears'.
        - (initial|initial-options)
      - (Condition: If the player is below level 72 Hunter:)
        - **Urluk:** Deberías ir a entrenar tu Hunter para atrapar pájaros chorlitos.
        - Se requiere nivel 72 Hunter para capturar pájaros chorlitos.
        - (initial|initial-options)
      - (Condition: If the player is below level 50 Crafting:)
        - **Urluk:** Deberías entrenar a tu Crafting para que haga Shifting Tombs.
        - Se requiere nivel 50 Crafting para hacer Tumbas Móviles.
        - (initial|initial-options)
      - (Condition: If the player has not completed Spirits of the Elid quest:)
        - **Urluk:** Podrías hacer una misión. Los ciudadanos de Nardah están sufriendo una sequía. Eso podría ser algo que arreglar de antemano.
        - Es necesario completar Spirits of the Elid para Crocodile Tears.
        - (initial|initial-options)
      - (Condition: If the player is missing any of the below requirements:)
        - (Condition: If the player is below level 88 Slayer:)
          - **Urluk:** Necesitas mejorar tu habilidad para matar para ingresar a la mazmorra Sophanem Slayer.
          - Se requiere 88 Slayer para la mazmorra Sophanem Slayer.
        - (Condition: If the player is below level 90 Divination:)
          - **Urluk:** Deberías mejorar tu habilidad de adivinación para utilizar la colonia en Sophanem.
          - Se requieren 90 Divination para cosechar la colonia de mechones luminosos Sophanem.
        - (continue|more-things)
      - (Condition: If Urluk has been asked about all the things that can be aimed for:)
        - **Urluk:{{anchor|more-things}}** Hmm, bueno, aquí hay algunas cosas más a las que podrías aspirar... pero dejaré que las descubras tú mismo.
        - (initial|initial-options)
      - (Condition: Earned Sandy title:)
        - **Urluk:** ¡Oh! Has hecho MUCHAS cosas en Menaphos. ¡Esto merece una recompensa mayor que una simple capa de palapa!
        - ¡Has desbloqueado el título '{{Coloury}}'!|color=#AAC371}}
        - ((Repeated in a pop-up:))
          - ¡Has desbloqueado el título '{{Coloury}}'!|color=#AAC371|shadow=no}}
          - (initial|initial-options)
      - (Condition: After obtaining Sandy title:)
        - **Urluk:** ¿Sabes qué? Creo que estáis todos bien.
        - (initial|initial-options)
  - [Choice]: ¿Puedo conseguir tu capa?
    - (Condition: If not eligible for the cape:)
      - **Urluk:** El Cabo de la Palapa es sólo para aquellos que han visto mundo.
      - **Urluk:** Haz una tumba móvil y prueba Woodcutting, Thieving, Mining, Fishing y Hunter en Menaphos y Sophanem para recibir la capa {{Sic}}.
    - (Condition: If eligible for the cape:)
      - (Condition: If the cape has not been claimed yet:)
        - ¡Felicitaciones! Has completado: 'Jack of all Menaphos' - Haz un poco de todo en Menaphos y reclama la capa de la palapa de Urluk.
        - ¡Has desbloqueado la capa de la palapa!
        - (continue)
      - **Urluk:** Hecho de hilos de tela trenzados. Nunca más te sentirás expuesto.
    - (initial|initial-options)
  - [Choice]: ¿Tienes algún rumor sobre City Quests?
    - (Condition: If a City Quest is active:)
      - **Urluk:** Alguien en la ciudad estaba buscando ayuda. No recuerdo el nombre.... ¿[NPC] tal vez?
    - (Condition: If a City Quest isn't active:)
      - **Urluk:** Deberías hacer una de las misiones de la ciudad. De vez en cuando un ciudadano necesitará ayuda, lo garantizo.
      - (initial|initial-options)
  - [Choice]: ¿Cómo puedo entenderte?
    - **Urluk:** Durante mis viajes, encontré un amuleto de habla humana. Debo decir que ha sido muy útil para evitar que me ataquen.
    - (initial|initial-options)
