# Stubthumb

- **Original Wiki Page**: [Transcript:Stubthumb](https://runescape.wiki/w/Transcript%3AStubthumb)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### En mundos gratuitos

- **Player:**Hola. ¿Puedo preguntarte sobre eso?
- **Stubthumb:**¡Hmph! ¿No sabes nada? No es seguro hablar ahora.
- **Player:**Pero ni siquiera sabes lo que iba a preguntar.
- **Stubthumb:**Sé lo suficiente como para saber que no es seguro hablar a menos que estemos en el mundo de miembros.

#### Antes de que todos se enciendan

- **Player:** ¡Hola!
- **Stubthumb:** Hmmph. Hola a ti mismo.
- **Player:** ¡Eso no suena muy amigable!
- **Stubthumb:** Es difícil sentirse amigable cuando te duelen los pies.
- **Player:** Entiendo tu punto. ¿Has intentado, ya sabes, simplemente sentarte?
- **Stubthumb:** Sentarse hace que duela la espalda.
- **Player:** Ah. Ése es un dilema.

#### Después de todo entusiasmado


##### Antes de darle un sombrero davy kebbit

- **Player:** Hola. Me preguntaba si podrías ayudarme.
- **Stubthumb:** Lo siento. No puedo oírte. Mis oídos están demasiado fríos y me duelen los pies.
- **Player:** ¿Cómo es que el dolor de pies te impide oír?
- **Stubthumb:** Me alegro de no poder oírte. Suenas muy molesto.
- **Player:** Correcto. Entonces, digamos que te trajera, oh, no lo sé, un bonito y cálido gorro para cubrirte las orejas. ¿Entonces podrías oírme?
- **Stubthumb:** Si fuera un lindo, cálido y peludo gorro kebbit hecho por Frawd la ogresa. Son muy bonitos a la vista y muy cálidos.
- **Player:** No eres muy sutil, ¿sabes?
- **Stubthumb:** ¿Qué? Lo siento. Oídos demasiado fríos para oírte a ti y a todo eso.

##### Dándole un sombrero davy kebbit

- **Stubthumb:** ¡Oh, sombrero de kebbit! Eso es exactamente lo que siempre quise. Sería perfecto para mantener el cabello alejado del viento.
- **Player:** ¿Qué pelo? ¡No tienes pelo!
- **Stubthumb:** ¿Vas a darlo o estás aquí para burlarte de mí?
- [Menu]: Selecciona una opción
  - [Choice]: Adelante, tómalo.
    - (removes=davy kebbit hat)
    - **Stubthumb:** Muchas gracias. ¡Encaja como un sueño! Mis oídos están tan calientes ahora.
    - **Player:** Me alegra que te guste. Te queda perfecto.
    - **Stubthumb:** Muy agradecido. Estoy en deuda contigo, humano.
  - [Choice]: Lo siento, sólo lo traje aquí para burlarme de ti.
    - **Player:** Lo siento, solo lo traje aquí para burlarme de ti.
    - **Stubthumb:** Harrumph. Es bueno que mis oídos estén demasiado fríos para escucharte o me enojaría mucho.

##### Después de darle un sombrero davy kebbit

- **Stubthumb:** Hmph, eres tú. Muchas gracias por el gran sombrero. ¿Algo que quieras a cambio?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: If the beacon is unlit:)
      - **Stubthumb:** Por supuesto. Una vez que enciendas la baliza, dame 5 logs y haré que el fuego arda por mucho tiempo.
    - (Condition: If the beacon is dying:)
      - **Stubthumb:** Sólo me ocupo del fuego ardiente. ¡Tú mismo te ocupas del fuego moribundo!
    - (Condition: If the beacon is not dying:)
      - (Condition: If Stubthumb does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Stubthumb:** ¿Cómo puedo cuidar el fuego por ti? ¡No tienes suficiente logs bueno para que yo lo use!
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Stubthumb:** Necesitas cinco logs para cuidar el fuego. ¿Bueno?
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Stubthumb:** Gracias. Utilizo estos cinco logs para mantener la baliza encendida mientras estás fuera.
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Stubthumb:** Bueno. Sabes dónde estoy si cambias de opinión.
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Stubthumb has five logs:)
        - **Stubthumb:** Por supuesto. Yo uso logs que ya dejaste aquí.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Stubthumb:** Sí, bueno, si es necesario, mira el mapa.
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Stubthumb:** Hmm, ¿qué estás diciendo? ¿Mis ojos no son buenos? ¡Son mucho mejores que los tuyos! Puedo informarle sobre todas las balizas en cualquier dirección, siempre que estén encendidas.
    - **Player:** Sí, pero ¿qué pasa con las balizas que no están encendidas?
    - **Stubthumb:** También podría contarte sobre las otras balizas, si tengo ayuda de la guacamaya.
    - **Player:** ¿Una guacamaya?
    - **Stubthumb:** Sí. Las guacamayas pueden volar muy alto en el aire y ver a larga distancia. También son criaturas muy inteligentes.
    - **Stubthumb:** Puede volar por el aire y luego informar sobre toda la red de balizas.
    - ((If the player has a macaw pouch in their backpack:))
      - **Stubthumb:** Oye, estás sosteniendo una guacamaya. Le das guacamayo, te hablo de otras balizas también.
      - (continue|macaw)
  - [Choice]: ¿Cómo te va?
    - **Player:** ¿Cómo te va?
    - **Stubthumb:** ¡Horrible! ¿Por qué haces preguntas tan estúpidas?
    - **Player:** ¡Eso no suena muy amigable!
    - **Stubthumb:** Es difícil ser amigable cuando te duelen los pies.
    - **Player:** Entiendo tu punto. ¿Has intentado, ya sabes, simplemente sentarte?
    - **Stubthumb:** Sentarse hace que duela la espalda.
    - **Player:** Ah. Ése es un dilema.
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Stubthumb:** Hmmph.

### Using a macaw pouch on Stubthumb


#### Antes de darle a Stubthumb una bolsa de guacamaya{{Anchor|macaw}}

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=a macaw pouch)
    - **Stubthumb:** Gracias. Guacamayo ayúdame a contarte más sobre otras balizas.
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Stubthumb:** Haz lo que quieras.

#### Después de darle a Stubthumb una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; él no necesita otro.

### Using logs on Stubthumb

- (Condition: If the beacon is unlit:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: If the beacon is dying:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: If the beacon is not dying:)
  - (Condition: If Stubthumb does not have five logs:)
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
  - (Condition: If Stubthumb has five logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
