# Captain Barnaby

- **Original Wiki Page**: [Transcript:Captain Barnaby](https://runescape.wiki/w/Transcript%3ACaptain%20Barnaby)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before My Arm's Big Adventure

- **Captain Barnaby:** ¿Quieres ir de viaje a Brimhaven?
- **Captain Barnaby:** El viaje te costará 30 coins.
- '''Seleccione una opción {{anchor|Select}}
  - [Choice]: Sí por favor.
    - **Player:** Sí, por favor.
    - (Condition: If the player has enough money:)
      - Pagas 30 coins y abordas el barco.
      - El barco llega a Brimhaven.
    - (Condition: If the player does not have enough money:)
      - **Player:** Dios mío, parece que no tengo suficiente dinero.
      - No puedes permitirte eso.
      - ((Repeated in a pop-up:))
        - No puedes permitirte eso.
    - (Condition: If the player has completed the Easy Karamja achievements:)
      - **Captain Barnaby:**Espera un minuto, ¿no te ganaste los guantes Karamja? Pensé que te había visto ayudando en la isla. Puedes ir a mitad de precio.
      - Pagas 15 coins y abordas el barco.
      - El barco llega a Brimhaven.
  - [Choice]: No, gracias.
    - **Player:** No, gracias.
  - [Choice]: *(Con un ring of charos (a) equipado :)* O podría no pagarte nada en absoluto...
    - **Player:** O no podría pagarte nada en absoluto...
    - **Captain Barnaby:** Mmmm, nada de nada, dices...
    - **Captain Barnaby:** Sí, ¿por qué no? Entonces, súbete a bordo.
    - Subes al barco.
    - El barco llega a Brimhaven.

### After My Arm's Big Adventure

- **Captain Barnaby:** ¡Oh, no, eres tú otra vez! ¿Quieres ir a Brimhaven?
- **Captain Barnaby:** El viaje te costará 30 coins.
- (continuea|Select)

### Pay-fare option

- (Condition: If the player has enough money:)
  - Pagas 30 coins y abordas el barco.
  - El barco llega a Brimhaven.
- (Condition: If the player does not have enough money:)
  - No tienes suficiente coins para pagar el viaje.
  - ((Repeated in a pop-up:))
    - No tienes suficiente coins para pagar el viaje.
- (Condition: If the player has completed the Easy Karamja achievements:)
  - La sonrisa del Capitán se amplía cuando reconoce que te has ganado guantes Karamja y te los dejó a mitad de precio: 15 coins.
