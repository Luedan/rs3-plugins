# Turgok

- **Original Wiki Page**: [Transcript:Turgok](https://runescape.wiki/w/Transcript%3ATurgok)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Turgok:** ¡Sopa de baba de cueva! ¿Quieres comprar sopa? Sólo 10 coins el bol.
- [Menu]: Selecciona una opción
  - [Choice]: Sí, por favor.
    - **Player:** Sí, por favor
  - (Condition: Without at least 10 coins:)
    - **Player:** Pero no tengo suficiente dinero encima.
  - (Condition: Without at least one free backpack space:)
    - **Turgok:** Parece que tienes las manos ocupadas. Tendrás que liberar algo de espacio en el inventario antes de que te venda algo.
  - (Condition: With at least one free backpack space:)
    - (removes=10 coins)
    - (receives=green gloop soup)
    - **Turgok:** Ahí lo tienes.
  - [Choice]: No, gracias.
    - **Player:** No, gracias.

### Overhead dialogue

- {{trandom}}
  - (Condition: Dialogue 1:)
    - **Turgok:** {{RSChat|Tasty soup!}}
  - (Condition: Dialogue 2:)
    - **Turgok:** {{RSChat|Green cave-slime soup!}}
  - (Condition: Dialogue 3:)
    - **Turgok:** {{RSChat|Soup!}}
  - (Condition: Dialogue 4:)
    - **Turgok:** {{RSChat|Hot, tasty soup!}}
  - (Condition: Dialogue 5:)
    - **Turgok:** {{RSChat|Cave slime soup!}}
