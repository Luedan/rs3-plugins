# Purple Pewter Director

- **Original Wiki Page**: [Transcript:Purple Pewter Director](https://runescape.wiki/w/Transcript%3APurple%20Pewter%20Director)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

- ''Nota: Antes y durante el Enano Gigante, todas las empresas comienzan con una reputación media. Después de The Giant Dwarf, la empresa elegida por el player tendrá permanentemente la mayor reputación, mientras que todas las demás empresas tendrán una reputación baja.

### Low, medium or high reputation

- {{trandom}}
  - (Condition: Dialogue 1:)
    - **Purple Pewter Director:** Mi secretaria está sentada justo ahí, gracias.
  - (Condition: Dialogue 2:)
    - **Purple Pewter Director:** Hoy no es un buen día, ¿puedes volver mañana?
  - (Condition: Dialogue 3:)
    - **Purple Pewter Director:** Estoy ocupado, por favor vete.
  - (Condition: Dialogue 4:)
    - **Purple Pewter Director:** Si buscas el mercado, está abajo.
  - (Condition: Dialogue 5:)
    - **Purple Pewter Director:** No puedo ayudarte, ve a ver a mi secretaria.
  - (Condition: Dialogue 6:)
    - **Purple Pewter Director:** Habla con mi secretaria. No tengo tiempo para tratar contigo.
  - (Condition: Dialogue 7:)
    - **Purple Pewter Director:** Mi secretaria atenderá cualquier consulta que tengas sobre Purple Pewter.
  - (Condition: Dialogue 8:)
    - **Purple Pewter Director:** ¿Te importa? Estás bloqueando mi vista.
  - (continue)
- (Condition: If the player has low reputation with the Purple Pewter:)
  - **Player:** Pero...
  - {{trandom}}
    - (Condition: Dialogue 1:)
      - **Purple Pewter Director:** ¡Dije que te fueras!
    - (Condition: Dialogue 2:)
      - **Purple Pewter Director:** ¡Te dije que te fueras, humano!

### Higher reputation

- {{trandom}}
  - (Condition: Dialogue 1:)
    - **Purple Pewter Director:** Eres un miembro excepcional de Purple Pewter.
  - (Condition: Dialogue 2:)
    - **Purple Pewter Director:** Pasa, Player, mi secretaria ha estado diciendo cosas buenas de ti.
  - (Condition: Dialogue 3:)
    - **Purple Pewter Director:** ¿Has venido a servir el Purple Pewter otra vez, Player?
  - (Condition: Dialogue 4:)
    - **Purple Pewter Director:** ¡Estás demostrando que eres un miembro leal de Purple Pewter, Player!
  - (Condition: Dialogue 5:)
    - **Purple Pewter Director:** ¡Player! ¡He estado escuchando cosas maravillosas sobre ti!
  - (Condition: Dialogue 6:)
    - **Purple Pewter Director:** Ven, Player, déjanos conversar un rato sobre tu futuro con nosotros.
  - (Condition: Dialogue 7:)
    - **Purple Pewter Director:** ¿Qué ha venido a pedirnos, honorable Player?
  - (continue)
- [Menu]: Elige una opción: {{anchor|cxz}}
  - [Choice]: ¡Es un honor conocerte!
    - **Player:** ¡Es un honor conocerte!
    - {{trandom}}
      - (Condition: Dialogue 1:)
        - **Purple Pewter Director:** Bien, bien, ¿ahora de qué querías hablar?
      - (Condition: Dialogue 2:)
        - **Purple Pewter Director:** ¿Y qué era lo que querías de mí, Player?
      - (Condition: Dialogue 3:)
        - **Purple Pewter Director:** Ciertamente debe serlo.
      - (Condition: Dialogue 4:)
        - **Purple Pewter Director:** Sí, bueno, no te excedas ahora, ¿quieres?
      - (Condition: Dialogue 5:)
        - **Purple Pewter Director:** Eres una de nuestras mejores personas, Player, naturalmente tengo tiempo para ti.
      - (Condition: Dialogue 6:)
        - **Purple Pewter Director:** ¡Me lo imagino!
      - (Condition: Dialogue 7:)
        - **Purple Pewter Director:** No todos los días te encuentras con alguien tan importante como yo, estoy seguro.
  - [Choice]: ¿Tienes más tareas para mí?
    - **Player:{{anchor|www}}** ¿Tienes más tareas para mí?
    - (Condition: Before The Giant Dwarf, the Director replies with one of the following at random:)
      - (Condition: Dialogue 1:)
        - **Purple Pewter Director:** En verdad, creo que sí.
      - (Condition: Dialogue 2:)
        - **Purple Pewter Director:** Pues, claro.
      - (Condition: Dialogue 3:)
        - **Purple Pewter Director:** Eso creo, sí.
      - (Condition: Dialogue 4:)
        - **Purple Pewter Director:** Un momento, por favor, déjame comprobarlo.
        - **Purple Pewter Director:** Sí, tengo algo apropiado para ti aquí.
    - **Purple Pewter Director:{{anchor|eee}}** Necesitamos barras [número] de [metal] en los próximos minutos [número].
    - [Menu]: Selecciona una opción
      - [Choice]: Yo lo tomaré.
        - **Player:** Lo aceptaré.
        - {{trandom}}
          - (Condition: Dialogue 1:)
            - **Purple Pewter Director:** Excelente, ¡hazlo ahora!
          - (Condition: Dialogue 2:)
            - **Purple Pewter Director:** ¡Feliz de escuchar eso!
          - (Condition: Dialogue 3:)
            - **Purple Pewter Director:** ¡Actitud admirable, Player!
          - (Condition: Dialogue 4:)
            - **Purple Pewter Director:** The Purple Pewter aprecia lo que estás haciendo, Player.
          - (Condition: Dialogue 5:)
            - **Purple Pewter Director:** Entonces vuelve rápido, Player, ¡cuento contigo!
      - [Choice]: No, gracias.
        - **Player:** No, gracias.
        - {{trandom}}
          - (Condition: Dialogue 1:)
            - **Purple Pewter Director:** Lamento escuchar eso, Player, la compañía realmente necesitaba esas barras.
          - (Condition: Dialogue 2:)
            - **Purple Pewter Director:** No entiendo, ¿pensé que eras un seguidor leal?
          - (Condition: Dialogue 3:)
            - **Purple Pewter Director:** Entonces, ¿por qué preguntaste, Player?
          - (Condition: Dialogue 4:)
            - **Purple Pewter Director:** Eso es algo inusual para ti, Player.
          - (Condition: Dialogue 5:)
            - **Purple Pewter Director:** ¿Ah? Pensé que te gustaba hacer este tipo de trabajo.
    - (Condition: If the player is already on a task:)
      - **Purple Pewter Director:** ¿Ya has completado tu tarea actual? ¿Me conseguiste mis barras [número] de [metal]?
      - **Player:** Todavía estoy trabajando en ello, lo siento.
      - **Purple Pewter Director:** Entonces date prisa, no tengo tiempo para todo esto.
      - (initial)
    - (Condition: After The Giant Dwarf, the Director replies with one of the following at random:)
      - (Condition: Dialogue 1:)
        - **Purple Pewter Director:** Ya que te gustan tanto los [chosen company during The Giant Dwarf], ¿por qué no les preguntas?
      - (Condition: Dialogue 2:)
        - **Purple Pewter Director:** Estás aliado con [chosen company], ¿no? Tu pregunta es inapropiada.
      - (Condition: Dialogue 3:)
        - **Purple Pewter Director:** ¡Pide trabajo al [chosen company]!
      - (Condition: Dialogue 4:)
        - **Purple Pewter Director:** ¿No eres asociado de [chosen company]? ¿Por qué me preguntas?
    - (Condition: If the player is already on a task from a different company:)
      - **Purple Pewter Director:** Creo que tienes asuntos pendientes con [other Company] para terminar primero.
    - (initial)
  - [Choice]: *(Sólo después de The Giant Dwarf:)* ¡Los guardias del piso de comercio siguen atacándome!
    - **Player:** Los guardias del piso comercial siguen atacándome.
    - **Purple Pewter Director:** Sin duda pensaron que les estabas robando a los comerciantes. Debería hablar con el director de su propia empresa.
  - [Choice]: Gracias por tu tiempo.
    - **Player:** Gracias por tu tiempo.
    - **Purple Pewter Director:** No lo menciones.

#### Entregar una tarea

- **Player:** ¡He completado tu tarea! ¡Aquí están tus barras!
- (removes=bars) (receives=coins)
- {{trandom}}
  - (Condition: Dialogue 1:)
    - **Purple Pewter Director:** The Purple Pewter siempre puede confiar en ti, Player.
  - (Condition: Dialogue 2:)
    - **Purple Pewter Director:** ¡Haré que mi secretaria envíe esto al parqué de inmediato!
- (continuea|cxz)

### Highest reputation

- {{trandom}}
  - (Condition: Dialogue 1:)
    - **Purple Pewter Director:** Bienvenido de nuevo, Player, ¡es un placer verte de nuevo!
  - (Condition: Dialogue 2:)
    - **Purple Pewter Director:** ¿Y cómo puede servirte el Purple Pewter hoy, Player?
  - (Condition: Dialogue 3:)
    - **Purple Pewter Director:** ¡Entra, entra amigo mío!
  - (Condition: Dialogue 4:)
    - **Purple Pewter Director:** ¡Purple Pewter se complace en verte de nuevo!
  - (Condition: Dialogue 5:)
    - **Purple Pewter Director:** Hola de nuevo, Player, ¡pasa!
- [Menu]: Elige una opción:
  - [Choice]: ¡Es un honor conocerte!
    - **Player:{{anchor|qwe}}** ¡Es un honor conocerte!
    - {{trandom}}
      - (Condition: Dialogue 1:)
        - **Purple Pewter Director:** ¡Encantado de verte de nuevo también!
      - (Condition: Dialogue 2:)
        - **Purple Pewter Director:** ¡Y es un honor para mí dedicar algo de tiempo a ti, Player!
      - (Condition: Dialogue 3:)
        - **Purple Pewter Director:** ¡Ni lo menciones, Player!
      - (Condition: Dialogue 4:)
        - **Purple Pewter Director:** ¡Es casi tan honor como volver a encontrarte, Player!
      - (Condition: Dialogue 5:)
        - **Purple Pewter Director:** ¡Siempre estoy feliz de tener tiempo para ti, Player!
    - (initial)
  - [Choice]: ¿Tienes más tareas para mí?
    - (above|www)
  - [Choice]: Gracias por tu tiempo.
    - **Player:** Gracias por tu tiempo.
    - {{trandom}}
    - (Condition: Dialogue 1:)
      - **Purple Pewter Director:** ¡Fue un tiempo bien empleado!
    - (Condition: Dialogue 2:)
      - **Purple Pewter Director:** Para nada, ¡fue un placer hablar contigo una vez más!

#### Entregar una tarea

- **Player:** ¡He completado tu tarea! ¡Aquí están tus barras!
- (removes=bars) (receives=coins)
- {{trandom}}
  - (Condition: Dialogue 1:)
    - **Purple Pewter Director:** ¡Alabado sea Guthix!
  - (Condition: Dialogue 2:)
    - **Purple Pewter Director:** ¡Estoy muy satisfecho con tu trabajo, Player!
  - (Condition: Dialogue 3:)
    - **Purple Pewter Director:** ¡Eres un verdadero activo para Purple Pewter!
  - (Condition: Dialogue 4:)
    - **Purple Pewter Director:** ¡Nunca dejas de satisfacer, Player!
  - (Condition: Dialogue 5:)
    - **Purple Pewter Director:** ¡Haré que mi secretaria envíe esto al parqué de inmediato!
- (initial)

### As the player's chosen director after The Giant Dwarf

- **Purple Pewter Director:** ¡Hola Player! ¿Has visto la estatua? ¡Se ve hermoso! ¡Purple Pewter está en deuda contigo por tu dedicación para hacer que esto sucediera!
- [Menu]: Elige una opción: {{anchor|xzx}}
  - [Choice]: ¡Es un honor conocerte!
    - (above|qwe)
  - [Choice]: ¿Tienes más tareas para mí?
    - **Player:** ¿Tienes más tareas para mí?
    - {{trandom}}
      - (Condition: Dialogue 1:)
        - **Purple Pewter Director:** ¿Más trabajo? Vaya, ciertamente eres un activo para la empresa.
      - (Condition: Dialogue 2:)
        - **Purple Pewter Director:** De verdad, Player, ya no necesitas hacer esto.
        - **Player:** ¡Pero quiero hacerlo!
        - **Purple Pewter Director:** Bueno, si insistes...
      - (Condition: Dialogue 3:)
        - **Purple Pewter Director:** Ya no necesitas hacer esto, ¿sabes?
      - (Condition: Dialogue 4:)
        - **Purple Pewter Director:** Ah, si tan solo todos los miembros de Purple Pewter tuvieran tanta dedicación como tú.
        - (continuea|eee)
    - (Condition: If the player is already on a task from a different company:)
      - **Purple Pewter Director:** Creo que tienes asuntos pendientes con [other Company] para terminar primero.
      - (initial)
  - [Choice]: ¡Los guardias del piso de comercio siguen atacándome!
    - **Player:** Los guardias del piso comercial siguen atacándome.
    - **Purple Pewter Director:** Quizás pueda quitarte los guardias de encima si realizas una tarea para la empresa.
    - [Menu]: Selecciona una opción
      - [Choice]: Muy bien.
        - **Player:** Muy bien.
        - (continuea|eee)
      - [Choice]: Olvídalo.
        - **Player:** Olvídalo.
  - [Choice]: Gracias por tu tiempo.
    - **Player:** Gracias por tu tiempo.
    - **Purple Pewter Director:** ¡Hasta luego, amigo! ¡Estoy seguro de que Purple Pewter volverá a desempeñar un papel en tu futuro en algún momento!

#### Entregar una tarea

- **Player:** ¡He completado tu tarea! ¡Aquí están tus barras!
- (removes=bars) (receives=coins)
- {{trandom}}
  - (Condition: Dialogue 1:)
    - **Purple Pewter Director:** ¡Alabado sea Guthix!
  - (Condition: Dialogue 2:)
    - **Purple Pewter Director:** ¡Estoy muy satisfecho con tu trabajo, Player!
  - (Condition: Dialogue 3:)
    - **Purple Pewter Director:** ¡Eres un verdadero activo para Purple Pewter!
  - (Condition: Dialogue 4:)
    - **Purple Pewter Director:** ¡Nunca dejas de satisfacer, Player!
  - (Condition: Dialogue 5:)
    - **Purple Pewter Director:** ¡Haré que mi secretaria envíe esto al parqué de inmediato!
- (continue)
- (Condition: If the player received the task from complaining about the trade floor guards:)
  - **Purple Pewter Director:** Hablaré con los guardias. No te estarán mirando durante los próximos diez minutos.
  - Los guardias del piso de comercio ahora están sobornados para que lo ignoren.
- (Condition: Otherwise:)
  - (continuea|xzx)

#### Después de la olvidable historia de un Drunken Dwarf

- **Purple Pewter Director:** ¡Hola Player! ¿Has visto la estatua? ¡Se ve hermoso! Es una pena que se haya visto eclipsado por la marcha del Red Axe.
- (continuea|xzx)

#### Después del Rey de los Enanos

- **Purple Pewter Director:** Entregar el poder a la monarquía fue el peor día de mi vida. Al menos el rey Veldaban ha mantenido al Consorcio como organismo asesor.
- (continuea|xzx)

#### Después de la primogenitura de los enanos

- (Condition: If Veldaban is still king:)
  - **Purple Pewter Director:** Espero que entiendas lo que has hecho, humano. Podrías haber convencido a Veldaban de que renunciara y dejara que los expertos se hicieran cargo. En cambio, volvemos a cargar con sus ridículas políticas.
- (Condition: If Drunken Dwarf III is king:)
  - **Purple Pewter Director:** Las cosas podrían ser peores, supongo. El nuevo rey está escuchando los consejos del Consorcio... en las pocas ocasiones en que está lo suficientemente sobrio como para entenderlos.
- (Condition: If the Consortium is back in power:)
  - **Purple Pewter Director:** Gracias por tu apoyo en la reunión, Player. Ahora Keldagrim puede dejar atrás los tontos negocios de los reyes y dejar que los directores de la empresa gestionen las cosas correctamente.
- (continuea|xzx)
