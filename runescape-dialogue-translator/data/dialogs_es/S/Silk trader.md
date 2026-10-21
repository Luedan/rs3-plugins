# Silk trader

- **Original Wiki Page**: [Transcript:Silk trader](https://runescape.wiki/w/Transcript%3ASilk%20trader)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Al Kharid

- **Silk trader:** ¿Quieres comprar sedas finas?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Cuanto son?
    - **Player:** ¿Cuánto cuestan?
    - **Silk trader:** 3mo.
    - [Menu]: Selecciona una opción
      - [Choice]: No, eso es demasiado para mí.
        - **Player:** No, eso es demasiado para mí.
        - **Silk trader:** 2gp y eso es lo más bajo que puedo llegar. No lo vendo por menos. Sólo irás a venderlo en Varrock para obtener ganancias.
        - [Menu]: Selecciona una opción
          - [Choice]: 2gp suena bien.
            - **Player:** 2gp suena bien.
            - (Condition: Si el player tiene suficiente dinero:)
              - Compras algo de seda por 2 po.
              - (receives=silk) (removes=2 coins)
            - (Condition: Si el player no tiene suficiente dinero:)
              - **Player:** Dios mío. No tengo suficiente dinero.
              - **Silk trader:** Bueno, vuelve cuando tengas algo de dinero.
              - No puedes permitirte eso.
          - [Choice]: No, de verdad, no lo quiero.
            - **Player:** No, de verdad, no lo quiero.
            - **Silk trader:** Está bien, pero ese es el mejor precio que obtendrás.
      - [Choice]: Vale, eso suena bien.
        - **Player:** Vale, eso suena bien.
        - (Condition: Si el player tiene suficiente dinero:)
          - Compras algo de seda por 3 po.
          - (receives=silk) (removes=3 coins)
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Player:** Dios mío. No tengo suficiente dinero.
          - **Silk trader:** Bueno, vuelve cuando tengas algo de dinero.
          - No puedes permitirte eso.
  - [Choice]: No, la seda no me queda bien.
    - **Player:** No, la seda no me sienta bien.
