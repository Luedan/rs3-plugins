# Bank guard

- **Original Wiki Page**: [Transcript:Bank guard](https://runescape.wiki/w/Transcript%3ABank%20guard)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Love Story


#### Primera vez

- **Bank Guard:** ¿Sí?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Puedo depositar mis cosas aquí?
    - **Player:** Hola. ¿Puedo depositar mis cosas aquí?
    - **Bank Guard:** No. Soy security guard, no empleado de banco.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Esa pared no se ve muy bien.
        - (abajo)
      - [Choice]: Muy bien, dejaré de molestarte ahora.
        - **Player:** Muy bien, dejaré de molestarte ahora.
        - **Bank Guard:** Buenos días, [sir/madam].
  - [Choice]: Esa pared no se ve muy bien.
    - **Player:** Esa pared no se ve muy bien.
    - **Bank Guard:** No, no es así.
      - [Choice]: ¿Me vas a decir qué pasó?
        - **Player:** ¿Me vas a contar qué pasó?
        - **Bank Guard:** Podría hacerlo.
        - **Player:** ¡Está bien, continúa!
        - **Bank Guard:** Alguien rompió la pared cuando <br> estaban robando el banco.
        - **Player:** ¿Alguien ha robado el banco?
        - **Bank Guard:** Sí.
        - **Player:** Pero... ¿alguien resultó herido? <br>¿Obtuvieron algo valioso?
        - **Bank Guard:** Sí, pero pudimos conseguir más staff y reparar la pared con bastante facilidad.
        - **Bank Guard:** El Banco ya repuso todos los objetos robados que pertenecían a los clientes.
        - **Player:** Oh, bien... ¿pero el banco staff resultó herido?
        - **Bank Guard:** Sí, pero los nuevos son igual de buenos.
        - **Player:** No eres muy amable, ¿verdad?
        - **Bank Guard:** Nadie espera que sea amable.
        - **Player:** De todos modos... Entonces, ¿alguien ha robado el banco?
        - **Bank Guard:** Sí.
        - **Player:** ¿Sabes quién lo hizo?
        - **Bank Guard:** Estamos bastante seguros de saber quién fue el ladrón. La grabación de seguridad resultó dañada durante el ataque, pero todavía muestra su rostro con bastante claridad.
        - **Player:** ¿Tienes una grabación de seguridad?
        - **Bank Guard:** Sí. Nuestras aseguradoras insistieron en que <br>instaláramos un orbe mágico de visión.
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: ¿Puedo ver la grabación?
            - **Player:** ¿Puedo ver la grabación?
            - **Bank Guard:** Supongo que sí. Pero es bastante largo.
            - [Menu]: ¿Quieres ver la grabación?
              - [Choice]: Está bien, muéstrame la grabación.
                - **Player:** Está bien, muéstrame la grabación.
                - **Bank Guard:** Muy bien... El dispositivo de reproducción mágico del banco introducirá las imágenes grabadas en tu mente. Sólo cierra los ojos.
                - Cierras los ojos y miras la grabación...
                - (ver | Robo del banco Draynor)
                - Fin de la grabación.
              - [Choice]: Gracias, tal vez otro día.
                - **Player:** Gracias, tal vez otro día.
                - **Bank Guard:** Vale.
          - [Choice]: Entonces ¿quién fue el ladrón?
            - **Player:** Entonces, ¿quién fue el ladrón?
            - **Bank Guard:** No puedo revelar esa información.
            - [Menu]: ¿Qué te gustaría decir?
              - [Choice]: ¿Puedo ver la grabación?
                - (arriba)
              - [Choice]: Muy bien, dejaré de molestarte ahora.
                - (abajo)
      - [Choice]: Muy bien, dejaré de molestarte ahora.
        - (arriba)
  - [Choice]: Lo siento, no quiero nada.
    - **Player:** Lo siento, no quiero nada.
    - **Bank Guard:** Vale.

#### Tiempos posteriores


##### Antes de ver la grabación

- **Bank Guard:** ¿Sí?
- **Player:** ¿Ya tienes idea de quién robó el banco?
- **Bank Guard:** Estamos bastante seguros de saber quién fue el ladrón. La grabación de seguridad resultó dañada durante el ataque, pero todavía muestra su rostro con bastante claridad.
- **Player:** ¿Tienes una grabación de seguridad?
- **Bank Guard:** Sí. Nuestras aseguradoras insistieron en que <br>instaláramos un orbe mágico de visión.
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Puedo ver la grabación?
    - (above|recording)
  - [Choice]: Entonces ¿quién fue el ladrón?
    - (above|robber)

##### Después de ver la grabación

- **Bank Guard:** ¿Sí?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: El ladrón de la grabación me resultaba familiar.
    - **Player:** El ladrón de la grabación me resultaba familiar.
    - **Bank Guard:** Oh, ¿tú también lo reconociste?
    - **Player:** ¡Sí, y puedo decirte dónde vive!
    - **Bank Guard:** Gracias, pero ya sabemos dónde encontrar a nuestro sospechoso.
    - **Player:** Entonces, ¿vas a hacer que lo arresten?
    - **Bank Guard:** Ciertamente lo estamos vigilando. Me temo que no puedo darle más detalles sobre el caso.
    - **Player:** Muy bien.
  - [Choice]: ¿Puedo ver esa grabación otra vez, por favor?
    - **Player:** ¿Puedo ver esa grabación otra vez, por favor?
    - **Bank Guard:** Me gustaría que me pagaras 50 po primero.
    - (Condition: With enough money in backpack or money pouch:)
      - [Menu]: ¿Pagar 50 po para volver a ver la grabación?
        - [Choice]: Bien, aquí tienes 50 po.
          - **Player:** Bien, aquí tienes 50 po.
          - Cierras los ojos y miras la grabación...
          - (ver | Robo del banco Draynor)
          - Fin de la grabación.
        - [Choice]: Gracias, tal vez otro día.
          - **Player:** Gracias, tal vez otro día.
          - **Bank Guard:** Vale.
    - (Condition: Without enough money in backpack or money pouch:)
      - **Player:** No llevo tanto.
      - (Condition: Without enough money in bank:)
        - **Bank Guard:** Oh, bueno, tal vez otro día.
      - (Condition: With enough money in bank:)
        - **Bank Guard:** Como empleado de banco, supongo que podría sacar el dinero directamente de tu cuenta bancaria.
        - [Menu]: ¿Pagar 50 po para volver a ver la grabación?
          - [Choice]: Bien, puedes sacar 50 po de mi cuenta bancaria.
            - (arriba)
          - [Choice]: Gracias, tal vez otro día.
            - (arriba)
  - [Choice]: Lo siento, no quiero nada.
    - **Player:** Lo siento, no quiero nada.
    - **Bank Guard:** Vale.

### After Love Story

- **Bank Guard:** ¿Sí?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: El ladrón de la grabación me resultaba familiar.
    - **Player:** El ladrón de la grabación me resultaba familiar.
    - **Bank Guard:** Oh, ¿tú también lo reconociste?
    - **Player:** ¡Sí, y admitió que fue él quien cometió el robo!
    - **Bank Guard:** La cantidad de pruebas en su contra hace que eso sea casi innecesario.
    - **Player:** Entonces, ¿vas a hacer que lo arresten?
    - **Bank Guard:** Creo que los staff de Wizards' Tower le han dado una lección y se están asegurando de que no cause más problemas en el futuro.
    - **Bank Guard:** Los ingresos que recibimos de las personas que vieron la grabación cubrieron adecuadamente el efectivo robado del banco, por lo que el banco de Gielinor está satisfecho.
    - **Player:** Muy bien.
  - [Choice]: ¿Puedo ver esa grabación otra vez, por favor?
    - (arriba)
  - [Choice]: Lo siento, no quiero nada.
    - (arriba)
