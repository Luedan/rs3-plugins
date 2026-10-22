# Gardener

- **Original Wiki Page**: [Transcript:Gardener](https://runescape.wiki/w/Transcript%3AGardener)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Falador Park


#### Hablando con él

- **Player:** Hola.
- **Gardener:** Estoy ocupado. A menos que tengas algunas semillas de lirio, puedes ir a buscar a Wyson si necesitas algo.
- [Menu]: Selecciona una opción
  - [Choice]: Pregunta sobre el intercambio de semillas de Lily
    - **Gardener:** Necesito cincuenta semillas de lirio blanco al día. A cambio, estoy dispuesto a enseñarte algunos de los trucos agrícolas que he aprendido a lo largo de los años.
    - [Menu]: Selecciona una opción
      - [Choice]: Intercambiar semillas
        - (Condition: If the player has no white lily seeds:)
          - **Gardener:** Parece que no llevas ninguna semilla contigo.
        - (Condition: If the player has traded in fifty white lily seeds for the day:)
          - **Gardener:** Me temo que no tengo nada más que pueda enseñarte hoy. ¿Podrías volver mañana?
          - Sólo puedes intercambiar 50 semillas al día.
        - (Condition: If the player has white lily seeds in backpack:)
          - **Gardener:** ¿Cuántas semillas estás dispuesto a ofrecer?
          - {{tinput|Enter amount:}}
            - ((After entering a positive amount:))
              - Obtendrás [amount] Farming xp a cambio de semillas [número].
              - (removes=white lily seeds) (receives=100 Farming XP for each white lily seed)
            - (Condition: If zero is entered:)
              - **Gardener:** Vuelve si cambias de opinión.
      - [Choice]: salir
        - (end)
  - [Choice]: Preguntar por planta extraña
    - **Player:** ¿No te has dado cuenta de que hay una fisura enorme en el parque?
    - **Gardener:** Oh, sí. Supongo que hay algún tipo de problema con los topos. Wyson dijo que lo tenía bajo control, así que no le presté mucha atención.
  - [Choice]: salir
    - (end)

#### Opción de intercambio de semillas

- ¿Cuántas semillas de lirio te gustaría intercambiar?
- {{tinput|Enter amount:}}
  - ((After entering a positive amount:))
    - (Condition: If the player has no white lily seeds:)
      - No tienes tantas semillas de lirio.
    - (Condition: If the player has traded in fifty white lily seeds for the day:)
      - **Gardener:** Me temo que no tengo nada más que pueda enseñarte hoy. ¿Podrías volver mañana?
      - Sólo puedes intercambiar 50 semillas al día.
    - (Condition: If the player has white lily seeds:)
      - Obtendrás [amount] Farming xp a cambio de semillas [número].
      - (removes=white lily seeds) (receives=100 Farming XP for each white lily seed)
  - (Condition: If zero is entered:)
    - **Gardener:** Vuelve si cambias de opinión.
