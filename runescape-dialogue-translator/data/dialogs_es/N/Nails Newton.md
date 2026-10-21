# Nails Newton

- **Original Wiki Page**: [Transcript:Nails Newton](https://runescape.wiki/w/Transcript%3ANails%20Newton)
- **Letter**: `N`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Let Them Eat Pie

- (ver|Déjalos comer pastel#Contratado para robar)

### After Let Them Eat Pie

- (ver|Déjalos comer pastel#Diálogo posterior a la misión)

### Treasure Trails


#### Recibiendo el pergamino de desafío

- (Condition: Sólo la primera vez:)
  - **Nails Newton:** ¿Estás aquí por algo?
  - **Player:** Estoy intentando completar un rastro del tesoro.
  - **Nails Newton:** Bueno, primero debes hacerme este favor.
- (receives=challenge scroll (medium))
- [¡Nails Newton te ha dado un pergamino de desafío!]

#### Cuando hablé de nuevo

- **Nails Newton:** Ingrese la respuesta a la pregunta.
- Ingrese la cantidad:<br>[Input field]
- (Condition: Cuando se le da la respuesta incorrecta:)
  - **Nails Newton:** Incorrecto. ¿Has probado a contar?
- (Condition: Cuando se le da la respuesta correcta:)
  - (removes=the clue scroll (medium) y desplazamiento de desafío (medio))
  - (Condition: Si el rastro continúa:)
    - (receives=a new clue scroll (medium))
    - [¡Nails Newton te ha dado otro pergamino de pistas!]
    - (continue)
  - (Condition: Si el sendero termina:)
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
    - (continue)
  - **Nails Newton:** ¡Correcto!
