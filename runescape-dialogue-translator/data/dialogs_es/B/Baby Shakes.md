# Baby Shakes

- **Original Wiki Page**: [Transcript:Baby Shakes](https://runescape.wiki/w/Transcript%3ABaby%20Shakes)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before completing the player-owned farm tutorial

- **Baby Shakes:** ¿Puedo tener animales?
- Baby Shakes quitará de tus manos todos y cada uno de los animales marcados a cambio del 10% de su valor base en frijol.
- **Granny Potterington:** Ahora querida, no nos adelantemos. Podrás encargarte de ese pequeño desgraciado una vez que hayamos terminado aquí.

### After completing the player-owned farm tutorial

- **Baby Shakes:** ¿Puedo tener animales?
- Baby Shakes quitará de tus manos todos y cada uno de los animales marcados a cambio del 10% de su valor base en frijol.
  - [Menu]: Elige una opción.
    - [Choice]: Ofrezca animales a Baby Shakes uno a la vez.
      - ¿Le gustaría vender [animal name] por frijoles [X]?
      - [Menu]: ¿Vender [animal name] por frijoles [X]?
        - [Choice]: Sí.
          - Frijoles [Amount] agregados a su bolsa de divisas.
          - (Condition: Si el player tiene otro animal para vender:)
            - (above|sell-one-animal)
          - (Condition: Si el player no tiene otro animal para vender:)
            - (end)
        - [Choice]: No.
          - (Condition: Si el player tiene otro animal para vender:)
            - (above|sell-one-animal)
          - (Condition: Si el player no tiene otro animal para vender:)
            - (end)
    - [Choice]: Entregue TODOS los animales retenidos a Baby Shakes.
      - **Baby Shakes:** ¿Estás seguro de que quieres que me lleve todos los animales que tienes? No aceptaré ninguno de tus favoritos.
      - [Menu]: ¿Vender todos los animales por un bajo precio de frijol?
        - [Choice]: si
          - (Condition: Si no se vendieron animales:)
            - No tienes animales para vender. ¡Cero animales, cero frijoles!
            - ((Repetido en una ventana emergente:))
              - No tienes animales para vender. ¡Cero animales, cero frijoles!
          - (Condition: Si se vendió un animal:)
            - (end)
          - (Condition: Si se vendieron varios animales:)
            - Has vendido animales [X] por un total de frijoles [X].
            - ((Repetido en una ventana emergente:))
              - Has vendido animales [X] por un total de frijoles [X].
        - [Choice]: No
          - (end)
    - [Choice]: [Back away slowly.]
      - (end)

### Using an animal on Baby Shakes

- **Baby Shakes:** {{RSChat|YUM! Me like [animal name].}}

### Using any other item on Baby Shakes

- **Baby Shakes:** Er, no, gracias.
