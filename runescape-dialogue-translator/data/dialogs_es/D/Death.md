# Death

- **Original Wiki Page**: [Transcript:Death](https://runescape.wiki/w/Transcript%3ADeath)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Upon death


#### En la primera muerte

- **Muerte:** Saludos.
- [Menu]: Selecciona una opción
  - [Choice]: Encantado de conocerte.
    - **Muerte:** Me alegra ver que te lo tomas tan bien. La mayoría de los fallecidos recientemente están más molestos.
    - (continue|not-your-time1)
  - [Choice]: ¿Estoy... muerto?
    - **Muerte:** Sí, me temo que lo eres.
    - (continue|not-your-time1)
  - [Choice]: ¡AHHHHHHHHHHHHH!
    - **Muerte:** Cálmate, cálmate. Simplemente estás muerto.
    - (continue|not-your-time1)
- **Muerte:{{anchor|not-your-time1}}** Afortunadamente para ti, aún no es tu momento.
- [Menu]: Selecciona una opción
  - [Choice]: ¡Genial! ¿Cómo vuelvo?
    - **Muerte:** No es tu momento. El destino te espera. No te reclamaré. Todavía.
    - **Player:** Correcto... gracias.
    - (continue|use-the-portal)
  - [Choice]: Espera... ¿No estoy muerto?
    - (continue|use-the-portal)
- **Muerte:{{anchor|use-the-portal}}** Puedes regresar ahora. Cuando salgas de aquí, volverás al pueblo.
- **Muerte:** Cuando mueres, conservas algunos de tus objetos, pero pierdes otros.
- **Player:** ¿Pierdo mis cosas?
- **Muerte:** Tu valioso equipo se dejará caer dondequiera que mueras. Sin embargo, puedes elegir tres de esos elementos para conservarlos.
- Puedes ver qué elementos caerán y cuáles se conservarán en la interfaz de Deathkeep en tu Inventario desgastado.
- **Muerte:** Cuando regresas al mundo de los vivos, tienes un límite de tiempo breve para regresar al lugar de tu muerte y recuperar el equipo que se te cayó.
- Siempre que mueras con elementos que podrían caer, verás una interfaz que te permitirá elegir cuáles conservar.
- Puedes tomar selectivamente tus artículos uno a la vez, tomarlos todos con el botón "tomar todo" o volver a equipar tu equipo y tomar el resto de tus artículos con el botón "Equipar todo".
- **Muerte:** Toma el portal detrás de ti y regresa al mundo de los vivos.
- [Menu]: Selecciona una opción
  - [Choice]: ¡Adiós!
    - (end)
  - [Choice]: Sólo quiero preguntarte sobre-
    - **Muerte:** ¡Vete!

#### En la primera muerte sin perder ningún objeto.

- **Muerte:** Saludos.
- Seleccione una opción
  - Encantado de conocerte.
    - **Muerte:** Me alegra ver que te lo tomas tan bien. La mayoría de los fallecidos recientemente están más molestos.
    - (continue|not-your-time)
  - ¿Estoy... muerto?
    - **Muerte:** Sí, me temo que lo eres.
    - (continue|not-your-time)
  - ¡AHHHHHHHHHHHHH!
    - **Muerte:** Cálmate, cálmate. Simplemente estás muerto.
    - (continue|not-your-time)
- **Muerte:{{anchor|not-your-time}}** Afortunadamente para ti, aún no es tu momento.
- Seleccione una opción
  - ¡Genial! ¿Cómo vuelvo?
    - **Muerte:** No es tu momento. El destino te espera. La muerte no te reclamará. Todavía.
    - **Player:** Correcto... gracias.
    - (continue|use-the-hourglass)
  - Espera... ¿No estoy muerto?
    - **Muerte:** Puedes regresar ahora. Cuando salgas de aquí, volverás al pueblo.
    - (continue|use-the-hourglass)
- **Muerte:{{anchor|use-the-hourglass}}** Usa el reloj de arena detrás de ti y regresa al mundo de los vivos.
- Seleccione una opción
  - ¡Adiós!
    - (end)
  - Sólo quiero preguntarte sobre-
    - **Muerte:** ¡Vete!

##### Intentando salir a través del reloj de arena

- **Muerte:** Ven aquí.

##### Intentando salir por la puerta del Retiro de War

- {{anchor|gracefully}} **Muerte:** No puedo dejarte usar esa puerta mientras te enseño cómo morir con gracia.

#### Segunda o más muertes, pero perdiendo objetos por primera vez

- **Muerte:** Hola de nuevo..
- Seleccione una opción
  - Hola de nuevo.
    - **Muerte:** Tengo más que contarte.
    - (continue|not-your-time2)
  - ¿Estoy muerto de verdad esta vez?
    - **Muerte:** No, pero tengo más que contarte.
    - (continue|not-your-time2)
  - ¡AHHHHHHHHHHHHH!
    - **Muerte:** Está bien, solo tengo más que contarte.
    - (continue|not-your-time2)
- **Muerte:{{anchor|not-your-time2}}** Ahora te mostraré lo que puedes reclamar de mí. Puede regresar en cualquier momento para reclamar estos artículos.
- (Se abre la interfaz de descripción general del costo de muerte).
- (Condition: After the player has reclaimed their items, or closed the interface without reclaming:)
  - **Muerte:** Usa el reloj de arena detrás de ti y regresa al mundo de los vivos.
  - Seleccione una opción
    - ¡Adiós!
      - (end)
    - Sólo quiero preguntarte sobre-
      - **Muerte:** ¡Vete!

##### Intentando salir por la puerta del Retiro de War

- (above|gracefully)

#### Después de muertes posteriores

  - **Muerte:** Pensé que volverías, Player. ¿Deseas reclamar tus artículos?
  - ¿Recuperar tus artículos?
    - Sí.
      - (Condition: With non-event free item reclaim:)
        - (receives=lost items)
        - La muerte te ha devuelto tus artículos gratis.<br>Es posible que la muerte no sea tan caritativa la próxima vez, así que entra en situaciones peligrosas bajo tu propia responsabilidad.
      - (Condition: With Item Protection Contract in backpack:)
        - **Muerte:** Veo que tienes en tu poder el Contrato de protección de artículos {{Sic|a}}. Con mucho gusto le devolveré sus artículos de forma gratuita a cambio de ese artículo, si lo desea.
        - ¿UTILIZAR SU CONTRATO DE PROTECCIÓN DE ARTÍCULOS?
          - Sí por favor.
            - (removes=Item Protection Contract) (receives=lost items)
            - Utiliza su Contrato de protección de artículos y recupera sus artículos de forma gratuita.
            - La muerte te ha devuelto tus artículos gratis.<br>Es posible que la muerte no sea tan caritativa la próxima vez, así que entra en situaciones peligrosas bajo tu propia responsabilidad.
          - Esta vez no, gracias.
            - (continue)
      - ((Reclaim Items interface opens.))
    - Pregunta por otra cosa.
      - ((Continues with Soul Reaper dialogue.))

### Soul Reaper tasks


#### Si hay menos de 60, las asignaciones de combate y de grupo están deshabilitadas

- **Muerte:** Aún no es tu momento, Player. ¿Qué requieres de mí?
- '''Selecciona una opción
  - ¿Hay algo en lo que pueda ayudar?
    - **Muerte:** Quizás puedas serme útil con el tiempo. Vuelve a mí cuando tengas más experiencia en lidiar con la muerte.
  - Me gustaría cambiar la configuración de mi botín.
    - *(Abre Death's Store y la interfaz de configuración de Slayer)*

#### Primera tarea

- **Muerte:** Bienvenido, Player.
- **Player:** ¿Estoy muerto? ¿Qué está pasando aquí?
- **Muerte:** No estás muerto... todavía. Te he permitido entrar porque necesito tu ayuda con una tarea.
- **Muerte:** Como sin duda sabrás, soy la Muerte. El Segador, el Recolector de Almas o cualquier otro nombre que me hayan dado las civilizaciones. Mi tarea es recuperar el alma de una criatura moribunda, permitiendo su paso al inframundo.
- **Player:** Entonces, ¿para qué me necesitas?
- **Muerte:** Hay un desequilibrio en la armonía entre la vida y la muerte. <br>Hay demasiada... vida.
- **Muerte:** Mis ojos han estado puestos en ti en esta época, Player, al igual que los ojos de muchos otros. Pareces tener las habilidades que necesito para lograr el equilibrio.
- **Player:** ¿Entonces quieres que mate cosas?
- **Muerte:** Si quieres decirlo de forma tan poco delicada, sí.
- **Player:** ¡Genial! ¿Cuándo empiezo?
- **Muerte:** Inmediatamente. Primero, debes tomar esta gema. Le permitirá ponerse en contacto conmigo de forma remota, en caso de que necesite ayuda o una nueva asignación.
- [Recibes una joya sombría.]
- **Muerte:** Antes de recibir tu primera tarea, ¿estás dispuesto a enfrentarte a criaturas en grupo o prefieres matarlas solo? Puede cambiar de opinión más adelante, si lo desea.
- '''¿Permitir que se asignen jefes de grupo?
  - Sí, estoy feliz de recibir jefes de grupo.
    - (continue)
  - No, no quiero tener que formar equipo con otros aventureros.
    - (continue)
- **Muerte:** Y una última cosa. ¿Estás contento de enfrentarte a criaturas que no son de combate y tienen habilidades, o prefieres usar el combate únicamente? Puede cambiar de opinión más adelante, si lo desea.
- '''¿Permitir que se asignen jefes con habilidades?
  - Sí, estoy feliz de recibir jefes de habilidades.
    - (continue)
  - No, no quiero tener que encontrarme con jefes expertos.
    - (continue)
- Si deseas cambiar de opinión acerca de que te asignen jefes de grupo o jefes de habilidades, puedes hacerlo en la pestaña "Opciones" en la tienda de Death. Sólo puedes hacer esto entre tareas.
- **Muerte:** Ahora para tu primera tarea. Espero que estés listo.
- **Muerte:** Necesito que recolectes almas <number> de la siguiente batalla: [Boss name]. ¿Puedo confiarte esta tarea?
- Tienes una nueva tarea de reaper: <number> x [Boss name].
- '''Selecciona una opción
  - Ciertamente puedes. ¡Gracias!
    - (end)
  - Me gustaría una tarea diferente.{{anchor|different-assignment}}
    - *En el primer intento de repetición:*
      - **Muerte:** Seré paciente contigo una vez, sin penalización. ¿Quieres que te asigne una nueva criatura?
        - Sí, elimina mi asignación actual y dame una nueva.
          - **Muerte:** Necesito que recolectes X almas de la siguiente batalla: [Boss name]. ¿Puedo confiarte esta tarea?
            - Ciertamente puedes. ¡Gracias!
              - (end)
            - Me gustaría una tarea diferente.
              - (above|different-assignment)
            - Necesito algunas pistas sobre mi tarea.
              - *(Igual que a continuación)*
        - No, he cambiado de opinión. Deja mi tarea.
    - *En el segundo intento de repetición:*
      - **Muerte:** No creas que te permitiré cambiar de opinión libremente. Si solicitas una tarea diferente hoy, solo recibirás el 75% de los puntos Reaper por completarla. Sin embargo, obtendrás la experiencia completa.
        - *(Igual que arriba)*
    - *En el tercer intento de repetición:*
      - **Muerte:** No creas que te permitiré cambiar de opinión libremente. Si solicitas una tarea diferente hoy, solo recibirás el 50% de los puntos Reaper por completarla. Sin embargo, obtendrás la experiencia completa.
        - *(Igual que arriba)*
    - *En el cuarto intento de repetición:*
      - **Muerte:** No creas que te permitiré cambiar de opinión libremente. Si solicitas una tarea diferente hoy, solo recibirás el 25 % de los puntos Reaper por completarla. Sin embargo, obtendrás la experiencia completa.
        - *(Igual que arriba)*
    - *En el quinto intento de repetición:*
      - **Muerte:** Tu indecisión me resulta tediosa. Si solicitas una tarea diferente nuevamente hoy, no recibirás ningún punto Reaper por completarla. No puedo evitar que recibas la experiencia completa... desafortunadamente.
        - *(Igual que arriba)*
    - *En el sexto intento de repetición:*
      - **Muerte:** Mi paciencia sólo llega hasta cierto punto. Ya me has hecho perder suficiente tiempo; debo abordar este desequilibrio yo mismo. Vete, mortal.
  - Necesito algunas pistas sobre mi tarea.
    - [sugerencia de tarea]

#### Tarea posterior

- *Si aún tienes que completar la tarea asignada actualmente*
  - **Muerte:** Estás tardando mucho en completar mi tarea, Player. ¿Te resulta demasiado difícil?
  - Si elige restablecer su tarea, esta será tratada como una tarea completamente nueva, con nuevas repeticiones. No hay garantía de que la nueva asignación sea diferente a la actual. Si deseas volver a realizar tu tarea actual, usa tu gema sombría.
    - Me gustaría una nueva tarea.
      - *(Igual que arriba)*
    - Me gustaría otra joya sombría.
      - Recibes una joya sombría.
        - Me gustaría una tarea diferente.
          - *(Igual que arriba)*
        - ¿Hay alguna recompensa por esto?
          - *(Igual que a continuación)*
        - Necesito algunas pistas sobre mi tarea.
          - *(Igual que arriba)*
        - ¿Estoy muerto? ¿Qué quieres de mí?
          - *(Igual que a continuación)*
    - ¿Hay alguna recompensa por esto?
      - *(Se abre la interfaz de la Tienda de la Muerte)*
    - Necesito algunas pistas sobre mi tarea.
      - *(Igual que arriba)*
    - ¿Estoy muerto? ¿Qué quieres de mí?
      - *(Igual que arriba)*
- *Si has completado una tarea hoy*
  - **Muerte:** El desequilibrio ha sido corregido para hoy; tu tarea está hecha. Visíteme mañana para obtener más instrucciones.

### Overcharging the ring of death

- **Muerte:** Puedo ayudarte pero tendrá un costo.
- **Muerte:** Para sobrecargar tu anillo necesitaré 25 corazones de piedra negra y 5 ónices tallados.
*Si el anillo de la muerte no está en el inventario*
- **Muerte:** No tienes un anillo para que te cobre de más.

### Activating the grim gem

- **Muerte:** ¿Qué es mortal? El tiempo corre.
  - **Player:** ¿Cómo me va hasta ahora?
    - **Muerte:** Te he solicitado que recolectes almas de lo siguiente: [Boss name]. Necesito X más antes de completar tu tarea.
      - *(Muestra otras opciones)*
  - **Player:** ¿Puedes darme alguna pista?
    - [sugerencia de tarea]
  - **Player:** ¿Qué quieres de mí?
    - **Muerte:** Como sin duda sabrás, soy la Muerte. El Segador, el Recolector de Almas o cualquier otro nombre que me hayan dado las civilizaciones. Mi tarea es recuperar el alma de una criatura moribunda, permitiendo su paso al inframundo.
    - **Player:** Entonces, ¿para qué me necesitas?
    - **Muerte:** Hay un desequilibrio en la armonía entre la vida y la muerte. Hay demasiada... vida. Mis ojos han estado puestos en ti en esta época, Player, al igual que los ojos de muchos otros. Pareces tener las habilidades que necesito para lograr el equilibrio.
    - **Player:** ¿Entonces quieres que mate cosas?
    - **Muerte:** Si quieres decirlo de forma tan poco delicada, sí.
    - **Player:** ¡Genial! ¿Cuándo empiezo?
    - **Muerte:** Inmediatamente. Ya te he encargado que recolectes almas de la siguiente batalla: [Boss name]. Aún tienes que traerme X almas.
  - **Player:** ¿Dónde estás?
    - **Muerte:** Puedes encontrarme en mi oficina, un portal al que se puede acceder al sur de Draynor Manor.
      - *(Muestra otras opciones)*
  - **Player:** Nada, gracias.

### 2015 Halloween event

*Después de Desaparecer, Presunta Muerte*
- **Muerte:** Ah, mi salvador me honra con su presencia una vez más.
*Antes de desaparecer, presunta muerte*
- **Muerte:** Saludos, mortal. Un asunto de gran urgencia requiere su atención.
- **Player:** ¿Qué está pasando?
- **Muerte:** Más allá de esta grieta, Icthlarin y Amascut luchan sobre el río Noumenon, frente a las puertas del inframundo. Están compitiendo por el control del único cruce entre las tierras de los vivos y los muertos. Si Amascut tiene éxito, puede ser el fin del más allá tal como lo conocemos. Su poder crecerá exponencialmente. Icthlarin necesita tu ayuda Player. Entra en la grieta. Ayúdalo en su lucha contra El Devorador.
- **Player:**
  - **¿Quiénes son Icthlarin y Amascut?**
    - **Muerte:** Icthlarin es el dios del Inframundo, y no solo eso, es mi amigo. Durante milenios ha llevado la carga de proteger a las almas en su viaje al más allá. Amascut es su hermana. Una vez estuvo junto a su hermano, ofreciendo a las almas más grandes la oportunidad de reencarnar. Pero desde entonces ha caído en la locura. Devorar esas mismas almas es ahora lo que la motiva. Ella de quien Icthlarin debe proteger a estas almas indefensas. Él es la luz que los guarda de sus bestias devoradoras.
    - **Player:** ¿Vendrás a ayudar también?
    - **Muerte:** Debo quedarme aquí para proteger la grieta, Player. Temo que nuestro viejo amigo Nomad intente entrar y obtener el poder de las almas para sí mismo. Está tramando algo siniestro. Estoy seguro de ello.
  - **¿Qué provocó que comenzara esta batalla?**
    - **Muerte:** Cuando el devorador de mundos, Tuska, se estrelló contra este planeta, no murió por completo. Curiosamente, su ánima permanece encerrada en su cuerpo sin vida, filtrándose gradualmente hacia Gielinor. Una investigación más profunda de la cáscara reveló que también se están escapando almas. Almas que no son de este mundo. Mientras the beast consumía otros mundos, ella también consumía sus inframundos y las almas dentro de ellos. Estas almas permanecieron dentro de ella hasta ahora. Se están filtrando y desbordando el inframundo de Gielinor.
    - **Player:** ¿Por qué eso ha provocado una batalla entre Icthlarin y Amascut?
    - **Muerte:** Amascut ha aprovechado su oportunidad para atacar mientras el Inframundo está en desorden. Hay una gran cantidad de almas para que ella devore. Icthlarin está disperso... no puede protegerlos a todos. Amascut obtiene poder de las almas que devora, Player. Si no la detienen, no se sabe qué tan fuerte se volverá.
  - **¿Cómo puedo ayudar?**
    - **Muerte:** Pasa por la grieta, mortal. Tenga cuidado: puede experimentar algunas náuseas, pero esto es perfectamente normal para un ser humano. Pronto pasará. Una vez al otro lado te encontrarás al borde del Reino de los Vivos, a orillas del río Noumenon. Busque los diversos habitantes de esta zona. Son un... grupo extraño, pero te instruirán bien. Creo que Icthlarin ha asignado a Ka, un gato que habla, a la grieta. Ella podrá ayudarte a tu llegada.
  - **¿Qué recibiré a cambio?**
    - **Muerte:** Es una pena que los aventureros siempre estén tan concentrados en el beneficio personal, pero les agradará saber que serán bien compensados. Mientras reúne almas en el río Noumenon, notará que hay algunas que se destacan del resto. Estas son las almas que alguna vez tuvieron una posibilidad de reencarnación. Coleccionarlos te recompensará con experiencia en la habilidad en la que se especializaron durante sus vidas. Hoy he notado que estas almas son *las cinco almas especiales del día*. También obtendrá Noumenon Favor por su contribución a los esfuerzos de Icthlarin, que puede canjearse por recompensas en Sinn Derkwill al otro lado de la grieta.
  - **Adiós.**

### 2018 Halloween event

*Antes de completar el tutorial*
- **Muerte:** [Player], ven aquí y habla conmigo antes de continuar.
*Antes del tutorial.*
- **Muerte:** ¿Sientes eso? Esa fuerza que viene de la grieta... Una energía que se siente antigua. Incluso para mí.
- **Player:** ¿Qué es?
- **Muerte:** Yo... no tengo idea. Pero sea lo que sea, me siento obligado a detenerlo. ¿Estarías dispuesto a ayudarme?
  - *Si se selecciona sí* **Player:** ¿Qué quieres que haga?
  - *Si se selecciona no* **Muerte:** Una lástima. Gielinor puede estar en juego aquí; Si lo reconsideras, con gusto aceptaré tu ayuda.
- **Muerte:** Esta energía se está desgarrando desde lo más profundo de la superficie de Gielinor. Necesitamos romper la brecha para asegurarnos de que lo que sea que esté detrás de ella no pueda escapar.
- **Player:** ¿Qué tiene que ver Moia con la grieta?
- **Muerte:** No lo sé, pero temo que la estén utilizando como conducto; su naturaleza única de mitad mahjarrat y mitad humana puede hacerla maleable a esta energía. Manipula su poder para acercarse.
- **Player:** ¿Entonces estás aquí para reclamar Moia? ¿No cerraría eso la brecha?
- **Muerte:** Puede ser, pero dime, ¿es esa realmente la solución que crees que debemos seguir?
  - *Si se selecciona sí*
    - **Muerte:** Interesante. Esperaba una respuesta más heroica de tu parte, [player]. ¿Sientes la necesidad de hablar con alguien al respecto?
    - **Player:** En realidad, eso sería bastante bueno. Resulta que vivir aventuras no es sólo hacer pasteles y salvar gatos desaparecidos. Recientemente he estado teniendo este sueño.
    - **Muerte:** No me estaba sugiriendo.
    - **Player:** Oh.
  - *Si se selecciona no*
    - **Player:** En realidad no quise decir que la matemos. Sólo lo estaba sugiriendo como una idea. ¿Qué dice eso? 'Ninguna idea es una mala idea'
    - **Muerte:** Esa fue una mala idea.
  - **Muerte:** De todos modos, todavía no es el momento de Moia. Todavía hay más en su historia.
  - **Player:** ¿Qué sugerirías que hiciéramos en su lugar?
  - **Muerte:** La grieta es una apertura que conduce a la fuente de este poder. He creado algunos pilares que pueden usarse para interrumpir la brecha. Si pudieras usar tus habilidades para asegurarte de que sigan funcionando, entonces nos permitirá entrar a la grieta por un corto período de tiempo. Una vez que ingreses a la grieta, busca dentro y encuentra una manera de romper la fuente.
  - **Player:** Parece un trabajo bastante fácil para World Guardian.
  - **Muerte:** No es tan simple: hay monstruos que escapan. Intentarán impedir que estabilices la grieta, por lo que tendrás que lidiar con ellos también. Sin embargo, me temo que ni siquiera esto será suficiente. Nunca quise hacer esto, pero temo tener que pedir ayuda a mis... compañeros de trabajo es probablemente la palabra más humana para describirlos.
  - **Player:** ¿Te refieres a los otros Guardianes de Guthix?
  - **Muerte:** Ah, si fuera así de simple. No, pero lo entenderás con el tiempo. Te mostraré todo lo que necesitas saber para ayudarme a estabilizar la energía proveniente de la grieta.
*Durante el tutorial*
- **Muerte:** Me alegra que hayas aceptado ayudar, [player]. Les informaré sobre mi plan para estabilizar esta grieta para que podamos volver a nuestras actividades diarias. He construido 5 pilares alrededor de la grieta para ayudar a estabilizar la energía que viene desde dentro. A cada uno de los pilares se le asignará una habilidad de forma aleatoria. Podrás entrenar: Prayer, Runecrafting, Divination, Magic, Crafting, Summoning, Smithing y Invention. Lidiar con los obstáculos te recompensará con la experiencia Slayer. Si no deseas ganar experiencia de combate, puedes hablar conmigo para activar o desactivar la ganancia de experiencia para todas las habilidades de combate.
- **Muerte:** Estabilizarte en un pilar aumentará los multiplicadores de XP en los otros pilares, lo que te animará a moverte entre ellos para obtener una experiencia óptima. Hay cinco etapas multiplicadoras, que se destacan por diferentes cantidades de energía que aumentan en intensidad a medida que se sube. A medida que trabajes en el pilar, progresarás lentamente hacia la estabilización de la grieta. Tu progreso puede verse a través de la energía que se dirige desde los pilares hacia el centro. Cuanto más se estabilice, más crecerá la intensidad del haz. Una vez que llegue a la grieta, la habrás estabilizado por completo.
- **Muerte:** Usar un fragmento contaminado te permitirá elegir entre duplicar la experiencia obtenida O reducir a la mitad el tiempo que te lleva estabilizar una grieta. Y esos son los conceptos básicos. Es hora de que nos pongamos a trabajar [player].

### City of Um


#### Antes de haber completado Rune Mythos o después de haber completado Vessel of the Harbinger

- **Player:** Quería preguntarte, pero ¿dónde estamos?
- **Muerte:** Eh.
- **Player:** ¿No lo sabes? Porque sonó como si lo hicieras.
- **Muerte:** Lo sé. Esta es Um.
- **Player:** ¿Lo has olvidado?
- **Muerte:** No. Este es Um. El nombre de esta ciudad es Um.
- **Player:** ...
- **Player:** Porque está bien si lo has olvidado.
- **Muerte:** ¡No lo he olvidado!
- **Muerte:** Escucha mis palabras: Um es el nombre de esta ciudad. ¡Este es el City of Um!
- **Muerte:** 'U' grande, 'm' pequeña: Um.
- **Player:** ¿Eh?
- **Muerte:** ¡Um!
- **Player:** Mmm... Mmm, um, um...
- **Muerte:** Si estabas pensando en contar algún chiste irónico, no lo hagas. NO estoy de humor.
- **Player:** Bien, enfoque diferente. ¿QUÉ es este lugar?
- **Muerte:** Son muchas cosas para muchas personas. Una ciudad para los muertos; una necrópolis; una estación de paso; una sala de espera...
- **Muerte:** Todos los que mueren pasan por ella. La mayoría sabe adónde van, por lo que rápidamente se dirigen río abajo hasta el puente y hacia su otra vida.
- **Muerte:** Pero algunos no están listos, no lo saben o simplemente están esperando que sus seres queridos se unan a ellos en la muerte. Para ellos, este es su hogar.
- **Muerte:** Y aquí esperan, en una ciudad construida a partir de los recuerdos de los muertos que la habitan.
- **Player:** Espera, ¿está construido a partir de recuerdos, pero ni siquiera puedes recordar cómo se llama? Qué irónico.
- **Muerte:** *mira fijamente tu alma*
- **Player:** ¡Estoy bromeando! Lo siento...

#### Después de haber completado Rune Mythos y antes de haber completado Vessel of the Harbinger

- (ver | Vaso del Heraldo)

### Death's office


#### Habla con

- (Condition: If the player has an active task from another day:)
  - **Muerte:** Estás tardando mucho en completar mi tarea, Player. ¿Te resulta demasiado difícil?
  - Si elige restablecer su tarea, esta será tratada como una tarea completamente nueva, con nuevas repeticiones. No hay garantía de que la nueva asignación sea diferente a la actual. Si deseas volver a realizar tu tarea actual, usa tu gema sombría en su lugar.
  - (continue)
- (Condition: Without an active task from another day:)
  - **Muerte:** ¿Qué te trae a mi reino?
  - (continue)
- [Menu]: Selecciona una opción
  - {{anchor|needassign}} [Elección]: Necesito una tarea.|cond=Sin una tarea activa:
    - (Condition: If the player has not previously completed today's task:)
      - {{anchor|assign}} (Condición: Por casualidad con la elección de Reaper desbloqueada o durante ciertos eventos :)
        - ((Se abre una interfaz titulada 'SELECCIONAR TAREA', que muestra una lista de todos los jefes.)) <!-- are group/skilling bosses greyed out if not enabled? -->
          - [Choice]: [Boss]
            - (continue)
    - (Condition: If the player has already completed today's task, but has not unlocked 'Additional tasks':)
      - {{transcript missing}}
    - (Condition: If the player has already completed today's task and has unlocked 'Additional tasks':)
      - **Muerte:** Has hecho lo que te pedí hoy, pero todavía hay un desequilibrio que abordar.
      - (Condition: Without 250 slayer points:)
        - **Muerte:** Te daría otra tarea, pero a cambio pido 250 puntos de cazador. No tienes lo que busco.
      - (Condition: With 250 slayer points:)
        - **Muerte:** Te daré otra tarea, pero a cambio necesitaré 250 puntos de cazador.
        - [Menu]: Selecciona una opción
          - [Choice]: Sí, me gustaría comprar otra tarea por 250 puntos de cazador.
            - Intercambias 250 puntos de cazador por una tarea de segador adicional.
            - (continue)
          - [Choice]: No, gracias.
            - (end)
    - **Muerte:** Necesito que recolectes almas [número] de la siguiente batalla: [Boss]. ¿Puedo confiarte esta tarea?
    - Tienes una nueva tarea de reaper: [número] x [Boss].
    - [Menu]: Selecciona una opción
      - [Choice]: Ciertamente puedes. ¡Gracias!
        - (end)
      - [Choice]: Me gustaría una tarea diferente.
        - (below|newassign)
      - [Choice]: Necesito algunas pistas sobre mi tarea.
        - (abajo)
  - {{anchor|newassign}} [Elección]: Me gustaría una nueva tarea.|cond=Con una tarea activa:
    - (Condition: First time rerolling an assignment today:)
      - **Muerte:** Seré paciente contigo una vez, sin penalización. ¿Quieres que te asigne una nueva criatura?
        - [Menu]: Selecciona una opción
          - [Choice]: Sí, elimina mi asignación actual y dame una nueva.
            - (above|assign)
          - [Choice]: No, he cambiado de opinión. Deja mi tarea.
            - (end)
    - (Condition: Second time rerolling an assignment today:)
      - **Muerte:** No creas que te permitiré cambiar de opinión libremente. Si solicitas una tarea diferente hoy, solo recibirás el 75% de los puntos Reaper por completarla. Sin embargo, obtendrás la experiencia completa.
      - {{anchor|reroll2}} [Menú]: seleccione una opción
        - [Choice]: Entiendo, elimina mi asignación actual y dame una nueva.
          - (above|assign)
        - [Choice]: No, he cambiado de opinión. Deja mi tarea.
          - (end)
    - (Condition: Third time rerolling an assignment today:)
      - **Muerte:** No creas que te permitiré cambiar de opinión libremente. Si solicitas una tarea diferente hoy, solo recibirás el 50% de los puntos Reaper por completarla. Sin embargo, obtendrás la experiencia completa.
      - (continuea|reroll2)
    - (Condition: Fourth time rerolling an assigment today:)
      - **Muerte:** No creas que te permitiré cambiar de opinión libremente. Si solicitas una tarea diferente hoy, solo recibirás el 25 % de los puntos Reaper por completarla. Sin embargo, obtendrás la experiencia completa.
      - (continuea|reroll2)
    - (Condition: Fifth time rerolling an assignment today:)
      - **Muerte:** Tu indecisión me resulta tediosa. Si solicita una tarea diferente nuevamente hoy, no recibirá puntos reaper por completarla. No puedo evitar que recibas la experiencia completa... desafortunadamente.
      - (continuea|reroll2)
    - (Condition: After the fifth reroll today:)
      - **Muerte:** Mi paciencia sólo llega hasta cierto punto. Ya me has hecho perder suficiente tiempo; debo abordar este desequilibrio yo mismo. Vete, mortal.
  - [Choice]: ¿Hay alguna recompensa por esto?
    - (opens=Death's Store)
  - [Choice]: ¿Estoy muerto? ¿Qué quieres de mí?
    - **Muerte:** No estás muerto... todavía. Te he permitido entrar porque necesito tu ayuda con una tarea.
    - **Muerte:** Como sin duda sabrás, soy la Muerte. El Segador, el Recolector de Almas o cualquier otro nombre que me hayan dado las civilizaciones. Mi tarea es recuperar el alma de una criatura moribunda, permitiendo su paso al inframundo.
    - **Player:** Entonces, ¿para qué me necesitas?
    - **Muerte:** Hay un desequilibrio en la armonía entre la vida y la muerte. Hay demasiada... vida.
    - **Muerte:** Mis ojos han estado puestos en ti en esta época, Player, al igual que los ojos de muchos otros. Pareces tener las habilidades que necesito para lograr el equilibrio.
    - **Player:** ¿Entonces quieres que mate cosas?
    - **Muerte:** Si quieres decirlo de forma tan poco delicada, sí.
    - **Player:** ¡Genial! ¿Cuándo empiezo?
    - (Condition: With an active assignemt:)
      - **Muerte:** Inmediatamente. Ya te he encargado que recolectes almas de la siguiente batalla: [Boss]. Todavía tienes que traerme almas [número]. <!-- still plural with 1 soul left? -->
    - (Condition: Without an active assignment:)
      - (above|needasssign)
  - [Choice]: Me gustaría otra joya sombría.
    - (receives=Grim gem)
    - [pic=Joya sombría detail.png]
    - (otro) <!-- not quite right, shows: 'different assigmment; any rewards?; hints; AmIdead?; That's all, thanks; -->
  - [Choice]: Más opciones.
    - [Choice]: ¿Puedes ayudarme a cobrar de más este anillo? <!-- does this only appear after unlocking the ability from Death's Store? -->
      - **Muerte:** Puedo ayudarte pero tendrá un costo.
      - **Muerte:** Para sobrecargar tu anillo necesitaré 25 corazones de piedra negra y 5 ónices tallados.
      - [Menu]: ¿Estás seguro de que quieres hacer esto?
      - [Choice]: si
        - (Condition: Without carrying a ring of death:)
          - **Muerte:** No tienes un anillo para que te cobre de más.
        - (Condition: With a ring of death, but without all ingredients:)
          - {{transcript missing}}
        - (Condition: With a ring of death and all ingredients:)
          - {{transcript missing}}
      - [Choice]: No
        - (end)
    - [Choice]: Me gustaría hablar sobre Nomad y el inframundo.
      - {{transcript missing}}
    - [Choice]: I need some hints about my assignment.|cond=Con una tarea activa:
    - [Choice]: Más opciones.
      - (previous)
    - [Choice]: Eso es todo, gracias.
      - (end)

#### Obtener tarea

- (Condition: If the player has an active task from another day:)
  - Si elige restablecer su tarea, esta será tratada como una tarea completamente nueva, con nuevas repeticiones. No hay garantía de que la nueva asignación sea diferente a la actual. Si deseas volver a realizar tu tarea actual, usa tu gema sombría en su lugar.
  - [Menu]: Selecciona una opción
    - [Choice]: Me gustaría una nueva tarea.
      - (arriba)
    - [Choice]: Me gustaría otra joya sombría.
      - (arriba)
    - [Choice]: ¿Hay alguna recompensa por esto?
      - (arriba)
    - [Choice]: Necesito algunas pistas sobre mi tarea.
      - (arriba)
    - [Choice]: ¿Estoy muerto? ¿Qué quieres de mí?
      - (arriba)
- (Condition: Without an active task from another day:)
  - {{transcript missing}}

#### Recompensas

- (opens=Death's Store)

#### Reclamar artículos


##### Con artículos para reclamar

- (above|reclaim-items)

##### Sin artículos para reclamar

- **Muerte:** No tienes nada que reclamar, Player.

#### Evento de muerte

- (Condition: If you have no additional death events unlocked:)
  - Actualmente no tienes eventos de muerte adicionales desbloqueados.
- (Condition: If you have at least one additional death event unlocked:)
  - {{Transcript missing}}
