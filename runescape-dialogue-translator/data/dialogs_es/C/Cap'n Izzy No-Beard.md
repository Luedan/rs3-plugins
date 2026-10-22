# Cap'n Izzy No-Beard

- **Original Wiki Page**: [Transcript:Cap'n Izzy No-Beard](https://runescape.wiki/w/Transcript%3ACap%27n%20Izzy%20No-Beard)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Pieces of Hate

- **Player:** ¡Ahoy, Capitán!
- **Cap'n Izzy No-Beard:** ¡Ahoy!
- **Loro:** ¡Avasten los hisopos de escorbuto!
- **Player:** ¿Eh?
- **Cap'n Izzy No-Beard:** ¡No me hagas caso, loro, es la taza de té de Jenny rota!
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué es este lugar?
    - **Player:** ¿Qué es este lugar?
    - **Cap'n Izzy No-Beard:** ¡Esta, cordialmente, es la entrada al Brimhaven Agility Arena!
    - **Cap'n Izzy No-Beard:** ¡Estaba buscando un tesoro enterrado cuando lo encontré! ¡Me sorprendió! ¡Era un espectáculo digno de contemplar!
    - **Loro:** ¡Tesoro enterrado!
    - **Cap'n Izzy No-Beard:** ¡Era lo más grande que había visto en mi vida! ¡Debió haber sido al menos una legua de lado a lado!
    - **Cap'n Izzy No-Beard:** Me hizo una lista, ¡estaba tan emocionado!
    - **Loro:** ¡Adelante!
    - **Cap'n Izzy No-Beard:** Encontré una cueva enorme con todas estas plataformas. Creo que fue una civilización antigua la que lo hizo. ¡Tenía que tener mucho cuidado, ya que había trampas por todas partes! ¡Peligroso era!
    - **Loro:** ¡Peligro! ¡Peligro!
    - **Cap'n Izzy No-Beard:** ¡La entrada cuesta solo 200 coins!
    - (initial|options)
  - [Choice]: ¿Qué hago en la arena?
    - **Player:** ¿Qué hago en la arena?
    - **Cap'n Izzy No-Beard:** Bueno, cariño, es simple. Puedes cruzar entre dos plataformas usando las trampas u obstáculos colocados a través de ellas. Intenta llegar al pilar indicado por la flecha parpadeante.
    - **Cap'n Izzy No-Beard:** Recibes tickets por etiquetar más de un pilar seguido. Por lo tanto, no obtendrás un ticket del primer pilar, pero sí por cada plataforma que etiquetes en una fila después de eso.
    - **Cap'n Izzy No-Beard:** Si pierdes una plataforma, te perderás el siguiente boleto, ¡así que intenta conseguir todas las plataformas que puedas! Cuando hayas terminado, ¡llévale los boletos a Jackie y ella los cambiará por más cosas!
    - **Loro:** ¡Etiqueta cuando la luz verde significa multas! ¡Etiqueta cuando la luz roja significa luz verde!
    - **Cap'n Izzy No-Beard:** ¡Gracias de todo corazón!
    - **Loro:** ¡Peligro! ¡Peligro!
    - **Player:** Esto suena peligroso. ¿Puedo morir ahí abajo?
    - **Cap'n Izzy No-Beard:** Sí, puedes, soy cordial, pero yo cuido a mis clientes, ¿ves? Si mueres, traeré tu lápida y tus objetos a esta cabaña.
    - **Player:** ¡Gracias!
    - (initial|options)
  - [Choice]: Me gustaría utilizar Agility Arena, por favor.
    - **Player:** Me gustaría utilizar Agility Arena, por favor.
    - (Condition: If the player has not completed Rocking Out:)
      - **Cap'n Izzy No-Beard:** Sí, la entrada será 200 coins.
      - **Loro:** ¡Piezas de ocho!
      - **Cap'n Izzy No-Beard:** ¡Una advertencia, de todo corazón! ¡Hay trampas peligrosas ahí abajo!
      - [Menu]: Selecciona una opción
        - [Choice]: Bien, aquí tienes 200 coins.
          - (Condition: If the player does not have enough money:)
            - No puedes permitirte eso.
            - **Player:** No tengo el dinero encima en este momento.
            - **Loro:** *graznado*
            - **Cap'n Izzy No-Beard:** ¡No coins, no hay entrada!
          - (Condition: If the player has enough money:)
            - **Player:** Bien, aquí tienes 200 coins.
            - (removes=200 coins)
            - [Le das al Capitán Izzy 200 coins.]
            - **Cap'n Izzy No-Beard:** ¡Que el viento sople en vuestras velas!
        - [Choice]: No importa.
          - **Player:** No importa.
    - (Condition: If the player has already paid:)
      - **Cap'n Izzy No-Beard:** Ya pagaste, así que baja...
    - (Condition: If the player has completed Rocking Out:)
      - **Cap'n Izzy No-Beard:** Siempre eres bienvenido aquí, Player. ¡No es necesario pagar!
  - [Choice]: ¿Es cierto que vendes Skillcapes o Agility?
    - (Condition: If the player has a ring of charos (a) equipped:)
      - **Cap'n Izzy No-Beard:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins por este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
      - [Menu]: Elige una opción:
        - [Choice]: ¿92.000 coins? Eso es demasiado caro.
          - **Player:** Sé dónde encontrarte si cambio de opinión.
        - [Choice]: De hecho, creo que tengo el dinero aquí.
          - (Condition: If the player has no backpack space:)
            - **Cap'n Izzy No-Beard:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar algo de espacio en backpack antes de que pueda venderte uno.
          - (Condition: If the player does not have enough money:)
            - **Player:** Pero desafortunadamente me equivoqué.
            - **Cap'n Izzy No-Beard:** Bueno, vuelve a verme cuando lo hagas.
          - (Condition: If the player has enough money:)
            - (receives=agility cape and agility hood) (removes=92,000 coins)
            - **Cap'n Izzy No-Beard:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
    - (Condition: If the player does not have a ring of charos (a) equipped:)
      - [Menu]: Elige una opción:
        - [Choice]: ¿99.000 coins? Eso es demasiado caro.
          - **Player:** Sé dónde encontrarte si cambio de opinión.
        - [Choice]: De hecho, creo que tengo el dinero aquí.
          - (Condition: If the player has no backpack space:)
            - (arriba)
          - (Condition: If the player does not have enough money:)
            - (arriba)
          - (Condition: If the player has enough money:)
            - (receives=agility cape and agility hood) (removes=99,000 coins)
            - **Cap'n Izzy No-Beard:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
  - [Choice]: He notado que hay un par de versiones de cada skillcape.
    - **Cap'n Izzy No-Beard:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
    - (Condition: If the player is using the old model:)
      - **Cap'n Izzy No-Beard:** Parece que actualmente estás usando el modelo anterior para tu Agility skillcape. ¿Quieres cambiar a uno más nuevo?
      - (continue)
    - (Condition: If the player is using the new model:)
      - **Cap'n Izzy No-Beard:** Aún puedes elegir usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, me gustaría usar la versión [new/old] del skillcape.
        - **Cap'n Izzy No-Beard:** ¿Te gustaría usar el modelo [old/newer] solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
        - [Menu]: Selecciona una opción
          - [Choice]: Sólo me gustaría cambiar la agilidad skillcape.
            - **Cap'n Izzy No-Beard:** No hay problema, ahora usarás el modelo [older/newer] para tu agilidad skillcape.
          - [Choice]: Me gustaría cambiar todos mis skillcapes.
            - **Cap'n Izzy No-Beard:** ¡No hay problema, ahora usarás el modelo [older/newer] para todos tus skillcapes!
          - [Choice]: ¡He cambiado de opinión!
            - (end)
      - [Choice]: No, gracias.
        - **Cap'n Izzy No-Beard:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión [old/new]!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Cap'n Izzy No-Beard:** Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas.
          - [Menu]: Selecciona una opción
            - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
              - **Cap'n Izzy No-Beard:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
            - [Choice]: No, gracias.
              - (end)

#### Intentando ingresar al Agility Arena sin pagar

- **Loro:** ¡Aplauda a [him/her] con hierros!
- **Cap'n Izzy No-Beard:** ¡Ahoy! ¡Paga primero!

#### Intentando entrar al Agility Arena con un seguidor fuera

- **Loro:** ¡Graznido!
- **Cap'n Izzy No-Beard:** ¡Oye, amigo! ¡No se permiten seguidores en la arena!

### After Pieces of Hate

- [Menu]: Selecciona una opción
  - [Choice]: Habla de Piezas de odio.
    - **Cap'n Izzy No-Beard:** ¡Ya está! ¡Se acabó! ¡Rabid Jack ya no nos amenazará más!
    - **Cap'n Izzy No-Beard:** Gracias, Player. No podríamos haberlo hecho sin ti.
  - [Choice]: Hable sobre el Agility Arena.
    - (continuea|greeting)

### Pay option


#### Antes de rockear

- (removes=200 coins)
- [Le das al Capitán Izzy la tarifa de entrada de 200 monedas.]
- Le das al Capitán Izzy la tarifa de entrada de 200 monedas.

#### Después de pagar

- **Cap'n Izzy No-Beard:** ¡Avast ahí, ya pagaste!
- **Loro:** Tiemblame maderas, ¡qué tonta!

#### Después de rockear

- **Cap'n Izzy No-Beard:** Siempre eres bienvenido aquí, Player. ¡No es necesario pagar!

### Treasure Trails

- **Cap'n Izzy No-Beard:** ¿Puedo ayudarte en algo?
- **Player:** Bueno, estoy aquí por un sendero del tesoro.
- **Cap'n Izzy No-Beard:** Ah, entonces querrás hablar con él.
- **Player:** ¿Él?
- **Loro:** ¡Avast!
- **Loro:** ¡Responde esto y te daré un tesoro!
- (receives=challenge scroll)
- [¡El loro te ha dado un pergamino de desafío!]

##### Cuando hablé de nuevo

- **Loro:** Ingrese la respuesta a la pregunta.
- ''(Cuando se le da la respuesta incorrecta:)
  - **Loro:** ¡Inténtalo de nuevo! ¡Intentar otra vez!
- ''(Cuando se le da la respuesta correcta:)
  - (removes=the challenge scroll and the old clue scroll (hard))
  - (Si el camino continúa:)
    - (receives=a new clue scroll (hard))
    - [¡El loro te ha dado otro pergamino de pistas!]
    - (continue)
  - (Si el sendero termina:)
    - (receives=reward casket (hard))
    - [¡Has encontrado un ataúd!]
    - (continue)
  - **Loro:** ¡Graznido! ¡Piezas de ocho!
