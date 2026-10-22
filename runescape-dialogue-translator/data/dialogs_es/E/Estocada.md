# Estocada

- **Original Wiki Page**: [Transcript:Estocada](https://runescape.wiki/w/Transcript%3AEstocada)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talking to Estocada

- (Condition: If either variant of duellist's cap has never been claimed:)
  - **Estocada:** Ah, una cara nueva. Estás aquí para fi- Ah, sí, quiero decir... estás aquí para vestirte a la moda, ¿no?
  - [Menu]: Selecciona una opción
    - [Choice]: Sí, eso es correcto.
      - **Player:** Sí, así es.
      - **Estocada:** ¡Me alegra oírlo! Entonces tengo algo para ti.
      - (Condition: If there is no backpack space:)
        - **Estocada:** Una vez que tengas espacio para llevarlo, claro está.
        - (continue|about-hat)
      - (receives=duellist's cap)
      - [Estocada te ofrece un sombrero de ala ancha.]
      - **Estocada:** Este sombrero es bastante especial, amigo mío. No suelo dar regalos, pero cuando lo hago, prefiero dárselos a los duelistas.
      - (continue|about-hat)
    - [Choice]: Mmmm, no.
      - **Player:** Erm, no.
      - **Estocada:** Ah. Me sorprendes.
      - (continue)
- (Condition: If either variant of the duellist's cap has been claimed before:)
  - (Condition: If the player has not lost both variants of duellist's cap:)
    - **Estocada:** Ahh, un duelista. Mantente victorioso, amigo mío.
    - (continue)
  - (Condition: If the player has lost either variant of duellist's cap:)
    - **Estocada:** Amigo mío, no tienes tu sombrero. ¿A dónde se fue?
    - **Player:** Lo perdí.
    - **Estocada:** Bueno, no es un problema, estas cosas se pueden superar.
    - (Condition: If there is no backpack space:)
      - **Estocada:** Todo lo que debes hacer es hablar conmigo una vez que haya espacio para realizar este reemplazo.
      - (continue)
    - (Condition: If the duellist's cap has been lost:)
      - (receives=duellist's cap)
      - (Condition: Before the removal of Duel Arena:)
        - **Estocada:** No suelo reemplazar sombreros, pero, cuando lo hago, elijo reemplazar las gorras de los duelistas.
        - (continue)
      - (Condition: After the removal of Duel Arena:)
        - **Estocada:** No suelo reemplazar los sombreros, pero, cuando lo hago, elijo solo lo último en moda.
        - (continue)
    - (Condition: If the antique duellist's cap has been lost and the duellist's cap wasn't just claimed:)
      - (receives=antique duellist's cap)
      - **Estocada:** No suelo reemplazar sombreros, pero tú eras un luchador en la antigua arena. ¿Cómo podría decir que no?
      - (continue)
    - **Player:** ¡Gracias!
    - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: Entonces cuéntame más sobre este sombrero.
    - **Player:** Entonces cuéntame más sobre este sombrero.
    - (Condition: Before the removal of Duel Arena:)
      - **Estocada:** Todo el tiempo que tengas este sombrero contigo o en tu banco, te verá ganar o caer en el Duel Arena y tomar nota. Gracias a su magia, puedes convertirte en una estatua, que muestra a quienes leen su placa lo bien que has luchado: a cuántos derrotas, tu racha de victorias y cosas por el estilo. Si lo deseas, puedes hacer que el sombrero olvide todo lo que ha visto de tu destreza o indicarle que no muestre ciertos elementos.
      - (continue)
    - (Condition: After the removal of Duel Arena:)
      - (Condition: Players battled there before:)
        - **Estocada:** El Duel Arena fue una vez un brillante símbolo de destreza en duelo... hasta que fue tragado por el desierto. Si recuerdas la época del Duel Arena y luchaste allí, este sombrero también te recordará.
        - **Estocada:** Gracias a su magia, puedes convertirte en una estatua, que muestra a quienes leen su placa lo bien que luchaste en la arena antes de que cayera: a cuántos derrotaste, tu racha de victorias y cosas por el estilo.
        - **Estocada:** Si lo deseas, puedes hacer que el sombrero olvide todo lo que ha visto de tu destreza. Aunque es posible que el Duel Arena ya no esté, aún puedes recuperar la gloria batiéndote en duelo con otros aventureros en Gielinor.
        - (continue)
      - (Condition: Players did not battle in Duel Arena:)
        - **Estocada:** El Duel Arena fue una vez un brillante símbolo de destreza en duelo... hasta que fue tragado por el desierto. Lo poco que queda se encuentra al norte de aquí.
        - **Estocada:** En aquel entonces, se usaban sombreros para mostrar tus habilidades: cuántos derrotabas, tu racha de victorias y cosas por el estilo.
        - **Estocada:** Hoy en día, se utilizan para mostrar tu éxito al batirte en duelo con otros aventureros en Gielinor.
        - (continue)
    - **Player:** ¡Útil, gracias!
  - [Choice]: Adiós.
    - **Player:** Adiós.
