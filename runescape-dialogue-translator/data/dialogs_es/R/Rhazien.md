# Rhazien

- **Original Wiki Page**: [Transcript:Rhazien](https://runescape.wiki/w/Transcript%3ARhazien)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pay


#### Con el matorral vacío

- **Rhazien:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.

#### Con el arbusto creciendo


##### Sin los elementos requeridos

- **Rhazien:** Quiero [número] [items] para eso.
- **Player:** Gracias, tal vez en otro momento.

##### Con los elementos requeridos, sin confirmación desactivada

- [Menu]: ¿Pagar [número] [items]?
  - [Choice]: Sí.
    - (removes=the requested items)
    - **Rhazien:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
    - El jardinero ahora se ocupará del parche por usted.
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (arriba)
  - [Choice]: No.
    - (end)

##### Con los elementos requeridos, con la confirmación desactivada

- (removes=the requested items)
- **Rhazien:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
- El jardinero ahora se ocupará del parche por usted.

##### Habiendo pagado ya por la protección

- **Rhazien:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
- **Player:** Oh, lo siento, lo olvidé.

#### Con el arbusto completamente desarrollado

- **Rhazien:** Ese parche ya está completamente desarrollado. No sé qué quieres que haga con él.

#### Si el arbusto es una hiedra venenosa

- **Rhazien:** No es necesario que cuide esa hiedra venenosa.
- **Player:** ¿En serio?
- **Rhazien:** Sí, la hiedra venenosa es un material bastante resistente y la mayoría de los animales evitarán comerla.
- **Rhazien:** Por lo tanto, no hay razón para preocuparse por eso.
- **Player:** Genial.

### Talk to


#### Diálogo estándar

- [Menu]: Elige una opción:
  - [Choice]: ¿Cuidarías mis cultivos por mí?
    - **Player:** ¿Cuidarías mis cultivos por mí?
    - (Condition: If the player has no crops in the patch:)
      - **Rhazien:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.
    - (Condition: If the player has fully grown crops planted in the patch:)
      - **Rhazien:** ¡Ese parche ya está completamente desarrollado! ¡No sé qué quieres que haga con él!
    - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
      - **Rhazien:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
      - **Player:** Oh, lo siento, lo olvidé.
    - (Condition: If a poison ivy bush is growing:)
      - **Rhazien:** No es necesario que cuide esa hiedra venenosa.
      - **Player:** ¿En serio?
      - **Rhazien:** Sí, la hiedra venenosa es un material bastante resistente y la mayoría de los animales evitarán comerla.
      - **Rhazien:** Por lo tanto, no hay razón para preocuparse por eso.
      - **Player:** Genial.
    - (Condition: If the crops in the patch are not yet fully grown:)
      - **Rhazien:** Si quieres, pero quiero [número] [item] para eso.
      - (Condition: If the player does not have the required items:)
        - **Player:** Me temo que no tengo suficientes en este momento.
        - **Rhazien:** Bueno, no voy a perder el tiempo gratis.
      - (Condition: If the player has the required items:)
        - [Menu]: Selecciona una opción
          - [Choice]: Está bien, es un trato.
            - **Player:** Está bien, es un trato.
            - (removes=the requested items)
            - **Rhazien:** Eso estará bien, [Sir/Madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
          - [Choice]: No, eso es demasiado.
            - **Player:** No, eso es demasiado.
            - **Rhazien:** Bueno, no voy a perder el tiempo gratis.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Rhazien}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|¿Puedes dejar de desyerbar mis parcelas agrícolas, por favor?
    - **Player:** ¿Puedes dejar de desherbar mis parcelas de cultivo, por favor?
    - **Rhazien:** Claro, dejaré de eliminarlos ahora.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|¿Puedes mantener mis parcelas agrícolas desyerbadas, por favor?
    - **Player:** ¿Puedes mantener mis parcelas de cultivo desyerbadas, por favor?
    - **Rhazien:** Eso no debería ser un problema, ¡Martin dijo que debería darte especial atención por tu ayuda con las hadas! ¡Asegúrate de limpiar tu asignación ya que no quiero interrumpir su crecimiento!
  - [Choice]: ¿Puedes venderme algo?
    - **Player:** ¿Puedes venderme algo?
    - **Rhazien:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
    - (opens=Farmer's Supplies)
  - [Choice]: Eso es todo, gracias.
    - **Player:** Eso es todo, gracias.

#### Diálogo histórico de venta anterior al 18 de julio de 2022

- **Player:** ¿Puedes venderme algo?
- **Rhazien:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
- [Menu]: Selecciona una opción
  - [Choice]: Alguna cura vegetal.
    - **Player:** Alguna cura vegetal.
    - **Rhazien:** Cura vegetal, ¿eh? Quizás tenga algo reservado para mí. Te diré una cosa, te venderé una cura vegetal por 25 po si quieres.
    - (Condition: If the player does not have enough money:)
      - **Player:** Me temo que no tengo suficiente dinero para eso.
    - (Condition: If the player has enough money:)
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, parece un precio justo.
          - **Player:** Sí, parece un precio justo.
          - (removes=25 coins) (receives=plant cure)
        - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
          - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
  - [Choice]: Un balde de abono.
    - **Player:** Un balde de abono.
    - **Rhazien:** Un balde de abono, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 35 po si quieres.
    - (Condition: If the player does not have enough money:)
      - **Player:** Me temo que no tengo suficiente dinero para eso.
    - (Condition: If the player has enough money:)
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, parece un precio justo.
          - **Player:** Sí, parece un precio justo.
          - (removes=35 coins) (receives=compost)
        - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
          - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
  - [Choice]: Un rastrillo.
    - **Player:** Un rastrillo.
    - **Rhazien:** Un rastrillo, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
    - (Condition: If the player does not have enough money:)
      - **Player:** Me temo que no tengo suficiente dinero para eso.
    - (Condition: If the player has enough money:)
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
        - **Rhazien:** Una regadera, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 25 po si quieres.
        - (Condition: If the player does not have enough money:)
          - **Player:** Me temo que no tengo suficiente dinero para eso.
        - (Condition: If the player has enough money:)
          - [Menu]: Selecciona una opción
            - [Choice]: Sí, parece un precio justo.
              - **Player:** Sí, parece un precio justo.
              - (removes=25 coins) (receives=a watering can)
            - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
              - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
      - [Choice]: Una paleta de jardinería
        - **Player:** Una paleta de jardinería.
        - **Rhazien:** Una paleta de jardín, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
        - (Condition: If the player does not have enough money:)
          - **Player:** Me temo que no tengo suficiente dinero para eso.
        - (Condition: If the player has enough money:)
          - [Menu]: Selecciona una opción
            - [Choice]: Sí, parece un precio justo.
              - **Player:** Sí, parece un precio justo.
              - (removes=15 coins) (receives=a gardening trowel)
            - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
              - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
      - [Choice]: Un zambullidor de semillas
        - **Player:** Un arrancador de semillas.
        - **Rhazien:** Un zambullidor de semillas, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
        - (Condition: If the player does not have enough money:)
          - **Player:** Me temo que no tengo suficiente dinero para eso.
        - (Condition: If the player has enough money:)
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

### Using items on Rhazien


#### Mostrando a Rhazien un artículo que puede hacer abono

- **Rhazien:** Parece algo con lo que se puede hacer abono normal. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de abono.

#### Mostrando a Rhazien un artículo que puede hacer supercompost

- **Rhazien:** Parece algo con lo que se puede hacer supercompost. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de supercompost.

### Manor Farm


#### Ayuda


##### Antes de haber completado la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Rhazien:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Rhazien:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - (Condition: With three requested animals:)
      - **Rhazien:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
      - (continue)
    - (Condition: With four requested animals:)
      - **Rhazien:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
      - (continue)
    - **Rhazien:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - **Rhazien:** Si completas esto, te daré: Una pieza de armadura de caparazón de roca, de espinas o de esqueleto x 1. ¡Estoy seguro de que también ganarás algo de reputación en el gremio de agricultores!
    - **Rhazien:** ¡Tendrás que ser rápido!, solo estoy aquí por [número] días, [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - ((Without the requested items:))
      - **Rhazien:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Rhazien:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - (Condition: With two requested animals:)
        - **Rhazien:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
        - (continue)
      - (Condition: With three requested animals:)
        - **Rhazien:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
        - (continue)
      - **Rhazien:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - ((With the requested items:))
      - (removes=the requested items) (receives=the reward)
      - Por completar esta solicitud, recibió 1 imprimación para Brassica.
      - ((Repeated in a pop-up:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - (continue)
      - Has recibido: [Reward] x 1<br>Y 5500 reputación Farming.

##### Después de haber completado la solicitud

- **Rhazien:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time]{{Sic|..}}

#### Entregar solicitud mediana


##### Antes de haber completado la solicitud


##### Sin artículos solicitados

- **Rhazien:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Rhazien:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- (Condition: With three requested animals:)
  - **Rhazien:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
  - (continue)
- (Condition: With four requested animals:)
  - **Rhazien:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
  - (continue)
- **Rhazien:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]

##### Con artículos solicitados

- (Condition: With multiple applicable animals:)
  - [Menu]: ¿Qué animal te gustaría entregar?
    - ((Repeated for each applicable animal:))
      - [Choice]: [Name]
        - (continue)
- (removes=the requested items) (receives=the reward)
- Por completar esta solicitud, recibió 1 imprimación para Brassica.
- ((Repeated in a pop-up:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - (continue)
- Has recibido: [Reward] x 1<br>Y 5500 reputación agrícola.

##### Después de tener la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud tridiaria en [time]{{Sic|..}}
