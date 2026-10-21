# Ezreal

- **Original Wiki Page**: [Transcript:Ezreal](https://runescape.wiki/w/Transcript%3AEzreal)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Ezreal:** ¡Todo pertenece a un museo! ¡También sucede que contribuir a las colecciones de Velucia es una buena manera de ganar cronotas, que puedes gastar en mi tienda! ¿Quieres echar un vistazo?
- **Ezreal:** ¡Tenemos una variedad de consumibles y desbloqueos para ayudarte en tu progreso arqueológico, sin importar el nivel de calificación que hayas alcanzado!
- (opens=Archaeology Guild Shop)

### With the energised meteorite shard in inventory

- **Ezreal:** Oh, veo que tienes un fragmento de meteorito energizado. ¿Tiene usted remordimiento del comprador? Si es así, puedo ofrecer un reembolso por eso.
- [Menu]: ¿Devolver un fragmento de meteorito energizado para obtener un reembolso completo?
  - [Choice]: Sí, reembolsame.
    - (removes=energised meteorite shard) (receives=250,000 chronotes)
  - [Choice]: No, me lo quedaré.
    - **Player:** No, gracias. Lo conservaré.
    - (continuea|Standard dialogue)
