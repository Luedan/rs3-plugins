# Bandit (Pollnivneach)

- **Original Wiki Page**: [Transcript:Bandit (Pollnivneach)](https://runescape.wiki/w/Transcript%3ABandit%20%28Pollnivneach%29)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before The Feud

- **Player:** Hola.
- **Bandido:** ¿Qué quieres?
- **Player:** Bueno, en realidad nada, soy nuevo en la ciudad y quería conocer a los lugareños.
- **Bandido:** Estoy demasiado ocupado para charlar. Vuelva si tiene algún asunto que discutir con nosotros.

### After The Feud

- **Bandido:** ¡Perro! Mataste a nuestro campeón y por eso morirás.
- (Action: El bandido ataca a el player.)

### Pickpocket

- (Condition: If the player is caught)
  - **Bandido:** {{RSChat|What do you think you're doing?}}
  - No logras robarle el bolsillo al bandido.
  - Has quedado atónito.

### Lure

- **Player:** Psst.  Aquí quiero mostrarles algo.
- (Condition: If the bandit is fooled:)
  - **Bandido:** ¿Qué pasa?
  - **Player:** ¡Es una sorpresa! Sígueme.
- (Condition: If the bandit is not fooled:)
  - **Bandido:** ¡Vete! Estoy ocupado.

### Knock-Out


#### Si hay otro bandido o bandido alrededor

- Quizás no debería hacer esto todavía. Creo que otro bandido me verá.

#### Si el player no tiene un blackjack equipado

- **Player:** Necesito un arma diferente para hacer esto. <br/> Quiero noquearlos, no matarlos.

#### Si el player tiene un blackjack equipado

- (Action: el player golpea al bandido en la cabeza con el blackjack. El bandido cae al suelo.)
- Golpeas al bandido en la cabeza y lo dejas inconsciente.
- **Bandido:** {{RSChat|Zzzzzz}}
- (Action: El bandido se levanta.)
- **Bandido:** {{RSChat|Arghh my head.}}
