# Gabooty

- **Original Wiki Page**: [Transcript:Gabooty](https://runescape.wiki/w/Transcript%3AGabooty)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Tai Bwo Wannai, after Jungle Potion

- **Gabooty:** Hola... gracias por ayudar a Trufitus a comunicarse con los dioses Bwana. Hemos podido regresar al pueblo gracias a vuestra ayuda.
- [Menu]: Seleccione una opción {{anchor|init}}
  - [Choice]: ¿Qué haces aquí?
    - **Player:** ¿Qué haces aquí?
    - **Gabooty:** No mucho realmente... Dirijo una tienda local que me permite ganar algunos puntos comerciales, pero eso es todo. Realmente me guardo para mí.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué son los palos comerciales? {{anchor|trading-sticks}}
        - **Player:** ¿Qué son los palos comerciales?
        - **Gabooty:** Son la moneda local Bwana, se usa en Tai Bwo Wannai, generalmente hay algunos trabajos ocasionales que deben realizarse en el pueblo y que puedes hacer para ganar algunos palos comerciales.
        - **Gabooty:** O, si tienes algo que les pueda gustar a los aldeanos locales, puedes vendérmelo y te lo pagaré intercambiando palos.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Qué tipo de cosas les gustan a los aldeanos locales?
            - **Player:** ¿Qué tipo de cosas les gustan a los aldeanos locales?
            - **Gabooty:** ¡Cócteles Gnome! ¡Es increíble pero a todos nos encantan! Afortunadamente, logré conseguir existencias de cócteles hechos con gnomos y se los proporciono a mis clientes favoritos. Sin embargo, a muchos de los clientes les gustan mucho los cócteles.
            - **Gabooty:** realizado por los aventureros que pasan por este camino. Si alguna vez tienes alguno, ¡tráemelo! ¡Te daré una buena oferta, eso seguro!
            - **Player:** ¿Cómo pudieron los aldeanos probar cócteles de gnomos?
            - **Gabooty:** Creo que fue ese piloto gnomo el que estrelló su planeador, ¿tal vez tenía un pequeño mini-bar a bordo? Ahora que lo pienso, uno esperaría que el pequeño reuniera sus cosas y se fuera de aquí, ¿no? ¡Debe amar la jungla para haberse quedado aquí tanto tiempo!
            - (initial|init)
          - [Choice]: ¿Tienes una tienda?
            - (below|about-shop)
          - [Choice]: Quiero hacer otra pregunta.
            - (below|another-question)
          - [Choice]: Bien, gracias.
            - **Player:** Vale, gracias.
      - [Choice]: ¿Tienes una tienda? {{anchor|about-shop}}
        - **Player:** ¿Tienes una tienda?
        - **Gabooty:** Sí, es la cooperativa Tai Bwo... ¡nombre pegadizo, eh! Vendemos algunas baratijas y herramientas del pueblo local. Además, hay algunos artículos que estamos buscando almacenar por el bien de los lugareños.
        - **Gabooty:** Si te encuentras con alguno de ellos, tráemelo, pagaré un buen precio por él. Estoy seguro de que encontrará los precios muy razonables.
        - [Menu]: Seleccione una opción{{anchor|options-2}}
          - [Choice]: ¿Qué son los palos comerciales?
            - (above|trading-sticks)
          - [Choice]: ¿Tienes una tienda?
            - (above|about-shop)
          - [Choice]: ¿Puedo echar un vistazo a lo que tienes para vender?
            - **Player:** ¿Puedo echar un vistazo a lo que tienes para vender?
            - **Gabooty:** Claro que puedes... ¿qué tienda te gustaría ver? ¿La Cooperativa o la tienda de Bebidas?
            - [Menu]: Selecciona una opción
              - [Choice]: La Cooperativa
                - (opens=Gabooty's Tai Bwo Wannai Cooperative)
              - [Choice]: La tienda de bebidas
                - (opens=Gabooty's Tai Bwo Wannai Drinky Store)
              - [Choice]: Ninguno gracias...
                - **Player:** Ninguno, gracias...
          - [Choice]: ¿Por qué sólo tomas un tipo de cóctel Gnome?
            - **Player:** ¿Por qué solo tomas un tipo de cóctel Gnome?
            - **Gabooty:** Es curioso, en realidad. He logrado conseguir un buen trato con el piloto de ese planeador gnomo. Él puede suministrarme directamente ahora. Sin embargo, es realmente interesante que a los aldeanos locales les gusten mucho los cócteles de gnomos preparados por los aventureros que pasan por este camino.
            - **Player:** ¿Por qué? ¿Cuál es la diferencia?
            - **Gabooty:** Creo que puede ser simplemente que estén hechos más frescos, o que haya un ligero cambio en el sabor de la bebida, ya sabes, un poco más de esto, un poco menos de aquello, ¡todo suma y crea una bebida interesante!
            - (previous2|options-2)
          - [Choice]: Quiero hacer otra pregunta.
            - (below|another-question)
      - [Choice]: Quiero hacer otra pregunta.
        - **Player:** Quiero hacer otra pregunta.
        - **Gabooty:** Claro, ¿qué quieres preguntar?
        - (initial|init)
      - [Choice]: Bien, gracias.
        - **Player:** Vale, gracias.
  - [Choice]: ¿Hay algo interesante que hacer aquí?
    - **Player:** ¿Hay algo interesante que hacer aquí?
    - {{Trandom}}
      - (Diálogo 1 :)
        - **Gabooty:** Bwana, si alguien más me hace esa pregunta hoy, ¡explotaré! ¡Ve y pregúntale a Murcaily!
      - (Diálogo 2 :)
        - **Gabooty:** Solo estoy disfrutando del sol, Bwana. Intente preguntarle a Murcaily.
      - (Diálogo 3 :)
        - **Gabooty:** Bueno, creo que hay trabajo por hacer... tal vez Murcaily pueda ayudarte. Por lo general, atiende el bosquecillo de madera al este de la cabaña de Trufitus.
      - (Diálogo 4 :)
        - **Gabooty:** Lo siento Bwana, ya estoy ocupado, ¿por qué no vas y hablas con Murcaily? Está en alguna parte del pueblo.
  - [Choice]: cond=With Tai Bwo Wannai Cleanup started|He estado trabajando en el pueblo.
    - (Condition: With unclaimed Tai Bwo Wannai favour:)
      - **Gabooty:** Oye, te he visto trabajando en el pueblo. Has estado haciendo un muy buen trabajo aquí para nosotros. Déjame darte algo por tu molestia.
      - (receives=trading sticks)
    - (Condition: Without unclaimed Tai Bwo Wannai favour:)
      - **Gabooty:** Ya te he dado algunos palitos de intercambio y no tengo ninguno más en este momento. ¿Por qué no vas y hablas con algunos de los otros aldeanos y consigues algunas contribuciones?
  - [Choice]: Bien, gracias.
    - **Player:** Vale, gracias.

#### Ocasionalmente con favor no reclamado

- **Gabooty:** Oye, te he visto trabajando en el pueblo. Has estado haciendo un muy buen trabajo aquí para nosotros. Déjame darte algo por tu molestia.
- (receives=trading sticks)
- Obtienes palos comerciales [número]. El favor restante asciende a [percentage].

#### Con una máscara tribal equipada.

- {{Trandom}}
  - (Diálogo 1 :)
    - **Gabooty:** Ahhhhhhhh - ¡Aléjate de mí, bestia!
    - (continue)
  - (Diálogo 2 :)
    - **Gabooty:** ¡Ahhhhhhhh!
    - (continue)
  - (Diálogo 3 :)
    - **Gabooty:** Ahhhhhhhh - ¡Es un monstruo!
    - (continue)
  - (Diálogo 4 :)
    - **Gabooty:** ¡Waahhhhh! - ¡Es una bestia malvada que viene a comerse mi alma!
    - (continue)
- **Player:** ¿Cuál es el problema? ¡Oh, estoy usando esta gran máscara aterradora! Será mejor que me lo quite antes de empezar a hablar con los nativos.

#### Senderos del tesoro

- (Condition: Only the first time:)
  - **Gabooty:** Hola. Si puedes resolverme una pregunta, puedes seguir adelante.
  - **Player:** ¿Cuál es la pregunta?
  - **Gabooty:** Toma, te lo anoté.
- (receives=challenge scroll (medium))
- [¡Gabooty te ha dado un pergamino de desafío!]

##### Cuando hablé de nuevo

- **Gabooty:** Ingrese la respuesta a la pregunta.
- Ingrese la cantidad:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Gabooty:** ¡Respuesta incorrecta!
- (Condition: When given the correct answer:)
  - (removes=the old clue scroll (medium) y desplazamiento de desafío (medio))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [¡Gabooty te ha dado otro pergamino de pistas!]
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
  - **Gabooty:** ¡Suena bien!
