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
        - (Condition: Si el player no tiene semillas de lirio blanco:)
          - **Gardener:** Parece que no llevas ninguna semilla contigo.
        - (Condition: Si el player ha intercambiado cincuenta semillas de lirio blanco para el día:)
          - **Gardener:** Me temo que no tengo nada más que pueda enseñarte hoy. ¿Podrías volver mañana?
          - Sólo puedes intercambiar 50 semillas al día.
        - (Condition: Si el player tiene semillas de lirio blanco en backpack:)
          - **Gardener:** ¿Cuántas semillas estás dispuesto a ofrecer?
          - {{tinput|Enter amount:}}
            - ((Después de ingresar una cantidad positiva:))
              - Obtendrás [amount] Farming xp a cambio de semillas [número].
              - (removes=white lily seeds) (receives=100 Farming XP for each white lily seed)
            - (Condition: Si se ingresa cero:)
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
  - ((Después de ingresar una cantidad positiva:))
    - (Condition: Si el player no tiene semillas de lirio blanco:)
      - No tienes tantas semillas de lirio.
    - (Condition: Si el player ha intercambiado cincuenta semillas de lirio blanco para el día:)
      - **Gardener:** Me temo que no tengo nada más que pueda enseñarte hoy. ¿Podrías volver mañana?
      - Sólo puedes intercambiar 50 semillas al día.
    - (Condition: Si el player tiene semillas de lirio blanco:)
      - Obtendrás [amount] Farming xp a cambio de semillas [número].
      - (removes=white lily seeds) (receives=100 Farming XP for each white lily seed)
  - (Condition: Si se ingresa cero:)
    - **Gardener:** Vuelve si cambias de opinión.
