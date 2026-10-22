# Thok of Daemonheim

- **Original Wiki Page**: [Transcript:Thok of Daemonheim](https://runescape.wiki/w/Transcript%3AThok%20of%20Daemonheim)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|missing dialogue to claim Daemonheim aura 4 for first time, skillcape dialogue is also outdated}}

### On Daemonheim Peninsula


#### Diálogo estándar

- **Thok of Daemonheim:** ¿Qué quieres con Thok?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué es este lugar?
    - **Player:** ¿Qué es este lugar?
    - **Thok of Daemonheim:** Este es el campamento. Aquí los guerreros descansan y se preparan para el ataque.
    - **Thok of Daemonheim:** Thok espera aquí para recompensar a aquellos que sobrevivan a Daemonheim, quienes muestran un poder tan grande como el de Thok.
    - [Menu]: Selecciona una opción
      - [Choice]: Daemonheim?
        - **Player:** Daemonheim?
        - **Thok of Daemonheim:** Significa Salas de Demonios. Name no está del todo bien, ya que hay cosas peores que los demonios en Daemonheim. Es menos una sala y más un foso también. Algunos dicen que no tiene fin, pero Thok lo sabe mejor.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Qué es este lugar?
            - (above|what-is-this-place)
          - [Choice]: ¿Qué puedo hacer aquí?
            - (below|what-can-i-do-here)
          - [Choice]: cond=If the player does not have 99 Dungeoneering|¿Qué es esa capa a tu lado?
            - (below|what-is-cape)
          - [Choice]: cond=If the player has 99 Dungeoneering|¿Puedo comprar un Skillcape de Dungeoneering?
            - (below|can-buy-cape)
      - [Choice]: ¿Qué puedo hacer aquí?
        - (below|what-can-i-do-here)
      - [Choice]: cond=If the player does not have 99 Dungeoneering|¿Qué es esa capa a tu lado?
        - (below|what-is-cape)
      - [Choice]: cond=If the player has 99 Dungeoneering|¿Puedo comprar un Skillcape de Dungeoneering?
        - (below|can-buy-cape)
  - [Choice]: ¿Qué puedo hacer aquí?
    - **Player:** ¿Qué puedo hacer aquí?
    - **Thok of Daemonheim:** El camino ascendente es Daemonheim. Contiene más tesoro del que Thok puede guardar en sus bolsillos, lo cual es una suerte para ti, pero está custodiado por innumerables monstruos, lo cual es una mala suerte para ti. Los principiantes deben hablar con el tutor antes de entrar al castillo.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué es este lugar?
        - (above|what-is-this-place)
      - [Choice]: cond=If the player does not have 99 Dungeoneering|¿Qué es esa capa a tu lado?
        - (below|what-is-cape)
      - [Choice]: cond=If the player has 99 Dungeoneering|¿Puedo comprar un Skillcape de Dungeoneering?
        - (below|can-buy-cape)
  - [Choice]: cond=If the player does not have 99 Dungeoneering|¿Qué es esa capa a tu lado?
    - **Player:** ¿Qué es esa capa a tu lado?
    - **Thok of Daemonheim:** Ah, este Dungeoneering skillcape. Marca al portador como un verdadero maestro de Demon Halls.
    - **Thok of Daemonheim:** Aunque Thok ha estado muy metido en Daemonheim, nadie le cree. Entonces, Thok debe proteger skillcape y ofrecerlo a los valientes guerreros que encuentren el fondo de este lugar.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué es este lugar?
        - (above|what-is-this-place)
      - [Choice]: ¿Qué puedo hacer aquí?
        - (above|what-can-i-do-here)
      - [Choice]: Daemonheim?
        - (above|daemonheim)
  - [Choice]: cond=If the player has 99 Dungeoneering|¿Puedo comprar un Skillcape de Dungeoneering?
    - **Player:** ¿Puedo comprar un Skillcape o un Dungeoneering?
    - (Condition: If the player has 99–119 Dungeoneering:)
      - **Thok of Daemonheim:** Bueno, dilo bien. Eres un gran guerrero y Thok te brindará una bebida esta tarde.
      - **Thok of Daemonheim:** Sin embargo, Thok debe pedir 99.000 coins para materiales.
      - (Condition: If the player has an inverted skillcape token:)
        - **Thok of Daemonheim:** ¡Mira que tienes una moneda de inversión! Thok tomará eso y le ofrecerá una capa de diferentes colores.
        - (removes=any inverted skillcape tokens and inverted master skillcape tokens)
      - [Menu]: Elige una opción:
        - [Choice]: ¿99.000 coins? Eso es demasiado caro.
          - **Player:** ¿99.000 coins? Eso es demasiado caro.
          - **Thok of Daemonheim:** En absoluto; ¡Hay muchos otros aventureros a quienes les encantaría tener la oportunidad de comprar un artículo tan prestigioso! Puedes encontrarme aquí si cambias de opinión.
        - [Choice]: De hecho, creo que tengo el dinero aquí.
          - **Player:** Creo que tengo el dinero aquí, de hecho.
          - (Se toman 99.000 coins de el player a cambio de la capa Dungeoneering).
          - **Thok of Daemonheim:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
    - ((If the player has 120 Dungeoneering:))
      - **Thok of Daemonheim:** Creo que me impresionó. Para ser un verdadero maestro de la habilidad tienes opción a dos skillcapes.
      - [Menu]: Elige una opción:
        - [Choice]: Compra el nivel 99 skillcape.
          - **Thok of Daemonheim:** Sin embargo, Thok debe pedir 99.000 coins para materiales.
          - [Menu]: Elige una opción:
            - [Choice]: ¿99.000 coins? Eso es demasiado caro.
              - (arriba)
            - [Choice]: De hecho, creo que tengo el dinero aquí.
              - (arriba)
            - [Choice]: I'd like a skillcape with the colours inverted.|cond=Si el player le ha dado a Thok un token inverted skillcape:
              - {{tmissing}}
            - [Choice]: He dominado esta habilidad. ¿Hay algo más?
              - **Thok of Daemonheim:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
              - **Thok of Daemonheim:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
              - **Thok of Daemonheim:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo...
              - **Thok of Daemonheim:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle un Dungeoneering master cape.
              - [Menu]: ¿Comprar Dungeoneering master cape por 120.000 coins?
                - [Choice]: Sí.
                  - (Se toman 120.000 coins de el player a cambio de Dungeoneering master cape.)
                - [Choice]: No.
                  - (end)
            - [Choice]: I'd like a master cape with the colours inverted.|cond=Si el player le ha dado a Thok un token maestro skillcape invertido:
              - {{tmissing}}
        - [Choice]: Compra el nivel 120 skillcape.
          - **Thok of Daemonheim:** Sin embargo, Thok debe pedir 120.000 coins para materiales.
          - (Condition: If the player has an inverted skillcape token:)
            - **Thok of Daemonheim:** ¡Mira que tienes una moneda de inversión! Thok tomará eso y le ofrecerá una capa de diferentes colores.
            - (removes=any inverted skillcape tokens and inverted master skillcape tokens)
          - [Menu]: Elige una opción:
            - [Choice]: No, eso es demasiado.
              - **Player:** No, eso es demasiado.
              - **Thok of Daemonheim:** Thok ofrecería un préstamo, pero gastó todo el dinero en cerveza.
            - [Choice]: Bien, eso parece razonable.
              - (Condition: If the player has given Thok an inverted master skillcape token:)
                - [Menu]: Selecciona una opción
                  - [Choice]: Me gustaría un master cape normal.
              - (above|buy-master-cape)
                  - [Choice]: Me gustaría un master cape invertido.
                    - [Menu]: ¿Comprar Dungeoneering master cape por 120.000 coins?
                      - [Choice]: Sí.
                        - (Se toman 120.000 coins de el player a cambio del Dungeoneering master cape invertido).
                      - [Choice]: No.
                        - (end)
              - (above|buy-master-cape)
  - [Choice]: cond=If the player has found all ten Marmaros and Thok Dungeoneering journals|Logré encontrar todas tus cartas.
    - **Player:** Logré encontrar todas tus cartas.
    - **Thok of Daemonheim:** ¡Marm! Marma, despierta. Thok se equivocó: ¡alguien logró encontrar nuestras cartas!
    - **Marmaros, comerciante de recompensas:** W... ¿Qué? ¿Todos ellos? Tú... ¿Sabes que llegamos al fondo de ese lugar?
    - **Player:** Debes haberlo hecho. Las letras llegan hasta los pisos más bajos.
    - **Marmaros, comerciante de recompensas:** ¡No puedo creerlo! ¿Sabes lo que me ha pasado? ¿Por qué tengo problemas para pensar? ¿Por qué ni siquiera puedo dormir por miedo?
    - **Player:** ¿Ninguno de ustedes se acuerda? Tus cartas no son claras, pero fue como si alguien desconectara y drenara a Marmaros de toda esperanza y optimismo. Te volviste suicida y Thok tuvo que evitar que te lastimaras rompiéndote los brazos.
    - **Thok of Daemonheim:** No lo recuerdo en absoluto, pero parece cierto. Thok y Marm no pueden recordar en absoluto lo que pasó al fondo de los pasillos, Player. La memoria es un desastre, como cuando Thok se quedó dormido en un barril de cerveza negra.
    - **Player:** Escribiste que alguien te salvó y te trajo de regreso aquí: un hombre con... barba blanca, creo que dijiste. Supongo que debe haber-
    - **Marmaros, comerciante de recompensas:** ¿Barba blanca? No, no puede ser...
    - **Thok of Daemonheim:** ¡Jaja, mira! Marm debe estar mejorando: ¡está usando la cabeza otra vez!
    - **Player:** ¿Qué es?
    - **Marmaros, comerciante de recompensas:** Yo... No puedo estar seguro, pero podría tener una idea de quién es este hombre de barba blanca. Hay alguien con quien necesito hablar... alguien que tiene mucho que dar explicaciones.
    - **Thok of Daemonheim:** Pero por ahora, Thok tiene trabajo que hacer y no debe agotar a Marm por la emoción. Tienes gracias, Player. Thok cantará tu nombre esta noche al atardecer.
  - [Choice]: cond=If the player has completed Thok It To 'Em|Yo he sido tú.
    - **Player:** Yo he sido tú.
    - **Thok of Daemonheim:** ¿Qué? Confundes a Thok.
    - **Player:** Skaldrun me mostró la historia de cómo te abriste camino a través de las mazmorras para salvar a Marmaros.
    - **Thok of Daemonheim:** Sí, fue una gran aventura.
    - [Menu]: Selecciona una opción
      - [Choice]: cond=After claiming the Hard Daemonheim Task rewards from Talsar|Gracias por enseñarme a dar cabezazos como tú.
        - **Player:** Gracias por enseñarme a dar cabezazos como tú.
        - **Thok of Daemonheim:** De nada. Pero no intentes darle un cabezazo a Thok. Creo que la cabeza es más gruesa que la tuya.
      - [Choice]: cond=Before claiming the Hard Daemonheim Task rewards from Talsar|¿Puedes enseñarme esa habilidad? Ya sabes, ¿ese en el que destruyes al enemigo con tu frente?
        - **Player:** ¿Puedes enseñarme esa habilidad? Ya sabes, ¿ese en el que destruyes al enemigo con tu frente?
        - **Thok of Daemonheim:** Ja, ja, ja. No, personita, sólo Thok tiene la cabeza lo suficientemente gruesa y poderosa para eso.
      - [Choice]: Todo parecía un poco
        - **Player:** Todo parecía un poco. ¿Realmente luchaste contra tantos monstruos jefes?
        - **Thok of Daemonheim:** Thok luchó contra muchos monstruos poderosos y Thok los venció a todos. No te burles de Thok.
        - **Player:** Erm, lo siento.
      - [Choice]: ¿Qué pasó con Mini Marm?
        - **Player:** ¿Qué pasó con Mini Marm?
        - **Thok of Daemonheim:** Mini Marm es un gran y poderoso guerrero cangrejo. Regresó al calabozo para matar muchos monstruos.
        - **Player:** ¿Estará bien?
        - **Thok of Daemonheim:** ¡No temas por Mini Marm, teme por los monstruos que se atreven a interponerse en su camino!
  - [Choice]: Acerca del sistema de tareas...
    - (Condition: If the player has completed the elite Daemonheim achievements and the rewards have not been claimed:)
      - **Player:** He completado todas las tareas Elite del conjunto Daemonheim.
      - **Thok of Daemonheim:** Bien, bien.
      - [Thok te entrega algunas lámparas.]
      - **Thok of Daemonheim:** En Daemonheim creas una segunda piedra de acceso y te teletransportas hasta ella. También en Daemonehim entierras los huesos de los enemigos muertos: obtendrás oración. Además, te permitirá atravesar la barrera mágica en Brimhaven Dungeon: Thok intenta dar cabezazos.
      - **Thok of Daemonheim:** pero ahora comparte el secreto.
      - **Player:** ¡Gracias! ¿Qué más hace?
      - **Thok of Daemonheim:** ¡Por hacer todas las tareas, tu anillo de parentesco mejoró! También Thok convence al contrabandista para que acepte menos dinero para las cosas. Si realmente crees que eres tan bueno como Thok, intenta el modo difícil... pero yo no creo que tu cabeza sea lo suficientemente dura para eso.
      - (continue)
    - [Menu]: Elige una opción:
      - [Choice]: Háblame del Sistema de Logros.
        - **Thok of Daemonheim:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
        - **Thok of Daemonheim:** Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
        - **Thok of Daemonheim:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
        - [Menu]: Elige una opción:
          - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
            - **Player:** Cuéntame sobre la recompensa establecida para esta área.
            - **Thok of Daemonheim:** Si Thok cree que eres lo suficientemente fuerte, obtienes aura.
            - **Thok of Daemonheim:** El aura mejorará si realizas conjuntos de tareas más difíciles.
            - **Thok of Daemonheim:** Cuando obtienes aura, aprendes sobre sus poderes.
            - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
            - (previous2|about-task-system)
          - [Choice]: ¿Cómo reclamo estas recompensas?
            - **Player:** ¿Cómo reclamo las recompensas?
            - **Thok of Daemonheim:** Para obtener una recompensa, debes completar todas las tareas del conjunto y luego recibirás la recompensa.
            - **Thok of Daemonheim:** Algunas de las tareas son simples, otras requieren buenas habilidades y otras necesitan misiones. ¡Thok hizo todas las tareas fácilmente!
            - **Thok of Daemonheim:** Para obtener recompensas brillantes, habla con Drangund, Dungeoneering Tutor, Marmaros the Rewards trader, Talsar o Thok.
            - (previous2|about-task-system)
          - [Choice]: Lo siento, me estaba yendo.
            - (end)
      - [Choice]: Lo siento, me estaba yendo.
        - (end)
  - [Choice]: cond=If the player has 99 Dungeoneering|He notado que hay un par de versiones de cada skillcape.
    - **Thok of Daemonheim:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
    - (Condition: If the player is using the old model:)
      - **Thok of Daemonheim:** Parece que actualmente estás usando el modelo anterior para tu Dungeoneering skillcape. ¿Quieres cambiar a uno más nuevo?
      - (continue)
    - (Condition: If the player is using the new model:)
      - **Thok of Daemonheim:** Aún puedes elegir usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, me gustaría usar la versión [new/old] del skillcape.
        - **Thok of Daemonheim:** ¿Te gustaría usar el modelo [old/newer] solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
        - [Menu]: Selecciona una opción
          - [Choice]: Solo me gustaría cambiar el Dungeoneering skillcape.
            - **Thok of Daemonheim:** No hay problema, ahora utilizarás el modelo [older/newer] para tu Dungeoneering skillcape.
          - [Choice]: Me gustaría cambiar todos mis skillcapes.
            - **Thok of Daemonheim:** ¡No hay problema, ahora usarás el modelo [older/newer] para todos tus skillcapes!
          - [Choice]: ¡He cambiado de opinión!
            - (end)
      - [Choice]: No, gracias.
        - **Thok of Daemonheim:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión [old/new]!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Thok of Daemonheim:** Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas.
          - [Menu]: Selecciona una opción
            - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
              - **Thok of Daemonheim:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
            - [Choice]: No, gracias.
              - (end)

#### Usando Thok on Wood con él

- **Thok of Daemonheim:** ¿Qué quieres con Thok?
- **Player:** Encontré este libro tuyo hurgando en la Rifa de Balthazar, ¡estaba en el fondo de un barril!
- **Thok of Daemonheim:** El libro no se vendió tan bien como Thok quería. Al mostrar un libro a la gente, golpeo a todos los que dicen que el libro es estúpido.
- **Thok of Daemonheim:** Entonces los débiles que cortan árboles con un hacha empiezan a odiar a Thok también. Dicen que tomo todos los árboles para que no tengan nada que cortar. Así que también les golpeo.
- **Thok of Daemonheim:** Después de que Thok golpea a los débiles, las personas verdes que abrazan a los árboles dicen que Thok no piensa en los sentimientos de los árboles. Dicen que a Thok no le importa si un árbol no quiere convertirse en el lugar donde va la cerveza, yo también los golpeo.
- **Thok of Daemonheim:** ¡No es estúpido, eres el rey de hacer cosas con árboles!
- **Player:** ¿Cómo se hace furniture? No veo un banco de trabajo por aquí y me sorprendería mucho que la Agencia de Vivienda le permitiera ser propietario de una casa.
- **Thok of Daemonheim:** Thok levanta un árbol y lo aplasta sobre la rodilla hasta que Thok esté feliz.
- **Player:** No estoy seguro de cómo funciona.
- **Thok of Daemonheim:** Piensa en qué hacer y aplasta la rodilla hasta que esté hecho. No es difícil, sólo hay que encontrar el árbol. Aquí Thok muestra
- **Player:** No, no, Thok, eso no es necesario. Gracias por lo que fue esa conversación.
- **Thok of Daemonheim:** Aunque estoy feliz de ver el libro de nuevo, aunque esta vez no te golpearé.

#### Después del evento navideño de 2010

- (ver|Oh Pequeño Pueblo de Daemonheim#Hablando con Thok, Maestro de Dungeoneering)

#### Player tiene Ferret of Doom como mascota seguidora

- **Thok of Daemonheim:** Creo que no te hablo con eso alrededor.
- **Player:** ¿Con qué alrededor?
- **Thok of Daemonheim:** ...
- **Thok of Daemonheim:** ¡CONDENACIÓN!
- [Thok apenas se atreve a mirar a su hurón mascota.]
- **Player:** Lo entiendo. Volveré una vez que tenga un compañero diferente.

### In Burthorpe Castle during Song of Seren

- **Bueno:** ¡Player! ¡Thok está encantado de verte! Pero Thok está ocupado, muy ocupado observando a todos estos villanos.
- **Thok:** Uno de ellos seguramente hará algo MALVADO y cuando lo haga, Thok les dará una lección.
- **Thok:** ¡Con su PUÑO!

### At War's Retreat (Thok's Smashing Buffs)

- {{Main|Transcript:Thok's Smashing Buffs}}
