# Squire Fyre

- **Original Wiki Page**: [Transcript:Squire Fyre](https://runescape.wiki/w/Transcript%3ASquire%20Fyre)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### En mundos gratuitos

- **Player:** Hola. ¿Puedo preguntarte sobre-?
- **Squire Fyre:** ¡Me temo que no por el momento! No es lo suficientemente seguro hablar ahora.
- **Player:** ¡Pero ni siquiera sabes lo que iba a preguntar!
- **Squire Fyre:** Oh, tengo una idea suficiente para saber que no es lo suficientemente seguro hablar de ello en un mundo libre.

#### Antes de que todos se enciendan

- **Player:** Entonces, tengo curiosidad. ¿Qué estás haciendo aquí arriba y qué es ese artilugio tan interesante?
- **Squire Fyre:** Bueno, todo es parte de la nueva iniciativa de seguridad de King Roald.
- **Player:** ¿Iniciativa de seguridad? Eso suena intrigante. ¿Qué está sucediendo?
- **Squire Fyre:** Me temo que no puedo discutirlo en detalle en este momento, pero si estás interesado, habla con el rey. Lo último que supe es que necesitábamos algunas manos extra.
- **Player:** Gracias, tal vez.

#### Después de todo entusiasmado

- **Squire Fyre:** ¡Hola de nuevo! ¿Y qué podría hacer por ti hoy?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: Si la baliza está apagada:)
      - **Squire Fyre:** Por supuesto. Una vez que la baliza esté encendida, déjame 5 logs y yo me ocuparé del fuego todo el tiempo que pueda.
    - (Condition: Si la baliza está muriendo:)
      - **Squire Fyre:** Bueno, podría, pero ya que estás aquí, es mejor que lo hagas tú mismo.
    - (Condition: Si la baliza no muere:)
      - (Condition: Si Squire Fyre no tiene cinco logs:)
        - (Condition: Si el player no tiene al menos cinco logs del mismo tipo:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Squire Fyre:** Me temo que no tienes suficiente registro del tipo correcto para que yo lo use.
        - (Condition: Si el player tiene al menos cinco logs del mismo tipo:)
          - (Condition: Si el mensaje de confirmación está habilitado:)
            - **Squire Fyre:** Necesitaré cinco logs para poder atender el fuego. ¿Está bien?
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Squire Fyre:** ¡Gracias! Usaré estos cinco logs para mantener encendida la baliza mientras estás fuera.
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Squire Fyre:** Bueno, ya sabes dónde estoy si cambias de opinión.
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: Si el mensaje de confirmación está deshabilitado:)
            - (above|talk-give-logs)
      - (Condition: Si Squire Fyre tiene cinco logs:)
        - **Squire Fyre:** Por supuesto que lo haré; no te preocupes. Usaré el logs que ya me dejaste.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Squire Fyre:** ¡Pero claro! Sólo echa un vistazo a mi mapa.
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Squire Fyre:** Puedo informarte del estado de las balizas en ambas direcciones, hasta los últimos fuegos que se encienden.
    - **Squire Fyre:** Probablemente también podría contarte sobre las otras balizas, pero necesitaría la ayuda de una guacamaya.
    - **Player:** ¿Una guacamaya?
    - **Squire Fyre:** Sí. Los guacamayos tienen la capacidad de volar muy alto en el aire y ver cosas que están mucho más lejos.
    - **Squire Fyre:** También son muy inteligentes y se les puede entrenar para proporcionar la información exacta que necesito para obtener una descripción completa de la red de balizas.
    - ((Si el player tiene una bolsa de guacamayo en su backpack:))
      - **Squire Fyre:** Ahora que lo pienso, la guacamaya que tienes en tu mochila sería perfecta.
      - (continue|macaw)
  - [Choice]: ¿Cómo te va?
    - **Player:** ¿Cómo te va?
    - **Squire Fyre:** Muy bien, gracias. Estamos muy agradecidos por su ayuda para probar la red de balizas.
    - **Player:** Oh, no fue gran cosa. Tú estás haciendo la mayor parte del trabajo duro, haciendo guardia de esa manera.
    - **Squire Fyre:** Para ser honesto, tenía la intención de convertirme en 'Arcanista', pero debido a un error administrativo, terminé siendo propuesto como 'Incendiario'.
    - **Player:** Imagínate.
    - **Squire Fyre:** Aún así, las cosas salieron bien. Es un gran honor desempeñar un papel tan importante en la protección del reino.
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Squire Fyre:** Adiós, entonces. Vuelve a visitarnos si estás en el vecindario: es bueno tener compañía.

### Using a macaw pouch on Squire Fyre


#### Antes de darle a Squire Fyre una bolsa de guacamaya{{Anchor|macaw}}

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=a macaw pouch)
    - **Squire Fyre:** Muchas gracias. Esta guacamaya me ayudará a brindarles información más detallada sobre la red de balizas.
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Squire Fyre:** Haz lo que quieras.

#### Después de darle a Squire Fyre una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; ella no necesita otra.

### Using logs on Squire Fyre

- (Condition: Si la baliza está apagada:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: Si la baliza está muriendo:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: Si la baliza no muere:)
  - (Condition: Si Squire Fyre no tiene cinco logs:)
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
  - (Condition: Si Squire Fyre tiene cinco logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
