# Vyrelady consumer

- **Original Wiki Page**: [Transcript:Vyrelady consumer](https://runescape.wiki/w/Transcript%3AVyrelady%20consumer)
- **Letter**: `V`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pickpocket


#### Con menos de 118 Thieving

- Debes ser un ladrón de nivel 118 para robarle el bolsillo a este Vyrelady consumer.
- ((Shown in a pop-up:))
  - (Pop-up: You need Thieving level 118.|warning=yes)

#### Con al menos 118 Thieving


##### Sin éxito


##### Con backpack completo

- No tienes suficiente espacio en tu inventario para hacer eso.
- No puedes seguir robando carteras porque tienes un inventario completo.

##### Que te atrapen

- No logra robarle el bolsillo al consumidor de Vyralady.
- **Vyrelady consumer:** {{RSChat|How uncouth!}}
- (Action: El vyrelady consumer golpea el player.)
- Has quedado atónito.

##### con éxito

- ((The following repeats until interrupted, out of backpack space, or caught:))
  - Escoges el bolsillo del Vyrelady consumer.
  - (Condition: If receiving coins:)
    - Se han añadido 900 coins a tu bolsa de dinero.
  - (Condition: If receiving other items:)
    - (receives=loot)
    - (Condition: If reaching full backpack:)
      - No puedes seguir robando carteras porque tienes un inventario completo.
