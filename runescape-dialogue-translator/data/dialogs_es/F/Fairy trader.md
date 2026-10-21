# Fairy trader

- **Original Wiki Page**: [Transcript:Fairy trader](https://runescape.wiki/w/Transcript%3AFairy%20trader)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pickpocket


#### Con menos de 113 Thieving

- Debes ser un ladrón de nivel 113 para robarle a este objetivo.
- (ventana emergente)
  - {{Popup|You need Thieving level 113.|warning=yes}}

#### Con al menos 113 Thieving


##### Sin éxito


##### Con backpack completo

- No puedes seguir robando carteras porque tienes un inventario completo.

##### Que te atrapen

- **Fairy trader:** {{RSChat|What do you think you're doing?}}
- (Action: El hada transforma el player en un objeto aleatorio.)

##### con éxito

- ((Lo siguiente se repite hasta que es interrumpido, fuera del espacio backpack o atrapado:))
  - Escoges el bolsillo del objetivo.
  - (Condition: Si recibe coins:)
    - [número] coins se han agregado a su bolsa de dinero.
  - (Condition: Si recibe otros artículos:)
    - (receives=loot)
    - (Condition: Si alcanza el backpack completo:)
      - No puedes seguir robando carteras porque tienes un inventario completo.
