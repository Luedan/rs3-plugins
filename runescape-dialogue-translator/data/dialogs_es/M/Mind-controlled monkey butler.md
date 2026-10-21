# Mind-controlled monkey butler

- **Original Wiki Page**: [Transcript:Mind-controlled monkey butler](https://runescape.wiki/w/Transcript%3AMind-controlled%20monkey%20butler)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Missing dialogue from Invention Guild before hiring and firing dialogue from POH}}

### In the Invention Guild

{{Cleanup|The dialogue title may be inaccurate, the "yes" branch may be missing dialogue, and the "no" branch is missing}}
- ¿Quieres contratar el mind-controlled monkey butler?
  - Sí.
    - **Mind-controlled monkey butler:** ¡Feliz! Steve tiene un nuevo Maestro.
    - (Action: el mayordomo desaparece)
  - No.
    - {{Transcript missing}}

### In a player-owned house


#### Llamando al mayordomo

- (Action: El mayordomo se teletransporta junto a el player.)
- **Mind-controlled monkey butler:** Feliz. ¿El Maestro necesita a Steve?
- (continue|butler-options)

#### Hablando con el mayordomo

- **Mind-controlled monkey butler:** Feliz. ¿El Maestro necesita ayuda?
- Seleccione una opción
  - Ir al banco/aserradero...
    - Seleccione una opción
      - llevar algo al banco
        - **Player:** ¿Puedes llevarme algo al banco?
        - **Mind-controlled monkey butler:** ¡Feliz! Dáselo a Steve. Steve lleva al banco.
      - Trae algo del banco
        - ¿Qué te gustaría del banco?
          - *Conjunto de opciones 1*
            - *(Si el player ha utilizado previamente al mayordomo para recuperar algo del banco:)*
              - Trae otro [quantity] [item].
            - planks de madera.
            - Roble planks.
            - Teca planks.
          - *Conjunto de opciones 2*
            - Caoba planks.
            - Arcilla blanda.
            - Ladrillo de piedra caliza.
            - Barra de acero.
          - *Conjunto de opciones 3*
            - Tela.
            - Pan de oro.
            - Bloque de mármol.
            - Magic vivienda de piedra.
          - Más...
            - ((Recorre los conjuntos de opciones anteriores.))
        - (Se abre la interfaz con el mensaje "Ingresar monto:".)
        - (Action: el mayordomo desaparece)
        - El sirviente va al banco.
        - (Action: El mayordomo reaparece junto a el player.)
        - (receives=some or all of the item(s) solicitado, dependiendo del espacio libre en backpack)
        - *(Si el player solicitó planks y tiene una caja de tablones con espacio para guardarlos:)*
          - **Mind-controlled monkey butler:** ¡Feliz! Steve puso las cosas de la Maestra en la caja de tablones de la Maestra.
        - *(Si el player no tenía suficiente espacio en el backpack para contener dos o más elementos:)*
          - **Mind-controlled monkey butler:** ¡Feliz! Steve guarda las cosas del Maestro hasta que el Maestro las necesite.
          - Seleccione una opción
            - Llévalo de vuelta al banco
              - **Player:** Llévalo al banco, por favor.
              - **Mind-controlled monkey butler:** Feliz. Steve devuelve artículos.
              - (Action: El mayordomo desaparece y luego reaparece junto a el player.)
            - gracias
              - **Player:** Gracias.
        - *(Si el player no tenía suficiente espacio en backpack para contener un elemento:)*
          - **Mind-controlled monkey butler:** ¡Feliz! Steve sostiene la cosa del Maestro hasta que el Maestro la necesite.
          - (above|butler-item-overflow)
        - *(De lo contrario:)*
          - **Mind-controlled monkey butler:** ¡Feliz! Steve regresa con las cosas del Maestro.
      - Lleva algo al aserradero.
        - **Mind-controlled monkey butler:** ¡Feliz! Steve va al aserradero.
  - Varios...
    - Seleccione una opción
      - hacer té
        - **Mind-controlled monkey butler:** ¡Feliz! Steve prepara té.
        - (Action: El mayordomo aparece en la cocina y prepara té, regresando a el player una vez terminado.)
        - **Mind-controlled monkey butler:** Feliz. ¿El amo quiere leche?
        - Seleccione una opción
          - si por favor
            - **Player:** Sí, por favor.
            - (receives=a milky cup of tea)
          - No gracias
            - **Player:** No, gracias.
            - (receives=a cup of tea)
          - En realidad no quiero ninguno
            - **Player:** En realidad no quiero ninguno.
      - servir la cena
        - **Mind-controlled monkey butler:** ¡Feliz! Servicio.
        - ''(Si el player no tiene nada construido en el espacio de la mesa del comedor:)
          - **Mind-controlled monkey butler:** Confundido. ¿Mesa? Falta mesa.
        - *(Si el player no tiene despensa, estufa, fregadero y estantes incorporados en la cocina:)*
          - **Mind-controlled monkey butler:** Confundido. Sin cocina. Steve necesita cocina.
          - Tu cocina debe contener:<br>Adespensa<br>Aestufa<br>Afregadero<br>Estantes de cocina
        - *(De lo contrario:)*
          - (Action: El mayordomo aparece en la cocina y prepara la cena, colocándola sobre la mesa del comedor una vez terminada.)
      - servir bebidas
        - **Player:** Sirva bebidas, por favor.
        - **Mind-controlled monkey butler:** Feliz. ¡Steve prepara bebidas!
        - *(Si el player no tiene nada construido en el espacio del barril de la cocina:)*
          - **Mind-controlled monkey butler:** Confundido. El Maestro no tiene tragos grandes para hacer tragos pequeños.
        - *(De lo contrario:)*
          - (Action: El mayordomo aparece en la cocina y prepara bebidas, regresando a el player una vez terminadas.)
          - **Mind-controlled monkey butler:** ¡Feliz! ¿El Maestro acepta una bebida?
          - Seleccione una opción
            - si por favor
              - **Player:** ¡Sí, por favor!
              - (receives=the drink corresponding to whichever beer barrel is built in the barrel space)
              - **Mind-controlled monkey butler:** Feliz. Steve espera que al Maestro le guste.
            - No gracias
              - **Player:** No, gracias.
            - algo mas
              - (initial|butler-options)
      - Saludar a los invitados
        - **Player:** Quédese en la entrada y salude a los invitados.
        - **Mind-controlled monkey butler:** ¡Feliz! Steve saluda a los amigos de la Maestra.
        - (Action: El mayordomo aparece junto al portal.)
  - deja de seguirme
    - (El mayordomo ahora deambula por la zona.)
  - estas despedido
    - ¿De verdad quieres despedir a tu sirviente?
      - Sí.
        - {{Transcript missing}}
      - No.
        - (end)

#### Hablando con el mayordomo mientras sostiene artículos traídos del banco

- (arriba2|objetos-de-mayordomo)

#### Usando un objeto en el mayordomo

- ¿Llevar este artículo al banco?
  - banco
    - (Se abre la interfaz con el mensaje "Ingresar monto:".)
    - (Action: El mayordomo desaparece, saca los artículos del backpack y los deposita en el banco.)
    - El sirviente va al banco.
  - Cancelar
    - (end)
