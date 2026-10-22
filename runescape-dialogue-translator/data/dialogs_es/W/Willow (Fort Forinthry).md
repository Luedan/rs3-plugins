# Willow (Fort Forinthry)

- **Original Wiki Page**: [Transcript:Willow (Fort Forinthry)](https://runescape.wiki/w/Transcript%3AWillow%20%28Fort%20Forinthry%29)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pay


#### Con el parche del árbol vacío

- **Willow:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.

#### Con el árbol creciendo


##### Sin los elementos requeridos

- **Willow:** Quiero [número] [items] para eso.
- **Player:** Gracias, tal vez en otro momento.

##### Con los elementos requeridos, sin confirmación desactivada

- [Menu]: ¿Pagar [número] [items]?
  - [Choice]: Sí.
    - (removes=requested items)
    - **Willow:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
    - El jardinero ahora se ocupará del parche por usted.
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (arriba)
  - [Choice]: No.
    - (end)

##### Con los elementos requeridos, con la confirmación desactivada

- (removes=requested items)
- **Willow:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
- El jardinero ahora se ocupará del parche por usted.

##### Habiendo pagado ya por la protección

- **Willow:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
- **Player:** Oh, lo siento, lo olvidé.

#### Con el árbol completamente desarrollado


##### Antes de haber comprobado su estado

- **Willow:** Creo que deberías reclamar los XP de ese parche antes de cortarlo.

##### Después de haber comprobado su estado, sin confirmación desactivada

- [Menu]: ¿Pagar 200 po para que talen el árbol?
  - [Choice]: Sí, deshazte del árbol.
    - ((Without 200 coins:))
      - **Willow:** Querré 200 po por talar ese árbol.
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
  - **Willow:** Querré 200 po por talar ese árbol.
  - No puedes permitirte eso.
- ((With 200 coins:))
  - (removes=200 coins)
  - (Action: El parche está borrado.)
  - El jardinero amablemente retira su árbol.

### Talk to

- [Menu]: Elige una opción:
  - [Choice]: cond=If the tree is fully grown|¿Podrías talar mi árbol por mí?
    - **Player:** ¿Podrías talar mi árbol por mí?
    - **Willow:** Parece que podrías cortarlo tú mismo. Puedo talar el árbol si quieres, pero necesitaré 200 po para que valga la pena.
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
      - **Willow:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.
    - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
      - **Willow:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
      - **Player:** Oh, lo siento, lo olvidé.
    - (Condition: If the crops in the patch are not yet fully grown:)
      - **Willow:** Si quieres, pero quiero [número] [item] para eso.
      - (Condition: If the player does not have the required items:)
        - **Player:** Me temo que no tengo suficientes en este momento.
        - **Willow:** Bueno, no voy a perder el tiempo gratis.
      - (Condition: If the player has the required items:)
        - [Menu]: Selecciona una opción
          - [Choice]: Está bien, es un trato.
            - **Player:** Está bien, es un trato.
            - (removes=requested items)
            - **Willow:** Eso estará bien, [Sir/Madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
          - [Choice]: No, eso es demasiado.
            - **Player:** No, eso es demasiado.
            - **Willow:** Bueno, no voy a perder el tiempo gratis.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Willow}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|¿Puedes dejar de desyerbar mis parcelas agrícolas, por favor?
    - **Player:** ¿Puedes dejar de desherbar mis parcelas de cultivo, por favor?
    - **Willow:** Claro, dejaré de desmalezarlos ahora.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|¿Puedes mantener mis parcelas agrícolas desyerbadas, por favor?
    - **Player:** ¿Puedes mantener mis parcelas de cultivo desyerbadas, por favor?
    - **Willow:** Eso no debería ser un problema, ¡Martin dijo que debería darte atención especial por tu ayuda con las hadas! ¡Asegúrate de limpiar tu asignación ya que no quiero interrumpir su crecimiento!
  - [Choice]: ¿Puedes venderme algo?
    - **Player:** ¿Puedes venderme algo?
    - **Willow:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
    - (opens=Farmer's Supplies)
  - [Choice]: Eso es todo, gracias.
    - **Player:** Eso es todo, gracias.

### Using items on Willow


#### Mostrándole a Willow un artículo que puede hacer abono

- **Willow:** Parece algo con lo que puedes hacer abono normal. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de abono.

#### Mostrándole a Willow un elemento que puede hacer supercompost

- **Willow:** Parece algo con lo que puedes hacer supercompost. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de supercompost.
