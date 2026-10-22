# Luthas

- **Original Wiki Page**: [Transcript:Luthas](https://runescape.wiki/w/Transcript%3ALuthas)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At Musa Point

- **Luthas:** Hola, soy Luthas, administro la plantación de plátanos aquí.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podría ofrecerme empleo en su plantación?
    - **Player:** ¿Podría ofrecerme empleo en su plantación?
    - **Luthas:** Sí, puedo solucionar algo. Hay una caja lista para cargar en el barco.
    - **Luthas:** No creerías la demanda de bananas de la tienda de Wydin en Port Sarim. Creo que esta es la tercera caja que le envío este mes.
    - **Luthas:** Si puedes llenarlo con plátanos, te pagaré 30 de oro.
  - [Choice]: Esa customs officer es molesta ¿no?
    - **Player:{{anchor|annoying}}** Esa customs officer es molesta, ¿no?
    - **Luthas:** Bueno, la conozco bastante bien. Ella ya no me causa ningún problema.
    - **Luthas:** Ya ni siquiera busca en mis cajas de exportación. Ella sabe que sólo contienen plátanos.
    - **Player:** ¿En serio? Qué interesante. ¿A dónde los enviáis?
    - **Luthas:** Hay una pequeña tienda en Port Sarim que los compra por cajas. Creo que está dirigido por un hombre llamado Wydin.

### Speaking to Luthas again

- **Luthas:** ¿Ya has completado tu tarea?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué tuve que hacer de nuevo?
    - **Player:** ¿Qué tuve que hacer de nuevo?
    - **Luthas:** Hay una caja lista para cargar en el barco. Si puedes llenarlo con plátanos, te pagaré 30 de oro.
  - [Choice]: No, la caja aún no está llena...
    - **Player:** No, la caja aún no está llena...
    - **Luthas:** Bueno, volveremos cuando sea así.
  - [Choice]: Entonces, ¿adónde se entregarán estos plátanos?
    - **Player:{{anchor|wydin}}** Entonces, ¿a dónde se entregarán estos plátanos?
    - **Luthas:** Se los vendo a Wydin, que tiene una tienda de comestibles en Port Sarim.
  - [Choice]: Esa customs officer es molesta ¿no?
    - (above|annoying)

### After filling up the crate

- **Player:** He llenado una caja con plátanos.
- **Luthas:** Bien hecho, aquí está tu pago.
- (receives=30 coins)
- [Menu]: Selecciona una opción
  - [Choice]: ¿Me pagarás por otra caja llena?
  - **Player:** ¿Me pagarás por otra caja llena?
    - **Luthas:** Sí, claro.
    - **Luthas:** Si sales, deberías ver que la caja vieja ha sido cargada en el barco y que hay otra caja vacía en su lugar.
  - [Choice]: Gracias, estaré en camino.
    - **Player:** Gracias, estaré en camino.
  - [Choice]: Entonces, ¿adónde se entregarán estos plátanos?
    - (above|wydin)
  - [Choice]: Esa customs officer es molesta ¿no?
    - (above|annoying)

### Treasure Trails

- **Luthas:** Felicitaciones.
- (removes=the old clue scroll (medium))
- (Condition: If the trail continues:)
  - (receives=a new clue scroll (medium))
  - [¡Luthas te ha dado otro pergamino de pistas!]
- (Condition: If the trail ends:)
  - (receives=reward casket (medium))
  - [¡Has encontrado un ataúd!]

### Sandy Clue Scroll (historical)

- **Luthas:** Ah, mi mono encontró esto para ti.
- ((Without space in backpack for a casket:))
  - Necesitas más espacio en el inventario para recibir tu cofre de pistas.
- ((With space in backpack:))
  - (removes=Sandy Clue Scroll)
  - (Condition: If the trail continues:)
    - (receives=Sandy Scroll box)
    - [scrollbox].}}
  - (Condition: If the trail ends:)
    - (receives=Sandy Casket and Sandy Casket (red))
    - [¡Te entregan un ataúd!]
