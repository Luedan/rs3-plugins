# Dororan

- **Original Wiki Page**: [Transcript:Dororan](https://runescape.wiki/w/Transcript%3ADororan)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Gunnar's Ground, at the Gunnarsgrunn gate

- (ver | Tierra de Gunnar)

### After Gunnar's Ground, at the Leptoc manor


#### Antes de grabar la pulsera de rubíes

- **Dororan:** ¡Pasa, amigo mío, pasa! Hay otro asunto en el que me vendría bien tu ayuda.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué es?
    - **Dororan:** Tengo más joyas para Gudrun y necesito tu ayuda para grabarlas.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Cuál es la primera pieza?
        - **Dororan:** Una magnífica pulsera de rubíes.
        - {{anchor|with-beauty-blessed}}**Dororan:** 'Con belleza bendita.'
        - [Menu]: Selecciona una opción
          - [Choice]: Graba la pulsera.
            - (Condition: Without at least level 42 Crafting:)
              - [Necesitas un nivel Crafting de al menos 42 para grabar la pulsera de rubíes.]
              - **Dororan:** Es una pena. Quizás puedas volver a intentarlo en otro momento.
            - (Condition: With at least level 42 Crafting:)
              - Obtuviste 2000 Crafting XP.
              - [Graba cuidadosamente "Con belleza bendecida" en el brazalete de rubíes.]
              - **Dororan: ** ¡Magnífico! ¡Pendiente! Le daré esto inmediatamente. Por favor, vuelve cuando tengas tiempo.
          - [Choice]: No grabes la pulsera.
            - **Dororan:** Es una pena. Quizás puedas volver a intentarlo en otro momento.
      - [Choice]: Quiero hablar de otra cosa.
        - (below|something-else)
      - [Choice]: No tengo tiempo ahora.
        - (end)
  - [Choice]: Quiero hablar de otra cosa.{{anchor|something-else}}
    - **Dororan:** ¿Qué puedo hacer por ti?
    - [Menu]: Elige una opción:
      - [Choice]: ¿Cómo están las cosas?
        - **Dororan:** ¡Cada mañana me despierto con el sol y el canto de los pájaros! ¡La vida es maravillosa!
        - [Menu]: Selecciona una opción
          - [Choice]: Quiero hablar de otra cosa.
            - (above|something-else)
          - [Choice]: Adiós.
            - **Dororan:** ¡Adiós!
      - [Choice]: Esta es una casa muy grande.
        - **Dororan:** ¡Lo sé! No sé de dónde habría sacado Gunthor algo así. Quizás Gudrun tenga alguna idea.
        - (continuea|something-else-sub-options)
      - [Choice]: Me gustaría ver el poema que escribiste para Gunthor.
        - (Condition: Without space in backpack:)
          - [No tienes espacio para el poema.]
        - (Condition: With space in backpack:)
          - [Dororan te regala una copia del poema.]
          - (receives=Gunnar's Ground)
          - **Dororan:** ¡Ahí lo tienes!
      - [Choice]: cond=Having lost the swanky boots:|Parece que he extraviado mis elegantes botas.
        - **Player:** Parece que perdí mis elegantes botas.
        - (Condition: If free pairs of swanky boots can still be claimed:)
          - **Dororan:** ¡No te preocupes! Quedan algunos. Aquí tienes.
          - (Condition: Without space in backpack:)
            - [No tienes espacio para las botas.]
          - (Condition: With space in backpack:)
            - [Dororan te regala algunas botas más.]
            - (receives=swanky boots)
            - **Dororan:** ¡Ten más cuidado con estos! No tengo un suministro infinito.
        - (Condition: If all 12 free pairs of swanky boots have been claimed:)
          - **Dororan:** ¡Has agotado mi suministro de botas!
          - **Dororan:** Podría conseguirte otro par, pero tendría que cambiarlos por ellos.
          - **Dororan:** He estado pensando en regalarle a Gudrun un anillo de rubí. Si me traes una, te la cambio por unas botas más.
          - [Menu]: Elige una opción:
            - [Choice]: cond=Without a ruby ring in backpack:|No tengo uno conmigo.
              - (end)
            - [Choice]: cond=With a ruby ring in backpack:|Aquí tienes un anillo de rubí.
              - [Le cambias a Dororan un anillo de rubí por las botas.]
              - (removes=ruby ring) (receives=swanky boots)
            - [Choice]: No gracias.
              - (end)
      - [Choice]: Adiós.
        - **Dororan:** ¡Adiós!
  - [Choice]: No tengo tiempo ahora.
    - (end)

##### Después de negarse a grabar el brazalete de rubíes

- **Dororan:** ¿Quieres intentar grabar la pulsera de rubíes nuevamente?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué quieres grabar en él?
    - (above|with-beauty-blessed)
  - [Choice]: Quiero hablar de otra cosa.
    - (above|something-else)
  - [Choice]: No tengo tiempo ahora.
    - (end)

#### Después de grabar la pulsera de rubíes.

- **Dororan:** Tengo otra joya que grabar.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué es éste?
    - **Dororan:** Un fino collar de piedra de dragón.
    - **Dororan:** No hay mucho espacio... ¿qué tal simplemente 'Gudrun'?
    - [Menu]: Selecciona una opción
      - [Choice]: Graba el collar.
        - (Condition: Without at least level 72 Crafting:)
          - [Necesitas un nivel Crafting de al menos 72 para grabar el collar de piedra dragón.]
          - **Dororan:** Es una pena. Quizás puedas volver a intentarlo en otro momento.
        - (Condition: With at least level 72 Crafting:)
          - Obtuviste 10,000 Crafting XP.
          - [Grabas hábilmente 'Gudrun' en el collar de piedra de dragón.]
          - **Dororan:** ¡Otro trabajo asombroso! Por favor, vuelve más tarde para ver si tengo otras tareas de elaboración.
      - [Choice]: No grabes el collar.
        - **Dororan:** Es una pena. Quizás puedas volver a intentarlo en otro momento.
  - [Choice]: Quiero hablar de otra cosa.
    - (above|something-else)
  - [Choice]: No tengo tiempo ahora.
    - (end)

##### Después de negarse a grabar el collar de piedra de dragón.

- **Dororan:** ¿Quieres intentar grabar el collar de piedra de dragón nuevamente?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué quieres grabar en él?
    - (above|just-gudrun)
  - [Choice]: Quiero hablar de otra cosa.
    - (above|something-else)
  - [Choice]: No tengo tiempo ahora.
    - (end)

#### Después de grabar el collar de piedra de dragón.

- **Dororan:** Tengo una última joya que grabar.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué es?
    - **Dororan:** ¡Un amuleto de ónix!
    - {{anchor|most-beautiful}}**Dororan:** 'La chica más hermosa de la habitación'.
    - [Menu]: Selecciona una opción
      - [Choice]: Graba el amuleto.
        - (Condition: Without at least level 90 Crafting:)
          - [Necesitas un nivel Crafting de al menos 90 para grabar el amuleto de ónix.]
          - **Dororan:** Es una pena. Quizás puedas volver a intentarlo en otro momento.
        - (Condition: With at least level 90 Crafting:)
          - ¡Felicitaciones! Has completado: 'Gunning for Jewellery' - Graba todas las joyas de Dororan.
          - Obtuviste 20 000 Crafting XP.
          - [Graba con destreza "La chica más bella de la habitación" en el amuleto de ónix.]
          - **Dororan:** ¡Eso es fantástico! Excelente trabajo.
      - [Choice]: No grabes el amuleto.
        - **Dororan:** Es una pena. Quizás puedas volver a intentarlo en otro momento.
  - [Choice]: Quiero hablar de otra cosa.
    - (above|something-else)
  - [Choice]: No tengo tiempo ahora.
    - (end)

##### Después de negarse a grabar el amuleto de ónix

- **Dororan:** ¿Quieres intentar grabar el amuleto de ónix nuevamente?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué quieres grabar en él?
    - (above|most-beautiful)
  - [Choice]: Quiero hablar de otra cosa.
    - (above|something-else)
  - [Choice]: No tengo tiempo ahora.
    - (end)

#### Después de grabar el amuleto de ónix.

- **Dororan:** ¡Muchas gracias por todo lo que has hecho por nosotros!
- (continuea|something-else)
