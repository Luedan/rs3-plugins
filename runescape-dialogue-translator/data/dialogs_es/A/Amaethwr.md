# Amaethwr

- **Original Wiki Page**: [Transcript:Amaethwr](https://runescape.wiki/w/Transcript%3AAmaethwr)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pay


#### Con el huerto de árboles frutales vacío

- **Amaethwr:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.

#### Con el árbol frutal creciendo


##### Sin los elementos requeridos

- **Amaethwr:** Quiero [número] [items] para eso.
- **Player:** Gracias, tal vez en otro momento.

##### Con los elementos requeridos, sin confirmación desactivada

- [Menu]: ¿Pagar [número] [items]?
  - [Choice]: Sí.
    - (removes=the requested items)
    - **Amaethwr:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
    - El jardinero ahora se ocupará del parche por usted.
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (arriba)
  - [Choice]: No.
    - (end)

##### Con los elementos requeridos, con la confirmación desactivada

- (removes=the requested items)
- **Amaethwr:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
- El jardinero ahora se ocupará del parche por usted.

##### Habiendo pagado ya por la protección

- **Amaethwr:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
- **Player:** Oh, lo siento, lo olvidé.

#### Con el árbol frutal completamente desarrollado.

- **Amaethwr:** Ese parche ya está completamente desarrollado. No sé qué quieres que haga con él.

### Talk to


#### Diálogo estándar

- [Menu]: Elige una opción:
  - [Choice]: ¿Cuidarías mis cultivos por mí?
    - **Player:** ¿Cuidarías mis cultivos por mí?
    - (Condition: If the player has no crops in the patch:)
      - **Amaethwr:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.
    - (Condition: If the player has fully grown crops planted in the patch:)
      - **Amaethwr:** ¡Ese parche ya está completamente desarrollado! ¡No sé qué quieres que haga con él!
    - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
      - **Amaethwr:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
      - **Player:** Oh, lo siento, lo olvidé.
    - (Condition: If the crops in the patch are not yet fully grown:)
      - **Amaethwr:** Si quieres, pero quiero [número] [item] para eso.
      - (Condition: If the player does not have the required items:)
        - **Player:** Me temo que no tengo suficientes en este momento.
        - **Amaethwr:** Bueno, no voy a perder el tiempo gratis.
      - (Condition: If the player has the required items:)
        - [Menu]: Selecciona una opción
          - [Choice]: Está bien, es un trato.
            - **Player:** Está bien, es un trato.
            - (removes=the requested items)
            - **Amaethwr:** Eso estará bien, [Sir/Madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
          - [Choice]: No, eso es demasiado.
            - **Player:** No, eso es demasiado.
            - **Amaethwr:** Bueno, no voy a perder el tiempo gratis.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Amaethwr}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|¿Puedes dejar de desyerbar mis parcelas agrícolas, por favor?
    - **Player:** ¿Puedes dejar de desherbar mis parcelas de cultivo, por favor?
    - **Amaethwr:** Claro, dejaré de eliminarlos ahora.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|¿Puedes mantener mis parcelas agrícolas desyerbadas, por favor?
    - **Player:** ¿Puedes mantener mis parcelas de cultivo desyerbadas, por favor?
    - **Amaethwr:** Eso no debería ser un problema, ¡Martin dijo que debería darte especial atención por tu ayuda con las hadas! ¡Asegúrate de limpiar tu asignación ya que no quiero interrumpir su crecimiento!
  - [Choice]: ¿Puedes venderme algo?
    - **Player:** ¿Puedes venderme algo?
    - **Amaethwr:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
    - (opens=Farmer's Supplies)
  - [Choice]: Eso es todo, gracias.
    - **Player:** Eso es todo, gracias.

#### Diálogo histórico de venta anterior al 18 de julio de 2022

- **Player:** ¿Puedes venderme algo?
- **Amaethwr:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
- [Menu]: Selecciona una opción
  - [Choice]: Alguna cura vegetal.
    - **Player:** Alguna cura vegetal.
    - **Amaethwr:** Cura vegetal, ¿eh? Quizás tenga algo reservado para mí. Te diré una cosa, te venderé una cura vegetal por 25 po si quieres.
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
    - **Amaethwr:** Un balde de abono, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 35 po si quieres.
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
    - **Amaethwr:** Un rastrillo, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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
        - **Amaethwr:** Una regadera, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 25 po si quieres.
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
        - **Amaethwr:** Una paleta de jardín, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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
        - **Amaethwr:** Un zambullidor de semillas, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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

### Using items on Amaethwr


#### Mostrando a Amaethwr un artículo que puede hacer abono

- **Amaethwr:** Parece algo con lo que se puede hacer abono normal. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de abono.

#### Mostrando a Amaethwr un artículo que puede hacer supercompost

- **Amaethwr:** Parece algo con lo que se puede hacer supercompost. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de supercompost.

### Treasure Trails

- (receives=lockbox (master))
- **Amaethwr:** ¿Puedes resolver esto por mí?
- [¡Amaethwr te ha regalado una caja de seguridad!]

#### Hablando con él con la caja de seguridad sin resolver en el backpack

- **Amaethwr:** No, eso aún no está completo.

#### Hablando con él con la caja fuerte sin resolver en el banco

- **Player:** Dejé el pergamino del rompecabezas en el banco.
- **Amaethwr:** Bueno, entonces ve a buscarlo para que pueda comprobar que lo has hecho.

#### Hablando con él con la caja de seguridad resuelta en el backpack

- **Amaethwr:** ¡Excelente, aquí tienes tu recompensa!
- (Condition: If the trail continues:)
  - (removes=the old clue scroll (master) y caja de seguridad (maestra)) (receives=the new clue scroll (master))
  - [¡Has encontrado otra pista!]
- (Condition: If the trail ends:)
  - (removes=the old clue scroll (master) y caja de seguridad (maestra)) (receives=reward casket (master))
  - [¡Has encontrado un ataúd!]

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- **¿Qué te gustaría hacer?**
  - Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Amaethwr:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Amaethwr:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **Amaethwr:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - **Amaethwr:** Si completas esto, te daré: Púas de Grenwall x 20. ¡Estoy seguro de que también ganarás algo de reputación en el gremio de agricultores!
    - **Amaethwr:** ¡Tendrás que ser rápido! Solo estoy aquí por [número] horas y [número] minutos. Para ser exactos.
  - Dales los artículos y animales que soliciten.
    - ((Without the requested items:))
      - **Amaethwr:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Amaethwr:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **Amaethwr:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]
    - ((With the requested items:))
      - (removes=the requested items) (receives=20 Grenwall spikes and possibly a Brassica primer)
      - ((If a Brassica primer was rewarded:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - ((Repeated in a pop-up:))
          - Por completar esta solicitud, recibió 1 imprimación para Brassica.
          - (continue)
      - [Has recibido: Picos de Grenwall x 20<br>Y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- **Amaethwr:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time].

#### Entregar solicitud fácil


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Amaethwr:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Amaethwr:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Amaethwr:** También estoy buscando un nuevo animal, actualmente estoy buscando A [animal]

##### Con artículos solicitados

- (removes=the requested items) (receives=20 Grenwall spikes and possibly a Brassica primer)
- ((If a Brassica primer was rewarded:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - ((Repeated in a pop-up:))
    - Por completar esta solicitud, recibió 1 imprimación para Brassica.
    - (continue)
- [Has recibido: Picos de Grenwall x 20<br>Y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud diaria en [time].
