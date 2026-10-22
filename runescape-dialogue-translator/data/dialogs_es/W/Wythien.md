# Wythien

- **Original Wiki Page**: [Transcript:Wythien](https://runescape.wiki/w/Transcript%3AWythien)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Wythien:** Hola, tú. ¿Quedan fragmentos de las fauces de Motherlode y quieres algunos elementos que tomé de las fauces de Motherlode antes de que se cerrara? Diez fragmentos de Motherlode para un artículo: no puedo decir nada más justo que eso.
- [Menu]: Selecciona una opción
  - [Choice]: Estoy interesado.
    - (Condition: With at least 10 motherlode shards:)
      - **Wythien:** Bien, bien. ¿Estás seguro de que quieres intercambiar diez fragmentos? No soy un tipo de persona que reembolsa dinero.
      - (continue)
    - (Condition: With less than 10 motherlode shards:)
      - **Wythien:** Necesitarás diez fragmentos de motherlode para un único artículo. Te faltan un poco para cumplir diez años.
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: Sí. {{anchor|accept}}
        - (Condition: With less than 10 motherlode shards:)
          - **Wythien:** Vuelve conmigo cuando tengas más fragmentos de motherlode. Diez bastarán.
        - (Condition: With at least 10 motherlode shards:)
          - (Condition: Before having exchanged motherlode shards on a given day:)
            - (removes=10 crystal motherlode shards) (receives=Motherlode Maw loot)
            - [pic=Crystal motherlode shard detail.png] <!-- pic2 = received reward -->
          - (Condition: After having exchanged motherlode shards on a given day:)
            - [Ya intercambiaste fragmentos de motherlode hoy.]
      - [Choice]: No... Adiós.
        - (end)
      - [Choice]: Me gustaría preguntar algo más.
        - (initial|initial-options)
  - [Choice]: ¿Quién eres exactamente?
    - **Wythien:** ¿Yo? Un emprendedor que no tiene miedo de correr algún que otro riesgo.
    - (initial|initial-options)
  - [Choice]: ¿Qué más tienes?
    - [Menu]: Selecciona una opción
      - [Choice]: Potenciadores.
        - ((Enhancer's Exchange interface opens.))
      - [Choice]: Tienda Dungeoneering.
        - (opens=Daemonheim Rewards)
      - [Choice]: Pregunta por otra cosa.
        - (initial|initial-options)
  - [Choice]: Esto suena sospechoso. Adiós
    - (end)

### Exchange motherlode shards

- (above|accept)

### Enhancers

- [Menu]: Selecciona una opción
  - [Choice]: Potenciadores del enfoque.
    - ((Enhancers Exchange interface opens.))
  - [Choice]: Cambie los potenciadores por fragmentos de motherlod.
    - ((Maw Enhancers interface opens with 'Exchange' buttons next to all enhancers types.))
  - [Choice]: Alternar efectos potenciadores.
    - ((La interfaz de Maw Enhancers se abre con casillas de verificación junto a los tipos de potenciadores.)) <!-- and 'Activate' buttons next to the final three -->
  - [Choice]: Nada.
    - (end)

### Dungeoneering shop

- (opens=Daemonheim Rewards)
