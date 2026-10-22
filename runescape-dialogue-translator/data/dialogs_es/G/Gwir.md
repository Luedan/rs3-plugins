# Gwir

- **Original Wiki Page**: [Transcript:Gwir](https://runescape.wiki/w/Transcript%3AGwir)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Gwir:** ¡Player! Qué bueno verte.
- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Gwir:** Soy Gwir el escriba.
    - **Player:** ¿Has estado escribiendo algo interesante recientemente?
    - **Gwir:** Toda la literatura me parece interesante, pero últimamente he estado intrigado por la historia reciente de los elfos. Estoy trabajando para documentarlo lo más claramente posible, para que quede registrado para las generaciones futuras.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Puedo ayudarte en algo?
        - (below||helpyouatall)
      - [Choice]: En realidad, no te preocupes.
        - **Player:** En realidad, no te preocupes.
  - [Choice]: ¿Puedo ayudarte en algo?
    - **Player:** ¿Puedo ayudarte en algo?
    - (below|helpyouatall)
  - [Choice]: ¿Puedes recordarme los acontecimientos hasta ahora?
    - (below|eventssofar)
  - [Choice]: Más...
    - [Menu]: Selecciona una opción
      - [Choice]: Acerca del sistema de tareas...
        - (below|tasksystem)
      - [Choice]: Adiós.
        - **Player:** Adiós.

### Telling your story to Gwir {{anchor|helpyouatall}}

- **Player:** ¿Puedo ayudarte en algo?
- (Condition: Offering to help Gwir for the first time:)
  - **Gwir:** Sí, puedes. Soy el escriba aquí y estoy tratando de documentar con precisión los acontecimientos recientes que nos han afectado.
  - **Player:** Ah, creo que entiendo por qué estabas feliz de verme. Déjame adivinar, ¿quieres mi ayuda ya que estuve algo involucrado con dichos eventos recientes?
  - **Gwir:** ¡'Involucrado' sería decirlo a la ligera! Sin embargo, has adivinado correctamente: ¿me ayudarías con esto?
  - [Menu]: Selecciona una opción
    - [Choice]: Claro.
      - (continue)
    - [Choice]: No, lo siento.
      - **Player:** No, lo siento.
- (Condition: Offering to help Gwir subsequently:)
  - **Gwir:** Bueno, como sabes, me ayudaste a documentar todos los descubrimientos que hiciste al trabajar con nosotros los elfos y alrededor de nosotros. Sigamos...
  - (continue)

#### Después de Regicide

- **Player:** Seguro que te ayudaré. ¿Empecemos por el principio?
- **Gwir:** ¡Suena como una gran idea!
- **Gwir:** ¿Cómo empezó todo esto para ti?
- **Player:** Bueno, hace bastante tiempo, Edmond de Ardougne me encargó encontrar a su hija secuestrada, Elena.
- **Gwir:** No había oído hablar de estas personas antes. ¿Dices que fue secuestrada?
- **Player:** Secuestrado y llevado a West Ardougne, sí. Era la primera vez que entré, así que tuvimos que pasar por las alcantarillas, pero lo logré y finalmente localicé y devolví a Elena a su padre.
- **Gwir:** Gran historia. Es extraño pensar que todo empezó de forma tan diferente para ti.
- **Gwir:** Entonces ingresaste a West Ardougne por primera vez y liberaste a Elena de sus captores. ¿Qué pasó después para ti?
- **Player:** Una buena pregunta. Fue en ese momento que me di cuenta de que Elena estaba, de hecho, investigando la plaga en sí. La ayudé a recuperar su destilador de manos de los dolientes para que pudiera continuar con su trabajo.
- **Gwir:** Déjame adivinar: ¿su trabajo reveló que la plaga era una mentira?
- [Menu]: Selecciona una opción
  - [Choice]: si,
    - (continue)
  - [Choice]: Oye, deja de interrumpir, te cuento lo que pasó.
    - **Player:** Oye, deja de interrumpir, te cuento lo que pasó.
    - **Gwir:** Pido disculpas, Player, por favor continúa.
    - (continue)
- **Player:** Sí, los hallazgos de la muestra de Elena revelaron que la plaga era una mentira.
- **Gwir:** ¿Qué hiciste cuando descubriste esto?
- **Player:** Fui directamente al propio King Lathas. Admitió todo el asunto, pero defendió sus acciones diciendo que aislar a West Ardougne era necesario para contener una amenaza mucho mayor para el resto de Gielinor.
- **Gwir:** ¿Y esta amenaza fue?
- **Player:** Iban. El siguiente paso de esta historia.
- **Gwir:** Entonces, en Iban es donde continúa esta historia. Iban es conocido por nosotros los elfos: no ingresamos al Underground Pass debido a las pérdidas que sufrimos allí en la antigüedad.
- [Menu]: Selecciona una opción
  - [Choice]: Dejen de desviar las cosas, esta es mi historia.
    - **Player:** Deja de desviar las cosas, esta es mi historia.
    - **Gwir:** Pido disculpas, Player, por favor continúa.
    - (continue)
  - [Choice]: ¿Qué pasó con los elfos?
    - **Player:** ¿Qué pasó con los elfos?
    - **Gwir:** Bueno, no estoy seguro de qué tan familiarizado estás con la historia de los elfos, pero solíamos ocupar las tierras del este.
    - **Gwir:** Llegó el momento en que se perdió el contacto entre los elfos de Isafdar y aquellos que habían viajado al este. Cuando eso sucedió, hubo un éxodo masivo hacia el oeste de aquellos elfos que habían abandonado su hogar en el bosque. ellos sufrieron
    - **Gwir:** innumerables pérdidas en el viaje a través de Underground Pass y ningún elfo ha vuelto a pisarlo desde entonces.
    - **Gwir:** Pero sigamos adelante. Se trata de tu propio viaje a través de Underground Pass.
    - (continue)
- **Player:** Eso decía. King Lathas temía la amenaza de Iban y me envió al Underground Pass para investigar y encontrar un camino a estas tierras.
- **Gwir:** ¿Qué pasó después?
- **Player:** Encontré el camino hasta el fondo del Underground Pass, donde combiné los cuatro elementos de Iban con un muñeco, que finalmente arrojé al Pozo del Viaje.
- **Player:** Esto derrotó a Iban y limpió el área, reabriendo el pozo y otorgando finalmente acceso a las tierras élficas.
- **Gwir:** Y creo que la siguiente parte de tu historia es donde nuestros destinos comienzan a entrelazarse...
- **Gwir:** Entonces continuemos. Habías atravesado el Underground Pass y llegaste a estas tierras por primera vez.
- **Player:** Sí. Después de una confrontación inicial (una emboscada de los elfos), navegué por los bosques hasta encontrar el campamento de Lord Iorwerth.
- **Gwir:** ¿Iorwerth? ¿El líder de los elfos oscuros?
- **Player:** Lo mismo. Desafortunadamente, creía que estaba trabajando del lado del bien, matando al supuestamente malvado Rey Tyras.
- **Player:** No entraré en detalles, pero aprendí sobre los explosivos, lo que llevó a catapultar una bomba de barril, matando a Tyras en el incendio que siguió.
- **Gwir:** No es el mejor momento de la historia.
- **Player:** Efectivamente no, pero al menos la verdad salió a la luz. En el camino de regreso para informar esta noticia a King Lathas, conocí a Arianwyn por primera vez. Él reveló la mentira y que, de hecho, era bueno en cierto modo, ya que me había ganado la confianza de King Lathas. yo
- **Player:** podría usar esa confianza para infiltrarse más profundamente en esta conspiración que cualquier elfo.
- **Gwir:** Bueno, el viaje puede haber sido difícil, pero al menos expuso la verdad y te permitió ganarte su confianza. ¿Qué pasó después?
- (continue)

#### Después de Roving Elves

- **Player:** A continuación yo...
- **Player:** I...
- **Player:** Ah, sí, de hecho me detuve para ayudar a Islwyn. Me reveló que es nieto de Glarial.
- **Gwir:** Gracioso Glarial.
- **Player:** Sí, sé que los elfos la valoran mucho. Islwyn se alegró de saber que su lugar de descanso final era la cascada que había elegido Baxtorian, pero su tumba no estaba consagrada.
- **Gwir:** ¿Entonces realizaste dicha consagración? Es muy noble de tu parte cumplir los deseos de Islwyn. Glarial, de hecho, descansa en paz, si tan solo tuviera a Baxtorian para descansar con ella...
- [Menu]: Selecciona una opción
  - [Choice]: Sigue hablando.
    - (continue)
  - [Choice]: Pregunta más sobre Baxtorian.
    - **Player:** Hablas en una especie de acertijo. ¿Qué pasó exactamente con Baxtorian?
    - **Gwir:** Nuestro gran rey de antaño, el más poderoso de todos nosotros, tenía tanto poder. Cuando regresó a su casa en el este y descubrió que Glarial había desaparecido, después de años de buscarla, entró en la cascada y nunca volvió a aparecer.
    - **Player:** Espera, ¿entró y nunca salió? Entonces ¿dónde está su cuerpo?
    - **Gwir:** Una buena pregunta; ¿dónde de hecho?
    - (continue)
- **Player:** ...
- **Player:** Bueno, eso fue lo que pasó. Después de la consagración, Eluned, que viaja con Islwyn, estaba listo para encargarme nuevamente.
- (continue)

#### Después de Mourning's End Parte I

- **Gwir:** Entonces, ¿dices que Eluned habló contigo después de la consagración? ¿Me imagino que fue ella quien te trajo de regreso a Arianwyn?
- **Player:** Sí, pero ¿cómo lo supiste?
- **Gwir:** Bueno, esto es un poco más reciente, así que espero tener ya los datos.
- **Player:** Eso debería ahorrarme un poco de conversación, así que te ayudaré asegurándome de que tengas información precisa.
- **Gwir:** ¡Genial! Entonces Arianwyn te contó que los dolientes eran elfos oscuros disfrazados que trabajaban desde su puesto de avanzada en West Ardougne.
- **Player:** Correcto, pero el puesto avanzado está, de hecho, debajo de Ardougne, no dentro de él.
- **Gwir:** Oh, gracias, déjame hacer ese cambio. Bien, entonces conseguiste un traje de doliente y te infiltraste en el puesto de avanzada.
- **Player:** Sí, lo hice, donde conocí al jefe de los dolientes.
- **Gwir:** Tengo entendido que fue él quien te contó sus planes, diciendo que estaban exagerando la amenaza a Lathas para que él les concediera el control.
- **Player:** Exacto. Como Lathas temía a Underground Pass, estaba feliz de que gobernaran de alguna manera West Ardougne, fingieran la plaga y lo aislaran.
- **Gwir:** Desafortunadamente, esto era precisamente lo que querían: tiempo y espacio para excavar debajo.
- **Player:** De hecho, estaban cavando, y después de que me probé a mí mismo al continuar con sus esfuerzos para fingir la plaga, el jefe de los dolientes finalmente confió en mí lo suficiente como para informarme que estaban buscando una antigua fuente de poder élfico... Algo que podría acelerar el regreso de su 'Señor Oscuro'.
- **Gwir:** Esta fuente de poder presumiblemente es el Templo de la Luz...
- (continue)

#### Después de Mourning's End Parte II

- **Player:** El Templo de la Luz fue la siguiente parte de mi búsqueda. Investigué el área y encontré un equipo cerca de la entrada.
- **Gwir:** ¿Asumo que perecieron a manos de las sombras?
- **Player:** De hecho. Hasta el día de hoy los dolientes todavía no lo han encontrado. Les digo que todavía estoy buscando a la tripulación desaparecida, pero que espero que nunca descubran la situación real.
- **Gwir:** Bueno, no creo que lo hagan. ¿Ya tengo documentado que usted mismo reinició las salvaguardias y defensas del templo para hacerlo seguro una vez más?
- **Player:** Me alegra decirte que tienes razón; Las salvaguardias del templo están intactas. No veo que los dolientes sean una amenaza particular ahora, a menos que encuentren alguna otra fuente de poder. Por supuesto, ¡y ni siquiera intentarán encontrar otra fuente hasta que descubran el templo y se encuentren incapaces de penetrar sus defensas!
- **Gwir:** Así que las defensas del Templo de la Luz están activas: es seguro y los dolientes están debilitados sin que ellos lo sepan. ¿Qué pasó después?
- (continue)

#### Después de Within The Light

- **Player:** Arianwyn me llamó una vez más. Thorgel, un enano que conocí en el templo, había enviado un mensaje del templo liberando algún tipo de energía. Estaba claro que Arianwyn sabía que esto llevaría a alguna parte, así que, después de algunas tareas, se disfrazó y fuimos a investigar juntos.
- **Gwir:** ¿A dónde condujo esta investigación?
- **Player:** Bueno, con la visión de Arianwyn, me llevó a recibir energía de una manera similar al cristal que usé para reiniciar las defensas del templo.
- **Gwir:** ¿Y esto era seguro?
- **Player:** Sobreviví, si a eso te refieres. La energía no fue letal, pero de alguna manera... ¿me transportó?
- **Gwir:** ¿Te transportas a dónde?
- **Player:** Hacia la luz misma. Los elfos que construyeron ese templo debieron ser poderosos, en verdad. Había otra sección entera con más interruptores de luz.
- **Gwir:** Entonces, ¿qué hicieron estos interruptores?
- **Player:** Después de descubrir cómo activar los interruptores, finalmente logré abrir la enorme puerta de la habitación. Conducía a un pasillo que lamentablemente había sido víctima de un gran derrumbe.
- **Gwir:** ¿Este corredor seguía siendo within the light o estaba nuevamente en el mundo real, por así decirlo?
- **Player:** Una gran pregunta. O seguía siendo within the light o servía de puente entre el Templo de la Luz y algún otro lugar.
- **Gwir:** ¿Qué te hace pensar eso?
- **Player:** Un cuerpo... había un cuerpo allí. Era un mensajero elfo muerto que debió haber perecido en el desprendimiento de rocas. El informe que llevaba es donde me enteré del destino de Prifddinas.
- **Gwir:** Esto lo he oído, ¡todo el mundo habla de ello! La revelación de que la ciudad volvió a su forma de cristal... ¡una ciudad entera!
- **Player:** De hecho, y ahora mismo hay mineros trabajando para limpiar ese derrumbe para que podamos trabajar en la restauración de la ciudad, una vez que se eliminen todas las amenazas.
- (continue|filledgaps)

#### Después de compartir la historia de tu misión completada más recientemente

- **Gwir:** Ah. Hemos cubierto todo lo que podemos por ahora; gracias por toda tu ayuda. Si regresa y nos ayuda más, venga a verme para que pueda mantener mis registros actualizados.
- **Player:** Por supuesto, nos vemos pronto.

#### Después de que se haya compartido la historia final

- **Gwir:** {{anchor|filledgaps}}Eso estuvo genial, muchas gracias. Creo que eso ha llenado todos los vacíos. Será mejor que empiece a escribir todo esto correctamente. Si alguna vez necesitas un repaso de lo que sucedió, con gusto te contaré todo lo que ha sucedido hasta la fecha.
- **Player:** Encantado de poder ayudar, Gwir. Nos vemos pronto.

#### Después de que se hayan compartido todas las historias

- **Gwir:** Oh, ya has hecho suficiente ayudándome a documentar los eventos hasta ahora, pero ¿puedo recordártelo si lo has olvidado?
- (continue|eventssofar)

### Having your story told back to you{{anchor|eventssofar}}

- **Player:** ¿Puedes recordarme los acontecimientos hasta ahora?
- **Gwir:** Por supuesto, déjame ver...
- [Menu]: ¿Qué te gustaría decir?{{anchor|remindme}}
  - [Choice]: Recuérdame la plaga.
    - (abajo2|ciudad-plaga)
  - [Choice]: Me recuerdan al biohazard.
    - (abajo2|biohazard)
  - [Choice]: Me recuerdan al Underground Pass.
    - (abajo2|paso subterráneo)
  - [Choice]: Más opciones.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Recuérdame lo que le pasó a Tyras.
        - (abajo2|regicide)
      - [Choice]: Recuérdame sobre Islwyn y Eluned.
        - (abajo2|ellos itinerantes)
      - [Choice]: Recuérdame lo de los dolientes.
        - (abajo2|mep1)
      - [Choice]: Recuérdame el Templo de la Luz.
        - (abajo2|mep2)
      - [Choice]: Más opciones.
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: Recuérdame lo que pasó within the light.
            - (abajo2|dentro de la luz)
          - [Choice]: Recuérdame cómo se volvió a cultivar Prifddinas.
            - (abajo2|envío de plaga)
          - [Choice]: volver al inicio
            - (previous2)
          - [Choice]: En realidad, no te preocupes.
            - **Player:** En realidad, no te preocupes.

#### Plague City

- (Condition: If Plague City is the only story described so far:)
  - **Gwir:** Sólo me has hablado de la plaga...
- {{anchor|plague-city}}**Player:** Me recuerdan a la plaga.
- **Gwir:** Me enteré de que Edmond de Ardougne te encargó encontrar a su hija secuestrada, Elena.
- **Player:** Ah, sí, Elena, por supuesto.
- **Gwir:** También dijiste que era la primera vez que ingresabas a West Ardougne. Pasaste por las alcantarillas para finalmente localizar y devolver a Elena a su padre.
- **Gwir:** ¿Necesitas ayuda con algo más?
- (previous|remindme)

#### Biohazard

- {{anchor|biohazard}}**Player:** Me recuerdan al biohazard.
- **Gwir:** Claro. Tengo entendido que fue en este punto que te diste cuenta de que Elena estaba investigando la plaga. La ayudaste a recuperar su destilador de manos de los dolientes para poder continuar con su trabajo.
- **Player:** ¡Sí! Lo recuerdo, todo está regresando a mí ahora.
- **Gwir:** Aquí dice que descubriste que la plaga era una mentira. Fuiste directamente al propio King Lathas, quien admitió todo el asunto, pero defendió sus acciones diciendo que bloquear a West Ardougne estaba ayudando a
- **Gwir:** una amenaza mucho mayor para el resto de Gielinor.
- **Gwir:** ¿Necesitas ayuda con algo más?
- (previous|remindme)

#### Underground Pass

- {{anchor|undergroundpass}}**Player:** Me recuerdan al Underground Pass.
- **Gwir:** No hay problema. Tengo escrito aquí que para ti todo se trataba de Iban.
- **Player:** Iban, ¿cómo podría olvidarme de él?
- **Gwir:** Me enteré de que encontraste el camino hasta el fondo de Underground Pass, donde combinaste cuatro elementos de Iban con un muñeco, que arrojaste al Pozo del Viaje para derrotarlo.
- **Gwir:** Después de esta derrota, el área fue limpiada y el pozo volvió a otorgar acceso a las tierras élficas.
- **Gwir:** ¿Necesitas ayuda con algo más?
- (previous|remindme)

#### Regicide

- {{anchor|regicide}}**Player:** Recuérdame lo que le pasó a Tyras.
- **Gwir:** No es tu mejor momento en los libros de historia...
- **Gwir:** Desafortunadamente, te hicieron creer que Iorwerth estaba del lado del bien y te enteraste de los explosivos que usaste para matar al rey Tyras.
- **Player:** Ah, sí, no es mi mejor momento, de hecho.
- **Gwir:** Quizás no, pero al menos la verdad salió a la luz. Cuando viniste a informar esta noticia a King Lathas, Arianwyn te interceptó, reveló la mentira y lo buena que era en cierto modo, ya que te habías ganado la confianza de King Lathas. Esto te permitiría
- **Gwir:** para infiltrarse más profundamente en esta conspiración que cualquier elfo.
- **Gwir:** ¿Necesitas ayuda con algo más?
- (previous2|remindme)

#### Roving Elves

- {{anchor|rovingelves}}**Player:** Recuérdame sobre Islwyn y Eluned.
- **Gwir:** Ah, sí, Eluned y Islwyn.
- **Gwir:** Hablaste de cómo ayudaste a Islwyn a consagrar la tumba de Glarial.
- **Player:** Glarial, efectivamente, descansa en paz. Si tan solo tuviera Baxtorian para descansar con ella.
- **Gwir:** ¿Necesitas ayuda con algo más?
- (previous2|remindme)

#### Mourning's End Parte I

- {{anchor|mep1}}**Player:** Recuérdame a los dolientes.
- **Gwir:** Fue en este punto que descubriste que los dolientes eran elfos oscuros disfrazados, trabajando en su puesto de avanzada bajo West Ardougne.
- **Gwir:** Tengo entendido que fue el jefe de los dolientes quien te contó sus planes, diciendo que estaban exagerando el hilo hacia Lathas para que él les otorgara el control.
- **Player:** Exacto. Como Lathas temía a Underground Pass, estaba feliz de que gobernaran de alguna manera West Ardougne, fingieran la plaga y lo aislaran.
- **Gwir:** Desafortunadamente, esto era precisamente lo que querían: tiempo y espacio para excavar debajo. Comenzaron a buscar una antigua fuente de poder élfico... Algo que pudiera acelerar el regreso de su 'Señor Oscuro'.
- **Gwir:** ¿Necesitas ayuda con algo más?
- (previous2|remindme)

#### Mourning's End Parte II

- {{anchor|mep2}}**Player:** Me recuerdan al Templo de la Luz.
- **Gwir:** El Templo de la Luz fue el siguiente paso de tu búsqueda. Ya tengo documentado que reiniciaste las salvaguardias y defensas del templo para hacerlo seguro una vez más.
- **Player:** Me alegra poder decir que es correcto; Las salvaguardias del templo están intactas.
- (Condition: Before Plague's End:)
  - **Player:** No veo que los dolientes sean una amenaza particular ahora, a menos que encuentren alguna otra fuente de poder. Por supuesto, ¡y ni siquiera intentarán encontrar otra fuente hasta que descubran el templo y se encuentren incapaces de penetrar sus defensas!
  - (continue)
- (Condition: After Plague's End:)
  - **Gwir:** Por supuesto, los Mourners finalmente encontraron otra fuente de poder... pero esa es una historia diferente.
  - (continue)
- **Gwir:** ¿Necesitas ayuda con algo más?
- (previous2|remindme)

#### Within The Light

- {{anchor|withinthelight}}**Player:** Recuérdame lo que pasó within the light.
- **Gwir:** Bueno, Arianwyn pidió tu ayuda una vez más. Después de algunas tareas, se disfrazó y ambos se fueron a investigar.
- **Gwir:** Esto te llevó a recibir energía de manera similar al cristal que usaste para reiniciar las defensas del templo.
- **Gwir:** Luego entraste en la luz misma. Después de descubrir cómo activar algunos interruptores allí, se abrió una enorme puerta en la habitación que conducía a un pasillo, que desafortunadamente se había derrumbado.
- **Gwir:** Había un mensajero elfo muerto allí que debió haber perecido en el desprendimiento de rocas. Fue su informe el que nos reveló a todos el destino de Prifddinas. La ciudad volvió a su forma de cristal... ¡una ciudad entera!
- (Condition: Before Plague's End:)
  - **Player:** De hecho, y ahora mismo hay mineros trabajando para limpiar ese derrumbe para que podamos trabajar en la restauración de la ciudad, una vez que se eliminen todas las amenazas.
  - (continue)
- **Gwir:** ¿Necesitas ayuda con algo más?
- (previous2|remindme)

#### El fin de la plaga

- {{anchor|plaguesend}}**Player:** Recuérdame cómo se volvió a cultivar Prifddinas.
- **Gwir:** Bueno, los mineros terminaron de limpiar el corredor entre el Templo de la Luz y Prifddinas, por lo que Arianwyn pidió tu ayuda por última vez.
- **Gwir:** Ustedes dos se infiltraron en Entrañas Prifddinas disfrazados de Mourners y descubrieron que Lord Iorwerth tenía un nuevo plan: convocar al Señor Oscuro asesinando a toda la población de West Ardougne.
- **Gwir:** Fuiste a Ardougne y comenzaste una revolución que expulsó a los dolientes de la ciudad, y [killed King Lathas/sent King Lathas into exile].
- **Gwir:** Luego, regresaste a las tierras de los elfos y encontraste a los líderes del clan de los elfos que habían estado escondidos desde que Lord Iorwerth tomó el control de la ciudad.
- **Gwir:** Con la ayuda de los líderes del clan, activaste el Sello de Seren. El Señor Oscuro apareció y trató de detenerte, pero lo derrotaste.
- **Gwir:** ¡Gracias a ti, la ciudad de Prifddinas volvió a crecer y los elfos ahora pueden vivir en paz!
- (previous2|remindme)

### Task System {{anchor|tasksystem}}

- (Condition: If the Medium Tirannwn achievements have been completed and the rewards not claimed:)
  - **Player:** He completado todas las tareas medianas del conjunto Tirannwn.
  - **Gwir:** Así que sí. Tengo un carcaj especial reservado para ti.
  - [Gwir te entrega un carcaj y una lámpara.]
  - **Gwir:** Ahí lo tienes, que te proteja en tus viajes. Ah, y alguien me dio esta lámpara, pero no la uso.
  - **Player:** ¡Gracias!
  - **Gwir:** Cuando llevas puesto el carcaj en Tirannwn, puedes atravesar trampas de veneno sin miedo, luchar contra criaturas de las sombras más fácilmente y teletransportarte al Campamento Tyras o a la mazmorra Poison Waste. Sin llevarlo puesto te has ganado el derecho
  - **Gwir:** para usar la zona de hongos entre Tyras Camp y Poison Waste, usa menos cargas cuando uses tu arco y escudo de cristal y podrás reclamar hasta 30 alquitrán de pantano gratis por día de Lletya General Store. Ah, y esos molestos grenwalls ya no necesitarán que les pongan cebo en las trampas.
  - (continue)
- (Condition: If the player has lost their Tirannwn quiver 2:)
  - **Gwir:** ¡Ah, el portador de la aljaba! ¿Cómo lo estás encontrando?
  - **Player:** Lo perdí.
  - **Gwir:** ¡Oh, no!
  - **Gwir:** No importa, tengo otro. Aquí...
  - [Gwir te entrega un carcaj.]
  - (receives=Tirannwn quiver 2)
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: Háblame del Sistema de Logros.
    - **Gwir:**  Muy bien: el sistema de logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
    - **Gwir:** Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
    - **Gwir:** Algunos también ofrecen elementos que ayudarán a completar otras tareas y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
    - Elige una opción:
      - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
        - **Player:**  Cuéntame sobre la recompensa establecida para esta área.
        - **Gwir:** Por completar el conjunto Tirannwn, recibirás un carcaj.
        - **Gwir:** Este carcaj será cada vez más útil a medida que completes conjuntos de tareas de mayor dificultad.
        - **Gwir:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
        - También puede seleccionar una tarea (indicada en la interfaz principal del Sistema de tareas por un pequeño ícono de escudo) y elegir 'Recompensas' para ver qué recompensas proporciona un elemento determinado.
        - (previous)
      - [Choice]: ¿Cómo reclamo estas recompensas?
        - **Player:**  ¿Cómo reclamo las recompensas?
        - **Gwir:**  Debes completar todas las tareas dentro de un conjunto de dificultad particular y luego podrás reclamar tu recompensa.
        - **Gwir:** Algunas de las tareas del conjunto Tirannwn son simples, algunas requieren cierto skill levels y otras requieren que se inicien o completen misiones.
        - **Gwir:** Para reclamar las recompensas del conjunto Tirannwn, habla con Elven Tracker cerca de Lodestone, Arianwyn en la ciudad, Elen en la ciudad o conmigo mismo.
        - (previous)
      - [Choice]: Lo siento, me estaba yendo.
        - (end)
  - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
    - [Menu]: Elige una opción:
      - [Choice]: Tirannwn carcaj 1
        - **Gwir:** Tirannwn carcaj 1? Sí, pero me temo que te costaría 5.000 coins.
        - [Menu]: ¿Comprar otro por 5.000 coins?
          - [Choice]: si
            - [Te entregan otro carcaj Tirannwn 1.]
            - (receives=Tirannwn quiver 1) (removes= 5,000 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Tirannwn carcaj 2
        - **Gwir:** ¿Tirannwn carcaj 2? Sí, pero me temo que te costaría 10.000 coins.
        - [Menu]: ¿Comprar otro por 10.000 coins?
          - [Choice]: si
            - [Te entregan otro carcaj Tirannwn 2.]
            - (receives=Tirannwn quiver 2) (removes= 10,000 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Tirannwn carcaj 3
        - **Gwir:** Tirannwn carcaj 3? Sí, pero me temo que te costaría 25.000 coins.
        - [Menu]: ¿Comprar otro por 25.000 coins?
          - [Choice]: si
            - [Te entregan otro carcaj Tirannwn 3.]
            - (receives=Tirannwn quiver 3) (removes= 25,000 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Tirannwn carcaj 4
        - **Gwir:** Tirannwn carcaj 4? Sí, pero me temo que te costaría 50.000 coins.
        - [Menu]: ¿Comprar otro por 50.000 coins?
          - [Choice]: si
            - [Te entregan otro carcaj Tirannwn 4.]
            - (receives=Tirannwn quiver 4) (removes= 50,000 coins)
          - [Choice]: No
            - **Player:** No, gracias.
  - [Choice]: Lo siento, me estaba yendo.
    - (end)
