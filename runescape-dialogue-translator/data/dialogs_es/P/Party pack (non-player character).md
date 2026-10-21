# Party pack (non-player character)

- **Original Wiki Page**: [Transcript:Party pack (non-player character)](https://runescape.wiki/w/Transcript%3AParty%20pack%20%28non-player%20character%29)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Retrieve item

- ((Se abre la interfaz de Party Pack.))
- (Condition: Al tomar un artículo:)
  - (Condition: Sin espacio backpack para el artículo:)
    - ((Lo siguiente se muestra en una interfaz emergente:))
      - Debes liberar espacio en el inventario para poder tomar este artículo.
        - [Choice]: bien
          - ((La interfaz se cierra.))
  - (Condition: Con espacio backpack para el artículo:)
    - (receives=item)
