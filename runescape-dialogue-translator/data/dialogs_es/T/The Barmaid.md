# The Barmaid

- **Original Wiki Page**: [Transcript:The Barmaid](https://runescape.wiki/w/Transcript%3AThe%20Barmaid)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **The Barmaid:** Hola, amor. ¿Está bien?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Cómo van las cosas, Surula?
    - **The Barmaid:** Oh, no me puedo quejar, capitán de puerto. Los aventureros y capitanes que aparecen aquí todos los días me mantienen ocupado. Eso sí, John estuvo aquí anoche. Borracho por supuesto. Gritando algo sobre navegar uno de los barcos hacia el este. Bendito sea. Me alegro que estés aquí. Hace tiempo que necesitábamos que alguien arreglara este lugar. Durante los últimos años hemos sentido como si hubiéramos estado atrapados en telarañas y sombras. Contigo aquí, se siente ligero otra vez.
    - (previous|PreviousOptions)
  - [Choice]: ¿Puedo hacer una pregunta personal?
    - **The Barmaid:** Quieres saber sobre los tentáculos, ¿verdad?
    - **Player:** Er, sí.
    - **The Barmaid:** Oh, no te sonrojes, pulpito. Verá, hay una aflicción en el este, nadie sabe la causa, pero algunos de nosotros nacemos con branquias, tentáculos e incluso aletas. Un hombre pobre tenía aletas; significaba que no podía usar zapatos. Pensarías que con esta apariencia tendríamos algunos poderes especiales, como esa sirena enfurruñada en los muelles, pero estarías equivocado. Puedo nadar mejor que la mayoría, claro, pero eso es todo. Por supuesto, hay mucha gente que desconfía de nosotros. Nos llaman huérfanos del mar, lo cual dice mucho. Y algunos son más que simplemente desconfiados. Los puristas de la región de Scythe nos odian con verdadera pasión. Difunden mentiras sobre nosotros, nos golpean, nos matan cuando tienen la oportunidad, asustan a las madres para que nos ahoguen al nacer. Nadie hace mucho por ellos. Gente cruel, esos puristas. Ah... lo siento, amor. No querrás oírme hablar más.
    - (previous|PreviousOptions)
  - [Choice]: ¿Tienes algún chisme?
    - (Condition: If it's not Thursday or A Barmaid's Tip has already been sent out:)
      - **The Barmaid:** No hay nada circulando en este momento, amor, pero mantendré mis tentáculos en el suelo.
      - Habla con the barmaid el jueves para conocer nuevos chismes.
      - Habla con the barmaid el jueves para conocer nuevos chismes.
    - (Condition: If it's Thursday:)
      - (Condition: Without having received A Barmaid's Tip:)
        - **The Barmaid:** Me enteré de algo especial que a tus equipos les podría resultar atractivo, si te apetece.
        - [Menu]: ¿Reemplazar la tercera misión de la lista con el consejo de the Barmaid?
          - [Choice]: Sí.
            - **The Barmaid:** ¡Oh, esto te va a encantar!
            - (La interfaz de Viajes se abre con la tercera misión enumerada reemplazada por el consejo de A Barmaid).
          - [Choice]: No.
            - (previous|PreviousOptions)
      - ((Having received A Barmaid's Tip but not yet sent it out:))
        - **The Barmaid:** Espero que ese consejo te haya funcionado bien, mi amor.
  - [Choice]: ¿Alguna posibilidad de una cerveza?
    - (Condition: If player has at least 1 coin in their inventory or money pouch:)
      - Se ha retirado una moneda de su bolsa de dinero.
      - **The Barmaid:** Ahí lo tienes, mi pequeño percebe, agradable y espumoso.
      - [Compras una cerveza mal servida a la que le falta la mayor parte de la espuma.]
      - (previous|PreviousOptions)
    - (Condition: If player has no coins)
      - **The Barmaid:** Pobre pulpito. No tienes ni siquiera la moneda para comprar una cerveza. Deben ser tiempos difíciles por aquí.
      - (previous|PreviousOptions)
  - [Choice]: Será mejor que me vaya. Cosas que hacer.
    - **The Barmaid:** Ahora cuídate tú.

### Last Orders random event

- (ver|Puerto propiedad de Player/Eventos aleatorios#Últimos pedidos)

### Reminder

- Se rumorea que Surula the barmaid tiene algunos chismes jugosos para ti.
{{Player-owned port}}
{{DEFAULTSORT|Barmaid, The}}
