# Bolkoy

- **Original Wiki Page**: [Transcript:Bolkoy](https://runescape.wiki/w/Transcript%3ABolkoy)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Tree Gnome Village

- **Player:** Hola.
- **Bolkoy:** Hola extraño, ¿nuevo en estos lugares? Por cierto, soy Bolkoy. Soy el comerciante del pueblo. ¿Quieres comprar algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué tienes?
    - **Player:** ¿Qué tienes?
    - **Bolkoy:** Echa un vistazo.
    - (opens=Bolkoy's Village Shop)
  - [Choice]: No, gracias.
    - **Player:** No, gracias.
    - **Bolkoy:** Ok, tal vez más tarde.

### After Tree Gnome Village

- **Player:** Hola.
- **Bolkoy:** Bienvenido, bienvenido. Es bueno verte de nuevo. La aldea es mucho más segura ahora que has devuelto los orbes.
- **Bolkoy:** Por cierto, soy el tendero del pueblo. ¿Quieres comprar algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué tienes?
    - (arriba)
  - [Choice]: No, gracias.
    - (arriba)

### Treasure Trails

- **Bolkoy:** ¡Hola! ¿Supongo que estás aquí por el rastro?
- **Player:** Sí. ¿Tienes un desafío para mí?
- **Bolkoy:** ¡Sí, aquí mismo!
- (receives=challenge scroll)
- [¡Bolkoy te ha dado un pergamino de desafío!]

##### Cuando hablé de nuevo

- **Bolkoy:** Ingrese la respuesta a la pregunta.
- (Condition: When given the wrong answer:)
  - **Bolkoy:** ¿Qué te pasa? ¿No puedes contar? ¡Esfuérzate más!
- (Condition: When given the correct answer:)
  - **Bolkoy:** ¡Por suerte para ti, esa es la respuesta correcta!
  - (continue)
- (removes=the challenge scroll and the old clue scroll (medium))
- ((If the trail continues:))
  - (receives=a new clue scroll (medium))
  - [¡Bolkoy te ha dado otro pergamino de pistas!]
- ((If the trail ends:))
  - (receives=reward casket (medium))
  - [¡Has encontrado un ataúd!]
