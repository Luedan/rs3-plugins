# Granny Rowan

- **Original Wiki Page**: [Transcript:Granny Rowan](https://runescape.wiki/w/Transcript%3AGranny%20Rowan)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before the player has the ability to use the botanist's workbench


#### Intentando utilizar el banco de trabajo del botánico

- **Granny Rowan:** ¡Por aquí, querida! Consiénteme con un poco de conversación antes de comenzar, ¿quieres, cariño?

#### Cualquier opción antes de completar el siguiente diálogo

- **Player:** ¿Quién eres? ¿Quién te dejó entrar aquí?
- **Granny Rowan:** Rowan, querida. Granny Rowan, si lo prefieres. La mayoría lo hace.
- **Granny Rowan:** Un pajarito me dijo que habías construido un nuevo banco para botánicos{{Sic}} en este pequeño y pintoresco fuerte tuyo, así que decidí subirme y echarte una mano.
- **Granny Rowan:** Sé un par de cosas sobre cómo hacer pociones, ¿sabes? ¿No es así, Hoja?
- **Hoja:** Miau.
- **Player:** ¿Por qué debería confiar en ti?
- **Granny Rowan:** El wilderness es un lugar peligroso, querida. Ahora más que nunca. Zombis corriendo desenfrenados, y ahora un Mahjarrat con un dragón no-muerto en camino...
- **Granny Rowan:** Nunca está de más tener aliados en estos momentos, querida. Especialmente cuando hacen una buena cerveza.
- **Hoja:** Miau.
- **Player:** ¿Cómo sabes eso?
- **Granny Rowan:** Tengo mis maneras, amor. Ese hombre muy, muy desagradable no es amigo de la abuela, te lo aseguro.
- **Player:** Siento que necesito hablar con captain of the guard...
- **Granny Rowan:** Como debes, dulzura. Pero no hagas esperar a un viejo querido.

#### Cualquier opción después de completar el diálogo anterior pero antes de hablar con guard captain Sofía

- **Granny Rowan:** ¿Ya has hablado con la pequeña Sofía?
- **Player:** ¿Cómo...? Oh, no importa. Aún no.
- **Granny Rowan:** Date prisa, dulzura. Es muy grosero hacer esperar a una anciana.

#### Cualquier opción después de hablar con guard captain Sofía

- **Granny Rowan:** ¿Ya has hablado con la pequeña Sofía?
- **Player:** ¿Cómo...? Oh, no importa. Un pajarito te lo dijo, ¿verdad?
- **Granny Rowan:** Eres una persona que aprende rápido. Ahora, ¿cuál es el veredicto?
- **Player:** Puedes quedarte y ayudar a administrar el banco de trabajo. Pero te estaremos vigilando.
- **Granny Rowan:** ¡Qué cariño! ¡Debes acompañarme a tomar un té algún día, insisto!
- **Hoja:** Miau.
- **Player:** En otro momento, tal vez.

### After the player has the ability to use the botanist's workbench


#### Habla con

- Elige una opción:
  - ¿Puedes decantar mis pociones por mí?
    - (below|Decant)
  - ((Con el Nivel 2 construido:))
    - ¿Tienes algo para intercambiar?
      - (opens=Granny Rowan's Supplies)
  - ((Con el Nivel 3 construido:))
    - ¿Puedes prepararme mis pociones?
      - (below|Prepare potions)
  - ¿Qué haces aquí?
    - **Player:** Entonces, ¿qué es exactamente lo que haces aquí?
    - **Granny Rowan:** Oh, ya sabes, esto y aquello.
    - En el nivel 1, Granny Rowan puede decantar tus pociones y grasas por ti.
    - En el nivel 2, Granny Rowan abrirá una tienda que tiene un stock limitado de suministros de herboristería comercializables. Además, podrás recibir viales de agua no identificados del banco del botánico.
    - En el nivel 3, Granny Rowan preparará sobrecargas y ungüentos de sobrecarga para usted, lo que le permitirá prepararlos en mayores cantidades en el banco de trabajo del botánico.
  - Cancelar
    - (end)

#### Decantar

- ((Lo siguiente se muestra en una interfaz titulada "SELECCIONE UNA OPCIÓN":))
  - Opciones de decantación
    - Decantar viales
      - (La interfaz se cierra.)
      - **¿EN CUÁNTAS DOSIS QUIERES DECANTAR?**
        - una dosis
          - ((Sin elementos en backpack:))
            - **Granny Rowan:** ¡No tienes nada que decantar!
          - ((Con elementos en backpack:))
            - Buscando...
            - ((Sin pociones compatibles encontradas:))
              - ((Sin pociones encontradas:))
                - **Granny Rowan:** Lo siento, no sé cómo decantar nada de lo que llevas.
              - ((Con una poción incompatible encontrada:))
                - **Granny Rowan:** Lo siento, no puedo hacer nada con esa poción.
              - ((Con múltiples pociones incompatibles encontradas:))
                - **Granny Rowan:** Lo siento, no puedo hacer nada con esas pociones.
            - ((Con pociones compatibles encontradas:))
              - ((Con coins para viales faltantes:))
                - ((Sin espacio backpack para los nuevos elementos:))
                  - **Granny Rowan:** Tu inventario está demasiado lleno para que pueda hacer algo por ti.
                - ((Con espacio backpack para los nuevos elementos:))
                  - (removes=two coins for each missing vial) (receives=as many one-dose potions as possible)
                  - ((Se repite para cada tipo de poción si el coins se tomó de la bolsa de dinero, luego continúa a continuación:))
                    - [número] coins se han eliminado de su bolsa de dinero.
                  - **Granny Rowan:** Ahí lo tienes, amigo.
              - ((Sin coins por viales faltantes:))
                - **Granny Rowan:** Lo sentimos, no tienes suficiente dinero para pagar suficientes viales vacíos.
        - Dos dosis
          - ((Sin elementos en backpack:))
            - **Granny Rowan:** ¡No tienes nada que decantar!
          - ((Con elementos en backpack:))
            - Buscando...
            - ((Sin pociones compatibles encontradas:))
              - ((Sin pociones encontradas:))
                - **Granny Rowan:** Lo siento, no sé cómo decantar nada de lo que llevas.
              - ((Con una poción incompatible encontrada:))
                - **Granny Rowan:** Lo siento, no puedo hacer nada con esa poción.
              - ((Con múltiples pociones incompatibles encontradas:))
                - **Granny Rowan:** Lo siento, no puedo hacer nada con esas pociones.
            - ((Con pociones compatibles encontradas:))
              - ((Con coins para viales faltantes:))
                - ((Sin espacio backpack para los nuevos elementos:))
                  - **Granny Rowan:** Tu inventario está demasiado lleno para que pueda hacer algo por ti.
                - ((Con espacio backpack para los nuevos elementos:))
                  - (removes=two coins for each missing vial) (receives=as many two-dose potions as possible)
                  - ((Se repite para cada tipo de poción si el coins se tomó de la bolsa de dinero, luego continúa a continuación:))
                    - [número] coins se han eliminado de su bolsa de dinero.
                  - **Granny Rowan:** Ahí lo tienes, amigo.
              - ((Sin coins por viales faltantes:))
                - **Granny Rowan:** Lo sentimos, no tienes suficiente dinero para pagar suficientes viales vacíos.
        - Tres dosis
          - ((Sin elementos en backpack:))
            - **Granny Rowan:** ¡No tienes nada que decantar!
          - ((Con elementos en backpack:))
            - Buscando...
            - ((Sin pociones compatibles encontradas:))
              - ((Sin pociones encontradas:))
                - **Granny Rowan:** Lo siento, no sé cómo decantar nada de lo que llevas.
              - ((Con una poción incompatible encontrada:))
                - **Granny Rowan:** Lo siento, no puedo hacer nada con esa poción.
              - ((Con múltiples pociones incompatibles encontradas:))
                - **Granny Rowan:** Lo siento, no puedo hacer nada con esas pociones.
            - ((Con pociones compatibles encontradas:))
              - ((Con coins para viales faltantes:))
                - ((Sin espacio backpack para los nuevos elementos:))
                  - **Granny Rowan:** Tu inventario está demasiado lleno para que pueda hacer algo por ti.
                - ((Con espacio backpack para los nuevos elementos:))
                  - (removes=two coins for each missing vial) (receives=as many three-dose potions as possible)
                  - ((Se repite para cada tipo de poción si el coins se tomó de la bolsa de dinero, luego continúa a continuación:))
                    - [número] coins se han eliminado de su bolsa de dinero.
                  - **Granny Rowan:** Ahí lo tienes, amigo.
              - ((Sin coins por viales faltantes:))
                - **Granny Rowan:** Lo sentimos, no tienes suficiente dinero para pagar suficientes viales vacíos.
        - Cuatro dosis
          - Buscando...
          - ((Sin elementos en backpack:))
            - **Granny Rowan:** ¡No tienes nada que decantar!
          - ((Con elementos en backpack:))
            - Buscando...
            - ((Sin pociones compatibles encontradas:))
              - ((Sin pociones encontradas:))
                - **Granny Rowan:** Lo siento, no sé cómo decantar nada de lo que llevas.
              - ((Con una poción incompatible encontrada:))
                - **Granny Rowan:** Lo siento, no puedo hacer nada con esa poción.
              - ((Con múltiples pociones incompatibles encontradas:))
                - **Granny Rowan:** Lo siento, no puedo hacer nada con esas pociones.
            - ((Con pociones compatibles encontradas:))
              - (receives=as many four-dose potions as possible)
              - **Granny Rowan:** Ahí lo tienes.
    - Decantar matraces
      - (La interfaz se cierra.)
      - ((Sin matraces en backpack:))
        - **Granny Rowan:** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener 2 matraces que no estén completamente llenos!
      - ((Con matraces en backpack:))
        - **Granny Rowan:** Veamos qué tienes. Decantaré sus frascos de poción nuevamente en 6 frascos dosificados. Puedo hacer uso de los frascos, así que los aceptaré como pago.
        - ((Sólo con la confirmación no desactivada:))
          - **¿DECANTAR LOS MATRACES Y GUARDARÉ LOS MATRACES VACÍOS?**
            - si
              - (continue)
            - No
              - (end)
            - Si y no vuelvas a preguntar
              - (continue)
        - (receives=as many six-dose flasks as possible) (removes=all flasks that were emptied completely)
        - **Granny Rowan:** Aquí tienes. ¡Eso es lo mejor que puedo hacer! {{Sic|If the flasks don't look too different, I gave them a clean}}
    - Convertir viales en matraces
      - (La interfaz se cierra.)
      - ((Sin matraces vacíos en backpack:))
        - **Granny Rowan:** Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos. Puedes traérmelos anotados o sin anotaciones.
      - ((Con matraces vacíos en backpack:))
        - **Granny Rowan:** {{Sic|Lets}} mira lo que tienes. Decantaré los viales de poción y todos los frascos con hasta 4 dosis en frascos de 6 dosis.  Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos.
        - ((Sin pociones para decantar o sin espacio backpack para los nuevos items:))
          - **Granny Rowan:** ¡Lo siento, parece que no tienes nada en lo que pueda ayudarte! Asegúrate de tener las pociones correctas y algo de espacio libre en tu inventario y podré intentarlo de nuevo.
        - ((Con pociones para decantar y espacio backpack para los nuevos items:))
          - (removes=as many potion doses as possible) (receives=empty vials for completely emptied potion vials and full potion flasks for all removed doses)
          - **Granny Rowan:** Aquí tienes. ¡Eso es lo mejor que puedo hacer!
    - Convertir matraces en viales
      - (La interfaz se cierra.)
      - ((Sin matraces para convertir o sin espacio backpack para los nuevos elementos:))
        - **Granny Rowan:** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener al menos 1 matraz!
      - ((Con matraces para convertir y con espacio backpack para los nuevos elementos:))
        - **Granny Rowan:** Por supuesto. Creo que puedo utilizar los matraces, así que te daré los viales gratis.
        - (removes=flasks) (receives=vials with corresponding number of doses)
        - **Granny Rowan:** Ahí lo tienes, ¡eso es lo mejor que puedo hacer!
    - combinar medusas
      - (La interfaz se cierra.)
      - ((Sin elementos en backpack:))
        - **Granny Rowan:** ¡No tienes medusas para combinar!
      - ((Con elementos en backpack:))
        - ((Sin medusas para combinar:))
          - **Granny Rowan:** Lo siento, no sé cómo combinar nada de lo que llevas.
        - ((Con medusas para combinar:))
          - (Action: Se combinan las medusas.)
          - **Granny Rowan:** Ahí lo tienes.
    - Cancelar
      - (La interfaz se cierra.)

#### Comercio

- (opens=Granny Rowan's Supplies)

#### Preparar pociones


##### Con la funcionalidad habilitada

- **Player:** ¿Puedes prepararme mis pociones, por favor?
- **Granny Rowan:** ¡Por supuesto! Sólo para advertirte que no podré recuperarlos después. Tampoco me beneficiaré de ninguno de tus elegantes beneficios.
  - ¿Quieres continuar?
    - Sí.
      - (La interfaz Make-X para la producción de artículos se abre con el artículo con el requisito Herblore más alto seleccionado, o sobrecarga (3) (unf) si el player no tiene materiales para ningún artículo).
      - ((Después de hacer pociones sin terminar:))
        - **Granny Rowan:** ¡Aquí tienes!
    - No.
      - (end)

##### Con la funcionalidad deshabilitada

- Granny Rowan está demasiado cansado para hacer esto ahora.
