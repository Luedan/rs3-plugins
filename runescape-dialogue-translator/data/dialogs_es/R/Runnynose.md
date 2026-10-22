# Runnynose

- **Original Wiki Page**: [Transcript:Runnynose](https://runescape.wiki/w/Transcript%3ARunnynose)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Runnynose:** Hola, tú. ¿Tienes alguna perla?
- **Runnynose:** Me gustan los brillantes. *olfatea*
- **Player:** ¿Qué cambias por ellos?
- **Runnynose:** Nada. Sólo me das.
- **Runnynose:** *sniff* No puedo dejar Globin porque hay tótems. Aterrador.
- **Runnynose:** *sniff* No puedo recolectar mis propias perlas.
- (Condition: Without any telepearls:)
  - **Player:** Lo siento, no lo hago.
  - **Runnynose:** ¡Ay! Runnynose triste.
- (Condition: With at least one telepearl:)
  - **Player:** Tengo una teleperla.
  - **Runnynose:** ¡Oh, puede escapar! ¿Puedo tener?
  - [Menu]: ¿Dar teleperla a Runnynose?
    - [Choice]: Sí.
      - **Player:** Aquí tienes.
      - (Condition: First time:)
        - (removes=1 x Bogolin telepearl) (receives=Divine Ichor V)
        - **Runnynose:** ¡Gracias! Puedes tener esto. De todos modos no es brillante.
      - (Condition: Afterwards:)
        - **Runnynose:** ¡Gracias! ¡Brillante! No puedo escapar de todos modos, solo recoge.
    - [Choice]: No.
      - **Runnynose:** ¡Ay! Runnynose triste.
