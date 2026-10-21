# Zahra (Menaphos)

- **Original Wiki Page**: [Transcript:Zahra (Menaphos)](https://runescape.wiki/w/Transcript%3AZahra%20%28Menaphos%29)
- **Letter**: `Z`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before mining the big sandstone boulder


#### Cuando hablamos


##### Primera vez

- **Player:** ¿Qué estás haciendo aquí?
- **Zahra:** El faraón, junto con otros benefactores, quisiera tener un huerto de cactus en este rincón.
- **Zahra:** Por supuesto, el lugar tenía que tener una roca de arenisca gigante encima...
- **Player:** Sí...
- **Zahra:** Te diré una cosa. Si construyes el huerto de cactus para mí, te dejaré usarlo para practicar tus habilidades agrícolas.
- **Player:** Suena justo. Podría extraer esa cosa en muy poco tiempo.
- **Zahra:** Antes de dejarte comenzar, tráeme 12 Acadia logs y trabajaré en un perímetro de parcela básico.
- **Player:** ¿Solo 12?
- **Zahra:** 12 Acadia logs está bien. ¡No voy a crear la Torre del Dominio!

##### Después


##### Sin logs

- **Player:** ¿Deberíamos seguir adelante y hacer este huerto de cactus?
- **Zahra:** Antes de dejarte comenzar, tráeme 12 Acadia logs y trabajaré en un perímetro de parcela básico.
- **Player:** ¿Solo 12?
- **Zahra:** 12 Acadia logs está bien. ¡No voy a crear la Torre del Dominio!

##### Con logs

- **Player:** ¿Deberíamos seguir adelante y hacer este huerto de cactus?
- **Zahra:** Veo que tienes 12 Acadia logs, dámelos y trabajaré en un perímetro de parcela básico mientras extraes esa roca.
- **Player:** Claro, no hay problema.
- **Zahra:** Bien. Les daré forma de planks y clavijas para el borde del parche de cactus. Adelante, extrae esa... cosa.

##### Después de entregar el logs

- **Zahra:** Mía esa roca para mí, por favor.

#### Pagar por protección

- **Zahra:** Lo siento, no puedo ayudarte hasta que termine de construir este huerto de cactus...

#### Mining la roca de arenisca

- **Zahra:** ¡Espera!
- **Zahra:** Espera un segundo. Podríamos solucionar esto rápidamente juntos.

### While mining the big sandstone boulder

- *(Uno de los siguientes se ve al azar:)*
  - **Zahra:** ¡Veo que se agrieta más!
  - **Zahra:** Muy bien hecho.
  - **Zahra:** Qué bonito pico tienes ahí.
  - **Zahra:** Smashy, smashy.

### After mining the big sandstone boulder


#### Primera vez

- **Zahra:** ¡Tienes la fuerza y la astucia del propio Scabaras!
- **Zahra:** Si pudieras dividirlo en pedazos aún más pequeños, sería genial. Menos arenisca y más... arena.

#### Después

- **Zahra:** Estás a punto de destrozar la roca de arenisca por completo. Son casi escombros.

### While mining the broken down sandstone boulder

- *(Uno de los siguientes se ve al azar:)*
  - **Zahra:** ¡Veo que se agrieta más!
  - **Zahra:** Smashy smashy.
  - **Zahra:** Qué bonito pico tienes ahí.
  - **Zahra:** Las piezas son casi lo suficientemente pequeñas.

### After mining the broken down sandstone boulder


#### Primera vez

- **Zahra:** Excelente trabajo. La madera de Acadia no es muy buena como material de construcción, pero estos planks básicos servirán para una parcela agrícola.

#### Después

- **Zahra:** Ya he colocado los materiales, ¿podrías construir el perímetro por favor?

### After constructing the planks

- **Zahra:** Ah, ¿ya lo has hecho? ¡Excelente! Hacemos un buen equipo.

### Standard dialogue


#### Pagar


##### Con el huerto de cactus vacío

- **Zahra:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.

##### Con el cactus creciendo


##### Sin los elementos requeridos

- **Zahra:** Quiero [número] [items] para eso.
- **Player:** Gracias, tal vez en otro momento.

##### Con los elementos requeridos, sin confirmación desactivada

- [Menu]: ¿Pagar [número] [items]?
  - [Choice]: Sí.
    - (removes=requested items)
    - **Zahra:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
    - El jardinero ahora se ocupará del parche por usted.
  - [Choice]: Sí, y no vuelvas a preguntar.
    - (arriba)
  - [Choice]: No.
    - (end)

##### Con los elementos requeridos, con la confirmación desactivada

- (removes=requested items)
- **Zahra:** Eso estará bien, [sir/madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
- El jardinero ahora se ocupará del parche por usted.

##### Habiendo pagado ya por la protección

- **Zahra:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
- **Player:** Oh, lo siento, lo olvidé.

##### Con el cactus completamente desarrollado.

- **Zahra:** Ese parche ya está completamente desarrollado. No sé qué quieres que haga con él.

#### Habla con

- [Menu]: Elige una opción:
  - [Choice]: ¿Cuidarías mis cultivos por mí?
    - **Player:** ¿Cuidarías mis cultivos por mí?
    - **Zahra:** ¿Para ti? No es un problema.
    - (Condition: Si el player no tiene cultivos en el parche:)
      - **Zahra:** No tienes nada plantado en ese parche. Planta algo y tal vez acepte cuidarlo por ti.
    - (Condition: Si el player tiene cultivos completamente desarrollados plantados en el parche:)
      - **Zahra:** ¡Ese parche ya está completamente desarrollado! ¡No sé qué quieres que haga con él!
    - (Condition: Si los cultivos en el parche aún no están completamente desarrollados pero el player ya le pagó al jardinero:)
      - **Zahra:** No sé de qué estás hablando. Ya estoy cuidando ese parche por ti.
      - **Player:** Oh, lo siento, lo olvidé.
    - (Condition: Si los cultivos en el parche aún no han crecido completamente:)
      - **Zahra:** Si quieres, pero quiero [número] [item] para eso.
      - (Condition: Si el player no tiene los elementos requeridos:)
        - **Player:** Me temo que no tengo suficientes en este momento.
        - **Zahra:** Bueno, no voy a perder el tiempo gratis.
      - (Condition: Si el player tiene los elementos requeridos:)
        - [Menu]: Selecciona una opción
          - [Choice]: Está bien, es un trato.
            - **Player:** Está bien, es un trato.
            - (removes=requested items)
            - **Zahra:** Eso estará bien, [Sir/Madam]. Déjamelo a mí, me aseguraré de que crezca para ti.
          - [Choice]: No, eso es demasiado.
            - **Player:** No, eso es demasiado.
            - **Zahra:** Bueno, no voy a perder el tiempo gratis.
  - <!--Can you give me any Farming advice?-->{{Transcript:Group of Advanced Gardeners|npc=Zahra}}
  - [Choice]: cond=After A Fairy Tale III, and with patches being weeded|¿Puedes dejar de desyerbar mis parcelas agrícolas, por favor?
    - **Player:** ¿Puedes dejar de desherbar mis parcelas de cultivo, por favor?
    - **Zahra:** Claro, dejaré de eliminarlos ahora.
  - [Choice]: cond=After A Fairy Tale III, and with patches not being weeded|¿Puedes mantener mis parcelas agrícolas desyerbadas, por favor?
    - **Player:** ¿Puedes mantener mis parcelas de cultivo desyerbadas, por favor?
    - **Zahra:** Eso no debería ser un problema, ¡Martin dijo que debería darte especial atención por tu ayuda con las hadas! ¡Asegúrate de limpiar tu asignación ya que no quiero interrumpir su crecimiento!
  - [Choice]: ¿Puedes venderme algo?
    - **Player:** ¿Puedes venderme algo?
    - **Zahra:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
    - (opens=Farmer's Supplies)
  - [Choice]: Eso es todo, gracias.
    - **Player:** Eso es todo, gracias.

#### Diálogo histórico de venta anterior al 18 de julio de 2022

- **Player:** ¿Puedes venderme algo?
- **Zahra:** Eso depende de si lo tengo para vender. ¿Qué es lo que estás buscando?
- [Menu]: Selecciona una opción
  - [Choice]: Alguna cura vegetal.
    - **Player:** Alguna cura vegetal.
    - **Zahra:** Cura vegetal, ¿eh? Quizás tenga algo reservado para mí. Te diré una cosa, te venderé una cura vegetal por 25 po si quieres.
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
    - **Zahra:** Un balde de abono, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 35 po si quieres.
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
    - **Zahra:** Un rastrillo, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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
        - **Zahra:** Una regadera, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 25 po si quieres.
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
        - **Zahra:** Una paleta de jardín, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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
        - **Zahra:** Un zambullidor de semillas, ¿eh? Puede que tenga uno de repuesto... Te lo vendo por 15 po si quieres.
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

#### Uso de elementos en Zahra


##### Mostrando a Zahra un artículo que puede hacer abono

- **Zahra:** Parece algo con lo que se puede hacer abono normal. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de abono.

##### Mostrando a Zahra un elemento que puede hacer supercompost

- **Zahra:** Parece algo con lo que se puede hacer supercompost. Llena el contenedor de abono con cosas así y eventualmente tendrás un contenedor lleno de supercompost.

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Zahra:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Zahra:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - (Condition: Con 3 animales solicitados:)
      - **Zahra:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
      - (continue)
    - (Condition: Con 4 animales solicitados:)
      - **Zahra:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
      - (continue)
    - **Zahra:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - **Zahra:** Si completas esto, te daré: Ofrenda de regalo menafita (mediana) x 1. ¡Estoy seguro de que también ganarás algo de reputación en el gremio de agricultores!
    - **Zahra:** ¡Tendrás que ser rápido!, solo estoy aquí por [número] días, [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - (Condition: Sin los artículos solicitados:)
      - **Zahra:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Zahra:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - (Condition: Con 3 animales solicitados:)
        - **Zahra:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal].
        - (continue)
      - (Condition: Con 4 animales solicitados:)
        - **Zahra:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
        - (continue)
      - **Zahra:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - (Condition: Con los artículos solicitados:)
      - (removes=the requested items) (receives=Menaphite gift offering (medium) y imprimación Brassica)
      - Por completar esta solicitud, recibió 1 imprimación para Brassica.
      - ((Repetido en una ventana emergente:))
        - Por completar esta solicitud, recibió 1 imprimación para Brassica.
        - (continue)
      - [Has recibido: Ofrenda de regalo menafita (mediana) x 1<br>Y 5500 reputación agrícola.]

##### Después de completar la solicitud

- **Zahra:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time]{{Sic|..}}

#### Entregar solicitud mediana


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Zahra:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Zahra:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Zahra:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal
- **Zahra:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]

##### Con artículos solicitados

- (Condition: Con múltiples animales aplicables:)
  - [Menu]: ¿Qué animal te gustaría entregar?
    - ((Lo siguiente se repite para cada animal aplicable:))
      - [Choice]: [Animal name]
        - (continue)
- (removes=the requested items) (receives=Menaphite gift offering (medium) y imprimación Brassica)
- Por completar esta solicitud, recibió 1 imprimación para Brassica.
- ((Repetido en una ventana emergente:))
  - Por completar esta solicitud, recibió 1 imprimación para Brassica.
  - (continue)
- [Has recibido: Ofrenda de regalo menafita (mediana) x 1<br>Y 5500 reputación agrícola.]

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud bidiaria en [time]{{Sic|..}}
