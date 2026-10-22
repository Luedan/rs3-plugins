# Robin

- **Original Wiki Page**: [Transcript:Robin](https://runescape.wiki/w/Transcript%3ARobin)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Ghosts Ahoy

- [Menu]: Elige una opción:
  - [Choice]: Acerca del sistema de tareas...
    - (abajo)
  - [Choice]: Habla de otra cosa.
    - (Condition: If the player doesn't have a bedsheet:)
      - **Player:** Es agradable ver otro rostro humano por aquí.
      - **Robin:** Déjame en paz, campesino, me estoy relajando.
      - **Player:** Bueno, ¡eso es genial!
      - **Robin:** ¿Sabes quién soy?
      - **Player:** Lo siento, no he tenido el privilegio.
      - **Robin:** Yo, campesino, soy Robin, Maestro Bowman. Soy muy famoso, ¿sabes?
      - **Player:** Oh, Robin, Maestro Bowman, ya veo.
      - **Robin:** ¿Has oído hablar de mí?
      - **Player:** No.
      - **Robin:** ¿Me harías un favor? Parece que se me acabó la ropa de cama. ¿Puedes ir corriendo donde el posadero y traerme una sábana limpia?
      - [Menu]: Selecciona una opción
        - [Choice]: Cualquier cosa para una persona famosa como tú.
          - **Player:** Cualquier cosa para una persona famosa como tú.
          - **Robin:** Ahora eso suena más parecido. Vete ahora, tráeme mi sábana.
        - [Choice]: Ve y consíguelo tú mismo.
          - **Player:** Ve y consíguelo tú mismo.
          - **Robin:** Oh, encantador. Simplemente no puedes conseguir el staff en estos días.
    - (Condition: If the player has a bedsheet:)
      - **Player:** Te he traído una sábana limpia, Robin.
      - (removes=bedsheet)
      - **Robin:** Bueno, ya era hora. Corre ahora, necesito algo de tiempo Robin.

### After Ghosts Ahoy

- [Menu]: Elige una opción:
  - [Choice]: Acerca del sistema de tareas...
    - ((If the player has completed the medium Morytania achievements and the rewards have not been claimed:))
      - **Player:** He completado todas las tareas medianas del conjunto Morytania.
      - **Robin:** Así que sí. Tengo unos leggings especiales reservados para ti.
      - [Robin te entrega un par de mallas y una lámpara.]
      - **Robin:** Ahí lo tienes. Aunque son un poco extraños. No estoy seguro de que me guste cómo me quedan; se sienten bastante viscosos, pero al menos puedes divertirte en la fragua de la ciudad. Ah, y alguien me regaló esta lámpara, pero en realidad no me sirve para nada.
      - **Player:** ¡Gracias!
      - **Robin:** Por cierto, Lyra dice que vendrá y cuidará tu huerto de hongos, y Razmire se ha puesto en contacto para pedir más planks y más dosis de su aceite de oliva. También... adquirí algo de esa baba, aventureros.
      - **Robin:** Parece que me gusta, y te cambiaré los huesos por harina de huesos, ya que hice un trato con alguien y parece que tengo bastante.
      - **Robin:** Además de eso, hay algunos cofres de almacenamiento en Mort'ton, cerca de las piras funerarias. A partir de ahora, podrás almacenar cualquier tipo de tronco de pira en ellos.
      - (continue)
    - (Condition: If the player has lost their Morytania legs 2:)
      - **Robin:** ¡Ah, el que usa calzas! ¿Cómo los estás encontrando?
      - **Player:** Los perdí.
      - **Robin:** ¡Oh, no!
      - **Robin:** No importa, tengo otro par. Aquí...
      - [Robin te entrega un par de leggings.]
      - (continue)
    - [Menu]: Elige una opción:
      - [Choice]: Háblame del Sistema de Logros.
        - **Robin:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
        - **Robin:**Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
        - **Robin:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
        - [Menu]: Elige una opción:
          - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
            - **Player:** Cuéntame sobre la recompensa establecida para esta área.
            - **Robin:** Para completar el conjunto Morytania, se te presentan unos leggings.
            - **Robin:** Estos leggings serán cada vez más útiles a medida que completes conjuntos de tareas de mayor dificultad.
            - **Robin:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
            - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
            - (previous2)
          - [Choice]: ¿Cómo reclamo estas recompensas?
            - **Player:** ¿Cómo reclamo las recompensas?
            - **Robin:** Debes completar todas las tareas dentro de un conjunto de dificultad particular y luego podrás reclamar tu recompensa.
            - **Robin:** Algunas de las tareas del conjunto Morytania son simples, algunas requieren cierto skill levels y otras requieren que se inicien o completen misiones.
            - **Robin:** Para reclamar las recompensas del conjunto Morytania, habla con Hiylik Myna justo al este de Paterdomus, con Strange Old Man en Barrows, con Old Man Ral en Meiyerditch o conmigo mismo.
            - (previous2)
          - [Choice]: Lo siento, me estaba yendo.
            - (end)
      - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
        - [Menu]: Elige una opción:
          - [Choice]: Morytania piernas 1
            - **Robin:** Morytania piernas 1? Sí, pero me temo que te costaría 1.500 coins.
            - [Menu]: ¿Comprar otro por 1.500 coins?
              - [Choice]: si
                - [Te entregan otras piernas Morytania 1.]
                - (receives=Morytania legs 1) (removes= 1,500 coins)
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: Morytania piernas 2
            - **Robin:** Morytania piernas 2? Sí, pero me temo que te costaría 2500 coins.
            - [Menu]: ¿Comprar otro por 2500 coins?
              - [Choice]: si
                - [Te entregan otras piernas Morytania 2.]
                - (receives=Morytania legs 2) (removes= 2,500 coins)
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: Morytania piernas 3
            - **Robin:** Morytania piernas 3? Sí, pero me temo que te costaría 7.500 coins.
            - [Menu]: ¿Comprar otro por 7.500 coins?
              - [Choice]: si
                - [Te entregan otras piernas Morytania 3.]
                - (receives=Morytania legs 3) (removes= 7,500 coins)
              - [Choice]: No
                - **Player:** No, gracias.
          - [Choice]: Morytania piernas 4
            - **Robin:** Morytania piernas 4? Sí, pero me temo que te costaría 15.000 coins.
            - [Menu]: ¿Comprar otro por 15.000 coins?
              - [Choice]: si
                - [Te entregan otras patas Morytania 4.]
                - (receives=Morytania legs 4) (removes= 15,000 coins)
              - [Choice]: No
                - **Player:** No, gracias.
      - [Choice]: Lo siento, me estaba yendo.
        - (end)
  - [Choice]: cond=If at least the medium Morytania tasks have been completed and the rewards claimed|Pide harina de huesos y baba.
    - **Player:** Dijiste algo sobre baba y harina de huesos cuando me diste las piernas de Morytania...
    - **Robin:** Oh, así lo hice. Me quedan [13/26/39] cubos de baba. Simplemente dame los huesos que deseas intercambiar.
  - [Choice]: cond=If at least the medium Morytania tasks have been completed and the rewards claimed|Pide información sobre harina de huesos y babas.
    - **Player:** Dijiste algo sobre baba y harina de huesos cuando me diste las piernas de Morytania. ¿Puedes contarme más?
    - **Robin:** Supongo que sí. Cambiaré los huesos que me traigas por harina de huesos molida y una cantidad equivalente de cubos de baba.
    - **Robin:** Recientemente también comencé a aceptar huesos notables. También se anotarán la harina de huesos y los cubos de baba que te daré a cambio.
    - **Player:** Entonces, si te traigo 2 huesos de wyvern y 3 huesos de dragón famosos, ¿me darás 2 lotes de harina de huesos de wyvern y 3 lotes de harina de huesos de dragón famoso?
    - **Robin:** Así es, y no olvides los cinco cubos de limo gratis. Puedes intercambiar hasta 26/13/39 huesos diariamente. ¡No olvides que necesitarás espacio libre para los cubos de baba!
  - [Choice]: Habla de otra cosa.
    - **Player:** Entonces, todavía aquí.
    - **Robin:** ¿Quieres otro juego de Runedraw?
    - **Player:** Tienes un problema grave con el juego, ¿sabes?

#### Usar huesos en Robin sin suficiente espacio en la bolsa

- **Robin:** ¡Vete, campesino, no tienes suficiente espacio libre en la bolsa para eso!
