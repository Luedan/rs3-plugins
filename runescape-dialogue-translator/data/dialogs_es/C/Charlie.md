# Charlie

- **Original Wiki Page**: [Transcript:Charlie](https://runescape.wiki/w/Transcript%3ACharlie)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### Normalmente


##### Antes del Pico de las Águilas

- **Player:** ¡Hola!
- **Charlie:** Sí, ejem, ¡bienvenido al zoológico! Me temo que estoy un poco ocupado en este momento; ¿Qué era lo que querías?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Ah, suenas como alguien que necesita una misión!
    - (Condition: If the player is below level 27 in Hunter:)
      - **Charlie:** Bueno... tal vez. ¿Cuánto sabes sobre la caza?
      - **Player:** Bueno, sé un poco...
      - **Charlie:** No, me vendría bien un poco de ayuda, pero me temo que necesito a alguien con un poco más de experiencia.
      - Misión [Eagles' Peak].}}
      - (initial)
    - (Condition: If the player is level 27 or above in Hunter:)
      - (ver|Pico de las Águilas#Comenzando)
  - [Choice]: ¿De dónde sacaste los animales?
    - **Charlie:** ¡Los recibimos de todas partes! Los exploradores han traído las criaturas más exóticas y nos las han vendido.
    - (initial)
  - [Choice]: Sigan con el buen trabajo.
    - (end)

##### Después del pico de las Águilas

- **Player:** Hola, ¿cómo te llevas con ese hurón?
- **Charlie:** Bueno, parece ser tan cruel como el que perdimos, pero aún así estamos muy agradecidos por tu ayuda para adquirirlo.

#### Durante la búsqueda de huevos de Gielinor

- **Charlie:** ¡Bienvenido al zoológico! ¿Hay algo con lo que necesites ayuda?
- **Player:** Hola. Supongo que no habrás visto un huevo de oro por aquí, ¿verdad?
- **Charlie:** De hecho, tengo uno de los huevos aquí mismo.
- **Charlie:** El amable compañero que lo dejó dijo que alguien vendría a buscarlo. Aquí tienes.
- [Charlie te entrega el huevo de oro.]
- (Condition: Without backpack space for a holiday reward casket during the 2026 egg hunt:)
  - Necesitas al menos 1 espacio en tu backpack antes de reclamar este huevo de oro.
  - (pop-up)
    - (Pop-up: You need at least 1 space in your backpack before claiming this golden egg.|warning=yes)
    - (continue)
- (Condition: With free backpack space for a holiday reward casket during the 2026 egg hunt or during the 2025 egg hunt:)
  - ¡Encontraste un huevo de oro!
  - (pop-up)
    - (Pop-up: You found a golden egg!|colour=#00FF00)
    - (continue)
  - (Condition: During the 2025 egg hunt only:)
    - Se ha agregado lo siguiente a su bolsa de divisas: 2 x puntos Egg.
    - Se ha agregado lo siguiente a su bolsa de divisas: 10 x Puntos Treasure Trail.
    - (continue)
  - (Condition: During the 2026 egg hunt only:)
    - (receives=holiday reward casket)
    - Se ha agregado lo siguiente a su bolsa de divisas: 10 x Puntos Treasure Trail.
    - Se ha agregado lo siguiente a su bolsa de divisas: 200 x fichas de primavera.
    - (continue)
- **Player:** Gracias, Charlie.

### Using a ferret on him

- **Player:** Oye, tengo otro hurón, ¿estás interesado?
- **Charlie:** ¡Eh, oh! Bueno, eres muy amable, pero me temo que no necesitamos otro hurón en este momento. Ya tenemos suficientes problemas para domar al que tenemos.

### Historical dialogue


#### Antes del Pico de las Águilas

- **Player:** ¡Hola!
- **Charlie:** Sí, ejem, ¡bienvenido al zoológico! Me temo que estoy un poco ocupado en este momento; ¿Qué era lo que querías?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Ah, suenas como alguien que necesita una misión!
    - (arriba)
  - [Choice]: ¿De dónde sacaste los animales?
    - **Charlie:** ¡Los recibimos de todas partes! Los exploradores han traído las criaturas más exóticas y nos las han vendido.
    - **Player:** ¡¿Dónde en Gielinor conseguiste ese cíclope de aspecto aterrador?!
    - **Charlie:** ¡Sí, tiene un aspecto aterrador!
    - **Charlie:** Es de una tierra muy lejana, ¡no pudimos saber más ya que el explorador que lo trajo murió poco después!
  - [Choice]: Sigan con el buen trabajo.
    - (end)
