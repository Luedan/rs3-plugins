# Nhitpyx

- **Original Wiki Page**: [Transcript:Nhitpyx](https://runescape.wiki/w/Transcript%3ANhitpyx)
- **Letter**: `N`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Exchange

- ((Farming Store interface opens.))

### Talk to

- **Nhitpyx:** ¿Qué quieres entonces?
- **ELIGE...**
  - Almacenamiento de herramientas.
    - **¿QUÉ TE GUSTARÍA DECIR?**
      - ¿Qué herramientas puedes almacenar?
        - (continue|What can you store)
      - Abre tu tienda de herramientas, por favor.
        - ((Farming Store interface opens.))
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
        - ((With refund available:))
          - (continue|Do you want a refund then)
        - ((Without refund available:))
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
        - ((Only with composting toggled on for some patches, and only the patches toggled on are listed:))
          - **Nhitpyx:** Usaremos su abono en:<br>Parches de árboles<br>Parches de huertos<br>Parches de lúpulo<br>Parches de arbustos<br>Parches de hierbas<br>Parches de flores<br>Parches especiales<br>
          - (continue)
        - ((Only with composting toggled off for some patches, and only the patches toggled off are listed:))
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
            - ((Farming Store interface opens.))
          - ((Only if not asked last:))
            - ¿Qué puedes almacenar?
              - **Player:** {{AnchorText|What can you store}}?
              - **Nhitpyx:** No pensé que esto fuera complicado... Puedo agarrar un rastrillo, un sembrador, una pala, unas tijeras de podar, una regadera y una paleta, pero no esos de arqueología poco fiables.
              - **Nhitpyx:** También puedo guardar algunos cubos y espantapájaros, además de compost, supercompost y ultracompost.
              - **Nhitpyx:** También me han dicho que si me das tus productos agrícolas, debería cambiarlos por estos billetes.
              - **Nhitpyx:** Entonces, ¿quieres que cuide tus herramientas agrícolas?
              - (previous)
          - ((Only after asking "What can you store?":))
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
        - ((With refund available:))
          - **¿QUÉ QUIERES REEMBOLSAR?**
            - ((Only with normal compost to refund:))
              - Abono normal.
                - (continue|Refunding compost)
            - ((Only with supercompost to refund:))
              - Supercompost.
                - (continue|Refunding compost)
            - ((Only with ultracompost to refund:))
              - Ultracompost.
                - (continue|Refunding compost)
            - Nada.
              - (end)
        - ((Without refund available:))
          - **Nhitpyx:** Parece que de todos modos no se te debe ningún reembolso.
      - No.
        - (end)

#### Comprar abono

- ((The prompt "Pay for how many (max [number])?" is shown.))
- ((After entering a number:))
  - **¿PAGAR [número] COINS? NO PODRÁS RECUPERARLOS.**
    - Sí.
      - ((If a number greater than zero was entered and you have enough coins:))
        - (removes=coins)
        - **Nhitpyx:** Muy bien, mantendré tus parches en abono. Simplemente mantenga su almacenamiento lleno.
      - ((If zero was entered or you don't have enough coins:))
        - **Nhitpyx:** No tienes suficiente oro, ¡no lo haré gratis!
    - No.
      - **Nhitpyx:** No tienes suficiente oro, ¡no lo haré gratis!

#### Reembolso de abono

- ((The prompt "Refund how many (max [number])?" is shown.))
- ((After entering a number:))
  - (receives=coins)
  - **Nhitpyx:** ¡Ahí lo tienes!
