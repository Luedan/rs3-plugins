# Jellyfish Mender Judd

- **Original Wiki Page**: [Transcript:Jellyfish Mender Judd](https://runescape.wiki/w/Transcript%3AJellyfish%20Mender%20Judd)
- **Letter**: `J`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Deep Sea Fishing hub


#### Opción de hablar con

- **Jellyfish Mender Judd:** ¡Hola!
- [Menu]: Selecciona una opción
  - [Choice]: ¿Cuál es tu historia?
    - **Player:** Entonces, ¿cuál es tu historia? ¿Qué haces aquí?
    - **Jellyfish Mender Judd:** ¡Me encanta estar aquí! Vine aquí para ganar dinero y pescar peces grandes, pero me quedé por la paz y la calma que me trae el océano y la camaradería entre la gente de aquí.
    - **Jellyfish Mender Judd:** Este espíritu colaborativo me inspiró a empezar a combinar partes de medusas para los demás pescadores. ¡Quiero hacer mi parte para convertir este lugar en una utopía de pesca!
    - **Player:** ¿Nunca te mareas en estas plataformas?
    - **Jellyfish Mender Judd:** ¡Nunca! Para mí, siento como si el océano me acunara dulcemente, noche y día.
    - **Player:** No estoy seguro de que mi estómago esté de acuerdo...
    - (initial|judd-options)
  - [Choice]: ¿Puedes combinar algunas medusas para mí? {{anchor|combine}}
    - (Condition: If the player has jellyfish that can be combined:)
      - **Jellyfish Mender Judd:** Ahí lo tienes.
    - (Condition: If the player has jellyfish that can't be combined:)
      - **Jellyfish Mender Judd:** Lo siento, no sé cómo combinar nada de lo que llevas.
    - (Condition: If the player does not have any jellyfish:)
      - **Jellyfish Mender Judd:** ¡No tienes medusas para combinar!

#### Combinar opción Medusa

- (above|combine)

#### Diálogo aéreo

- {{Trandom}}
  - **Jellyfish Mender Judd:** {{RSChat|I love to help my fellow fisherfolk.}}
  - **Jellyfish Mender Judd:** {{RSChat|Let's create a fishing utopia!}}
  - **Jellyfish Mender Judd:** {{RSChat|I'll mend your broken jellyfish.}}
  - **Jellyfish Mender Judd:** {{RSChat|Bring out your jellyfish pieces!}}
