# Lucy (Party Room)

- **Original Wiki Page**: [Transcript:Lucy (Party Room)](https://runescape.wiki/w/Transcript%3ALucy%20%28Party%20Room%29)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to

- **Lucía:** ¡Hola! Soy lucía. ¡Bienvenidos al Salón de Fiestas!
- **Player:** Hola.
- **Lucy:** ¿Te gustaría comprar una cerveza?
- **Player:** ¿Cuánto cuestan?
- **Lucy:** Sólo 2 piezas de oro.
- [Menu]: Selecciona una opción
  - [Choice]: ¡Sí, por favor!
    - **Player:** ¡Sí, por favor!
    - **Lucy:** ¡Ya viene [sir/ma'am]!
    - (Condition: Si el player no tiene al menos dos coins:)
      - No puedes permitirte eso.
      - ((Repetido en una ventana emergente:))
        - No puedes permitirte eso.
        - (continue)
      - **Lucy:** ¡Dije 2 coins! ¡No tienes 2 coins!
      - **Player:** Lo siento, volveré otro día.
    - (Condition: Si el player tiene al menos dos coins:)
      - Se han eliminado 2 coins de tu bolsa de dinero.
      - (receives=a beer)
      - **Player:** Gracias, Lucy.
  - [Choice]: No gracias, no puedo permitirme eso.
    - **Player:** No, gracias, no puedo permitirme eso.
    - **Lucía:** Ya veo. Bueno, ven a verme si cambias de opinión. ¡Sabes dónde estoy!
