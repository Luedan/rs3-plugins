# Rionasta

- **Original Wiki Page**: [Transcript:Rionasta](https://runescape.wiki/w/Transcript%3ARionasta)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Tai Bwo Wannai, after Jungle Potion

- **Rionasta:** Hola... gracias por ayudar a Trufitus a comunicarse con los dioses Bwana. Hemos podido regresar al pueblo gracias a vuestra ayuda.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué haces aquí?
    - **Player:** ¿Qué haces aquí?
    - **Rionasta:** Bueno, es curioso que preguntes que, en realidad, dirijo el servicio de paquetería local al continente.
    - **Player:** ¿Servicio de paquetería?
    - **Rionasta:** Sí, a veces nos piden que enviemos artículos al continente. Podemos enviar artículos a cuentas bancarias de particulares, por una pequeña tarifa, por supuesto.
    - [Menu]: Seleccione una opción{{anchor|opts-2}}
      - [Choice]: ¿Cuánto cuesta?
        - **Player:** ¿Cuánto cuesta?
        - **Rionasta:** Cuesta 10 barras comerciales por artículo; desafortunadamente, incluso los artículos apilables cuestan lo mismo.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Qué son los palos comerciales y cómo los consigo?
            - **Player:** ¿Qué son los sticks comerciales y cómo los consigo?
            - **Rionasta:** Los bastones comerciales son nuestra moneda local. Quizás puedas ganar algunos bastones comerciales trabajando un poco en la aldea.
            - **Rionasta:** Charla con Murcaily, creo que estaba buscando a alguien que lo ayudara, trabaja cerca del bosquecillo de madera al este de la cabaña de Trufitus.
            - (previous2|opts-2)
          - [Choice]: ¿Puedo enviar un paquete por favor?
            - **Player:** ¿Puedo enviar un paquete, por favor?
            - (Condition: With less than 10 trading sticks in backpack:)
              - **Rionasta:** Cuesta al menos 10 unidades comerciales utilizar este servicio. Lo siento pero no tienes suficiente.
              - [Menu]: Selecciona una opción
                - [Choice]: ¿Qué son los palos comerciales y cómo los consigo?
                  - (arriba)
                - [Choice]: Bien, gracias.
                  - (abajo)
            - (Condition: With at least 10 trading sticks in backpack:)
              - **Rionasta:** Por supuesto... ¿qué artículos te gustaría enviar a tu banco?
              - (opens=Parcel service)
          - [Choice]: Bien, gracias.
            - **Player:** Vale, gracias.
      - [Choice]: ¿Puedo enviar un paquete por favor?
        - (arriba)
      - [Choice]: Bien, gracias.
        - (arriba)
  - [Choice]: ¿Hay algo interesante que hacer aquí?
    - **Player:** ¿Hay algo interesante que hacer por aquí?
    - **Rionasta:** Bueno, creo que hay trabajo por hacer... tal vez Murcaily pueda ayudarte. Por lo general, atiende el bosquecillo de madera al este de la cabaña de Trufitus.
  - [Choice]: cond=With Tai Bwo Wannai Cleanup started|He estado trabajando en el pueblo.
    - (Condition: With unclaimed Tai Bwo Wannai favour:)
      - **Rionasta:** Oye, te he visto trabajando en el pueblo. Has estado haciendo un muy buen trabajo aquí para nosotros. Déjame darte algo por tu molestia.
      - (receives=trading sticks)
    - (Condition: Without unclaimed Tai Bwo Wannai favour:)
      - **Rionasta:** Ya te he dado algunos palitos de intercambio y no tengo ninguno más en este momento. ¿Por qué no vas y hablas con algunos de los otros aldeanos y consigues algunas contribuciones?
  - [Choice]: Bien, gracias.
    - **Player:** Vale, gracias.

#### Ocasionalmente con favor no reclamado

- **Rionasta:** Oye, te he visto trabajando en el pueblo. Has estado haciendo un muy buen trabajo aquí para nosotros. Déjame darte algo por tu molestia.
- (receives=trading sticks)
- Obtienes palos comerciales [número]. El favor restante asciende a [percentage].

#### Con una máscara tribal equipada.

- {{Trandom}}
  - (Diálogo 1 :)
    - **Rionasta:** Ahhhhhhhh - ¡Aléjate de mí, bestia!
    - (continue)
  - (Diálogo 2 :)
    - **Rionasta:** ¡Ahhhhhhhh!
    - (continue)
  - (Diálogo 3 :)
    - **Rionasta:** Ahhhhhhhh - ¡Es un monstruo!
    - (continue)
  - (Diálogo 4 :)
    - **Rionasta:** ¡Waahhhhh! - ¡Es una bestia malvada que viene a comerse mi alma!
    - (continue)
- **Player:** ¿Cuál es el problema? ¡Oh, estoy usando esta gran máscara aterradora! Será mejor que me lo quite antes de empezar a hablar con los nativos.
