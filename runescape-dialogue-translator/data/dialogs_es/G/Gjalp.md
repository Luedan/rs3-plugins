# Gjalp

- **Original Wiki Page**: [Transcript:Gjalp](https://runescape.wiki/w/Transcript%3AGjalp)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### En mundos gratuitos

- Debes estar en un mundo de miembros para acceder a este contenido.
- (pop-up)
  - (Pop-up: You need to be on a members' world to access this content.|colour=#EBE0BC|shadow=no)

#### Antes de que todos se enciendan

- **Gjalp:** Estoy ocupado aquí. No hay tiempo para charlar.
- **Player:** No me pareces ocupado.
- **Gjalp:** Qué poco entiendes.
- **Player:** ¿Exactamente qué es lo que no entiendo entonces?
- **Gjalp:** Se tarda demasiado en explicarlo.
- **Player:** Bueno, no tengo nada urgente que hacer. Por favor, explícalo.
- **Gjalp:** No vale la pena. ¡Me molestas, vete!
- **Player:** Bien, te veré más tarde, ¿de acuerdo?
- **Gjalp:** ¡Vete!
- **Player:** ¡Adiós!
- **Gjalp:** ¡VAYA!

#### Después de todo entusiasmado


##### Sin haber completado la Fortaleza de Seguridad

- **Gjalp:** Me haces perder el tiempo.
- **Player:** ¿Perdón?
- **Gjalp:** Necesito mantener los ojos bien abiertos en el horizonte, no hablar con gente como tú.
- **Player:** ¡Pero estoy aquí para ayudar a probar la red de balizas para King Roald!
- **Gjalp:** ¿Tú? ¿Tú que no sabes nada de seguridad?
- **Player:** Bu-
- **Gjalp:** ¡Sin peros! Vas a ganar algo de experiencia del mundo que te rodea, *luego* vuelves para hablar de ayudar.
- [Stronghold of Security].}}

##### Habiendo completado la Fortaleza de Seguridad

- **Gjalp:** Hola. ¿Lo que quieras?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: If the beacon is unlit:)
      - **Gjalp:** Por supuesto. Una vez que enciendas la baliza, dame 5 logs y haré que el fuego arda por mucho tiempo.
    - (Condition: If the beacon is dying:)
      - **Gjalp:** Sólo me ocupo del fuego ardiente. ¡Tú mismo te ocupas del fuego moribundo!
    - (Condition: If the beacon is not dying:)
      - (Condition: If Gjalp does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Gjalp:** ¿Cómo esperas que te atienda el fuego? ¡No tienes suficiente logs bueno para que yo lo use!
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Gjalp:** Necesito cinco logs para cuidar el fuego por ti. ¿Bueno?
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Gjalp:** Gracias. Utilizo estos cinco logs para mantener la baliza encendida mientras estás fuera.
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Gjalp:** Hmph. Sabes dónde estoy si cambias de opinión.
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Gjalp has five logs:)
        - **Gjalp:** Por supuesto. Yo uso logs que me dejaste antes.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Gjalp:** Sí. Echa un vistazo a mi mapa.
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Gjalp:** Mmm. Mis ojos están bien. Puede informarle sobre todas las balizas en cualquier dirección, siempre que estén encendidas.
    - **Gjalp:** También podría contarte sobre las otras balizas, si tengo la ayuda de un guacamayo.
    - **Player:** ¿Una guacamaya?
    - **Gjalp:** Sí. El guacamayo puede volar alto en el aire y ver a larga distancia. También son criaturas muy inteligentes.
    - **Gjalp:** El guacamayo puede volar por el aire y luego informar sobre toda la red de balizas.
    - ((If the player does not have a macaw pouch in their backpack:))
      - **Gjalp:** Si me das una guacamaya, también puedo contarte sobre otras balizas.
    - ((If the player has a macaw pouch in their backpack:))
      - **Gjalp:** Oye, estás sosteniendo una guacamaya, justo ahí. Le das guacamayo, te hablo de otras balizas también.
      - (continue|macaw)
  - [Choice]: ¿Cómo te va?
    - **Player:** ¿Cómo te va?
    - **Gjalp:** Muy, muy tranquilo. No hay peligro a la vista.
    - **Player:** ¡Eso es genial!
    - **Gjalp:** Al contrario. ¡Entonces cuando el peligro sea mayor! No hay nada más peligroso que el peligro que uno no puede ver ni oír.
    - **Gjalp:** Ahora, a menos que tengas buenas preguntas, vete. Debo mirar y escuchar.
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Gjalp:** ¡Entonces déjame en paz! Tengo cosas más importantes que hacer que escucharte seguir hablando.

### Using a macaw pouch on Gjalp


#### Antes de darle a Gjalp una bolsa de guacamaya{{Anchor|macaw}}

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=a macaw pouch)
    - **Gjalp:** Muchas gracias. Esta guacamaya me ayudará a brindarles información más detallada sobre la red de balizas.
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Gjalp:** Haz lo que quieras.

#### Después de darle a Gjalp una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; ella no necesita otra.

### Using logs on Gjalp

- (Condition: If the beacon is unlit:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: If the beacon is dying:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: If the beacon is not dying:)
  - (Condition: If Gjalp does not have five logs:)
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
  - (Condition: If Gjalp has five logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Gjalp:** ¡Oye! ¡Aléjate de eso! Hasta que no hayas demostrado que eres un verdadero aliado de Varrock, ¡no podrás usar eso!
- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
