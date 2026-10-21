# Barman

- **Original Wiki Page**: [Transcript:Barman](https://runescape.wiki/w/Transcript%3ABarman)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- (Condition: Si el player tiene más de 2000 coins en su backpack o bolsa de dinero:)
  - **Barman:** ¿Y qué será para ti, bien [sir/madam]?
  - (continue)
- (Condition: Si el player tiene 2000 coins o menos en su backpack o bolsa de dinero:)
  - **Barman:** ¿Sí? ¿Puedo ayudarte con algo?
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: Una cerveza por favor.
    - **Player:** Una cerveza por favor.
    - **Barman:** Será 1 moneda de oro, por favor.
    - [Menu]: Selecciona una opción
      - [Choice]: Paga.
        - (Condition: Sin al menos un espacio backpack libre:)
          - **Barman:** No tienes espacio para tomar una cerveza.
        - (Condition: Con al menos un espacio backpack libre:)
          - (Condition: Si el player no tiene al menos 1 moneda:)
            - **Player:** Lo siento, parece que me he quedado sin dinero.
          - (Condition: Si el player tiene al menos 1 moneda:)
            - (removes=1 coin)
            - (receives=a beer)
            - **Barman:** Aquí tienes. Una deliciosa pinta de cerveza.
      - [Choice]: No pagues.
        - **Player:** Lo siento, cambié de opinión.
  - [Choice]: Una corpulenta enana, por favor.
    - **Player:** Una corpulenta enana, por favor.
    - **Barman:** ¡Será tuyo por solo 2 gold coins!
    - [Menu]: Selecciona una opción
      - [Choice]: Paga.
        - (Condition: Sin al menos un espacio backpack libre:)
          - **Barman:** No tienes espacio para tomar una cerveza.
        - (Condition: Con al menos un espacio backpack libre:)
          - (Condition: Si el player no tiene al menos 2 coins:)
            - **Player:** Lo siento, parece que me he quedado sin dinero.
          - (Condition: Si el player tiene al menos 2 coins:)
            - (removes=2 coins)
            - (receives=a dwarven stout)
            - **Barman:** ¡Una cerveza negra enana, la mejor de todo Keldagrim!
      - [Choice]: No pagues.
        - **Player:** Lo siento, cambié de opinión.
  - [Choice]: Un buen vino por favor.
    - **Player:** Un buen vino, por favor.
    - **Barman:** ¡Ah, [sir/madam] tiene gusto! Una jarra de vino te costará 10 gold coins.
    - [Menu]: Selecciona una opción
      - [Choice]: Paga.
        - (Condition: Sin al menos un espacio backpack libre:)
          - **Barman:** No tienes espacio para llevar una jarra de vino.
        - (Condition: Con al menos un espacio backpack libre:)
          - (Condition: Si el player no tiene al menos 10 coins:)
            - **Player:** Lo siento, parece que me he quedado sin dinero.
          - (Condition: Si el player tiene al menos 10 coins:)
            - (receives=a jug of wine for 10 coins)
            - **Barman:** ¡Espero que [sir/madam] lo disfrute!
      - [Choice]: No pagues.
        - **Player:** Lo siento, cambié de opinión.
  - [Choice]: Nada, gracias.
    - **Player:** Nada, gracias.
