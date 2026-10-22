# Orla Fairweather

- **Original Wiki Page**: [Transcript:Orla Fairweather](https://runescape.wiki/w/Transcript%3AOrla%20Fairweather)
- **Letter**: `O`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At the Divination camp


#### Habla con


##### Introducción a Divination


##### Primera vez

- **Player:** ¿Qué está pasando aquí?
- **Orla Fairweather:** ¡Me alegra que hayas preguntado! Soy Orla Fairweather y estos son mis colegas. ¡Somos pioneros en investigar el arte de la adivinación!
- **Player:** ¿Divination? ¿Te refieres a leer hojas de té, fundir huesos y ese tipo de cosas?
- **Orla Fairweather:** ¡Oh, no, esto es mucho más grande! ¡Aquí estamos tratando con la energía del mundo! ¡El destino de Gielinor puede estar determinado por nuestras acciones!
- **Player:** Vaya, eso suena interesante.
- **Orla Fairweather:** Ah, sí. Aún es temprano, pero ya hemos obtenido resultados interesantes.
- (Condition: Before collecting a memory:)
  - **Player:** ¿Puedo empezar a entrenar adivinación yo mismo?
  - (continue)
- (Condition: After collecting a memory:)
  - **Player:** ¿Puedes ayudarme a mejorar mi habilidad en adivinación?
  - (continue)
- **Orla Fairweather:** ¡Por supuesto! ¡Nos vendría bien toda la ayuda que podamos conseguir!
- (Condition: Before collecting a memory:)
  - (continue|before-collecting-a-memory)
- (Condition: After collecting a memory:)
  - (continue|after-collecting-a-memory)
- (Condition: After converting a memory into experience:)
  - (continue|after-convert-memory-into-experience)
- (Condition: After converting a memory into energy:)
  - (continue|after-convert-memory-into-energy)
- (Condition: After converting a memory and energy into experience:)
  - (continue|after-convert-memory-and-energy)

##### Hablando con Orla nuevamente antes de recoger un recuerdo.

- **Orla Fairweather:** ¿Estás listo para empezar?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, muéstrame cómo entrenar la adivinación.
    - {{anchor|before-collecting-a-memory}}**Orla Fairweather:** El primer paso es recopilar un recuerdo. Los fuegos fatuos del sur servirán: mira cómo te va y vuelve a verme si necesitas ayuda.
  - [Choice]: Por el momento no, gracias.
    - (end)

##### Hablando con Orla después de recoger un recuerdo

- **Orla Fairweather:** ¡Creo que estás listo para el siguiente paso! ¿Quieres seguir aprendiendo los métodos de adivinación?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Sí!
    - {{anchor|after-collecting-a-memory}}**Orla Fairweather:** ¡Tienes algunos recuerdos, pero no te sirven de nada así! Necesitas devolverlos a la tierra. ¡Pruébalo!
  - [Choice]: Por el momento no, gracias.
    - (end)

##### Hablando con Orla después de convertir un recuerdo en experiencia

- **Orla Fairweather:** ¡A este paso, superarás mis conocimientos en poco tiempo! ¿Estás listo para seguir aprendiendo?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, por favor.
    - {{anchor|after-convert-memory-into-experience}}**Orla Fairweather:** Como has visto, los recuerdos se pueden convertir en experiencia, pero eso no es todo para lo que se pueden utilizar. Si concentras tu mente, también podrás recibir energía divina, un material útil. ¿Por qué no lo intentas?
  - [Choice]: Por el momento no, gracias.
    - (end)

##### Hablando con Orla después de convertir un recuerdo en recuerdo

- **Orla Fairweather:** ¡No hay tiempo que perder! ¿Estás listo para continuar?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Sí!
    - {{anchor|after-convert-memory-into-energy}}**Orla Fairweather:** Si te sobra energía divina, puedes usarla a tu favor. Simplemente concentre su mente en una experiencia mejorada y obtendrá más beneficios de sus recuerdos.
  - [Choice]: Por el momento no, gracias.
    - (end)

##### Después de la introducción a Divination

- {{anchor|after-convert-memory-and-energy}}**Orla Fairweather:** Parece que estás al día de mis descubrimientos. Sin embargo, Faizan está logrando avances con energía divina; deberías hablar con él.
- [Menu]: Selecciona una opción
  - [Choice]: Bien, hablaré con Faizan.
    - (end)
  - [Choice]: ¿Cómo puedo coleccionar recuerdos? {{anchor|how-to-collect-memories}}
    - (Condition: If the player is below level 10 Divination:)
      - **Orla Fairweather:** Primero, necesitas localizar una mecha. Los mechones ideales para ti están aquí, justo al sur del campamento. A medida que te vuelvas más hábil en la adivinación, deberás pasar a mechones más complejos.
      - (continue|how-to-collect-memories-2)
    - (Condition: If the player is level 10 Divination or higher:)
      - **Orla Fairweather:** Primero, necesitas localizar una mecha. Ya tienes cierta habilidad en adivinación, por lo que sería mejor que encontraras una colonia más compleja que la que tenemos aquí.
      - (continue|how-to-collect-memories-2)
    - **Orla Fairweather:{{anchor|how-to-collect-memories-2}}** Puedes usar el mapa a mi lado para saber dónde se encuentran los mechones más adecuados para ti.
    - **Orla Fairweather:** ¡Interactúa con una brizna para transformarla en un manantial y cosechar recuerdos de ella!
    - **Orla Fairweather:** También obtendrás una pequeña cantidad de energía divina. ¡Aférrate a eso, se puede usar más tarde!
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Cómo puedo convertir recuerdos?
        - (below|how-to-convert-memories)
      - {{anchor|enriched-memories}}¿Qué son los recuerdos enriquecidos?
        - **Orla Fairweather:** Los recuerdos enriquecidos son recuerdos particularmente fuertes, cargados de poder.
        - **Orla Fairweather:** Si conviertes un recuerdo enriquecido en un cráter, recibirás experiencia o energía adicional en comparación con un recuerdo normal.
        - **Player:** ¡Suena genial! ¿Dónde puedo conseguirlos?
        - **Orla Fairweather:** ¡Puedes recibir recuerdos enriquecidos simplemente por recolectar mechones normales, si tienes suerte!
        - **Orla Fairweather:** Alternativamente, si estás atento, puedes ver una brizna enriquecida flotando alrededor de una colonia. Estos siempre brindan recuerdos enriquecidos cuando se cosechan.
        - **Orla Fairweather:** Sin embargo, son inestables. Si quieres que uno se quede, tendrás que darle un recuerdo que hayas cosechado anteriormente. Haz que tus amigos también lo hagan: ¡cuantas más personas lo alimenten, más tiempo permanecerá ahí!
        - **Orla Fairweather:** Finalmente, ten en cuenta que tendrás que visitar los fuegos fatuos más alejados del campamento. Nunca hemos visto ningún recuerdo enriquecido de los fuegos fatuos del sur, ni ningún fuego enriquecido flotando por ahí abajo.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Cómo puedo coleccionar recuerdos?
            - (above|how-to-collect-memories)
          - [Choice]: ¿Cómo puedo convertir recuerdos?
            - (below|how-to-convert-memories)
          - [Choice]: Eso es todo, gracias.
            - (end)
      - [Choice]: Eso es todo lo que necesitaba saber, gracias.
        - (end)
  - {{anchor|how-to-convert-memories}}¿Cómo puedo convertir memorias?
    - (Condition: If the player doesn't have a memory in the inventory:)
      - **Orla Fairweather:** Bueno, ¡necesitarás algunos recuerdos! Recuerdas cómo conseguirlos, ¿no?
      - [Menu]: Selecciona una opción
        - [Choice]: No, por favor repasa eso otra vez.
          - (arriba2|cómo-coleccionar-recuerdos)
        - [Choice]: Sí, lo recuerdo.
          - (continue|how-to-convert-memories-2)
    - (Condition: If the player has a memory in the inventory:)
      - **Orla Fairweather:** Bueno, tienes algunos recuerdos contigo, ¡que es el primer paso!
      - (continue|how-to-convert-memories-2)
    - **Orla Fairweather:{{anchor|how-to-convert-memories-2}}** Necesitas llevar uno o más recuerdos a un cráter. Estos se pueden encontrar cerca de cualquiera de las colonias de wisp.
    - **Orla Fairweather:** Deposita recuerdos en el cráter para recibir conocimiento de adivinación adicional o energía divina, ¡algo que puede usarse para crear objetos más adelante!
    - **Orla Fairweather:** Alternativamente, si tienes energía divina extra, puedes combinarla con los recuerdos para obtener conocimientos adicionales de adivinación. A esto lo llamamos experiencia "mejorada".
    - **Orla Fairweather:** Para hacer esto, necesitarás arrojar un recuerdo y algo de energía divina al cráter.
    - **Orla Fairweather:** Para recuerdos normales, necesitarás 5 energías del mismo nivel que tu memoria y para recuerdos enriquecidos necesitarás 10 lotes de energía para el mismo nivel.
      - [Menu]: Selecciona una opción
        - [Choice]: ¿Cómo puedo coleccionar recuerdos?
          - (above|how-to-collect-memories)
        - [Choice]: ¿Qué son los recuerdos enriquecidos?
          - (above|enriched-memories)
        - [Choice]: Eso es todo lo que necesitaba saber, gracias.
          - (end)
  - [Choice]: Eso es todo, gracias.
    - (end)

##### Después de las lecciones de Faizan Augour en Divination

- **Orla Fairweather:** ¡Se ha hecho un nuevo descubrimiento! ¿Quieres que te lo muestre?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Sí!
    - **Orla Fairweather:** Mi último descubrimiento es bastante emocionante, aunque desafortunadamente no hemos podido observarlo en los mechones de aquí.
    - **Orla Fairweather:** En las otras colonias, ocasionalmente verás una mecha enriquecida, o tendrás especial éxito al recolectar una mecha normal, lo que te permitirá recolectar un recuerdo enriquecido.
    - **Orla Fairweather:** ¿Por qué no intentas encontrar uno?
  - [Choice]: Por el momento no, gracias.
    - (end)

##### Después de reunir un recuerdo enriquecido

- **Orla Fairweather:** Has cubierto todo lo que sé. Sin embargo, Faizan ha descubierto algo nuevo. Deberías alcanzarlo.

##### Después de completar los 10 logros introductorios de Divination

- **Orla Fairweather:** Primero, me gustaría darte una recompensa por aprender los conceptos básicos de la adivinación. ¡Has demostrado verdadera dedicación!
- ¡Recibes 500 piezas de energía parpadeante!
- (receives=500 flickering energy)
- **Orla Fairweather:** Úsalos sabiamente.
- (initial|initial-options-camp)

##### Después de reclamar la recompensa por logros de Divination

- **Orla Fairweather:** ¿En qué puedo ayudarte hoy?
- [Menu]: Seleccione una opción {{anchor|initial-options-camp}}
  - [Choice]: Me gustaría preguntar sobre la adivinación.
    - [Menu]: Seleccione una opción {{anchor|about-divination}}
      - [Choice]: ¿Cómo puedo coleccionar recuerdos?
        - (arriba2|cómo-coleccionar-recuerdos)
      - [Choice]: ¿Cómo puedo convertir recuerdos?
        - (arriba2|cómo-convertir-memorias)
      - [Choice]: ¿Qué son los recuerdos enriquecidos?
        - (arriba2|recuerdos-enriquecidos)
      - [Choice]: Eso es todo, gracias.
        - (end)
  - [Choice]: ¿Puedes hablarme de esa capa?
    - **Orla Fairweather:** Precioso, ¿no? Lo reservamos para verdaderos maestros de la adivinación, quienes podrán usarlo como señal de su logro.
    - (previous)
  - [Choice]: ¿Puedes ayudarme con los trajes de adivinación? {{anchor|fragments}}
    - (Condition: If the player can't receive divination fragments and hasn't unlocked the blueprint required to make the outfit pieces:)
      - **Orla Fairweather:** En el nivel 70 puedes comenzar a recolectar fragmentos para crear trajes de habilidades de élite. Cuando llegues a ese nivel, automáticamente comenzarás a recolectar fragmentos. Luego puedes usarlos con un plano para hacerte las piezas restantes del atuendo de élite para esta habilidad.
    - (Condition: If the player can receive divination fragments but hasn't unlocked the blueprint required to make the outfit pieces:)
      - **Orla Fairweather:** Estás configurado para recibir fragmentos. Cuando llegues al nivel 80 podrás crear prendas de vestir.
    - (Condition: If the player can receive divination fragments and has unlocked the blueprint required to make the outfit pieces:)
      - **Orla Fairweather:** Estás configurado para recibir fragmentos. Cuando tengas 3600 fragmentos, podrás usarlos para crear una pieza de atuendo de élite. Simplemente acude a un banco de trabajo Invention para crear las piezas.
    - (Condition: If the player owns the full elder divination outfit, or all of the outfit pieces required to craft it:)
      - **Orla Fairweather:** Ya has creado todas las prendas posibles. Me aseguraré de que no reciba más fragmentos.
      - **Orla Fairweather:** Recuerda que puedes combinar las piezas del atuendo básico para crear las versiones de nivel alto y obtener beneficios adicionales.

##### Si el player tiene 99 Divination

- [Menu]: Elige una opción:
  - [Choice]: ¿Puedes venderme un Divination skillcape?{{anchor|skillcape}}
    - (Condition: If the player has a ring of charos (a) equipped:)
      - **Orla Fairweather:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins por este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
      - [Menu]: Elige una opción:
        - [Choice]: ¿92.000 coins? Eso es demasiado caro.
          - **Player:** Sé dónde encontrarte si cambio de opinión.
        - [Choice]: De hecho, creo que tengo el dinero aquí.
          - (Condition: If the player has no backpack space:)
            - **Orla Fairweather:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar algo de espacio en backpack antes de que pueda venderte uno.
          - (Condition: If the player does not have enough money:)
            - **Player:** Pero desafortunadamente me equivoqué.
            - **Orla Fairweather:** Bueno, vuelve a verme cuando lo hagas.
          - (Condition: If the player has enough money:)
            - (receives=Divination cape and Divination hood) (removes=92,000 coins)
            - **Orla Fairweather:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
        - [Choice]: cond=If the player has 120 Divination:|He dominado esta habilidad. ¿Hay algo más?
          - **Orla Fairweather:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
          - **Orla Fairweather:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
          - **Orla Fairweather:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo...
          - **Orla Fairweather:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle un Divination master cape.
          - [Menu]: ¿Comprar Divination master cape por 120.000 coins?
            - [Choice]: Sí.
              - (Condition: Without free backpack space:)
                - **Orla Fairweather:** No tienes suficiente espacio en tu backpack. Por favor regresa cuando tengas más.
              - (Condition: With free backpack space:)
                - (Condition: Without 120,000 coins:)
                  - No tienes suficiente dinero para comprar esta capa.
                  - (pop-up)
                    - (Pop-up: You do not have enough money to purchase this cape.|warning=yes)
                - (Condition: With 120,000 coins:)
                  - (removes=120,000 coins) (receives=Divination master cape)
                  - (Action: Suena música Master cape.)
            - [Choice]: No.
              - (end)
    - (Condition: If the player does not have a ring of charos (a) equipped:)
      - **Orla Fairweather:** Por supuesto. Sin embargo, es un artículo muy prestigioso, por lo que tiene un precio elevado. El skillcape cuesta 99.000 de oro.
      - [Menu]: Elige una opción:
        - [Choice]: ¿99.000 coins? Eso es demasiado caro.
          - **Player:** Sé dónde encontrarte si cambio de opinión.
        - [Choice]: De hecho, creo que tengo el dinero aquí.
          - (Condition: If the player has no backpack space:)
            - (arriba)
          - (Condition: If the player does not have enough money:)
            - (arriba)
          - (Condition: If the player has enough money:)
            - (receives=Divination cape and Divination hood) (removes=99,000 coins)
            - **Orla Fairweather:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
        - [Choice]: cond=If the player has 120 Divination:|He dominado esta habilidad. ¿Hay algo más?
          - (arriba)
  - [Choice]: He notado que hay un par de versiones de cada skillcape. {{anchor|skillcape-version}}
    - **Orla Fairweather:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
    - (Condition: If the player uses the old model:)
      - **Orla Fairweather:** Parece que actualmente estás usando el modelo anterior para tu Divination skillcape. ¿Quieres cambiar a uno más nuevo?
      - (continue)
    - (Condition: If the player uses the new model:)
      - **Orla Fairweather:** Aún puedes elegir usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, me gustaría usar la versión [new/old] del skillcape.
        - **Orla Fairweather:** ¿Te gustaría usar el modelo [old/newer] solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
        - [Menu]: Selecciona una opción
          - [Choice]: Solo me gustaría cambiar el Divination skillcape.
            - **Orla Fairweather:** No hay problema, ahora utilizarás el modelo [older/newer] para tu Divination skillcape.
          - [Choice]: Me gustaría cambiar todos mis skillcapes.
            - **Orla Fairweather:** ¡No hay problema, ahora usarás el modelo [older/newer] para todos tus skillcapes!
          - [Choice]: ¡He cambiado de opinión!
            - (end)
      - [Choice]: No, gracias.
        - **Orla Fairweather:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión [old/new]!
        - (Condition: If the player uses the new model for any other skillcape:)
          - **Orla Fairweather:** Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas.
          - [Menu]: Selecciona una opción
            - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
              - **Orla Fairweather:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
            - [Choice]: No, gracias.
              - (end)
  - [Choice]: Me gustaría hablar de otra cosa.
    - **Orla Fairweather:** ¿En qué puedo ayudarte hoy?
    - [Menu]: Selecciona una opción
      - [Choice]: Me gustaría preguntar sobre la adivinación.
        - (above|about-divination)
      - [Choice]: ¿Puedes venderme un Divination skillcape?
        - (above|skillcape)
      - [Choice]: He notado que hay un par de versiones de cada skillcape.
        - (above|skillcape-version)
      - [Choice]: ¿Puedes ayudarme con los trajes de adivinación?
        - (above|fragments)
  - [Choice]: ¿Puedes ayudarme con los trajes de adivinación?
    - (above|fragments)

#### Usando un fragmento de crónica sobre ella.

- **Orla Fairweather:** Este es un fragmento de una crónica. Deberías hablar con May sobre esto.

#### Usando energía en ella

- **Orla Fairweather:** Esta es energía divina. Se puede utilizar para producir objetos y efectos útiles.

#### Usando un recuerdo en ella


##### Normalmente

- **Orla Fairweather:** Ah, eso es un recuerdo. Deberías llevarlo a un cráter y convertirlo en experiencia o energía.

##### Durante la tarea de celebraciones del 25 Aniversario

- **Orla Fairweather:** Ah, los recuerdos...
- **Player:** Y las energías, crónicas y briznas...
- **Orla Fairweather:** Muy gracioso.
- **Orla Fairweather:** Pero tienes razón, no deberíamos insistir tanto en el pasado.
- **Orla Fairweather:** Quizás estés aquí para que yo adivine tu futuro...
- **Player:** Bueno, ya que estoy aquí.
- **Orla Fairweather:** Hmm, déjame ver... ¡Te mantendrás erguido y lucharás contra dioses poderosos, pero terminarás triunfante!
- **Player:** Um, todo eso quedó en el pasado.
- **Orla Fairweather:** Hmm, déjame ver... ¡Completarás una serie de tareas nostálgicas y aparentemente aleatorias a cambio de una brillante recompensa!
- **Player:** Lo siento, no, ese es el presente.
- **Orla Fairweather:** Hmm, déjame ver... Recibirás un codazo en las costillas de un adivino furioso.
- {{RSFontAchievement|By Guthix, to Orla!|Show Orla Fairweather a Divination memory.}}
- ((Shown in a task completion pop-up:))
  - {{Colour|#F0BE79| TAREA DEL 25 ANIVERSARIO |#181513}}
  - ¡Por Guthix, por Orla!
  - Mostrar Orla Fairweather una memoria Divination.
  - (continue)
- **Player:** ¡Ah, no! ¡Por favor, líbrame de mi terrible destino!
- (Condition: If all the tasks have been completed:)
  - **Player:** Parece que he completado todo. ¡Será mejor que vaya a ver a Hans sobre esa recompensa!

### In Burthorpe

- **Orla Fairweather:** ¿Puedes recordarlo ahora también? Lo había olvidado. Todos lo habíamos olvidado. ¡Ahora sé que tenemos que irnos! El Memorial a Guthix nos estaba esperando para recordarlo. ¿Vamos juntos?
- [Menu]: ¿Teletransportarse al Memorial a Guthix?
  - [Choice]: Sí.
    - (Action: el player es teletransportado al Memorial a Guthix.)
  - [Choice]: No.
    - (end)

### At Memorial to Guthix


#### Primera vez

- **Player:** ¿Qué es este lugar?
- **Orla Fairweather:** Ha estado aquí durante años, querida. Lo sabía, lo he leído, pero nunca pudimos verlo. Se mantuvo oculto a la vista por razones que desconozco.
- **Orla Fairweather:** Desde que Guthix dejó este mundo, he ido adquiriendo una sensación cada vez mayor de la existencia de este lugar.
- **Orla Fairweather:** Pequeñas hebras de recuerdos Guthixianos han comenzado a aparecer cerca de los cráteres Divination.
- **Orla Fairweather:** Parece que estuvieron ocultos a la vista hasta ahora.
- **Orla Fairweather:** Intentaré explicar lo que he estado investigando desde que estoy aquí. Todo está regresando a mí lentamente.
- **Orla Fairweather:** Todo comienza con engramas. Los engramas son marcadores permanentes que se dejan en la línea de tiempo.
- **Orla Fairweather:** Son causados por actividades importantes de los seres vivos y solo pueden ser detectados por aquellos que tienen un conocimiento experto de Divination.
- **Orla Fairweather:** Es posible cargar estos engramas infundiéndoles energía divina y hebras de memoria.
- **Player:** ¿Qué les hace eso?
- **Orla Fairweather:** Oh, es un teatro de luz y magia, querida. Los engramas contienen un eco de la historia.
- **Player:** Todos estos 'ecos' pertenecen a Guthix, ¿verdad? Engramas, hilos de memoria, energía divina... todos son parte de la fuerza vital residual de Guthix.
- **Orla Fairweather:** Qué astuto. Supongo que no debería esperar menos de ti.
- **Orla Fairweather:** Solo he cargado un par de engramas débiles, pero ambos eran desde el punto de vista del propio Guthix. Podemos suponer que es casi seguro que el resto también esté relacionado con Guthix.
- **Player:** Podría haber mucha información valiosa almacenada en estos engramas. ¿Cómo los encontramos?
- **Orla Fairweather:** En el centro de este vestíbulo, detrás de mí, verás una piscina rebosante de energía. Probablemente lo sientas antes de verlo. Emite un aura tan gloriosa.
- **Orla Fairweather:** Todos los zócalos dentro del edificio están conectados de alguna manera a esta piscina.
- **Orla Fairweather:** Una vez cargado, pude mostrar los ecos que se encuentran dentro de los engramas allí, como estatuas de vida cruda; ecos animados de la realidad.
- **Orla Fairweather:** Si juegas con los pedestales, es posible que puedas descubrir una vaga idea de la ubicación de otros engramas. Sin embargo, no puedo prometer que serán fáciles de detectar.
- **Player:** Entonces, una vez que encuentro un engrama, ¿puedo cargarlo llenándolo con energía divina y estos hilos de memoria?
- **Orla Fairweather:** Sí, y luego tráemelo. Puedo hacer que la reserva de energía absorba cualquier engrama cargado que traigas aquí. Después de eso, deberías poder interactuar con los ecos como mejor te parezca.
- **Player:** Esto parece bastante simple, pero permítanme resumirlo rápidamente.
- **Player:** ¿Necesito usar los pedestales para obtener pistas sobre dónde encontrar los engramas, luego cargar estos engramas con hilos de memoria y energía divina, y luego dártelos para que los agregues al grupo aquí?
- **Orla Fairweather:** Sí, parece que lo tienes.
- **Orla Fairweather:** ¡Oh, una cosa más!
- **Player:** ¿Mmm?
- **Orla Fairweather:** El charco de energía. Una vez que cargué algunos engramas, noté que sentía una conexión más fuerte con este lugar.
- **Orla Fairweather:** ¿Quizás podamos concentrar la energía en este lugar para ayudarte con tu habilidad Divination? Sólo una corazonada, por supuesto.
- **Player:** Suena interesante. Voy a investigar.
- **Orla Fairweather:** Fantástico. Por favor, tome uno de los engramas que encontré para comenzar y familiarizarse con ellos.
- Etapa tutorial 1/6 completa.
- (pop-up)
  - (Pop-up: Tutorial stage 1/6 complete.)
- (Condition: Without space in backpack:)
  - **Orla Fairweather:** Parece que estás demasiado agobiado para llevar los hilos del engrama y la memoria. Vuelve cuando tengas más espacio.
- (Condition: With space in backpack:)
  - (receives=Naragi engram and 80 memory strands)
  - **Orla Fairweather:** ¡Intenta no perderlo!

#### Después

- **Orla Fairweather:** Mira si puedes sintonizar el engrama que te di. Es necesario ponerlo en marcha con algo de energía divina.

#### Regalando hilos de memoria

- [Orla sólo puede hacer eso por ti una vez que hayas obtenido prestigio al menos una vez.]

#### Recuperando el engrama naragi

- **Orla Fairweather:** Dios mío, ¿has perdido contacto con el engrama que te di?
- **Orla Fairweather:** Vamos, intentémoslo de nuevo. Toma este engrama.
- (Condition: Without space in backpack:)
  - **Orla Fairweather:** Parece que estás demasiado agobiado para llevar los hilos del engrama y la memoria. Vuelve cuando tengas más espacio.
- (Condition: With space in backpack:)
  - (receives=Naragi engram)
  - **Orla Fairweather:** ¡Intenta no perderlo!

#### Intentando entrar a la piscina sin 70 Divination

- **Orla Fairweather:** Hay una energía extraña que emana de esa piscina. Intenté entrar a la piscina pero no me pasa nada.
- Necesitas el nivel 70 de Divination para ingresar al Salón de los Recuerdos.

#### Regresando con el engrama Naragi cargado

- **Player:** He cargado este engrama con energía divina y algunos hilos de memoria. ¿Podrías echarle un vistazo?
- **Orla Fairweather:** ¡Esto es perfecto! <br> Puedo sentir las energías del pasado irradiando desde este engrama.
- (removes=Naragi engram (charged))
- Etapa tutorial 2/6 completa.
- (pop-up)
  - (Pop-up: Tutorial stage 2/6 complete.)
- **Orla Fairweather:** Agregaré el eco a la piscina y aprovecharé su poder para ti. Gratis, por supuesto, aunque no me importaría una palmadita en la espalda de vez en cuando.

#### Hablando con ella de nuevo

- **Orla Fairweather:** Agregué el engrama cargado que me diste al conjunto de energía. Debes asignar ese eco a uno de los zócalos que rodean la piscina.

#### Añadiendo el eco de Naragi

- Etapa tutorial 3/6 completa.
- (pop-up)
  - (Pop-up: Tutorial stage 3/6 complete.)

#### Hablando con ella después de agregar el eco de Naragi

- **Orla Fairweather:** Ese eco, querida: ¿es un naragi?
- **Orla Fairweather:** Solo he leído descripciones, pero tiene sentido. Me pregunto qué podemos aprender de ello.

#### Comprobando el naragi

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Habla con el eco.
    - **Guthix:** La naturaleza de las cosas es un ciclo perfecto, de un estado a otro, y un retorno a la existencia anterior.
    - **Guthix:** Las cosas que alguna vez existieron, pero que ahora están perdidas, aún pueden regresar y en forma mejorada.
    - **Guthix:** Lo que ya no existe volverá de nuevo, renovado con más vigor y poder que antes.
    - **Guthix:** Aquellos que recuerden el pasado verán la verdad en mis palabras.
    - **Guthix:** De los eventos futuros, los veo más claros, sin embargo, las cosas que deben ser, deben ser.
    - **Guthix:** Podría cambiarlos si así lo deseara, pero no lo hago, ya que todas las cosas deben suceder a medida que siguen su curso.
    - Etapa tutorial 4/6 completa.
- (pop-up)
  - (Pop-up: Tutorial stage 4/6 complete.)
  - [Choice]: Vuelve a colorear este eco.
    - ((Non-related dialogue))
  - [Choice]: Limpia este pedestal.
    - (Action: Se borra el echo plinth.)

#### Regresando a Orla

- **Orla Fairweather:** El conocimiento es poder. Esa metáfora tiene un peso casi tangible en tiempos como estos. Existimos alegremente al lado de seres capaces de golpearnos con una palabra.
- **Orla Fairweather:** Algunos días me quedo y disfruto de la serenidad de este mundo, pero otros me siento como un observador indefenso en un mundo donde los niños tiránicos se vuelven locos.
- **Orla Fairweather:** No hay que desdeñar la posibilidad de que se produzca incluso un reequilibrio minúsculo, si se presenta la oportunidad, querida. Juguemos con los poderes aquí y veamos qué surge.
- **Player:** ¿Qué es lo que me estás pidiendo que haga?
- **Orla Fairweather:** Lo siento, a veces me salgo por la tangente.
- **Orla Fairweather:** La estatua de la mariposa en el borde del estanque de energía controla el flujo de energía aquí. Deberías poder potenciar tu habilidad Divination jugando con ella. Déjame saber si funciona.

#### Dirigiendo la fuente de energía.

- Etapa tutorial 5/6 completa.
- (pop-up)
  - (Pop-up: Tutorial stage 5/6 complete.)

#### Terminando el tutorial

- **Orla Fairweather:** ¿Conseguiste potenciar tus habilidades Divination de alguna manera?
- **Player:** Elegí un efecto y le fijé la energía. Parece que hay más opciones para mí allí, pero no pude acceder a ellas.
- **Orla Fairweather:** ¡Oh, sabía que podías hacerlo! No pude lograrlo yo mismo, pero supe que había algo en esa estatua tan pronto como encontré este lugar.
- **Orla Fairweather:** ¡Por permitirme aprender de ti, te permitiré a ti aprender de mí a cambio!
- **Orla Fairweather:** Ahora casi no hay límite para la cantidad de crónicas que puedes llevar, y también deberían ser un poco más fáciles de encontrar.
- Etapa tutorial 6/6 completa.
- (pop-up)
  - (Pop-up: Tutorial stage 6/6 complete.)
- **Player:** Muy amable de tu parte. ¡Gracias!

#### Después del tutorial


##### Sin engramas cargados

- [Menu]: hablar con orla
  - [Choice]: ¿Tienes algo más para mí?
    - *(Sin suficientes engramas :)*
      - **Orla Fairweather:** ¡No has sintonizado suficientes engramas para tu recompensa!
    - *(Con suficientes engramas :)*
      - *(Sin haber reclamado las hebras:)*
        - **Orla Fairweather:** Toma mi colección de recuerdos. Lo lograste, querida, aunque yo no pude descifrarlo del todo, así que tiene sentido.
        - Orla te ha dado hilos de memoria [amount].
        - **Orla Fairweather:** Cuando agregué ese engrama cargado al conjunto de energía, todo se sintió... ¿terminado? ¿Es esa la palabra correcta? Tengo la sensación de que hay una serie de ecos y parece que los hemos recogido todos.
      - *(Habiendo reclamado los hilos:)*
        - **Orla Fairweather:** Nada en este momento: puedes tener una idea de la ubicación de los engramas interactuando con los pedestales.
  - [Choice]: ¿Puedes hablarme de estas mariposas?
    - **Orla Fairweather:** Parecen estar hechos de energía mágica dispersa, del propio Guthix.
    - **Orla Fairweather:** Parece seguro recogerlos. Siguiendo las enseñanzas del equilibrio de Guthix, será en una de las áreas de conocimiento o habilidad en las que tengas más inexperiencia.
    - **Player:** ¿Qué pasa si no quiero recibir experiencia por atrapar mariposas?
    - **Orla Fairweather:** Bueno, yo... Supongo que podría ayudarte. ¿De verdad quieres dejar de adquirir experiencia cazando mariposas?
    - [Menu]: Selecciona una opción
      - [Choice]: Bloquea XP de las mariposas
        - **Orla Fairweather:** Ya no obtendrás más experiencia atrapando mariposas Guthixianas. ¡Pregúntame sobre mariposas otra vez si cambias de opinión!
      - [Choice]: Gana XP de las mariposas
        - **Orla Fairweather:** Ahora obtendrás experiencia capturando mariposas Guthixianas. ¡Pregúntame sobre mariposas otra vez si cambias de opinión!
  - [Choice]: No importa.
    - **Orla Fairweather:** Puedes tener una idea de la ubicación de los engramas interactuando con los pedestales.

##### Con engramas cargados

- **Player:** He cargado este engrama con energía divina y algunos hilos de memoria. ¿Podrías echarle un vistazo?
- **Orla Fairweather:** ¡Esto es perfecto! <br> Puedo sentir las energías del pasado irradiando desde este engrama.
- **Orla Fairweather:** Agregaré el eco a la piscina y aprovecharé su poder para ti. Gratis, por supuesto, aunque no me importaría una palmadita en la espalda de vez en cuando.
- (Condition: If the player still has charged engrams:)
  - **Player:** Ese no fue el único engrama cargado que tengo.
  - **Orla Fairweather:** ¿Ah? Alguien ha estado ocupado. Está claro que su reputación de hacer las cosas no es infundada. <br> Tomaré las que tenga más y las agregaré al grupo.
