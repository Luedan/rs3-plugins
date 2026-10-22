# Battlemaster

- **Original Wiki Page**: [Transcript:Battlemaster](https://runescape.wiki/w/Transcript%3ABattlemaster)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

- **Battlemaster:** Bienvenido al campo de batalla del clan. ¿Qué puedo hacer por ti?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Qué es un campo de batalla de clanes?
    - **Player:** ¿Qué es un campo de batalla de clanes?
    - **Battlemaster:** Además de estas ciudadelas, los clanes tienen un campo de batalla privado donde pueden organizar batallas.
    - **Battlemaster:** Los miembros con rango suficiente pueden cambiar el diseño del campo de batalla, construir muros, colocar picos, agregar monstruos agresivos para luchar y mucho más. Es posible que otros miembros puedan iniciar una batalla, si aún no hay ninguna en progreso. Las batallas no tienen por qué implicar combate; si un clan quiere patear una pelota o perseguir una bandera por el campo de batalla, eso depende de ellos.
    - **Battlemaster:** Los campos de batalla son seguros; No pierdes tus artículos cuando mueres allí.
    - (otro)
  - [Choice]: Quiero unirme a una batalla.
    - **Player:** Quiero unirme a una batalla.
    - **Battlemaster:** Lo estoy buscando ahora...
    - ((Clan Battlefield Setup interface opens.))
      - [Choice]: dejar de fumar
        - [Intentando abandonar el campo de batalla...]
        - Entrando a la ciudadela...
      - [Choice]: Confirmar
        - No eres la persona que inició esta batalla. Si quieres iniciar una batalla, habla con el maestro de batalla de tu ciudadela.
  - [Choice]: Quiero iniciar una nueva batalla.
    - **Player:** Quiero iniciar una nueva batalla.
    - (Condition: If the player has permission to start a battle:)
      - {{tmissing}}
    - (Condition: If the player doesn't have permission to start a battle:)
      - {{tmissing}}
    - (Condition: If the player is in another clan's citadel:)
      - **Battlemaster:** ¡Espera, no estás en este clan! Tendrás que dejar que alguien más comience la batalla.
  - [Choice]: Quiero editar el campo de batalla.
    - **Player:** Quiero editar el campo de batalla.
    - (Condition: If the player has permission to edit the battlefield:)
      - {{tmissing}}
    - (Condition: If the player doesn't have permission to edit the battlefield:)
      - {{tmissing}}
    - (Condition: If the player is in another clan's citadel:)
      - **Battlemaster:** ¡Espera, no estás en este clan! No puedes editar su campo de batalla.
  - [Choice]: No importa.
    - **Player:** No importa.
