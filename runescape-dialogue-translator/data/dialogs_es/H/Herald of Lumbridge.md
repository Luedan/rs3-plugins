# Herald of Lumbridge

- **Original Wiki Page**: [Transcript:Herald of Lumbridge](https://runescape.wiki/w/Transcript%3AHerald%20of%20Lumbridge)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Lumbridge


#### Antes de reclamar una capa de heraldo

- **Herald of Lumbridge:** ¡Hola, querida! ¿Cómo puedo hacer que tu día Lumbridge sea aún más maravilloso?
- **Player:** ¡Hola a ti también!<br>¿Qué haces aquí?
- **Herald of Lumbridge:** ¡Soy el heraldo de Lumbridge, querida! Mi trabajo es hacer de Lumbridge un lugar encantador para estar.
- **Herald of Lumbridge:** ¿Necesitas un desfile? ¡Yo lo arreglaré! ¿Necesitas una pancarta elegante? ¡Yo también puedo hacer eso! Necesitas una capa de heraldo...
- **Player:** ¿Capa Herald? ¿Qué es eso?
- **Herald of Lumbridge:** Vaya, es lo último y lo mejor en vestimenta de Lumbridge. ¡Te proporcionamos una hermosa capa Lumbridge para que la uses, gratis!
- **Herald of Lumbridge:** Y si has sido particularmente hábil en el área, ¡te mostraremos cómo personalizarlo para convertirlo en algo más fabuloso!
- **Herald of Lumbridge:** De hecho, he oído que otras ciudades, como Varrock y Falador, también ofrecen capas de heraldo con sus propios diseños especiales.
- **Herald of Lumbridge:** Naturalmente, nuestras capas Lumbridge son mucho más bonitas.
- **Herald of Lumbridge:** ¿Puedo interesarte en llevar una capa?
- [Menu]: ¿Aceptas esta capa de heraldo Lumbridge?
  - [Choice]: si
    - (receives=herald cape) <!-- worn ones will be swapped, not sure about poh -->
    - **Player:** ¡Claro, lo aceptaré!
    - **Herald of Lumbridge:** ¡Maravilloso! Echemos un vistazo a las personalizaciones que podemos hacer...
    - (continue|Customise)
  - [Choice]: No
    - **Player:** No, gracias.
    - **Herald of Lumbridge:** Oh, Dios mío. Bueno, vuelve a visitarnos si cambias de opinión, cariño.

#### Después de reclamar una capa de heraldo

- **Herald of Lumbridge:** ¡Hola, querida! ¿Cómo puedo hacer que tu día Lumbridge sea aún más maravilloso?
- [Menu]: Elige una opción:
  - [Choice]: ¡Hola de nuevo a ti! ¿Qué haces aquí?
    - **Herald of Lumbridge:** ¡Soy el heraldo de Lumbridge, querida! Mi trabajo es hacer de Lumbridge un lugar encantador para estar.
    - **Herald of Lumbridge:** ¿Necesitas un desfile? ¡Yo lo arreglaré! ¿Necesitas una pancarta elegante? ¡Yo también puedo hacer eso! Necesitas una capa de heraldo...
    - (Condition: Si se posee la capa de heraldo de otra ciudad:)
      - **Player:** Aunque ya tengo una capa de heraldo de otra ciudad.
      - **Herald of Lumbridge:** *tsk* Sí, me di cuenta, aunque no creo que te convenga. ¡La capa Lumbridge es MUCHO más bonita!
      - **Herald of Lumbridge:** Si quieres, puedo quitarte esa capa de heraldo de las manos y en su lugar darte una maravillosa capa de heraldo Lumbridge.
      - [Menu]: ¿Cambiar tu capa de heraldo a Lumbridge?
        - [Choice]: si
          - (continuea|accept)
        - [Choice]: No
          - **Player:** No gracias, me quedaré con la capa que tengo.
          - **Herald of Lumbridge:** ¿Esa tontería? Bueno, si es necesario. Vuelve a visitarnos si cambias de opinión, cariño.
    - (Condition: Si posee la capa de heraldo Lumbridge:)
      - **Player:** Oh, ya tengo uno de esos.
      - **Herald of Lumbridge:** ¡Sí, lo noté! Te queda muy elegante. ¿Quizás te gustaría personalizarlo un poco más?
      - [Menu]: ¿Personalizar tu capa de heraldo Lumbridge?
        - [Choice]: si
          - (continue|Customise)
        - [Choice]: No
          - (end)
  - [Choice]: Could you be a little less...noisy?|cond=Predeterminado, y después de decirle que está demasiado silencioso:
    - **Herald of Lumbridge:** Bueno, SOY un heraldo, querida. Proclamar con orgullo el valor cívico de Lumbridge es lo mío.
    - **Player:** ¿Quizás podrías hacer lo tuyo con un poco menos... de entusiasmo?
    - **Herald of Lumbridge:** En una escala de "uno" a "yo", ¿cuánto entusiasmo preferirías?
    - **Player:** La menor cantidad de "tú" posible, por favor.<br>Eso sería espléndido.
    - **Herald of Lumbridge:** Correcto. Dejaré mi cháchara hasta que digas lo contrario.
    - **Player:** Maravilloso.<br>Entonces, recuérdame ¿qué haces aquí?
    - (continuea|what-do-you-do)
  - [Choice]: It's quiet. Almost too quiet.|cond=Después de pedirle que hiciera menos ruido antes:
    - **Herald of Lumbridge:** Podría volver a gritar sobre Lumbridge, si quieres.
    - **Player:** Supongo que tus gritos sobre Lumbridge tienen que ser insoportablemente efervescentes.
    - **Herald of Lumbridge:** Esa es la única manera que sé.
    - **Player:** Continúa, entonces. Proclama tus dulces tonterías.
    - **Herald of Lumbridge:** ¡YIPPI!
    - **Player:** Ahora, supongo que quieres presentarte de nuevo, a pesar de nuestras conversaciones anteriores.
    - **Herald of Lumbridge:** Me conoces demasiado bien.
    - **Player:** Muy bien. Cuéntame qué haces aquí.
    - (continuea|what-do-you-do)

#### Personalizar

- **Herald of Lumbridge:** Parece que tienes algunas crestas adicionales para desbloquear, querida. ¡Qué emocionante!
- ((Lumbridge Herald Se abre la interfaz de personalización de Cape.))

#### Diálogo aéreo

- **Herald of Lumbridge:** {{RSChat|"Give me an L!"}}
- **Herald of Lumbridge:** {{RSChat|"Give me a U!"}}
- **Herald of Lumbridge:** {{RSChat|"Give me a Lumbridge herald cape!"}}
- **Herald of Lumbridge:** {{RSChat|"Lumbridge; the friendliest place to be"}}
- **Herald of Lumbridge:** {{RSChat|"Wear a Lumbridge herald cape with pride!"}}
- **Herald of Lumbridge:** {{RSChat|"It's Lumbridge!"}}
- **Herald of Lumbridge:** {{RSChat|"The eye of the fun hurricane"}}
- **Herald of Lumbridge:** {{RSChat|"Whoo! This is tiring work."}}
- **Herald of Lumbridge:** {{RSChat|"Have yourself a snazzy Lumbridge day!"}}

#### Diálogo histórico

- **Herald of Lumbridge:** ¡Hola, querida! ¿Cómo puedo hacer que tu día Lumbridge sea aún más maravilloso?
- [Menu]: Elige una opción:
  - [Choice]: ¡Hola de nuevo a ti! ¿Qué haces aquí?
    - (continuea|what-do-you-do)
  - [Choice]: Could you be a little less...noisy?|cond=Predeterminado, y después de decirle que está demasiado silencioso:
    - (above|noisy)
  - [Choice]: It's quiet. Almost too quiet.|cond=Después de pedirle que hiciera menos ruido antes:
    - (above|quiet)
  - [Choice]: ¡Parece que esta ciudad ha visto días mejores!
    - (Condition: Durante el Lumbridge Rebuildathon:)
      - **Herald of Lumbridge:** Fue la batalla de Lumbridge, donde Saradomin y Zamorak lucharon por la supremacía después de la muerte de Guthix. Aunque me entristece pensar en ello. ¡Mira mi ciudad que alguna vez fue hermosa! ¡Tiendas y casas arruinadas! ¡Pero estoy tratando de mejorar el estado de ánimo de todos!
      - **Player:** ¿Por qué? ¿Qué haces aquí?
      - (continuea|what-do-you-do)
    - (Condition: Durante la Batalla de Lumbridge:)
      - **Player:** ¿Maravilloso? ¡Estamos prácticamente en medio de una batalla!
      - **Herald of Lumbridge:** Lo sé, pero no es necesario que me lo recuerdes. ¡La batalla ha sido mala para todos! ¡Mira mi ciudad que alguna vez fue hermosa! ¡Es prácticamente un campo de guerra! ¡Pero estoy tratando de mejorar el estado de ánimo de todos!
      - **Player:** ¿Por qué? ¿Qué haces aquí?
      - (continuea|what-do-you-do)
