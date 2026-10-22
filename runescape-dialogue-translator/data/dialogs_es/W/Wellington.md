# Wellington

- **Original Wiki Page**: [Transcript:Wellington](https://runescape.wiki/w/Transcript%3AWellington)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Hand in fish with raw tropical trout

- (removes=raw tropical trout)
- Le entregas el pescado [número] a Wellington.
- (pop-up)
  - (Pop-up: You hand [number] fish to Wellington.)

### Hand in fish without raw tropical trout or talk to

- [Menu]: Selecciona una opción
  - [Choice]: cond=Only if not asked last:|¿Qué está pasando aquí?
    - **Wellington:** Aquí se puede pescar muy bien. Las truchas tropicales son juguetonas, pero ideales para preparar un sabroso manjar de verano.
    - [Usar los lugares de pesca te brinda experiencia de pesca. Puedes adquirir experiencia adicional entregando el pescado a Wellington o entregándolo en la zona de barbacoa.]
    - (previous)
  - [Choice]: cond=Only if not asked last:|¿Por qué hay barcos piratas?
    - **Wellington:** ¡Esos barcos son luchadores! Están buscando algo con qué luchar.
    - **Wellington:** Si tienes acorazados, puedes enfrentarlos contra uno de los barcos piratas, pero ¡cuidado, {{Colour|#FF0000|los piratas nunca pierden}}!
    - (previous)
  - [Choice]: cond=Only if not asked last:|¿Cómo van las cosas?
    - **Wellington:** No me puedo quejar. {{Sic|Sunshine and fish what more could a man want?}}
    - **Wellington:** Aunque, dicho esto, no me importaría tener en mis manos a esa bestia en la piscina. Haría una comida digna de un reino.
    - **Wellington:** ¡Quizás necesite una caña más grande!
    - (previous)

### Any option with the Sandy Clue Scroll (historical)

- **Wellington:** ¡Toma, no quiero involucrarme en este {{Sic|fishyness}}!
- (Condition: Receiving a scroll box:)
  - (removes=Sandy Clue Scroll) (receives=Sandy Scroll box)
  - [scrollbox].}}
- (Condition: Receiving caskets:)
  - (Condition: Without free backpack space:)
    - [Necesitas 1 espacio libre en nuestro backpack para recibir tus cofres de pistas.]
  - (Condition: With free backpack space:)
    - (removes=Sandy Clue Scroll) (receives=Sandy Casket and its red version)
    - [¡Te entregan un ataúd!]
