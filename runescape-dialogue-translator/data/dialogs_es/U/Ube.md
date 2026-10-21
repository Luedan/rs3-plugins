# Ube

- **Original Wiki Page**: [Transcript:Ube](https://runescape.wiki/w/Transcript%3AUbe)
- **Letter**: `U`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### En mundos gratuitos

- **Player:** Hola. ¿Puedo preguntarte sobre-?
- **Ube:** ¡Me temo que no por el momento! No es lo suficientemente seguro hablar ahora.
- **Player:** ¡Pero ni siquiera sabes lo que iba a preguntar!
- **Ube:** Oh, tengo una idea suficiente para saber que no es lo suficientemente seguro hablar de ello en un mundo libre.

#### Antes de que todos se enciendan

- **Player:** Hola. ¿Qué estás haciendo aquí?
- **Ube:** Me temo que no tengo mucho tiempo para charlar en este momento.
- **Player:** ¿En serio? Parece que no estás haciendo nada más que quedarte parado.
- **Ube:** Bueno, ¡ahí es donde tus ojos te engañan! No sólo estoy parado, sino que también escudriño el horizonte. Se necesita mucha energía y concentración para estar preparado para las emergencias.
- **Player:** Ya veo.

#### Después de todo entusiasmado


##### Antes de darle una fruta blanca.

- **Ube:** ¡Hola viajero! ¿Puedo imponerte por un momento?
- **Player:** ¿Qué es?
- **Ube:** Bueno, se supone que debo cuidar estas balizas, pero estoy completamente agotado. Escudriñar constantemente el horizonte es un trabajo duro.
- **Ube:** He oído que la fruta del Árbol Blanco puede animarnos un poco. ¿Hay alguna manera de que puedas traerme uno? Estaría eternamente agradecido.
- [Menu]: Selecciona una opción
  - [Choice]: Estaré feliz de poder ayudar.
    - **Player:** Estaré encantado de ayudarte. Después de todo, la seguridad del reino es primordial.
    - **Ube:** Muchas gracias. Me preocupa que si sigo en este estado, podría perderme algo importante.
  - [Choice]: Lo siento, estoy ocupado en este momento.
    - **Player:** Lo siento, estoy ocupado en este momento.
    - **Ube:** Ah, bueno. No cuesta nada preguntar.

##### Regalándole una fruta blanca.

- **Ube:** ¡Hola viajero! Mira, odio ser grosero, pero ¿es ese el aroma de la fruta del Árbol Blanco lo que huelo?
- **Player:** Puede que lo sea.
- **Ube:** No tendrás uno de repuesto, ¿verdad? Estoy completamente exhausto y me vendría bien un estímulo.
- [Menu]: Selecciona una opción
  - [Choice]: Por supuesto; Traje uno solo para ti.
    - **Player:** Por supuesto; Traje uno solo para ti.
    - (removes=white tree fruit)
    - **Ube:** Muchas gracias. No puedo decirte cuánto ansiaba la fruta del Árbol Blanco.
    - **Player:** Encantado de poder ayudar.
    - **Ube:** Si algún día puedo devolverte el favor, házmelo saber.
  - [Choice]: Lo siento, no puedo ayudarte en este momento.
    - **Player:** Lo siento, no puedo ayudarte en este momento.
    - **Ube:** Ah, bueno. No cuesta nada preguntar.

##### Después de darle una fruta blanca.

- **Ube:** Hola. ¿Puedo ayudarte en algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: Si la baliza está apagada:)
      - **Ube:** Por supuesto. Una vez que la baliza esté encendida, déjame 5 logs y yo me ocuparé del fuego todo el tiempo que pueda.
    - (Condition: Si la baliza está muriendo:)
      - **Ube:** Bueno, podría, pero ya que estás aquí, es mejor que lo hagas tú mismo.
    - (Condition: Si la baliza no muere:)
      - (Condition: Si Ube no tiene cinco logs:)
        - (Condition: Si el player no tiene al menos cinco logs del mismo tipo:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Ube:** Me temo que no tienes suficiente registro del tipo correcto para que yo lo use.
        - (Condition: Si el player tiene al menos cinco logs del mismo tipo:)
          - (Condition: Si el mensaje de confirmación está habilitado:)
          - **Ube:** Necesitaré cinco logs para poder atender el fuego. ¿Está bien?
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Ube:** ¡Gracias! Usaré estos cinco logs para mantener encendida la baliza mientras estás fuera.
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Ube:** Bueno, ya sabes dónde estoy si cambias de opinión.
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: Si el mensaje de confirmación está deshabilitado:)
            - (above|talk-give-logs)
      - (Condition: Si Ube tiene cinco logs:)
        - **Ube:** Por supuesto que lo haré, no te preocupes, usaré el logs que ya me dejaste.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Ube:** Pero claro. Sólo echa un vistazo a mi mapa.
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Ube:** Puedo informarte del estado de las balizas en ambas direcciones, hasta los últimos fuegos que se encienden.
    - **Ube:** Probablemente también podría contarte sobre las otras balizas, pero necesitaría la ayuda de una guacamaya.
    - **Player:** ¿Una guacamaya?
    - **Ube:** Sí. Los guacamayos tienen la capacidad de volar muy alto en el aire y ver cosas que están mucho más lejos.
    - **Ube:** También son muy inteligentes y se les puede entrenar para proporcionar la información exacta que necesito para obtener una descripción completa de la red de balizas.
    - ((Si el player tiene una bolsa de guacamayo en su backpack:))
      - **Ube:** Ahora que lo pienso, la guacamaya que tienes en tu mochila sería perfecta.
      - (continue|macaw)
  - [Choice]: ¿Cómo estás?
    - **Player:** ¿Cómo te va?
    - **Ube:** Bastante bien, en su mayor parte. He mirado mucho el horizonte hoy; es un trabajo bastante duro.
    - **Player:** ¿Has visto algo preocupante?
    - **Ube:** No hasta ahora, afortunadamente, pero hay que estar constantemente atento a las amenazas que vienen del norte.
    - **Player:** ¿No es agotador tener los ojos bien abiertos constantemente?
    - **Ube:** Bueno, en realidad, mirar fijamente algo durante demasiado tiempo puede resultar agotador para la vista.
    - **Ube:** Tomo un pequeño descanso aproximadamente cada hora y aparto la vista del horizonte durante unos minutos, sólo para descansar la vista.
    - **Player:** ¿Ah? ¿Qué miras entonces?
    - **Ube:** Bueno, en realidad, también estoy aprovechando esta oportunidad para aumentar mis conocimientos sobre mohos y hongos locales.
    - **Player:** ¿Hablas en serio?
    - **Ube:** ¡No solo puedo detectar el peligro a kilómetros de distancia, sino que soy el identificador más rápido de moho en el pan de este lado del río Lum!
    - **Player:** Ese es... un reclamo único a la fama.
    - **Ube:** Estoy muy orgulloso de ello, de verdad. Espero expandirme a las levaduras y luego a los champiñones.
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Ube:** ¡Bien! Entonces ya terminé de hablar contigo.

### Using a macaw pouch on Ube


#### Antes de darle a Ube una bolsa de guacamaya{{Anchor|macaw}}

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=a macaw pouch)
    - **Ube:** Muchas gracias. Esta guacamaya me ayudará a brindarles información más detallada sobre la red de balizas.
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Ube:** Haz lo que quieras.

#### Después de darle a Ube una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; ella no necesita otra.

### Using logs on Ube

- (Condition: Si la baliza está apagada:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: Si la baliza está muriendo:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: Si la baliza no muere:)
  - (Condition: Si Ube no tiene cinco logs:)
    - (Condition: Si el mensaje de confirmación está habilitado:)
      - [Menu]: ¿Quieres darle cinco logs al fuego?
        - [Choice]: Sí.
          - (Condition: Si el player no tiene al menos cinco logs del mismo tipo:)
            - El bombero necesita cinco troncos del mismo tipo para mantener este fuego.
          - (Condition: Si el player tiene al menos cinco logs del mismo tipo:)
            - (removes=five logs)
            - Le das al fuego tierno 5 [type] logs.
        - [Choice]: No.
          - **Player:** Creo que, después de todo, me quedaré con mi logs.
        - [Choice]: Sí. Por favor, no vuelvas a pedirme confirmación.
          - (above|use-give-logs)
    - (Condition: Si el mensaje de confirmación está deshabilitado:)
      - (above|use-give-logs)
  - (Condition: Si Ube tiene cinco logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
