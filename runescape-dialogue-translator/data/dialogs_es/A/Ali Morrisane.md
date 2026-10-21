# Ali Morrisane

- **Original Wiki Page**: [Transcript:Ali Morrisane](https://runescape.wiki/w/Transcript%3AAli%20Morrisane)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{dialogue|npc}}
{{transcript npc|Ali Morrisane}}

### In Al Kharid


#### Antes de The Feud, sin cumplir los requisitos de la misión

- **Ali Morrisane:** Hola amigo. Eche un vistazo a mis productos.
- [Menu]: Selecciona una opción
  - [Choice]: No, realmente estoy demasiado ocupado.
    - **Player:** No, realmente estoy demasiado ocupado.
  - [Choice]: Está bien.
    - (Action: opens=Artículos con descuento de Ali)

#### Antes de The Feud, cumpliendo los requisitos de la misión

- **Ali Morrisane:** Buenos días y bienvenido de nuevo a Al Kharid.
- **Player:** Hola a ti también.
- **Ali Morrisane:** Mi nombre es Ali Morrisane, el mejor vendedor del mundo.
- [Menu]: Selecciona una opción
  - [Choice]: Si es así, ¿por qué sigues vendiendo productos en un puesto?
    - **Player:** Si es así, ¿por qué sigues vendiendo productos en un puesto?
    - **Ali Morrisane:** Bueno, uno sólo puede hacer y vender una cantidad determinada. Si tuviera más staff podría vender más, en lugar de perder el tiempo en cosas insignificantes, podría seguir vendiendo arena a los Bedabin y baratijas turísticas inútiles a todo el mundo.
    - [Menu]: Selecciona una opción
      - [Choice]: Estoy demasiado ocupado; las aventuras son un trabajo de tiempo completo, ¿sabes?
        - **Player:** Estoy demasiado ocupado; las aventuras son un trabajo de tiempo completo, ¿sabes?
        - **Ali Morrisane:** No hay problema amigo mío, tal vez en otro momento.
        - **Ali Morrisane:** De todos modos, echa un vistazo a mis productos.
        - (removes=10 coins) (receives=a random junk item)
        - A pesar de tus mejores esfuerzos, Ali M todavía se las arregla para venderte algo de basura.
        - (Action: arriba|productos)
      - [Choice]: Me gustaría ayudarte pero.....
        - (ver|La disputa#Hablando con Ali Morrisane)
  - [Choice]: Entonces, ¿qué estás vendiendo?
    - (Action: opens=Artículos con descuento de Ali)

#### Después de la pelea

- (ver|Ali the Trader)

#### Después de Ali the Trader


- **Ali Morrisane:** Hola Player. ¿Cómo va la aventura?
- (Condition: Si el player no ha completado Extrañando a mi mamá)
  - **Player:** Hola Ali. Nada mal. ¿Cómo estás?
  - **Ali Morrisane:** Aún se vende.
  - [Menu]: Selecciona una opción
    - (Condition: Requiere completar The Feud y la sección de blackjack de Rogue Trader.)
      - [Choice]: Me gustaría echar un vistazo a su selección de blackjacks.
        - (opens=Ali's Discount Wares)
    - (Condition: Requiere completar la sección de ropa de Rogue Trader)
      - [Choice]: Me gustaría echar un vistazo a tu selección de ropa.
        - (opens=Ali's Discount Wares)
      - [Choice]: Me gustaría echar un vistazo a tu selección de runas.
      - [Menu]: Selecciona una opción
        - [Choice]: Intenta abrir un pequeño cofre de runas.
          - **Player:** Creo que tendré que abrir un pequeño cofre de runas.
          - (Condition: Si el player no ha abierto un pequeño cofre ese día)
            - [Menu]: Selecciona una opción
              - [Choice]: Caja de fuerza.
                - (Condition: Si el player no logra forzar el bloqueo)
                  - Tus brazos se cansan por el esfuerzo de intentar abrir el ataúd...
                  - **Player:** Hmmm... Parece que este candado será imposible de abrir con fuerza.
                - (Condition: Si el player fuerza con éxito el bloqueo)
                  - Fuerzas la apertura de la cerradura con una combinación de tu fuerza y agilidad.
                  - [Menu]: Selecciona una opción
                    - [Choice]: Compra todas las runas para [amount] coins.
                      - (Condition: Si el player tiene suficiente coins y espacio libre en el inventario para comprar todas las runas)
                        - (removes=[amount] coins)
                        - **Ali Morrisane:** Como siempre, es un placer hacer negocios con usted.
                        - **Player:** Lo mismo.
                      - (Condition: Si el player no tiene suficiente coins para comprar todas las runas:)
                        - **Player:** Maldita sea, no tengo suficiente coins en mi inventario para comprarlos.
                        - **Ali Morrisane:** No te preocupes, te diré que no pondré las runas a la venta todavía. Te dejaré ser el primero en decidir sobre ellos.
                        - (opens=Ali's Rune Shop)
                      - (Condition: Si el player no tiene suficiente espacio libre en el inventario para comprar todas las runas)
                        - **Player:** ¡Explosión! No tengo suficiente espacio para todas las runas en mi inventario.
                        - **Ali Morrisane:** No te preocupes, te diré que no pondré las runas a la venta todavía. Te dejaré ser el primero en decidir sobre ellos.
                        - (opens=Ali's Rune Shop)
                    - [Choice]: Descubre qué son las runas.
                      - (opens=Ali's Rune Shop)
              - [Choice]: Abrir cerradura.
                - (Player se agacha ligeramente e intenta forzar la cerradura)
                - (Condition: Si el player no logra forzar la cerradura:)
                  - (Condition: Si la ganzúa se rompe:)
                    - (removes=lockpick)
                    - [Tu ganzúa se rompe.]
                    - (continue)
                  - [No logras forzar la cerradura: tus dedos se entumecen al intentar abrir la cerradura.]
                - (Condition: Si el player abre con éxito la cerradura)
                  - Abres el ataúd...
                  - (above|runes)
              - [Choice]: Examinar la cerradura.
                - (Se abre la interfaz del rompecabezas RuneSudoku para un pequeño cofre).
                - (above|runes)
          - (Condition: Si el player ya abrió un pequeño ataúd ese día)
            - **Ali Morrisane:** Lo siento amigo, hoy no tengo más ataúdes pequeños. Vuelve mañana y habrá llegado otro envío.
        - [Choice]: Intenta abrir un gran cofre de runas.
          - **Player:** Me siento afortunado, echemos un vistazo a cómo abrir uno de esos ataúdes grandes.
          - (Condition: Si el player no ha abierto un ataúd grande ese día)
            - [Menu]: Selecciona una opción
              - [Choice]: Caja de fuerza.
                - (Condition: Si el player no logra forzar el bloqueo)
                  - Tus brazos se cansan por el esfuerzo de intentar abrir el ataúd...
                  - **Player:** Hmmm... Parece que este candado será imposible de abrir con fuerza.
              - [Choice]: Abrir cerradura.
                - (Player se agacha ligeramente e intenta forzar la cerradura)
                - (Condition: Si el player no logra forzar la cerradura:)
                  - No logras forzar la cerradura: tus dedos se entumecen al intentar abrir la cerradura.
                  - (Condition: Si la ganzúa se rompe:)
                    - (removes=lockpick)
                    - [Tu ganzúa se rompe.]
                    - (continue)
                  - **Player:** Hmmm... Parece que esta cerradura será imposible de abrir.
                - (Condition: Si el player abre con éxito la cerradura)
                  - Abres el ataúd...
                  - (above|runes)
              - [Choice]: Examinar la cerradura.
                - (Se abre la interfaz del rompecabezas RuneSudoku para un ataúd grande).
                - (above|runes)
          - (Condition: Si el player ya abrió un ataúd grande ese día)
            - **Ali Morrisane:** Lo siento amigo, hoy no tengo más ataúdes grandes. Vuelve mañana y habrá llegado otro envío.
        - [Choice]: Compra runas elementales.
          - (opens=Ali's Rune Shop)
        - [Choice]: Compra otras runas.
          - (opens=Ali's Rune Shop)
        - [Choice]: Pensándolo bien, realmente no necesito runas.
          - **Player:** Pensándolo bien, realmente no necesito ninguna runa.
      - [Choice]: Me gustaría echar un vistazo a su stock general.
        - (opens=Ali's Discount Wares)
    - (Condition: Si el player ha preguntado a alguno de los comerciantes de Al Kharid sobre Ali Morrisane)
      - [Choice]: He oído que estás planeando expandir tu negocio aquí...
        - **Player:** He oído que estás planeando expandir tu negocio aquí...
        - **Ali Morrisane:** Por supuesto, amigo mío. Cualquier buen vendedor debe aprovechar las oportunidades que se presenten.
        - **Player:** ¡Pero tus hombres están amenazando a los demás comerciantes!
        - **Ali Morrisane:** Me temo que eso es lamentable.
        - (Condition: Si el player le ha preguntado a Captain Dalbur qué piensa de Ali Morrisane)
          - **Player:** Y los gnomos no parecen muy contentos con tu negocio de alfombra mágica.
          - **Ali Morrisane:** Un buen hombre de negocios busca todas las oportunidades que puede.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿No vas a hacer nada con tus hombres?
            - **Player:** ¿No vas a hacer nada con tus hombres?
            - **Ali Morrisane:** Bueno, estos asociados de mi sobrino pueden ser algo... demasiado entusiastas.
            - **Ali Morrisane:** Estoy seguro de que se calmarán pronto.
            - [Menu]: Selecciona una opción
              - [Choice]: ¡Pero amenazan con hacer daño a los comerciantes si no cooperan!
                - **Player:** ¡Pero amenazan con lastimar a los comerciantes si no cooperan!
                - **Ali Morrisane:** Bueno, hay una solución sencilla, ¿no estás de acuerdo?
                - **Player:** ¿Estás planeando hacerte cargo de todas las tiendas de Al Kharid?
                - **Ali Morrisane:** Es un paso en la dirección correcta.
                - **Ali Morrisane:** Ahora, ¿te gustaría echar un vistazo a mis productos?
                - (Action: A Player le quitan 10 coins y recibe un artículo basura aleatorio: "A pesar de tus mejores esfuerzos, Ali M todavía se las arregla para venderte algo de basura".)
                - (above|wares)
              - [Choice]: Bueno, buena suerte con tu negocio.
                - **Player:** Bueno, buena suerte con tu negocio.
                - **Ali Morrisane:** Antes de irte, echa un vistazo a mis productos.
                - (Action: A Player le quitan 10 coins y recibe un artículo basura aleatorio: "A pesar de tus mejores esfuerzos, Ali M todavía se las arregla para venderte algo de basura".)
                - (above|wares)
          - (Condition: Si el player le ha preguntado a Captain Dalbur qué piensa de Ali Morrisane:)
            - [Choice]: ¿Qué harás con los gnomos?
              - **Player:** ¿Qué harás con los gnomos?
              - **Ali Morrisane:** Ellos pueden seguir lanzando sus planeadores hacia los árboles y yo seguiré con mi negocio. Tarde o temprano todo saldrá a mi favor.
              - **Player:** Supongo que sí...
              - **Ali Morrisane:** De todos modos, antes de irte, echa un vistazo a mis productos.
              - (Action: A Player le quitan 10 coins y recibe un artículo basura aleatorio: "A pesar de tus mejores esfuerzos, Ali M todavía se las arregla para venderte algo de basura".)
              - (above|wares)
          - [Choice]: Bueno, buena suerte con tu negocio.
            - (above|goodluck)
- (Condition: Si el player ha completado Extrañando a mi mamá)
  - [Menu]: Selecciona una opción
    - [Choice]: Hola Ali. Nada mal. ¿Cómo estás?
      - (above|standard)
    - [Choice]: Tengo algunas preguntas sobre una tumba.
      - **Player:** Tengo algunas preguntas sobre una tumba.
      - **Ali Morrisane:** Entonces, ¿qué es exactamente lo que necesitas saber?
      - **Player:** Sólo vengo a decir que resolví el problema de la momia, así que todo ha acabado bien.
      - **Ali Morrisane:** ¡Bah, dónde está el beneficio para mí en todo esto! Fuera de mi vista, fanfarrón.

#### Opción comercial

- (Acción: arriba2|comercio) <!--Some options appear here but will not appear when talking to Ali Morrisane with standard dialogue.-->

#### Usando un volante Al Kharid sobre él

- **Player:** ¡Hola! ¡Tengo este vale de descuento!
- **Ali Morrisane:** ¡Oh! Err... ¡desafortunadamente parece haber caducado ayer!
- **Player:** ¡Pero acabo de recibirlo de Waseem the Leaflet!
- **Ali Morrisane:** Lo siento, no hay nada que pueda hacer.
- **Player:** ¡Pero tú eres quien los imprimió!
- **Ali Morrisane:** Mira, los hice imprimir para ganarme a los comerciantes locales. No estaban muy contentos con el vale de descuento, pero les prometí que les pagaría sus pérdidas.
- **Player:** Entonces, ¿por eso todos están desactualizados?
- **Ali Morrisane:** ¡No sé a qué te refieres!
- **Ali Morrisane:** De todos modos, antes de irte, echa un vistazo a mis productos.
- (Action: continuar|trade2)

#### Usando cualquier otro objeto sobre él

- **Ali Morrisane:** Deja de intentar descargarme tu mercancía. ¿No ves que ya tengo suficientes activos de los que disponer?
