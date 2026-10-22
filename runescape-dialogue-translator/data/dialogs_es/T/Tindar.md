# Tindar

- **Original Wiki Page**: [Transcript:Tindar](https://runescape.wiki/w/Transcript%3ATindar)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Tindar:** ¡Ancas de rana espeluznantes! ¡Consigue tus espeluznantes ancas de rana! ¿Quieres unas ancas de rana crujientes? Sólo 10 po.
- [Menu]: Selecciona una opción
- [Choice]: Sí por favor.
  - **Player:** ¡Sí, por favor!
  - (Condition: Without at least 10 coins:)
    - **Player:** Pero no tengo suficiente dinero encima.
  - (Condition: Without at least one free backpack space:)
    - **Tindar:** Parece que tienes las manos ocupadas. Tendrás que liberar algo de espacio en el inventario antes de que te venda algo.
  - (Condition: With at least one free backpack space:)
    - (removes=10 coins)
    - (receives=coated frogs' legs)
    - **Tindar:** Ahí lo tienes.
- [Choice]: No gracias.
  - **Player:** No, gracias.

### Overhead dialogue

- {{trandom}}
  - (Condition: Dialogue 1:)
    - **Tindar:** {{RSChat|Crispy!}}
  - (Condition: Dialogue 2:)
    - **Tindar:** {{RSChat|Creeeespy frogs' legs!}}
  - (Condition: Dialogue 3:)
    - **Tindar:** {{RSChat|Get your crispy frogs' legs!}}
  - (Condition: Dialogue 4:)
    - **Tindar:** {{RSChat|Frogs' legs!}}
  - (Condition: Dialogue 5:)
    - **Tindar:** {{RSChat|Crispy frogs' legs!}}
