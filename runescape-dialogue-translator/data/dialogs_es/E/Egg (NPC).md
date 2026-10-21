# Egg (NPC)

- **Original Wiki Page**: [Transcript:Egg (NPC)](https://runescape.wiki/w/Transcript%3AEgg%20%28NPC%29)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### Antes de que todos se enciendan

- **Player:** Entonces, ¿qué estás haciendo exactamente aquí arriba, solo?
- **Huevo:** Oh, yo vigilo muy de cerca el horizonte; es un trabajo muy importante, vigilar al rey.
- **Player:** ¿Nunca te sientes solo?
- **Huevo:** Oh, para nada. Hay muchas piedras y palos con quienes hablar; son una muy buena compañía.
- **Player:** ¿Hablas con piedras y palos?
- **Egg:** Sí, son muy buenos oyentes.
- **Player:** Bueno, no puedo discutir eso.

#### Después de todo entusiasmado


##### Sin haber completado Troll Romance y La gran aventura de My Arm

- **Player:** Entonces, ¿qué estás haciendo exactamente aquí arriba, solo?
- **Huevo:** Lo habitual. Mira el fuego. Mirar horizonte. Mira disparar un poco más.
- **Player:** Suena absolutamente emocionante. Mira, no quiero cambiar de tema, pero ¿hay alguna manera de que puedas ayudarme? Tengo un par de preguntas.
- **Huevo:** Hmm, no estoy tan seguro. Quizás si ayudas a los trolls, yo te ayude.
- **Player:** Ah, pero soy un gran amigo de los trolls. Pregúntale a cualquiera, me refiero a cualquier troll.
- **Huevo:** No lo sé. Lo pienso. Mientras tanto, déjame en paz y déjame volver a mirar el fuego.
- [My Arm's Big Adventure] para ganarse la confianza de Egg.}}

##### Habiendo completado también Troll Romance y My Arm's Big Adventure

- **Huevo:** Oh, hola. ¿Lo que quieras?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: Si la baliza está apagada:)
      - **Huevo:** Sí. Una vez encendida la baliza, deja 5 logs conmigo y yo me encargo del fuego por un tiempo.
    - (Condition: Si la baliza está muriendo:)
      - **Huevo:** Podría, pero el fuego ya se está extinguiendo. Tú lo haces arder de nuevo y luego yo lo cuido por ti.
    - (Condition: Si la baliza no muere:)
      - (Condition: Si Egg no tiene cinco logs:)
        - (Condition: Si el player no tiene al menos cinco logs del mismo tipo:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Huevo:** ¿Cómo puedo cuidar el fuego por ti? ¡No tienes suficiente logs bueno para mí!
        - (Condition: Si el player tiene al menos cinco logs del mismo tipo:)
          - (Condition: Si el mensaje de confirmación está habilitado:)
            - **Huevo:** Necesitas cinco logs para cuidar el fuego. ¿Te parece bien?
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Huevo:** Gracias. Utilizo estos cinco logs para mantener la baliza encendida mientras estás fuera.
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Huevo:** Está bien. Sabes dónde estoy si cambias de opinión.
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: Si el mensaje de confirmación está deshabilitado:)
            - (above|talk-give-logs)
      - (Condition: Si Egg tiene cinco logs:)
        - **Huevo:** Por supuesto. Yo uso logs que ya me dejaste.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Huevo:** Aquí tienes. Mira mi mapa.
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Huevo:** Hmm, tengo ojos agudos, puedo ver muy lejos. Puedo informarle sobre todas las balizas encendidas en ambas direcciones desde aquí. Pero el pequeño guacamayo flappy puede ver mucho más lejos aún.
    - **Player:** ¿Guacamaya Flappy?
    - **Huevo:** Si le traes a Egg una pequeña guacamaya flappy, ¡te cuento todo lo que quieras saber sobre TODAS las balizas!
    - **Huevo:** El guacamayo puede volar alto en el aire y ver a larga distancia. Son lo suficientemente inteligentes como para informar sobre cosas muy lejanas.
    - ((Si el player tiene una bolsa de guacamayo en su backpack:))
      - **Huevo:** Tienes guacamayo ahí en tu mochila. Le das guacamayo, te hablo de otras balizas.
      - (continue|macaw)
  - [Choice]: ¿Cómo te va?
    - **Player:** ¿Cómo te va?
    - **Huevo:** ¡Oh, va genial! Bonita montaña rocosa. Tierra agradable y pintoresca. Lo mejor de todo es que es un día agradable y tranquilo; hasta el momento no hay peligro a la vista, aunque no dejo de mirar.
    - **Player:** Entonces, ¿qué estás haciendo exactamente aquí arriba, solo?
    - **Huevo:** Oh, yo vigilo muy de cerca el horizonte; es un trabajo muy importante, vigilar al rey.
    - **Player:** ¿Nunca te sientes solo?
    - **Huevo:** Oh, para nada. Hay muchas piedras y palos con quienes hablar; son una muy buena compañía.
    - **Player:** ¿Hablas con piedras y palos?
    - **Egg:** Sí, son muy buenos oyentes.
    - **Player:** Bueno, no puedo discutir eso.
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Huevo:** Adiós guarida, pequeño humano.

### Using a macaw pouch on Egg


#### Antes de darle a Egg una bolsa de guacamaya{{Anchor|macaw}}

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=a macaw pouch)
    - **Huevo:** Gracias. Guacamayo ayúdame a contarte más sobre las otras balizas.
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Huevo:** Bien.

#### Después de darle a Egg una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; ella no necesita otra.

### Using logs on Egg

- (Condition: Si la baliza está apagada:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: Si la baliza está muriendo:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: Si la baliza no muere:)
  - (Condition: Si Egg no tiene cinco logs:)
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
  - (Condition: Si Egg tiene cinco logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Huevo:** ¡Oye! ¡Aléjate de eso! Hasta que no hayas demostrado que eres un verdadero aliado de Varrock, ¡no podrás usar eso!
- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
