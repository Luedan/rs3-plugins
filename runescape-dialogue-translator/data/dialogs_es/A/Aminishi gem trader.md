# Aminishi gem trader

- **Original Wiki Page**: [Transcript:Aminishi gem trader](https://runescape.wiki/w/Transcript%3AAminishi%20gem%20trader)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Transcript npc|Aminishi gem trader}}

### Before purchasing the Aminishi miststone


#### Sin especias de puerto

- **Aminishi gem trader:** ¿Quizás estaría dispuesto a realizar un intercambio?
- **Aminishi gem trader:** Estoy buscando Ports Spice y estoy dispuesto a darte algo valioso a cambio.
- **Aminishi gem trader:** Yo quiero 1 y tú tienes 0. ¿Qué te parece?

#### Con al menos un Oporto Spice

- **Aminishi gem trader:** ¿Quizás estaría dispuesto a realizar un intercambio?
- **Aminishi gem trader:** Estoy buscando Ports Spice y estoy dispuesto a darte algo valioso a cambio.
- **Aminishi gem trader:** Quiero 1 y tienes [número]. ¿Qué tal?
- [Menu]: Selecciona una opción
  - [Choice]: si
    - (Condition: Without any space in backpack:)
      - **Aminishi gem trader:** Lo sentimos, ¡no tienes suficiente espacio!
    - (Condition: With space in backpack:)
      - **Aminishi gem trader:** Genial, toma esta piedra de niebla de Aminishi.
      - (receives=Aminishi miststone)
      - **Aminishi gem trader:** ¡Gracias amigo!
  - [Choice]: No
    - **Player:** No, gracias.

### After purchasing the Aminishi miststone

- **Aminishi gem trader:** ¡Gracias amigo!
