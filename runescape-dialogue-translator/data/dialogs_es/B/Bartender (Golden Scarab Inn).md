# Bartender (Golden Scarab Inn)

- **Original Wiki Page**: [Transcript:Bartender (Golden Scarab Inn)](https://runescape.wiki/w/Transcript%3ABartender%20%28Golden%20Scarab%20Inn%29)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Bartender:** ¡Bienvenido al Golden Scarab Inn! Ven y tómate un descanso antes de emprender tu próxima aventura.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Puedo comprar una cerveza, por favor?
    - **Player:** ¿Puedo comprar una cerveza, por favor?
    - **Bartender:** Claro, serán dos gold coins, por favor.
    - (Condition: If the player has enough money:)
      - (removes=2 coins) (receives=beer)
      - **Player:** Gracias, camarero.
    - (Condition: If the player does not have enough money:)
      - No puedes permitirte eso.
      - **Bartender:** ¡Dije 2 coins! ¡No tienes 2 coins!
      - **Player:** Lo siento, volveré otro día.
  - [Choice]: ¿Vendes algo especial?
    - **Bartender:** Bueno, hay una bebida que vendemos que está un poco "por ahí". Se llama jugo Squeck.
    - **Player:** Oh, ¿me ayudará con mis robos?
    - **Bartender:** Ni mucho menos. ¿Quieres probarlo? Son 10 de oro.
    - [Menu]: ¿Comprar un poco de jugo Squeck?
      - [Choice]: Sí.
        - (Condition: If the player has no space in backpack:)
          - **Player:** No tienes espacio para llevarlo.
        - (Condition: If the player has enough money:)
          - (removes=10 coins) (receives=squeck juice)
          - Compras un poco de jugo Squeck.
        - (Condition: If the player does not have enough money:)
          - No puedes permitirte eso.
      - [Choice]: No.
        - **Player:** No, gracias.
  - [Choice]: ¿Qué hacer en el barrio de los Puertos?
    - **Bartender:** Este es el punto de ruta hacia el resto del mundo: tenemos barcos que pueden llevarte a donde necesites estar, ya sea para llevarte a una nueva aventura o ayudarte a escapar de problemas.
    - **Bartender:** Por supuesto, estarás feliz de esconderte aquí cuando quieras. El Escarabajo Dorado tiene fama de mantenernos la boca cerrada si la guardia imperial viene a hacer preguntas.
    - **Bartender:** Así que no seas tímido, cuéntame tus secretos.
    - (previous)
  - [Choice]: ¡Adiós!
    - **Bartender:** Cuídate, marinero.

#### Comprar opción de cerveza

- (above|squeck)
