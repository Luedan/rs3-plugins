# TokHaar-Hok

- **Original Wiki Page**: [Transcript:TokHaar-Hok](https://runescape.wiki/w/Transcript%3ATokHaar-Hok)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Antes de sacrificar la capa de fuego.

- **TokHaar-Hok:** Hablemos...
- [Menu]: Elige una opción:
  - [Choice]: La última vez que estuve aquí, ¿hablaste de una batalla?
    - **TokHaar-Hok:** Las escaramuzas en las que participamos la última vez que estuviste aquí fueron entretenidas, pero no excedieron nuestras capacidades.
    - **TokHaar-Hok:** Un verdadero desafío es todo lo que deseamos...
    - **TokHaar-Hok:** Hemos oído que los TzHaar compiten por una capa compuesta exclusivamente de fuego...
    - [Menu]: Selecciona una opción
      - [Choice]: Continúe.
        - (continue)
      - [Choice]: ¿Cómo sabes eso?
        - **TokHaar-Hok:** Las bestias han vagado por aquí y hemos fundido su ser en nosotros. Algunas de estas bestias lucharon en lo que llamáis 'La Cueva de la Lucha'.
        - **Player:** Está bien. Sigue...
        - (continue)
    - **TokHaar-Hok:** Alguien que poseyera tal capa sería digno de nuestro desafío.
    - (Condition: If a fire cape is not in the backpack or bank:)
      - **Player:** Iré a ver si puedo ganarme uno.
    - (Condition: With a fire cape in the bank:)
      - **Player:** Tengo uno, pero no lo llevo encima.
      - **TokHaar-Hok:** Tráelo aquí...
    - (Condition: With a fire cape in the backpack:)
      - **Player:** Tengo una capa de fuego aquí...
      - **TokHaar-Hok:** Debes sacrificarlo...
      - [Menu]: Selecciona una opción
        - [Choice]: Eh... ¿Qué?
          - **TokHaar-Hok:** Demuestra que estás por encima de los desafíos que TzHaar te plantearía y acepta un nuevo nivel de desafío. Esa capa limita tu potencial...
          - (continue)
        - [Choice]: Si eso es lo que quieres.
          - (continue)
        - [Choice]: No voy a hacer eso.
          - **TokHaar-Hok:** Esa es tu elección.
      - [¿Te gustaría sacrificar tu capa de fuego? Obtendrás entrada permanente al Fight Kiln, pero perderás una capa de fuego. Siempre puedes ganar una nueva capa de fuego derrotando a Jad en Fight Cave nuevamente.]
      - [Menu]: ¿Estás seguro de que quieres destruir tu capa de fuego?
        - [Choice]: si
          - (removes=fire cape)
          - (Action: el player le da su capa de fuego a TokHaar-Hok, quien la rompe por la mitad. el player se protege del fuego que se escapa de la capa.)
          - [TokHaar-Hok destruye tu capa de fuego.]
          - **TokHaar-Hok:** Excelente... excelente... Si estás preparado para asumir nuestro desafío, podríamos comenzar de inmediato... Tenemos hambre de ello.
          - **TokHaar-Hok:** ¿Tiene alguna pregunta sobre las reglas de enfrentamiento?
          - [Menu]: Selecciona una opción
            - [Choice]: No, peleemos.
              - **Player:** No, solo peleemos.
              - (Action: La pantalla se desvanece y vuelve a aparecer. Comienza Fight Kiln.)
            - [Choice]: No, simplemente peleemos. Y hazlo rápido.
              - **Player:** No, solo peleemos. Y hazlo rápido.
              - (Action: La pantalla se desvanece y vuelve a aparecer. Comienza Fight Kiln.)
            - [Choice]: ¿Qué obtengo si te gano?
              - **TokHaar-Hok:** Sobrevive contra nosotros y te ofreceremos varias recompensas.
              - **TokHaar-Hok:** La primera opción es una capa que forjaremos con la obsidiana que nos atraviesa. Aumentará tu fuerza en el combate.
              - **TokHaar-Hok:** Si lo prefieres, podemos darte un ónix sin cortar que arrancamos del suelo de nuestro horno como marca de tu victoria.
              - **TokHaar-Hok:** ¿Alguna otra pregunta, humano?
              - (previous)
            - [Choice]: ¿Cuáles son las reglas?
              - **TokHaar-Hok:** No puedes abandonar el horno hasta que te hayas enfrentado a todo lo que queremos lanzarte en tu contra. Al hacerlo, admitirás la derrota y tendrás que empezar de nuevo.
              - "Tenga en cuenta: puede cerrar sesión durante una ola y regresar a donde estaba cuando vuelva a iniciar sesión".
              - **TokHaar-Hok:** Le proporcionaremos cristales que se han formado debajo de la corteza de nuestro hogar. Estos tienen propiedades mágicas que pueden mejorar tus habilidades. No los sacarás de nuestro horno.
              - **TokHaar-Hok:** Eso es todo. Sobrevive contra nosotros durante 37 oleadas de nuestro ataque y te recompensaremos.
              - **TokHaar-Hok:** ¿Tiene alguna otra pregunta?
              - (previous)
        - [Choice]: No
          - **TokHaar-Hok:** Esa es tu elección.
  - [Choice]: Me gustaría hablar más sobre usted y los de su especie.
    - **TokHaar-Hok:** Continúa.
    - (continue|Who-are-you)

#### Diálogo estándar

- **TokHaar-Hok:** Hablemos...
- [Menu]: Elige una opción:
  - [Choice]: Luchemos.
    - **TokHaar-Hok:** ¿Tiene alguna pregunta sobre las reglas de nuestro compromiso?
    - [Menu]: Selecciona una opción
      - [Choice]: No, peleemos.
        - **Player:** No, solo peleemos.
        - (Action: La pantalla se desvanece y vuelve a aparecer. Comienza Fight Kiln.)
      - [Choice]: No, simplemente peleemos. Y hazlo rápido.
        - **Player:** No, solo peleemos. Y hazlo rápido.
        - (Action: La pantalla se desvanece y vuelve a aparecer. Comienza Fight Kiln.)
      - [Choice]: ¿Qué obtengo si te gano?
        - **TokHaar-Hok:** Sobrevive contra nosotros y te ofreceremos varias recompensas.
        - **TokHaar-Hok:** La primera opción es una capa que forjaremos con la obsidiana que nos atraviesa. Aumentará tu fuerza en el combate.
        - **TokHaar-Hok:** Si lo prefieres, podemos darte un ónix sin cortar que arrancamos del suelo de nuestro horno como marca de tu victoria.
        - **TokHaar-Hok:** ¿Alguna otra pregunta, humano?
        - (previous)
      - [Choice]: ¿Cuáles son las reglas?
        - **TokHaar-Hok:** No puedes abandonar el horno hasta que te hayas enfrentado a todo lo que queremos lanzarte en tu contra. Al hacerlo, admitirás la derrota y tendrás que empezar de nuevo.
        - "Tenga en cuenta: puede cerrar sesión durante una ola y regresar a donde estaba cuando vuelva a iniciar sesión".
        - **TokHaar-Hok:** Le proporcionaremos cristales que se han formado debajo de la corteza de nuestro hogar. Estos tienen propiedades mágicas que pueden mejorar tus habilidades. No los sacarás de nuestro horno.
        - **TokHaar-Hok:** Eso es todo. Sobrevive contra nosotros durante 37 oleadas de nuestro ataque y te recompensaremos.
        - **TokHaar-Hok:** ¿Tiene alguna otra pregunta?
        - (previous)
  - [Choice]: Me gustaría hablar más sobre usted y los de su especie.
    - **TokHaar-Hok:** Continúa.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Quién eres?
        - **TokHaar-Hok:** Somos... los TokHaar.
        - **TokHaar-Hok:** Fuimos forjados para construir las montañas de Gielinor... aunque entonces tenían un nombre diferente. Nuestros maestros nos forjaron en este horno.
        - **TokHaar-Hok:** Cuando terminamos nuestro trabajo, construimos una gran montaña alrededor de este Horno y volvimos a vivir dentro de él... para esperar más instrucciones.
        - **TokHaar-Hok:** O, al menos... algunos de nosotros lo hicimos. Algunos de nosotros nos quedamos en la montaña.
        - **Player:** ¿El TzHaar?
        - **TokHaar-Hok:** Ah... sí... ahora se llaman a sí mismos TzHaar.
        - **TokHaar-Hok:** Eligieron vivir dentro de la montaña que habíamos construido. Hicieron túneles a través de él para construir sus ciudades... socavando nuestro gran propósito.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Cómo puedes hablar mi idioma?
            - **TokHaar-Hok:** En ocasiones, criaturas... como tú... han entrado en nuestra casa.
            - **TokHaar-Hok:** Debajo de tus pies fluye la lava de la creación... aquellos que caen en ella entregan su forma, recuerdos y lenguaje... Se vuelven uno con el TokHaar...
            - **TokHaar-Hok:** Muchas bestias de las cuevas circundantes han sido sumergidas en nuestro Horno.
            - **TokHaar-Hok:** Contaminan nuestra determinación... pero hay ciertas ventajas... aprendemos de ellos.
            - (previous)
          - [Choice]: ¿Cuánto tiempo llevas aquí? ¿Qué has estado haciendo?
            - **TokHaar-Hok:** No mantenemos el tiempo...humano. Estábamos aquí al principio y todavía estamos aquí.
          - [Choice]: ¿Cómo puedes hablar mi idioma?
            - **TokHaar-Hok:** Hemos estado practicando nuestras habilidades unos contra otros; perfeccionando nuestras fuerzas en anticipación del regreso de nuestros amos. El combate... es nuestro gran placer.
            - (previous)
          - [Choice]: ¿Quiénes son tus maestros?
            - **TokHaar-Hok:** Nuestros maestros fueron los diseñadores de este mundo. Fueron arquitectos de los mares y los valles, las tierras heladas del norte, las llanuras desérticas... y las montañas.
            - **TokHaar-Hok:** Éramos sus herramientas... sus constructores de montañas.
            - **TokHaar-Hok:** Construyeron el Xil para excavar la tierra y las rocas... el Mej para hacerlo explotar hasta un tamaño que el Ket pudiera transportar... y el Hur para transformar el sedimento en acantilados y laderas.
            - [Menu]: Selecciona una opción
              - [Choice]: ¿Recuerdas a tus maestros?
                - **TokHaar-Hok:** Los recordamos... sí... y esperaremos su regreso.
                - (previous)
              - [Choice]: ¿Cómo crearon tus maestros el mundo?
                - **TokHaar-Hok:** Nuestros maestros forjaron muchos poderosos artefactos de creación. Los TokHaar son uno de esos artefactos. Quizás hayas oído hablar de otra... la Piedra de Jas.
                - (previous)
              - [Choice]: ¿Tus amos son dioses?
                - **TokHaar-Hok:** No como tú los definirías.
                - **TokHaar-Hok:** Los jóvenes que ustedes, los mortales, glorifican como deidades... Son meramente seres corpóreos, de un tipo u otro, que han abusado de los artefactos de nuestro maestro para ascender a un estado superior del ser.
                - **TokHaar-Hok:** Han robado su poder y no son dignos de tu adoración.
                - (previous)
              - [Choice]: ¿Podemos hablar de otra cosa?
                - (previous2|How-can-you)
          - [Choice]: ¿Podemos hablar de otra cosa?
            - **TokHaar-Hok:** Sí...
            - (previous2|Who-are-you)
      - [Choice]: ¿Qué es este lugar?
        - **TokHaar-Hok:** Este es el Gran Horno del que fuimos forjados.
        - **TokHaar-Hok:** El Horno fue construido por nuestros maestros para formar las montañas. Hemos completado esa tarea...ahora esperamos el turno de nuestros amos...y nuevas órdenes.
        - **TokHaar-Hok:** Dentro de este horno fluye lava sagrada. A través de él, permanecemos constantes. Si somos destruidos dentro de este lugar, la lava sube y el Horno nos forja una vez más.
        - **TokHaar-Hok:** A través de esto somos uno... nuestros recuerdos compartidos por la lava. La existencia como individuos es siempre... fugaz.
        - (previous)
      - [Choice]: ¿Por qué nos perseguiste?
        - **TokHaar-Hok:** Nos disculpamos. Hace mucho tiempo que no nos enfrentamos a nadie más que a nosotros mismos. Hablar contigo y... conocer... al pequeño TzHaar despertó nuestra curiosidad.
        - **TokHaar-Hok:** Aquellos que destruiste ahora los hemos perdido. Somos nosotros los que sufrimos por nuestro deporte.
        - (previous)
      - [Choice]: ¿Estás relacionado con los TzHaar?
        - **TokHaar-Hok:** Ah... sí... no regresaron con nosotros... eligieron profanar la montaña que estaban destinados a construir y llamarse a sí mismos TzHaar.
        - **TokHaar-Hok:** Son el epítome de la debilidad y la corrupción.
        - **Player:** No entiendo.
        - **TokHaar-Hok:** Fuimos forjados para construir las montañas. Cuando terminamos, la mayoría de nosotros regresamos a este Horno.
        - **TokHaar-Hok:** Pero algunos se quedaron a vivir en esta montaña. Hicieron túneles a través de nuestro gran trabajo para crear sus ciudades y laberintos.
        - **TokHaar-Hok:** Es...antinatural...vivir fuera de nuestro Horno. Cuando somos destruidos... el Horno nos vuelve a forjar. Nuestros recuerdos permanecen como uno solo.
        - **TokHaar-Hok:** Los TzHaar se han vuelto tan... débiles. Transmiten sus recuerdos poniendo huevos sórdidamente... dejando que la lava sagrada pase de uno a otro de manera tan derrochadora.
        - **TokHaar-Hok:** Al final, se convierten en lo que ellos llaman 'TokKul', y a menudo descuidan transmitir sus conocimientos.
        - **TokHaar-Hok:** Sus recuerdos se van a desperdiciar... sin regresar a la lava sagrada. Han olvidado su gran propósito.
        - **TokHaar-Hok:** Y... ¿por qué? Para construir ciudades de desechos... santuarios de falta de respeto a nuestra gran causa... a nuestro propósito.
        - (previous)
      - [Choice]: ¿Podemos hablar de otra cosa?
        - (previous2|Lets-fight)
  - [Choice]: ¿Por qué intentaste destruir el TzHaar?
    - **TokHaar-Hok:** ¿Destruirlos? Esa nunca fue nuestra intención. Por el contrario, esperábamos... sacar a nuestros hermanos descarriados de la extinción.
    - **Player:** Explica.
    - **TokHaar-Hok:** Los TzHaar tienen defectos. Débil. Sus óvulos son frágiles y propensos a fallar, como hemos demostrado. Soportan una existencia antinatural fuera de la fuente de la creación.
    - **TokHaar-Hok:** Sin embargo, este Elder Kiln es la fuente del calor de la ciudad. Los TzHaar dependen de él para reproducirse.
    - **TokHaar-Hok:** Cada huevo de TzHaar es una imitación imperfecta de su antepasado, una copia de una copia, un fragmento de la lava sagrada que robaron del Elder Kiln.
    - **TokHaar-Hok:** Cuando los TzHaar mueren, esos preciosos recuerdos que no fueron transferidos quedan atrapados para siempre en discos aplastantes de TokKul, esperando ser liberados.
    - [Menu]: Elige una opción:
      - [Choice]: ¿Qué pasará con el TzHaar?
        - **TokHaar-Hok:** Mientras permanezcan fuera del Horno, los TzHaar están destinados a la destrucción y se debilitan con cada generación.
        - **TokHaar-Hok:** A menos que regresen al Horno, el TzHaar se degradará hasta que no quede nada de nuestros parientes caídos.
        - **TokHaar-Hok:** Los TzHaar se están desvaneciendo, perdiendo gradualmente recuerdos con cada generación.
        - **TokHaar-Hok:** Si continúan con su rumbo actual, se enfrentan a una extinción lenta pero inevitable.
        - (previous)
      - [Choice]: ¿Por qué hiciste esto?
        - **TokHaar-Hok:** Los TzHaar ya no recuerdan su verdadero propósito y aborrecen el cambio. Al cortarles el suministro de calor, esperábamos obligar a los TzHaar a actuar.
        - **TokHaar-Hok:** Aunque despreciamos la debilidad de los TzHaar, siguen siendo nuestros parientes.
        - **TokHaar-Hok:** Nos beneficiaría absorber su conocimiento y destreza en combate cada vez menores.
        - **TokHaar-Hok:** Los TokHaar son inmortales pero finitos en número; Absorber el TzHaar reforzaría nuestras filas.
        - **TokHaar-Hok:** Como esperábamos, viajaste al Elder Kiln para buscar una solución al problema.
        - **TokHaar-Hok:** Le recordaste a los TzHaar los TokHaar y el destino que les espera en TokKul.
        - **TokHaar-Hok:** Nos has servido bien.
        - (previous)
      - [Choice]: ¿Eres responsable de la creación de Ga'al?
        - **TokHaar-Hok:** Sólo esperábamos que los huevos de TzHaar nacieran muertos, lo que obligaría a los TzHaar a buscar el horno o morir. Los Ga'al son una anomalía que no anticipábamos.
        - **TokHaar-Hok:** Nos complace satisfacer tu deseo de forjar un Ga'al con un TokKul de TzHaar si eso animaba a los TzHaar a realizar más expediciones al Elder Kiln.
        - **TokHaar-Hok:** Esperábamos que si los TzHaar regresaban a su lugar de nacimiento, pudieran aprender el error de sus caminos.
        - (previous)
      - [Choice]: Tengo otras preguntas.
        - (previous2|Lets-fight|Back to options)

#### Con recompensas no reclamadas

- **TokHaar-Hok:** Hablemos...
- **TokHaar-Hok:** Lo has hecho muy bien. Para conmemorar tu triunfo, acepta un trofeo de nuestra casa.
- [Menu]: Elige tu recompensa:
  - [Choice]: cond=Only after inflicting enough damage with melee:|El TokHaar-Kal-Ket.
    - (Condition: Without backpack space:)
      - **TokHaar-Hok:** Tenemos una recompensa para ti... pero primero tendrás que hacer espacio en tu inventario. Vuelva a utilizarlo cuando pueda aceptarlo.
    - (Condition: With backpack space:)
      - [El TokHaar-Kal-Ket es una capa poderosa que permitirá que otros vean que dominas el Fight Kiln. Además de esto, proporciona varios aumentos de estadísticas, incluido un bono de 33 Strength.]
      - [Menu]: ¿Aceptar el TokHaar-Kal-Ket?
        - [Choice]: Sí.
          - (receives=TokHaar-Kal-Ket)
          - **TokHaar-Hok:** Probemos nuestra fuerza otra vez... pronto...
        - [Choice]: No.
          - **TokHaar-Hok:** ¿No? Vuelve con nosotros... cuando hayas tomado una decisión.
  - [Choice]: cond=Only after inflicting enough damage with ranged:|El TokHaar-Kal-Xil.
    - (Condition: Without backpack space:)
      - **TokHaar-Hok:** Tenemos una recompensa para ti... pero primero tendrás que hacer espacio en tu inventario. Vuelva a utilizarlo cuando pueda aceptarlo.
    - (Condition: With backpack space:)
      - [El TokHaar-Kal-Xil es una capa poderosa que permitirá que otros vean que dominas el Fight Kiln. Además de esto, proporciona varios aumentos de estadísticas, incluido un bono de 33 Ranged.]
      - [Menu]: ¿Aceptar el TokHaar-Kal-Xil?
        - [Choice]: Sí.
          - (receives=TokHaar-Kal-Xil)
          - **TokHaar-Hok:** Probemos nuestra fuerza otra vez... pronto...
        - [Choice]: No.
          - **TokHaar-Hok:** ¿No? Vuelve con nosotros... cuando hayas tomado una decisión.
  - [Choice]: cond=Only after inflicting enough damage with magic:|El TokHaar-Kal-Mej.
    - (Condition: Without backpack space:)
      - **TokHaar-Hok:** Tenemos una recompensa para ti... pero primero tendrás que hacer espacio en tu inventario. Vuelva a utilizarlo cuando pueda aceptarlo.
    - (Condition: With backpack space:)
      - [El TokHaar-Kal-Mej es una capa poderosa que permitirá que otros vean que dominas el Fight Kiln. Además de esto, proporciona varios aumentos de estadísticas, incluido un bono de 33 Magic.]
      - [Menu]: ¿Aceptar el TokHaar-Kal-Mej?
        - [Choice]: Sí.
          - (receives=TokHaar-Kal-Mej)
          - **TokHaar-Hok:** Probemos nuestra fuerza otra vez... pronto...
        - [Choice]: No.
          - **TokHaar-Hok:** ¿No? Vuelve con nosotros... cuando hayas tomado una decisión.
  - [Choice]: cond=Only after inflicting enough damage with necromancy:|El TokHaar-Kal-Mor.
    - (Condition: Without backpack space:)
      - **TokHaar-Hok:** Tenemos una recompensa para ti... pero primero tendrás que hacer espacio en tu inventario. Vuelva a utilizarlo cuando pueda aceptarlo.
    - (Condition: With backpack space:)
      - [El TokHaar-Kal-Mor es una capa poderosa que permitirá que otros vean que dominas el Fight Kiln. Además de esto, proporciona varios aumentos de estadísticas, incluido un bono de 33 Necromancy.]
      - [Menu]: ¿Aceptar el TokHaar-Kal-Mor?
        - [Choice]: Sí.
          - (receives=TokHaar-Kal-Mor)
          - **TokHaar-Hok:** Probemos nuestra fuerza otra vez... pronto...
        - [Choice]: No.
          - **TokHaar-Hok:** ¿No? Vuelve con nosotros... cuando hayas tomado una decisión.
  - [Choice]: Un ónix sin cortar.
    - [El ónix es una gema preciosa y rara que puede convertirse en uno de varios objetos poderosos, incluido el codiciado Amuleto de la furia.]
      - [Menu]: ¿Aceptar el ónix sin cortar?
        - [Choice]: Sí.
          - (receives=Uncut onyx)
          - **TokHaar-Hok:** Probemos nuestra fuerza otra vez... pronto...
        - [Choice]: No.
          - **TokHaar-Hok:** ¿No? Vuelve con nosotros... cuando hayas tomado una decisión.

### Fight Kiln


#### Inicio de la ola 1

- **TokHaar-Hok:** Entonces, aceptas nuestro desafío. Que nuestro deporte sea glorioso. Xil - ¡ataca!

#### Inicio de la ola 11

- **TokHaar-Hok:** Bien peleado, [player]. Eres feroz, pero debes luchar más rápido... La lava está subiendo.
- **TokHaar-Hok:** Nuestro Mej desea ponerte a prueba...

#### Inicio de la ola 21

- **TokHaar-Hok:** Debes estar tallado en una roca resistente a la magia... Eres un enemigo bastante digno.
- **TokHaar-Hok:** Ah, la plataforma se está desmoronando. Sé rápido, pequeño: nuestros Ket están en camino.

#### Inicio de la ola 31

- **TokHaar-Hok:** Date prisa, [player]... Mata a mis hermanos antes de que la lava te consuma.

#### Inicio de la ola 34

- **TokHaar-Hok:** ¡Increíble! Hacía mucho tiempo que no nos divertíamos tanto. Pero ahora comienza el verdadero desafío...
- **Player:** ¿El verdadero desafío?
- **TokHaar-Hok:** Muchas criaturas han entrado en el horno a lo largo de los siglos. Recordamos sus formas.

#### Inicio de la ola 37

- **TokHaar-Hok:** Te hemos lanzado muchas olas... Te has manejado como un verdadero TokHaar. Te has ganado nuestro respeto.
- **TokHaar-Hok:** Toma esta capa como símbolo de nuestro -
- **TokHaar-Hok:** Ah, sí, hay un desafío final...

#### Después de completar el horno de lucha

- **TokHaar-Hok:** Eres un TokHaar... nacido en el cuerpo de un humano. En verdad, no hemos visto tanta habilidad en nadie fuera de nuestro horno.
- **TokHaar-Hok:** Lo has hecho muy bien. Para conmemorar tu triunfo, acepta un trofeo de nuestra casa.
- [Menu]: Elige tu recompensa:
  - [Choice]: El TokHaar-Kal-[Ket/Mej/Mor/Xil].
    - (continue)
  - [Choice]: Un ónix sin cortar.
    - (continue)
- (Condition: Without one free backpack space:)
  - **Tokhaar-Hok:** Tenemos una recompensa para ti... pero primero tendrás que hacer espacio en tu inventario. Vuelve con nosotros cuando puedas aceptarlo.
  - (continue)
- (Condition: With one free backpack space:)
  - (receives=their chosen reward)
  - **TokHaar-Hok:** Probemos nuestra fuerza nuevamente... pronto...
  - (continue)
- **TokHaar-Hok:** Ahora, vete... antes de que la lava te consuma.
- (Action: La pantalla se desvanece y vuelve a aparecer.)

### Fight Cauldron

- ¡TokHaar-Hok te reta a duelo! ¿Aceptar?
  - Sí.
    - **TokHaar-Hok:** Vamos a disfrutar esto...
  - No.
    - **TokHaar-Hok:** Cobarde.
- (Mientras TokHaar-Hok se retira para curarse en la lava)
- (Uno de los siguientes TokHaar-Hok dice :)
  - **TokHaar-Hok:** {{RSChat|We require healing...}}
  - **TokHaar-Hok:** {{RSChat|We must regenerate...}}
  - (Si el player no aturde a TokHaar-Hok)
    - Golpea a TokHaar-Hok con una habilidad asombrosa. por ejemplo, revés, patada, tiro vinculante, impacto, golpe.
- (Mientras TokHaar-Hok se cura con la lava del Horno)
- (Uno de los siguientes TokHaar-Hok dice :)
  - **TokHaar-Hok:** {{RSChat|Lava of life...}}
  - **TokHaar-Hok:** {{RSChat|The lava is life!}}
  - **TokHaar-Hok:** {{RSChat|We are unstoppable!}}
  - **TokHaar-Hok:** {{RSChat|Delicious...}}
- (Después de que TokHaar-Hok se recupere completamente de la lava)
  - **TokHaar-Hok:** {{RSChat|We are whole!}}
- (Después de que TokHaar-Hok esté convocando minions)
  - **TokHaar-Hok:** {{RSChat|Now, we will crush you.}}
- (Después de que el player sorprenda a TokHaar-Hok)
  - **TokHaar-Hok:** {{RSChat|We... cannot... move...}}
- (Cuando pelea con TokHaar-Hok)
  - TokHaar-Hok agota tus puntos de oración.
