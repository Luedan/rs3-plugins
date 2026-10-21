# Suspicious Spy

- **Original Wiki Page**: [Transcript:Suspicious Spy](https://runescape.wiki/w/Transcript%3ASuspicious%20Spy)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pickpocket

- (Action: el player comienza a robar el Suspicious Spy.)
- (Condition: Por cada intento exitoso:)
  - Escoges el bolsillo del objetivo.
  - Arrebatas las notas de los espías. Untarlos en chocolate sin posibilidad de reparación.
  - (Condition: Con menos de 30.000 tokens de primavera:)
    - Se ha agregado lo siguiente a su bolsa de divisas: [número] Fichas de primavera.
    - (continue)
  - (Condition: Con al menos 30.000 fichas de primavera:)
    - Ha alcanzado el límite flexible del token Spring de 30 000. Debes gastar algunas fichas en la tienda de Gummy antes de poder ganar más.
    - (ventana emergente)
      - (Ventana emergente: has alcanzado el límite flexible de tokens de primavera de 30 000. Debes gastar algunos tokens en la tienda de Gummy antes de poder ganar más.|advertencia=yes)
      - (continue)
  - (Condition: Si la probabilidad de éxito cae por debajo del 100%:)
    - Su objetivo carterista se da cuenta de su presencia.
- (Condition: Con backpack completo:)
  - No puedes seguir robando carteras porque tienes un inventario completo.
- (Condition: Ser atrapado:)
  - **Suspicious Spy:** {{RSChat|What do you think you're doing?}}
  - (Action: El Suspicious Spy golpea el player.)
  - No logras robarle al objetivo.
  - Has quedado atónito.
