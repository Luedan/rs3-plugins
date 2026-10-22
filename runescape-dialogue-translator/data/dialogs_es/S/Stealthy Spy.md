# Stealthy Spy

- **Original Wiki Page**: [Transcript:Stealthy Spy](https://runescape.wiki/w/Transcript%3AStealthy%20Spy)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pickpocket

- (Action: el player comienza a robar el Stealthy Spy.)
- (Condition: For each successful attempt:)
  - Escoges el bolsillo del objetivo.
  - Arrebatas las notas de los espías. Untarlos en chocolate sin posibilidad de reparación.
  - (Condition: With under 30,000 spring tokens:)
    - Se ha agregado lo siguiente a su bolsa de divisas: [número] Fichas de primavera.
    - (continue)
  - (Condition: With at least 30,000 spring tokens:)
    - Ha alcanzado el límite flexible del token Spring de 30 000. Debes gastar algunas fichas en la tienda de Gummy antes de poder ganar más.
    - (pop-up)
      - (Pop-up: You have reached the Spring token soft cap of 30,000. You need to spend some tokens in Gummy's store before you can earn more.|warning=yes)
      - (continue)
  - (Condition: If the success chance drops below 100%:)
    - Su objetivo carterista se da cuenta de su presencia.
- (Condition: With full backpack:)
  - No puedes seguir robando carteras porque tienes un inventario completo.
- (Condition: Getting caught:)
  - **Stealthy Spy:** {{RSChat|What do you think you're doing?}}
  - (Action: El Stealthy Spy golpea el player.)
  - No logras robarle al objetivo.
  - Has quedado atónito.
