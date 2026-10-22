# Waldo

- **Original Wiki Page**: [Transcript:Waldo](https://runescape.wiki/w/Transcript%3AWaldo)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### En mundos gratuitos

- **Player:** Hola. ¿Puedo preguntarte sobre-?
- **Waldo:** ¡Me temo que no por el momento! No es lo suficientemente seguro hablar ahora.
- **Player:** ¡Pero ni siquiera sabes lo que iba a preguntar!
- **Waldo:** Oh, tengo una idea suficiente para saber que no es lo suficientemente seguro hablar de ello en un mundo libre.

#### Antes de que todos se enciendan

- **Player:** Entonces, ¿qué estás haciendo en este buen día?
- **Waldo:** Oh, solo atendiendo este fuego.
- **Player:** ¿Qué fuego? No veo ningún fuego.
- **Waldo:** Oh, todavía no está encendido.
- **Player:** Entonces, ¿estás aquí parado, mirando una fogata vacía?
- **Waldo:** Por supuesto que no. Al cuidar una baliza, es mucho más importante observar el entorno que observar el fuego en sí.
- **Player:** ¿Lo es?
- **Waldo:** Por supuesto. Hay que estar constantemente atento a cualquier señal de peligro. De hecho, hablar contigo me distrae un poco de mis deberes para con el reino. Me temo que tendré que despedirme ahora.
- **Player:** Ah, claro. Lo siento.

#### Después de todo entusiasmado


##### Antes de completar el tutorial de Grand Exchange

- **Player:** Hola. Me preguntaba si podrías ayudarme...
- **Waldo:** Supongo que podría, pero debo admitir que me siento un poco intimidado al hablar con alguien que parece tan valiente y aventurero.
- **Player:** ¿Hablas en serio?
- **Waldo:** Oh, muy en serio. No creo que tengamos suficientes puntos en común para poder siquiera empezar a tener una conversación contigo.
- **Player:** Entonces, ignorando el hecho de que, de hecho, estamos teniendo una conversación en este mismo momento, ¿estás diciendo que me ayudarías si... compartiéramos algunos intereses?
- **Waldo:** Eso es exactamente.
- **Player:**Entonces, ¿qué te interesa?
- **Waldo:** Bueno, tal vez si aprendieras más sobre el apasionante mundo del comercio, me sentiría más capaz de hablar contigo.
- **Player:** Eres una persona muy extraña.
- **Waldo:** Ese tipo de comentario no ayuda, ¿sabes?
- [Grand Exchange].}}

##### Después de completar el tutorial de Grand Exchange

- **Waldo:** Hola. ¿Hay algo en lo que pueda ayudarte?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: If the beacon is unlit:)
      - **Waldo:** Por supuesto. Una vez que la baliza esté encendida, déjame 5 logs y yo me ocuparé del fuego todo el tiempo que pueda.
    - (Condition: If the beacon is dying:)
      - **Waldo:** Bueno, podría, pero ya que estás aquí, es mejor que lo hagas tú mismo.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Waldo does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Waldo:** Me temo que no tienes suficiente logs del tipo correcto para que yo lo use.
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Waldo:** Necesitaré cinco logs para poder atender el fuego. ¿Está bien? Ronroneo.
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Waldo:** ¡Gracias! Usaré estos cinco logs para mantener encendida la baliza mientras estás fuera.
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Waldo:** Bueno, ya sabes dónde estoy si cambias de opinión.
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Waldo has five logs:)
        - **Waldo:** Por supuesto que lo haré; no te preocupes. Usaré el logs que ya me dejaste.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Waldo:** Ah, sí. Quizás sería más fácil para mí mostrarte en mi mapa...
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given Waldo a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Waldo:** Puedo informarte del estado de las balizas en ambas direcciones, hasta los últimos fuegos que se encienden.
    - **Waldo:** Probablemente también podría contarte sobre las otras balizas, pero necesitaría la ayuda de una guacamaya.
    - **Player:** ¿Una guacamaya?
    - **Waldo:** Sí. Los guacamayos tienen la capacidad de volar muy alto en el aire y ver cosas que están mucho más lejos.
    - **Waldo:** También son muy inteligentes y se les puede entrenar para proporcionar la información exacta que necesito para obtener una descripción completa de la red de balizas.
    - ((If the player has a macaw pouch in their backpack:))
      - **Waldo:** Ahora que lo pienso, la guacamaya que tienes en tu mochila sería perfecta, por ejemplo.
      - (continue|macaw)
  - [Choice]: ¿Cómo te va?
    - **Player:** ¿Cómo te va?
    - **Waldo:** Nada mal, nada mal.
    - **Player:** Entonces, ¿qué estás haciendo en este buen día?
    - **Waldo:** Oh, lo de siempre.
    - **Player:** ¿Qué es 'lo habitual'?
    - **Waldo:** Bueno, estoy vigilando de cerca las señales de peligro y estoy constantemente escaneando el horizonte en busca del brillo de otras balizas.
    - **Player:** ¿Eso es todo en lo que piensas?
    - **Waldo:** Oh, no. Es muy importante mantener la mente activa en un trabajo como este. Si te vuelves perezoso al pensar, es posible que te vuelvas perezoso al observar.
    - **Player:** Intrigante... Entonces, ¿en qué piensas para mantener tu mente activa?
    - **Waldo:** Oh, supongo que pienso principalmente en mi colección de estampillas.
    - **Player:** ¿Mayormente?
    - **Waldo:** También pienso en los pájaros que he visto últimamente.
    - **Player:** ¿Pájaros? ¿Piensas en los pájaros?
    - **Waldo:** Sí. Soy un ávido ornitólogo.
    - **Player:** Te gusta observar aves, ¿eh? ¡Debes ver muchos pájaros en el trabajo!
    - **Waldo:** Oh, bastante. Es muy conveniente tener un hobby que se integre tan bien con la carrera.
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Waldo:** Entonces baja la voz. Ahuyentarás a los pájaros.

### Using a macaw pouch on Waldo


#### Antes de darle a Waldo una bolsa de guacamaya{{Anchor|macaw}}

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=a macaw pouch)
    - **Waldo:** Muchas gracias. Esta guacamaya me ayudará a brindarles información más detallada sobre la red de balizas.
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Waldo:** Haz lo que quieras.

#### Después de darle a Waldo una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; él no necesita otro.

### Using logs on Waldo

- (Condition: If the beacon is unlit:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: If the beacon is dying:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: If the beacon is not dying:)
  - (Condition: If Waldo does not have five logs:)
    - (Condition: If the confirmation prompt is enabled:)
      - [Menu]: ¿Quieres darle cinco logs al fuego?
        - [Choice]: Sí.
          - (Condition: If the player does not have at least five logs of the same type:)
            - El bombero necesita cinco troncos del mismo tipo para mantener este fuego.
          - (Condition: If the player has at least five logs of the same type:)
            - (removes=five logs)
            - Le das al fuego tierno 5 [type] logs.
        - [Choice]: No.
          - **Player:** Creo que, después de todo, me quedaré con mi logs.
        - [Choice]: Sí. Por favor, no vuelvas a pedirme confirmación.
          - (above|use-give-logs)
    - (Condition: If the confirmation prompt is disabled:)
      - (above|use-give-logs)
  - (Condition: If Waldo has five logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Waldo:** ¡Oye! ¡Aléjate de eso! Hasta que no hayas demostrado que eres un verdadero aliado de Varrock, ¡no podrás usar eso!
- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
