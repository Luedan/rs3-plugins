# Adam Antite

- **Original Wiki Page**: [Transcript:Adam Antite](https://runescape.wiki/w/Transcript%3AAdam%20Antite)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{transcript npc|Adam Antite|noplayer}}

### Send off

- **¿Enviar the trapper por 100 frijoles?**
  - [Choice]: si
    - (Action: Adam Antite desaparece.)
    - Tu trampero parte en busca de animales perdidos.
  - [Choice]: No
    - (end)
  - [Choice]: Si y no me vuelvas a preguntar
    - (Action: arriba|enviado)

### Collect

- (Condition: Without any space in inventory:)
  - **Adam Antite:** Tengo 1 animal para ti, pero tendrás que hacer espacio en tu inventario antes de que pueda dártelo.
- (Condition: With at least one space in inventory:)
  - (receives=a random unchecked animal item)
  - The trapper te entrega un [Animal] nuevo (sin marcar) para que lo guardes en tu granja.
  - **Adam Antite:** Encontré a este pequeño desgraciado deambulando solo y luciendo perdido, espero que lo cuides bien.

### When the trapper returns after being sent off

- Tu trampero ha regresado con un animal para ti.
