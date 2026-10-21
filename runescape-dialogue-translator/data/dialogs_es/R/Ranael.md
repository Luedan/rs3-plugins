# Ranael

- **Original Wiki Page**: [Transcript:Ranael](https://runescape.wiki/w/Transcript%3ARanael)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Al Kharid


#### Hablando con ella

- **Ranael:** ¿Quieres comprar faldas blindadas? Diseñado especialmente para mujeres a las que les gusta pelear.
- [Menu]: Elige una opción:
  - [Choice]: Sí, por favor.
    - (opens=Ranael's Super Skirt Store)
  - [Choice]: No, gracias, ese no es mi lugar.
    - **Player:**No, gracias, ese no es mi lugar.
  - [Choice]: ¿Qué opinas de Ali Morrisane?
    - **Player:**¿Qué opinas de Ali Morrisane?
    - **Ranael:** Es un hombre astuto. Trajo a varios hombres de su pueblo natal para intentar montar aquí tiendas, o eso dice. Pero si recién están estableciendo sus negocios, ¿por qué necesita enviarlos para amenazarnos? ¡Uno de ellos vino aquí, agitó su martillo peligrosamente y dijo que las cosas serían peores para nosotros si no nos uníamos a ellos!
    - **Player:** ¿Qué harás al respecto?
    - **Ranael:** No voy a permitir que esos matones me echen de esta ciudad. Así que seguiré vendiendo faldas blindadas aquí. ¿Quieres comprar alguno?
    - (initial)

#### Entregándole un folleto de Al Kharid

- **Player:** Hola. Tengo este vale de descuento.
- **Ranael:** Ya veo. Lamentablemente, parece haber caducado ayer. No importa.
- **Player:** ¡Pero acabo de recibirlo!
- **Ranael:** Lo siento. No hay nada que pueda hacer. Adiós.

#### Sandy Pergamino de pistas (histórico)

- **Ranael:** Me han dicho que necesitas esto.
- ((Sin espacio en backpack para ataúd:))
  - Necesitas más espacio en el inventario para recibir tu cofre de pistas.
- ((Con espacio en backpack:))
  - (removes=Sandy Clue Scroll)
  - (Condition: Si el rastro continúa:)
    - (receives=Sandy Scroll box)
    - [scrollbox].}}
  - (Condition: Si el sendero termina:)
    - (receives=Sandy Casket and Sandy Casket (red))
    - [¡Te entregan un ataúd!]
