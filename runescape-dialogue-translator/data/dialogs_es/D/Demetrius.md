# Demetrius

- **Original Wiki Page**: [Transcript:Demetrius](https://runescape.wiki/w/Transcript%3ADemetrius)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pay (north) or pay (south)


#### Con el parche de asignación vacío

- **Demetrius:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.

#### Con el cultivo creciendo


##### Sin los elementos requeridos

- **Demetrius:** Quiero [número] [items] para eso.
- **Player:** Gracias, tal vez en otro momento.

##### Con los elementos requeridos, sin confirmación desactivada

- [Menu]: ¿Pagar [número] [items]?
  - [Choice]: Sí.
    - (removes=the requested items)
    - **Demetrius:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
    - El jardinero ahora se ocupará del parche por usted.
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (arriba)
  - [Choice]: No.
    - (end)

##### Con los elementos requeridos, con la confirmación desactivada

- (removes=the requested items)
- **Demetrius:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
- El jardinero ahora se ocupará del parche por usted.

##### Habiendo pagado ya por la protección

- **Demetrius:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
- **Player:** Oh, lo siento, lo olvidé.

#### Con el cultivo completamente desarrollado

- **Demetrius:** Ese parche ya está completamente desarrollado. No sé qué quieres que haga con él.

### Talk to

- [Menu]: Elige una opción:
  - [Choice]: ¿Cuidarías mis cultivos por mí?
    - **Player:** ¿Cuidarías mis cultivos por mí?
    - **Demetrius:** Podría hacerlo. ¿En cuál estabas pensando?
    - [Menu]: Selecciona una opción
      - [Choice]: La parcela del norte
        - **Player:** La parcela del norte.
        - (above|Pay (north) o pagar (sur))
      - [Choice]: La parcela del sur
        - **Player:** La parcela del sur.
        - (above|Pay (north) o pagar (sur))
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Demetrius}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded:|¿Puedes dejar de desyerbar mis parcelas agrícolas, por favor?
    - **Player:** ¿Puedes dejar de desherbar mis parcelas de cultivo, por favor?
    - **Demetrius:** Claro, dejaré de eliminarlos ahora.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded:|¿Puedes mantener mis parcelas agrícolas desyerbadas, por favor?
    - **Player:** ¿Puedes mantener mis parcelas de cultivo desyerbadas, por favor?
    - **Demetrius:** Eso no debería ser un problema, ¡Martin dijo que debería darte especial atención por tu ayuda con las hadas! ¡Asegúrate de limpiar tu asignación ya que no quiero interrumpir su crecimiento!
  - [Choice]: ¿Puedes venderme algo?
    - **Player:** ¿Puedes venderme algo?
    - **Demetrius:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
    - (opens=Farmer's Supplies)
  - [Choice]: Eso es todo, gracias.
    - **Player:** Eso es todo, gracias.

### Using items on Demetrius


#### Mostrando a Demetrius un artículo que puede hacer abono

- **Demetrius:** Parece algo con lo que se puede hacer abono normal. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de abono.

#### Mostrando a Demetrius un artículo que puede hacer supercompost

- **Demetrius:** Parece algo con lo que se puede hacer supercompost. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de supercompost.
