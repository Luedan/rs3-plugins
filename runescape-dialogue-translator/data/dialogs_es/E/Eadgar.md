# Eadgar

- **Original Wiki Page**: [Transcript:Eadgar](https://runescape.wiki/w/Transcript%3AEadgar)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Player:**¡Hola!
- {{Trandom}}
  - **Eadgar:**¡Bienvenido a Mad Eadgar! ¡No servimos a trolls!
  - **Eadgar:**¡Bienvenido a Mad Eadgar! ¡Nunca querrás irte!
  - **Eadgar:**¡Bienvenido a Mad Eadgar! ¡Felicidad en un cuenco!
  - **Eadgar:**¡Bienvenido a Mad Eadgar! ¡Sirviendo todo el día, todos los días!
- **Eadgar:** ¿Te importaría probar nuestra deliciosa cocina casera?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Por qué vives tan cerca de los trolls?
    - **Player:** ¿Por qué vives tan cerca de los trolls? ¿No es peligroso?
    - **Eadgar:** Bueno, supongo que los trolls me siguen capturando y encarcelando... Pero al final siempre me liberan, soy demasiado viejo y flaco para sus gustos.
    - **Eadgar:** En cualquier caso, esta es mi casa y no voy a salir de ella. ¡Y esta zona tiene las cabras más sabrosas!
  - [Choice]: ¿Qué tienes para ofrecer?
    - **Player:** ¿Qué tienes para ofrecer?
    - **Eadgar:** La recomendación de The chef para hoy es el guiso de cabrito. Daré un guiso a cambio de logs para mi fuego. Es difícil conseguirlos por aquí.
    - (Condition: If the player has no logs in the backpack)
      - **Player:** Gracias, puede que vuelva con algo de logs.
    - (Condition: If the player has some logs in the backpack)
      - [Menu]: Selecciona una opción
        - [Choice]: Quisiera un guiso de cabra montesa, por favor.
          - **Player:** Me gustaría un guiso de cabra montesa, por favor.
          - (removes=logs or willow logs)
          - Comes el guiso de cabra montesa de Eadgar.
        - [Choice]: No, gracias Eadgar.
          - (continue|no-thanks)
    - [Choice]: No, gracias Eadgar.
      - **Player:** No, gracias, Eadgar.
      - **Eadgar:** ¡Tú te lo pierdes!
