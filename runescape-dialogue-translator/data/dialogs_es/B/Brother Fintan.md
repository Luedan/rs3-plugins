# Brother Fintan

- **Original Wiki Page**: [Transcript:Brother Fintan](https://runescape.wiki/w/Transcript%3ABrother%20Fintan)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### En mundos gratuitos

- **Player:** Hola. ¿Puedo preguntarte sobre-?
- **Brother Fintan:** ¡Me temo que no por el momento! No es lo suficientemente seguro hablar ahora.
- **Player:** ¡Pero ni siquiera sabes lo que iba a preguntar!
- **Brother Fintan:** Oh, tengo una idea suficiente para saber que no es lo suficientemente seguro hablar de ello en un mundo libre.

#### Antes de que todos se enciendan

- **Player:** ¡Hola! ¿Qué podrías estar haciendo?
- **Brother Fintan:** Oh, estoy cuidando esta baliza para King Roald.
- **Player:** ¿Cómo te está yendo eso?
- **Brother Fintan:** Oh, muy bien, gracias. El tiempo fuera del Monasterio me ha dado la oportunidad de meditar y reflexionar sobre mi camino en la vida.
- **Player:** Eso suena muy satisfactorio espiritualmente.
- **Brother Fintan:** Así es, efectivamente. Es muy satisfactorio poder atender las necesidades espirituales de uno y al mismo tiempo servir al reino.

#### Después de todo entusiasmado


##### Sin 53 Prayer

- **Brother Fintan:** ¡Salve, viajero!
- **Player:** Sí, hola. Entonces me preguntaba si podrías ayudarme...
- **Brother Fintan:** ¡Pero claro que podría, peregrino! Parece como si realmente le vendría bien un poco de orientación.
- **Player:** ¡Excelente! Entonces, aquí está el problema:
- **Brother Fintan:** Ah, pero el problema es obvio; ¡Necesitas desarrollo espiritual!
- **Player:** Pero, la playa
- **Brother Fintan:** Estoy cuidando la baliza, [brother/sister]. No te preocupes por eso. Concéntrate en tu desarrollo interior: eso es lo más importante.
- [53] Prayer antes de Brother Fintan estarán dispuestos a hablar contigo sobre asuntos no espirituales.}}

##### Con 53 Prayer o más

- **Brother Fintan:** ¡Salve, viajero! ¿Le puedo ayudar en algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: If the beacon is unlit:)
      - **Brother Fintan:** Por supuesto. Una vez que la baliza esté encendida, déjame 5 logs y yo me ocuparé del fuego todo el tiempo que pueda.
    - (Condition: If the beacon is dying:)
      - **Brother Fintan:** Bueno, podría, pero ya que estás aquí, es mejor que lo hagas tú mismo.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Brother Fintan does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Brother Fintan:** Me temo que no tienes suficiente registro del tipo correcto para que yo lo use.
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Brother Fintan:** Necesitaré cinco logs para poder atender el fuego. ¿Está bien?
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Brother Fintan:** ¡Gracias! Usaré estos cinco logs para mantener encendida la baliza mientras estás fuera.
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Brother Fintan:** Bueno, ya sabes dónde estoy si cambias de opinión.
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Brother Fintan has five logs:)
        - **Brother Fintan:** Por supuesto que lo haré; no te preocupes. Usaré el logs que ya me dejaste.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Brother Fintan:** ¡Ah, pero claro! Permíteme ayudarte mostrándote mi mapa.
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Brother Fintan:** Puedo informarte del estado de las balizas en ambas direcciones, hasta los últimos fuegos que se encienden.
    - **Brother Fintan:** Probablemente también podría contarte sobre las otras balizas, pero necesitaría la ayuda de una guacamaya.
    - **Player:** ¿Una guacamaya?
    - **Brother Fintan:** Sí. Los guacamayos tienen la capacidad de volar muy alto en el aire y ver cosas que están mucho más lejos.
    - **Brother Fintan:** También son muy inteligentes y se les puede entrenar para proporcionar la información exacta que necesito para obtener una descripción completa de la red de balizas.
    - ((If the player has a macaw pouch in their backpack:))
      - **Brother Fintan:** Ahora que lo pienso, la guacamaya que tienes en tu mochila sería perfecta, por ejemplo.
      - (continue|macaw)
  - [Choice]: ¿Cómo te va?
    - **Player:** ¿Cómo te va?
    - **Brother Fintan:** Oh, muy bien, gracias. El tiempo fuera del Monasterio me ha dado la oportunidad de meditar y reflexionar sobre mi camino en la vida.
    - **Player:** Eso suena muy satisfactorio espiritualmente.
    - **Brother Fintan:** Ciertamente lo es. Debo admitir que ha sido muy agradable pasar un rato al aire libre. El Monasterio es bastante sofocante en esta época del año, por no mencionar un poco aburrido.
    - **Player:** ¿Ah?
    - **Brother Fintan:** A veces, realmente desearía haberlo seguido de memoria al elegir una carrera, pero mi madre quería un monje en la familia. Le habría roto el corazón.
    - **Brother Fintan:** Oh, pero no le dirás al abad que lo dije, ¿verdad? Estaría muy decepcionado.
    - [Menu]: Selecciona una opción
      - [Choice]: Por supuesto que no lo haré.
        - **Player:** Por supuesto que no lo haré.
        - **Brother Fintan:** Te lo agradezco.
      - [Choice]: Aún no es demasiado tarde para dedicarse a otra profesión, ¿sabes?
        - **Player:** Aún no es demasiado tarde para empezar otra profesión, ¿sabes?
        - **Brother Fintan:** ¿De verdad lo crees?
        - **Player:** ¡Por supuesto!
        - **Brother Fintan:** Pero, mi querida madre...
        - **Player:** Bueno, ¿qué quiere decir que no puedes ser monje Y hacer otra cosa?
        - **Brother Fintan:** ¿Un monje y algo más? ¡Nunca había considerado eso!
        - **Player:** Por ejemplo, parece que actualmente estás haciendo un buen trabajo como monje y bombero profesional.
        - **Brother Fintan:** ¡Sabes, tienes razón! Gracias, Player, me has dado mucho en qué pensar. Estoy muy agradecido por tu consejo.
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Brother Fintan:** ¡Vaya, qué asertividad!

### Using a macaw pouch on Brother Fintan


#### Antes de darle a Brother Fintan una bolsa de guacamaya{{Anchor|macaw}}

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=a macaw pouch)
    - **Brother Fintan:** Muchas gracias. Esta guacamaya me ayudará a brindarles información más detallada sobre la red de balizas.
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Brother Fintan:** Haz lo que quieras.

#### Después de darle a Brother Fintan una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; él no necesita otro.

### Using logs on Brother Fintan

- (Condition: If the beacon is unlit:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: If the beacon is dying:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: If the beacon is not dying:)
  - (Condition: If Brother Fintan does not have five logs:)
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
  - (Condition: If Brother Fintan has five logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
