# Zookeeper

- **Original Wiki Page**: [Transcript:Zookeeper](https://runescape.wiki/w/Transcript%3AZookeeper)
- **Letter**: `Z`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Player:** ¡Hola!
- **Cuidador del zoológico:** ¡Bienvenido al zoológico Ardougne! ¿Le puedo ayudar en algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Tienes alguna misión para mí?
    - **Zookeeper:** No por el momento. Los exploradores que regresan de tierras lejanas cuentan historias asombrosas. ¡Asegúrate de mantener los ojos y los oídos abiertos ya que puedes encontrar nuevos lugares para explorar!
    - **Player:** ¡Oh, lo haré!
    - (initial)
  - [Choice]: ¿De dónde sacaste los animales?
    - **Zookeeper:** ¡Los recibimos de todas partes! Los exploradores han traído las criaturas más exóticas y nos las han vendido.
  - [Choice]: Sigan con el buen trabajo.
    - (end)

### Treasure Trails

- (Condition: Only the first time:)
  - **Zookeeper:** Antes de ayudarte, ¿puedes hacer algo por mí?
  - **Player:** Claro.
  - **Zookeeper:** Necesito saber cuántos camellos tenemos.
- (receives=challenge scroll (medium))
- [¡El cuidador del zoológico te ha dado un pergamino de desafío!]

##### Cuando hablé de nuevo

- **Zookeeper:** Por favor, dime cuántos camellos hay.
- Ingrese la cantidad:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Zookeeper:** Lo siento, ¡pero eso no suena bien!
- (Condition: When given the correct answer:)
  - (removes=the old clue scroll (medium) y desplazamiento de desafío (medio))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [¡El cuidador del zoológico te ha dado otro pergamino de pistas!]
    - (continue)
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
    - (continue)
  - **Zookeeper:** ¡Gracias!
