# Feng, the Bounty Master

- **Original Wiki Page**: [Transcript:Feng, the Bounty Master](https://runescape.wiki/w/Transcript%3AFeng%2C%20the%20Bounty%20Master)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talking to Feng, the Bounty Master

- **Feng, the Bounty Master:**  Bienvenido, compañero mercenario, bienvenido.
- **ELIGE UNA OPCIÓN:**
  - ¿Puedes asignarme una recompensa?
    - ((Si actualmente no tienes una recompensa y te quedan recompensas:))
      - **Feng, the Bounty Master:**  ¿Por qué facción luchas hoy, amigo mío?
      - **SELECCIONA UNA FACCIÓN CON LA QUE GANAR REPUTACIÓN.**
        - Sliske.
          - **Feng, the Bounty Master:**  Muy bien. ¡Tu recompensa es matar a los leales a [Faction] en nombre de Sliske!
          - (previous2)
        - Zamorak.
          - **Feng, the Bounty Master:**  Muy bien. ¡Tu recompensa es matar a los leales a [Faction] en nombre de Zamorak!
          - (previous2)
        - Seren.
          - **Feng, the Bounty Master:**  Muy bien. ¡Tu recompensa es matar a los leales a [Faction] en nombre de Seren!
          - (previous2)
        - Zaros.
          - **Feng, the Bounty Master:**  Muy bien. ¡Tu recompensa es matar a los leales a [Faction] en nombre de Zaros!
          - (previous2)
    - ((Si actualmente no tienes una recompensa y no te quedan recompensas:))
      - **Feng, the Bounty Master:** ¡Qué sanguinario! Ya has tenido tu cuota de recompensas, amigo mío. Vuelve otro día.
      - (previous)
    - ((Si actualmente tienes una recompensa:))
      - ((Si estás ganando reputación con Sliske:))
        - **Feng, the Bounty Master:**  ¡Ya tienes una recompensa para matar a los leales a [Faction] en nombre de Sliske!
        - (previous)
      - ((Si estás ganando reputación con Zamorak:))
        - **Feng, the Bounty Master:**  ¡Ya tienes una recompensa para matar a los leales a [Faction] en nombre de Zamorak!
        - (previous)
      - ((Si estás ganando reputación con Seren:))
        - **Feng, the Bounty Master:**  ¡Ya tienes una recompensa para matar a los leales a [Faction] en nombre de Seren!
        - (previous)
      - ((Si estás ganando reputación con Zaros:))
        - **Feng, the Bounty Master:**  ¡Ya tienes una recompensa para matar a los leales a [Faction] en nombre de Zaros!
        - (previous)
  - ¿Cuántas recompensas tengo disponibles?
    - ((Con recompensas restantes:))
      - ((Si actualmente no tienes una recompensa:))
        - **Feng, the Bounty Master:**  Puedo asignarte [número] [bounty/bounties] antes de que alcances tu cuota. ¿Puedes tener uno ahora, si quieres?
          - Sí, me gustaría una recompensa.
            - (above|get-bounty)
          - No, no ahora mismo.
            - (previous)
      - ((Si actualmente tienes una recompensa:))
        - **Feng, the Bounty Master:**  Puedo asignarte [número] [bounty/bounties] antes de que alcances tu cuota.
        - (previous)
    - ((Sin recompensas restantes:))
      - **Feng, the Bounty Master:** ¡Qué sanguinario! Ya has tenido tu cuota de recompensas, amigo mío. Vuelve otro día.
      - (previous)
  - ((Si actualmente tienes una recompensa:))
    - Me gustaría abandonar mi recompensa actual.
      - **Feng, the Bounty Master:**  Hmm, ¿abandonas tu recompensa? Debo advertirte que seguirá contando para tu cuota. ¿Está seguro?
      - **¿ABANDONAS TU RECOMPENSA ACTUAL?**
        - Sí, abandona mi recompensa.
          - (Se elimina la recompensa).
          - (previous2)
        - No, quédate con mi recompensa.
          - (previous2)
  - ¿Puedes contarme más sobre tus recompensas?
    - **Feng, the Bounty Master:** Asigno recompensas a compañeros mercenarios como tú. Verás, esto es una guerra y hay que matar. Los acuerdos que cerré con los representantes de las facciones aquí significan que puedes elegir uno para hacer tus recompensas, ganando reputación con ellos a cambio.
    - **Player:** ¿Qué implica una recompensa?
    - **Feng, the Bounty Master:**  Bueno, matar, por supuesto. Te asigno cien muertes de la facción, para ser precisos, ¡pero si matas a su general cuenta como veinticinco! Tú eliges la facción por la que luchas, yo elijo la facción contra la que luchas y luego te vas. Feliz caza.
    - **Player:** Entonces, ¿por qué estás aquí en primer lugar?
    - **Feng, the Bounty Master:** Soy un mercenario, como cualquier otra persona en este lugar devastado por la guerra. Por supuesto que tengo mis propios planes nefastos, pero eso es algo que debo saber yo.
    - (previous)
  - Adiós.
    - **Feng, the Bounty Master:** Feliz caza.

### Get bounty

- (above|get-bounty)

### Hand in bounty


#### Sin recompensa

- **Feng, the Bounty Master:** No puedes entregar una recompensa, no te he asignado ninguna...
- (above|options)

#### Con una recompensa incompleta

- **Feng, the Bounty Master:** Aún no has completado tu recompensa. Ve y mata a algunos más.
- (above|options)

#### Con una recompensa completa

- **Feng, the Bounty Master:** Ah, sí, veo que has completado tu recompensa. Buena caza, aquí tienes tu recompensa.
- ((Si se entregó una recompensa Serenista:))
  - ¡Has ganado 150 de reputación con las fuerzas serenistas!
  - (above|bounties-available)
- ((Si se entregó una recompensa de Sliske:))
  - ¡Has ganado 150 de reputación con las fuerzas de Sliske!
  - (above|bounties-available)
- ((Si se entregó una recompensa zamorakiana:))
  - ¡Has ganado 150 puntos de reputación con las fuerzas zamorakianas!
  - (above|bounties-available)
- ((Si se entregó una recompensa zarosiana:))
  - ¡Has ganado 150 de reputación con las fuerzas zarosianas!
  - ((Si los componentes de ilujankan estuvieran desbloqueados:))
    - Ahora puede descubrir el plano de los componentes de Ilujankan si tiene al menos 89 Invention.
    - (continue)
  - (above|bounties-available)

### Using the broken disguise kit

- **Feng, the Bounty Master:**  Interesante hallazgo. Lo has traído al lugar correcto.
- **Seleccione una opción**
  - Por supuesto que lo hice.
    - **Player:** Era cuestión de tiempo. Sólo hay cinco personas aquí arriba.
  - ¿Lo hice?
    - (continue)
- **Player:** ¿Para qué podrías quererlo?
- **Feng, the Bounty Master:** He oído hablar de un [gal/guy] que colecciona baratijas extrañas. Quizás pueda obtener un precio justo.
- **Feng, the Bounty Master:** ¿Tal vez usted mismo estaría interesado en un intercambio razonable? Adquirí una bocina de señales encantada que estaría dispuesto a dejar ir.
- **¿Cambiar tu cofre de basura por una bocina de señal?**
  - si
    - (removes=the broken disguise kit) (receives=a signal horn)
    - [Feng te da un cuerno a cambio del cofre. De quienquiera que esté hablando le deben gustar algunas cosas raras.]
  - No
    - (end)
