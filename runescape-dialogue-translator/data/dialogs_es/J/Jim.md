# Jim

- **Original Wiki Page**: [Transcript:Jim](https://runescape.wiki/w/Transcript%3AJim)
- **Letter**: `J`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- (Condition: If the player is inside a clockwork suit:)
  - **Player:** ¡Hola Jim!
  - **Jim:** ¿Qué crees que estás haciendo? Vas a arruinar tu tapadera. Déjame sacarte ese traje.
  - [Menu]: ¿Quieres quitarte el traje de pingüino?
    - [Choice]: si
      - (Condition: Without at least one free backpack space:)
        - **Player:** No tengo suficiente espacio para guardar mi traje de pingüino en mi mochila. Primero tendré que hacer espacio.
      - (Action: el player sale del traje de relojería y vuelve a crecer hasta su tamaño normal.)
      - (receives=a clockwork suit)
      - El hechizo desaparece cuando te quitas el traje y vuelve a crecer hasta su tamaño normal.
    - [Choice]: No
      - **Player:** No, gracias.
- [Menu]: Selecciona una opción
  - [Choice]: Hora del esmoquin.
    - (Condition: With something equipped in the main- or off-hand slots:)
      - **Jim:** Necesitará tener las manos libres para operar el traje.
    - (Condition: With a cape equipped:)
      - **Jim:** No puedes usar una capa dentro del traje, podría quedar atrapada.
    - (Action: el player se encoge y se pone un traje de reloj.)
    - (removes=a clockwork suit (if one was present in the backpack))
    - Te encoges y te pones el traje de pingüino.
  - [Choice]: Preguntar por cotos de caza.
    - (Condition: First time talking after completing Hunt for Red Raktuber:)
      - **Jim:** Psst.
      - **Player:** Oh, ¿entonces puedes hablar ahora?
      - **Jim:** Siempre podría hablar. Pero no quería revelarme al enemigo.
      - **Player:** Bueno, ¿qué quieres?
      - **Jim:** He oído hablar de la captura de Larry. Lamento tu pérdida. Larry es muy valiente.
      - **Player:** Sí. Espero que esté bien. Dondequiera que esté.
      - **Jim:** Por eso deseo hablar contigo. Me han ordenado que le ayude a infiltrarse entre los pingüinos y a entrenar para futuras asignaciones.
      - **Player:** ¿Qué? ¿Qué futuras asignaciones?
      - **Jim:** Cuando vayas a rescatar a Larry, claro. No es una tarea que deba abordarse sin estar preparado.
      - **Player:** Entonces, ¿qué se supone que debo hacer exactamente?
      - **Jim:** Si deseas infiltrarte entre los pingüinos, se me ha concedido acceso al hechizo que te pone tu traje de pingüino.
      - **Jim:** Pero hay más que eso. Un nuevo iceberg ha descendido flotando desde el norte, trayendo consigo refuerzos para Penguin Outpost.
      - **Jim:** Para prepararte para los tiempos venideros, te proporcionamos algunos equipos para que practiques la caza y el rastreo de pingüinos.
      - **Jim:** A cambio de la experiencia que ganes, solo te pedimos que nos entregues a los agentes de KGP capturados.
      - **Jim:** Simplemente salta sobre los témpanos de hielo aquí.
      - **Player:** ¿Por qué agentes de KGP? ¿Qué harás con ellos?
      - **Jim:** Eso está clasificado. No necesitas saberlo.
      - [Menu]: ¿Qué quieres hacer?
        - [Choice]: Presiónelo más.
          - **Player:** ¿Eso no es suficiente? Estoy cansado de sólo recibir órdenes. ¿Qué harás con los pingüinos capturados?
          - **Jim:** Muy bien, si insistes en saberlo. Los interrogaremos y los mantendremos encarcelados. Pueden revelar información valiosa sobre la ubicación de Larry. Por eso solo queremos agentes del KGP, los otros pingüinos no saben nada de ello.
          - **Jim:** interés.
        - [Choice]: La ignorancia es felicidad.
          - **Player:** Bien, no quiero saberlo.
          - **Jim:** Es lo mejor.
    - (Condition: Thereafter:)
      - **Jim:** ¿Tiene algún agente de KGP capturado que le gustaría entregar?
      - [Menu]: Selecciona una opción
        - [Choice]: Sí.
          - **Player:** Sí, tengo algunos.
          - **Jim:** Muy bien. Déjame echar un vistazo.
          - (Condition: If the player doesn't have any KGP penguins with them:)
            - **Jim:** Parece que no tienes ninguno contigo.
          - (Condition: If the player does have KGP penguins with them:)
            - **Jim:** La PBJ te agradece tu ayuda.
        - [Choice]: No.
          - **Player:** No, no tengo ninguno para ti en este momento.

### Tickle

- **Jim:** {{RSChat|Hee hee hee}}
- Le haces cosquillas al oso polar.

### Tuxedo-Time

- (Condition: While not inside a clockwork suit:)
  - (above|tuxedo-time)
- (Condition: While inside a clockwork suit:)
  - (Condition: Without at least one free space in the backpack:)
    - No tienes suficiente espacio en tu inventario para quitarte el traje.
  - (above|exit-suit)
