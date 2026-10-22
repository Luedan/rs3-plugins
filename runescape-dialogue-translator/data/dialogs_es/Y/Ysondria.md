# Ysondria

- **Original Wiki Page**: [Transcript:Ysondria](https://runescape.wiki/w/Transcript%3AYsondria)
- **Letter**: `Y`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Dialogue before fully cleansing the Nexus


#### Diálogo por primera vez

- **Ysondria:** Saludos, extraño. ¿Ha sido enviado para ayudarnos en la lucha para purificar esta zona de la corrupción invasora?
- {{RSFontAchievement|The Nexus Has You}}
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Ysondria:** Me alegro mucho. Necesitamos a todos los que podamos conseguir.
    - **Ysondria:** Sólo puedo esperar que todavía quieras ayudar cuando te haya dado más detalles.
    - (continue|standard)
  - [Choice]: No.
    - **Ysondria:** Eso es una pena. Aquí hay un grave peligro.
    - **Ysondria:** ¿Tal vez si escuchas mi historia estarás dispuesto a ayudar?
    - (continue|standard)

#### Diálogo estándar


##### Sin poseer un saco encantado

- **Ysondria:** ¿Te gustaría un saco encantado para poder recolectar corrupción?
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - (Condition: Without space in backpack:)
      - **Ysondria:** No tienes suficiente espacio para llevar el saco en este momento.
    - (Condition: With space in backpack:)
      - (receives=charmed sack)
      - **Ysondria:** Ahí lo tienes.
      - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
      - (continue|standard)
  - [Choice]: No.
    - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
    - (continue|standard)

##### Mientras posee un saco encantado

- **Ysondria:** Hola de nuevo, Player.
- **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Cómo puedo ayudar?
    - **Ysondria:** La fe es la respuesta.
    - **Ysondria:** La criatura es un ser de malicia y maldad; una cicatriz en nuestra tierra. De esta manera, contiene las semillas de su propia destrucción.
    - **Ysondria:** La razón por la que contaminó el área es que no puede sobrevivir en condiciones puras.
    - **Player:** ¿Entonces purificamos la tierra?
    - **Ysondria:** Aún mejor. Con nuestra fe y fuerza de espíritu canalizadas en los pilares, podemos purificar la corrupción que está arrojando y retroalimentarla a sí misma, purificándola de adentro hacia afuera.
    - **Ysondria:** De esta manera destruiremos the beast y eliminaremos su asqueroso control sobre la tierra.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Cómo funciona?
        - **Ysondria:** El Nexo por donde esa cosa intenta abrirse paso es la clave. Su corrupción, el poder que utiliza para contaminar la tierra, escapa.
        - **Ysondria:** Si recolectamos esta corrupción, la repugnante nube naranja, podemos devolverla a través de los pilares.
        - **Ysondria:** Para usar los pilares necesitas usar el poder de la oración.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Cómo ayuda la oración?
            - (below|faith)
          - [Choice]: ¿Cómo recojo la corrupción?
            - (abajo)
          - [Choice]: ¿Hay alguna manera de acelerar el proceso?
            - (abajo)
          - [Choice]: Pongámonos manos a la obra.
            - (below|business)
      - [Choice]: ¿Cómo ayuda la fe?
        - **Ysondria:** Esto es más simple de lo que parece.
        - **Ysondria:** Cada cuenco sobre los pilares está en sintonía con un aspecto diferente del espíritu: orden, caos, batalla y lealtad, para lo cual todos tienen el potencial.
        - **Ysondria:** Todo lo que tienes que hacer es reunir tu fuerza de voluntad, manteniendo firmemente el aspecto necesario en tu corazón mientras viertes la corrupción en el cuenco, y los pilares harán el resto.
        - **Ysondria:** Tu fuerza espiritual aumentará a medida que hagas esto.
        - (otro)
      - [Choice]: ¿Cómo recojo la corrupción?
        - **Ysondria:** El saco encantado que tienes ha sido tejido para permitirle contener la corrupción.
        - **Ysondria:** Ve al Nexus para recoger la corrupción.
        - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
        - (initial|standard)
      - [Choice]: ¿Hay alguna manera de acelerar el proceso?
        - **Ysondria:** Hemos descubierto que el efecto de la purificación es mucho más fuerte si cada uno de los pilares canaliza un aspecto diferente.
        - **Ysondria:** Esto parece amplificar la pureza que estamos enviando al Nexo, y puedo sentir el mal retroceder allí.
        - **Ysondria:** Sin embargo, esto tiene un efecto secundario.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Cuáles son los efectos secundarios?
            - **Ysondria:** Cuando se enoja, utiliza esta energía para intentar atravesar el Nexo.
            - **Ysondria:** Rara vez llega lejos, generalmente solo interrumpe el flujo por unos momentos, pero a veces...
            - **Player:** Continúa...
            - **Ysondria:** Él... emerge, mostrando su rostro indescriptible. Debes estar preparado para desterrarlo con cada gramo de tu voluntad si esto sucede.
            - **Ysondria:** ¡No se puede permitir que se libere!
            - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
            - (initial|standard)
          - [Choice]: Pongámonos manos a la obra.
            - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
            - (initial|standard)
      - [Choice]: Pongámonos manos a la obra.
        - (above|business)
  - [Choice]: ¿Qué está pasando aquí?
    - **Ysondria:** Nuestra hermosa tierra ha sido contaminada por ese horror. Hay que detenerlo.
    - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
    - (initial|standard)
  - [Choice]: ¿Qué es esa cosa?
    - **Ysondria:** Es una criatura de pesadillas. No sé su nombre y no deseo saberlo. Es una abominación y hay que detenerlo.
    - **Player:** ¿Qué clase de criatura es?
    - **Ysondria:** Nuevamente, no lo sé. muchos años, transformando la tierra en el pantano húmedo que ves aquí. Por eso lo llamo Grotesco.
    - [Menu]: Selecciona una opción
      - [Choice]: Si ha estado aquí durante muchos años, ¿por qué no había pruebas de ello?
        - **Ysondria:** Oh, lo hubo. ¿Alguna vez has estado en los túneles debajo de estos pantanos y has visto las manos saliendo de las paredes? Fueron la primera evidencia de este horror.
        - **Player:** ¿Por qué no hiciste algo en aquel entonces?
        - **Ysondria:** Ah, si hubiéramos sabido entonces lo que hacemos ahora, tal vez podríamos haber salvado parte de esta área; Detuvo el crecimiento de la monstruosidad.
        - **Ysondria:** Mi mentor, Augrum, vino a estudiar el área cuando se enteró de las manos. A pesar de toda su sabiduría, no tenía forma de saber el alcance del mal aquí.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Qué hizo?
            - **Ysondria:** Durante algún tiempo estudió las manos y el área circundante, pero sin saber cuán insidiosa era la criatura. Pensó que era seguro, que no estaba creciendo... que no nos haría daño.
            - **Ysondria:** Así que me envió a mí, su aprendiz, a vigilar la zona.
            - **Ysondria:** Cuando me di cuenta de la magnitud del peligro, ya era demasiado tarde.
            - **Player:** Continúa...
            - **Ysondria:** Cuando quedó claro que su poder estaba creciendo, llamé a Augrum para investigar.
            - **Ysondria:** Augrum tenía claro que la corrupción en la zona había aumentado y que, si no se controlaba, podría destruir la zona.
            - **Ysondria:** Entonces se fue a buscar ayuda para luchar contra the beast.
            - [Menu]: Selecciona una opción
              - [Choice]: ¿A dónde fue?
                - **Ysondria:** Fue a visitar a unos druidas de los que había oído hablar, lejos de aquí. Nunca dijo dónde exactamente, sólo que tenían algunas... ideas radicales.
                - **Ysondria:** Esos fueron los momentos más difíciles, estar aquí con ese mal creciendo, sin saber cuándo, o si, Augrum iba a regresar.
                - **Player:** ¿Pero lo hizo?
                - **Ysondria:** Sí. Después de muchos meses regresó. Esto fue hace sólo unos días. Vino con algunos de los druidas de los que había hablado (hombres salvajes con ojos desorbitados y túnicas hechas jirones) llevando los cuatro pilares que ves aquí entre ellos.
                - **Ysondria:** Augrum estaba muy enfermo cuando regresó; era un old man y el viaje le había pasado factura. Además, el precio que pagó por la ayuda de los druidas fue... alto.
                - **Player:** ¿Cuánto cuesta?
                - **Ysondria:** No puedo atreverme a hablar de eso ahora. Baste decir que murió por la causa de proteger la tierra. Quizás más adelante hablemos más sobre esto.
                - [Menu]: Selecciona una opción
                  - [Choice]: ¿Qué hicieron los druidas?
                    - **Ysondria:** Los druidas no hablaron, ni siquiera con Augrum. Simplemente colocaron el pilar en la formación que ves y cavaron los canales. Cuando terminaron, simplemente se fueron.
                    - **Ysondria:** Pasé la mayor parte de ese tiempo con Augrum, mientras él me explicaba cómo se pueden usar los pilares para hacer retroceder al mal.
                    - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
                    - (initial|standard)
                  - [Choice]: Pongámonos manos a la obra.
                    - (above|business)
              - [Choice]: Pongámonos manos a la obra.
                - (above|business)
          - [Choice]: Pongámonos manos a la obra.
            - (above|business)
      - [Choice]: Pongámonos manos a la obra.
        - (above|business)
  - [Choice]: ¿Quién eres?
    - **Ysondria:** Soy Ysondria: Guardián del Nexo. Es mi responsabilidad asegurarme de que la monstruosidad que intenta abrirse paso no salga y propague su maldad en otros lugares.
    - **Player:** ¿Qué es el Nexus?
    - **Ysondria:** Es el punto en el que la criatura intenta atravesar la superficie, pero también donde está más débil; está más expuesto.
    - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
    - (initial|standard)
  - [Choice]: No ahora mismo.
    - **Ysondria:** Te deseo suerte y espero que trabajes duro para ayudar en esto.

#### Obtener saco encantado


##### Sin poseer un saco encantado

- (above|Without owning a charmed sack)

##### Mientras posee un saco encantado

- **Ysondria:** Ya tienes un saco encantado. Recoge la corrupción del Nexus y purifícala en uno de los pilares.

### Dialogue after fully cleansing the Nexus


#### Después de limpiar completamente el Nexus:

- **Ysondria:** Gracias de nuevo, Player. Me preocupaba que este día no llegara, pero ustedes han detenido la corrupción.
- **Ysondria:** Hay algo de energía residual en el saco. Permítame devolvérselo.
- (removes=charmed sack) (receives=Prayer experience)
- **Ysondria:** Estaré eternamente agradecido por su ayuda para liberar esta tierra.
- **Ysondria:** Los efectos de la purificación ya se pueden ver. Creo que the memory de Augrum se siente honrado por el trabajo realizado aquí.
- **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
- [Menu]: Seleccione una opción {{anchor|standard}}
  - [Choice]: ¿Cómo puedo entrenar mis habilidades espirituales ahora?
    - **Ysondria:** Tradicionalmente, el entierro ceremonial se utiliza para honrar a los muertos. Para hacer esto, debes enterrar los huesos de los que han sido asesinados.
    - **Ysondria:** Según tengo entendido, cuanto más poderosa era la criatura cuando estaba viva, mayor es la experiencia que recibes al enterrar los huesos.
    - **Ysondria:** Si te dedicas a entrenar tus habilidades espirituales, puedes crear un altar dorado en tu casa para impulsar este proceso.
    - **Ysondria:** También he oído hablar de algo llamado Ectofuntus, que otorga mayor experiencia a partir de huesos, pero no sé qué es. Lo único que sé es que está situado cerca de Port Phasmatys, muy al noreste.
    - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
    - (previous)
  - [Choice]: ¿Quién es Augrum?
    - **Ysondria:** Augrum fue mi mentor. Dio su vida creando esas reliquias como un medio para liberar a la tierra de su inevitable decadencia.
    - **Ysondria:** Era un hombre muy valiente y de buen corazón, y agradezco su ayuda para hacer realidad su intención.
    - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
    - (previous)
  - [Choice]: ¿El área permanecerá limpia?
    - **Ysondria:** Creo que así será, gracias al arduo trabajo que has realizado aquí. No permitiré que ese mal vuelva.
    - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
    - (previous)
  - [Choice]: ¿Por qué sigues aquí?
    - **Ysondria:** Me siento cercano a Augrum aquí y quiero asegurarme de que todos sepan lo que hizo y lo que sacrificó para liberar esta tierra de esa corrupción.
    - **Ysondria:** También deseo hacer correr la voz sobre todas las personas que se unieron a la lucha y se enfrentaron al horror, usando su fe y fuerza interior para salvar la tierra.
    - **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
    - (previous)
  - [Choice]: Adiós.
    - **Ysondria:** Tu ayuda siempre será recordada.

#### Diálogo estándar después de devolver el saco encantado

- **Ysondria:** Estaré eternamente agradecido por su ayuda para liberar esta tierra.
- **Ysondria:** Los efectos de la purificación ya se pueden ver. Creo que the memory de Augrum se siente honrado por el trabajo realizado aquí.
- **Ysondria:** ¿Hay alguna otra ayuda que pueda brindarte?
- (continue|standard)

#### Obtener saco encantado

- **Ysondria:** Estaré eternamente agradecido por su ayuda para liberar esta tierra. Tu trabajo está hecho aquí.

### Treasure Trails

- **Ysondria:** Sabía que vendrías. Toma, toma esto.
- (receives=challenge scroll)
- [¡Ysondria te ha dado un pergamino de desafío!]

#### Cuando hablé de nuevo

- **Ysondria:** Ingrese la respuesta a la pregunta.
- ''(Cuando se le da la respuesta incorrecta:)
  - **Ysondria:** Eso no está nada bien.
- ''(Cuando se le da la respuesta correcta:)
  - (removes=the old clue scroll (medium))
  - ((If the trail continues:))
    - (receives=a new clue scroll (medium))
    - [¡Ysondria te ha dado otro pergamino de pistas!]
    - (continue)
  - ((If the trail ends:))
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
    - (continue)
  - **Ysondria:** ¡Correcto!
