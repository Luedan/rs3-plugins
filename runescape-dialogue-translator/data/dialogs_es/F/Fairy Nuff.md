# Fairy Nuff

- **Original Wiki Page**: [Transcript:Fairy Nuff](https://runescape.wiki/w/Transcript%3AFairy%20Nuff)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before A Fairy Tale I - Growing Pains


#### Primera vez

- **Fairy Nuff:** Hola, ¿puedo ayudarte en algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué haces por aquí?
    - **Player:** ¿Qué haces por aquí?
    - **Fairy Nuff:** Oh, soy el sanador residente. Mi nombre es Nuff, Fairy Nuff. ¿Quién eres?
    - **Player:** Mi nombre es Player.
    - **Fairy Nuff:** Encantado de conocerte, Player. Como decía, soy el sanador de Zanaris. Me gradué hace más de 200 años humanos. Mira, ahí está mi Certificado de Curación Avanzada en la pared. Nunca voy a ningún lado sin él. Mi trabajo es cuidar de las hadas enfermas, heridas o moribundas de aquí. Por supuesto, como las hadas son mágicas por naturaleza, no muchas de ellas resultan heridas, así que normalmente no tengo mucho que hacer.
    - **Player:** ¿Qué pasa con la curación de humanos? Muchos aventureros deben resultar heridos luchando contra seres del Otro Mundo.
    - **Fairy Nuff:** Sí, lo hacen. Tonto ¿no? A veces uso mi magia curativa con humanos, pero no me gusta que ataquen a nuestros otros invitados, así que les cobro por el servicio.
    - **Player:** ¿Cuánto cobras por curar a alguien, entonces?
    - **Fairy Nuff:** Bueno, el oro que tanto les gusta a los humanos no tiene valor real en Zanaris, así que les pido a mis pacientes que me paguen en gemas. Curaré 40 puntos de vida por un ópalo, 50 puntos de vida por un zafiro o un trozo de jade, 70 puntos de vida por una esmeralda o topacio rojo, 90 por un rubí y 110 por un diamante.
    - **Player:** ¿Solo 110 puntos de vida por un diamante? ¿No parece un poco caro?
    - **Fairy Nuff:** Quizás para ti, pero te sorprendería saber cuántos aventureros están dispuestos a pagar esos precios.
  - [Choice]: No gracias. Sólo mirando a mi alrededor.
    - **Player:** No, gracias. Sólo mirando a mi alrededor.
    - **Fairy Nuff:** Está bien. Si quieres saber algo, sólo pregunta.

#### Tiempos posteriores

- **Fairy Nuff:** Hola Player, ¿necesitas ayuda?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, por favor. Necesito curación.
    - **Player:** Sí, por favor. Necesito curación.
    - **Fairy Nuff:** Claro, ¿cuántos puntos de vida te gustaría que sane?
    - [Menu]: Selecciona una opción
      - [Choice]: 40 puntos de vida.
        - **Player:** 40 puntos de vida.
        - **Fairy Nuff:** Eso te costará 1 ópalo.
        - [Menu]: Selecciona una opción
          - [Choice]: Muy bien.
            - **Player:** Muy bien.
            - (Condition: Si el player tiene un ópalo en backpack:)
              - (removes=opal)
              - (Action: el player se cura un máximo de 40 puntos de vida.)
            - (Condition: Si el player no tiene un ópalo en backpack:)
              - **Fairy Nuff:** ¡No tienes que pagarme!
              - **Player:** Vaya, lo siento.
          - [Choice]: Pensándolo bien, no gracias.
            - **Player:** Pensándolo bien, no, gracias.
            - **Fairy Nuff:** Está bien, haz lo que quieras.
      - [Choice]: 50 puntos de vida.
        - **Player:** 50 puntos de vida.
        - **Fairy Nuff:** Eso te costará 1 zafiro o 1 pieza de jade.
        - [Menu]: Selecciona una opción
          - [Choice]: Muy bien.
            - **Player:** Muy bien.
            - (Condition: Si el player tiene un zafiro o jade en el backpack:)
              - (removes=sapphire or jade)
              - (Action: el player se cura un máximo de 50 puntos de vida.)
            - (Condition: Si el player no tiene zafiro o jade en backpack:)
              - **Fairy Nuff:** ¡No llevas ni un zafiro ni un trozo de jade contigo!
              - **Player:** Vaya, lo siento.
          - [Choice]: Pensándolo bien, no gracias.
            - **Player:** Pensándolo bien, no, gracias.
            - **Fairy Nuff:** Está bien, haz lo que quieras.
      - [Choice]: 70 puntos de vida.
        - **Player:** 70 puntos de vida.
        - **Fairy Nuff:** Eso te costará 1 esmeralda o 1 topacio rojo.
        - [Menu]: Selecciona una opción
          - [Choice]: Muy bien.
            - **Player:** Muy bien.
            - (Condition: Si el player tiene una esmeralda o un topacio rojo en el backpack:)
              - (removes=emerald or red topaz)
              - (Action: el player se cura un máximo de 70 puntos de vida.)
            - (Condition: Si el player no tiene una esmeralda o un topacio rojo en el backpack:)
              - **Fairy Nuff:** ¡No tienes una esmeralda o un topacio rojo para pagarme!
              - **Player:** Vaya, lo siento.
          - [Choice]: Pensándolo bien, no gracias.
            - **Player:** Pensándolo bien, no, gracias.
            - **Fairy Nuff:** Está bien, haz lo que quieras.
      - [Choice]: 90 puntos de vida.
        - **Player:** 90 puntos de vida.
        - **Fairy Nuff:** Eso te costará 1 rubí.
        - [Menu]: Selecciona una opción
          - [Choice]: Muy bien.
            - **Player:** Muy bien.
            - (Condition: Si el player tiene un rubí en backpack:)
              - (removes=ruby)
              - (Action: el player se cura un máximo de 90 puntos de vida.)
            - (Condition: Si el player no tiene un rubí en backpack:)
              - **Fairy Nuff:** ¡No tienes ni un rubí para pagarme!
              - **Player:** Vaya, lo siento.
          - [Choice]: Pensándolo bien, no gracias.
            - **Player:** Pensándolo bien, no, gracias.
            - **Fairy Nuff:** Está bien, haz lo que quieras.
      - [Choice]: 110 puntos de vida.
        - **Player:** 110 puntos de vida.
        - **Fairy Nuff:** Eso te costará 1 diamante.
        - [Menu]: Selecciona una opción
          - [Choice]: Muy bien.
            - **Player:** Muy bien.
            - (Condition: Si el player tiene un diamante en backpack:)
              - (removes=diamond)
              - (Action: el player se cura un máximo de 110 puntos de vida.)
            - (Condition: Si el player no tiene un diamante en backpack:)
              - **Fairy Nuff:** ¡No tienes un diamante para pagarme!
              - **Player:** Vaya, lo siento.
          - [Choice]: Pensándolo bien, no gracias.
            - **Player:** Pensándolo bien, no, gracias.
            - **Fairy Nuff:** Está bien, haz lo que quieras.
  - [Choice]: No gracias. Sólo mirando a mi alrededor.
    - **Player:** No, gracias. Sólo mirando a mi alrededor.
    - **Fairy Nuff:** Está bien. Si quieres saber algo, sólo pregunta.

### After Fairy Tale II

- **Fairy Nuff:** Muchas gracias por todo lo que has hecho por nosotros, Player.

### After Fairy Tale III

- **Fairy Nuff:** Oh, Player, ¡muchas gracias por tu ayuda! ¡Eres un verdadero amigo para nosotras las hadas!

### Treasure Trails


#### Recibiendo la caja del rompecabezas

- **Fairy Nuff:** ¡Tengo un rompecabezas para ti!
- (receives=puzzle box)
- [¡Fairy Nuff te ha regalado una caja de rompecabezas!]

#### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- **Fairy Nuff:** ¿Es ese tu mejor intento? Tendrás que esforzarte más.

#### Cuando se le habla con el rompecabezas resuelto

- (Condition: Si el rastro continúa:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [¡Fairy Nuff te ha dado otro pergamino de pistas!]
  - (continue)
- (Condition: Si el sendero termina:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Fairy Nuff:** ¡Ahí lo tienes!
