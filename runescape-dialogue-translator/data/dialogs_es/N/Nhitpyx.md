# Nhitpyx

- **Original Wiki Page**: [Transcript:Nhitpyx](https://runescape.wiki/w/Transcript%3ANhitpyx)
- **Letter**: `N`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Exchange

- ((Se abre la interfaz de la tienda Farming.))

### Talk to

- **Nhitpyx:** ¿Qué quieres entonces?
- **ELIGE...**
  - Almacenamiento de herramientas.
    - **¿QUÉ TE GUSTARÍA DECIR?**
      - ¿Qué herramientas puedes almacenar?
        - (continue|What can you store)
      - Abre tu tienda de herramientas, por favor.
        - ((Se abre la interfaz de la tienda Farming.))
      - En realidad, estoy bien.
        - **Player:** En realidad, estoy bien.
  - La granja de Winkin.
    - **¿QUÉ TE GUSTARÍA DECIR?**
      - ¿Puedes llevarme a la granja de Winkin?
        - **Player:** ¿Puedes llevarme a Winkin's Farm?
        - **Nhitpyx:** {{RSChat|Avach nimporto!}}
        - (Action: el player es teletransportado a Winkin's Farm.)
      - En realidad, estoy bien.
        - **Player:** En realidad, estoy bien.
  - Compostaje.
    - **¿QUÉ TE GUSTARÍA DECIR?**
      - ¿Pueden hacerme abono con parches?
        - **Player:** ¿Pueden hacerme abono con parches?
        - **Nhitpyx:** Vaya, alguien es un vago... Lo haré, pero te costará.
        - **Nhitpyx:** 500 de oro para abono normal, 1500 de oro para supercompost o 2500 de oro para ultracompost. Paga hasta 60.000 por adelantado, pero no hay reembolsos.
        - (continue|Compost)
      - ¿Puedes dejar de hacer abono con parches por mí?
        - **Player:** ¿Puedes dejar de hacer abono con parches por mí?
        - ((Con reembolso disponible:))
          - (continue|Do you want a refund then)
        - ((Sin reembolso disponible:))
          - **Nhitpyx:** No me habías pagado, así que no lo haría de todos modos.
      - ¿Cuánto he pagado?
        - **Player:** ¿Cuánto abono usarás?
        - **Nhitpyx:** Usaremos [número] regular, supercompost [número] y ultracompost [número]. ¿Quieres recargar?
        - **SELECCIONA UNA OPCIÓN**
          - Sí.
            - (continue|Compost)
          - No.
            - (continue|Do you want a refund then)
      - ¿Puedo cambiar qué parches compostas?
        - ((Solo con el compostaje activado para algunos parches, y solo se enumeran los parches activados:))
          - **Nhitpyx:** Usaremos su abono en:<br>Parches de árboles<br>Parches de huertos<br>Parches de lúpulo<br>Parches de arbustos<br>Parches de hierbas<br>Parches de flores<br>Parches especiales<br>
          - (continue)
        - ((Solo con el compostaje desactivado para algunos parches, y solo se enumeran los parches desactivados:))
          - **Nhitpyx:** No usaremos su abono en:<br>Parches de árboles<br>Parches de huertos<br>Parches de lúpulo<br>Parches de arbustos<br>Parches de hierbas<br>Parches de flores<br>Parches especiales<br>
          - (continue)
        - **SELECCIONA UNA OPCIÓN**
          - Alternar parches de árbol.
            - (continue|After toggling a patch)
          - Alternar parches de asignación.
            - (continue|After toggling a patch)
          - Alternar parches de saltos.
            - (continue|After toggling a patch)
          - Alternar parches de arbustos.
            - (continue|After toggling a patch)
          - [Más opciones]
            - **SELECCIONA UNA OPCIÓN**
              - Alternar parches de hierbas.
                - (continue|After toggling a patch)
              - Alternar parches de flores.
                - (continue|After toggling a patch)
              - Alternar parches varios.
                - (continue|After toggling a patch)
              - [Opciones anteriores]
                - (previous2)
      - En realidad, estoy bien.
        - **Player:** En realidad, estoy bien.
  - Otros temas.
    - **¿QUÉ TE GUSTARÍA DECIR?**
      - ¿No eres un poco alto para ser un duende?
        - **Player:** ¿No eres un poco alto para ser un duende?
        - **Nhitpyx:** ¿Qué? <br>A ¿No eres un poco mayor para preguntas tan estúpidas?
        - **Player:** Bueno, estás cuidando las herramientas como lo hacen los duendes.
        - **Nhitpyx:** Le juro por Guthix que me estoy haciendo demasiado mayor para esto. Ahora, ¿quieres que cuide tus herramientas agrícolas?
        - **¿QUÉ TE GUSTARÍA DECIR?**
          - Sí, por favor.
            - **Player:** Sí, por favor.
            - ((Se abre la interfaz de la tienda Farming.))
          - ((Sólo si no se le preguntó al final:))
            - ¿Qué puedes almacenar?
              - **Player:** {{AnchorText|What can you store}}?
              - **Nhitpyx:** No pensé que esto fuera complicado... Puedo agarrar un rastrillo, un sembrador, una pala, unas tijeras de podar, una regadera y una paleta, pero no esos de arqueología poco fiables.
              - **Nhitpyx:** También puedo guardar algunos cubos y espantapájaros, además de compost, supercompost y ultracompost.
              - **Nhitpyx:** También me han dicho que si me das tus productos agrícolas, debería cambiarlos por estos billetes.
              - **Nhitpyx:** Entonces, ¿quieres que cuide tus herramientas agrícolas?
              - (previous)
          - ((Sólo después de preguntar "¿Qué puedes almacenar?":))
            - ¿Qué haces con las herramientas que estás almacenando?
              - **Player:** ¿Qué haces con las herramientas que guardas?<br>¡No es posible que quepan todas en tus bolsillos!
              - **Nhitpyx:** Qué... Bueno, obviamente no los guardo en mis bolsillos, mira, tiendo a tirarlos detrás del viejo contenedor de abono que hay allí con las herramientas del otro aventurero.
              - **Nhitpyx:** Ahora, ¿quieres que cuide tus herramientas o no?
          - No gracias, guardaré mis cosas.
            - **Player:** No, gracias, guardaré mis cosas.
            - **Nhitpyx:** ¿Está bien? Tu pérdida.
      - En realidad, estoy bien.
        - **Player:** En realidad, estoy bien.

#### Después de alternar un parche

- **Nhitpyx:** ¿Quieres cambiar algo más?
- **SELECCIONA UNA OPCIÓN**
  - Sí.
    - (above|patches)
  - No.
    - (end)

### Note produce


#### Con elementos a tener en cuenta

- (Action: Se anotan los elementos.)
- **Nhitpyx:** Aquí están tus billetes.

#### Sin elementos a destacar

- **Nhitpyx:** No hay nada que pueda intercambiar.

### Compost

- **¿QUÉ QUIERES RECARGAR?**
  - Abono normal.
    - (continue|Buying compost)
  - Supercompost.
    - (continue|Buying compost)
  - Ultracompost.
    - (continue|Buying compost)
  - Nada.
    - **Nhitpyx:** {{AnchorText|Do you want a refund then}}?
    - **SELECCIONA UNA OPCIÓN**
      - Sí.
        - ((Con reembolso disponible:))
          - **¿QUÉ QUIERES REEMBOLSAR?**
            - ((Sólo con abono normal se reembolsará:))
              - Abono normal.
                - (continue|Refunding compost)
            - ((Sólo con supercompost a reembolsar:))
              - Supercompost.
                - (continue|Refunding compost)
            - ((Sólo con ultracompost a reembolsar:))
              - Ultracompost.
                - (continue|Refunding compost)
            - Nada.
              - (end)
        - ((Sin reembolso disponible:))
          - **Nhitpyx:** Parece que de todos modos no se te debe ningún reembolso.
      - No.
        - (end)

#### Comprar abono

- ((El mensaje "¿Pagar por cuántos (máx. [número])?" se muestra.))
- ((Después de ingresar un número:))
  - **¿PAGAR [número] COINS? NO PODRÁS RECUPERARLOS.**
    - Sí.
      - ((Si ingresó un número mayor que cero y tiene suficiente coins:))
        - (removes=coins)
        - **Nhitpyx:** Muy bien, mantendré tus parches en abono. Simplemente mantenga su almacenamiento lleno.
      - ((Si ingresó cero o no tiene suficiente coins:))
        - **Nhitpyx:** No tienes suficiente oro, ¡no lo haré gratis!
    - No.
      - **Nhitpyx:** No tienes suficiente oro, ¡no lo haré gratis!

#### Reembolso de abono

- ((El mensaje "¿Cuántos reembolsos (máx. [número])?" se muestra.))
- ((Después de ingresar un número:))
  - (receives=coins)
  - **Nhitpyx:** ¡Ahí lo tienes!
