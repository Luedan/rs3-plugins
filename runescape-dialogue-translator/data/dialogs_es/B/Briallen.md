# Briallen

- **Original Wiki Page**: [Transcript:Briallen](https://runescape.wiki/w/Transcript%3ABriallen)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pay


#### Con el matorral vacío

- **Briallen:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.

#### Con el arbusto creciendo


##### Sin los elementos requeridos

- **Briallen:** Quiero [número] [items] para eso.
- **Player:** Gracias, tal vez en otro momento.

##### Con los elementos requeridos, sin confirmación desactivada

- [Menu]: ¿Pagar [número] [items]?
  - [Choice]: Sí.
    - (removes=the requested items)
    - **Briallen:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
    - El jardinero ahora se ocupará del parche por usted.
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (arriba)
  - [Choice]: No.
    - (end)

##### Con los elementos requeridos, con la confirmación desactivada

- (removes=the requested items)
- **Briallen:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
- El jardinero ahora se ocupará del parche por usted.

##### Habiendo pagado ya por la protección

- **Briallen:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
- **Player:** Oh, lo siento, lo olvidé.

#### Con el arbusto completamente desarrollado

- **Briallen:** Ese parche ya está completamente desarrollado. No sé qué quieres que haga con él.

#### Si el arbusto es una hiedra venenosa

- **Briallen:** No es necesario que cuide esa hiedra venenosa.
- **Player:** ¿En serio?
- **Briallen:** Sí, la hiedra venenosa es un material bastante resistente y la mayoría de los animales evitarán comerla.
- **Briallen:** Por lo tanto, no hay razón para preocuparse por eso.
- **Player:** Genial.

### Talk to


#### Diálogo estándar

- [Menu]: Elige una opción:
  - [Choice]: ¿Cuidarías mis cultivos por mí?
    - **Player:** ¿Cuidarías mis cultivos por mí?
    - **Briallen:** Podría hacerlo. Sólo puedo proteger la mente del bosque.
    - [Menu]: Selecciona una opción
      - [Choice]: Está bien.
        - (Condition: Si el player no tiene cultivos en el parche:)
          - **Briallen:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.
        - (Condition: Si el player tiene cultivos completamente desarrollados plantados en el parche:)
          - **Briallen:** ¡Ese parche ya está completamente desarrollado! ¡No sé qué quieres que haga con él!
        - (Condition: Si los cultivos en el parche aún no están completamente desarrollados pero el player ya le pagó al jardinero:)
          - **Briallen:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
          - **Player:** Oh, lo siento, lo olvidé.
        - (Condition: Si está creciendo un arbusto de hiedra venenosa:)
          - **Briallen:** No es necesario que cuide esa hiedra venenosa.
          - **Player:** ¿En serio?
          - **Briallen:** Sí, la hiedra venenosa es un material bastante resistente y la mayoría de los animales evitarán comerla.
          - **Briallen:** Por lo tanto, no hay razón para preocuparse por eso.
          - **Player:** Genial.
        - (Condition: Si los cultivos en el parche aún no han crecido completamente:)
          - **Briallen:** Si quieres, pero quiero [número] [item] para eso.
          - (Condition: Si el player no tiene los elementos requeridos:)
            - **Player:** Me temo que no tengo suficientes en este momento.
            - **Briallen:** Bueno, no voy a perder el tiempo gratis.
          - (Condition: Si el player tiene los elementos requeridos:)
            - [Menu]: Selecciona una opción
              - [Choice]: Está bien, es un trato.
                - **Player:** Está bien, es un trato.
                - (removes=the requested items)
                - **Briallen:** Eso estará bien, [Sir/Madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
              - [Choice]: No, eso es demasiado.
                - **Player:** No, eso es demasiado.
                - **Briallen:** Bueno, no voy a perder el tiempo gratis.
      - [Choice]: Ah, entonces no te molestes.
        - (end)
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Briallen}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|¿Puedes dejar de desyerbar mis parcelas agrícolas, por favor?
    - **Player:** ¿Puedes dejar de desherbar mis parcelas de cultivo, por favor?
    - **Briallen:** Claro, dejaré de eliminarlos ahora.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|¿Puedes mantener mis parcelas agrícolas desyerbadas, por favor?
    - **Player:** ¿Puedes mantener mis parcelas de cultivo desyerbadas, por favor?
    - **Briallen:** Eso no debería ser un problema, ¡Martin dijo que debería darte especial atención por tu ayuda con las hadas! ¡Asegúrate de limpiar tu asignación ya que no quiero interrumpir su crecimiento!
  - [Choice]: ¿Puedes venderme algo?
    - **Player:** ¿Puedes venderme algo?
    - **Briallen:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
    - (opens=Farmer's Supplies)
  - [Choice]: Eso es todo, gracias.
    - **Player:** Eso es todo, gracias.

#### Diálogo histórico de venta anterior al 18 de julio de 2022

- **Player:** ¿Puedes venderme algo?
- **Briallen:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
- [Menu]: Selecciona una opción
  - [Choice]: Alguna cura vegetal.
    - **Player:** Alguna cura vegetal.
    - **Briallen:** Cura vegetal, ¿eh? Quizás tenga algo reservado para mí. Te diré una cosa, te venderé una cura vegetal por 25 po si quieres.
    - (Condition: Si el player no tiene suficiente dinero:)
      - **Player:** Me temo que no tengo suficiente dinero para eso.
    - (Condition: Si el player tiene suficiente dinero:)
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, parece un precio justo.
          - **Player:** Sí, parece un precio justo.
          - (removes=25 coins) (receives=plant cure)
        - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
          - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
  - [Choice]: Un balde de abono.
    - **Player:** Un balde de abono.
    - **Briallen:** Un balde de abono, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 35 po si quieres.
    - (Condition: Si el player no tiene suficiente dinero:)
      - **Player:** Me temo que no tengo suficiente dinero para eso.
    - (Condition: Si el player tiene suficiente dinero:)
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, parece un precio justo.
          - **Player:** Sí, parece un precio justo.
          - (removes=35 coins) (receives=compost)
        - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
          - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
  - [Choice]: Un rastrillo.
    - **Player:** Un rastrillo.
    - **Briallen:** Un rastrillo, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
    - (Condition: Si el player no tiene suficiente dinero:)
      - **Player:** Me temo que no tengo suficiente dinero para eso.
    - (Condition: Si el player tiene suficiente dinero:)
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, parece un precio justo.
          - **Player:** Sí, parece un precio justo.
          - (removes=15 coins) (receives=a rake)
        - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
          - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
  - [Choice]: (Ver más artículos)
    - [Menu]: Selecciona una opción
      - [Choice]: una regadera
        - **Player:** Una regadera.
        - **Briallen:** Una regadera, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 25 po si quieres.
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Player:** Me temo que no tengo suficiente dinero para eso.
        - (Condition: Si el player tiene suficiente dinero:)
          - [Menu]: Selecciona una opción
            - [Choice]: Sí, parece un precio justo.
              - **Player:** Sí, parece un precio justo.
              - (removes=25 coins) (receives=a watering can)
            - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
              - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
      - [Choice]: Una paleta de jardinería
        - **Player:** Una paleta de jardinería.
        - **Briallen:** Una paleta de jardín, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Player:** Me temo que no tengo suficiente dinero para eso.
        - (Condition: Si el player tiene suficiente dinero:)
          - [Menu]: Selecciona una opción
            - [Choice]: Sí, parece un precio justo.
              - **Player:** Sí, parece un precio justo.
              - (removes=15 coins) (receives=a gardening trowel)
            - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
              - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
      - [Choice]: Un zambullidor de semillas
        - **Player:** Un arrancador de semillas.
        - **Briallen:** Un zambullidor de semillas, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Player:** Me temo que no tengo suficiente dinero para eso.
        - (Condition: Si el player tiene suficiente dinero:)
          - [Menu]: Selecciona una opción
            - [Choice]: Sí, parece un precio justo.
              - **Player:** Sí, parece un precio justo.
              - (removes=15 coins) (receives=a seed dibber)
            - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
              - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
      - [Choice]: (Ver artículos anteriores)
        - (previous)
  - [Choice]: Olvídalo.
    - **Player:** Olvídalo, no tienes nada que necesite.

### Using items on Briallen


#### Mostrando a Briallen un artículo que puede hacer abono

- **Briallen:** Parece algo con lo que se puede hacer abono normal. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de abono.

#### Mostrando a Briallen un artículo que puede hacer supercompost

- **Briallen:** Parece algo con lo que se puede hacer supercompost. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de supercompost.
