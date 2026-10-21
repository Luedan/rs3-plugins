# Doronbol

- **Original Wiki Page**: [Transcript:Doronbol](https://runescape.wiki/w/Transcript%3ADoronbol)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### Sin amuleto de lengua de gato

- **Doronbol:** ¿Miau?

#### Con un amuleto de lengua de gato


##### Antes de que todos se enciendan

- **Player:** Hola, gato. ¿Qué diablos estás haciendo aquí?
- **Doronbol:** Oh, estoy cuidando esta baliza para King Roald.
- **Player:** ¿Cómo te va?
- **Doronbol:** Todo está bien, la vida es pacífica, las flores florecen, los pájaros cantan y hoy es el día más hermoso.
- **Player:** ¡Vaya, pareces muy contento con las cosas!
- **Doronbol:** ¡Lo soy! ¡Estoy tan feliz que no puedo evitar mover la cola y dar vueltas imprudentemente!
- **Doronbol:** Es agradable tener un propósito tan elevado en la vida y haberse ganado la confianza y el afecto de un ser humano tan noble como King Roald.
- **Player:** Espera, eres un gato, ¿verdad? ¿No es un perro disfrazado?
- **Doronbol:** Eh, con "mover la cola" quise decir... um... "ronronear muy fuerte". Y, sólo para que conste, soy completamente indiferente a los humanos. Y distante. Soy muy, muy distante.
- **Player:** Eso suena más bien.
- **Doronbol:** Oye, no repetirás lo que dije antes, ¿verdad? No quisiera más marcas en mi licencia de gato.
- **Player:** No te preocupes, moggy; Tus secretos están a salvo conmigo.
- **Doronbol:** ¡Purrrrrrr!

##### Después de todo encendido pero antes de Una cola de dos gatos

- **Player:** Hola. Me preguntaba si podrías ayudarme.
- **Doronbol:** Eso depende. ¿Puedes contarme alguna historia interesante? Es bastante aburrido por aquí, ¿sabes?
- **Player:** ¡Por supuesto que puedo contarte grandes historias! Soy un aventurero increíblemente interesante, ¿no lo sabes?
- **Doronbol:** ¡Pshaw! No me interesan tus aburridas historias humanas, me interesan algunos buenos chismes felinos.
- **Player:** Oh, eh...
- **Doronbol:** Oh, no importa; era pedir mucho. Si encuentras alguna cosita jugosa, pasa por aquí para charlar.
- [A Tail of Two Cats].}}

##### Después de todo entusiasmado y después de Una cola de dos gatos

- **Doronbol:** ¡Rronroneo! Hola. ¿Hay algo que pueda hacer por ti?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: Si la baliza está apagada:)
      - **Doronbol:** Por supuesto. Una vez que la baliza esté encendida, déjame 5 logs y yo me ocuparé del fuego todo el tiempo que pueda.
    - (Condition: Si la baliza está muriendo:)
      - **Doronbol:** Bueno, podría, pero ya que estás aquí, es mejor que lo hagas tú mismo.
    - (Condition: Si la baliza no muere:)
      - (Condition: Si Doronbol no tiene cinco logs:)
        - (Condition: Si el player no tiene al menos cinco logs del mismo tipo:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Doronbol:** Me temo que no tienes suficiente logs del tipo correcto para que yo lo use.
        - (Condition: Si el player tiene al menos cinco logs del mismo tipo:)
          - (Condition: Si el mensaje de confirmación está habilitado:)
            - **Doronbol:** Necesitaré cinco logs para poder atender el fuego. ¿Está bien? Ronroneo.
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Doronbol:** ¡Gracias! Usaré estos cinco logs para mantener encendida la baliza mientras estás fuera.
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Doronbol:** >Bueno, ya sabes dónde estoy si cambias de opinión.
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: Si el mensaje de confirmación está deshabilitado:)
            - (above|talk-give-logs)
      - (Condition: Si Doronbol tiene cinco logs:)
        - **Doronbol:** Por supuesto que lo haré, no te preocupes. Usaré el logs que ya me dejaste.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Doronbol:** Ronroneo. ¡Seguro! Sólo echa un vistazo a este mapa mío.
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given Doronbol a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Doronbol:** Bueno, puede que sea bajo, pero puedo ver muy lejos. Puedo decirte cuántas balizas están encendidas en cada dirección.
    - **Doronbol:** Sin embargo, si quieres saber más sobre las balizas más allá de eso, necesitaré la ayuda de una criatura cuyos ojos son incluso más agudos que los míos.
    - **Player:** ¿Qué clase de criatura es esa?
    - **Doronbol:** Una criatura que puede ver el mundo desde arriba y que es lo suficientemente inteligente como para informar sobre lo que ha descubierto.
    - **Player:** Sí, pero ¿qué tipo de criatura exactamente?
    - **Doronbol:** Ronroneo…una guacamaya.
    - **Player:** ¿Una guacamaya?
    - **Doronbol:** Sí, una guacamaya deliciosa y deliciosa. Ronroneo.
    - **Player:** Sólo estás intentando engañarme para que te traiga un bocadillo, ¿no?
    - **Doronbol:** No, no. Lamentablemente, si me trajeras un guacamayo con el fin de obtener información sobre las balizas, mi integridad como bombero exigiría que no lo usara como almuerzo.
    - ((Si el player tiene una bolsa de guacamayo en su backpack:))
      - **Player:** Ya veo. Qué noble.
      - (continue|macaw)
  - [Choice]: ¿Cómo te va?
    - **Player:** ¿Cómo te va?
    - **Doronbol:** Todo está bien, la vida es pacífica, las flores están floreciendo, los pájaros cantan y hoy es el día más hermoso.
    - **Player:** ¡Vaya, pareces muy contento con las cosas!
    - **Doronbol:** ¡Lo soy! ¡Estoy tan feliz que no puedo evitar mover la cola y dar vueltas imprudentemente!
    - **Doronbol:** Es agradable tener un propósito tan elevado en la vida y haberse ganado la confianza y el afecto de un ser humano tan noble como King Roald.
    - **Player:** Espera, eres un gato, ¿verdad? ¿No es un perro disfrazado?
    - **Doronbol:** Eh, con "mover la cola" quise decir... um... "ronronear muy fuerte". Y, sólo para que conste, soy completamente indiferente a los humanos. Y distante. Soy muy, muy distante.
    - **Player:** Eso suena más bien.
    - **Doronbol:** Oye, no repetirás lo que dije antes, ¿verdad? No quisiera más marcas en mi licencia de gato.
    - **Player:** No te preocupes, moggy; Tus secretos están a salvo conmigo.
    - **Doronbol:** ¡Purrrrrrr!
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Doronbol:** ¡Felices senderos! Ronroneo.

### Using a macaw pouch on Doronbol


#### Antes de darle a Doronbol una bolsa de guacamaya


##### Sin un amuleto de lengua de gato

- (removes=macaw pouch)
- **Doronbol:** Miau. ¡Miaow miaow miaow meeeeooow!

##### Con un amuleto de lengua de gato

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=macaw pouch)
    - **Doronbol:** Muchas gracias; ¡Qué delicia de merienda! Eres muy considerado.
    - **Player:** ¡Oye, espera! No te traje una guacamaya por eso.
    - **Doronbol:** Oh, está bien, lo que sea. Por suerte para ti, acabo de desayunar mucho. Supongo que puedo usar la guacamaya para darte información más detallada sobre la red contra incendios, al menos hasta que vuelva a tener hambre.
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Doronbol:** Vergüenza. Me hubiera venido bien un bocadillo.
    - **Player:** ¿Qué fue eso?
    - **Doronbol:** Oh, nada.

#### Después de darle a Doronbol una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; ella no necesita otra.

### Using logs on Doronbol

- (Condition: Si la baliza está apagada:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: Si la baliza está muriendo:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: Si la baliza no muere:)
  - (Condition: Si Doronbol no tiene cinco logs:)
    - (Condition: Si el mensaje de confirmación está habilitado:)
      - [Menu]: ¿Quieres darle cinco logs al fuego?
        - [Choice]: Sí.
          - (Condition: Si el player no tiene al menos cinco logs del mismo tipo:)
            - El bombero necesita cinco troncos del mismo tipo para mantener este fuego.
          - (Condition: Si el player tiene al menos cinco logs del mismo tipo:)
            - (removes=five logs)
            - Le das al fuego tierno 5 [type] logs.
        - [Choice]: No.
          - **Player:** Creo que, después de todo, me quedaré con mi logs.
        - [Choice]: Sí. Por favor, no vuelvas a pedirme confirmación.
          - (above|use-give-logs)
    - (Condition: Si el mensaje de confirmación está deshabilitado:)
      - (above|use-give-logs)
  - (Condition: Si Doronbol tiene cinco logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed


#### Si un amuleto de lengua de gato está equipado o no

- **Doronbol:** ¡Oye! ¡Aléjate de eso! Hasta que no hayas demostrado que eres un verdadero aliado de Varrock, ¡no podrás usar eso!
- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
