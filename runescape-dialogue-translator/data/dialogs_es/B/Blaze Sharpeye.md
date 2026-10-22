# Blaze Sharpeye

- **Original Wiki Page**: [Transcript:Blaze Sharpeye](https://runescape.wiki/w/Transcript%3ABlaze%20Sharpeye)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### Antes de que todos se enciendan

- **Player:** ¡Hola! ¿Te importaría que te preguntara qué es exactamente lo que estás haciendo... y qué es ese gran artilugio de ahí?
- **Blaze Sharpeye:** Oh, me temo que es un asunto ultrasecreto, muy importante y muy secreto. No puedo decirte de qué se trata, pero si pudiera...
- **Blaze Sharpeye:** Les contaría todo sobre esta increíble nueva red de balizas que estamos creando para protegernos contra las crecientes amenazas en Morytania y Wilderness. Ups, ¿dije eso en voz alta?
- **Player:** Sí. Sí, lo hiciste.
- (Condition: If the player has 43 Firemaking:)
  - **Blaze Sharpeye:** Sabes, parece que eres bastante hábil con el viejo polvorín. Dime, ¿tienes un deseo ardiente de prender fuego a las cosas?
  - **Player:** Eh... ¿tal vez?
  - **Blaze Sharpeye:** Bueno, entonces, ¡quizás seas el [man/woman] para nosotros!
  - **Player:** Mmm, está bien...
  - **Blaze Sharpeye:** Si alguna vez estás buscando trabajo, ¿por qué no charlas con King Roald en Varrock? Dile que yo te envié y quizás te ayude con algo.
  - **Player:** Gracias por eso; Lo tendré en cuenta.
- (Condition: If the player is below 43 Firemaking:)
  - **Blaze Sharpeye:** Bueno, finge que no escuchaste nada, ¿eh? Como un favor a tu viejo amigo Blaze. Mientras tanto, si conoces a alguien con una habilidad particular para Firemaking, ¿me lo enviarías? Me vendría bien una mano, jeje.
  - [Menu]: Selecciona una opción
    - [Choice]: ¿Puedo ayudar?
      - **Blaze Sharpeye:** No hasta que tengas un poco más de mirada pirománica en tus ojos. Frota algunos palos y practica un poco más. Si aún quieres ayudar después de eso, habla con King Roald.
      - Necesitas un nivel Firemaking de al menos 43 para iniciar All Fired Up.
    - [Choice]: Vale, claro.
      - **Player:** Está bien, claro.

#### Después de todo entusiasmado


##### Diálogo por primera vez

- **Blaze Sharpeye:** ¡Hola, Player! Has vuelto por más, ¿verdad?
- **Player:** Bueno, King Roald dijo que te vendría bien un poco de ayuda para realizar pruebas serias a toda la red de balizas.
- **Blaze Sharpeye:** ¡Podríamos alguna vez! Hay catorce balizas en total, que abarcan los límites sur y oeste de Wilderness. Lo que realmente necesitamos es que alguien intente mantener encendidas tantas balizas como sea posible, todas al mismo tiempo.
- **Blaze Sharpeye:** Debo advertirte: no es tan fácil como parece: algunas balizas son más difíciles de encender que otras y es posible que haya problemas candentes que tengas que resolver antes de poder acceder a cada baliza.
- **Blaze Sharpeye:** Sin embargo, cuantas más pruebas hagamos, más preparados estaremos en caso de adversidad.
- **Blaze Sharpeye:** Si estás interesado en ayudar, te sugiero que planifiques una ruta y luego la pruebes una o dos veces, solo para asegurarte de que puedes llegar a donde necesitas y que tienes todo lo que necesitas.
- **Blaze Sharpeye:** Requiere algunas habilidades especializadas, pero serás bien recompensado. Por no hablar de la satisfacción laboral. No sólo estás haciendo un gran servicio para los reinos del sur, sino que...
- **Player:** ¿Pero?
- **Blaze Sharpeye:** ¡Pero qué podría ser mejor que dedicar cada momento de la vida a iniciar GRANDES Y LARGAS LÍNEAS DE FUEGO!
- **Player:** Eh, ¿Blaze?
- **Blaze Sharpeye:** Ejem. Lo siento. Entonces, sí. ¿Tiene alguna pregunta candente para mí?
- (continue|standard)

##### Diálogo posterior

- **Blaze Sharpeye:** ¡Hola, Player! ¿Tiene alguna pregunta candente para mí hoy?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: If the beacon is unlit:)
      - **Blaze Sharpeye:** Por supuesto. Una vez que la baliza esté encendida, déjame 5 logs y yo me ocuparé del fuego todo el tiempo que pueda.
    - (Condition: If the beacon is dying:)
      - **Blaze Sharpeye:** Bueno, podría, pero ya que estás aquí, es mejor que lo hagas tú mismo.
    - (Condition: If the beacon is not dying:)
      - (Condition: If Blaze Sharpeye does not have five logs:)
        - (Condition: If the player does not have at least five logs of the same type:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Blaze Sharpeye:** Me temo que no tienes suficiente registro del tipo correcto para que yo lo use.
        - (Condition: If the player has at least five logs of the same type:)
          - (Condition: If the confirmation prompt is enabled:)
            - **Blaze Sharpeye:** Necesitaré cinco logs para poder atender el fuego. ¿Está bien?
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Blaze Sharpeye:** ¡Gracias! Usaré estos cinco logs para mantener encendida la baliza mientras estás fuera.
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Blaze Sharpeye:** Bueno, ya sabes dónde estoy si cambias de opinión.
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: If the confirmation prompt is disabled:)
            - (above|talk-give-logs)
      - (Condition: If Blaze Sharpeye has five logs:)
        - **Blaze Sharpeye:** Por supuesto que lo haré, no te preocupes. Usaré el logs que ya me dejaste.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Blaze Sharpeye:** ¡Pero claro! Sólo echa un vistazo a mi mapa.
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Blaze Sharpeye:** Puedo informarte del estado de las balizas en ambas direcciones, hasta los últimos fuegos que se encienden.
    - **Blaze Sharpeye:** Probablemente también podría contarte sobre las otras balizas, pero necesitaría la ayuda de una guacamaya.
    - **Player:** ¿Una guacamaya?
    - **Blaze Sharpeye:** Sí. Los guacamayos tienen la capacidad de volar muy alto en el aire y ver cosas que están mucho más lejos.
    - **Blaze Sharpeye:** También son muy inteligentes y se les puede entrenar para proporcionar la información exacta que necesito para obtener una descripción completa de la red de balizas.
    - ((If the player has a macaw pouch in their backpack:))
      - **Blaze Sharpeye:** Ahora que lo pienso, la guacamaya que tienes en tu mochila sería perfecta.
      - (continue|macaw)
  - [Choice]: Tengo algunas otras preguntas para ti.
    - **Player:** Tengo otras preguntas para ti.
    - **Blaze Sharpeye:** ¡Fuego a voluntad!
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Puedes explicar qué se supone que debo hacer de nuevo?
        - **Player:** ¿Puedes explicar qué se supone que debo hacer otra vez?
        - **Blaze Sharpeye:** ¡Pero claro! Esencialmente, a King Roald realmente le gustaría realizar pruebas serias a toda la red de balizas.
        - **Blaze Sharpeye:** Hay catorce balizas en total, que abarcan los límites sur y oeste de Wilderness. Lo que realmente necesitamos es que alguien intente mantener encendidas tantas balizas como sea posible, todas al mismo tiempo.
        - **Blaze Sharpeye:** Debo advertirte: no es tan fácil como parece: algunas balizas son más difíciles de encender que otras y es posible que haya problemas candentes que tengas que resolver antes de poder acceder a cada baliza.
        - **Blaze Sharpeye:** Sin embargo, cuantas más pruebas hagamos, más preparados estaremos en caso de adversidad.
        - **Blaze Sharpeye:** Si estás interesado en ayudar, te sugiero que planifiques una ruta y luego la pruebes una o dos veces, solo para asegurarte de que puedes llegar a donde necesitas y que tienes todo lo que necesitas.
        - **Blaze Sharpeye:** Requiere algunas habilidades especializadas, pero serás bien recompensado. Por no hablar de la satisfacción laboral. No sólo estás haciendo un gran servicio para los reinos del sur, sino que...
        - **Player:** ¿Pero?
        - **Blaze Sharpeye:** ¡Pero qué podría ser mejor que dedicar cada momento de la vida a iniciar GRANDES Y LARGAS LÍNEAS DE FUEGO!
        - **Player:** Eh, ¿Blaze?
        - **Blaze Sharpeye:** Ejem. Lo siento.
      - [Choice]: ¿Hace alguna diferencia qué tipo de logs uso?
        - **Player:** ¿Hace alguna diferencia qué tipo de logs uso?
        - **Blaze Sharpeye:** ¡Por supuesto que sí! El fuego de una baliza permanecerá encendido durante un tiempo determinado, dependiendo del tipo de tronco que utilices en ella.
        - **Blaze Sharpeye:** En general, cuanto más difícil sea encender un tronco, más tiempo arderá en la baliza.
        - **Player:** ¿De cuánto tiempo estamos hablando aquí?
        - **Blaze Sharpeye:** Bueno, una baliza cargada con logs normal arderá durante aproximadamente diez minutos, pero una baliza cargada con magic logs arderá durante unos veinte minutos.
        - **Blaze Sharpeye:** Entonces, si quieres que una baliza se queme durante mucho tiempo, es mejor que uses logs, que son más difíciles de encender.
        - **Player:** ¿Qué pasa cuando le doy logs a un bombero para que lo queme por mí? ¿Importa entonces el tipo de tronco?
        - **Blaze Sharpeye:** Sí, hasta cierto punto. Si cuida el fuego usted mismo, sospecho que obtendrá un resultado ligeramente mejor, sin importar qué tipo de tronco utilice.
        - **Blaze Sharpeye:** Sin embargo, si nos deja su logs, haremos todo lo posible por usted. Todos tenemos bastante experiencia en el cuidado de incendios, pero hay mucho que podemos hacer.
      - [Choice]: ¿Puedes hablarme sobre las recompensas?
        - **Player:** ¿Puedes contarme sobre las recompensas?
        - **Blaze Sharpeye:** Creo que King Roald ofrece recompensas por mantener seis, diez y catorce balizas encendidas simultáneamente.
        - **Blaze Sharpeye:** Una baliza cuenta como encendida si está en estado de llamas o si se está apagando. Si logras mantener seis, diez o catorce balizas en cualquiera de esos dos estados al mismo tiempo, habla con King Roald para reclamar tu recompensa.
        - **Seleccione una opción**
          - [Choice]: ¿Qué tipo de recompensas ofrece?
            - **Player:** ¿Qué tipo de recompensas ofrece? ¿Algo bueno?
            - **Blaze Sharpeye:** ¡Pues sí, de hecho!
            - ((If the player has not already claimed the ring of fire:))
              - [Cuando mantienes seis balizas encendidas simultáneamente, King Roald te dará un timbre que te ayudará cuando Firemaking.]
              - (continue)
            - ((If the player has already claimed the ring of fire:))
              - [Ya has reclamado el Anillo de Fuego por mantener seis balizas encendidas simultáneamente. Este anillo puede ayudarte cuando Firemaking.]
              - (continue)
            - ((If the player has not already claimed the flame gloves:))
              - [Cuando mantengas diez balizas encendidas simultáneamente, King Roald te dará un par de guantes. Estos también son de ayuda cuando Firemaking y funcionan muy bien en combinación con Ring of Fire.]
              - (continue)
            - ((If the player has already claimed the flame gloves:))
              - [Ya has reclamado los guantes de llamas por mantener diez balizas encendidas simultáneamente. Estos también son de ayuda cuando Firemaking y funcionan bien en combinación con el Anillo de Fuego.]
              - (continue)
            - ((If the player has not already claimed the inferno adze:))
              - [Cuando mantengas las catorce balizas encendidas simultáneamente, King Roald te dará el Inferno Adze. Este artículo puede ser de gran utilidad cuando Woodcutting, Firemaking o Mining.]
              - (continue)
            - ((If the player has already claimed the inferno adze:))
              - [Ya lograste mantener las catorce balizas encendidas simultáneamente y, como resultado, recibiste el Inferno Adze. Este elemento puede resultar de gran utilidad cuando se utiliza Woodcutting, Firemaking o Mining.]
              - (continue)
            - **Player:** ¿Puedo reclamar más de uno de cada uno de estos artículos?
            - **Blaze Sharpeye:** ¿Por qué necesitarías hacerlo? No se pueden usar, digamos, dos pares de guantes al mismo tiempo.
            - **Blaze Sharpeye:** Más te agobiaría cuando intentas... ¡PONER FUEGO A LAS COSAS!
            - **Player:** Entonces, ¿la respuesta es 'no'?
            - **Blaze Sharpeye:** ¡FUEGO!
            - **Player:** Correcto.
            - **Blaze Sharpeye:** ¿Tienes más preguntas sobre las recompensas?
            - (previous|rewards)
          - [Choice]: ¿Cómo reclamo mi recompensa?
            - **Player:** ¿Cómo reclamo mi recompensa?
            - **Blaze Sharpeye:** Simplemente habla con King Roald en Varrock Palace una vez que hayas mantenido la cantidad correcta de balizas encendidas; él te solucionará de inmediato.
            - **Blaze Sharpeye:** ¿Tienes más preguntas sobre las recompensas?
            - (previous|rewards)
          - [Choice]: ¿Qué pasa si pierdo un artículo de recompensa?
            - **Player:** ¿Qué pasa si pierdo un artículo de recompensa? ¿Podré reclamarlo de nuevo?
            - **Blaze Sharpeye:** Sospecho que tendrás que repetir la prueba. King Roald no es de los que regalan.
            - **Blaze Sharpeye:** ¿Tienes más preguntas sobre las recompensas?
            - (previous|rewards)
          - [Choice]: Eso es todo lo que necesito saber, gracias.
            - **Player:** Eso es todo lo que necesito saber, gracias.
            - **Blaze Sharpeye:** ¡En cualquier momento!
      - [Choice]: ¿Podemos hablar de advertencias?
        - **Blaze Sharpeye:** Lanzamos ofertas para que sean útiles, pero no queremos molestarlo con conversaciones innecesarias cuando está ocupado con asuntos urgentes.
        - **Blaze Sharpeye:** Si lo deseas, podemos avisarte antes de que uses logs en las balizas o darnos una pila de logs para cuidar las balizas, o simplemente podemos quedarnos callados.
        - **Blaze Sharpeye:** ¿Qué prefieres?
        - [Menu]: Avisarme sobre...
          - [Choice]: ¡Todo!
            - **Player:** ¡Avísame de todo!
            - **Blaze Sharpeye:** ¡Lo haré! Si cambias de opinión, házmelo saber.
          - [Choice]: Usar logs en balizas, pero no dar logs para disparar licitaciones.
            - **Player:** Adviérteme sobre el uso de logs en balizas, pero no sobre el uso de logs para disparar embarcaciones.
            - **Blaze Sharpeye:** ¡Lo haré! Si cambias de opinión, házmelo saber.
          - [Choice]: Dar logs para disparar licitaciones, pero no usar logs en balizas.
            - **Player:** Adviérteme sobre dar logs para disparar embarcaciones, pero no sobre usar logs en balizas.
            - **Blaze Sharpeye:** ¡Lo haré! Si cambias de opinión, házmelo saber.
          - [Choice]: ¡Nada!
            - **Player:** ¡Avísame de nada!
            - **Blaze Sharpeye:** ¡Lo haré! Si cambias de opinión, házmelo saber.
      - [Choice]: ¿Por qué tu voz se vuelve pegajosa cuando hablas de Squire Fyre?
        - **Player:** ¿Por qué tu voz se vuelve pegajosa cuando hablas de Squire Fyre?
        - **Blaze Sharpeye:** Oh, solo pensar en su brillo y chispa ilumina mi vida. Se toma muy en serio hacer fuego: es un brillante ejemplo para todos nosotros.
        - **Blaze Sharpeye:** No le dirás una palabra a nadie, ¿verdad? Es un poco...*ascua*-rascadora.
        - **Player:** Eso fue horrible.
        - **Blaze Sharpeye:** Lo sé, lo sé. A veces simplemente no puedo evitarlo.
        - **Player:** No, en serio, eso fue realmente malo.
        - **Blaze Sharpeye:** Lo siento mucho.
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Blaze Sharpeye:** ¿Entonces vamos a encender algunos fuegos? Brillante. ¡Eres un [man/woman] según mi propio corazón!

### Using a macaw pouch on Blaze Sharpeye


#### Antes de darle a Blaze Sharpeye una bolsa de guacamaya{{Anchor|macaw}}

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=a macaw pouch)
    - **Blaze Sharpeye:** Muchas gracias. Esta guacamaya me ayudará a brindarles información más detallada sobre la red de balizas.
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Blaze Sharpeye:** Haz lo que quieras.

#### Después de darle a Blaze Sharpeye una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; él no necesita otro.

### Using logs on Blaze Sharpeye

- (Condition: If the beacon is unlit:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: If the beacon is dying:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: If the beacon is not dying:)
  - (Condition: If Blaze Sharpeye does not have five logs:)
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
  - (Condition: If Blaze Sharpeye has five logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed

- **Blaze Sharpeye:** ¡Oye! ¡Aléjate de eso! Hasta que no hayas demostrado que eres un verdadero aliado de Varrock, ¡no podrás usar eso!
- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
