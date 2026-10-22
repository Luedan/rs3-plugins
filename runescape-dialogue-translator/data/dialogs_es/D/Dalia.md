# Dalia

- **Original Wiki Page**: [Transcript:Dalia](https://runescape.wiki/w/Transcript%3ADalia)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Page should have standard dialogue post-The Lute of Love, any achievement related dialogue should be moved to its respective transcript.}}

### Any option before The Lute of Love achievement

- (ver|El laúd del amor)

### After the Lute of Love achievement


#### Pay (Parcela de árboles) o Pay (Parcela de árboles frutales)


##### Si el parche está vacío

- **Dalia:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.

##### Si en el parche está creciendo algo


##### Sin los elementos requeridos.

- **Dalia:** Quiero [número] [items] para eso.
- **Player:** Gracias, tal vez en otro momento.

##### Con los elementos requeridos, sin confirmación desactivados.

- [Menu]: ¿Pagar [número] [items]?
  - [Choice]: Sí.
    - (removes=the requested items)
    - **Dalia:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
    - El jardinero ahora se ocupará del parche por usted.
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (arriba)
  - [Choice]: No.
    - (end)

##### Con los elementos requeridos, con la confirmación desactivada.

- (removes=the requested items)
- **Dalia:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
- El jardinero ahora se ocupará del parche por usted.

##### Con protección ya pagada

- **Dalia:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
- **Player:** Oh, lo siento, lo olvidé.

##### Si Patch está completamente desarrollado

- **Dalia:** Ese parche ya está completamente desarrollado. No sé qué quieres que haga con él.

#### Habla con

- [Menu]: Elige una opción:
  - [Choice]: ¿Cuidarías mis cultivos por mí?
    - **Player:** ¿Cuidarías mis cultivos por mí?
    - **Dalia:** Podría hacerlo. ¿En cuál estabas pensando?
    - [Menu]: Selecciona una opción
      - [Choice]: El parche del árbol.
        - (Condition: If the player has no crops in the patch:)
          - **Dalia:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.
        - (Condition: If the player has fully grown crops planted in the patch:)
          - **Dalia:** ¡Ese parche ya está completamente desarrollado! ¡No sé qué quieres que haga con él!
        - (Condition: If the crops in the patch are not yet fully grown but the player has already paid the gardener:)
          - **Dalia:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
          - **Player:** Oh, lo siento, lo olvidé.
        - (Condition: If the crops in the patch are not yet fully grown:)
          - **Dalia:** Si quieres, pero quiero [número] [item] para eso.
          - (Condition: If the player does not have the required items:)
            - **Player:** Me temo que no tengo suficientes en este momento.
            - **Dalia:** Bueno, no voy a perder el tiempo gratis.
          - (Condition: If the player has the required items:)
            - [Menu]: Selecciona una opción
              - [Choice]: Está bien, es un trato.
                - **Player:** Está bien, es un trato.
                - (removes=the requested items)
                - **Dalia:** Eso estará bien, [Sir/Madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
              - [Choice]: No, eso es demasiado.
                - **Player:** No, eso es demasiado.
                - **Dalia:** Bueno, no voy a perder el tiempo gratis.
      - [Choice]: El huerto de árboles frutales.
        - (arriba)
  - [Choice]: ¿Puedes contarme sobre el vivero de árboles?
    - **Dalia:** A cambio de tu ayuda, te dejaré usar mi vivero de árboles.
    - **Dalia:** Tiene una parcela de árboles y una parcela de árboles frutales.
    - **Dalia:** También hay tres parcelas de suelo de alta calidad.
    - (Condition: Before completing "From Here to Eternity":)
      - **Dalia** Están vacíos, ya que no he encontrado ningún árbol lo suficientemente especial como para justificar su plantación en un suelo tan bueno.
      - **Dalia** Si encuentras algún árbol de este tipo en tus aventuras, me encantaría verlo aprovecharlo al máximo.
    - (Condition: After completing "From Here to Eternity":)
      - **Dalia:** Todavía no estoy acostumbrado a la belleza sobrenatural de los árboles que plantaste allí.
      - **Dalia:** Son exactamente el tipo de espécimen especial para el que reservé esas parcelas.
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|¿Puedes dejar de desyerbar mis parcelas agrícolas, por favor?
    - **Player:** ¿Puedes dejar de desherbar mis parcelas de cultivo, por favor?
    - **Dalia:** Claro, dejaré de eliminarlos ahora.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|¿Puedes mantener mis parcelas agrícolas desyerbadas, por favor?
    - **Player:** ¿Puedes mantener mis parcelas de cultivo desyerbadas, por favor?
    - **Dalia:** Eso no debería ser un problema, ¡Martin dijo que debería darte especial atención por tu ayuda con las hadas! ¡Asegúrate de limpiar tu asignación ya que no quiero interrumpir su crecimiento!
  - [Choice]: ¿Puedes venderme algo?
    - **Player:** ¿Puedes venderme algo?
    - **Dalia:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
    - (opens=Farmer's Supplies)
  - [Choice]: Eso es todo, gracias.
    - **Player:** Eso es todo, gracias.

#### Comercio

- {{Transcript missing}}
