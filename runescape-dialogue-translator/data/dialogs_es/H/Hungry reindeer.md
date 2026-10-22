# Hungry reindeer

- **Original Wiki Page**: [Transcript:Hungry reindeer](https://runescape.wiki/w/Transcript%3AHungry%20reindeer)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Feed


#### Durante un evento navideño


##### Sin comida navideña o solo con comida navideña indicada

- **Player:** No parecen interesados en comer nada de lo que tengo conmigo. ¿Qué preferiría comer un reno amante de la Navidad?

##### Con comida navideña desapercibida

- [Menu]: ¿Alimentar a los renos con la comida navideña que llevas?
  - [Choice]: si
    - (Condition: Before feeding 25 daily pieces of Christmas food:)
      - (removes=all or as many as is missing from the daily 25 unnoted Christmas food)
      - (Condition: If one piece of unnoted Christmas food was fed:)
        - Le das al hungry reindeer un trozo de comida navideña.
        - (pop-up)
          - (Pop-up: You feed the hungry reindeer a piece of Christmas food.)
          - (continue)
      - (Condition: If multiple pieces of unnoted Christmas food were fed:)
        - Le das de comer a los hungry reindeer [número] trozos de comida navideña.
        - (pop-up)
          - (Pop-up: You feed the hungry reindeer [number] pieces of Christmas food.)
          - (continue)
      - (Condition: Reaching 50,000 Christmas spirit:)
        - Has alcanzado el límite flexible de espíritu navideño de 50.000. Debes gastar algunas fichas en la tienda navideña Spirit antes de poder ganar más.
        - (pop-up)
          - (Pop-up: You have reached the Christmas spirit soft cap of 50,000. You need to spend some tokens in the Christmas Spirit Shop before you can earn more.|warning=yes)
          - (continue)
      - (Condition: With under 50,000 Christmas spirit before:)
        - Se ha agregado lo siguiente a su bolsa de divisas: [número] x Espíritu navideño.
        - (continue)
      - (Condition: If Rudi is obtained:)
        - (receives=Rudi)
        - Mientras alimentas a los renos, te encuentras con Rudi, la mascota reno de Christmas Village.
        - (pop-up)
          - (Pop-up: Whilst feeding the reindeer you find Rudi, the Christmas Village reindeer pet.|colour=#00FF00)
    - (Condition: After feeding 25 daily pieces of Christmas food:)
      - **Player:** Parece que ha comido todo lo que pudo por hoy.
      - En su lugar, se puede añadir comida navideña adicional al comedero cercano.
  - [Choice]: No
    - (end)

#### Fuera de un evento navideño

- [Las fiestas navideñas ya han terminado.]

### Check

- [Horas alimentadas hoy: [número]/25<br>Total de horas alimentadas: [número]]

### Using items


#### Durante un evento navideño


##### Artículo incompatible

- **Player:** No parecen interesados en comer eso. ¿Qué preferiría comer un reno amante de la Navidad?

##### Artículo compatible

- (above|feed)

#### Fuera de un evento navideño

- [Las fiestas navideñas ya han terminado.]
