# Fisherman (Fish Flingers)

- **Original Wiki Page**: [Transcript:Fisherman (Fish Flingers)](https://runescape.wiki/w/Transcript%3AFisherman%20%28Fish%20Flingers%29)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Fuera de la sala de espera

- (Condition: If you are on a free world:)
  - **Pescador:** Lo sentimos, tendrás que cambiar al mundo de miembros para poder jugar Fish Flingers.
  - (continue)
- (Condition: If Fish Flingers hasn't started yet, but you can teleport to the waiting area:)
  - **Pescador:** Fish Flingers comienza en [número] [minute/minutes].
  - (continue)
- (Condition: If you just missed Fish Flingers:)
  - **Pescador:** Me temo que te acabas de perder el inicio de una competencia de Lanzadores de Peces. La sala de espera para la próxima competición Fish Flingers se abre en 15 minutos. Si vuelves a hablarme entonces, te teletransportaré a la competencia.
  - (continue)
- (Condition: (If Fish Flingers won't start for several more minutes:)
  - **Pescador:** La zona de espera para la próxima competencia Fish Flingers se abre en [número] [minute/minutes]. Si vuelves a hablarme entonces, te teletransportaré a la competencia.
  - (continue)
- [Menu]: ¿Qué te gustaría decir?{{anchor|initial-select}}
  - [Choice]: cond=Only if a competition is about to start:|Teletransportame a Fish Flingers.
    - (Condition: Before the Dailyscape Overhaul update:)
    - **Pescador:** Cuando comience Fish Flingers, utilizarás uno de tus boletos de entrada, lo que te dejará con [número] boletos más. ¿Está bien?
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Sí, usaré un boleto para competir.
        - (Condition: If the competition has already started:)
          - **Pescador:** ¡Oh no! Me temo que la competencia Fish Flingers ha comenzado, así que no puedo teletransportarte. La próxima competición comienza en [número] minutos. Si vuelves a hablarme entonces, te teletransportaré a la competencia.
        - (Condition: If the competition hasn't started:)
          - (Action: el player es teletransportado a la zona de espera.)
      - [Choice]: No, he cambiado de opinión.
        - (end)
  - [Choice]: cond=Only if a competition is about to start:|Dame una pista para la próxima competición.
    - ((As below, then shows the initial options.))
  - [Choice]: cond=Only if there is no competition about to start soon:|¿Puedo participar en el concurso ahora?
    - (Condition: If you are on a free world:)
      - **Pescador:** Lo sentimos, tendrás que cambiar al mundo de miembros para poder jugar Fish Flingers.
      - (initial)
    - (Condition: If you are on a member's world:)
      - **Pescador:** La zona de espera para la próxima competencia Fish Flingers se abre en [número] minutos. Si vuelves a hablarme entonces, te teletransportaré a la competencia.
      - (initial)
  - [Choice]: Acerca de los arrojadores de pescado...
    - **Pescador:** ¿Qué te gustaría que te dijera?
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿De qué se trata la competencia?
        - **Pescador:** Es una oportunidad para que demuestres lo bien que puedes pescar eligiendo el mejor equipo y hábitat.
        - **Pescador:** Los veteranos conocemos un lugar especial, Isla Anglerine, donde parecen reunirse enormes bancos de peces inusuales.
        - **Pescador:** No estoy seguro de qué es lo que les resulta tan atractivo a los peces allí, ¡pero es un paraíso para los pescadores!
        - **Pescador:** Puedo teletransportarte a la isla si quieres participar. Sólo di la palabra.
        - (previous)
      - [Choice]: ¿Cómo pesco?
        - **Pescador:** Una vez que te haya teletransportado, espera en el área de inicio a que comience la competencia. Luego, camina hasta el paseo marítimo donde te gustaría pescar.
        - **Pescador:** A continuación, seleccione un anzuelo y un cebo que crea que le gustarán al pez, agregue algunos pesos para obtener la distancia de lanzamiento que necesita y estará listo para lanzar el sedal.
        - **Pescador:** A medida que pesques, se te mostrará qué tan efectivo es tu aparejo y podrás realizar mejoras a medida que aprendas qué le gusta a cada pez.
        - **Pescador:** Recuerde, diferentes especies tienen diferentes tamaños. Tendrás que intentar pescar en diferentes zonas para encontrar las especies más pesadas.
        - **Pescador:** También vale la pena recordar que los peces son criaturas adaptables, por lo que el aparejo que funciona bien en una competencia puede no funcionar tan bien en la siguiente.
        - (previous)
      - [Choice]: ¿Con qué frecuencia puedo competir?
        - (Condition: Before the Dailyscape Overhaul update:)
        - **Pescador:** A todo el mundo se le permiten 2 entradas cada día. Guardamos los billetes por usted, por lo que no es necesario llevarlos consigo ni guardarlos en su banco.
        - **Pescador:** Si quieres saber cuántos te quedan o quieres reclamar más boletos, dímelo.
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: ¿Cuántas entradas me quedan?
            - **Pescador:** Te quedan entradas [número] en este momento.
            - (previous)
          - [Choice]: ¿Cuándo podré reclamar las entradas?
            - (Condition: If enough time has passed:)
            - **Pescador:** Ha pasado suficiente tiempo desde la última vez que reclamaste boletos de entrada, por lo que podrás reclamar más tan pronto como hayas agotado los que te quedan.
            - (previous)
          - [Choice]: ¿Existe otra forma de conseguir entradas?
            - **Pescador:** Es curioso que preguntes eso. Recientemente tuvimos una tormenta feroz. El vendaval recogió una gran cantidad de entradas y las esparció por todo Gielinor.
            - **Pescador:** Recogimos todos los que pudimos encontrar, pero la mayoría terminó en el agua.
            - **Pescador:** Entonces, nunca se sabe. Es posible que encuentres un boleto de entrada cada vez que pesques.
            - (previous)
          - [Choice]: Hablemos de otra cosa...
            - (initial)
        - (Condition: After the Dailyscape Overhaul update:)
        - **Pescador:** ¡Tantas veces como quieras!
      - [Choice]: Sobre la puntuación de la competición...
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: Dame una copia de mi historial de competencia.
            - ((Without Fish Flingers scorecard in backpack:))
              - (Condition: Without one free backpack space:)
                - **Pescador:** No tienes espacio para cargarlo. No hay problema, solo pregúntame nuevamente cuando tengas un espacio libre en el inventario.
                - (previous)
              - (Condition: With one free backpack space:)
                - (receives=Fish Flingers scorecard)
                - [El pescador te entrega una tarjeta de puntuación de Fish Flingers.]
                - (previous)
            - (Condition: With Fish Flingers scorecard in backpack:)
              - **Pescador:** Parece que ya tienes uno en tu inventario.
              - (previous)
          - [Choice]: ¿Cómo se calcula mi puntuación?
            - **Pescador:** Tomamos en cuenta la cantidad de peces capturados, el peso total capturado y el pez más pesado capturado.
            - **Pescador:** También incluimos cuántos peces grandes pescaste y con qué frecuencia ayudaste a otros concursantes a pescar sus peces grandes.
            - **Pescador:** Encontrar el aparejo perfecto para cada especie es una parte importante de la pesca. Obtendrás puntos de bonificación por cada especie para la que encuentres el equipo perfecto.
            - **Pescador:** Sabrás que has encontrado el aparejo perfecto cuando tu calificación de captura de ese pez alcance el 100%.
            - **Pescador:** Después de la competencia se te mostrarán tus resultados, para que puedas ver qué tuvo un impacto en tu puntuación.
            - (previous)
          - [Choice]: Háblame de peces grandes.
            - **Pescador:** Mantén una calificación del 100% y eventualmente pescarás un pez grande y valioso. Los peces grandes son tan pesados ​​que necesitarás la ayuda de otros concursantes para sacarlos del agua.
            - **Pescador:** Capturar peces grandes mejora significativamente tu puntuación, pero ayudar a otros a pescar sus peces grandes te otorga la mayor recompensa de todas.
            - (previous)
          - [Choice]: Háblame de las medallas.
            - **Pescador:** Si te desempeñas lo suficientemente bien, recibirás hasta cuatro medallas, lo que te dará una bonificación a tu puntuación. El tablón de anuncios de la zona de espera describe las condiciones para ganar medallas.
            - (previous)
          - [Choice]: Hablemos de otra cosa...
            - (initial)
      - [Choice]: Hablemos de otra cosa...
        - (initial)
    - [Choice]: Muéstrame la tienda de recompensas.
      - ((Fish Flingers Reward Shop interface opens.))
  - [Choice]: Acerca de las recompensas...{{anchor|about-rewards}}
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Cuéntame sobre la recompensa de la experiencia Fishing.
        - **Pescador:** Descubrirás que la habilidad adicional que implica la pesca competitiva puede hacerte ganar más experiencia que la pesca diaria.
        - **Pescador:** Al final de cada competencia recibirás toda la experiencia que hayas obtenido, por lo que no es necesario que hables conmigo para recogerla.
        - **Pescador:** Puede que te lleve algunos intentos acostumbrarte al equipo de competición, pero una vez que hayas aprendido la mejor manera de encontrar y capturar las especies de peces más grandes, deberías notar una gran mejora en la experiencia que obtienes.
        - **Pescador:** La cantidad de experiencia que ganes depende de tu habilidad en Fishing. Tener un nivel Fishing más alto significa que ganas más experiencia.
        - (previous)
      - [Choice]: Me gustaría saber más sobre la recompensa por pescado crudo.
        - **Pescador:** Te daremos pescado crudo marcado, que es mucho más fácil de llevar al banco.
        - **Pescador:** Cuando reclames tu pez anotado, se te dará una selección de peces apropiada para tu nivel Fishing. Por ejemplo, si normalmente pescas pez espada, te darán una mezcla de pez espada y langostas.
        - (previous)
      - [Choice]: Cuéntame sobre la recompensa de la caja de aparejos.
        - **Pescador:** La caja de aparejos contiene equipos de pesca y pescado crudo, lo que le ahorra inventario y espacio en el banco. También tienen una copia de su historial de competencia, para que pueda revisar su desempeño.
        - **Pescador:** Es cierto que cuando adquieres tu caja de aparejos por primera vez no cabe mucho, pero con el tiempo puedes mejorarla para que aguante mucho más.
        - (previous)
      - [Choice]: Cuéntame sobre la recompensa del traje de pesca.
        - **Pescador:** El equipo de pesca aumenta la cantidad de experiencia Fishing que obtienes. Cuando estás pescando o jugando a Fish Flingers, es una buena idea usar tantas piezas del traje de pesca como sea posible.
        - (previous)
      - [Choice]: Hablemos de otra cosa.
        - (initial)

#### En la sala de espera

- (Condition: If there is more than a minute to the start:)
  - **Pescador:** Ya no falta mucho. La competición comienza en [número] [minute/minutes].
  - (continue)
- (Condition: If there is less than a minute to the start:)
  - **Pescador:** La competencia está por comenzar. ¡Divertirse!
  - (continue)
- [Menu]: ¿Qué te gustaría decir?
  - (Condition: Only if a competition is about to start:)
    - [Choice]: Dame una pista para la próxima competición.
      - ((As below, then shows the initial options.))
  - [Choice]: Acerca de los arrojadores de pescado...
    - **Pescador:** ¿Qué te gustaría que te dijera?
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿De qué se trata la competencia?
        - **Pescador:** Es una oportunidad para que demuestres lo bien que puedes pescar eligiendo el mejor equipo y hábitat.
        - **Pescador:** Aquí en Isla Anglerine, parecen reunirse enormes bancos de peces inusuales. No estoy seguro de qué es lo que les resulta tan atractivo a los peces aquí, ¡pero es un paraíso para los pescadores!
        - (previous)
      - [Choice]: ¿Cómo pesco?
        - **Pescador:** Cuando se abran las puertas, apresúrate a llegar a la costa donde quieras pescar.
        - **Pescador:** Puedes pescar en cualquiera de los muelles al este y al oeste, el lago al norte, el río al este del lago y la playa al extremo noreste.
        - **Pescador:** A continuación, seleccione un anzuelo y un cebo que crea que le gustarán al pez, agregue algunos pesos para obtener la distancia de lanzamiento que necesita y estará listo para lanzar el sedal.
        - **Pescador:** A medida que pesques, se te mostrará qué tan efectivo es tu aparejo y podrás realizar mejoras a medida que aprendas qué le gusta a cada pez.
        - **Pescador:** Recuerde, diferentes especies tienen diferentes tamaños. Tendrás que intentar pescar en diferentes zonas para encontrar las especies más pesadas.
        - **Pescador:** También vale la pena recordar que los peces son criaturas adaptables, por lo que el aparejo que funciona bien en una competencia puede no funcionar tan bien en la siguiente.
        - (previous)
      - [Choice]: ¿Con qué frecuencia puedo competir?
        - **Pescador:** A todo el mundo se le permiten 2 entradas cada día. Guardamos los billetes por usted, por lo que no es necesario llevarlos consigo ni guardarlos en su banco.
        - **Pescador:** Si quieres saber cuántos te quedan o quieres reclamar más boletos, dímelo.
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: ¿Cuántas entradas me quedan?
            - **Pescador:** Te quedan entradas [número] en este momento.
            - (previous)
          - [Choice]: ¿Cuándo podré reclamar las entradas?
            - **Pescador:** Ha pasado suficiente tiempo desde la última vez que reclamaste boletos de entrada, por lo que podrás reclamar más tan pronto como hayas agotado los que te quedan.
            - (previous)
          - [Choice]: ¿Existe otra forma de conseguir entradas?
            - **Pescador:** Es curioso que preguntes eso. Recientemente tuvimos una tormenta feroz. El vendaval recogió una gran cantidad de entradas y las esparció por todo Gielinor.
            - **Pescador:** Recogimos todos los que pudimos encontrar, pero la mayoría terminó en el agua.
            - **Pescador:** Entonces, nunca se sabe. Es posible que encuentres un boleto de entrada cada vez que pesques.
            - (previous)
          - [Choice]: Hablemos de otra cosa...
            - (initial)
      - [Choice]: Sobre la puntuación de la competición...
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: Dame una copia de mi historial de competencia.
            - (Condition: Without Fish Flingers scorecard in backpack:)
              - ((Without space in backpack:))
                - **Pescador:** No tienes espacio para cargarlo. No hay problema, solo pregúntame nuevamente cuando tengas un espacio libre en el inventario.
                - (previous)
              - ((With space in backpack:))
                - (receives=Fish Flingers scorecard)
                - [El pescador te entrega una tarjeta de puntuación de Fish Flingers.]
                - (previous)
            - ((With Fish Flingers scorecard in backpack:))
              - **Pescador:** Parece que ya tienes uno en tu inventario.
              - (previous)
          - [Choice]: ¿Cómo se calcula mi puntuación?
            - **Pescador:** Tomamos en cuenta la cantidad de peces capturados, el peso total capturado y el pez más pesado capturado.
            - **Pescador:** También incluimos cuántos peces grandes pescaste y con qué frecuencia ayudaste a otros concursantes a pescar sus peces grandes.
            - **Pescador:** Encontrar el aparejo perfecto para cada especie es una parte importante de la pesca. Obtendrás puntos de bonificación por cada especie para la que encuentres el equipo perfecto.
            - **Pescador:** Sabrás que has encontrado el aparejo perfecto cuando tu calificación de captura de ese pez alcance el 100%.
            - **Pescador:** Después de la competencia se te mostrarán tus resultados, para que puedas ver qué tuvo un impacto en tu puntuación.
            - (previous)
          - [Choice]: Háblame de peces grandes.
            - **Pescador:** Mantén una calificación del 100% y eventualmente pescarás un pez grande y valioso. Los peces grandes son tan pesados ​​que necesitarás la ayuda de otros concursantes para sacarlos del agua.
            - **Pescador:** Capturar peces grandes mejora significativamente tu puntuación, pero ayudar a otros a pescar sus peces grandes te otorga la mayor recompensa de todas.
            - (previous)
          - [Choice]: Háblame de las medallas.
            - **Pescador:** Si te desempeñas lo suficientemente bien, recibirás hasta cuatro medallas, lo que te dará una bonificación a tu puntuación. El tablón de anuncios de la zona de espera describe las condiciones para ganar medallas.
            - (previous)
          - [Choice]: Hablemos de otra cosa...
            - (initial)
      - [Choice]: Hablemos de otra cosa...
        - (initial)
    - [Choice]: Muéstrame la tienda de recompensas.
      - ((Fish Flingers Reward Shop interface opens.))
  - [Choice]: Sobre las recompensas...
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Cuéntame sobre la recompensa de la experiencia Fishing.
        - **Pescador:** Descubrirás que la habilidad adicional que implica la pesca competitiva puede hacerte ganar más experiencia que la pesca diaria.
        - **Pescador:** Al final de cada competencia recibirás toda la experiencia que hayas obtenido, por lo que no es necesario que hables conmigo para recogerla.
        - **Pescador:** Puede que te lleve algunos intentos acostumbrarte al equipo de competición, pero una vez que hayas aprendido la mejor manera de encontrar y capturar las especies de peces más grandes, deberías notar una gran mejora en la experiencia que obtienes.
        - **Pescador:** La cantidad de experiencia que ganes depende de tu habilidad en Fishing. Tener un nivel Fishing más alto significa que ganas más experiencia.
        - (previous)
      - [Choice]: Me gustaría saber más sobre la recompensa por pescado crudo.
        - **Pescador:** Te daremos pescado crudo marcado, que es mucho más fácil de llevar al banco.
        - **Pescador:** Cuando reclames tu pez anotado, se te dará una selección de peces apropiada para tu nivel Fishing. Por ejemplo, si normalmente pescas pez espada, te darán una mezcla de pez espada y langostas.
        - (previous)
      - [Choice]: Cuéntame sobre la recompensa de la caja de aparejos.
        - **Pescador:** La caja de aparejos contiene equipos de pesca y pescado crudo, lo que le ahorra inventario y espacio en el banco. También tienen una copia de su historial de competencia, para que pueda revisar su desempeño.
        - **Pescador:** Es cierto que cuando adquieres tu caja de aparejos por primera vez no cabe mucho, pero con el tiempo puedes mejorarla para que aguante mucho más.
        - (previous)
      - [Choice]: Cuéntame sobre la recompensa del traje de pesca.
        - **Pescador:** El equipo de pesca aumenta la cantidad de experiencia Fishing que obtienes. Cuando estás pescando o jugando a Fish Flingers, es una buena idea usar tantas piezas del traje de pesca como sea posible.
        - (previous)
      - [Choice]: Hablemos de otra cosa.
        - (initial)

### Teleport


#### Si Fish Flingers aún no ha comenzado, pero puedes teletransportarte a la zona de espera

- **Pescador:** Fish Flingers comienza en [número] minutos.
- (Action: el player es teletransportado a la zona de espera.)

#### Si Fish Flingers no se inicia durante varios minutos más

- **Pescador:** La zona de espera para la próxima competencia Fish Flingers se abre en [número] minutos. Si vuelves a hablarme entonces, te teletransportaré a la competencia.

### Claim reward

- ((Fish Flingers Reward Shop interface opens.))

#### Diálogo por primera vez

- **Pescador:** A todos les gusta ser recompensados por sus esfuerzos, por supuesto. Podrás recibir experiencia Fishing, pescado crudo, un equipo de pesca y, si eres lo suficientemente bueno, una caja de aparejos para guardar tus suministros de pesca.
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: Cuéntame más sobre las recompensas.
    - (continuea|about-rewards)
  - [Choice]: Muéstrame la tienda de recompensas.
    - ((Fish Flingers Reward Shop interface opens.))
  - [Choice]: Hablemos de otra cosa.
    - (Condition: Before the Dailyscape Overhaul update:)
      - **Pescador:** ¡Buenas noticias! Eres elegible para reclamar boletos de entrada. Ahora tienes entradas para [número] Fish Flingers. Vuelve mañana para reclamar más.
      - (continuea|initial-select)

#### Actualización de una caja de aparejos

- (Condition: With the previous tackle box in the bank:)
  - **Pescador:** Necesitarás conseguir tu caja de aparejos del banco antes de que pueda actualizarla.
- (Condition: With the previous tackle box in the inventory:)
  - (removes=previous tackle box) (receives=upgraded tackle box)
  - [La caja de aparejos de tu inventario se ha actualizado y ahora puede contener más artículos.]
  - (Condition: Upgrading to the Champion's tackle box:)
    - {{RSFontAchievement|Master Angler|Purchase the champion's tackle box from the Fish Flingers fisherman.}}
- (Condition: With the tackle box already fully upgraded:)
  - Ya posees la mejor caja de aparejos disponible.

### Get hint from


#### Si la competencia aún no ha comenzado


##### Si la zona de espera acaba de abrir

- **Pescador:** Todavía estamos ordenando lo de la última competencia. Dame un minuto y te daré esa pista.

##### Si la zona de espera ha estado abierta por un tiempo

- ((One of the following is shown:))
  - **Pescador:** Encontrarás salmón bolina en la playa. Han sido avistados lejos de la orilla, así que coloca muchos pesos en tu línea para alcanzarlos.
  - **Pescador:** Encontrarás lubinas en la playa. Son inteligentes y pueden detectar metales a un kilómetro de distancia. Será mejor que pienses detenidamente qué tipo de anzuelo utilizas.
  - **Pescador:** Encontrarás bacalao dardo en el río. Se sabe que les gustan los mariscos, especialmente los grises.
  - **Pescador:** Encontrarás bacalao dardo en el río. Han sido vistos cerca de la orilla, por lo que no necesitarás mucho peso en tu línea para alcanzarlos.
  - **Pescador:** Encontrarás arenque a la deriva en los muelles. Se les ha visto a bastante distancia de la orilla, pero no demasiado. Tendrás que colocar algunos pesos para alcanzarlos.
  - **Pescador:** Encontrarás lubinas poco profundas en el lago. Han sido vistos cerca de la orilla, por lo que no necesitarás mucho peso en tu línea para alcanzarlos.
  - **Pescador:** Encontrarás lucios moteados en el lago. Se sabe que les gustan las criaturas que se retuercen, especialmente las rojas.
  - **Pescador:** Encontrarás truchas trueno en el río. Son inteligentes y pueden detectar metales a un kilómetro de distancia. Será mejor que pienses detenidamente qué tipo de anzuelo utilizas.
  - **Pescador:** Encontrarás anhelantes truchas en los muelles. Se sabe que les gustan las criaturas revoloteantes, especialmente las verdes.
  - {{Transcript missing|More clues}}

#### Si la competencia ya comenzó o acaba de terminar

- **Pescador:** Estás interesado, ¿no? <br>Tendrás que esperar a que comience la cuenta regresiva para la próxima competencia antes de que pueda darte una pista.

### Overhead

- **Pescador:** {{RSChat|Fish Flingers starts in [number] minutes.}}
