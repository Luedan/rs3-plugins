# Hemlock

- **Original Wiki Page**: [Transcript:Hemlock](https://runescape.wiki/w/Transcript%3AHemlock)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Exchange

- ((Se abre la interfaz de la tienda Farming.))

### Talk to

- **Hemlock:** ¡Es un día bastante agradable aquí en Um! ¿Puedo ayudarte con el almacenamiento de herramientas, con un viaje a la granja de Winkin o con algo más?
- [Menu]: Elige...
  - [Choice]: Almacenamiento de herramientas.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Qué herramientas puedes almacenar?
        - **Player:** ¿Qué puedes almacenar?
        - **Hemlock:** Puedo sostener tu rastrillo, sembrador, pala, tijeras de podar, regadera y paleta, pero no esas paletas que se usan en arqueología.
        - **Hemlock:** También puedo guardarte algunos cubos y espantapájaros, e incluso compost, supercompost y ultracompost. Por supuesto, el abono es esencial para una buena agricultura, así que puedo almacenar mucho para ti.
        - **Hemlock:** Además, si me entregas tus productos agrícolas, tal vez pueda convertirlos en billetes.
        - **Hemlock:** Entonces, ¿te gustaría que cuidara tus herramientas agrícolas?
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: Sí, por favor.
            - **Player:** Sí, por favor.
            - ((Se abre la interfaz de la tienda Farming.))
          - [Choice]: ¿Qué haces con las herramientas que estás almacenando?
            - **Player:** ¿Qué haces con las herramientas que almacenas? ¡No caben todos en tus bolsillos!
            - **Hemlock:** Por supuesto que no. Tengo un cobertizo para herramientas. Aunque es un cobertizo bastante curioso. A veces, los elementos simplemente parecen aparecer allí.
            - **Hemlock:** Entonces, ¿te gustaría que cuidara tus herramientas?
            - [Menu]: ¿Qué te gustaría decir?
              - [Choice]: Sí por favor.
                - **Player:** Sí, por favor.
                - ((Se abre la interfaz de la tienda Farming.))
              - [Choice]: ¿Qué puedes almacenar?
                - (arriba)
              - [Choice]: No gracias, guardaré mis cosas.
                - (abajo)
          - [Choice]: No gracias, guardaré mis cosas.
            - **Player:** No, gracias, guardaré mis cosas.
            - **Hemlock:** Bueno, estaré aquí si alguna vez decides que puedo ser útil.
      - [Choice]: Abre tu tienda de herramientas, por favor.
        - ((Se abre la interfaz de la tienda Farming.))
      - [Choice]: En realidad, estoy bien.
        - **Player:** En realidad, estoy bien.
  - [Choice]: La granja de Winkin.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Puedes llevarme a la granja de Winkin?
        - **Player:** ¿Puedes llevarme a Winkin's Farm?
        - **Hemlock:**{{RSChat|Avach nimporto!}}
        - (Action: Hemlock te teletransporta a Winkin's Farm.)
      - [Choice]: En realidad, estoy bien.
        - (arriba)
  - [Choice]: Compostaje.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Pueden hacerme abono con parches?
        - **Player:** ¿Pueden hacerme abono con parches?
        - **Hemlock:** Claro, puedo hacerlo en todos tus parches usando el abono que me das, si estás dispuesto a pagar por la conveniencia.
        - **Hemlock:** 500 de oro para abono normal, 1500 de oro para supercompost o 2500 de oro para ultracompost. Paga hasta 60.000 por adelantado, pero no hay reembolsos.
        - ((Con compost que queda por comprar:))
          - [Menu]: ¿Qué quieres recargar?
            - (Condition: Con compost normal queda por comprar:)
              - [Choice]: abono normal
                - {{Tinput|Pay for how many (max [number])?}}
                - ((Después de ingresar un número positivo:))
                  - [Menu]: ¿Pagar [número] coins?
                    - [Choice]: Sí.
                      - (Condition: Si no tienes suficiente dinero contigo:)
                        - **Hemlock:** No tienes suficiente coins, vuelve cuando lo tengas
                      - (Condition: Si tienes suficiente dinero contigo:)
                        - (removes=coins)
                        - **Hemlock:** Muy bien, mantendré tus parches en abono. Simplemente mantenga su almacenamiento lleno.
                    - [Choice]: No.
                      - **Hemlock:** No tienes suficiente coins, vuelve cuando lo tengas
                - ((Después de ingresar 0:))
                  - **Hemlock:** Haz lo que quieras.
            - (Condition: Con supercompostaje queda por comprar:)
              - [Choice]: supercompost
                - {{Tinput|Pay for how many (max [number])?}}
                - ((Después de ingresar un número positivo:))
                  - [Menu]: ¿Pagar [número] coins?
                    - [Choice]: Sí.
                      - (Condition: Si no tienes suficiente dinero contigo:)
                        - **Hemlock:** No tienes suficiente coins, vuelve cuando lo tengas
                      - (Condition: Si tienes suficiente dinero contigo:)
                        - (removes=coins)
                        - **Hemlock:** Muy bien, mantendré tus parches en abono. Simplemente mantenga su almacenamiento lleno.
                    - [Choice]: No.
                      - **Hemlock:** No tienes suficiente coins, vuelve cuando lo tengas
                - ((Después de ingresar 0:))
                  - **Hemlock:** Haz lo que quieras.
            - (Condition: Con ultracompostaje queda por comprar:)
              - [Choice]: Ultracompost.
                - {{Tinput|Pay for how many (max [number])?}}
                - ((Después de ingresar un número positivo:))
                  - [Menu]: ¿Pagar [número] coins?
                    - [Choice]: Sí.
                      - (Condition: Si no tienes suficiente dinero contigo:)
                        - **Hemlock:** No tienes suficiente coins, vuelve cuando lo tengas
                      - (Condition: Si tienes suficiente dinero contigo:)
                        - (removes=coins)
                        - **Hemlock:** Muy bien, mantendré tus parches en abono. Simplemente mantenga su almacenamiento lleno.
                    - [Choice]: No.
                      - **Hemlock:** No tienes suficiente coins, vuelve cuando lo tengas
                - ((Después de ingresar 0:))
                  - **Hemlock:** Haz lo que quieras.
            - [Choice]: nada
              - (continue|refund)
        - (Condition: Sin compostaje queda por comprar:)
          - **Hemlock:** Parece que ya pagaste todo.
      - [Choice]: ¿Puedes dejar de hacer abono con parches por mí?
        - **Player:** ¿Puedes dejar de hacer abono con parches por mí?
          - ((Si no has pagado por el compostaje:))
            - **Hemlock:** No me habías pagado, así que no lo haría de todos modos.
          - ((Si has pagado por el compostaje:))
            - (continue|refund)
      - [Choice]: ¿Cuánto he pagado?
        - **Player:** ¿Cuánto abono usarás?
        - **Hemlock:** Usaremos [número] regular, [número] súper compost y [número] ultracompost. ¿Quieres recargar?
        - [Menu]: Selecciona una opción
          - [Choice]: Sí.
            - (above|top-up)
          - [Choice]: No.
            - **Hemlock:** ¿Quieres un reembolso entonces?
            - [Menu]: Selecciona una opción
              - [Choice]: Sí.
                - (Condition: Sin nada que reembolsar:)
                  - **Hemlock:** Parece que de todos modos no se te debe ningún reembolso.
                - (Condition: Con algo para reembolsar:)
                  - [Menu]: ¿Qué quieres reembolsar?
                    - (Condition: Sólo con abono normal se reembolsará:)
                      - [Choice]: Abono normal.
                        - {{Tinput|Refund how many (max [number])?}}
                        - ((Después de ingresar un número positivo:))
                          - (receives=coins)
                          - **Hemlock:** ¡Ahí lo tienes!
                        - ((Después de ingresar 0:))
                          - **Hemlock:** Haz lo que quieras.
                    - (Condition: Sólo con supercompost a reembolsar:)
                      - [Choice]: Supercompost.
                        - {{Tinput|Refund how many (max [number])?}}
                        - ((Después de ingresar un número positivo:))
                          - (receives=coins)
                          - **Hemlock:** ¡Ahí lo tienes!
                        - ((Después de ingresar 0:))
                          - **Hemlock:** Haz lo que quieras.
                    - (Condition: Sólo con ultracompost a reembolsar:)
                      - [Choice]: Ultracompost.
                        - {{Tinput|Refund how many (max [number])?}}
                        - ((Después de ingresar un número positivo:))
                          - (receives=coins)
                          - **Hemlock:** ¡Ahí lo tienes!
                        - ((Después de ingresar 0:))
                          - **Hemlock:** Haz lo que quieras.
                    - Nada.
                      - (end)
              - [Choice]: No.
                - (end)
      - [Choice]: ¿Puedo cambiar qué parches compostas?
        - (Condition: Si hay parches que se están compostando:)
          - ((A continuación solo se enumeran los parches que se están compostando:))
            - **Hemlock:** Actualmente usaremos su abono en:<br>Parches de árboles<br>Parches de huertos<br>Parches de lúpulo<br>Parches de arbustos<br>Parches de hierbas<br>Parches de flores<br>Parches especiales
            - (continue)
        - (Condition: Si hay parches que no se están convirtiendo en abono:)
          - ((A continuación, solo se enumeran los parches que no se están convirtiendo en abono:))
            - **Hemlock:** No usaremos su abono en:<br>Parches de árboles<br>Parches de huertos<br>Parches de lúpulo<br>Parches de arbustos<br>Parches de hierbas<br>Parches de flores<br>Parches especiales
            - (continue)
        - [Menu]: Selecciona una opción
          - [Choice]: Alternar parches de árbol.
            - **Hemlock:** ¿Quieres cambiar algo más?
            - [Menu]: Selecciona una opción
              - [Choice]: Sí.
                - (previous)
              - [Choice]: No.
                - (end)
          - [Choice]: Alternar parches de asignación.
            - **Hemlock:** ¿Quieres cambiar algo más?
            - [Menu]: Selecciona una opción
              - [Choice]: Sí.
                - (previous)
              - [Choice]: No.
                - (end)
          - [Choice]: Alternar parches de saltos.
            - **Hemlock:** ¿Quieres cambiar algo más?
            - [Menu]: Selecciona una opción
              - [Choice]: Sí.
                - (previous)
              - [Choice]: No.
                - (end)
          - [Choice]: Alternar parches de arbustos.
            - **Hemlock:** ¿Quieres cambiar algo más?
            - [Menu]: Selecciona una opción
              - [Choice]: Sí.
                - (previous)
              - [Choice]: No.
                - (end)
          - [Choice]: [More Options]
            - [Menu]: Selecciona una opción
              - [Choice]: Alternar parches de hierbas.
                - **Hemlock:** ¿Quieres cambiar algo más?
                - [Menu]: Selecciona una opción
                  - [Choice]: Sí.
                    - (previous2)
                  - [Choice]: No.
                    - (end)
              - [Choice]: Alternar parches de flores.
                - **Hemlock:** ¿Quieres cambiar algo más?
                - [Menu]: Selecciona una opción
                  - [Choice]: Sí.
                    - (previous2)
                  - [Choice]: No.
                    - (end)
              - [Choice]: Alternar parches varios.
                - **Hemlock:** ¿Quieres cambiar algo más?
                - [Menu]: Selecciona una opción
                  - [Choice]: Sí.
                    - (previous2)
                  - [Choice]: No.
                    - (end)
              - [Choice]: [Previous Options]
                - (previous)
      - [Choice]: Otros temas.
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: Háblame de ti.
            - **Player:** ¿Cómo llegaste a ser jardinero en Um? Mucha gente probablemente querría dejar de trabajar después de morir.
            - **Hemlock:** Bueno, verás, toda mi vida quise ser jardinero.
            - **Hemlock:** El olor de la tierra, la alegría que se siente al recoger un cultivo cuidado...
            - **Hemlock:** Pero tenía miedo de lo que la gente pensaría de mí...
            - **Hemlock:** Todos los jardineros eran duendes en ese momento, ¡y yo no me parecía en nada a un duende!
            - **Player:** Todavía no te pareces en nada a un duende.
            - **Hemlock:** ¡Exactamente! Entonces nunca me convertí en jardinero.
            - **Hemlock:** Sin embargo, después de la muerte, creé este pequeño jardín en Um.
            - **Hemlock:** Cuando llegó mi amigo duende, estaba preparado para lo peor...
            - **Hemlock:** 'Solo hay lugar para un jardinero en esta ciudad', esperaba que dijera. O algo parecido.
            - **Hemlock:** ¡Pero él ha estado notando pero aceptando! Al final resultó que, estaba más que feliz de jubilarse después de morir.
            - **Player:** Qué lindo.
            - **Hemlock:** De todos modos, ¿quieres que cuide tus herramientas agrícolas?
            - (above|farming-tools)
          - [Choice]: En realidad, estoy bien.
            - (arriba)

### Note produce


#### Sin productos a destacar

- **Hemlock:** No hay nada que pueda intercambiar.

#### Con productos a tener en cuenta

- (Se anotan todos los productos en backpack de el player).
- **Hemlock:** Aquí están tus billetes.

### Compost

- (above|top-up)

### Using items


#### Si Hemlock no puede registrar el artículo ni almacenarlo en la tienda Farming

- **Hemlock:** Lo siento, no tengo ningún billete para cambiar por ese artículo.

#### Si Hemlock puede anotar el artículo

- (Se anota todo el elemento en backpack de el player).
- El esqueleto cambia tu [item/items] por: [número] x [banknote/banknotes].
- ((Repetido en una ventana emergente:)
  - El esqueleto cambia tu [item/items] por: [número] x [banknote/banknotes].

#### Si el artículo se puede almacenar en la tienda Farming


##### Sin espacio para el artículo

- No puedes almacenar más de esos.

##### Con espacio para el artículo

- (removes=item)
- Agregas [número] x [Item] a la tienda.
