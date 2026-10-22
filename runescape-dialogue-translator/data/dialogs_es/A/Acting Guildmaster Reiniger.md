# Acting Guildmaster Reiniger

- **Original Wiki Page**: [Transcript:Acting Guildmaster Reiniger](https://runescape.wiki/w/Transcript%3AActing%20Guildmaster%20Reiniger)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Archaeology tutorial

- (ver|tutorial Archaeology)

### After Archaeology tutorial


#### Habla con


##### Primera vez después del tutorial

- **Acting Guildmaster Reiniger:** Bien, ahora que eres miembro oficial del gremio, ¡deberías salir y comenzar a excavar!
- **Acting Guildmaster Reiniger:** Tenemos un equipo en Kharid-et al que le vendría bien otro par de manos. Haré que alguien te lleve allí ahora.
- (Action: La pantalla se desvanece y desaparece.)
- (Condition: If on a League world, and without Desert unlocked:)
  - No tienes esa región desbloqueada.
  - (pop-up)
    - (Pop-up: You do not have that region unlocked.|warning=yes)
- (Condition: If on a Regular world, or with Desert unlocked in a League world:)
  - {{Tmissing}}

##### Normalmente


##### Sin ceremonia de calificación para asistir

- [Menu]: ¿Sobre qué te gustaría charlar?
  - [Choice]: ¿Dónde debería estar excavando?
    - **Acting Guildmaster Reiniger:** Veamos... ¿Dónde serías más útil en este momento?
    - (Condition: With access to only Kharid-et Dig Site:)
      - **Acting Guildmaster Reiniger:** Por ahora, creo que es mejor que te quedes con Kharid-et, que está situado al este de Al Kharid. Busque Dr Nabanik al sur de Duel Arena. Él te mostrará los entresijos un poco más.
    - (Condition: With access up to the Infernal Source Dig Site:)
      - **Acting Guildmaster Reiniger:** Puedes continuar en Kharid-et, o hemos recibido una solicitud para que ayudes en la excavación al noroeste de aquí.
      - **Acting Guildmaster Reiniger:** Probablemente haya algunos misterios que puedas ayudar a Dr Nabanik a descubrir si continúas en Kharid-et.
      - **Acting Guildmaster Reiniger:** O si prefieres un poco más de calidez, Movario está siguiendo una pista sobre algo llamado Infernal Source, justo al noroeste de aquí.
      - **Acting Guildmaster Reiniger:** La entrada del sitio está al lado del Jolly Boar Inn y conduce a un edificio mucho más antiguo sobre el cual está construida la posada.
      - **Acting Guildmaster Reiniger:** Hay rumores de que una secta solía operar a partir de ahí, así que es algo que vale la pena investigar.
    - (Condition: With access up to the Everlight Dig Site:)
      - **Acting Guildmaster Reiniger:**Si está más contento quedándose en los sitios Kharid-et o Infernal Source, hágalo por todos los medios. Estoy seguro de que hay numerosos misterios por descubrir ahora y que podrías utilizarlos para trabajar en tu próxima calificación {{Sic}}.
      - **Acting Guildmaster Reiniger:**Sin embargo, ahora también recibí una solicitud de Vanescula en la excavación de Everlight. Everlight está situado en la costa sureste de Morytania. Aparentemente, puedes llegar corriendo hacia el sur desde Port Phasmatys y bajando por la costa.
      - **Acting Guildmaster Reiniger:**Aparentemente, hay un faro muy brillante, por lo que no debería ser demasiado difícil de localizar. Fue el hogar del pueblo helado a principios de la Tercera Edad. Estoy seguro de que habrá algo interesante que descubrir allí.
    - (Condition: With access up to the Senntisten Dig Site:)
      - {{Transcript missing}}
    - (Condition: With access up to the Stormguard Dig Site:)
      - **Acting Guildmaster Reiniger:**Siéntete libre de continuar en Kharid-et, Everlight o Infernal Source, pero hemos recibido una solicitud de voluntarios en un sitio recientemente descubierto al noreste de Ardougne.
      - **Acting Guildmaster Reiniger:**La administradora del sitio es una aviansie llamada Gee'ka, y dice que este podría ser el Stormguard Citadel perdido hace mucho tiempo... Ha instalado su campamento base en la entrada de superficie del Templo de Ikov.
    - (Condition: With access up to the Daemonheim Dig Site:)
      - {{Transcript missing}}
    - (Condition: With access up to the Warforge Dig Site:)
      - **Acting Guildmaster Reiniger:**Si buscas algo un poco más realista, bueno, subterráneo, hay una dama duende llamada Zanik que te ha pedido, por su nombre, que te unas a ella en el suroeste de Feldip Hills.
      - **Acting Guildmaster Reiniger:**¡Ha encontrado la entrada a algo llamado Warforge! Suena aterrador y emocionante... Por supuesto, continúa en los otros sitios si eso no te parece atractivo.
    - (Condition: With access up to the Orthen Dig Site:)
      - **Acting Guildmaster Reiniger:**¡Me alegra decir que Mr Mordaut ha iniciado una excavación en Anacronia para explorar las ruinas de la ciudad dragonante Orthen que se encuentran en ella!
      - **Acting Guildmaster Reiniger:**¡La actividad volcánica reciente ha desenterrado una serie de nuevos y emocionantes hallazgos!
    - (Condition: With access to all the dig sites:)
      - **Acting Guildmaster Reiniger:** Bueno, ¡realmente es tu elección en este momento! Puedes ir a cualquier parte. Te sugiero que elijas un enfoque: una colección que deseas completar, un misterio que te gustaría resolver, alguna investigación en la que te gustaría centrarte o incluso una reliquia en particular que te gustaría encontrar.
      - **Acting Guildmaster Reiniger:** Hasta que los duendes del tiempo nos indiquen una nueva ubicación, no podemos estar seguros de dónde excavar, pero en el momento en que lleguen a un lugar nuevo, te lo haremos saber.
      - **Acting Guildmaster Reiniger:** Queremos que nuestros mejores y más brillantes excavadores allí, ejem, dondequiera que esté "allí", ¡eso es seguro!
  - [Choice]: ¿Qué pasó con Toni?
    - [Menu]: Selecciona una opción
      - [Choice]: Levantando el monolito (escena).
        - ((Transcript:Archaeology/Pre-release#At the Varrock Dig Site cutscene plays.))
      - [Choice]: El descubrimiento de Tony (escena).
        - (Action: La pantalla aparece y desaparece. Comienza la escena.)
        - **Guildmaster Tony:** ¡Creo que lo he resuelto!
        - **Guildmaster Tony:** Oh, espero que esto realmente funcione.
        - **Guildmaster Tony:** No soy ningún dios, esto podría ser realmente peligroso.
        - **Guildmaster Tony:** Aquí va...
        - (Action: El monolito comienza a emanar poder.)
        - **Guildmaster Tony:** {{RSChat|Uh}}
        - (Action: El monolito comienza a tirar de Tony.)
        - **Guildmaster Tony:** {{RSChat|Oh}}
        - **Guildmaster Tony:** {{RSChat|No}}
        - **Guildmaster Tony:** {{RSChat|No, no, no}}
        - (Action: El monolito atrae a Tony.))
        - **Guildmaster Tony:** {{RSChat|NOOOOOOOOOOOOOOO}}
        - (Action: La pantalla aparece y desaparece. La escena termina.)
  - [Choice]: cond=If the player has 99 Archaeology|Pregunta por skillcapes.
    - [Menu]: Selecciona una opción
      - [Choice]: Me pregunto si tienes algún skillcapes por ahí.
        - **Player:** Me pregunto si tienes algún skillcapes por ahí.
        - **Acting Guildmaster Reiniger:** ¡Espero que no estén holgazaneando! Cualquier viejo podría coger uno y hacer alarde de él, pero...
        - **Acting Guildmaster Reiniger:** He hecho algo especialmente para ti, el skillcape de Archaeology como muestra de tu maestría en el campo.
        - **Acting Guildmaster Reiniger:** Desafortunadamente, es bastante costoso conseguir los materiales necesarios para crear una capa tan impresionante, por lo que es tuya a un costo.
        - ((If the player has 99–119 Archaeology:))
          - (continue|99-skillcape)
        - ((If the player has 120 Archaeology:))
          - [Menu]: ¿Qué skillcape te gustaría comprar?
            - [Choice]: 99 skillcape.
              - **Player:** Me gustaría el 99 skillcape, por favor.
              - (Condition: If the player has a ring of charos (a) equipped:)
                - **Acting Guildmaster Reiniger:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins por este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
                - [Menu]: Elige una opción:
                  - [Choice]: ¿92.000 coins? Eso es demasiado caro.
                    - **Player:** Sé dónde encontrarte si cambio de opinión.
                  - [Choice]: De hecho, creo que tengo el dinero aquí.
                    - (Condition: If the player has no backpack space:)
                      - **Acting Guildmaster Reiniger:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar algo de espacio en backpack antes de que pueda venderte uno.
                    - (Condition: If the player does not have enough money:)
                      - **Player:** Pero desafortunadamente me equivoqué.
                      - **Acting Guildmaster Reiniger:** Bueno, vuelve a verme cuando lo hagas.
                    - (Condition: If the player has enough money:)
                      - (receives=Archaeology cape and Archaeology hood) (removes=92,000 coins)
                      - **Acting Guildmaster Reiniger:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
                  - [Choice]: cond=If the player has given Reiniger an inverted skillcape token:|Me gustaría un skillcape con los colores invertidos.
                    - (receives=inverted hooded Archaeology cape)
                    - **Acting Guildmaster Reiniger:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
                  - [Choice]: cond=If the player has 120 Archaeology|He dominado esta habilidad. ¿Hay algo más?
                    - **Acting Guildmaster Reiniger:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
                    - **Acting Guildmaster Reiniger:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
                    - **Acting Guildmaster Reiniger:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo...
                    - **Acting Guildmaster Reiniger:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle un Archaeology master cape.
                    - (Condition: With inverted Archaeology master cape unlocked:)
                      - [Menu]: Selecciona una opción
                        - [Choice]: Me gustaría un master cape normal.
                          - (continue)
                        - [Choice]: Me gustaría un master cape invertido.
                          - [Menu]: ¿Comprar Archaeology master cape por 120.000 coins?
                            - [Choice]: Sí.
                              - (Condition: Without free backpack space:)
                                - **Acting Guildmaster Reiniger:** No tienes suficiente espacio en tu backpack. Por favor regresa cuando tengas más.
                              - (Condition: With free backpack space:)
                                - {{Transcript missing}}
                            - [Choice]: No.
                              - (end)
                    - [Menu]: ¿Comprar Archaeology master cape por 120.000 coins?
                      - [Choice]: Sí.
                        - (Condition: If the player has no backpack space:)
                          - **Acting Guildmaster Reiniger:** No tienes suficiente espacio en tu backpack. Por favor regresa cuando tengas más.
                        - (Condition: If the player does not have enough money:)
                          - No tienes suficiente dinero para comprar esta capa.
                        - (Condition: If the player has enough money:)
                          - (receives=Archaeology master cape) (removes=120,000 coins)
                          - (Action: Suena música Master cape.)
                      - [Choice]: No.
                        - (end)
              - (Condition: If the player does not have a ring of charos (a) equipped:)
                - **Acting Guildmaster Reiniger:** Para eso necesito 99.000 coins.
                - (Condition: If the player has an inverted skillcape token or inverted master skillcape token in their backpack attuned to Archaeology:)
                  - **Acting Guildmaster Reiniger:** ¡Veo que tienes una de las fichas de inversión de capa de Hans! Te quitaré eso de las manos y te venderé cualquier inverted cape para el que seas elegible.
                  - (removes=any inverted skillcape token and inverted master skillcape token)
                  - (continue)
                - [Menu]: Elige una opción:
                  - [Choice]: ¿99.000 coins? Eso es demasiado caro.
                    - **Player:** Sé dónde encontrarte si cambio de opinión.
                  - [Choice]: De hecho, creo que tengo el dinero aquí.
                    - (Condition: If the player has no backpack space:)
                      - (Action: arriba)
                    - (Condition: If the player does not have enough money:)
                      - (Action: arriba)
                    - (Condition: If the player has enough money:)
                      - (receives=Archaeology cape and Archaeology hood) (removes=99,000 coins)
                      - **Acting Guildmaster Reiniger:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
                  - [Choice]: cond=With inverted Archaeology cape unlocked:|Me gustaría un skillcape con los colores invertidos.
                    - (Condition: Without free backpack space:)
                      - **Acting Guildmaster Reiniger:** Desafortunadamente necesitarás liberar espacio en backpack antes de que pueda venderte uno.
                    - (Condition: With free backpack space:)
                      - {{Transcript missing}}
                  - [Choice]: cond=If the player has 120 Archaeology|He dominado esta habilidad. ¿Hay algo más?
                    - (Action: arriba)
                  - [Choice]: cond=With inverted Archaeology master cape unlocked:|Me gustaría un master cape con los colores invertidos.
                    - **Acting Guildmaster Reiniger:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
                    - **Acting Guildmaster Reiniger:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
                    - **Acting Guildmaster Reiniger:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo...
                    - **Acting Guildmaster Reiniger:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle {{Sic|a}} Archaeology master cape.
                    - [Menu]: ¿Comprar Archaeology master cape por 120.000 coins?
                      - [Choice]: Sí.
                        - (Condition: Without free backpack space:)
                          - **Acting Guildmaster Reiniger:** No tienes suficiente espacio en tu backpack. Por favor regresa cuando tengas más.
                        - (Condition: With free backpack space:)
                          - {{Transcript missing}}
                      - [Choice]: No.
                        - (end)
            - [Choice]: 120 Maestro skillcape
              - **Player:** Me gustaría el Master cape, por favor.
              - **Acting Guildmaster Reiniger:** Realmente has demostrado tu valía, no solo ante el gremio, sino también ante mí, Player. Estoy más que impresionado con lo que has logrado.
              - **Acting Guildmaster Reiniger:** Con eso, me gustaría ofrecerle el Master skillcape por el costo de 120,000 coins.
              - (Condition: If the player has an inverted skillcape token or inverted master skillcape token in their backpack attuned to Archaeology:)
                - **Acting Guildmaster Reiniger:** ¡Veo que tienes una de las fichas de inversión de capa de Hans! Te quitaré eso de las manos y te venderé cualquier inverted cape para el que seas elegible.
                - (removes=any inverted skillcape token and inverted master skillcape token)
                - (continue)
              - (Action: continuar|comprar-capa-master)
      - [Choice]: He notado que hay un par de versiones de cada skillcape.
        - **Acting Guildmaster Reiniger:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado las nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
        - (Condition: If the player currently has the new model activated:)
          - **Acting Guildmaster Reiniger:** Aún puedes elegir usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
          - [Menu]: Selecciona una opción
            - [Choice]: Sí, me gustaría usar la versión antigua del skillcape.
              - **Acting Guildmaster Reiniger:** ¿Te gustaría usar el modelo antiguo solo para esta capa, o para la capa de puntos Quest y todos los skillcapes que tienes?
              - [Menu]: Selecciona una opción
                - [Choice]: Solo me gustaría cambiar el Archaeology skillcape.
                  - **Acting Guildmaster Reiniger:** No hay problema, ahora utilizarás el modelo anterior para tu Archaeology skillcape.
                - [Choice]: Me gustaría cambiar todos mis skillcapes.
                  - **Acting Guildmaster Reiniger:** No hay problema, ¡ahora usarás el modelo anterior para todos tus skillcapes!
                - [Choice]: ¡He cambiado de opinión!
                  - (end)
            - [Choice]: No, gracias.
              - **Acting Guildmaster Reiniger:** ¡Genial! ¡Me alegra que estés disfrutando de nuestra nueva versión!
              - (Condition: If there are skillcapes not using the new model:)
                - **Acting Guildmaster Reiniger:** ¡Si quieres, puedo hacerlo para que uses el modelo más nuevo para todos los skillcapes que tienes!
                - [Menu]: Selecciona una opción
                  - [Choice]: Ok, me gustaría usar la versión más nueva para todos mis skillcapes.
                    - **Acting Guildmaster Reiniger:** ¡Genial, ahora usarás el modelo más nuevo para todos tus skillcapes!
                  - [Choice]: No, gracias.
                    - (end)
        - (Condition: If the player currently has the old model activated:)
          - **Acting Guildmaster Reiniger:** Parece que actualmente estás usando el modelo anterior para tu Archaeology skillcape. ¿Quieres cambiar a uno más nuevo?
          - [Menu]: Selecciona una opción
            - [Choice]: Sí, me gustaría usar la nueva versión del skillcape.
              - **Acting Guildmaster Reiniger:** ¿Te gustaría usar el modelo más nuevo solo para esta capa o para todos los skillcapes que tienes?
              - [Menu]: Selecciona una opción
                - [Choice]: Solo me gustaría cambiar el Archaeology skillcape.
                  - **Acting Guildmaster Reiniger:** No hay problema, ahora utilizarás el modelo más nuevo para tu Archaeology skillcape.
                - [Choice]: Me gustaría cambiar todos mis skillcapes.
                  - **Acting Guildmaster Reiniger:** No hay problema, ¡ahora usarás el modelo más nuevo para todos tus skillcapes!
                - [Choice]: ¡He cambiado de opinión!
                  - (end)
            - [Choice]: No, gracias.
              - **Acting Guildmaster Reiniger:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión anterior!
              - **Acting Guildmaster Reiniger:** ¡Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas!
              - [Menu]: Selecciona una opción
                - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
                  - **Acting Guildmaster Reiniger:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
                - [Choice]: No, gracias.
                  - (end)
  - [Choice]: cond=If there are rewards to claim|Pregunte acerca de las recompensas de calificación.
    - **Acting Guildmaster Reiniger:** ¡Aquí tienes!
    - (Player recibe las recompensas que faltan).

##### Con ceremonia de calificación para asistir.

- **Acting Guildmaster Reiniger:** Parece que has estado trabajando duro y estás listo para ascender de rango. ¡Estás listo para la ceremonia!
- (Se reproduce la escena de la ceremonia de clasificación).

##### Durante la tarea de celebraciones del 25 Aniversario

- **Acting Guildmaster Reiniger:** Bueno, ¡esos artefactos no van a desenterrarse solos!
- **Acting Guildmaster Reiniger:** ¡Coge un azadón y empieza a excavar!
- **Player:** ¿Podrías marcar mi tarea primero, por favor?
- **Acting Guildmaster Reiniger:** Ah, continúa, entonces... pero no nos olvides aquí.
- **Acting Guildmaster Reiniger:** ¡Archaeology es muy divertido y también muy gratificante!
- {{RSFontAchievement|Digging up the Past|Talk to Acting Guildmaster Reiniger inside the Archaeology Guild.}}
- ((Shown in a task completion pop-up:))
  - {{Colour|#F0BE79| TAREA DEL 25 ANIVERSARIO |#181513}}
  - Desenterrar el pasado
  - Habla con Acting Guildmaster Reiniger dentro del gremio Archaeology.
  - (continue)
- **Player:** Lo tendré en cuenta, tal vez vuelva más tarde. ¡Adiós!
- (Condition: If all the tasks have been completed:)
  - **Player:** Parece que he completado todo. ¡Será mejor que vaya a ver a Hans sobre esa recompensa!

#### Verificar calificaciones

- **Acting Guildmaster Reiniger:** Ah, entonces estás buscando subir de rango. Veamos...
- (Condition: If no new qualifications are met and player is not a guildmaster:)
  - (opens=Achievements)
  - (Condition: If the next qualification is Professor:)
    - Aún no estás preparado para obtener el título de "Profesor". Consulte la pestaña Logros para ver lo que le queda por lograr.
    - (continue)
  - (Condition: If the next qualification is Guildmaster:)
    - {{Tmissing}}
  - **Acting Guildmaster Reiniger:** Parece que aún no estás listo para progresar.
- (Condition: If new qualifications are met:)
  - **Acting Guildmaster Reiniger:** Parece que has estado trabajando duro y estás listo para ascender de rango. ¡Estás listo para la ceremonia!
  - (Se reproduce la escena de la ceremonia de clasificación).
- (Condition: If the player has attained Guildmaster:)
  - **Acting Guildmaster Reiniger:** ¡Parece que ya estás en la cima! Felicidades.

### Certifications

*Además del cuadro de diálogo, los siguientes diálogos aparecen encima de Acting Guildmaster Reiniger como texto general.*

#### Intern

{{Transcript|Qualification - Intern}}

#### Asistente

{{Transcript|Qualification - Assistant}}

#### Asociado

{{Transcript|Qualification - Associate}}

#### Profesor

{{Transcript|Qualification - Professor}}

#### Guildmaster

{{Transcript|Qualification - Guildmaster}}
