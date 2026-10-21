# Flo (The Beach)

- **Original Wiki Page**: [Transcript:Flo (The Beach)](https://runescape.wiki/w/Transcript%3AFlo%20%28The%20Beach%29)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Flo:** ¿Listo para regresar?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, estoy listo para partir.
    - (Action: el player se traslada al Grand Exchange, frente al portal de Sunlight Sands Beach.)
  - [Choice]: No, me quedaré un poco más.
    - **Flo:** No me puedo quejar. {{Sic|Sunshine and fish what more could a man want?}}
    - **Flo:** Aunque, dicho esto, no me importaría tener en mis manos a esa bestia en la piscina. Haría una comida digna de un reino.
    - **Flo:** ¡Quizás necesite una caña más grande!
    - [Menu]: Selecciona una opción
      - [Choice]: cond=Only if not asked last:|¿Qué está pasando aquí?
        - **Flo:** Aquí se puede pescar muy bien. Las truchas tropicales son juguetonas, pero ideales para preparar un sabroso manjar de verano.
        - [Usar los lugares de pesca te brinda experiencia de pesca. Puedes adquirir experiencia adicional entregando el pescado a Wellington o entregándolo en la zona de barbacoa.]
        - (previous)
      - [Choice]: cond=Only if not asked last:|¿Por qué hay barcos piratas?
        - **Flo:** ¡Esos barcos son luchadores! Están buscando algo con qué luchar.
        - **Flo:** Si tienes acorazados, puedes enfrentarlos contra uno de los barcos piratas, pero ¡cuidado, {{Colour|#FF0000|los piratas nunca pierden}}!
        - (previous)
      - [Choice]: cond=Only after asking something else:|¿Cómo van las cosas?
        - (above|I can't complain)

### Head Home

- (Action: el player se traslada al Grand Exchange, frente al portal de Sunlight Sands Beach.)

### Trying to open the store with the relevant Sandy Clue Scroll (historical)

- ¡Oh, un extraño te dejó esto!
- (Condition: Recibir un cuadro de desplazamiento:)
  - (removes=Sandy Clue Scroll) (receives=Sandy Scroll box)
  - [scrollbox].}}
- (Condition: Recibir ataúdes:)
  - (Condition: Sin espacio libre en backpack:)
    - Necesitas 1 espacio libre en tu backpack para recibir tus cofres de pistas.
  - (Condition: Con espacio libre en backpack:)
    - (removes=Sandy Clue Scroll) (receives=Sandy Casket and its red version)
    - [¡Te entregan un ataúd!]
