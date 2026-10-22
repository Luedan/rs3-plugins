# Smokey

- **Original Wiki Page**: [Transcript:Smokey](https://runescape.wiki/w/Transcript%3ASmokey)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Upon appearing

- (Action: Smokey el carbón aparece cerca de la estufa con una barra de progreso roja encima.)
- {{Colour AAH! TOO HOT! TOO HOT!}}
- **Smokey:** {{RSChat|AAH! TOO HOT! TOO HOT!}}

### Pelt snowball


#### Antes de que Smokey se haya enfriado


##### Sin bola de nieve equipada

- Necesitas equipar una bola de nieve para enfriar el carbón.
- (pop-up)
  - (Pop-up: You need to equip a snowball to cool down the coal.|warning=yes)

##### Con una bola de nieve equipada.

- (removes=one equipped snowball)
- (Condition: If this was the third snowball pelted:)
  - (Condition: With less than 49,926 Christmas spirit:)
    - (receives=75 Christmas spirit)
    - Se ha añadido lo siguiente a su bolsa de divisas: 75 x Espíritu navideño.
    - (continue)
  - (Condition: With at least 49,926 Christmas spirit:)
    - (Condition: With under 50,000 Christmas spirit:)
      - (receives=as much Christmas spirit as is missing from 50,000)
      - Se ha agregado lo siguiente a su bolsa de divisas: [número] x Espíritu navideño.
      - (continue)
    - Has alcanzado el límite flexible de espíritu navideño de 50.000. Debes gastar algunas fichas en la tienda navideña Spirit antes de poder ganar más.
    - (continue)
  - Enfrías completamente el carbón.
  - (pop-up)
    - (Pop-up: You fully cool down the coal.|colour=#00FF00)
    - (continue)
  - {{Colour Thank you Player!}}
  - **Smokey el carbón:** {{RSChat|Thank you Player!}}

#### Después de que Smokey se haya enfriado

- ¡El carbón ya se ha enfriado!
- (pop-up)
  - (Pop-up: The coal has already cooled down!|warning=yes)

### Failing to pelt Smokey three times before 18 seconds have elapsed

- {{Colour Ah. The fresh snow air is nice and cooling.}}
- **Smokey el carbón:** {{RSChat|Ah. The fresh snow air is nice and cooling.}}
