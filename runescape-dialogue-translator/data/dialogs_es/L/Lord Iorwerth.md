# Lord Iorwerth

- **Original Wiki Page**: [Transcript:Lord Iorwerth](https://runescape.wiki/w/Transcript%3ALord%20Iorwerth)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### After Regicide and before Plague's End


#### Sin usar el equipo Mourner completo

- **Player:** Buenos días, Lord Iorwerth.
- **Lord Iorwerth:** Ahh Player. Buenos días, lo siento, no puedo parar a hablar. Hay tanto que hacer, tan poco tiempo.
- **Player:** Muy bien, adiós.

#### Mientras usas el equipo Mourner completo

- **Lord Iorwerth:** ¡¿Qué haces aquí?! Lo arruinarás todo... ¡Vuelve a Ardougne ahora!

#### Mientras usa equipo Mourner completo junto con artículos seleccionados que no son Mourner

- **Lord Iorwerth:** ¡¿Qué haces aquí?! Lo arruinarás todo... ¡Vuelve a Ardougne ahora! Y no dejes que te vuelva a ver con ese equipo no reglamentario.

### Treasure Trails


#### Sin espacio en backpack

- No tienes suficiente espacio en el inventario para llevarte la caja del rompecabezas.

#### Recibiendo la caja del rompecabezas

- **Lord Iorwerth:** ¡Antes de que te ayude, humano, debes completar esto por mí!
- (receives=puzzle box)
- [¡Lord Iorwerth te ha regalado una caja de rompecabezas!]

#### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- **Lord Iorwerth:** ¡No me hagas perder el tiempo, humano!

#### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- (Condition: If the trail continues:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [¡Lord Iorwerth te ha dado otro pergamino de pistas!]
  - (continue)
- (Condition: If the trail ends:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Lord Iorwerth:** ¡Lo has hecho bien, humano!
