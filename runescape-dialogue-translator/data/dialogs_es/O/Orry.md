# Orry

- **Original Wiki Page**: [Transcript:Orry](https://runescape.wiki/w/Transcript%3AOrry)
- **Letter**: `O`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### En mundos gratuitos

- **Player:** Hola. ¿Puedo preguntarte sobre-?
- **Orry:** ¡Por el momento no, [dude/dudette]! No es lo suficientemente seguro hablar ahora.
- **Player:** ¡Pero ni siquiera sabes lo que iba a preguntar!
- **Orry:** Oh, tengo una idea suficiente para saber que no es lo suficientemente seguro hablar de ello en un mundo libre.

#### Antes de que todos se enciendan

- **Player:** ¡Hola! ¿Qué estás haciendo hoy?
- **Orry:** Hombre, simplemente me relajaría y me lo tomaría con calma, pero hay mucho que hacer.
- **Player:** ¿Ah? ¿Cómo qué?
- **Orry:** Lo siento, [dude/dudette], sé que es un fastidio total, pero tengo que concentrarme ahora mismo. Nos vemos luego, ¿sí?
- **Player:** Oh, claro. Buena suerte con todo.

#### Después de todo entusiasmado


##### Antes del escudo familiar

- **Player:** Hola. Me preguntaba si podrías ayudarme.
- **Orry:** ¡No puedo sintonizar tu longitud de onda ahora mismo, hombre! Estoy demasiado angustiado.
- **Player:** ¿Qué pasa?
- **Orry:** Es mi amigo, en el Jolly Boar, como. Está realmente enfermo y yo estoy atrapado mirando esta baliza, así que no puedo ayudarlo.
- **Player:** Lamento oír eso. Si ayuda-
- **Orry:** Mira, ni siquiera me hables, ¿vale? Necesito algo de espacio para la cabeza, como. Es mi mejor amigo, hombre.
- Misión [Family Crest].}}

##### Después del escudo familiar

- **Orry:** Hola, [dude/dudette]. ¿Qué pasa?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: If the beacon is unlit:)
      - **Orry:** Por supuesto. Una vez que la baliza esté encendida, déjame 5 logs y yo me ocuparé del fuego todo el tiempo que pueda.
    - (Condition: If the beacon is dying:)
      - **Orry:** Bueno, podría, pero ya que estás aquí, es mejor que lo hagas tú mismo.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Orry does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Orry:** 'Me temo que no tienes suficiente registro del tipo correcto para que yo lo use.
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Orry:** [Dude/dudette], necesitaré como cinco logs para cuidar el fuego por ti. ¿Eso es genial?
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Orry:** ¡As! Usaré estos cinco logs para mantener encendida la baliza mientras estás fuera.
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Orry:** Bueno, sabes dónde estoy si cambias de opinión, ¿no?
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Orry has five logs:)
        - **Orry:** Por supuesto [dude/dudette]; no hay problema. Usaré el logs que ya me dejaste.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Orry:** ¡Claro, [dude/dudette]! Simplemente apunten sus mirones a este increíble mapa mío.
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Orry:** Mis ojos son impresionantes. Puedo contarte todo sobre las balizas en cualquier dirección, siempre y cuando los fuegos estén encendidos.
    - **Orry:** Para contarte sobre los otros, necesitaría la ayuda de una guacamaya, como.
    - **Player:** ¿Una guacamaya?
    - **Orry:** Sí. Las guacamayas pueden volar muy alto en el aire y ver cosas que están mucho más lejos, como.
    - **Orry:** También son muy inteligentes y se les puede entrenar para que regresen con la información exacta que necesitaría para contarles todo sobre la red de balizas.
    - ((If the player has a macaw pouch in their backpack:))
      - **Orry:** Ahora que lo pienso, la guacamaya que tienes en tu mochila sería perfecta.
      - (continue|macaw)
  - [Choice]: ¿Cómo te va?
    - **Player:** ¿Cómo te va?
    - **Orry:** Hombre, me relajaría y me lo tomaría con calma, ¡pero hay mucho que hacer!
    - **Player:** ¿Ah? ¿Cómo qué?
    - **Orry:** Bueno, están estas balizas, hombre. Necesitan que los cuiden.
    - **Player:** ¿No es agotador tener los ojos bien abiertos constantemente?
    - **Orry:** Bueno, en realidad, mirar fijamente algo durante demasiado tiempo puede resultar agotador para la vista.
    - **Orry:** Y cuando no estoy haciendo eso, necesito mantener a los mirones pegados al horizonte, atentos constantemente a señales de problemas.
    - **Player:** ¡Eso parece mucho trabajo!
    - **Orry:** Totalmente, como. No puedo esperar para encontrarme con Jonathan más tarde en el Jolly Boar. ¡Estoy *seco*!
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Orry:** ¡Duro, [dude/dudette]!

### Using a macaw pouch on Orry


#### Antes de darle a Orry una bolsa de guacamaya{{Anchor|macaw}}

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=a macaw pouch)
    - **Orry:** Muchas gracias. Esta guacamaya me ayudará a brindarles información más detallada sobre la red de balizas.
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Orry:** Haz lo que quieras.

#### Después de darle a Orry una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; él no necesita otro.

### Using logs on Orry

- (Condition: If the beacon is unlit:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: If the beacon is dying:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: If the beacon is not dying:)
  - (Condition: If Orry does not have five logs:)
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
  - (Condition: If Orry has five logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Orry:** ¡Oye! ¡Aléjate de eso! Hasta que no hayas demostrado que eres un verdadero aliado de Varrock, ¡no podrás usar eso!
- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
