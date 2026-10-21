# Kuradal

- **Original Wiki Page**: [Transcript:Kuradal](https://runescape.wiki/w/Transcript%3AKuradal)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|needs Raptor meeting dialogue}}

### At the [[Ancient Cavern]]


#### Hablando con Kuradal

- **Kuradal:** Oye, ¿puedo ayudarte?
- [Menu]: Selecciona una opción
  - [Choice]: Necesito otra tarea.
    - **Player:** Necesito otra tarea.
    - (Condition: Si el player no es nivel 110 Combate y 75 Slayer:)
      - **Kuradal:** Lo siento, pero no eres lo suficientemente fuerte para que yo te enseñe.
  - [Choice]: ¿Podemos hablar de artículos e incentivos?
    - **Player:** ¿Podemos hablar de artículos e incentivos?
    - **Kuradal:** Por supuesto, ¿de qué le gustaría hablar: artículos en venta o incentivos?
    - [Menu]: Selecciona una opción
      - [Choice]: Hablemos de elementos.
        - **Player:** Hablemos de elementos.
        - **Player:** Tengo una amplia selección de equipos Slayer. ¡Échale un vistazo!
        - (opens=Slayer Equipment)
      - [Choice]: Hablemos de incentivos.
        - [Menu]: Selecciona una opción
          - [Choice]: Ver recompensas.
            - (opens=Slayer Rewards)
          - [Choice]: ¿Cómo gano puntos cooperativos para gastarlos en recompensas?
            - **Kuradal:** Obtendrás puntos de recompensa cooperativa si completas al menos la mitad de tu contribución a una tarea con un amigo. Eso significa que debes estar en un grupo la mayor parte del tiempo que estés trabajando en la tarea, ¡pero no importa si tu amigo te gana en la mayoría de las muertes! Aún habrás estado en un grupo durante la mayor parte de tu contribución, por lo que aún tendrás derecho a un punto de recompensa cooperativa.
              - [Choice]: Ver recompensas.
                - (arriba)
              - [Choice]: ¿Dónde puedo usar las recompensas cooperativas de comida y pociones?
                - (abajo)
              - [Choice]: Eso es todo, gracias.
                - (end)
          - [Choice]: ¿Dónde puedo usar las recompensas cooperativas de comida y pociones?
            - **Kuradal:** Las recompensas se pueden usar en la mayoría de las áreas que comúnmente te enviamos para completar tus tareas.
            - [Choice]: Ver recompensas.
              - (arriba)
            - [Choice]: ¿Cómo gano puntos cooperativos para gastarlos en recompensas?
              - (arriba)
            - [Choice]: Eso es todo, gracias.
  - [Choice]: cond=If the player does not have 99 Slayer|Cuéntame sobre tu skillcape, por favor.
    - **Player:** Cuéntame sobre tu skillcape, por favor.
    - **Kuradal:** Este es un Skillcape de Slayer. Sólo un verdadero Slayer master puede usar uno. Necesitas más entrenamiento antes de ganar ese honor.
  - [Choice]: cond=If the player has 99 Slayer:|¿Puedes venderme un Slayer skillcape?
    - **Kuradal:** Bueno, te has desempeñado bien como estudiante. Supongo que ahora te has ganado el derecho a llevar una capa tan prestigiosa. Serán 99.000 coins, por favor.
    - ((Si el player tiene un Ring of charos (a) equipado, el mensaje se reemplaza por lo siguiente:))
      - **Kuradal:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins para este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
    - (Condition: Si el player tiene un token inverted skillcape o un token maestro skillcape invertido en su inventario sintonizado con Slayer:)
      - **Kuradal:** ¡Veo que tienes una de las fichas de inversión de capa de Hans! Te quitaré eso de las manos y te venderé cualquier inverted cape para el que seas elegible.
      - (removes=any inverted skillcape token and inverted master skillcape token)
        - (continue)
    - [Menu]: Elige una opción:
      - [Choice]: ¿99.000 coins? Eso es demasiado caro. ((o 92.000 coins con Ring of charos (a)))
        - **Kuradal:** En absoluto; ¡Hay muchos otros aventureros a quienes les encantaría tener la oportunidad de comprar un artículo tan prestigioso! Puedes encontrarme aquí si cambias de opinión.
      - [Choice]: De hecho, creo que tengo el dinero aquí.
        - *(Si el player tiene al menos dos espacios backpack libres:)*
          - (removes=99,000 coins (or 92,000 coins with Ring of charos (a))) Campana (receives=Slayer cape (or trimmed version if level 99 in at least two skills) y Slayer)
          - **Kuradal:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
        - (Condition: Si el player no tiene al menos dos espacios backpack libres:)
          - **Kuradal:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar algo de espacio en el inventario antes de que pueda venderte uno.
      - [Choice]: cond=If the player has given Kuradal an inverted skillcape token:|Me gustaría un skillcape con los colores invertidos.
        - (receives=Inverted Slayer skillcape)
      - [Choice]: cond=If the player has level 120 Slayer:|He dominado esta habilidad. ¿Hay algo más?
        - **Kuradal:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
        - **Kuradal:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
        - **Kuradal:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo...
        - **Kuradal:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderte una capa Slayer master.
          - ¿Comprar capa Slayer master por 120.000 coins?
            - Sí.
              - *(Si el player tiene al menos un espacio backpack libre:)*
                - (removes=120,000 coins) (receives=Slayer master cape)
              - *(Si el player no tiene al menos un espacio libre en backpack:)*
                - **Kuradal:** No tienes suficiente espacio en tu inventario. Por favor regresa cuando tengas más.
            - No.
            - (end)
      - [Choice]: cond=If the player has given Kuradal an inverted master skillcape token:|Me gustaría un master cape con los colores invertidos.
        - ((Igual que he dominado esta habilidad. ¿Hay algo más?, excepto recibir un Slayer skillcape maestro invertido en lugar de una capa Slayer master normal.))
  - [Choice]: He notado que hay un par de versiones de cada skillcape.
    - **Kuradal:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
    - *(Si el player ha elegido los nuevos modelos skillcape :)*
      - **Kuradal:** Aún puedes optar por usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
      - Seleccione una opción
        - Sí, me gustaría usar la versión antigua del skillcape.
          - **Kuradal:** ¿Te gustaría usar el modelo antiguo solo para esta capa, o para la capa de puntos Quest y todos los skillcapes que tienes?
          - Seleccione una opción
            - Solo me gustaría cambiar el Slayer skillcape.
              - **Kuradal:** No hay problema, ahora utilizarás el modelo anterior para tu Slayer skillcape.
            - Me gustaría cambiar todos mis skillcapes.
              - **Kuradal:** No hay problema, ¡ahora usarás el modelo anterior para todos tus skillcapes!
            - ¡He cambiado de opinión!
              - (end)
        - [Choice]: No, gracias.
          - **Kuradal:** ¡Genial! ¡Me alegra que estés disfrutando de nuestra nueva versión!
          - *(Si el player está usando los modelos skillcape antiguos excepto la capa Slayer :)*
            - **Kuradal:** ¡Si quieres, puedo hacerlo para que uses el modelo más nuevo para todos los skillcapes que tienes!
            - [Menu]: Selecciona una opción
              - [Choice]: Ok, me gustaría usar la versión más nueva para todos mis skillcapes.
                - **Kuradal:** ¡Genial, ahora usarás el modelo más nuevo para todos tus skillcapes!
              - No, gracias.
                - (end)
    - *(Si el player ha elegido los modelos antiguos skillcape :)*
      - **Kuradal:** Parece que actualmente estás usando el modelo anterior para tu Slayer skillcape. ¿Quieres cambiar a uno más nuevo?
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, me gustaría usar la nueva versión del skillcape.
          - **Kuradal:** ¿Te gustaría usar el modelo más nuevo solo para esta capa o para todos los skillcapes que tienes?
          - Seleccione una opción
            - Solo me gustaría cambiar el Slayer skillcape.
              - **Kuradal:** No hay problema, ahora utilizarás el modelo más nuevo para tu Slayer skillcape.
            - Me gustaría cambiar todos mis skillcapes.
              - **Kuradal:** No hay problema, ¡ahora usarás el modelo más nuevo para todos tus skillcapes!
            - ¡He cambiado de opinión!
              - (end)
        - No, gracias.
          - **Kuradal:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión anterior!
          - *(Si el player está usando los nuevos modelos skillcape excepto la capa Slayer :)*
            - **Kuradal:** ¡Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas!
            - Seleccione una opción
              - Ok, me gustaría usar la versión antigua para todos mis skillcapes.
                - **Kuradal:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
              - No, gracias.
                - (end)
  - [Choice]: Hablemos de ti.
    - **Player:** Hablemos de ti.
    - **Kuradal:** Soy Kuradal, hija de Duradel. ¿Qué más te gustaría saber?
      - Cuéntame más sobre tus antecedentes.
        - **Player:** Cuéntame más sobre tus antecedentes.
        - **Kuradal:** Si así lo deseas. Como dije, soy Kuradal, hija de Duradel - otro gran maestro de Slayer. Sin embargo, a diferencia de los demás, me aventuré no sólo a matar, sino también a capturar. He capturado muchos tipos diferentes de criaturas y las mantengo dentro de esta mazmorra, reservada exclusivamente para que mis alumnos las maten.
        - **Player:** Entonces, ¿matar es cosa de familia?
        - **Kuradal:** Por supuesto. Uno no puede simplemente "crecer" con alguien como mi padre. Mi infancia fue toda entrenamiento de combate, enfrentándome a las bestias de esta tierra al lado de mi padre.
          - Entonces ¿quién es tu madre?
            - **Player:** Entonces, ¿quién es tu madre?
            - **Kuradal:** Preferiría no decirlo. ¿Podemos hablar de otra cosa?
              - Sobre tu padre...
                - *(Igual que a continuación)*
              - Eso es todo por ahora.
                - **Player:** Eso es todo por ahora.
                - **Kuradal:** Bien. Estaré aquí si me necesitas.
          - ¡Parece que tuviste una infancia agitada!
            - **Player:** ¡Parece que tuviste una infancia agitada!
            - **Kuradal:** Se podría decir eso, pero estoy agradecido por ello, ya que me convirtió en la persona que soy hoy.
              - Sobre tu padre...
                - *(Igual que a continuación)*
              - Eso es todo por ahora.
                - *(Igual que arriba)*
      - Sobre tu padre...
        - *Si aún no has completado Mientras Guthix duerme*
          - **Player:** Sobre tu padre... ¿Cómo es que no estás con él ahora?
          - **Kuradal:** Todavía estamos cerca, pero el combate y la competencia corren profundamente en nuestras venas. Me esfuerzo por ser el mejor, por eso asumí un puesto en Slayer Master y quiero brindarles a las personas un desafío mayor que el de mi padre.
        - *Si has completado el Ritual del Mahjarrat*
          - **Player:** Acerca de tu padre... ¡Lucien está muerto!
          - **Kuradal:** Lo sé. Vi su cadáver en el lugar del ritual.
          - **Player:** ¿Qué? ¿Estabas allí? No te vi.
          - **Kuradal:** Yo tampoco, pero yo estaba allí, luchando contra Mahjarrat y sus secuaces. Sin embargo, ninguno de ellos era Lucien. Perseguí a uno de ellos hasta una cueva llena de elementales de hielo llamados glacors. Después de matar a un par de cientos de ellos, logré escapar, pero para entonces todo había terminado: todos se habían ido.
          - **Player:** Suenas enojado. ¡Pensé que te alegrarías de que estuviera muerto!
          - **Kuradal:** Lo soy, ¡pero Lucien fue mi presa! ¡Solo mío! ¡Nadie tenía derecho a quitarme eso! ¡Nadie! ... ¿Cómo honraré la memoria de mi padre?
            - Lo honras todos los días.
              - **Player:** Lo honras todos los días.
              - **Kuradal:** ¡Bah! Si sigues con esas tonterías sensibleras me veré obligado a revocar tu licencia de Slayer...
              - **Player:** Pero, yo-
              - **Kuradal:** ¡Jajaja! ¡La expresión de tu cara! Eso me animó un poco. Gracias, Player. "Lo honras todos los días".
              - **Player:** Me alegro de poder ayudar.
              - **Kuradal:** Ahora, ¿puedo ayudar con algo más?
            - ¡Ayudando a derrotar a lo que mató a Lucien!
              - **Player:** ¡Ayudando a derrotar a lo que mató a Lucien!
              - **Kuradal:** ¿Qué era exactamente?
              - **Player:** Un dragonante. De hecho, tres de ellos.
              - **Kuradal:** Hmm, eso suena como un desafío digno de un slayer master. Tengo algunos preparativos que hacer. Recolectarlos para una mazmorra podría ser complicado...
              - **Player:** ¿Coleccionarlos? ¡Estás loco!
              - **Kuradal:** Ahora, ¿puedo ayudar con algo más?
      - Entonces, ¿qué hay en esta mazmorra?
        - **Player:** Entonces, ¿qué hay en esta mazmorra?
        - **Kuradal:** Bueno, estuve por todas partes y logré capturar perros del infierno, demonios mayores, gárgolas, demonios abisales, airut, bestias oscuras, dragones azules, de hierro y de acero.
          - *Si juegas como un personaje masculino* **Player:** ¿Los atrapaste sin ayuda de nadie?
          - **Kuradal:** ¿Dudas de mis habilidades?
          - No quise decir nada con eso.
            - **Player:** No quise decir nada con eso.
            - **Kuradal:** Me alegra saberlo. *(continúa como a continuación)*
          - Bueno, vamos. ¡Tú eres solo una niña y yo soy un guerrero duro!
            - **Player:** Bueno, vamos. ¡Tú eres solo una niña y yo soy un guerrero duro!
            - **Kuradal:** Sólo una niña, ¿verdad? ¿Bien? *(Kuradal te noquea y te despiertas fuera de las antiguas cavernas.)*
        - **Player:** Entonces, ¿hay algo más que sea especial en esta mazmorra?
        - **Kuradal:** Me alegra que lo hayas preguntado. Es posible que encuentres criaturas dentro de la mazmorra que dejen caer algo llamado anillo feroz; deben haberlos recolectado de los restos del área.
        - **Player:** Bueno, eso es genial y todo, pero ¿qué hace exactamente?
        - **Kuradal:** Bueno, por un lado, están vinculados a estas cuevas, por lo que encontrarás que tiene cargas de teletransporte que te devolverán a este lugar si lo ordenas.
        - **Player:** Suena bien, pero ¿es eso todo?
        - **Kuradal:** Oh, no. Como dije, está vinculado a esta área, por lo que encontrarás que haces más daño a las criaturas en la mazmorra si lo llevas puesto. Además, si estás cerca de la muerte en la mazmorra, te salvará de manera similar a un anillo de vida, teletransportándote de regreso a la seguridad de mi presencia.
        - **Player:** ¿Incluso si estoy usando combate a distancia o mágico? ¿Y qué pasa si no estoy en el calabozo cuando muera usándolo?
        - **Kuradal:** Cálmate, una pregunta a la vez. Primero, es un artefacto poderoso y afectará a todos los estilos de combate. En segundo lugar, tendría cuidado de no morir afuera usándolo. No creo que funcione en ningún otro lugar que no sea dentro de la mazmorra aquí.
        - **Player:** Gracias por tu ayuda, Kuradal.
        - **Kuradal:** No hay problema. ¿Algo más?
          - (initial)
  - [Choice]: cond=If the player has special slayer assignments disabled, the "Let's talk about you" option is replaced with the following|¿Puedo volver a recibir asignaciones especiales de asesino?
    - **Kuradal:** Claro, ahora comenzaré a darte tareas especiales de cazador nuevamente.
  - [Choice]: Eh... nada...
    - **Player:** Eh... nada...
    - (end)

#### Intentando entrar a su mazmorra

*Sin tarea de ella:*
- **Kuradal:** Lo siento, mi mazmorra es exclusiva solo para aquellos que necesitan entrar allí.
- **Player:** ¿Exclusivo?
- **Kuradal:** Sí, solo permito que los alumnos de Slayer entren en esta mazmorra y solo si necesitan matar a las criaturas que he atrapado dentro.
- **Player:** Ya veo. Entonces, ¿qué criaturas necesito que me asignen para matar? ¿Qué criaturas hay dentro?
- **Kuradal:** Bueno, hice un recorrido navideño por Gielinor y traje algunos 'souvenirs'. Por supuesto, como Slayer master, "souvenirs" significa perros del infierno, demonios mayores, gárgolas, demonios abisales, airut, bestias oscuras y dragones azules, de hierro y acero.
- **Player:** Normalmente lo mantendría sencillo con una postal.
- **Kuradal:** ¿Qué fue eso?
- **Player:** Dije que debe haber sido difícil.
*Con un cañón:*
- **Kuradal:** Lo sentimos, no se permiten cañones allí. Ahora que he reunido a todas estas criaturas, no quiero particularmente que destruyan su guarida.

### Activating the [[enchanted gem]]


#### Si Kuradal es tu Slayer Master actual

- **Kuradal:**  Hola, Player, ¿en qué puedo ayudarte?
  - ¿Cómo estoy hasta ahora?
    - **Player:** ¿Cómo me va hasta ahora?
      - *Si actualmente estás en una tarea Slayer que aún no está completa: *
        - **Kuradal:**  Actualmente estás asignado para matar a [assigned creatures]; sólo faltan X más.
          - ¿Quién eres?
            - *(Igual que a continuación)*
          - ¿Dónde estás?
            - *(Igual que a continuación)*
          - ¿Tienes algún consejo para mí?
            - *(Igual que a continuación)*
          - Eso es todo gracias.
            - **Player:** Eso es todo, gracias.
      - *Si has completado tu tarea Slayer más reciente: *
        - {{Transcript missing}}
  - ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Kuradal:**  Mi nombre es Kuradal; Soy un Slayer Master.
      - ¿Cómo estoy hasta ahora?
        - *(Igual que arriba)*
      - ¿Dónde estás?
        - *(Igual que a continuación)*
      - ¿Tienes algún consejo para mí?
        - *(Igual que a continuación)*
      - Eso es todo gracias.
        - *(Igual que arriba)*
  - ¿Dónde estás?
    - **Player:** ¿Dónde estás?
    - **Kuradal:**  Me encontrarás en la caverna antigua, cerca de Dragonkin Forge. Estaré aquí cuando necesites una nueva tarea.
      - ¿Cómo estoy hasta ahora?
        - *(Igual que arriba)*
      - ¿Quién eres?
        - *(Igual que arriba)*
      - ¿Tienes algún consejo para mí?
        - *(Igual que a continuación)*
      - Eso es todo gracias.
  - ¿Tienes algún consejo para mí?
    - **Player:** ¿Tienes algún consejo para mí?
    - **Kuradal:**  El último [assigned creature] que maté descubrí que [weapons] los derribó de manera efectiva.
    - [sugerencia de tarea]
      - ¿Cómo estoy hasta ahora?
        - *(Igual que arriba)*
      - ¿Quién eres?
        - *(Igual que arriba)*
      - ¿Dónde estás?
        - *(Igual que arriba)*
      - Eso es todo gracias.
        - *(Igual que arriba)*
  - Nada realmente.
    - **Player:**  En realidad, nada.

### Casting [[NPC Contact]]

- **Player:** ¿Hola?
- **Kuradal:** 'Hola, ¿quién es?
- **Player:** Soy Player. Estoy usando mi magia para comunicarme contigo.
- **Kuradal:** Una aplicación útil del talento mágico. ¿Cómo puedo ayudar?
  - Seleccione una opción
    - Necesito otra tarea.
      - *(Igual que arriba)*
    - Eh... nada.
      - **Player:** Eh... nada.

### Assignment advice


#### Espectros aberrantes

- **Kuradal:** Los espectros aberrantes son fantasmas fétidos y viles. El solo olor de ellos te paralizará y te hará daño. Una clavija ayudará a ignorar su hedor cuando luches contra ellos. Se pueden encontrar en la Torre Slayer cerca de Canifis y he escuchado rumores de que también viven debajo de Pollnivneach en el desierto.

#### Demonios abisales

- **Kuradal:** Los demonios abisales son criaturas desagradables con las que lidiar. En realidad, no son parte de este reino y pueden moverse muy rápidamente para atrapar a sus presas. Me las arreglé para atrapar a algunos en la mazmorra que estoy custodiando.

#### mamuts de Acheron

- **Kuradal:** Los mamuts de Acheron son bestias honorables pero poderosas del norte helado. Cuando te cobren, ¡apártate del camino! Se pueden encontrar en un iceberg al que se puede acceder desde un muelle cerca de Rellekka.

#### Dragones inflexibles

- **Kuradal:** Los dragones Adamant son incluso más peligrosos que los dragones de mithril. Búscalos en la mazmorra Brimhaven, debajo de una escalera al noroeste de los dragones de hierro y acero.

#### Airut

- **Kuradal:** Los Airut son criaturas agresivas de otro mundo. Tienen brazos poderosos y atacan con gran vigor, ciertas habilidades son capaces de contrarrestar y aturdir al Airut.

#### Acuanitas

- **Kuradal:** Los acuanitas son criaturas anfibias que atraen a sus presas utilizando los señuelos brillantes que tienen en la cabeza. Atacan a oponentes más fuertes desde la distancia con magia de agua y no les agradan aquellos que rezan en contra de ella. Habitan en la mazmorra Fremennik Slayer, en una cámara más allá de los kurasks.

#### Miembros de la Ascensión

- **Kuradal:** La Orden de la Ascensión son usuarios de magia. Se recomienda encarecidamente utilizar ataques a distancia. Sus tácticas pueden hacerlos difíciles uno a uno, por lo que sería beneficioso traer a un amigo.

#### Avianas

- **Kuradal:** Los aviansies se pueden encontrar en Godwars Dungeon al norte de Trollheim. Mientras vuelan, descubrirás que los ataques cuerpo a cuerpo no serán suficientes.

#### Demonios negros

- **Kuradal:** Los demonios negros son débiles ante los ataques a distancia. Sin embargo, siguen siendo el demonio más fuerte y muy peligroso. Búscalos en las mazmorras Edgeville o Brimhaven.

#### Dragones negros

- **Kuradal:** Los dragones negros se encuentran entre los dragones más fuertes y son muy feroces. Cuidado con su aliento de fuego. Estoy seguro de que los habrás visto en tus viajes y habrás perfeccionado tus técnicas con dragones menores.

#### manto de sangre

- **Kuradal:** Los Bloodvelds son criaturas extrañas y demoníacas. Utilizan su lengua larga y áspera para alimentarse de casi cualquier cosa que encuentren. Recuerda que sus lenguas son de naturaleza mágica, pero, más aún, merecen morir.

#### Dragones azules

- **Kuradal:** Los dragones azules no son tan fuertes como otros dragones, pero siguen siendo muy poderosos. Me las arreglé para atrapar a algunos en la mazmorra que estoy custodiando.

#### guerreros Camel

- **Kuradal:** Los guerreros Camel pueden usar magia antigua para atacarte. También cuentan con las bendiciones de Akthanakos y pueden crear espejismos poderosos y desorientadores.  Se pueden encontrar en lo profundo del desierto.

#### Dragones celestiales

- **Kuradal:** Los dragones celestiales son uno de los dragones más extraños que asigno. Usan combate cuerpo a cuerpo pero tienen un poderoso fuego de dragón, así como una habilidad fascinante para detener el tiempo momentáneamente. Puedes encontrarlos en las profundidades de la isla Dragontooth.

#### Gigantes del caos

- **Kuradal:** Puedes encontrar gigantes del Caos en los túneles de Barendir, más allá de Keldagrim. Ten cuidado, ya que pueden lanzar su hacha arrojadiza Dragón a distancia o golpearte si te acercas. Quizás puedas recuperar algo.

#### Criaturas corruptas

- **Kuradal:** Puedes encontrar criaturas corruptas en la mazmorra Sophanem Slayer.

#### Autómatas de Cres

- **Kuradal:** Sin su maestro, los autómatas de Cres deambulan por las cámaras de Guthix, atacando a cualquiera que entre. Están programados para usar magia, cuerpo a cuerpo o a distancia y realizar un violento ataque de área de efecto. Se puede llegar a las cámaras de Guthix a través de su santuario o de la excavación al oeste de Legends' Guild.

#### Dagannot

- **Kuradal:** Los Dagannoth son criaturas marinas grandes que son muy agresivas. A menudo los encontrarás en cuevas cerca del agua de mar. No hay alegría tan grande como limpiar estos de the face de Gielinor.

#### Bestias oscuras

- **Kuradal:** La última bestia oscura que maté encontré una ballesta con pernos que los derribó de manera efectiva.
- [Las bestias oscuras son depredadores grandes, parecidos a perros, con cuerpos enormemente musculosos que los protegen de las armas aplastantes. Me las arreglé para atrapar a algunos en la mazmorra que estoy custodiando.]

#### Vermis del desierto

- **Kuradal:** Los encontrarás al este de Al Kharid, en la cima de la montaña. ¡Cuidado con sus feroces ataques a distancia!

#### Diablos de polvo

- **Kuradal:** Los remolinos de polvo utilizan nubes de polvo, arena, cenizas y cualquier otra cosa que puedan inhalar para cegar y desorientar a sus víctimas. Buena suerte para obtener una cota de malla de dragón a partir de sus restos polvorientos.

#### Edimmu

- **Kuradal:** Edimmu son fantasmas que no lograron escapar de su cuerpo. Son fantasmas y zombis, pero de alguna manera completamente diferentes. Usan ataques a distancia y son muy agresivos. Puedes encontrarlos en una mazmorra de recursos a la que tiene acceso el clan Meilyr en Prifddinas.

#### Elfos

- **Kuradal:** Los elfos son luchadores expertos en todas las disciplinas de los que puedes aprender mucho. Recomiendo desafiar sólo a un tipo de combatiente elfo a la vez.

#### Gigantes de fuego

- **Kuradal:** Al igual que otros gigantes, los gigantes de fuego suelen empuñar armas grandes. Aprende a reconocer qué tipo de arma es y actúa en consecuencia. Recuerda los días en que estos eran un desafío para ti y ríe.

#### Criaturas ganodermicas

- **Kuradal:** Las bestias ganodermicas y los enanos viven en las profundidades de una cueva al noreste de Mage Training Arena. Las criaturas de esa mazmorra están cubiertas de hongos tóxicos, por lo que debes luchar contra ellas desde la distancia. El hongo les ayuda a reparar el daño físico, por lo que quizás prefieras usar ataques mágicos.

#### Gárgolas

- **Kuradal:** Las gárgolas son criaturas aladas de piedra. Tendrás que luchar contra ellos hasta que estén al borde de la muerte antes de romperlos con un martillo de piedra. Me las arreglé para atrapar a algunos en la mazmorra que estoy custodiando.

#### Dragones de piedras preciosas

- **Kuradal:** Puedes encontrar dragones de piedras preciosas debajo de la mina de gemas en Shilo Village.

#### Glaciares

- **Kuradal:** Lucien trajo los glacors a este mundo. Usan ataques mágicos, a distancia y cuerpo a cuerpo. Puedes encontrarlos en una caverna subterránea en Frozen Plateau.

#### Demonios mayores

- **Kuradal:** Los demonios mayores son débiles ante los ataques a distancia. Aunque no son los demonios más fuertes, siguen siendo peligrosos. Me las arreglé para atrapar a algunos en la mazmorra que estoy custodiando.

#### Grifolapinas

- **Kuradal:** Los grifolapinos viven en las profundidades de una cueva al noreste de Mage Training Arena. Las criaturas de esa mazmorra están cubiertas de hongos tóxicos, por lo que debes luchar contra ellas desde la distancia y esquivar cuando cargan contra ti. El hongo les ayuda a reparar el daño físico, por lo que quizás prefieras usar ataques mágicos.

#### Grifolaroos

- **Kuradal:** Los grifolaroos viven en las profundidades de una cueva al noreste de Mage Training Arena. Las criaturas de esa mazmorra están cubiertas de hongos tóxicos, por lo que deberás luchar contra ellas desde la distancia, aunque intentarán saltar los obstáculos hacia ti. El hongo les ayuda a reparar el daño físico, por lo que quizás prefieras usar ataques mágicos.

#### Gusanos de grosella

- **Kuradal:** Recientemente se han visto gusanos grot en una cueva cerca de Rimmington. Morderán y atacarán con una especie de saliva ácida. Tenga cuidado, son muy agresivos.

#### Perros del infierno

- **Kuradal:** Los Hellhounds son un cruce entre perros y demonios; También son peligrosos con un mordisco feroz. Me las arreglé para atrapar a algunos en la mazmorra que estoy custodiando.

#### Vermis de hielo

- **Kuradal:** Los más fríos de su tipo, se encuentran debajo de las montañas Fremennik. Como son seres de hielo, descubrí que los hechizos de fuego les infligen mucho más daño.

#### Dragones de hierro

- **Kuradal:** Los dragones de hierro son algunos de los dragones metálicos más débiles, con escamas de hierro que son mucho más gruesas que las armaduras de hierro normales. Su aliento de fuego y sus afiladas garras pueden anularse de diversas formas. Me las arreglé para atrapar a algunos en la mazmorra que estoy custodiando.

#### Wyrms de la selva

- **Kuradal:** Estas engañosas criaturas se esconden bajo la jungla al noroeste de Oo'glog. Ten cuidado, ya que a estos venenosos wyrms de la jungla les gusta usar ataques mágicos desde la distancia, mientras que deberían ser débiles para apuñalar ataques.

#### Demonios Kal'gerion

- **Kuradal:** Los demonios Kal'gerion son criaturas poderosas que usan tanto magia como cuerpo a cuerpo. Residen en un calabozo de almacenamiento cerca de Daemonheim. Te recomendaría que te cubrieras cuando rompan el suelo o cuando usen magia para atraerte hacia ellos.

#### Calfitos

- **Kuradal:** Los calfitos son insectos grandes que viven en colmenas bajo las arenas del desierto. Estoy seguro de que ya los habrás visto al suroeste del paso Shantay.

#### Vermis de lava

- **Kuradal:** Los strykewyrms de lava son los más poderosos de su tipo. Atacan con todos los estilos de combate y son débiles o nada. Se pueden encontrar en lo profundo de Wilderness, por lo que yo te cuidaría las espaldas mientras los mato.

#### Criaturas vivientes de las rocas

- **Kuradal:** Estos son seres duros de roca que se encuentran debajo de las minas enanas. Pueden usar ataques a distancia o cuerpo a cuerpo contra ti, ¡así que planifica en consecuencia!

#### Wyverns vivientes

- **Kuradal:** Los wyverns vivos respiran un veneno que te matará rápidamente a menos que te congeles. Pero cuidado; cuanto más frío tengas, más duro te golpearán sus ataques habituales.  Se pueden encontrar en la mazmorra de hielo de Asgarnia.

#### Dragones de mitril

- **Kuradal:** Los dragones de mitril son oponentes muy peligrosos. Viven justo al norte de donde estamos ahora. Eres un maestro de batalla: prueba tus habilidades.

#### Muspa

- **Kuradal:** Los muspah son criaturas nacidas de pesadillas. La magia antigua es lo más eficaz que se puede utilizar contra ellos. Puedes encontrarlos viajando a Freneskae. Serán agresivos a menos que uses tu fragmento de Zaros.

#### Jadinkos mutados

- **Kuradal:** Estas criaturas deformadas de enredadera de jade no dudarán en utilizar su entorno para ayudarles en el combate si no pueden tomar represalias de otra manera. Las crías de jadinkos son más fáciles de matar, pero los machos ofrecen las mayores recompensas. Las armas Ranged hechas de enredaderas son mejores contra ellos.

#### Necriael

- **Kuradal:** Nechryael son demonios de la decadencia que convocan a pequeños seres alados para que les ayuden a luchar contra sus víctimas. Se pueden encontrar en los Túneles del Caos o en la Torre Canifis Slayer.

#### Criaturas de pesadilla

- **Kuradal:** Puedes encontrar criaturas de pesadilla en Freneskae, a las que se puede acceder a través de la puerta del mundo.

#### nihil

- **Kuradal:** Los sujetos supervivientes de los experimentos de Zaros. Tienen poderosos ataques cargados y luchan en grupos de cuatro. Puedes encontrarlos viajando a Freneskae. Serán agresivos a menos que uses tu fragmento de Zaros.

#### Demonios destripadores

- **Kuradal:** Los demonios destripadores se vuelven locos por el olor a sangre. Te golpearán más fuerte cuanto peores sean tus lesiones. Y cuidado; A veces pueden caer sobre ti desde arriba, lo cual es letal.  Se pueden encontrar en una fisura cerca de Al Kharid.

#### Hombres lobo sanguíneos

- **Kuradal:** El último hombre lobo Sanguine que maté descubrí que los hechizos de tierra los derribaron de manera efectiva.
- [Los hombres lobo sanguinarios son hombres lobo retorcidos por los sanguinarios. Los encontrarás en Berylbrook en Havenhythe.]

#### Wyverns esqueléticos

- **Kuradal:** Los wyverns esqueléticos son extremadamente peligrosos y es difícil golpearlos con flechas cuando se deslizan a través de ellos. Para tener buenas posibilidades de sobrevivir, necesitarás algo de protección elemental contra su aliento helado.

#### Devoradores de almas

- **Kuradal:** Puedes encontrar devoradores de almas en la mazmorra Sophanem Slayer.

#### Magos espirituales

- **Kuradal:** Los magos espirituales son los más fuertes de los guardianes espirituales. Son devastadores contra los guerreros, pero un explorador inteligente a veces puede derrotarlos. Por supuesto, Prayer también podría resultarle útil. Se pueden encontrar en las cavernas heladas cerca de Trollheim, apoyando la causa de su dios elegido.

#### Criaturas acosadoras

- **Kuradal:** El último Soulgazer que maté encontré un arco y las flechas lo derribaron de manera efectiva.
- [Puedes encontrar criaturas acosadoras dentro del escondite de Zamorak.]

#### Dragones de acero

- **Kuradal:** Los dragones de acero son peligrosos y metálicos, con escamas de acero que son mucho más gruesas que las armaduras de acero normales. Me las arreglé para atrapar a algunos en la mazmorra que estoy custodiando.

#### Suqahs

- **Kuradal:** Las suqahs solo se pueden encontrar en el místico Lunar Isle. Usan ataques cuerpo a cuerpo y mágicos y, a menudo, dejan caer piel, dientes y hierbas.

#### Perros terroristas

- **Kuradal:** Los perros del terror son, como era de esperar, perros que aterrorizan a los débiles. Los encontrarás en la Mina Encantada, cerca de la guarida de Tarn.

#### Demonios atormentados

- **Kuradal:** Los demonios atormentados son criaturas poderosas que usan ataques mágicos, a distancia y cuerpo a cuerpo. También tienen la capacidad de protegerse. Puedes encontrarlos debajo de la cueva Lágrimas de Guthix.

#### Tzhaar

- **Kuradal:** El TzHaar contiene algunos guerreros poderosos, ponte a prueba contra ellos. Los encontrarás en lo profundo del volcán Karamja.

#### Criaturas volcánicas

- **Kuradal:** Estas son las criaturas que viven dentro de las cuevas de lucha de TzHaar. Tendrás que aventurarte en la cueva del volcán Karamja para enfrentarte a ellos.

#### Vyrewatch

- **Kuradal:** Estas repugnantes criaturas se pueden encontrar en Meiyerditch y Darkmeyer en Morytania. Tienen una habilidad telepática que les permite esquivar los ataques entrantes, por lo que necesitarás un arma especialmente creada para dañarlos.

#### Tortugas deformadas

- **Kuradal:** Las tortugas deformadas son criaturas contaminadas por desechos mágicos. Son vulnerables a un timbre élfico. Sé que los has visto en tus aventuras, así que ve a romper un caparazón.

#### Demonios del agua

- **Kuradal:** Los Waterfiends son criaturas acuáticas que viven justo al norte de nosotros. Aquellos seguidos por familiares están deseosos de acabar con estas fuerzas elementales.
