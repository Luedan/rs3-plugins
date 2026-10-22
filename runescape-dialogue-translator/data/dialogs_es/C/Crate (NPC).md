# Crate (NPC)

- **Original Wiki Page**: [Transcript:Crate (NPC)](https://runescape.wiki/w/Transcript%3ACrate%20%28NPC%29)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### En mundos gratuitos

- **Player:** Hola. ¿Puedo preguntarte sobre eso?
- **Crate:** No. Es demasiado secreto para hablar de ello ahora.
- **Player:** ¡Pero ni siquiera sabes lo que iba a preguntar!
- **Crate:** Sé lo suficiente como para saber que no es seguro hablar a menos que estemos en el mundo de los miembros.

#### Antes de que todos se enciendan

- **Crate:** ¿Qué haces aquí? ¡Nadie le dijo a Crate que esperara visitas!
- **Player:** ¿Eh? Espera, ¿qué está pasando aquí?
- **Crate:** No autorizado a decirlo. Es demasiado importante.
- **Player:** Bueno, parece que estás parado, soñando despierto con rocas.
- **Cajón:** Es mucho más importante, ¡y ultrasecreto! Caja de trolls demasiado importante para hablar con gente como tú.
- **Player:** Está bien, está bien. Nos vemos más tarde.

#### Después de todo entusiasmado


##### Antes de darle una anguila de las cavernas

- **Crate:** ¿Qué haces aquí? ¡Nadie le dijo a Crate que esperara visitas!
- **Player:** Estoy ayudando a King Roald a probar la red de balizas contra incendios.
- **Crate:** Hmph, nadie me cuenta nada sobre eso. Pero, mientras estés aquí, tal vez puedas ser de utilidad.
- **Player:** ¿Cómo es eso?
- **Cajón:** Tengo mucha hambre. Quiero un poco de anguila de lava. Tráeme un poco.
- **Player:** ¿Qué? ¡No soy un recado [boy/girl]! Estoy aquí para ayudar a probar estas balizas.
- **Crate:** Hablaremos de eso más tarde. Por ahora tengo hambre. ¿Me traes anguila de lava o no?
- [Menu]: Selecciona una opción
  - [Choice]: Bien, te traeré un poco de anguila de lava.
    - **Player:** Bien, te traeré un poco de anguila de lava.
    - **Caja:** Bien. Y date prisa. Es un asunto de gran importancia.
    - **Player:** Claro.
  - [Choice]: ¡Sigue soñando!
    - **Player:** ¡Sigue soñando!
    - **Crate:** Entonces vete, antes de que pierda los estribos.

##### Dándole una anguila de las cavernas

- **Cajón:** ¡Alto! ¿Quién va ahí?
- **Player:** Oh, no te preocupes, soy solo yo.
- **Crate:** ¿Te conozco? ¿Se supone que deberías estar aquí? Espera un momento, ¡huelo anguila! ¿Eso es para mí?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, es todo tuyo, si lo quieres.
    - **Player:** Sí, es todo tuyo, si lo quieres.
    - (Condition: If the player has both raw and cooked lava eels in backpack:)
      - [Menu]: ¿Qué anguila de lava quieres regalarle a Crate?
        - [Choice]: Crudo.
          - (abajo)
        - [Choice]: Cocido.
          - (abajo)
    - (Condition: If the player has either only raw or only cooked lava eels in backpack:)
      - (removes=raw lava eel or cooked lava eel)
      - **Cajón:** Muchas gracias. Anguila de lava, mi favorita.
      - **Player:** Me alegra que te guste.
      - **Cajón:** Muy agradecido. Si necesitas ayuda, házmelo saber.
  - [Choice]: No, es todo para mí.
    - **Player:** No, es todo para mí.
    - **Crate:** Entonces vete, antes de que pierda los estribos.

##### Después de darle una anguila de las cavernas

- **Crate:** Hola, ¿qué haces aquí otra vez? ¿Quieres algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: If the beacon is unlit:)
      - **Caja:** Sí. Una vez encendida la baliza, deja 5 logs conmigo y yo me encargo del fuego por un tiempo.
    - (Condition: If the beacon is dying:)
      - **Crate:** Podría, pero el fuego ya se está extinguiendo. Tú lo haces arder de nuevo y luego yo lo cuido por ti.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Crate does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Crate:** ¿Cómo puedo cuidar el fuego por ti? ¡No tienes suficiente logs bueno para que yo lo use!
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Caja:** Necesitas cinco logs para cuidar el fuego. ¿Está bien?
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Caja:** Gracias. Utilizo estos cinco logs para mantener la baliza encendida mientras estás fuera.
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Caja:** Bien. Sabes dónde estoy si cambias de opinión.
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Crate has five logs:)
        - **Caja:** Por supuesto. Yo uso el logs que ya dejaste aquí.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Crate:** Bueno, entonces mira mi mapa. Pero date prisa.
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Crate:** Hmm, tengo ojos agudos, puedo ver muy lejos. Puedo contarle todo sobre las balizas encendidas en ambas direcciones desde aquí. Pero el pequeño guacamayo flappy puede ver mucho más lejos aún.
    - **Player:** ¿Guacamaya Flappy?
    - **Crate:** Si le traes a Crate una pequeña guacamaya flappy, ¡te contaré todo lo que quieras saber sobre TODAS las balizas!
    - **Caja:** El guacamayo puede volar alto en el aire y ver a larga distancia. Son lo suficientemente inteligentes como para informar sobre cosas muy lejanas.
    - ((If the player has a macaw pouch in their backpack:))
      - **Caja:** Tienes guacamayo ahí en tu mochila. Le das guacamayo, te hablo de otras balizas también.
      - (continue|macaw)
  - [Choice]: ¿Cómo te va?
    - **Player:** ¿Cómo te va?
    - **Crate:** Hmm, la presión del trabajo es muy grande, pero soy fuerte y mis ojos son agudos. Sólo eligen trolls muy importantes para este tipo de trabajo.
    - **Player:** Debes sentirte muy orgulloso.
    - **Caja:** Por supuesto. Pero tener tantos trolls que me respetan y tener tanto trabajo que hacer me da mucha, mucha hambre.
    - **Player:** Hmm, debe ser difícil.
    - **Crate:** Oh, lo es. Alguien como tú nunca podría entenderlo.
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Caja:** Hmph.

### Using a macaw pouch on Crate


#### Antes de darle a Crate una bolsa de guacamaya{{Anchor|macaw}}

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=a macaw pouch)
    - **Cajón:** Gracias. Guacamayo ayúdame a contarte más sobre las otras balizas.
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Caja:** Bien.

#### Después de darle a Crate una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; él no necesita otro.

### Using logs on Crate

- (Condition: If the beacon is unlit:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: If the beacon is dying:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: If the beacon is not dying:)
  - (Condition: If Crate does not have five logs:)
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
  - (Condition: If Crate has five logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Caja:** ¡Oye! ¡Aléjate de eso! Hasta que no hayas demostrado que eres un verdadero aliado de Varrock, ¡no podrás usar eso!
- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
