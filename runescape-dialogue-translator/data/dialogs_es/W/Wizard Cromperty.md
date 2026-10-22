# Wizard Cromperty

- **Original Wiki Page**: [Transcript:Wizard Cromperty](https://runescape.wiki/w/Transcript%3AWizard%20Cromperty)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In East Ardougne


#### Hablando con él

- **Wizard Cromperty:**Hola Player, soy Cromperty. Sedridor me ha hablado de ti. ¡Como mago e inventor, él me ha ayudado en mi gran invento!
- [Menu]: Elige una opción:
  - [Choice]: ¿Dos trabajos? Eso tiene que ser duro.
    - **Player:** ¿Dos trabajos? Eso tiene que ser duro.
    - **Wizard Cromperty:** ¡No cuando los combinas no lo es! ¡Invento cosas MÁGICAS!
    - [Menu]: Selecciona una opción
      - [Choice]: Entonces, ¿qué has inventado?
        - (below|invent)
      - [Choice]: Bueno, te dejaré con tus inventos.
        - **Player:** Bueno, te dejo con tus inventos.
        - **Wizard Cromperty:** ¡Gracias por pasar por aquí! ¡Detente de nuevo en cualquier momento!
  - [Choice]: Entonces, ¿qué has inventado? {{anchor|invent}}
    - **Player:** Entonces, ¿qué has inventado?
    - **Wizard Cromperty:** ¡Ah! ¡Mi último invento es mi bloque de teletransportación pendiente de patente! ¡Emite una señal mágica de bajo nivel, que me permitirá ubicarlo en cualquier parte del mundo y teletransportar cualquier cosa directamente a él! ¡Espero revolucionar todo el sistema de teletransportación! ¿No crees que soy genial? Uh, quiero decir, ¿es genial?
    - [Menu]: Selecciona una opción
      - [Choice]: Entonces ¿dónde está el otro bloque?
        - **Player:** Entonces, ¿dónde está el otro bloque?
        - **Wizard Cromperty:** Bueno... Mmmm. Supongo que en algún lugar entre aquí y el Wizards' Tower en Misthalin. Todo lo que sé es que aún no ha llegado allí ya que los magos de allí me habrían contactado.
        - **Wizard Cromperty:** Estoy usando el RPDT para la entrega. Me aseguraron que sería entregado rápidamente.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Me pueden teletransportar por favor?
            - **Wizard Cromperty:** ¡Por supuesto! Sin embargo, me temo que no puedo darte ningún detalle sobre dónde saldrás. Presumiblemente donde se encuentre el otro bloque.
            - (continue)
          - [Choice]: ¿Quiénes son los RPDT?
            - **Player:** ¿Quiénes son los RPDT?
            - **Wizard Cromperty:** El equipo de entrega de paquetes de RuneScape. Vienen muy recomendables. Su lema es: "¡Nuestro objetivo es entregarte tus cosas en algún momento después de que nos hayas pagado!".
      - [Choice]: ¿Me pueden teletransportar por favor?
        - **Player:** ¿Me pueden teletransportar, por favor?
        - **Wizard Cromperty:** ¡Por supuesto! Sin embargo, me temo que no puedo darte ningún detalle sobre dónde saldrás. Presumiblemente donde se encuentre el otro bloque.
        - [Menu]: Selecciona una opción
          - [Choice]: Sí, eso suena bien. ¡Teletransportame!
            - **Player:** Sí, eso suena bien. ¡Teletransportame!
            - **Wizard Cromperty:** ¡Okey, dokey! ¿Listo?
            - (Condition: With unknown condition:)
              - **Wizard Cromperty:** {{RSChat|Dipsolum sententa sententi!}}
              - (Action: Wizard Cromperty teletransporta a el player a la oficina de RPDT.)
            - (Condition: With unknown condition:)
              - **Wizard Cromperty:** Hmmm... eso es extraño... Parece que no puedo recibir señal...
              - **Player:** Oh, bueno, no importa.
          - [Choice]: Eso suena peligroso. Déjame aquí.
            - **Player:** Eso suena peligroso. Déjame aquí.
            - **Wizard Cromperty:** Como desees.
      - [Choice]: Bien hecho, eso es muy inteligente.
        - **Player:** Bien hecho, es muy inteligente.
        - **Wizard Cromperty:** Sí, lo es, ¿no? Perdóneme por sentirme un poco engreído, ¡este es un gran avance en el campo de la teletransportación!
  - [Choice]: ¿Puedes teletransportarme a la Esencia Rúnica?
    - **Player:** ¿Puedes teletransportarme a la Esencia Rúnica?
    - **Wizard Cromperty:** {{RSChat|Senventior disthine molenko!}}
    - (Action: Wizard Cromperty teletransporta a el player a la mina Rune Essence.)

#### Opción de teletransporte

- **Wizard Cromperty:** {{RSChat|Senventior disthine molenko!}}
- (Action: Wizard Cromperty teletransporta a el player a la mina Rune Essence.)

#### Opción de reclamo


##### Con tareas medianas de Ardougne o superiores

- **Wizard Cromperty:** Como has hecho tan bien al impresionar no solo a los ciudadanos de Ardougne, sino también a los de Vanille, te daré la esencia de [700/1050]. ¡Feliz creación de runas!
- (receives=700 or 1050 noted pure essence)

##### Sin las tareas medianas Ardougne o superiores

- **Wizard Cromperty:** Lo siento, viejo amigo. No he conseguido nada para ti.
- Debes completar las tareas Ardougne Medianas o Difíciles para ganar las recompensas de Cromperty.

##### Habiendo ya reclamado el día

- **Wizard Cromperty:** Por mucho que me gustes, viejo, ya tienes tu esencia. Vuelve en [X] días/mañana.
