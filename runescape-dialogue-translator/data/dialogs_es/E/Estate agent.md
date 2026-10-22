# Estate agent

- **Original Wiki Page**: [Transcript:Estate agent](https://runescape.wiki/w/Transcript%3AEstate%20agent)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Antes de comenzar No hay lugar como el hogar...


##### Fuera de Rimmington

- **Estate agent:** Si lo que buscas es una casa, querrás dirigirte a Rimmington y charlar con estate agent allí.

##### En Rimmington

- **Estate agent:** Estoy seguro de que es la casa que deseas, pero dado que recientemente reclutamos a Alfred Stonemason, dejaré que te dé un resumen de la vivienda. Acércate a él para charlar.

#### Durante No hay lugar como el hogar...

- (ver|No hay lugar como el hogar...)

#### Después de completar No hay lugar como el hogar...

- **Estate agent:** ¡Bienvenido a la Agencia de Vivienda Gielinorian! ¿Qué puedo hacer por ti?
- [Menu]: Selecciona una opción
  - [Choice]: Háblame de casas.
    - **Player:** Háblame de casas.
    - **Estate agent:** Todo surgió de los experimentos de los magos. Encontraron una manera de plegar el espacio, de modo que pudieran agrupar muchos acres de tierra en un área de sólo un pie de ancho.
    - **Estate agent:** Crearon varias regiones de espacio plegado en todo el mundo. Cada uno contiene cientos de pequeñas parcelas donde la gente puede construir casas.
    - **Player:** ¡Ah, así es como todos pueden tener una casa sin que abarroten el mundo!
    - **Estate agent:** Bastante. Los magos no querían empantanarse en el aspecto comercial así que me contrataron para vender las casas.
    - **Estate agent:** Hay otras personas en Gielinor que pueden ayudarte a amueblar tu casa. O si eres un experto en Construction, construye furniture tú mismo en un banco de trabajo furniture.
    - **Estate agent:** Deberías empezar por conseguir algo de planks para construir furniture. Intente comprarlos en Grand Exchange o hacerlos usted mismo en un aserradero.
    - (previous)
  - [Choice]: ¿Cómo puedo entrenar construcción?
    - **Player:** ¿Cómo puedo entrenar la construcción?
    - (Condition: In Rimmington:)
      - **Estate agent:** ¡Puedes entrenarlo aquí mismo! Encontrará un banco de trabajo furniture, así como miembros de la Agencia de Vivienda Gielinorian que pueden convertir su logs en planks, o convertir sus materiales destacados en materias primas.
      - **Estate agent:** Una vez que hayas construido un furniture, puedes colocarlo en un cofre de almacenamiento furniture para usarlo dentro de tu casa.
      - (previous)
    - (Condition: Elsewhere:)
      - **Estate agent:** ¡Puede comenzar con la capacitación en construcción visitando nuestra sede en Rimmington!
      - **Estate agent:** Allí encontrará una gran cantidad de comodidades que lo ayudarán a comenzar a construir furniture para hacer de su casa un hogar.
      - (previous)
  - [Choice]: ¿Puede cambiar la ubicación de mi portal de salida preferida, por favor?
    - ((The following is shown in an interface titled "SELECT AN OPTION":))
      - ¿A dónde le gustaría trasladar el portal de su casa?
        - [Choice]: 1. Rimmington (2,500 coins)
          - (continue)
        - [Choice]: 2. Taverley (2,500 coins)
          - (continue)
        - [Choice]: 3. Pollnivneach (3,750 coins)
          - (continue)
        - [Choice]: 4. Rellekka (5,000 coins)
          - (continue)
        - [Choice]: 5. Brimhaven (7,500 coins)
          - (continue)
        - [Choice]: 6. Yanille (12,500 coins)
          - (continue)
        - [Choice]: 7. Menaphos (25,000 coins)
          - (continue)
        - [Choice]: 8. Otot (Mazcab) (25.000 coins)
          - (continue)
        - [Choice]: 9. Prifddinas (25,000 coins)
          - (continue)
      - (Condition: With the house already in the selected location:)
        - ¡El portal de tu casa ya está ahí!
        - (pop-up)
          - (Pop-up: Your house portal is already there!|warning=yes)
      - (Condition: Without the house already in the selected location:)
        - (Condition: Without enough coins:)
          - Necesitas [número] coins para mover el portal de tu casa allí.
          - (pop-up)
            - (Pop-up: You need [number] coins to move your house portal there.|warning=yes)
        - (Condition: With enough coins:)
          - (La interfaz se cierra y el diálogo continúa a continuación).
      - ((Tooltips on the options:))
        - ((Location where the portal is:))
          - {{Interface tooltip|Your main portal is already there!}}
        - ((Other locations without enough coins:))
          - {{Interface tooltip|You need [number] coins.}}
    - (removes=coins depending on the selected location)
    - [El portal de su casa se ha trasladado a [Location].]
  - [Choice]: ¿Puedes hablarme de construction contracts?
    - (continue|Contracts)
  - [Choice]: ¿Puedes hablarme sobre el Construction skillcape?
    - (Condition: With below 99 Construction:)
      - **Player:** ¿Puedes hablarme sobre el Construction skillcape?
      - **Estate agent:** Como sabrás, skillcapes solo está disponible para maestros en una habilidad. ¡He pasado toda mi vida construyendo casas y ahora dedico mi tiempo a venderlas! Como muestra de mis habilidades llevo este Skillcape de Construction. Si alguna vez tienes la habilidad suficiente para construir un trono demoníaco, ven a hablar conmigo y te venderé un skillcape como el mío.
    - (Condition: With at least 99 Construction:)
      - [Menu]: Selecciona una opción
        - [Choice]: Me pregunto si tienes algún skillcapes por ahí.
          - **Player:** Me pregunto si tienes algún skillcapes por ahí.
          - **Estate agent:** ¡Espero que no estén holgazaneando! Cualquier viejo podría coger uno y hacer alarde de él, pero...
          - **Estate agent:** He hecho algo especialmente para ti, el skillcape de Construction como muestra de tu maestría en el campo.
          - **Estate agent:** Desafortunadamente, es bastante costoso conseguir los materiales necesarios para crear una capa tan impresionante, por lo que es tuya a un costo.
          - [Menu]: ¿Qué skillcape te gustaría comprar?
            - [Choice]: 99 skillcape.
              - **Player:** Me gustaría el 99 skillcape, por favor.
              - (Condition: If the player has a ring of charos (a) equipped:)
                - **Estate agent:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins por este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
                - [Menu]: Elige una opción:
                  - [Choice]: ¿92.000 coins? Eso es demasiado caro.
                    - **Player:** Sé dónde encontrarte si cambio de opinión.
                  - [Choice]: De hecho, creo que tengo el dinero aquí.
                    - (Condition: If the player has no backpack space:)
                      - **Estate agent:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar algo de espacio en backpack antes de que pueda venderte uno.
                    - (Condition: If the player does not have enough money:)
                      - **Player:** Pero desafortunadamente me equivoqué.
                      - **Estate agent:** Bueno, vuelve a verme cuando lo hagas.
                    - (Condition: If the player has enough money:)
                      - (receives=Construction cape and Construction hood) (removes=92,000 coins)
                      - **Estate agent:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
                  - [Choice]: cond=If the player has 120 Construction|He dominado esta habilidad. ¿Hay algo más?
                    - **Estate agent:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
                    - **Estate agent:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
                    - **Estate agent:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo...
                    - **Estate agent:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle un Construction master cape.
                    - (continue|120)
              - (Condition: If the player does not have a ring of charos (a) equipped:)
                - **Estate agent:** Para eso necesito 99.000 coins.
                - [Menu]: Elige una opción:
                  - [Choice]: ¿99.000 coins? Eso es demasiado caro.
                    - **Player:** Sé dónde encontrarte si cambio de opinión.
                  - [Choice]: De hecho, creo que tengo el dinero aquí.
                    - (Condition: Without 99,000 coins:)
                      - **Player:** Pero, desafortunadamente, no tengo suficiente coins.
                      - **Estate agent:** Bueno, vuelve a verme cuando lo hagas.
                    - (Condition: With 99,000 coins:)
                      - (Condition: Without two free backpack slots:)
                        - **Estate agent:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar algo de espacio en backpack antes de que pueda venderte uno.
                      - (Condition: With two free backpack slots:)
                        - (removes=99,000 coins) (receives=Construction cape and Construction hood)
                        - **Estate agent:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
                  - [Choice]: cond=If the player has 120 Construction|He dominado esta habilidad. ¿Hay algo más?
                    - **Estate agent:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
                    - **Estate agent:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
                    - **Estate agent:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo...
                    - **Estate agent:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle un Construction master cape.
                    - (continue|120)
            - [Choice]: 120 Maestro skillcape.
              - **Player:** Me gustaría el Master cape, por favor.
              - **Estate agent:** Realmente has demostrado tu valía, no solo ante el gremio, sino también ante mí, Player. Estoy más que impresionado con lo que has logrado.
              - **Estate agent:** Con eso, sería mi {{Sic|honor}} ofrecerte el Master skillcape por el costo de 120,000 coins.
              - [Menu]: ¿Comprar Construction master cape por 120.000 coins?
                - [Choice]: Sí.
                  - (Condition: Without free backpack space:)
                    - **Estate agent:** No tienes suficiente espacio en tu backpack. Por favor regresa cuando tengas más.
                  - (Condition: With free backpack space:)
                    - (Condition: Without 120,000 coins:)
                      - No tienes suficiente dinero para comprar esta capa.
                      - (pop-up)
                        - (Pop-up: You do not have enough money to purchase this cape.|warning=yes)
                    - (Condition: With 120,000 coins:)
                      - (removes=120,000 coins) (receives=Construction master cape)
                      - (Action: Suena música Master cape.)
                - [Choice]: No.
                  - (end)
        - [Choice]: He notado que hay un par de versiones de cada skillcape.
          - **Estate agent:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
          - (Condition: If you use the old model:)
            - **Estate agent:** Parece que actualmente estás usando el modelo anterior para tu Construction skillcape. ¿Quieres cambiar a uno más nuevo?
            - (continue)
          - (Condition: If you use the new model:)
            - **Estate agent:** Aún puedes elegir usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
            - (continue)
          - [Menu]: Selecciona una opción
            - [Choice]: Sí, me gustaría usar la versión [new/old] del skillcape.
              - **Estate agent:** ¿Te gustaría usar el modelo [old/newer] solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
              - [Menu]: Selecciona una opción
                - [Choice]: Solo me gustaría cambiar el Construction skillcape.
                  - **Estate agent:** No hay problema, ahora utilizarás el modelo [older/newer] para tu Construction skillcape.
                - [Choice]: Me gustaría cambiar todos mis skillcapes.
                  - **Estate agent:** ¡No hay problema, ahora usarás el modelo [older/newer] para todos tus skillcapes!
                - [Choice]: ¡He cambiado de opinión!
                  - (end)
            - [Choice]: No, gracias.
              - **Estate agent:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión [old/new]!
              - (Condition: If the player uses the new model for any other skillcape:)
                - **Estate agent:** ¡Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas!
                - [Menu]: Selecciona una opción
                  - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
                    - **Estate agent:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
                  - [Choice]: No, gracias.
                    - (end)

### Redecorate


#### Antes de comenzar No hay lugar como el hogar...


##### Fuera de Rimmington

- **Estate agent:** Si lo que buscas es una casa, querrás dirigirte a Rimmington y charlar con estate agent allí.

##### En Rimmington

- **Estate agent:** Estoy seguro de que es la casa que deseas, pero dado que recientemente reclutamos a Alfred Stonemason, dejaré que te dé un resumen de la vivienda. Acércate a él para charlar.

#### Durante No hay lugar como el hogar...

- (ver|No hay lugar como el hogar...)

#### Después de completar No hay lugar como el hogar...

- **Estate agent:** Por supuesto. ¡Mi magia puede reconstruir el exterior de tu casa con un estilo completamente nuevo! ¿Cuál te gustaría?
- ((The following is shown in an interface titled "SELECT AN OPTION":))
  - ¿Qué estilo de casa te gustaría?
    - [Choice]: 1. Madera básica (1.250)
      - ((The interface closes and the dialogue continues below.))
    - [Choice]: 2. Piedra básica (2500)
      - ((The interface closes and the dialogue continues below.))
    - [Choice]: 3. Piedra elegante (12.500)
      - ((The interface closes and the dialogue continues below.))
    - [Choice]: 4. Piedra oscura (12.500)
      - ((The interface closes and the dialogue continues below.))
    - [Choice]: 5. Madera estilo Fremennik (5.000)
      - ((The interface closes and the dialogue continues below.))
- (removes=coins corresponding to the cost of the selected option)
- **Estate agent:** Tu casa ha sido redecorada.

### Contracts

- [Menu]: Elige una opción:
  - [Choice]: cond=Without a contract|Quiero un nuevo contrato.
    - (Condition: Without free backpack space:)
      - **Estate agent:** Necesitará algo de espacio en su backpack para un contrato.
    - (Condition: With free backpack space:)
      - (receives=Construction contract)
      - Te entregan un Construction contract.
      - **Estate agent:** Aquí tienes, esto acaba de llegar para [character] en [location].
      - **Player:** ¡Gracias! Veré qué puedo hacer.
  - [Choice]: cond=With a contract|¿Cuál es mi contrato actual?
    - **Estate agent:** Parece que estás ayudando a [character] en [location].
    - (Condition: If the Construction contract has been lost:)
      - (Condition: Without free backpack space:)
        - **Estate agent:** Necesitará algo de espacio en su backpack para un contrato.
      - (Condition: With free backpack space:)
        - (receives=Construction contract)
        - Te entregan un Construction contract.
  - [Choice]: Háblame de contracts
    - **Estate agent:** Hay muchos propietarios alrededor de Gielinor que tienen dificultades para mantenerse al día con las reparaciones de forma regular.
    - **Estate agent:** Ahora mismo existe una oportunidad de mercado para poner en práctica sus habilidades de construcción y ayudarlos.
    - **Estate agent:** Nosotros, los agentes inmobiliarios, podemos proporcionarle un contrato. Este contrato le indicará quién necesita ayuda y qué necesita reparación.
    - **Estate agent:** Todo lo que necesitas hacer es ir y reparar todos los furniture rotos.
    - **Estate agent:** Puedes utilizar materiales básicos para un trabajo de reparación más económico pero más lento. O puede utilizar materiales más caros para una devolución más rápida y más experiencia.
    - **Estate agent:** Elijas lo que elijas, obtendrás una gran cantidad de experiencia una vez que hayas reparado todos los pieces of furniture que necesitan reparación.
    - **Estate agent:** También te recompensaremos con créditos de contrato, que puedes canjear desde cualquier estate agent por recompensas variadas.
    - (previous|Contracts)
  - [Choice]: cond=If the player has lost their plank box|He perdido mi caja de tablones.
    - **Player:** He perdido mi caja de tablones.
    - **Estate agent:** No te preocupes, tengo otro por ahí.
    - (Condition: Without free backpack space:)
      - **Estate agent:** Vuelve cuando tengas algo de espacio libre en tu backpack.
    - (Condition: With free backpack space:)
      - (receives=plank box)
      - **Estate agent:** Pero intenta no perder este.
  - [Choice]: ¿Tienes algo que pueda comprar?
    - (opens=Estate Agents Shop)
  - [Choice]: [Leave]
    - (end)

### Shop

- (opens=Estate Agents Shop)
