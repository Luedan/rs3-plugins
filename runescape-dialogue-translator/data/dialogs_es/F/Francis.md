# Francis

- **Original Wiki Page**: [Transcript:Francis](https://runescape.wiki/w/Transcript%3AFrancis)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pay


#### Con el parche de lúpulo vacío

- **Francis:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.

#### Con el lúpulo creciendo


##### Sin los elementos requeridos

- **Francis:** Quiero [número] [items] para eso.
- **Player:** Gracias, tal vez en otro momento.

##### Con los elementos requeridos, sin confirmación desactivada

- [Menu]: ¿Pagar [número] [items]?
  - [Choice]: Sí.
    - (removes=the requested items)
    - **Francis:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
    - El jardinero ahora se ocupará del parche por usted.
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (arriba)
  - [Choice]: No.
    - (end)

##### Con los elementos requeridos, con la confirmación desactivada

- (removes=the requested items)
- **Francis:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
- El jardinero ahora se ocupará del parche por usted.

##### Habiendo pagado ya por la protección

- **Francis:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
- **Player:** Oh, lo siento, lo olvidé.

#### Con el lúpulo completamente desarrollado.

- **Francis:** Ese parche ya está completamente desarrollado. No sé qué quieres que haga con él.

### Talk to


#### Diálogo estándar

- [Menu]: Elige una opción:
  - [Choice]: ¿Cuidarías mis cultivos por mí?
    - **Player:** ¿Cuidarías mis cultivos por mí?
    - (Condition: Si el player no tiene cultivos en el parche:)
      - **Francis:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.
    - (Condition: Si el player tiene cultivos completamente desarrollados plantados en el parche:)
      - **Francis:** ¡Ese parche ya está completamente desarrollado! ¡No sé qué quieres que haga con él!
    - (Condition: Si los cultivos en el parche aún no están completamente desarrollados pero el player ya le pagó al jardinero:)
      - **Francis:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
      - **Player:** Oh, lo siento, lo olvidé.
    - (Condition: Si los cultivos en el parche aún no han crecido completamente:)
      - **Francis:** Si quieres, pero quiero [número] [item] para eso.
      - (Condition: Si el player no tiene los elementos requeridos:)
        - **Player:** Me temo que no tengo suficientes en este momento.
        - **Francis:** Bueno, no voy a perder el tiempo gratis.
      - (Condition: Si el player tiene los elementos requeridos:)
        - [Menu]: Selecciona una opción
          - [Choice]: Está bien, es un trato.
            - **Player:** Está bien, es un trato.
            - (removes=the requested items)
            - **Francis:** Eso estará bien, [Sir/Madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
          - [Choice]: No, eso es demasiado.
            - **Player:** No, eso es demasiado.
            - **Francis:** Bueno, no voy a perder el tiempo gratis.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Francis}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|¿Puedes dejar de desyerbar mis parcelas agrícolas, por favor?
    - **Player:** ¿Puedes dejar de desherbar mis parcelas de cultivo, por favor?
    - **Francis:** Claro, dejaré de eliminarlos ahora.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|¿Puedes mantener mis parcelas agrícolas desyerbadas, por favor?
    - **Player:** ¿Puedes mantener mis parcelas de cultivo desyerbadas, por favor?
    - **Francis:** Eso no debería ser un problema, ¡Martin dijo que debería darte especial atención por tu ayuda con las hadas! ¡Asegúrate de limpiar tu asignación ya que no quiero interrumpir su crecimiento!
  - [Choice]: ¿Puedes venderme algo?
    - **Player:** ¿Puedes venderme algo?
    - **Francis:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
    - (opens=Farmer's Supplies)
  - [Choice]: Eso es todo, gracias.
    - **Player:** Eso es todo, gracias.

#### Diálogo histórico de venta anterior al 18 de julio de 2022

- **Player:** ¿Puedes venderme algo?
- **Francis:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
- [Menu]: Selecciona una opción
  - [Choice]: Alguna cura vegetal.
    - **Player:** Alguna cura vegetal.
    - **Francis:** Cura vegetal, ¿eh? Quizás tenga algo reservado para mí. Te diré una cosa, te venderé una cura vegetal por 25 po si quieres.
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
    - **Francis:** Un balde de abono, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 35 po si quieres.
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
    - **Francis:** Un rastrillo, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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
        - **Francis:** Una regadera, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 25 po si quieres.
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
        - **Francis:** Una paleta de jardín, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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
        - **Francis:** Un zambullidor de semillas, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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

### Using items on Francis


#### Mostrando a Francis un artículo que puede hacer abono

- **Francis:** Parece algo con lo que se puede hacer abono normal. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de abono.

#### Mostrando a Francis un artículo que puede hacer supercompost

- **Francis:** Parece algo con lo que se puede hacer supercompost. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de supercompost.
