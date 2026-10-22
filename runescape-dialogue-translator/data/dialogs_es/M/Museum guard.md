# Museum guard

- **Original Wiki Page**: [Transcript:Museum guard](https://runescape.wiki/w/Transcript%3AMuseum%20guard)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Attempting to purchase the completionist cape without enough money or space in backpack}}

### At the Varrock Museum


#### En la planta baja, en la entrada al área de limpieza arqueológica

- **Guardia:** ¡Bienvenido! ¿Te gustaría acceder al área de limpieza arqueológica del Sitio de Excavación?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Sí, entraré!
    - (Action: El guardia le hace un gesto a el player y el player ingresa al área de limpieza.)
  - [Choice]: No gracias, echaré un vistazo por aquí.
    - **Player:** No, gracias, echaré un vistazo por aquí.

#### En la entrada trasera del museo.

- **Museum guard:** Hola. ¿Vienes a ver el nuevo museo?
- **Player:** Sí, ¿cómo entro?
- **Museum guard:** Bueno, la entrada principal está al frente. Simplemente dirígete hacia el oeste y luego ligeramente hacia el norte, ¡no te lo puedes perder!
- **Player:** ¿Qué pasa con estas puertas?
- **Museum guard:** Son principalmente para los trabajadores que traen hallazgos del sitio de excavación, pero puedes pasar si quieres.
- **Player:** Está bien, gracias.

#### Investigando la capa completista en el último piso


##### Primera vez

- **Museum guard:** ¡Oye! ¡Quita tus manos de eso! ¿No sabes que no debes tocar objetos en un museo?
- **Player:** Lo siento, sólo me preguntaba qué era.
- **Museum guard:** Una buena pregunta. Quizás sea una de las exhibiciones más misteriosas de este museo.
- **Museum guard:** Fue descubierto recientemente, pero nuestros curadores lo fecharon casi hasta donde podemos rastrear. Resulta que esta capa podría ser producto, o al menos estar relacionada con un mago de la Segunda Edad llamado Dahmaroc.
- **Player:** ¿Dahmaroc?
- **Museum guard:** De hecho, es posible que hayas aprendido sobre él abajo. Era un mago poderoso en la Segunda Edad. También estaba muy centrado en las habilidades, por lo que esta capa fue un hallazgo particular.
- **Player:** ¿Qué quieres decir con eso?
- **Museum guard:** Bueno, en general, sus habilidades mágicas se centraban fuera del combate; parece que esta capa está bajo el encantamiento más poderoso que jamás hayamos visto.
- **Player:** ¿Esta capa está encantada?
- **Museum guard:** Sí, y más de lo que podemos comprender. Repele físicamente a cualquiera que intente tocarlo. Tuvimos bastantes problemas para subirlo hasta aquí.
- **Player:** ¿Entonces nadie ha usado esta capa?
- **Museum guard:** ¡Nadie puede! ¡Es como si tuviera mente propia y juzgara a aquellos que lo intentan como indignos!
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Puedo intentarlo?
    - **Player:** ¿Puedo intentarlo?
    - (Condition: Only on the first time asking:)
      - **Museum guard:** Dije que no lo toques... pero, si te acercas lo suficiente, estoy seguro de que verás los efectos del encantamiento...
      - **Museum guard:** ¡Buena suerte!
      - (continue)
    - (Condition: Subsequent times asking:)
      - **Museum guard:** ¡Por supuesto!
      - (continue)
    - (Condition: Without having completed all completionist requirements:)
      - (Action: el player hace el gesto Think, se convierte en un animal aleatorio, vuelve a ser humano y es empujado lejos de la misteriosa capa.)
      - **Museum guard:** ¡Parece que Dahmaroc tenía sentido del humor!
      - **Museum guard:** Lo siento, no parece que seas digno de esta capa. Al menos no todavía...
    - (Condition: Having completed all completionist requirements:)
      - (Action: el player toca la capa y realiza una animación.)
      - **Museum guard:** ¡Nunca había visto una reacción así! Creo que la capa está identificando a su verdadero dueño.
      - **Player:** ¿Quieres decir que puedo tenerlo?
      - **Museum guard:** Bueno, sí, pero... No puedo dejar que te lleves la exhibición. Puede que seas el verdadero propietario, pero es uno de los objetos más preciados que tenemos aquí.
      - **Museum guard:** Supongo que si el museo fuera compensado, tal vez podría dejar que te lo lleves... ¿Qué te parece 5.000.000 coins?
      - [Menu]: ¿Qué te gustaría decir?
        - [Choice]: Eso suena justo.
          - **Player:** Eso suena justo.
          - (Condition: Without enough money:)
            - {{Tmissing}}
          - (Condition: With enough money but without space in backpack:)
            - {{Tmissing}}
          - (Condition: With enough money and with space in backpack:)
            - (removes=5,000,000 coins) (receives=hooded completionist cape)
            - sombra=si
            - **Museum guard:** Puedes volver a comprarme una copia cuando quieras. ¡Además la capucha y la capa son desmontables!
            - [¡También has desbloqueado las anulaciones de capa y capucha Complecionista en tu guardarropa!]
        - [Choice]: ¡Parece una broma!
          - **Player:** ¡Parece una broma!
          - **Museum guard:** Que así sea; la capa se queda donde está.
  - [Choice]: Que interesante.
    - **Player:** Qué interesante.
    - **Museum guard:** Gracias por hacerme perder el tiempo.

##### Tiempos posteriores

- **Museum guard:** ¡Oye! ¡Quita tus manos de eso! ¿No sabes que no debes tocar objetos en un museo?
- **Museum guard:** Lo siento, no quise ofender, ¿qué te gustaría saber?
- [Menu]: ¿Qué te gustaría preguntar?
  - [Choice]: ¿Qué es esta capa?
    - (arriba)
  - [Choice]: ¿Puedo probar y usarlo?
    - (arriba)

##### Investigando la tribuna vacía, habiendo reclamado la capa completista


##### Sin haber completado todos los logros finalistas recortados

- **Museum guard:** Vaya, Player. ¡Eres el dueño de esta capa legendaria! ¡Es un honor verte!
- [Menu]: ¿Qué te gustaría preguntar?
  - [Choice]: ¿Qué es esta capa?
    - (arriba)
  - [Choice]: ¿Puedo probar y usarlo?
    - **Museum guard:** Parece que la versión recortada de esta capa no te responde.
    - Debes completar los logros de la capa de completista recortada para desbloquear la anulación cosmética de esta capa y obtener la capa.
    - **Museum guard:** Sin embargo, ¿puedo venderte una copia idéntica de la capa completista si quieres?
    - [Menu]: ¿Te gustaría comprar otra capa completista?
      - [Choice]: si
        - **Museum guard:**Te costará 5.000.000 coins por otro, ya que no es barato replicarlos.
        - [Menu]: ¿Pagar 5 000 000 coins por una capa completista (con capucha)?
          - [Choice]: si
            - (Condition: Without enough money:)
              - {{Tmissing}}
            - (Condition: With enough money but without space in backpack:)
              - {{Tmissing}}
            - (Condition: With enough money and with space in backpack:)
              - (removes=5,000,000 coins) (receives=hooded completionist cape)
              - **Museum guard:** Gracias, la capucha es desmontable si prefieres que estén separadas. ¡Espero que lo disfrutes!
          - [Choice]: No
            - {{Transcript missing}}
      - [Choice]: No
        - {{Transcript missing}}

##### Habiendo completado todos los logros finalistas recortados

- **Museum guard:** Vaya, ¿el dueño de la capa legendaria? Qué bueno verte de regreso.
- **Player:** Gracias.
- **Museum guard:** ¿Hay algo en lo que pueda ayudarte ahora, Player?
- **Player:** No lo sé, ¿verdad?
- **Museum guard:** Veo que has superado lo requerido para obtener esa capa que te di, y parece que Dahmaroc previó esto...
- **Museum guard:** ¡Vaya, funcionó! ¡Disfrutar!
- sombra=si

### At the path leading to the Digsite

- **Museum guard:** ¡Hola! Lo siento, no puedo parar de hablar. Estoy supervisando a los trabajadores que usan este camino. Les gusta tomar descansos, ¿sabes?

### At the Archaeology Campus


#### Antes de restaurar el artefacto en el tutorial de Archaeology

- **Museum guard:** Deberías hablar con Acting Guildmaster Reiniger. Sin embargo, tan pronto como hayas restaurado un artefacto, estaré encantado de hablar más contigo.

#### Después de restaurar el artefacto en el tutorial Archaeology

- **Museum guard:** Bien, entonces, ¡el Museo Varrock estará encantado de aceptar todos y cada uno de los artefactos restaurados que obtengas! Simplemente coloque los que desee intercambiar para usarlos en un contenedor de donaciones.
- **Museum guard:** No hay límite para lo que te quitaremos de las manos. ¡Te daremos cronos por cada donación!
- **Museum guard:** Claro, completar las colecciones de coleccionistas privados quizás podría ser más lucrativo, pero ellos solo quieren artefactos específicos en un momento dado, dependiendo de lo que ya hayas contribuido a sus colecciones.
- **Museum guard:** ¡El Museo Varrock siempre está abierto al público!

#### Después de completar el tutorial de Archaeology

- **Museum guard** Hola. ¿Quieres hacer una donación al museo?
- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Player** ¿Quién eres?
    - **Museum guard** Soy un museum guard y trabajo para el Museo Varrock.
    - (initial)
  - [Choice]: ¿Qué estás haciendo aquí?
    - **Player** ¿Qué haces aquí?
    - **Museum guard** Los arqueólogos vienen aquí para restaurar artefactos dañados encontrados en todo el mundo.
    - **Museum guard** El Museo Varrock está interesado en estos artefactos para asegurarse de que se conserven por el resto del tiempo.
    - **Museum guard** Superviso a los trabajadores que transfieren los artefactos restaurados al museo.
    - (initial)
  - [Choice]: ¿Para qué sirve el contenedor de donaciones?
    - **Player** ¿Para qué sirve el contenedor de donaciones?
    - **Museum guard** Puede colocar sus artefactos restaurados en el contenedor de donaciones aquí para que nuestros trabajadores los transporten de manera segura al museo.
    - **Museum guard** A cambio de tu generosa donación, recibirás algunas cronotas. Es una pequeña moneda nueva que ha creado el Gremio de Arqueólogos.
    - (initial)
  - [Choice]: ¿Qué tan gratificante es donar al museo?
    - **Museum Guard** Bien, entonces, ¡el Museo Varrock estará encantado de aceptar todos y cada uno de los artefactos restaurados que obtengas! Simplemente coloque cualquier cosa que desee intercambiar con nosotros en un contenedor de donaciones.
    - **Museum Guard** No hay límite para lo que te quitaremos de las manos. ¡Te daremos cronos por cada donación! Sin embargo, solo el 40% del valor de cronota base de cada artefacto; obtenemos muchos duplicados.
    - **Museum Guard** Claro, completar las colecciones de coleccionistas privados quizás podría ser más lucrativo, pero ellos solo quieren artefactos específicos en un momento dado, dependiendo de lo que ya hayas contribuido a sus colecciones.
    - **Museum Guard** ¡El Museo Varrock siempre está abierto al público!
    - (initial)
