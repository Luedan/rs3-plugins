# Goob

- **Original Wiki Page**: [Transcript:Goob](https://runescape.wiki/w/Transcript%3AGoob)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Anachronia


#### Intentando minar la roca antes de hablar con Goob

- **Goob:** ¡Espera!
- **Goob:** ¡Tengo planes para esta gran roca!

#### Hablando con antes de comenzar a minar


##### Primera vez

- **Player:** ¿Qué estás haciendo aquí?
- **Goob:** ¡Hola! Estoy pensando en hacer un pequeño jardín aquí.
- **Goob:** ¡Esta roca capta toda la luz del cielo! Si podemos despedirnos de la gran roca, ¡el suelo aquí será el terreno perfecto para plantar!
- **Player:** ¿Qué quieres plantar?
- **Goob:** ...
- [El ancient zygomite frunce el ceño, mira a su alrededor lentamente y nota la enorme planta parecida a un cactus a poca distancia.]
- **Goob:** ¡Cactus!
- **Player:** ¡Qué sorpresa!
- **Player:** ¿Tiene que ser donde está la roca?
- **Goob:** Sí.
- **Player:** Obviamente.
- **Player:** Ya veo. Podría extraer esa cosa por ti.
- **Goob:** ¿Puedes traerme un poco de magic logs? ¡Comenzaré a hacer un parche perimetral y podrás romper la roca! {{anchor|bringlogs}}
- (Condition: Si el player no tiene magic logs:)
  - [Menu]: Selecciona una opción
    - [Choice]: [Polite] No veo por qué no.
      - **Goob:** ¡Gracias!
      - (continue)
    - [Choice]: [Angry] ¿Quieres que te proporcione los materiales también?
      - **Goob:** Yo tampoco soy muy bueno recogiendo trozos grandes de madera. ¡Lo siento!
      - (continue)
    - [Choice]: [Sarcastic] Oh, bien, me encanta repartir los artículos que he ganado con tanto esfuerzo.
      - **Goob:** ¡Me alegra oírlo!
      - (continue)
  - **Player:** Está bien. ¿Cuántos magic logs necesitas que consiga?
  - **Goob:** ¡12 magic logs por favor! ¡Definitivamente será suficiente, lo prometo!
- (Condition: Si el player ya tiene magic logs:)
  - **Player:** ¡Claro, no hay problema!
  - (removes=12 magic logs)
  - **Goob:** Tú rompes la roca y yo crearé la frontera.

##### Opción 'Pagar' antes de ayudar

- **Goob:** Lo siento, no puedo ayudarte hasta que termine de construir mi pequeño jardín.

##### Hablar con Goob después sin magic logs

- **Player:** ¿Deberíamos seguir adelante y hacer este huerto de cactus?
- (continuea|bringlogs)

##### Hablando con Goob después con el magic logs

- **Player:** ¿Deberíamos seguir adelante y hacer este huerto de cactus?
- **Goob:** ¡Puedo sentir magic logs! ¡Dámelos y los cortaré en planky-planks para el perímetro del jardín!
- **Player:** ¡Claro, no hay problema!
- (removes=12 magic logs)
- **Goob:** Tú rompes la roca y yo crearé la frontera.

##### Hablando con Goob después de dar el magic logs

- **Goob:** ¿Puedes romper la gran roca por mí, por favor?

#### Mining la roca

- *(Ocasionalmente se ve uno de los siguientes:)*
  - **Goob:** {{RSChat|Hooray! It's working!}}
  - **Goob:** {{RSChat|I see it cracking more!}}
  - **Goob:** {{RSChat|That's a nice rock breaker you have there.}}

#### Rompiendo la roca en roca arenisca

- **Goob:** ¡Eres realmente bueno en eso!
- **Goob:** ¡Vamos a romperlo en pedazos más pequeños y hacer que diga adiós!

#### Hablar con una vez que se ha roto la roca

- **Goob:** Estás a punto de destrozar la gran roca. Puedo sentir cómo se resquebraja.

#### Mining la roca de arenisca

- *(Ocasionalmente se ve uno de los siguientes:)*
  - **Goob:** {{RSChat|I'm making another magic plank now.}}
  - **Goob:** {{RSChat|Smashy smashy.}}
  - **Goob:** {{RSChat|The pieces are almost small enough.}}

#### Terminando la minería

- **Goob:** ¡Bien hecho! Hice un poco de planks para el jardín de cactus.

#### Hablar con una vez que se haya limpiado la roca de arenisca

- **Goob:** Ya coloqué los trozos de madera, ¿podrías construir el perímetro del parche, por favor?

#### Terminando la construcción

- **Goob:** Ah, ¿ya lo has hecho? ¡Excelente! Hacemos un buen equipo.

#### Intentando pagar antes de crear el parche

- **Goob:** Lo siento, no puedo ayudarte hasta que termine de construir mi pequeño jardín.

#### Intentando pagar después de crear el parche


##### Con el huerto de cactus vacío

- **Goob:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.

##### Con el cactus creciendo


##### Sin los elementos requeridos

- **Goob:** Quiero [número] [items] para eso.
- **Player:** Gracias, tal vez en otro momento.

##### Con los elementos requeridos, sin confirmación desactivada

- [Menu]: ¿Pagar [número] [items]?
  - [Choice]: Sí.
    - (removes=requested items)
    - **Goob:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
    - El jardinero ahora se ocupará del parche por usted.
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (arriba)
  - [Choice]: No.
    - (end)

##### Con los elementos requeridos, con la confirmación desactivada

- (removes=requested items)
- **Goob:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
- El jardinero ahora se ocupará del parche por usted.

##### Habiendo pagado ya por la protección

- **Goob:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
- **Player:** Oh, lo siento, lo olvidé.

##### Con el cactus completamente desarrollado.

- **Goob:** Ese parche ya está completamente desarrollado. No sé qué quieres que haga con él.

#### Hablando con después de crear el parche

- [Menu]: Elige una opción:
  - [Choice]: ¿Cuidarías mis cultivos por mí?
    - **Player:** ¿Cuidarías mis cultivos por mí?
    - (Condition: Si el player no tiene cultivos en el parche:)
      - **Goob:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.
    - (Condition: Si el player tiene cultivos completamente desarrollados plantados en el parche:)
      - **Goob:** ¡Ese parche ya está completamente desarrollado! ¡No sé qué quieres que haga con él!
    - (Condition: Si los cultivos en el parche aún no están completamente desarrollados pero el player ya le pagó al jardinero:)
      - **Goob:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
      - **Player:** Oh, lo siento, lo olvidé.
    - (Condition: Si los cultivos en el parche aún no han crecido completamente:)
      - **Goob:** Si quieres, pero quiero [número] [item] para eso.
      - (Condition: Si el player no tiene los elementos requeridos:)
        - **Player:** Me temo que no tengo suficientes en este momento.
        - **Goob:** Bueno, no voy a perder el tiempo gratis.
      - (Condition: Si el player tiene los elementos requeridos:)
        - [Menu]: Selecciona una opción
          - [Choice]: Está bien, es un trato.
            - **Player:** Está bien, es un trato.
            - (removes=requested items)
            - **Goob:** Eso estará bien, [Sir/Madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
          - [Choice]: No, eso es demasiado.
            - **Player:** No, eso es demasiado.
            - **Goob:** Bueno, no voy a perder el tiempo gratis.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Goob}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|¿Puedes dejar de desyerbar mis parcelas agrícolas, por favor?
    - **Player:** ¿Puedes dejar de desherbar mis parcelas de cultivo, por favor?
    - **Goob:** Claro, dejaré de eliminarlos ahora.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|¿Puedes mantener mis parcelas agrícolas desyerbadas, por favor?
    - **Player:** ¿Puedes mantener mis parcelas de cultivo desyerbadas, por favor?
    - **Goob:** Eso no debería ser un problema, ¡Martin dijo que debería darte especial atención por tu ayuda con las hadas! ¡Asegúrate de limpiar tu asignación ya que no quiero interrumpir su crecimiento!
  - [Choice]: ¿Puedes venderme algo?
    - **Player:** ¿Puedes venderme algo?
    - **Goob:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
    - (opens=Farmer's Supplies)
  - [Choice]: Eso es todo, gracias.
    - **Player:** Eso es todo, gracias.

#### Mostrando a Goob un artículo que puede hacer abono

- **Goob:** Parece algo con lo que se puede hacer abono normal. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de abono.

#### Mostrando a Goob un artículo que puede hacer supercompost

- **Goob:** Parece algo con lo que se puede hacer supercompost. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de supercompost.

#### Diálogo histórico de venta anterior al 18 de julio de 2022

- **Player:** ¿Puedes venderme algo?
- **Goob:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
- [Menu]: Selecciona una opción
  - [Choice]: Alguna cura vegetal.
    - **Player:** Alguna cura vegetal.
    - **Goob:** Cura vegetal, ¿eh? Quizás tenga algo reservado para mí. Te diré una cosa, te venderé una cura vegetal por 25 po si quieres.
    - (Condition: Si el player no tiene suficiente dinero:)
      - **Player:** Me temo que no tengo suficiente dinero para eso.
    - (Condition: Si el player tiene suficiente dinero:)
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, parece un precio justo.
          - **Player:** Sí, parece un precio justo.
          - (removes=25 coins) (receives=plant cure)
        - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
          - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
  - [Choice]: Un balde de abono.
    - **Player:** Un balde de abono.
    - **Goob:** Un balde de abono, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 35 po si quieres.
    - (Condition: Si el player no tiene suficiente dinero:)
      - **Player:** Me temo que no tengo suficiente dinero para eso.
    - (Condition: Si el player tiene suficiente dinero:)
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, parece un precio justo.
          - **Player:** Sí, parece un precio justo.
          - (removes=35 coins) (receives=compost)
        - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
          - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
  - [Choice]: Un rastrillo.
    - **Player:** Un rastrillo.
    - **Goob:** Un rastrillo, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
    - (Condition: Si el player no tiene suficiente dinero:)
      - **Player:** Me temo que no tengo suficiente dinero para eso.
    - (Condition: Si el player tiene suficiente dinero:)
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, parece un precio justo.
          - **Player:** Sí, parece un precio justo.
          - (removes=15 coins) (receives=a rake)
        - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
          - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
  - [Choice]: (Ver más artículos)
    - [Menu]: Selecciona una opción
      - [Choice]: una regadera
        - **Player:** Una regadera.
        - **Goob:** Una regadera, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 25 po si quieres.
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Player:** Me temo que no tengo suficiente dinero para eso.
        - (Condition: Si el player tiene suficiente dinero:)
          - [Menu]: Selecciona una opción
            - [Choice]: Sí, parece un precio justo.
              - **Player:** Sí, parece un precio justo.
              - (removes=25 coins) (receives=a watering can)
            - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
              - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
      - [Choice]: Una paleta de jardinería
        - **Player:** Una paleta de jardinería.
        - **Goob:** Una paleta de jardín, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Player:** Me temo que no tengo suficiente dinero para eso.
        - (Condition: Si el player tiene suficiente dinero:)
          - [Menu]: Selecciona una opción
            - [Choice]: Sí, parece un precio justo.
              - **Player:** Sí, parece un precio justo.
              - (removes=15 coins) (receives=a gardening trowel)
            - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
              - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
      - [Choice]: Un zambullidor de semillas
        - **Player:** Un arrancador de semillas.
        - **Goob:** Un zambullidor de semillas, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
        - (Condition: Si el player no tiene suficiente dinero:)
          - **Player:** Me temo que no tengo suficiente dinero para eso.
        - (Condition: Si el player tiene suficiente dinero:)
          - [Menu]: Selecciona una opción
            - [Choice]: Sí, parece un precio justo.
              - **Player:** Sí, parece un precio justo.
              - (removes=15 coins) (receives=a seed dibber)
            - [Choice]: No gracias, puedo conseguirlo mucho más barato en otro lado.
              - **Player:** No, gracias, puedo conseguirlo mucho más barato en otro sitio.
      - [Choice]: (Ver artículos anteriores)
        - (previous)
  - [Choice]: Olvídalo.
    - **Player:** Olvídalo, no tienes nada que necesite.

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Goob:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Goob:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **Goob:** También estoy buscando un nuevo animal, actualmente estoy buscando A [Animal]
    - **Goob:** Si completas esto, te daré: bendición de reputación Farming (mediana) x 1. ¡Estoy seguro de que también ganarás algo de reputación con el gremio de agricultores!
    - **Goob:** ¡Tendrás que ser rápido! Solo estoy aquí por [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - ((Sin los artículos solicitados:))
      - **Goob:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Goob:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **Goob:** También estoy buscando un nuevo animal, actualmente estoy buscando A [Animal]
    - ((Con los artículos solicitados:))
      - (removes=the requested items) (receives=Farming reputation boon (medium) y posiblemente una imprimación Brassica)
      - ((Si se premió una imprimación de Brassica:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - ((Repetido en una ventana emergente:))
          - Por completar esta solicitud, recibió 1 imprimación para Brassica.
          - (continue)
      - [Has recibido: bendición de reputación Farming (mediana) x 1 <br> y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- **Goob:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time].

#### Entregar solicitud fácil


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Goob:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Goob:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Goob:** También estoy buscando un nuevo animal, actualmente estoy buscando A [Animal]

##### Con artículos solicitados

- (removes=the requested items) (receives=Farming reputation boon (medium) y posiblemente una imprimación Brassica)
- ((Si se premió una imprimación de Brassica:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - ((Repetido en una ventana emergente:))
    - Por completar esta solicitud, recibió 1 imprimación para Brassica.
    - (continue)
- [Has recibido: bendición de reputación Farming (mediana) x 1 <br> y 2750 de reputación agrícola.]

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud diaria en [time].
