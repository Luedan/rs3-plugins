# Tool leprechaun

- **Original Wiki Page**: [Transcript:Tool leprechaun](https://runescape.wiki/w/Transcript%3ATool%20leprechaun)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At all Farming patches


#### Intercambio

- ((Farming Store interface opens.))

#### Habla con

- **Tool leprechaun:** ¡Ah, es un buen día! ¿Puedo ayudarte con el almacenamiento de herramientas, o con un viaje a Winkin's Farm, o qué?
- **Elige...**
  - Almacenamiento de herramientas.
    - **¿Qué te gustaría decir?**
      - ¿Qué herramientas puedes almacenar?
        - **Player:** ¿Qué puedes almacenar?
        - **Tool leprechaun:** Nos quedaremos con tu rastrillo, sembrador, pala, tijeras de podar, regadera y paleta, pero ten en cuenta que no es una de esas paletas elegantes que solo usan los arqueólogos.
        - **Tool leprechaun:** También te quitaremos algunos cubos y espantapájaros de las manos, e incluso tu abono, supercompost y ultracompost. Hay espacio en nuestro cobertizo para mucho abono, así que tráelo.
        - **Tool leprechaun:** Además, si nos entrega sus productos Farming, es posible que podamos convertirlos en billetes.
        - **Tool leprechaun:** Entonces, ¿quieres usar la tienda?
        - **¿Qué te gustaría decir?**
          - Sí, por favor.
            - **Player:** Sí, por favor.
            - ((Farming Store interface opens.))
          - ¿Qué haces con las herramientas que estás almacenando?
            - **Player:** ¿Qué haces con las herramientas que almacenas? ¡No caben todos en tus bolsillos!
            - **Tool leprechaun:** Los duendes tenemos un cobertizo donde los guardamos. Es un cobertizo mágico, por lo que puedes recuperar tus objetos de cualquiera de nosotros, los duendes, cuando quieras. ¡Te ahorras tener que cargar un montón de cosas por todo el país!
            - **Tool leprechaun:** Entonces... ¿quieres usar la tienda?
            - **¿Qué te gustaría decir?**
              - {{Sic|Yes please.}}
                - **Player:** Sí, por favor.
                - ((Farming Store interface opens.))
              - ¿Qué puedes almacenar?
                - (arriba)
              - No gracias, guardaré mis cosas.
                - (abajo)
          - No gracias, guardaré mis cosas.
            - **Player:** No, gracias, guardaré mis cosas.
            - **Tool leprechaun:** Debes ser más tonto de lo que pareces si te gusta llevar tus herramientas a todas partes.
      - Abre tu tienda de herramientas, por favor.
        - ((Farming Store interface opens.))
      - En realidad, estoy bien.
        - **Player:** En realidad, estoy bien.
  - La granja de Winkin.
    - **¿Qué te gustaría decir?**
      - ¿Puedes llevarme a la granja de Winkin?
        - **Player:** ¿Puedes llevarme a Winkin's Farm?
        - **Tool leprechaun:**{{RSChat|Avach nimporto!}}
        - (Action: Tool leprechaun te teletransporta a Winkin's Farm.)
      - En realidad, estoy bien.
        - (arriba)
  - Compostaje.
    - **¿Qué te gustaría decir?**
      - ¿Pueden hacerme abono con parches?
        - **Player:** ¿Pueden hacerme abono con parches?
        - **Tool leprechaun:** Claro, lo haremos en cada uno de tus parches usando el abono que tú nos das, pero no gratis.
        - **Tool leprechaun:** 500 de oro para abono normal, 1500 de oro para supercompost o 2500 de oro para ultracompost. Paga hasta 60.000 por adelantado, pero no hay reembolsos.
        - ((With composting left to buy:))
          - **¿Qué quieres recargar?**
            - ((With normal composting left to buy:))
              - Abono normal.
                - ((A number input with prompt "Pay for how many (max 60,000)?" opens.))
                - ((After entering a positive number:))
                  - **¿Pagar [número] coins?**
                    - Sí.
                      - ((If you do not have sufficient money with you:))
                        - **Tool leprechaun:** Parece que no puedes pagar. Vuelve cuando puedas.
                      - ((If you have sufficient money with you:))
                        - (removes=coins)
                        - **Tool leprechaun:** Ya no te preocupes por el abono, ¡simplemente mantén tu almacenamiento lleno!
                    - No.
                      - **Tool leprechaun:** Parece que no puedes pagar. Vuelve cuando puedas.
                - ((After entering 0:))
                  - **Tool leprechaun:** Haz lo que quieras.
            - ((With supercomposting left to buy:))
              - Supercompost.
                - ((A number input with prompt "Pay for how many (max 60,000)?" opens.))
                - ((After entering a positive number:))
                  - **¿Pagar [número] coins?**
                    - Sí.
                      - ((If you do not have sufficient money with you:))
                        - **Tool leprechaun:** Parece que no puedes pagar. Vuelve cuando puedas.
                      - ((If you have sufficient money with you:))
                        - (removes=coins)
                        - **Tool leprechaun:** Ya no te preocupes por el abono, ¡simplemente mantén tu almacenamiento lleno!
                    - No.
                      - **Tool leprechaun:** Parece que no puedes pagar. Vuelve cuando puedas.
                - ((After entering 0:))
                  - **Tool leprechaun:** Haz lo que quieras.
            - ((With ultracomposting left to buy:))
              - Ultracompost.
                - ((A number input with prompt "Pay for how many (max 60,000)?" opens.))
                - ((After entering a positive number:))
                  - **¿Pagar [número] coins?**
                    - Sí.
                      - ((If you do not have sufficient money with you:))
                        - **Tool leprechaun:** Parece que no puedes pagar. Vuelve cuando puedas.
                      - ((If you have sufficient money with you:))
                        - (removes=coins)
                        - **Tool leprechaun:** Ya no te preocupes por el abono, ¡simplemente mantén tu almacenamiento lleno!
                    - No.
                      - **Tool leprechaun:** Parece que no puedes pagar. Vuelve cuando puedas.
                - ((After entering 0:))
                  - **Tool leprechaun:** Haz lo que quieras.
            - nada
              - (continue|refund)
        - ((Without composting left to buy:))
          - **Tool leprechaun:** Parece que ya pagaste todo.
      - ¿Puedes dejar de hacer abono con parches por mí?
        - **Player:** ¿Puedes dejar de hacer abono con parches por mí?
          - ((If you have not paid for composting:))
            - **Tool leprechaun:** No has pagado de todos modos, no estaba sucediendo de todos modos.
          - ((If you have paid for composting:))
            - (continue|refund)
      - ¿Cuánto he pagado?
        - **Player:** ¿Cuánto abono usarás?
        - **Tool leprechaun:** Usaremos [número] regular, supercompost [número] y ultracompost [número]. ¿Quieres recargar?
        - **Seleccione una opción**
          - Sí.
            - (above|top-up)
          - No.
            - **Tool leprechaun:** Entonces, ¿no crees que estás buscando un reembolso? Puedo devolverte todo el dinero que me diste originalmente.
            - **Seleccione una opción**
              - Sí.
                - ((Without anything to refund:))
                  - **Tool leprechaun:** ¡Parece que ya te han reembolsado todo! Uf...
                - ((With something to refund:))
                  - **¿Qué quieres reembolsar?**
                    - ((Only with normal compost to refund:))
                      - Abono normal.
                        - ((A number input opens with prompt "Refund how many (max [number])?"))
                        - ((After entering a positive number:))
                          - (receives=coins)
                          - **Tool leprechaun:** ¡Ahí lo tienes!
                        - ((After entering 0:))
                          - **Tool leprechaun:** Haz lo que quieras.
                    - ((Only with supercompost to refund:))
                      - Supercompost.
                        - ((A number input opens with prompt "Refund how many (max [number])?"))
                        - ((After entering a positive number:))
                          - (receives=coins)
                          - **Tool leprechaun:** ¡Ahí lo tienes!
                        - ((After entering 0:))
                          - **Tool leprechaun:** Haz lo que quieras.
                    - ((Only with ultracompost to refund:))
                      - Ultracompost.
                        - ((A number input opens with prompt "Refund how many (max [number])?"))
                        - ((After entering a positive number:))
                          - (receives=coins)
                          - **Tool leprechaun:** ¡Ahí lo tienes!
                        - ((After entering 0:))
                          - **Tool leprechaun:** Haz lo que quieras.
                    - Nada.
                      - (end)
              - No.
                - (end)
      - ¿Puedo cambiar qué parches compostas?
        - ((If there are patches that the tool leprechauns are composting:))
          - ((In the following only the patches that the leprechauns are composting are listed:))
            - **Tool leprechaun:** Actualmente usaremos su abono en:<br>Parches de árboles<br>Parches de huertos<br>Parches de lúpulo<br>Parches de arbustos<br>Parches de hierbas<br>Parches de flores<br>Parches especiales
            - (continue)
        - ((If there are patches that the tool leprechauns are not composting))
          - ((In the following only the patches that the leprechauns are not composting are listed:))
            - **Tool leprechaun:** No usaremos su abono en<br>Parches de árboles<br>Parches de huertos<br>Parches de lúpulo<br>Parches de arbustos<br>Parches de hierbas<br>Parches de flores<br>Parches especiales
            - (continue)
        - **Seleccione una opción**
          - Alternar parches de árbol
            - **Tool leprechaun:** ¿Quieres cambiar un poco más?
            - **Seleccione una opción**
              - Sí.
                - (previous)
              - No.
                - (end)
          - Alternar parches de asignación
            - **Tool leprechaun:** ¿Quieres cambiar un poco más?
            - **Seleccione una opción**
              - Sí.
                - (previous)
              - No.
                - (end)
          - Alternar parches de lúpulo
            - **Tool leprechaun:** ¿Quieres cambiar un poco más?
            - **Seleccione una opción**
              - Sí.
                - (previous)
              - No.
                - (end)
          - Alternar parches de arbustos
            - **Tool leprechaun:** ¿Quieres cambiar un poco más?
            - **Seleccione una opción**
              - Sí.
                - (previous)
              - No.
                - (end)
          - [Más opciones]
            - **Seleccione una opción**
              - Alternar parches de hierbas
                - **Tool leprechaun:** ¿Quieres cambiar un poco más?
                - **Seleccione una opción**
                  - Sí.
                    - (previous2)
                  - No.
                    - (end)
              - Alternar parches de flores
                - **Tool leprechaun:** ¿Quieres cambiar un poco más?
                - **Seleccione una opción**
                  - Sí.
                    - (previous2)
                  - No.
                    - (end)
              - Alternar parches varios
                - **Tool leprechaun:** ¿Quieres cambiar un poco más?
                - **Seleccione una opción**
                  - Sí.
                    - (previous2)
                  - No.
                    - (end)
              - [Opciones anteriores]
                - (previous)
      - En realidad, estoy bien.
        - (arriba)
  - ((If you have any rewards to collect from the Evil Tree:))
    - Otros temas.
      - ¿Puedo recoger mis recompensas del Árbol del Mal?
        - **Player:** ¿Puedo recoger mis recompensas del Árbol del Mal?
          - **Tool leprechaun:** Sin duda, sin duda.
          - El duende te entrega tus recompensas [rewards list]. ¡También encontraste algunas semillas [type of seed]!
          - El duende chasquea los dedos y se te otorga una habilidad mágica para almacenar registros durante los próximos X minutos.
          - **Tool leprechaun:** ¡Gracias por tu ayuda, [lad/lass]! Durante los próximos X minutos, si tienes un inventario completo, cualquier roble, sauce, arce, sí, mágico o anciano logs que tengas, te teletransportaré directamente a tu banco.
          - **Tool leprechaun:** También solucionaré un poco de magia, lo que hará que sea menos probable que tales árboles normales, robles, sauces, arces, tejos o mágicos, pero esto solo funcionará en algunos árboles que encuentres mientras deambulas, no en los que hayas cultivado tú mismo.
          - **Player:** ¡Gracias!
      - En realidad, estoy bien.
        - (arriba)

#### Nota producir


##### Sin productos a tener en cuenta

- **Tool leprechaun:** No hay nada que pueda intercambiar.

##### Con productos a tener en cuenta

- (Se anotan todos los productos en backpack de el player).
- **Tool leprechaun:** Aquí tienes algunos billetes.

#### Abono

- (above|top-up)

#### Usando elementos


##### Si los duendes de herramientas no pueden notar el artículo

- **Tool leprechaun:** No, no tengo billetes para cambiar por ese artículo.

##### Si los duendes de herramientas pueden notar el artículo

- (Se anota todo el elemento en backpack de el player).
- El duende cambia tu [item/items] por: [número] x [banknote/banknotes].
- (pop-up)
  - (Pop-up: The leprechaun exchanges your [item/items] for: [number] x [banknote/banknotes].|color=#00FF00)

### At the allotment patch south of Falador


#### Intentando cambiar repollo(s) por billetes

- **Tool leprechaun:** ¿Un repollo? No vayas a mostrarme tu repollo; ¡Toda esta granja apesta a cosas! Llévatelo y cámbialo en otro lugar.

### At the Herblore Habitat


#### Preguntar "¿Qué herramientas puedes almacenar?"

- **Tool leprechaun:** ¡Ah, es un buen día, sin duda! ¿Puedo ayudarte con el almacenamiento de herramientas, o con un viaje a Winkin's Farm, o qué?
  - Almacenamiento de herramientas.
    - ¿Qué herramientas puedes almacenar?
      - **Player:** ¿Qué puedes almacenar?
      - **Tool leprechaun:** Nos quedaremos con tu rastrillo, sembrador, pala, tijeras de podar, regadera y paleta, pero ten en cuenta que no es una de esas paletas elegantes que solo usan los arqueólogos.
      - **Tool leprechaun:** También te quitaremos algunos cubos y espantapájaros de las manos, e incluso tu abono y supercompost. Hay espacio en nuestro cobertizo para mucho abono, así que tráelo.
      - **Tool leprechaun:** Además, si nos entregas tus productos Farming, es posible que podamos convertirlos en billetes.
      - **Tool leprechaun:** También podemos almacenar algunas de las pociones que ayudan a mantener este hábitat funcionando sin problemas. Sólo pociones de 3 dosis, ojo: no nos vamos a ocupar de tus vacías.
      - **Tool leprechaun:** Entonces, ¿quieres usar la tienda?
        - Sí, por favor.
          - **Player: **Sí, por favor.
          - **Tool leprechaun:** ¿Qué te gustaría almacenar?
            - Herramientas Farming.
              - *(Se abre la tienda Farming)*
            - Pociones de vid.
              - *(Se abre la tienda de pociones)*
            - Cancelar
        - ¿Qué haces con las herramientas que estás almacenando?
          - *(Igual que arriba)*
        - No gracias, guardaré mis cosas.
          - *(Igual que arriba)*

#### Opción seleccionada "Intercambio"

- ¿Qué te gustaría intercambiar?
  - Herramientas Farming.
    - *(Se abre la tienda Farming)*
  - Pociones de vid.
    - *(Se abre la tienda de pociones)*
  - Cancelar

### At Zolarea

- **Tool leprechaun:** ¡Dios, qué lindo día! Ahora, ¿puedo ayudarte con el almacenamiento de herramientas, con un viaje a la granja de Winkin o con algo más?
- **ELIGE...**
  - Almacenamiento de herramientas.
    - **¿QUÉ TE GUSTARÍA DECIR?**
      - ¿Qué herramientas puedes almacenar?
        - **Player:** ¿Qué puedes almacenar?
          - **Tool leprechaun:** Puedo sostener tu rastrillo, sembrador, pala, tijeras de podar, regadera y paleta, pero no esas paletas que se usan en arqueología.
          - **Tool leprechaun:** También puedo guardarte algunos cubos y espantapájaros, e incluso compost, supercompost y ultracompost. Por supuesto, el abono es esencial para una buena agricultura, así que puedo almacenar mucho para ti.
          - **Tool leprechaun:** Además, si me entregas tus productos agrícolas, tal vez pueda convertirlos en billetes.
          - **Tool leprechaun:** Entonces, ¿te gustaría que cuidara tus herramientas agrícolas?
          - **¿QUÉ TE GUSTARÍA DECIR?**
            - Sí, por favor.
              - **Player:** Sí, por favor.
              - ((Farming Store interface opens.))
            - ¿Qué haces con las herramientas que estás almacenando?
              - **Player:** ¿Qué haces con las herramientas que almacenas? ¡No caben todos en tus bolsillos!
              - **Tool leprechaun:** Por supuesto que no. Tengo un cobertizo para herramientas. Aunque es un cobertizo bastante curioso. A veces, los elementos simplemente parecen aparecer allí.
              - **Tool leprechaun:** Entonces, ¿te gustaría que cuidara tus herramientas agrícolas?
              - **¿QUÉ TE GUSTARÍA DECIR?**
                - {{Sic|Yes please.}}
                  - **Player:** Sí, por favor.
                  - ((Farming Store interface opens.))
                - ¿Qué puedes almacenar?
                  - (arriba)
                - No gracias, guardaré mis cosas.
                  - (abajo)
            - No gracias, guardaré mis cosas.
              - **Player:** No, gracias, guardaré mis cosas.
              - **Tool leprechaun:** Bueno, estaré aquí si alguna vez decides que puedo ser de utilidad.
      - Abre tu tienda de herramientas, por favor.
        - ((Farming Store interface opens.))
      - En realidad, estoy bien.
        - **Player:** En realidad, estoy bien.
  - La granja de Winkin.
    - (arriba)
  - Compostaje.
    - (arriba)
  - Otros temas.
    - Háblame de ti.
      - **Player:** ¿Qué haces aquí en Zolarea?
      - **Tool leprechaun:** Oh, a mí me encantan las aventuras.
      - **Tool leprechaun:** Escuché a algunos de los magos en el Wizards' Tower parlotear sobre este planeta recién descubierto y logré conseguir un viaje hasta aquí para verlo yo mismo.
      - **Tool leprechaun:** Y vaya, ¡me alegro de haberlo hecho! Este lugar está repleto de hermosas flores estelares. Te lo digo, el suelo aquí es perfecto para cultivarlas.
      - **Tool leprechaun:** Pero ya basta de mí, ¿quieres que cuide tus herramientas agrícolas?
        - **¿QUÉ TE GUSTARÍA DECIR?**
          - Sí, por favor.
            - (arriba)
          - ¿Qué puedes almacenar?
            - (arriba)
          - No gracias, guardaré mis cosas.
            - (arriba)
    - En realidad, estoy bien.
      - **Player:** En realidad, estoy bien.

### Applying compost to a patch

- El tool leprechaun utiliza automáticamente [compost/supercompost/ultracompost] en su parche.  <!-- filtered -->
