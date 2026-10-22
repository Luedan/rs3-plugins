# Eniola

- **Original Wiki Page**: [Transcript:Eniola](https://runescape.wiki/w/Transcript%3AEniola)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Bank

- ((The rune payment interface opens.))
- (Condition: If the player has enough runes of the chosen type with them:)
  - (removes=20 of the selected rune)
  - (opens=Bank)
- (Condition: If the player does not have enough runes of the chosen type with them:)
  - **Eniola:** Me temo que no tienes las runas necesarias contigo en este momento, por lo que no puedo permitirte acceder a tu cuenta. Traiga veinte runas de un tipo y podrá abrir su cuenta.

### Talk to

- **Eniola:** ¡Bien conocido, compañero aventurero! ¿Le puedo ayudar en algo?
- (Condition: If the player has items they can collect from the Grand Exchange:)
  - **Eniola:** Antes de continuar, debo informarle que tiene artículos listos para ser recogidos en Grand Exchange.
  - (continue)
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Eniola:** Qué terriblemente grosero de mi parte, mi querido [chap/lady]. Mi nombre es Eniola y trabajo para la excelente empresa, el Banco de Gielinor.
    - [Menu]: Selecciona una opción
      - [Choice]: Si trabajas en el banco, ¿qué haces aquí?
        - **Player:** Si trabajas para el banco, ¿qué haces aquí?
        - **Eniola:** Mi presencia aquí es el comienzo de una nueva empresa de bancos ambulantes.
        - **Eniola:** Yo y otros como yo le brindaremos la comodidad de contar con servicios bancarios que le serán de máxima utilidad.
        - **Player:** Entonces... ¿qué estás haciendo aquí?
        - **Eniola:** La Z.M.I., es decir el Instituto Mágico Zamorakiano, solicitó mis servicios al descubrir este altar. Nosotros en el Banco de Gielinor somos una parte neutral y estamos dispuestos a ofrecer nuestros servicios independientemente de su afiliación.
        - **Eniola:** Por eso estoy aquí.
        - **Player:** ¿Puedo acceder a mi cuenta bancaria hablando con usted?
        - **Eniola:** Por supuesto, querido [sir/lady].
        - **Eniola:** Sin embargo, debo informarles que debido a que el Z.M.I. están pagando por mis servicios, exigen que cualquier persona que no sea parte del Instituto pague una tarifa de acceso para abrir su cuenta bancaria.
        - **Eniola:** Pero, como nuestro objetivo como banqueros ambulantes es hacer la vida de nuestros clientes más cómoda, nos adaptamos a sus necesidades. Sabemos que estará ocupado creando runas y no desea llevar dinero consigo. El cargo por abrir su cuenta es la pequeña cantidad de veinte de un tipo de runa. El tipo de runa depende de ti.
        - **Eniola:** ¿Te gustaría pagar el precio de veinte runas para abrir tu cuenta bancaria?
          - [Menu]: Selecciona una opción
            - [Choice]: Sí por favor.
              - **Player:** Sí, por favor.
              - (above|Bank)
            - [Choice]: Déjame abrir mi cuenta y luego te daré las runas.
              - **Player:** No tengo las runas encima. Déjame abrir mi cuenta y luego te los daré.
              - **Eniola:** No es que no confíe en ti, viejo [chap/girl], pero como dice el viejo refrán: "El pago está antes que los amigos".
            - [Choice]: ¡De ninguna manera! No estoy pagando para retirar mi propio dinero.
              - **Player:** ¡Eso es absurdo! No estoy pagando runas para retirar mis propias cosas.
              - **Eniola:** Lamento oír eso, [sir/madam]. Si debes reconsiderarlo, porque creo que este servicio ofrece una excelente relación calidad-precio, no dudes en contactarme.
      - [Choice]: Me gustaría acceder a mi cuenta bancaria, por favor.
        - (above|Bank)
      - [Choice]: Me gustaría verificar la configuración de mi PIN.
        - (opens=Bank PIN)
  - [Choice]: Me gustaría acceder a mi cuenta bancaria, por favor.
    - [Menu]: Cuesta veinte runas de un tipo.<br>¿Quieres continuar?
      - [Choice]: si
        - (above|Bank)
      - [Choice]: No
        - (end)
  - [Choice]: Me gustaría verificar la configuración de mi PIN.
    - (opens=Bank PIN)
  - [Choice]: Me gustaría ver mi caja de Colección.
    - (continue|Collect)

### Collect

- ((The rune payment interface opens.))
- (Condition: If the player has enough runes of the chosen type with them:)
  - (removes=20 of the selected rune)
  - (opens=Collection box)
- (Condition: If the player does not have enough runes of the chosen type with them:)
  - **Eniola:** Me temo que no tienes las runas necesarias contigo en este momento, por lo que no puedo permitirte acceder a tu cuenta. Traiga veinte runas de un tipo y podrá abrir su cuenta.
