# Chimp ice chimp

- **Original Wiki Page**: [Transcript:Chimp ice chimp](https://runescape.wiki/w/Transcript%3AChimp%20ice%20chimp)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Desert Monkey Colony


#### Mientras no uses un amuleto de mono

- **Rug merchant:** ¡Ok, ok! ¡Ah! ¡Ah, ah, ah! ¡Ok, ah, ook!
- No puedes entenderlo.

#### Mientras llevas un amuleto de mono

- **Chimp ice chimp:** ¡Hielo de chimpancé! ¡Consigue tu hielo de chimpancé!
- [Menu]: Selecciona una opción
  - [Choice]: Claro, compraré uno.
    - **Player:** Claro, compraré uno.
    - (Condition: Con un hielo de chimpancé ya en backpack:)
      - **Chimp ice chimp:** Ya tienes un hielo de chimpancé. No seas codicioso.
    - (Condition: Sin hielo de chimpancé en backpack:)
      - **Chimp ice chimp:** Serán 100 coins.
      - (Condition: Sin espacio en backpack:)
        - **Chimp ice chimp:** No tienes espacio para llevar hielo a un chimpancé.
      - (Condition: Sin suficiente dinero:)
        - No puedes permitirte eso.
        - **Chimp ice chimp:** No tienes suficiente.
      - (Condition: Con suficiente dinero, y con espacio en backpack:)
        - (removes=100 coins) (receives=chimp ice)
        - (Condition: Si se trata de una entrega número 5, 10, 15, etc.:)
          - **Chimp ice chimp:** Me lo comería muy rápido. Lo dejé al sol.
  - [Choice]: ¿Cómo va el negocio?
    - **Player:** ¿Cómo va el negocio?
    - **Chimp ice chimp:** En auge, amigo mío. ¡En auge! Comprar los derechos de estas delicias puede ser el mejor movimiento financiero que jamás hayamos hecho. ¿Quieres comprar uno?
    - (otro)
  - [Choice]: Tengo que irme.
    - **Player:** Tengo que irme.

#### Compra la opción hielo de chimpancé, sin amuleto de habla de mono

- (above|While not wearing a monkeyspeak amulet)

#### Compra la opción hielo de chimpancé, con un amuleto de habla de mono

- (above|sure)
