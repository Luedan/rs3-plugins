# Wizard Myrtle

- **Original Wiki Page**: [Transcript:Wizard Myrtle](https://runescape.wiki/w/Transcript%3AWizard%20Myrtle)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At the Wizards' Tower


#### Hablando con ella


##### Antes de debajo de las mareas malditas

- **Wizard Myrtle:** Bien recibido, viajero.
- **Player:** Hola, ¿qué estás haciendo?
- **Wizard Myrtle:** ¿Oh, esto? Me especializo en un tipo de magia basada en la manipulación del agua, solo estoy practicando mi técnica.
- **Wizard Myrtle:** ¡Mi nombre es Myrtle, soy hidromante!
- **Player:** Encantado de conocerte. ¿Eres miembro de Wizards' Tower?
- (Condition: Without the quest requirements:)
  - **Wizard Myrtle:** Se podría decir que estoy afiliado. Vine aquí en busca de ayuda, pero me temo que necesito a alguien con un poco más de experiencia.
  - **Player:** ¡Volveré cuando haya entrenado un poco más!
- (Condition: With the quest requirements:)
  - (ver|Debajo de las mareas malditas#Comenzando)

##### Después de debajo de las mareas malditas

- **Wizard Myrtle:** ¡Player! Qué bueno verte de nuevo, ¿te gustaría volver a la isla hundida?
- [Menu]: Elige una opción:
  - [Choice]: Me gustaría cambiar mi bajo el agua.
    - [Menu]: ¿Qué método de respiración bajo el agua te gustaría utilizar?
      - [Choice]: Hechizo de respiración bajo el agua.
        - **Wizard Myrtle:** Genial, te lanzaré mi hechizo para que puedas respirar sin ningún aparato de buceo.
      - [Choice]: Traje de buceo para acuario.
        - **Wizard Myrtle:** ¡Genial, puedes usar el traje de buceo desde tu casa!
      - [Choice]: Casco de pecera y aparato de buceo.
        - (Condition: If both fishbowl helmet and diving apparatus are equipped or in backpack:)
          - **Wizard Myrtle:** ¡Genial, el casco de pecera y el aparato de buceo deberían funcionar perfectamente!
        - (Condition: Without both fishbowl helmet and diving apparatus equipped or in backpack:)
          - **Wizard Myrtle:** Si quieres utilizar el casco de pecera y el aparato de buceo, primero tendrás que ir a buscarlos.
  - [Choice]: Me gustaría bucear en la isla hundida.
    - (below|Dive option)
  - [Choice]: Necesito depositar algunos artículos.
    - (below|Deposit option)
  - [Choice]: cond=With unclaimed rewards|¿Podría conseguir alguna recompensa que me tengas?
    - (Condition: Without enough space in backpack)
      - **Wizard Myrtle:** Parece que no tienes suficiente espacio para llevarte todas las recompensas que tengo para ti. Los guardaré hasta que lo hagas.
    - (Condition: With enough space in backpack)
      - (receives=unclaimed quest rewards)
      - **Wizard Myrtle:** Eso es todo lo que tengo para ti. ¡Gracias de nuevo por tu ayuda!
  - [Choice]: No gracias.
    - **Wizard Myrtle:** Ok, avísame si es así.

#### Opción de depósito

- **Wizard Myrtle:** Puedo depositar algunos artículos para ti si quieres.
- (opens=Bank deposit box)

#### Opción de buceo

- (Condition: If the player has weapons equipped, or with both weapons equipped and a follower out:)
  - **Wizard Myrtle:** Debes desequipar tus armas antes de irte, el agua podría dañarlas.
- (Condition: If the player has a follower out:)
  - **Wizard Myrtle:** Debes descartar a tu seguidor antes de irte, no podemos estar seguros de que esté a salvo.
- (Condition: Otherwise:)
  - (Action: La pantalla aparece y desaparece. el player ahora está bajo el agua frente a la ostra gigante.)

#### Diálogo aéreo

(Uno de los siguientes se reproduce aleatoriamente junto con la animación de lanzamiento de hechizos inactivo de Myrtle:)
- **Wizard Myrtle:** {{RSChat|Be patient, like water. Water always finds its way.}}
- **Wizard Myrtle:** {{RSChat|Present water with an obstacle - a force - and it will find a way around.}}
- **Wizard Myrtle:** {{RSChat|Water seeks to be guided. It does not resist, it flows.}}
- **Wizard Myrtle:** {{RSChat|We are all made of water. All you must do, is let it flow through you.}}
