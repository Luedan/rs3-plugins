# Makeover Mage

- **Original Wiki Page**: [Transcript:Makeover Mage](https://runescape.wiki/w/Transcript%3AMakeover%20Mage)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Makeover Mage:** ¡Hola! ¡Me conocen como Makeover Mage! He pasado muchos años investigando magias que pueden cambiar tu apariencia física.
- **Makeover Mage:** Yo lo llamo un 'cambio de imagen'.<br>¿Quieres que te realice mis magias?
- [Menu]: Elige una opción:
  - [Choice]: Cuéntame más sobre este 'cambio de imagen'.{{anchor|about-makeover}}
    - **Player:** Cuéntame más sobre este 'cambio de imagen'.
    - **Makeover Mage:** ¡Por supuesto! Básicamente, y esto te lo explicaré para que lo entiendas correctamente.
    - **Makeover Mage:** Utilizo mi técnica mágica secreta para derretir tu cuerpo en un charco de sus elementos.
    - **Makeover Mage:** Cuando he descompuesto todos los componentes de tu cuerpo, lo reconstruyo en la forma en la que estoy pensando.
    - **Makeover Mage:** O, ya sabes, algo vagamente parecido, de todos modos.
    - **Player:** Uh... eso no me parece particularmente seguro.
    - **Makeover Mage:** ¡Es tan seguro como las casas! ¡Si sólo he tenido treinta y seis accidentes graves este mes!
    - **Makeover Mage:** Entonces, ¿qué dices? ¿Te apetece un cambio?
    - [Menu]: Selecciona una opción
      - [Choice]: Claro, hazlo.
        - (below|sure)
      - [Choice]: No, gracias.
        - (below|no-thanks)
  - [Choice]: Claro, hazlo.{{anchor|sure}}
    - **Player:** Claro, hazlo.
    - **Makeover Mage:** Por supuesto, aceptas que si por algún accidente te conviertes en rana no tienes derecho a compensación o reembolso.
    - (opens=Makeover Mage)
    - (Después de cambiar de apariencia:)
    - (Condition: Un conjunto aleatorio de los siguientes diálogos:)
      - (Condition: Conjunto 1:)
        - **Makeover Mage:** Dos brazos, dos piernas, una cabeza; Parece que el hechizo finalmente funcionó bien.
        - (continue|thanks)
      - (Condition: Conjunto 2:)
        - **Makeover Mage:** Hmm, no sentiste ningún crecimiento inesperado en tu cabeza en ese momento, ¿verdad?
        - **Player:** Eh, ¿no?
        - **Makeover Mage:** ¡Bien, bien! Me preocupé por un segundo.
        - (continue|thanks)
      - (Condition: Conjunto 3:)
        - **Makeover Mage:** ¡Uf! Eso fue suerte.
        - **Player:** ¿Qué fue?
        - **Makeover Mage:** ¡Nada! ¡Está todo bien! Pareces vivo de todos modos.
        - (continue|thanks)
      - (Condition: Conjunto 4:)
        - **Makeover Mage:** ¡Guau!
        - **Player:** ¿Qué?
        - **Makeover Mage:** ¡Todavía pareces humano!
        - (continue|thanks)
    - {{anchor|thanks}}**Player:** Eh, gracias, supongo.
    - (Condition: Si el player elige la misma apariencia que tiene actualmente:)
      - **Makeover Mage:** Eso no es diferente de lo que ya tienes. Pero feliz de que hayas encontrado tu look.
  - [Choice]: No, gracias.{{anchor|no-thanks}}
    - **Player:** No, gracias. Estoy feliz tal como soy.
    - **Makeover Mage:** Bueno, siempre estaré encantado de ayudarte si cambias de opinión. ¿Hay algo más en lo que pueda ayudarte?
    - (initial|initial-options)
  - [Choice]: Can you give me some more pharmakos berries?|cond=Durante y después de Land of the Goblins:
    - **Player:** ¿Puedes darme más pharmakos berries?
    - (Condition: Si el player aún no tiene ninguno en su backpack o banco:)
      - **Makeover Mage:** Por supuesto. Sólo necesitas combinarlos con toadflax en un vial y tendrás una poción para transformarte en un duende.
      - **Makeover Mage:** Pero es difícil para mí conseguirlos, así que no desperdicies la poción.
      - **Makeover Mage:** Recuerde, se revertirá si está expuesto a la luz solar directa o si realiza una actividad extenuante como pelear. Ahora, aquí están los berries.
      - (receives=pharmakos berries)
      - [bunch] de extraño rojo berries.}}
    - (Condition: Si el player no tiene espacio en backpack:)
      - **Makeover Mage:** No hasta que liberes algo de espacio en el inventario.
    - (Condition: Si el player ya tiene el berries en su backpack o banco:)
      - **Makeover Mage:** Creo que ya tienes algo, así que sólo necesitas conseguir un poco de lino de sapo y hacer la poción.
  - [Choice]: [More...]
    - [Menu]: Elige una opción:
      - [Choice]: ¡Genial amuleto! ¿Puedo tener uno?
        - **Player:** ¡Genial amuleto! ¿Puedo tener uno?
        - **Makeover Mage:** No hay problema, pero recuerda que el amuleto que te venderé es solo una copia del mío. No contiene poderes mágicos y, como tal, sólo te costará 100 coins.
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Player:** Oh, no tengo suficiente dinero para eso.
        - (Condition: Si el player tiene suficiente dinero:)
          - [Menu]: Selecciona una opción
            - [Choice]: Claro, aquí tienes.
              - **Player:** Claro, aquí tienes.
              - (Condition: Si el player no tiene espacio en backpack:)
                - **Makeover Mage:** Um... parece que no tienes espacio para llevarte el amuleto. Quizás deberías comprarlo en otro momento.
                - **Player:** Oh, sí, eso es cierto.
              - (Condition: Si el player tiene espacio en backpack:)
                - (removes=100 coins) (receives=yin yang amulet)
                - [Recibes un amuleto a cambio de 100 coins.]
            - [Choice]: ¡De ninguna manera! Eso es demasiado caro.
              - **Player:** ¡De ninguna manera! Eso es demasiado caro.
              - **Makeover Mage:** Eso es justo, mis joyas no son del gusto de todos.
      - [Choice]: ¿Podrías hacer algo con mi voz?
        - **Player:** ¿Podrías hacer algo con mi voz?
        - **Makeover Mage:** No es algo en lo que tenga mucha experiencia, pero he aprendido un par de cosas de mis compañeros a lo largo de los años. ¿Quieres que altere tu voz?
        - [Menu]: Selecciona una opción
          - [Choice]: ¡Sí, por favor!
            - **Player:** ¡Sí, por favor!
            - **Makeover Mage:** Bueno, entonces, si te quedas quieto, esto no debería doler demasiado.
            - **Player:** No mencionaste que iba a ser hu-
            - **Player:** ¡Ay!
            - **Player:** ¡Guau! Sueno tan diferente, ¡gracias!
            - **Makeover Mage:** Me alegro de poder ayudar. ¿Había algo más en lo que pudiera ayudar?
            - (initial|initial-options)
          - [Choice]: Pensándolo bien, lo pasaré.
            - **Player:** Pensándolo bien, lo pasaré.
            - **Makeover Mage:** ¿Hay algo más en lo que pueda ayudarte?
            - (initial|initial-options)
      - [Choice]: ¿Puedes hacerme un color diferente?
        - **Makeover Mage:** ¡Por supuesto! Tengo una amplia gama de colores para que elijas.
        - **Makeover Mage:** También tengo algunos colores especiales para ti si deseas aprovecharlos.
        - **Makeover Mage:** Además, tengo algunas pociones especiales disponibles para que las compres si quieres adquirir un color más vibrante. Yo los llamo 'extracto de camaleón', son bastante útiles si eso es lo que buscas, pero son pociones de un solo uso.
        - **Makeover Mage:** Entonces, ¿qué dices? ¿Te apetece un cambio?
        - [Menu]: Selecciona una opción
          - [Choice]: Claro, hazlo.
            - (above|sure)
          - [Choice]: Me gustaría comprar un 'extracto de camaleón'.
            - **Player:** Me gustaría comprar un poco de 'extracto de camaleón'.
            - **Makeover Mage:** Excelente. Los vendo en paquetes de 1, 3 o 6. ¿Cuántos te gustaría comprar?
            - [Menu]: ¿Cuántos te gustaría comprar?
              - [Choice]: Uno.
                - (Se abre la interfaz de compra de Chameleon Extract (x1) por 126 RuneCoins)
                - (Condition: Si se presiona el botón 'confirmar':)
                  - (receives=a chameleon extract)
                  - Tu extracto de camaleón ha sido añadido a tu banco.
                - (Condition: Si se presiona el botón 'cancelar':)
                  - (end)
              - [Choice]: Tres.
                - (Se abre la interfaz de compra de Chameleon Extract (x3) por 270 RuneCoins)
                - (Condition: Si se presiona el botón 'confirmar':)
                  - (receives=three chameleon extract)
                  - Tu extracto de camaleón ha sido añadido a tu banco.
                - (Condition: Si se presiona el botón 'cancelar':)
                  - (end)
              - [Choice]: Seis.
                - (Se abre la interfaz de compra de Chameleon Extract (x6) por 396 RuneCoins)
                - (Condition: Si se presiona el botón 'confirmar':)
                  - (receives=six chameleon extract)
                  - Tu extracto de camaleón ha sido añadido a tu banco.
                - (Condition: Si se presiona el botón 'cancelar':)
                  - (end)
              - [Choice]: Ninguno, cambié de opinión.
                - **Player:** Ninguno, he cambiado de opinión.
                - **Makeover Mage:** Bueno, si cambias de opinión ya sabes dónde encontrarlos. ¿Algo más que quisieras preguntar?
                - (initial|initial-options)
          - [Choice]: No, gracias.
            - (above|no-thanks)
      - [Choice]: [More...]
        - (initial|initial-options)

#### Cómo usar un vale de cambio de imagen en Makeover Mage

- [Menu]: ¿Utilizas tu vale de cambio de imagen?
  - [Choice]: si
    - **Player:** Claro, hazlo. Voy a utilizar este cupón para un cambio de imagen gratuito.
    - **Makeover Mage:** ¡Ah, pero claro! No sabía que todavía estaban por ahí. El servicio es gratuito de todos modos.
    - (opens=Makeover Mage)
  - [Choice]: No
    - (end)

### After Evil Dave's Big Day Out

- **Makeover Mage:** Me alegro de verte de nuevo en tu cuerpo real. Supongo que todo salió bien en lo que respecta a recuperar tu cuerpo.
- **Player:** ¡Efectivamente!
- **Makeover Mage:** Me alegra saberlo. Ahora, ¿qué puedo hacer por ti?
- (above|initial-options)

### Overhead dialogue

- (Action: El mago se lanza un hechizo a sí mismo.)
- (Action: El mago cambia su propia apariencia.)
- (Condition: Si pasaron de hombre a mujer:)
  - **Makeover Mage:** {{RSChat|Ooh!}}
- (Condition: Si pasaron de mujer a hombre:)
  - **Makeover Mage:** {{RSChat|Aha!}}
