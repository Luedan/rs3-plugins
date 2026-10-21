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
    - (Condition: Antes de alimentar con 25 piezas diarias de comida navideña:)
      - (removes=all or as many as is missing from the daily 25 unnoted Christmas food)
      - (Condition: Si se le dio un trozo de comida navideña que no se anotó:)
        - Le das al hungry reindeer un trozo de comida navideña.
        - (ventana emergente)
          - (Ventana emergente: le das al hungry reindeer un trozo de comida navideña).
          - (continue)
      - (Condition: Si se le dieron varios trozos de comida navideña que no se mencionaron:)
        - Le das de comer a los hungry reindeer [número] trozos de comida navideña.
        - (ventana emergente)
          - (Ventana emergente: le das de comer a los hungry reindeer [número] trozos de comida navideña).
          - (continue)
      - (Condition: Llegar a 50.000 espíritu navideño:)
        - Has alcanzado el límite flexible de espíritu navideño de 50.000. Debes gastar algunas fichas en la tienda navideña Spirit antes de poder ganar más.
        - (ventana emergente)
          - (Ventana emergente: has alcanzado el límite mínimo de espíritu navideño de 50 000. Debes gastar algunas fichas en la tienda navideña Spirit antes de poder ganar más.|advertencia=yes)
          - (continue)
      - (Condition: Con menos de 50.000 espíritu navideño antes:)
        - Se ha agregado lo siguiente a su bolsa de divisas: [número] x Espíritu navideño.
        - (continue)
      - (Condition: Si se obtiene Rudi:)
        - (receives=Rudi)
        - Mientras alimentas a los renos, te encuentras con Rudi, la mascota reno de Christmas Village.
        - (ventana emergente)
          - (Ventana emergente: mientras alimentas a los renos, encuentras a Rudi, la mascota reno de Christmas Village.|color=#00FF00)
    - (Condition: Después de alimentar con 25 piezas diarias de comida navideña:)
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
