# Horacio

- **Original Wiki Page**: [Transcript:Horacio](https://runescape.wiki/w/Transcript%3AHoracio)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Pay


#### Antes de Volver a mis Raíces

- (Action: No pasa nada.)

#### Después de Volver a mis raíces


##### Con el parche de vid de jade vacío

- **Horacio:** Err... ¡todavía no has plantado una enredadera!

##### Con la vid de jade creciendo

- **Horacio:** Necesitaré 10 lúpulos wildblood para poder preparar una cerveza sabrosa.
- (Condition: If the player does not have enough wildblood hops in backpack:)
  - **Player:** No tengo suficientes. Supongo que volveré más tarde.
- (Condition: If the player has ten wildblood hops in backpack:)
  - [Menu]: ¿Pagar 10 saltos de sangre salvaje?
    - [Choice]: Está bien, es un trato.
      - **Player:** Está bien, es un trato.
      - (removes=ten wildblood hops)
      - **Horacio:** Eso funcionará muy bien. No temas, Horacio está aquí, tu vid crecerá segura en mis manos.
    - [Choice]: No, eso es demasiado.
      - **Player:** No, eso es demasiado.
      - **Horacio:** Bueno, no voy a arriesgar mi vida gratis.

##### Habiendo pagado ya por la protección

- **Horacio:** ¡Ya estoy cuidando tu vid! ¡Tienes mazorcas como el maíz!

##### Con la vid de jade completamente desarrollada

- **Horacio:** ¡La vid ya está completamente desarrollada! ¡No sé qué quieres que haga con él!

##### Con una enredadera de jade salvaje

- **Horacio:** ¡No estoy protegiendo esa cosa vil! ¡Debes estar enojado!

### Talk-to


#### Antes del tótem tribal

- **Horacio:** Hace un buen día para estar en el jardín, ¿no?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, es muy bonito.
    - **Player:** Sí, es muy bonito.
    - **Horacio:** ¡Días como estos me alegran de estar vivo!
  - [Choice]: Entonces... ¿quién eres tú?
    - **Player:** Entonces... ¿quién eres tú?
    - **Horacio:** Mi nombre es Horacio Dobson. Soy el jardinero de Lord Handelmort. Echa un vistazo a este hermoso jardín, todo esto es obra mía.

#### Después del tótem tribal

- **Horacio:** Hace un buen día para estar en el jardín, ¿no?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, es muy bonito.
    - **Player:** Sí, es muy bonito.
    - **Horacio:** ¡Días como estos me alegran de estar vivo!
  - [Choice]: Entonces... ¿quién eres tú?
    - **Player:** Entonces... ¿quién eres tú?
    - **Horacio:** Mi nombre es Horacio Dobson. Soy el jardinero de Lord Handelmort. Echa un vistazo a este hermoso jardín, todo esto es obra mía.
    - [Menu]: Selecciona una opción
      - [Choice]: Entonces... ¿también haces jardinería en la parte de atrás?
        - **Player:** Entonces... ¿tienes jardín en la parte de atrás también?
        - **Horacio:** ¡Eso sí!
        - **Player:** Entonces, ¿toda la seguridad de la casa no se interpone en tu camino?
        - **Horacio:** Ah, ya estoy acostumbrado a todo eso. Tengo mis llaves, los perros guardianes me conocen y sé la combinación de la cerradura de la puerta. Es bastante fácil, es su segundo nombre.
        - **Player:** ¿De quién es el segundo nombre?
        - **Horacio:** Hum. Probablemente no debería haber dicho eso. Olvídate de que lo mencioné.
      - [Choice]: ¿Necesitas ayuda?
        - **Player:** ¿Necesitas ayuda?
        - (Condition: If the player does not meet the requirements for Back to my Roots:)
          - **Horacio:** En realidad, ahora que lo mencionas, sí... pero todavía no tienes la experiencia suficiente para ayudarme.
          - Consulta tu diario de misiones para conocer los requisitos para iniciar la misión Regreso a mis raíces.
        - (Condition: If the player meets the requirements for Back to my Roots:)
          - **Horacio:** En realidad, ahora que lo mencionas, sí... Voy a mejorar el jardín que rodea la casa. ¿Estarías dispuesto a ayudarme?
          - (ver|Regreso a mis raíces)
        - (Condition: If the player has completed Back to my Roots:)
          - **Horacio:** Has hecho más que suficiente para ayudar. ¡Espero que estés disfrutando de tu parcela de vid!
  - [Choice]: cond=After Back to my Roots|Habla de la vid.
    - (Condition: If the player does not have a jade vine seed:)
      - ((Horacio says one of the following at random:))
      - ((Dialogue 1:))
        - **Horacio:** Los jardineros que plantan árboles con hojas según sus propias habilidades, pero los jardineros que plantan enredaderas son simplemente divinos. Entonces, ¿te gustaría recuperar tu semilla perdida?
        - (continue|lost)
      - ((Dialogue 2:))
        - **Horacio:** A pesar de haber hecho un completo abono con tu primer intento de cultivar la vid, salvaste mi vida... ¿Te gustaría otra semilla para reemplazar la perdida?
        - (continue|lost)
      - ((Dialogue 3:))
        - **Horacio:** Me alegra ver que todavía estás vivo y creciendo. ¿Le gustaría otra semilla para reemplazar la perdida?
        - (continue|lost)
      - ((Dialogue 4:))
        - **Horacio:** Veo que no llegaste a la raíz del problema antes de perder tu vid. ¿Quieres otra semilla?
        - (continue|lost)
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, por favor.
          - **Player:** Sí, por favor.
          - (receives=jade vine seed)
          - **Horacio:** Aquí tienes entonces.
        - [Choice]: Por el momento no, gracias.
          - (end)
    - (Condition: If the player has a jade vine seed but has not planted it:)
      - **Horacio:** Espero que te estés divirtiendo cultivando tu vid, la mía se ve particularmente bien.
      - **Player:** ¿Cómo estás?
      - **Horacio:** Oh, soy vid. Yo digo que es un buen día para estar en el jardín, ¿no?
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, es muy bonito.
          - (arriba)
        - [Choice]: Entonces... ¿quién eres tú?
          - (arriba)
    - (Condition: If the player has a jade vine seed and has planted it:)
      - **Horacio:** Espero que te estés divirtiendo cultivando tu vid, la mía se ve particularmente bien.{{anchor|having-fun}}
      - (Condition: If there is no wild jade vine:)
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Podrías cuidar mi vid por mí?
            - (Condition: If the jade vine is growing:)
              - **Horacio:** Sí, por supuesto, pero te costará. Mi tomillo es valioso.
              - **Player:** ¿Cuánto?
              - **Horacio:** Necesitaré 10 lúpulos wildblood para poder preparar una cerveza sabrosa.
              - (Condition: If the player does not have ten wildblood hops in backpack:)
                - **Player:** No tengo suficientes. Supongo que volveré más tarde.
              - (Condition: If the player has ten wildblood hops in backpack:)
                - [Menu]: ¿Pagar 10 saltos de sangre salvaje?
                  - [Choice]: Está bien, es un trato.
                    - **Player:** Está bien, es un trato.
                    - (removes=ten wildblood hops)
                    - **Horacio:** Eso funcionará muy bien. No temas, Horacio está aquí, tu vid crecerá segura en mis manos.
                  - [Choice]: No, eso es demasiado.
                    - **Player:** No, eso es demasiado.
                    - **Horacio:** Bueno, no voy a arriesgar mi vida gratis.
            - (Condition: If the player has already paid for protection:)
              - **Horacio:** ¡Ya estoy cuidando tu vid! ¡Tienes mazorcas como el maíz!
            - (Condition: If the jade vine is fully grown:)
              - **Horacio:** ¡La vid ya está completamente desarrollada! ¡No sé qué quieres que haga con él!
          - [Choice]: ¿Podrías limpiar mi parcela de enredaderas, por favor?
            - **Horacio:** Tienes una hermosa enredadera joven creciendo allí. Probablemente sea mejor no molestarlo. Espera hasta que haya crecido.
            - **Player:** Está bien. Esperaré entonces.
          - [Choice]: ¿Podrías contarme más sobre la vid de jade?
            - **Horacio:** Por supuesto. ¿Qué te gustaría saber?
            - [Menu]: Selecciona una opción
              - [Choice]: Háblame de la propagación.
                - **Player:** Cuéntame sobre la propagación.
                - **Horacio:** Estas plantas tienen género, el mismo que tú o yo, y necesitan una de cada género para propagar la especie por semilla, razón por la cual no obtuvimos semillas hasta que cultivaste con éxito otra enredadera en mi parcela. Suelen ser polinizados por murciélagos nocturnos que pueden volar grandes distancias.
                - **Player:** Entonces, ¿el de Karamja nunca habría dado semilla hasta que tuviéramos otro de diferente género creciendo?
                - **Horacio:** Tal vez, tal vez no, pero nunca habría crecido, incluso si hubiera dado semilla. Necesita el otro género para ser fértil.
                - **Player:** Interesante, gracias.
              - [Choice]: ¿Puedes contarme algo sobre su historia?
                - **Player:** ¿Puedes contarme algo sobre su historia?
                - **Horacio:** Los Slayer Masters alguna vez pensaron que la enredadera de jade, o 'strongylodon macrobotrys', estaba cazada hasta la extinción porque pensaban que era lo mejor para entrenar sin necesidad de una tarea. Como hemos descubierto, hay
                - **Horacio:** parece haber sido uno que se escapó de la red y creció por sí solo, sin ser molestado en Karamja. Puede ser un oponente formidable cuando está completamente salvaje. ¡No creo que me hubiera gustado matarlo por diversión!
                - **Player:** No fue tan difícil.
          - [Choice]: ¿Puedes venderme algo?
            - **Player:** ¿Puedes venderme algo?
            - **Horacio:** Eso depende de lo que tenga para vender. ¿Qué es lo que estás buscando?
            - (opens=Farmer's Supplies)
      - (Condition: If there is a wild jade vine:)
        - **Player:** En realidad, el mío se ha vuelto a salir un poco de control.
        - **Horacio:** ¡ARG! ¡Otra vez no!
        - **Horacio:** ¿Quieres que lo elimine por ti?
        - [Menu]: Selecciona una opción
          - [Choice]: ¡Sí, por favor!
            - **Horacio:** Está bien, pero no lo hago en vano. Cinco cocos y cinco sandías para hacer eso.
            - (Condition: Without five watermelons and five coconuts in backpack:)
              - **Player:** No tengo eso. Supongo que volveré o me ocuparé de ello yo solo.
            - (Condition: With five watermelons and five coconuts in backpack:)
              - [Menu]: Selecciona una opción
                - [Choice]: Está bien, es un trato.
                  - **Player:** Está bien, es un trato.
                  - (removes=five watermelons and five coconuts)
                  - (Action: La enredadera de jade salvaje desaparece, dejando un espacio vacío detrás.)
                  - **Horacio:** Listo, todo hecho para ti.
                  - **Player:** ¡Gracias!
                - [Choice]: No, eso es demasiado.
                  - **Player:** No, eso es demasiado.
                  - **Horacio:** Bueno, no voy a arriesgar mi vida gratis.
          - [Choice]: No, gracias. Puedo manejarlo.
            - (end)

### Retrieve seed


#### Antes de Volver a mis Raíces

- (Action: No pasa nada.)

#### Si el player ya tiene la semilla plantada

- **Horacio:** ¿No tengo semillas para regalarte?
- **Horacio:** Espero que te estés divirtiendo cultivando tu vid, la mía se ve particularmente bien.
- (continuea|having-fun)

#### Si el player ya tiene la semilla pero no está plantada

- **Horacio:** Ya te tengo una semilla. ¿Quizás lo has guardado en algún lugar?

#### Si el player no tiene semilla

- **Horacio:** Aquí tienes.
- (receives=jade vine seed)
