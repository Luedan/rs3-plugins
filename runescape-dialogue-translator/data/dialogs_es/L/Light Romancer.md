# Light Romancer

- **Original Wiki Page**: [Transcript:Light Romancer](https://runescape.wiki/w/Transcript%3ALight%20Romancer)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Player:** ¡Hola!
- **Light Romancer:** ¡Hola!
- **Player:** ¿Qué haces aquí?
- **Light Romancer:** Por supuesto, es la época más amorosa del año, así que estoy buscando Cartas de Amor.
- **Player:** ¿Cartas de amor?
- **Light Romancer:** ¡Sí! ¡Son simplemente los mejores!
- [Trae Light Romancer Love Letters antes de que finalice el 17 de febrero para avanzar hacia el título y las variantes de color de 'The Lover', así como uno de los siguientes:]
- [Aumento de XP del 20 % durante +5 minutos (hasta 60 minutos como máximo).<br> Aumento de quema de XP adicional del 25 % +5 minutos (hasta 60 minutos como máximo).<br>250x Corazones.]
- [Si no quieres entregar cartas de amor, o Light Romancer se ha ido, puedes romperlas, lo que otorga un aumento de XP del 5 % durante +5 minutos (hasta 60 minutos como máximo) a todos los jugadores que las vean.]
- (Condition: Without Love Letters:)
  - **Player:** Si encuentro alguno, ¡te lo traeré!
  - **Light Romancer:** ¡Gracias!
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
      - **Light Romancer:** ¿Para mí?
      - **Light Romancer:** ¡Qué lindo!
      - **Light Romancer:** ¡Oh, eso es encantador!
      - **Light Romancer:** ¡Qué dulce!
      - **Light Romancer:** ¡Muy lindo!
    - **Light Romancer:** ¡Gracias! Me gustaría darte algo a cambio.
    - [Menu]: ¿Qué te gustaría (por 1 letra)?
      - [Choice]: +20 % de XP durante +5 minutos (hasta 60 minutos como máximo)
        - (Condition: If the player is already receiving a +5% XP boost from witnessing a love letter being ripped up:)
          - Tienes un aumento activo de XP del 5% al presenciar una estafa de Love Letter. Activar esto borrará el impulso actual.
          - [Menu]: ¿Continuar?
            - [Choice]: Sí.
              - (continue)
            - [Choice]: No.
              - (end)
        - (Condition: With at least 55 minutes of the buff active:)
          - [La duración del impulso de Love Letter BXP tendrá un límite de 60 minutos. ¿Quieres continuar?]
          - [Menu]: ¿Continuar?
            - [Choice]: Sí.
              - (continue)
            - [Choice]: No.
              - (end)
        - (removes=the chosen number of love letters)
        - Ahora tienes un aumento de XP del 20 % durante los minutos [número] y los segundos [número].
        - ((Repeated in a pop-up:))
          - (Pop-up: You now have a 20% XP boost for [number] minutes and [number] seconds.|colour=#63D21D)
          - (continue)
        - (continue|Upon giving letters)
      - [Choice]: +25 % de bonificación de XP quemada durante +5 minutos (hasta 60 minutos como máximo)
        - (Condition: With at least 55 minutes of the buff active:)
          - [La duración del impulso de grabación de Love Letter BXP tendrá un límite de 60 minutos. ¿Quieres continuar?]
          - [Menu]: ¿Continuar?
            - [Choice]: Sí.
              - (continue)
            - [Choice]: No.
              - (end)
        - (removes=the chosen number of love letters)
        - (Condition: Not having given over 20 Love Letters previously:)
          - (continue|Upon giving letters)
      - [Choice]: 250x corazones
        - (removes=the chosen number of love letters) (receives=250 heartments per letter handed in)
        - Obtienes corazones [número].
        - (Condition: Not having given over 20 Love Letters previously:)
          - (continue|Upon giving letters)

#### Al dar cartas


##### Debajo de cinco letras

- Progreso hacia el título rojo de 'The Lover': [1/2/3/4]/5

##### Al entregar la quinta carta

- ¡Felicitaciones! Has desbloqueado: el Amante. Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
- ((Repeated in a pop-up:))
  - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: el Amante. Tus nuevos artículos se pueden encontrar en la Interfaz de personalizaciones.|color=#00FF00)

##### Entre cinco y diez letras

- Progreso hacia el título de la variante rosa de 'The Lover': [5/6/7/8/9]/10

##### Al dar la décima carta

- ¡Felicitaciones! Has desbloqueado: el Amante (rosa). Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
- ((Repeated in a pop-up:))
  - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: el Amante (rosa). Tus nuevos artículos se pueden encontrar en la Interfaz de personalizaciones.|color=#00FF00)

##### Entre diez y veinte letras

- Progreso hacia el título de la variante roja y rosa de 'The Lover': [10/11/12/13/14/15/16/17/18/19]/20

##### Al entregar la vigésima carta

- ¡Felicitaciones! Has desbloqueado: el Amante (rojo y rosa). Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
- ((Repeated in a pop-up:))
  - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: el Amante (rojo y rosa). Tus nuevos artículos se pueden encontrar en la Interfaz de personalizaciones.|color=#00FF00)
