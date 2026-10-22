# Peckish

- **Original Wiki Page**: [Transcript:Peckish](https://runescape.wiki/w/Transcript%3APeckish)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Peckish:** ¿Tienes algo de eso bueno para mí?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué buscas?
    - **Player:** ¿Qué buscas?
    - **Peckish:** Objetos de valor, riquezas, tesoros perdidos hace mucho tiempo. Cualquier cosa que pueda vender para ayudar a llenar las arcas del clan.
    - **Peckish:** Verás, las cosas por aquí no tienden a permanecer enterradas. Algunas de estas tumbas están tan cargadas de riquezas que literalmente están a punto de estallar.
    - **Peckish:** De vez en cuando, los ataúdes y mausoleos se abren y se vuelven accesibles para cualquier persona cercana con dedos ligeros.
    - **Peckish:** Si alguna de estas curiosidades antiguas de alguna manera llega a tus manos, estaré feliz de pagar por ellas; Tengo una valla bastante respetable.
    - (previous)
  - [Choice]: Tengo algunos productos para ti.
    - **Player:** Tengo algunos productos para ti.
    - **Peckish:** ¡Sssh, ssh! Mantenlo bajo. Déjame ver qué tienes ahí...
    - (Condition: Without ancient heirlooms or ancient valuables:)
      - No tienes nada que darle a Peckish.
      - (ventana emergente)
        - (Pop-up: You have nothing to give to Peckish.|warning=yes)
        - (previous)
    - (Condition: With ancient heirlooms or ancient valuables:)
      - (Condition: If not surpassing 150,000 spooky tokens if all ancient heirlooms and ancient valuables in backpack would be handed in:)
        - (removes=all ancient heirlooms and ancient valuables)
        - Entregas riquezas [número] [valuable/valuables] y [número] por tokens Spooky [number before potential multiplication].
        - (ventana emergente)
          - (Pop-up: You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.|colour=#FF6600)
          - (continue)
        - Se ha agregado lo siguiente a su bolsa de divisas: [number after potential multiplication] x tokens Spooky.
        - (previous)
      - (Condition: If surpassing 150,000 spooky tokens if all ancient heirlooms and ancient valuables in backpack would be handed in:)
        - (Condition: With something to hand in without surpassing 150,000 spooky tokens:)
          - **Peckish:** Vaya, amigo. Eso es demasiado rico para mis huesos. Puedo tomar algunas de esas, pero tendrás que gastar algunas fichas espeluznantes antes de que tome el resto.
          - (removes=just enough ancient heirlooms and ancient valuables to not surpass 150,000 spooky tokens, with as many as possible ancient heirlooms included)
          - Entregas riquezas [número] [valuable/valuables] y [número] por tokens Spooky [number before potential multiplication].
          - (ventana emergente)
            - (Pop-up: You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.|colour=#FF6600)
            - (continue)
          - (Condition: If reaching exactly 150,000 spooky tokens:)
            - Ha alcanzado el límite flexible del token Spooky de 150.000. Debes gastar algunas fichas en Spooky Reward Shop antes de poder ganar más.
            - (pop-up)
              - (Pop-up: You have reached the Spooky token soft cap of 150,000. You need to spend some tokens in the Spooky Reward Shop before you can earn more.|warning=yes)
              - (continue)
          - Se ha agregado lo siguiente a su bolsa de divisas: [número] x tokens Spooky.
          - (previous)
        - (Condition: Without anything to hand in without surpassing 150,000 spooky tokens:)
          - **Peckish:** No puedo tomar más de esos en este momento; Tienes que gastar algunas de tus espeluznantes fichas o no podré pagarte.
          - (previous)
  - [Choice]: Adiós.
    - **Player:** Adiós.
    - **Peckish:** *sollozo* Adiós.

### Hand in


#### Con reliquias antiguas u objetos de valor antiguos


##### Si no se superan los 150.000 tokens espeluznantes, se entregarían todas las reliquias antiguas y objetos de valor antiguos en backpack.

- (removes=all ancient heirlooms and ancient valuables)
- Entregas riquezas [número] [valuable/valuables] y [número] por tokens Spooky [number before potential multiplication].
- (ventana emergente)
  - (Pop-up: You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.|colour=#FF6600)
  - (continue)
- Se ha agregado lo siguiente a su bolsa de divisas: [number after potential multiplication] x tokens Spooky.

##### Si se superan los 150.000 tokens espeluznantes, si se entregaran todas las reliquias antiguas y objetos de valor antiguos en backpack


##### Con algo que entregar sin superar las 150.000 fichas espeluznantes

- **Peckish:** Vaya, amigo. Eso es demasiado rico para mis huesos. Puedo tomar algunas de esas, pero tendrás que gastar algunas fichas espeluznantes antes de que tome el resto.
- (removes=just enough ancient heirlooms and ancient valuables to reach 150,000 spooky tokens, with as many as possible ancient heirlooms included)
- Entregas riquezas [número] [valuable/valuables] y [número] por tokens Spooky [number before potential multiplication].
- (ventana emergente)
  - (Pop-up: You hand over [number] [valuable/valuables] and [number] riches for [number before potential multiplication] Spooky tokens.|colour=#FF6600)
  - (continue)
- (Condition: If reaching exactly 150,000 spooky tokens:)
  - Ha alcanzado el límite flexible del token Spooky de 150.000. Debes gastar algunas fichas en Spooky Reward Shop antes de poder ganar más.
  - (pop-up)
    - (Pop-up: You have reached the Spooky token soft cap of 150,000. You need to spend some tokens in the Spooky Reward Shop before you can earn more.|warning=yes)
    - (continue)
- Se ha agregado lo siguiente a su bolsa de divisas: [número] x tokens Spooky.

##### Sin nada que entregar sin superar las 150.000 fichas espeluznantes

- **Peckish:** No puedo tomar más de esos en este momento; Tienes que gastar algunas de tus espeluznantes fichas o no podré pagarte.

#### Sin reliquias antiguas ni objetos de valor antiguos

- No tienes nada que darle a Peckish.
- (ventana emergente)
  - (Pop-up: You have nothing to give to Peckish.|warning=yes)
