# Vyrelord consumer

- **Original Wiki Page**: [Transcript:Vyrelord consumer](https://runescape.wiki/w/Transcript%3AVyrelord%20consumer)
- **Letter**: `V`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pickpocket


#### Con menos de 118 Thieving

- Debes ser un ladrón de nivel 118 para robarle el bolsillo a este Vyrelord consumer.
- ((Shown in a pop-up:))
  - (Pop-up: You need Thieving level 118.|warning=yes)

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

- ((The following repeats until interrupted, out of backpack space, or caught:))
  - Escoges el bolsillo del Vyrelord consumer.
  - (Condition: If receiving coins:)
    - Se han añadido 900 coins a tu bolsa de dinero.
  - (Condition: If receiving other items:)
    - (receives=loot)
    - (Condition: If reaching full backpack:)
      - No puedes seguir robando carteras porque tienes un inventario completo.
