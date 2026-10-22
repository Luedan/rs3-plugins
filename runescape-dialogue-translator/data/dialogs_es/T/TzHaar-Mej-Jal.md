# TzHaar-Mej-Jal

- **Original Wiki Page**: [Transcript:TzHaar-Mej-Jal](https://runescape.wiki/w/Transcript%3ATzHaar-Mej-Jal)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### TzHaar City

- **Tzhaar-Mej-Jal:** ¿Quieres ayuda, [Title]-[Caste]-Player?
  - [Choice]: cond=With fire cape in backpack:|Me gustaría volver a venderte mi capa de bomberos.
    - **Tzhaar-Mej-Jal:** Te doy 8.000 TokKul por la capa de fuego.<br>Pero, ¿de verdad quieres vender la capa? Debes derrotar a TzTok-Jad nuevamente para conseguir otro.
    - [Menu]: Elige una opción:
      - [Choice]: Sí, entiendo que no puedo volver a comprarlo.
        - (Condition: With only one fire cape in backpack:)
          - (removes=fire cape) (receives=8,000 TokKul)
          - **Player:** Muchas gracias.
          - (previous2)
        - (Condition: With more than one fire cape in backpack:)
          - **Tzhaar-Mej-Jal:** ¿Cuántos quieres vender?
          - {{Tinput|How many will you sell? You have [number] in your inventory.}}
          - (Condition: After entering 0:)
            - **Tzhaar-Mej-Jal:** ¿Quizás cambiaste de opinión?
          - (Condition: After entering a positive number:)
            - (removes=specified number of fire capes) (receives=8,000 TokKul for each fire cape removed)
            - **Player:** Muchas gracias.
            - (previous2)
      - [Choice]: ¿Sigues usando TokKul?
        - **Tzhaar-Mej-Jal:** TzHaar no necesita moneda. Cada TzHaar trabaja duro y cumple con su deber según su casta. TzHaar se asegura de que tengan comida y refugio, y de que se satisfagan todas sus necesidades.
        - **Tzhaar-Mej-Jal:** JalYt viene a la ciudad de TzHaar, con la cabeza llena de oro, riqueza y avaricia. El oro no le sirve a TzHaar. Suave y fácil de romper, como JalYt.
        - **Tzhaar-Mej-Jal:** JalYt necesita un token raro para intercambiar. TokKul son recuerdos de TzHaar muerto. Atrapado. Precioso.
        - **Tzhaar-Mej-Jal:** TokKul es la única ficha rara que tiene TzHaar. Hasta que TzHaar encuentre un nuevo token, o JalYt tenga menos codicia, debe intercambiar TokKul.
        - (previous)
      - [Choice]: En realidad, creo que me quedaré con mi capa.
        - (previous2)
  - ¿Qué es este lugar?
    - **Tzhaar-Mej-Jal:** Esta es la Cueva de la Lucha. TzHaar-Xil lo hizo para practicar, pero muchos JalYt también vienen aquí para pelear. Simplemente ingresa a la cueva y asegúrate de estar preparado.
      - ¿Hay alguna regla?
        - **Tzhaar-Mej-Jal:** ¿Reglas? La supervivencia es la única regla allí.
          - ¿Gano algo?
            - **Tzhaar-Mej-Jal:** Haces muchas preguntas. Podría darte TokKul si aguantas lo suficiente.
        - *(Si el player ha completado la misión Al borde de la extinción:)*
          - **Player:** ¿Sigues entregando TokKul como recompensa? TzHaar-Mej-Jeh dijo que iba a ser derretido en la lava sagrada, para liberar a tus muertos de su tormento.
          - **TzHaar-Mej-Jal:** TzHaar no necesita moneda. Cada TzHaar trabaja duro y cumple con su deber según su casta. TzHaar se asegura de que tengan comida y refugio, y de que se satisfagan todas sus necesidades. JalYt llega a la ciudad de TzHaar con la cabeza llena de oro, riqueza y avaricia. El oro no le sirve a TzHaar. Suave y fácil de romper, como JalYt. JalYt necesita un token raro para comerciar. TokKul son recuerdos de TzHaar muerto. Atrapado. Precioso. TokKul es la única ficha rara que tiene TzHaar. Hasta que TzHaar encuentre un nuevo token, o JalYt tenga menos codicia, debe intercambiar TokKul.
        - *(De lo contrario:)*
          - **Player:** ...
          - **TzHaar-Mej-Jal:** Antes de que preguntes, TokKul es como tu coins.
          - **TzHaar-Mej-Jal:** El oro es como tú JalYt: suave. ¡Usamos obsidiana dura, forjada al fuego como TzHaar!
          - Suena bien.
            - *(vuelve a opciones anteriores)*
      - Gracias.
        - *(termina el diálogo)*
  - ¿Cómo me llamaste?
    - **TzHaar-Mej-Jal:** ¿No eres [Title]-[Caste]?
    - Seleccione una opción
      - ¿Por qué me llamas '[Title]-[Caste]'?
        - *(Si el player es de la casta Ket:)*
          - **TzHaar-Mej-Jal:** Eso es lo que eres... eres duro y fuerte, ¿no?
        - *(Si el player es de la casta Xil:)*
          - **TzHaar-Mej-Jal:** Eso lo que eres...eres ágil y rápido, ¿no?
        - *(Si el player es de la casta Mej:)*
          - **TzHaar-Mej-Jal:** Eso es lo que eres...usuario de poderes místicos, ¿no?
        - *(Si el player es de la casta Hur:)*
          - **TzHaar-Mej-Jal:** Eso es lo que eres... eres hábil para hacer cosas, ¿no?
        - *(Si el player ha completado El borde de la extinción:)*
          - **TzHaar-Mej-Jal:** Y ya no eres JalYt. Ahora eres TzHaar.
        - **Player:** Bueno, sí, supongo que lo soy...
        - **TzHaar-Mej-Jal:** ¡Entonces tú [Title]-[Caste]!
        - Seleccione una opción
          - ¿Qué eres entonces?
            - *(Si el player no ha completado The Elder Kiln:)*
              - **TzHaar-Mej-Jal:** El tonto JalYt. Soy TzHaar-Mej, uno de los místicos de esta ciudad.
              - **TzHaar-Mej-Jal:** También están los poderosos TzHaar-Ket que nos protegen, los veloces TzHaar-Xil que cazan nuestra comida y los hábiles TzHaar-Hur que fabrican nuestros hogares y herramientas.
            - *(De lo contrario:)*
              - **TzHaar-Mej-Jal:** Soy TzHaar-Mej, uno de los místicos de la ciudad. Los TzHaar-Mej guían a los TzHaar cuando es necesario un cambio y cuidan los huevos de TzHaar para asegurarse de que estén calientes y saludables. TzHaar-Mej son depósitos de conocimiento y magia.
              - **TzHaar-Mej-Jal:** También están los poderosos TzHaar-Ket que nos protegen, los veloces TzHaar-Xil que cazan nuestra comida y los hábiles TzHaar-Hur que fabrican nuestros hogares y herramientas.
          - Gracias por explicarlo.
            - (end)
      - *(Si el player no ha completado El borde de la extinción:)*
        - Supongo que sí...
          - **TzHaar-Mej-Jal:** Bueno, entonces. No hay ningún problema.
        - ¡No, no lo soy!
          - **TzHaar-Mej-Jal:** ¡Lo que digas, JalYt!
      - *(De lo contrario:)*
        - Sí, ciertamente lo soy.
          - **TzHaar-Mej-Jal:** Entonces es un honor hablar contigo, TzHaar-[Caste]-Player. Tú, gran y poderoso TzHaar, y defensor de nuestra ciudad.
        - Debes haberme confundido con otro TzHaar.
          - **TzHaar-Mej-Jal:** Escuché que eres modesto, TzHaar-[Caste]-Player. No hay necesidad. Deléitate con nuestra alabanza. Mereces todo honor.
  - No, estoy bien. Gracias.
    - *(termina el diálogo)*

### Fight Cave

*Si el player intenta ingresar a Fight Cave con un familiar o una mascota siguiéndolos:*
- **Tzhaar-Mej-Jal:** ¡No hay Kimit-Zil en la cueva! ¡Esta es una pelea para TI, no para tus amigos!
*Inicio de la ola 1:*
- **Tzhaar-Mej-Jal:** Ahora estás solo, JalYt. ¡Prepárate para luchar por tu vida!
*Inicio de la ola 63:*
- **Tzhaar-Mej-Jal:** ¡Cuidado, aquí viene TzTok-Jad!
*Después de derrotar a TzTok-Jad:*
- **Tzhaar-Mej-Jal:** Incluso derrotaste a TzTok-Jad, ¡estoy muy impresionado! Acepte este regalo como recompensa.
*Después de morir en la Cueva de la Lucha:*
- **Tzhaar-Mej-Jal:** Bien hecho en la cueva, aquí llévate a Tokkul como recompensa.
*Después de salir o morir en Fight Cave sin ganar TokKul:*
- **Tzhaar-Mej-Jal:** Bueno, supongo que lo intentaste... más suerte la próxima vez.

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- **¿QUÉ TE GUSTARÍA HACER?**
  - Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **TzHaar-Mej-Jal:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **TzHaar-Mej-Jal:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **TzHaar-Mej-Jal:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
    - **TzHaar-Mej-Jal:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - **TzHaar-Mej-Jal:** Si completas esto, te daré: Amuleto de obsidiana x 15. ¡Estoy seguro de que también ganarás algo de reputación en el gremio de agricultores!
    - **TzHaar-Mej-Jal:** ¡Tendrás que ser rápido! Solo estoy aquí por [time]. Para ser exactos.
  - Dales los artículos y animales que soliciten.
    - ((Without the requested items:))
      - **TzHaar-Mej-Jal:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **TzHaar-Mej-Jal:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **TzHaar-Mej-Jal:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
      - **TzHaar-Mej-Jal:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - ((With the requested items:))
      - ((With multiple requested animals:))
        - **¿QUÉ ANIMAL TE GUSTARÍA ENTREGAR?**
          - ((Option repeated for each applicable animal:))
            - [Name]
              - (continue)
      - (removes=the requested items) (receives=the reward)
      - Por completar esta solicitud, recibió 1 imprimación para Brassica.
      - ((Repeated in a pop-up:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - (continue)
      - Has recibido: Amuleto de obsidiana x 15<br>Y 5500 de reputación agrícola.

##### Después de completar la solicitud

- **TzHaar-Mej-Jal:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time].

#### Entregar solicitud mediana


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **TzHaar-Mej-Jal:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **TzHaar-Mej-Jal:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **TzHaar-Mej-Jal:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
- **TzHaar-Mej-Jal:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]

##### Con artículos solicitados

- (removes=the requested items) (receives=the reward)
- Por completar esta solicitud, recibió 1 imprimación para Brassica.
- ((Repeated in a pop-up:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - (continue)
- Has recibido: Amuleto de obsidiana x 15<br>Y 5500 de reputación agrícola.

##### Después de completar la solicitud

- Ya completó esta solicitud, habrá una nueva solicitud tridiaria en [time].
