# Isaura

- **Original Wiki Page**: [Transcript:Isaura](https://runescape.wiki/w/Transcript%3AIsaura)
- **Letter**: `I`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Black Knights' Base

- **Isaura:** ¿Quién eres y qué haces aquí?
- (Condition: Before completing the Archaeology tutorial:)
  - **Player:** No estoy seguro de por qué estoy aquí, pero mi nombre es Player.
  - **Isaura:** Bueno, Player, si fueras arqueólogo, te estaría preguntando sobre colecciones.
  - (continue)
- (Condition: After completing the Archaeology tutorial:)
  - **Player:** ¡Mi nombre es Player y soy arqueólogo! Estoy aquí porque aparentemente estás interesado en coleccionar artefactos.
  - **Isaura:** Ah, sí. Eso es correcto. Excelente.
  - (continue)
- **Player:** ¿Por qué los Black Knights quieren coleccionar todas estas cosas viejas?
- **Isaura:** Eso no es de tu incumbencia. Estamos pagando por tus artefactos y para que no hagas preguntas.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Isaura:** Soy el director de solicitudes de Isaura Wabub. Puedes llamarme precisamente así.
    - **Player:** Ese es un nombre inusual. ¿Estás seguro de que eres un Black Knight y no un Caballero Blanco disfrazado?
    - **Isaura:** ¿Estás sugiriendo que el nombre que me dieron mis padres es un juego de palabras o una broma tonta?
    - **Player:** Espera, no, lo siento, eso no es lo que quise decir. Yo solo yo-
    - **Isaura:** ¡Jaja! Sólo estoy tirando de tu cadena. He oído todos los chistes, no te preocupes.
    - **Isaura:** Pero sí, por supuesto que soy un Black Knight... aunque difícilmente se lo revelaría a un arqueólogo al azar si fuera un espía, ¿verdad?
    - (initial)
  - [Choice]: ¿Qué estás coleccionando?
    - **Isaura:** Echa un vistazo a mis requisitos, a menos que seas de esos tipos que prefieren - urgh - hablar...
    - [Menu]: Selecciona una opción
      - [Choice]: Ver colecciones.
        - ((Cult-ural Appropriation interface opens.))
      - [Choice]: Habla de colecciones.
        - **Isaura:** Bueno, soy un Black Knight, ¡así que aceptaré cualquier cosa zamorakiana! La orden está muy interesada en todo lo que puedas descubrir en Infernal Source. Es parte de la historia y el patrimonio de nuestra organización.
        - **Player:** ¿Movario no está conectado con su organización? ¿Qué opinas de que él administre el sitio?
        - **Isaura:** Según tengo entendido, hemos trabajado con él en el pasado, pero es más un profesional independiente. También entiendo que él está principalmente en esto por sí mismo, por lo que confiaría más en ti que en él.
        - **Isaura:** El Kinshra puede hacer que valga la pena.
        - (initial)
  - [Choice]: ¿Cuáles son las recompensas de tu colección?
    - **Isaura:** Para empezar, te cambiaremos cronotas por cualquier cosa que nos traigas. Tienen valor para los arqueólogos por varias razones.
    - **Isaura:** Sin embargo, para cada una de mis colecciones, tengo algunos artículos específicos y únicos para intercambiar.
    - ((If the player hasn't obtained abyssal thread yet:))
      - **Isaura:** Hmm, ¿supongo que puedes quedarte con este hilo abismal al que no he encontrado uso?
      - **Player:** Oh, ¿qué es eso?
      - **Isaura:** Creo que son los trozos fibrosos de criaturas abisales entrelazados.
      - **Player:** Vaya, no gracias.
      - **Isaura:** ¡No te apresures! El dark mage de ZMI en el centro del Abismo dice que podrías usarlo en una bolsa de esencia gigante Runecrafting, y evitaría permanentemente que tus bolsas de esencia se degraden.
      - **Player:** En realidad, eso suena bien, ¡gracias!
      - (continue)
    - ((If the player has obtained abyssal thread:))
      - **Isaura:** ¿Ya usaste ese hilo abisal para proteger tus bolsas de esencia rúnica?
      - ((If the player hasn't yet made Threads of Fate:))
        - ((If the player still has the abyssal thread:))
          - **Player:** Todavía no.
          - (continue)
        - ((If the player has lost the abyssal thread:))
          - **Player:** Um, ¿tienes algún hilo más abisal? Perdí el mío antes de usarlo.
          - **Isaura:** Bien, ¡pero no te pierdas este!
          - [Menu]: ¿Tomar hilo abisal de Isaura?
            - [Choice]: Sí.
              - (receives=abyssal thread)
              - (continue)
            - [Choice]: No.
              - (end)
        - ((If the player has made Threads of Fate:))
          - **Player:** Sí, le di un buen uso, gracias.
          - (continue)
    - **Isaura:** Tengo un par de piezas de tetracompass que puedes tener para completar mis dos colecciones intermedias.
    - ((If the player hasn't obtained Ariadne's Diadem yet:))
      - **Isaura:** Tengo una reliquia: una prenda para la cabeza llamada Diadema de Ariadna. Te mejora en las habilidades de apoyo y te ayuda a entrenarlas un poco más rápido.
      - (initial)
    - ((If the player has obtained Ariadne's Diadem:))
      - **Isaura:** ¿Cómo es ese soporte para la cabeza? ¿Bien? Bien. No es necesario hablar más sobre eso.
      - (initial)
  - [Choice]: Adiós.
    - **Isaura:** ¡Descartado!
