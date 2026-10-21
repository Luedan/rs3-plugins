# Brigand

- **Original Wiki Page**: [Transcript:Brigand](https://runescape.wiki/w/Transcript%3ABrigand)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before The Feud

- **Player:** Hola.
- **Brigand:** ¿Qué quieres?
- **Player:** Bueno, en realidad nada, soy nuevo en la ciudad y quería conocer a los lugareños.
- **Brigand:** Estoy demasiado ocupado para charlar. Vuelva si tiene algún asunto que discutir con nosotros.

### After The Feud

- **Brigand:** ¡Perro! Mataste a nuestro campeón y por eso morirás.
- (Action: El bandido ataca a el player.)

### Pickpocket

- (Condition: Si el player es atrapado)
  - **Brigand:** {{RSChat|What do you think you're doing?}}
  - No logras robarle el bolsillo al bandido.
  - Has quedado atónito.

### Lure

- **Player:** Psst.  Aquí quiero mostrarles algo.
- (Condition: Si el bandido se deja engañar:)
  - **Brigand:** ¿Qué es?
  - **Player:** ¡Es una sorpresa! Sígueme.
- (Condition: Si el bandido no se deja engañar:)
  - **Brigand:** ¡Vete! Estoy ocupado.

### Knock-Out


#### Si hay otro bandolero o bandido cerca

- Quizás no debería hacer esto todavía. Creo que otro bandido me verá.

#### Si el player no tiene un blackjack equipado

- **Player:** Necesito un arma diferente para hacer esto. <br/> Quiero noquearlos, no matarlos.

#### Si el player tiene un blackjack equipado

- (Action: el player golpea al bandido en la cabeza con la cachiporra. El bandido cae al suelo.)
- Golpeas al bandido en la cabeza y lo dejas inconsciente.
- **Brigand:** {{RSChat|Zzzzzz}}
- (Action: El bandido se levanta.)
- **Brigand:** {{RSChat|Arghh my head.}}
