# Vyrelord consumer

- **Original Wiki Page**: [Transcript:Vyrelord consumer](https://runescape.wiki/w/Transcript%3AVyrelord%20consumer)
- **Letter**: `V`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pickpocket


#### Con menos de 118 Thieving

- Debes ser un ladrón de nivel 118 para robarle el bolsillo a este Vyrelord consumer.
- ((Se muestra en una ventana emergente:))
  - (Ventana emergente: necesita el nivel 118 de Thieving.|advertencia=yes)

#### Con al menos 118 Thieving


##### Sin éxito


##### Con backpack completo

- No tienes suficiente espacio en tu inventario para hacer eso.
- No puedes seguir robando carteras porque tienes un inventario completo.

##### Que te atrapen

- No logra robarle el bolsillo al consumidor de Vyralady.
- **Vyrelord consumer:** {{RSChat|How uncouth!}}
- (Action: El vyrelord consumer golpea el player.)
- Has quedado atónito.

##### con éxito

- ((Lo siguiente se repite hasta que es interrumpido, fuera del espacio backpack o atrapado:))
  - Escoges el bolsillo del Vyrelord consumer.
  - (Condition: Si recibe coins:)
    - Se han añadido 900 coins a tu bolsa de dinero.
  - (Condition: Si recibe otros artículos:)
    - (receives=loot)
    - (Condition: Si alcanza el backpack completo:)
      - No puedes seguir robando carteras porque tienes un inventario completo.
