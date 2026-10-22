# Prissy Scilla

- **Original Wiki Page**: [Transcript:Prissy Scilla](https://runescape.wiki/w/Transcript%3APrissy%20Scilla)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pay


#### Con el parche del árbol vacío

- **Prissy Scilla:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.

#### Con el árbol creciendo


##### Sin los elementos requeridos

- **Prissy Scilla:** Quiero [número] [items] para eso.
- **Player:** Gracias, tal vez en otro momento.

##### Con los elementos requeridos, sin confirmación desactivada

- [Menu]: ¿Pagar [número] [items]?
  - [Choice]: Sí.
    - (removes=requested items)
    - **Prissy Scilla:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
    - El jardinero ahora se ocupará del parche por usted.
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (arriba)
  - [Choice]: No.
    - (end)

##### Con los elementos requeridos, con la confirmación desactivada

- (removes=requested items)
- **Prissy Scilla:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
- El jardinero ahora se ocupará del parche por usted.

##### Habiendo pagado ya por la protección

- **Prissy Scilla:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
- **Player:** Oh, lo siento, lo olvidé.

#### Con el árbol completamente desarrollado


##### Antes de haber comprobado su estado

- **Prissy Scilla:** Creo que deberías reclamar los XP de ese parche antes de eliminarlo.

##### Después de haber comprobado su estado, sin confirmación desactivada

- [Menu]: ¿Pagar 200 po para que talen el árbol?
  - [Choice]: Sí, deshazte del árbol.
    - ((Without 200 coins:))
      - **Prissy Scilla:** Querré 200 po por talar ese árbol.
      - No puedes permitirte eso.
    - ((With 200 coins:))
      - (removes=200 coins)
      - (Action: El parche está borrado.)
      - El jardinero amablemente retira su árbol.
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (arriba)
  - [Choice]: No gracias.
    - (end)

##### Después de haber comprobado su estado, con la confirmación desactivada

- ((Without 200 coins:))
  - **Prissy Scilla:** Querré 200 po por talar ese árbol.
  - No puedes permitirte eso.
- ((With 200 coins:))
  - (removes=200 coins)
  - (Action: El parche está borrado.)
  - El jardinero amablemente retira su árbol.

### Talk to

- [Menu]: Elige una opción:
  - [Choice]: cond=If the tree is fully grown|¿Podrías talar mi árbol por mí?
    - **Player:** ¿Podrías talar mi árbol por mí?
    - **Prissy Scilla:** Parece que podrías cortarlo tú mismo. Puedo talar el árbol si quieres, pero necesitaré 200 po para que valga la pena.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿200 po? Lo haré yo mismo.
        - **Player:** ¿200 po? Lo haré yo mismo.
      - [Choice]: Está bien, adelante.
        - ((Without 200 coins:))
          - **Player:** Me temo que no tengo 200 po.
          - No puedes permitirte eso.
        - ((With 200 coins:))
          - (removes=200 coins)
          - **Player:** Está bien, adelante.
          - (Action: El parche está borrado.)
          - El jardinero amablemente retira su árbol.
  - [Choice]: cond=If the tree isn't fully grown|¿Cuidarías mis cultivos por mí?
    - **Player:** ¿Cuidarías mis cultivos por mí?
    - (Condition: If the player has nothing planted in the patch:)
      - **Prissy Scilla:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.
    - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
      - **Prissy Scilla:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
      - **Player:** Oh, lo siento, lo olvidé.
    - (Condition: If the crops in the patch are not yet fully grown:)
      - **Prissy Scilla:** Si quieres, pero quiero [número] [item] para eso.
      - (Condition: If the player does not have the required items:)
        - **Player:** Me temo que no tengo suficientes en este momento.
        - **Prissy Scilla:** Bueno, no voy a perder el tiempo gratis.
      - (Condition: If the player has the required items:)
        - [Menu]: Selecciona una opción
          - [Choice]: Está bien, es un trato.
            - **Player:** Está bien, es un trato.
            - (removes=requested items)
            - **Prissy Scilla:** Eso estará bien, [Sir/Madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
          - [Choice]: No, eso es demasiado.
            - **Player:** No, eso es demasiado.
            - **Prissy Scilla:** Bueno, no voy a perder el tiempo gratis.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Prissy Scilla}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|¿Puedes dejar de desyerbar mis parcelas agrícolas, por favor?
    - **Player:** ¿Puedes dejar de desherbar mis parcelas de cultivo, por favor?
    - **Prissy Scilla:** Claro, dejaré de eliminarlos ahora.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|¿Puedes mantener mis parcelas agrícolas desyerbadas, por favor?
    - **Player:** ¿Puedes mantener mis parcelas de cultivo desyerbadas, por favor?
    - **Prissy Scilla:** Eso no debería ser un problema, ¡Martin dijo que debería darte especial atención por tu ayuda con las hadas! ¡Asegúrate de limpiar tu asignación ya que no quiero interrumpir su crecimiento!
  - [Choice]: ¿Puedes venderme algo?
    - **Player:** ¿Puedes venderme algo?
    - **Prissy Scilla:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
    - (opens=Farmer's Supplies)
  - [Choice]: Eso es todo, gracias.
    - **Player:** Eso es todo, gracias.

#### Diálogo histórico de venta anterior al 18 de julio de 2022

- **Player:** ¿Puedes venderme algo?
- **Prissy Scilla:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
- [Menu]: Selecciona una opción
  - [Choice]: Alguna cura vegetal.
    - **Player:** Alguna cura vegetal.
    - **Prissy Scilla:** Cura vegetal, ¿eh? Quizás tenga algo reservado para mí. Te diré una cosa, te venderé una cura vegetal por 25 po si quieres.
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
    - **Prissy Scilla:** Un balde de abono, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 35 po si quieres.
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
    - **Prissy Scilla:** Un rastrillo, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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
        - **Prissy Scilla:** Una regadera, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 25 po si quieres.
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
        - **Prissy Scilla:** Una paleta de jardín, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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
        - **Prissy Scilla:** Un zambullidor de semillas, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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

### Using items on Prissy Scilla


#### Mostrando a Prissy Scilla un artículo que puede hacer abono

- **Prissy Scilla:** Parece algo con lo que se puede hacer abono normal. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de abono.

#### Mostrando a Prissy Scilla un artículo que puede hacer supercompost

- **Prissy Scilla:** Parece algo con lo que se puede hacer supercompost. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de supercompost.
