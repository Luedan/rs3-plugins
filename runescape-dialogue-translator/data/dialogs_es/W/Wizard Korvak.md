# Wizard Korvak

- **Original Wiki Page**: [Transcript:Wizard Korvak](https://runescape.wiki/w/Transcript%3AWizard%20Korvak)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|missing dialogue from having omni-talisman + runecrafting staff/tiara in the backpack}}

### Standard dialogue

- **Wizard Korvak:** ¡AAAAAAAAAAH! No me acerques así.
- **Player:** Eh, lo siento.
- [Menu]: Elige una opción:
  - [Choice]: ¿Puedes ayudarme con mis bolsas de esencias?
    - **Player:** ¿Puedes ayudarme con mis bolsas de esencias?
    - (Condition: If the player doesn't have any pouches that need repair:)
      - **Wizard Korvak:** No tienes ninguna bolsa que necesite reparación... Podría venderte una bolsa, ¡pero solo si no me lo dices!
      - [Menu]: Selecciona una opción
        - [Choice]: Me gustaría comprar una bolsa.
          - (continue|Trade option)
        - [Choice]: No importa.
          - **Player:** No importa.
    - (Condition: If the player has pouches that need repair:)
      - **Wizard Korvak:** Puedo restaurarlos por un precio; por un precio, de hecho. ¡Muajajajajajajaja!
      - **Player:** Eh, ¿qué tipo de precio?
      - **Wizard Korvak:** Lo que las voces me digan que pida. Actualmente, necesitan 9.000 po para una bolsa grande y 12.000 po para una bolsa gigante. Shhhh, no se lo digas a nadie más: tengo una conexión por dentro y te puedo vender bolsas también. Por sólo 25.000 po, puedes tener una bolsa grande. Con 50.000 po razonables conseguirás una bolsa gigante.
        - [Choice]: Me gustaría que me repararan una bolsa.
          - **Player:** Me gustaría que repararan una bolsa.
          - **Wizard Korvak:** Muy bien. Echemos un vistazo.
          - (continue|Repair-all option)
        - [Choice]: Me gustaría comprar una bolsa.
          - (continue|Trade option)
  - [Choice]: cond=If the medium pouch has been lost:|He perdido mi bolsa mediana. ¿Podrías reemplazarlo?
    - **Player:** He perdido mi bolsa mediana. ¿Podrías reemplazarlo?
    - (receives=medium pouch)
    - **Wizard Korvak:** Lo perdiste, ¿verdad? ¿O lo retiraron? ¡RECLAMARLO DE VUELTA! Rápido, será mejor que tomemos otro antes de que lleguen las cucharas.
  - [Choice]: ¿Por qué estás tan nervioso?
    - **Player:** ¿Por qué estás tan nervioso?
    - **Wizard Korvak:** ¡No estoy nervioso! Estoy loco. Hay una diferencia.
    - **Player:** Si estás loco, ¿no creerías que estás cuerdo y por eso serías insensible a la locura que eres?
    - **Wizard Korvak:** Yebno.
    - **Player:** ¿Perdón?
    - **Wizard Korvak:** Yebno. Es una forma rápida de decir Sí, tal vez no. Como no sabía la respuesta a tu pregunta, te di todas las respuestas.
    - **Player:** ¿Cómo llegaste a tener esa mentalidad tan peculiar?
    - **Wizard Korvak:** Me enviaron al lugar. Sabían que los magos oscuros estaban allí y que alguien los había traicionado. A nosotros. Entonces me enviaron a espiar. Al lugar. Me enviaron y no me dejaron volver.
    - **Player:** ¿Quién te envió? ¿Qué traición?
    - **Wizard Korvak:** Se sienta ahí con la luz girando, siempre pensando. Uno de nosotros los llevó al lugar donde martilleaba el pico y así ocurrió la traición. Por favor no me hagas hablar de eso.
    - **Player:** Está bien, no tenemos que hablar de eso.
  - [Choice]: ¿Quién es ese mago fuera del portal del gremio?
    - **Wizard Korvak:** Ah, el joven Finix: ¡un joven y brillante mago!
    - **Vief:** ¡Joven alborotador, más bien!
    - **Wizard Korvak:** El hecho de que sus teorías choquen con las tuyas no significa que sean incorrectas.
    - **Vief:** ¡La mera idea de que los altares se estén acabando es absurda! No puedes quedarte sin espacio en una dimensión infinitamente plegada.
    - **Wizard Korvak:** Sólo porque el espacio es infinito, no significa que la energía del interior llene todo el espacio.
    - **Vief:** ¡Por supuesto que sí! Todos sabemos que la energía dentro de una dimensión debe distribuirse uniformemente para evitar que colapse sobre sí misma.
    - **Wizard Korvak:** Puede que sea cierto, pero ¿por qué entonces los altares de Gielinor están agrietados?
    - **Player:** Er... Voy a dejar que ustedes se queden con eso.
  - [Choice]: No importa.
    - **Player:** No importa.

### Trade option

- **Player:** Me gustaría comprar una bolsa.
- **Wizard Korvak:** Ah, coins para financiar mi colección de rocas.
- [Menu]: ¿Qué bolsa te gustaría comprar?
  - [Choice]: Compra una bolsa grande por 25.000 po.
    - (Condition: If the player doesn't already have a large pouch:)
      - (removes=25,000 coins) (receives=large pouch)
    - (Condition: If the player already has a large pouch:)
      - **Wizard Korvak:** ¡Ya tienes una bolsa grande! ¿No sabes que desequilibrarás el mundo si tienes dos? Los perros odiarán a los gatos, los ratones bailarán y todos vendrán por mí. No, no hay bolsa para ti.
  - [Choice]: Compra una bolsa gigante por 50.000 po.
    - (Condition: If the player doesn't already have a giant pouch:)
      - (removes=50,000 coins) (receives=giant pouch)
    - (Condition: If the player already has a large pouch:)
      - **Wizard Korvak:** No, no, no. Me dijeron cuando estuve allí. Sólo una preciosa bolsa, por tamaño, por persona. No más. No puedo venderte esta bolsa, o podrían hacerme regresar allí para recibir castigos.
  - [Choice]: No importa.
    - **Player:** No importa.

### Repair-all option

- [Menu]: ¿Qué bolsa te gustaría reparar?
  - [Choice]: Reparar una bolsa grande por 9.000 po.
    - (Condition: If the pouch needs repair:)
      - **Wizard Korvak:** Magic me hace feliz, la magia me alegra, la magia calma las voces y nada rima con morado.
    - (Condition: If the pouch does not need repair:)
      - **Wizard Korvak:** ¡Las voces están enojadas contigo! No tienes nada que reparar. Déjanos en paz.
    - (Condition: If the player does not have enough money:)
      - {{Transcript missing}}
  - [Choice]: Reparar bolsa gigante por 12.000 po.
    - (Condition: If the pouch needs repair:)
      - **Wizard Korvak:** Ahhh, el simple acto de un hechizo de transformación. Tan reconfortante. Silencia las voces. Su bolsa está reparada.
    - (Condition: If the pouch does not need repair:)
      - **Wizard Korvak:** ¡Las voces están enojadas contigo! No tienes nada que reparar. Déjanos en paz.
    - (Condition: If the player does not have enough money:)
      - {{Transcript missing}}
  - [Choice]: No importa.
    - (end)
