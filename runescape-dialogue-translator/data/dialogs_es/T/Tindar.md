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
  - (Condition: Sin al menos 10 coins:)
    - **Player:** Pero no tengo suficiente dinero encima.
  - (Condition: Sin al menos un espacio backpack libre:)
    - **Tindar:** Parece que tienes las manos ocupadas. Tendrás que liberar algo de espacio en el inventario antes de que te venda algo.
  - (Condition: Con al menos un espacio backpack libre:)
    - (removes=10 coins)
    - (receives=coated frogs' legs)
    - **Tindar:** Ahí lo tienes.
- [Choice]: No gracias.
  - **Player:** No, gracias.

### Overhead dialogue

- {{trandom}}
  - (Condition: Diálogo 1:)
    - **Tindar:** {{RSChat|Crispy!}}
  - (Condition: Diálogo 2:)
    - **Tindar:** {{RSChat|Creeeespy frogs' legs!}}
  - (Condition: Diálogo 3:)
    - **Tindar:** {{RSChat|Get your crispy frogs' legs!}}
  - (Condition: Diálogo 4:)
    - **Tindar:** {{RSChat|Frogs' legs!}}
  - (Condition: Diálogo 5:)
    - **Tindar:** {{RSChat|Crispy frogs' legs!}}
