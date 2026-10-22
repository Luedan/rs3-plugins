# Dark Romancer

- **Original Wiki Page**: [Transcript:Dark Romancer](https://runescape.wiki/w/Transcript%3ADark%20Romancer)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Player:** ¡Hola!
- **Dark Romancer:** Urrm... ¡hola!
- **Player:** ¿Qué haces aquí?
- **Dark Romancer:** Estoy buscando cartas de amor.
- **Player:** ¿Cartas de amor?
- **Dark Romancer:** ¡Sí! Cuanto más puedo encontrar y destruir, menos amor se comparte. ¡No soporto esta época del año!
- [Trae Dark Romancer Love Letters antes de que finalice el 17 de febrero para avanzar hacia el título y las variantes de color de 'The Hater', así como uno de los siguientes:]
- [Aumento de XP del 20 % durante +5 minutos (hasta 60 minutos como máximo).<br> Aumento de quema de XP adicional del 25 % +5 minutos (hasta 60 minutos como máximo).<br>250x Corazones.]
- [Si no quieres entregar cartas de amor, o Dark Romancer se ha ido, puedes romperlas, lo que otorga un aumento de XP del 5 % durante +5 minutos (hasta 60 minutos como máximo) a todos los jugadores que las vean.]
- (Condition: Without Love Letters:)
  - **Player:** Si encuentro alguno, ¡te lo traeré!
  - **Dark Romancer:** ¡Gracias!
- (Condition: With Love Letters:)
  - (continue|I've)

### Give Love Letter

- **Player:** Tengo algo que darte.
- (Condition: Without Love Letters:)
  - No tienes una Carta de Amor para dar.
  - (pop-up)
    - (Pop-up: You do not have a Love Letter to give.)
- (Condition: With Love Letters:)
  - {{Tinput|How many letters do you want to give?}}
  - (Condition: After entering a positive number:)
    - ((A random dialogue is selected from the following, then continues below:))
      - **Dark Romancer:** No puedo esperar para quemar esto.
      - **Dark Romancer:** ¡Bien!
      - **Dark Romancer:** Oh, está bien.
      - **Dark Romancer:** Está bien...
      - **Dark Romancer:** Sí, nunca abriré esto.
    - **Dark Romancer:** ¡Gracias, supongo! Toma, toma esto.
    - [Menu]: ¿Qué te gustaría (por 1 letra)?
      - [Choice]: +20 % de XP durante +5 minutos (hasta 60 minutos como máximo)
        - (Condition: If the player is already receiving a +5% XP boost from witnessing a love letter being ripped up:)
          - Tienes un aumento activo de XP del 5% al presenciar una estafa de Love Letter. Activar esto borrará el impulso actual.
          - [Menu]: ¿Continuar?
            - [Choice]: Sí.
              - (continue)
            - [Choice]: No.
              - (end)
        - (removes=the chosen number of love letters)
        - Ahora tienes un aumento de XP del 20 % durante los minutos [número] y los segundos [número].
        - ((Repeated in a pop-up:))
          - (Pop-up: You now have a 20% XP boost for [number] minutes and [number] seconds.|colour=#63D21D)
      - [Choice]: +25 % de bonificación de XP quemada durante +5 minutos (hasta 60 minutos como máximo)
        - (removes=the chosen number of love letters)
        - Ahora tienes un aumento de quema de XP adicional del 25 % durante [número] minutos y [número] segundos.
        - ((Repeated in a pop-up:))
          - (Pop-up: You now have a 25% Bonus XP burn boost for [number] minutes and [number] seconds.|colour=#63D21D)
      - [Choice]: 250x corazones
        - (removes=the chosen number of love letters) (receives=250 heartments per letter handed in)
        - Obtienes corazones [número].

#### Al dar cartas


##### Debajo de cinco letras

- Progreso hacia el título rojo de 'The Hater': [1/2/3/4]/5

##### Al entregar la quinta carta

- ¡Felicitaciones! Has desbloqueado: el Hater. Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
- ((Repeated in a pop-up:))
  - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: el Hater. Tus nuevos elementos se pueden encontrar en la interfaz de personalizaciones.|color=#00FF00)

##### Entre cinco y diez letras

- Progreso hacia el título de la variante gris de 'The Hater': [5/6/7/8/9]/10

##### Al dar la décima carta

- ¡Felicitaciones! Has desbloqueado: el Hater (gris). Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
- ((Repeated in a pop-up:))
  - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: el Hater (gris). Tus nuevos elementos se pueden encontrar en la interfaz de personalizaciones.|color=#00FF00)

##### Entre diez y veinte letras

- Progreso hacia el título de la variante roja y gris de 'The Hater': [10/11/12/13/14/15/16/17/18/19]/20

##### Al entregar la vigésima carta

- ¡Felicitaciones! Has desbloqueado: el Hater (rojo y gris). Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
- ((Repeated in a pop-up:))
  - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: el Hater (rojo y gris). Tus nuevos elementos se pueden encontrar en la interfaz de personalizaciones.|color=#00FF00)
