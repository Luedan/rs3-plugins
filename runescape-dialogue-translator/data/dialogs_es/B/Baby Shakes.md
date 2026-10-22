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
          - (Condition: If the player has another animal to sell:)
            - (above|sell-one-animal)
          - (Condition: If the player does not have another animal to sell:)
            - (end)
        - [Choice]: No.
          - (Condition: If the player has another animal to sell:)
            - (above|sell-one-animal)
          - (Condition: If the player does not have another animal to sell:)
            - (end)
    - [Choice]: Entregue TODOS los animales retenidos a Baby Shakes.
      - **Baby Shakes:** ¿Estás seguro de que quieres que me lleve todos los animales que tienes? No aceptaré ninguno de tus favoritos.
      - [Menu]: ¿Vender todos los animales por un bajo precio de frijol?
        - [Choice]: si
          - (Condition: If no animals were sold:)
            - No tienes animales para vender. ¡Cero animales, cero frijoles!
            - ((Repeated in a pop-up:))
              - No tienes animales para vender. ¡Cero animales, cero frijoles!
          - (Condition: If one animal was sold:)
            - (end)
          - (Condition: If multiple animals were sold:)
            - Has vendido animales [X] por un total de frijoles [X].
            - ((Repeated in a pop-up:))
              - Has vendido animales [X] por un total de frijoles [X].
        - [Choice]: No
          - (end)
    - [Choice]: [Back away slowly.]
      - (end)

### Using an animal on Baby Shakes

- **Baby Shakes:** {{RSChat|YUM! Me like [animal name].}}

### Using any other item on Baby Shakes

- **Baby Shakes:** Er, no, gracias.
