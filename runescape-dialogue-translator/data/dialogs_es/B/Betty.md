# Betty

- **Original Wiki Page**: [Transcript:Betty](https://runescape.wiki/w/Transcript%3ABetty)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Port Sarim

- **Betty:** Bienvenido al emporio mágico.
- [Menu]: Elige una opción:
  - [Choice]: cond=After The Hand in the Sand, and on a members world|Habla con Betty sobre La mano en la arena.
    - **Betty:** Zavistic me dijo el buen trabajo que hiciste. Si quieres más dye rosa, he preparado un lote y puedes conseguirlo por 20 de oro.
    - [Menu]: Selecciona una opción
      - [Choice]: No, gracias Betty.
        - **Player:** No, gracias, Betty. Buena suerte con la tienda. Puede que vuelva para tomar un poco de dye más tarde.
        - **Betty:** Gracias, Player. Nos vemos pronto.
      - [Choice]: ¡Sí, por favor!
        - **Player:** ¡Sí, por favor!
        - (Condition: If the player has no space in backpack for the dye:)
          - **Betty:** Me temo que no tienes espacio en tu mochila para nada más, vuelve cuando lo tengas.
        - (Condition: If the player does not have 20 coins:)
          - No puedes permitirte eso.
          - No tienes suficiente dinero en este momento, vuelve más tarde.
        - (Condition: Otherwise:)
          - Entregas 20 piezas de oro a cambio del dye.
          - (removes=20 coins) (receives=pink dye)
  - [Choice]: ¿Puedo ver tus productos?
    - (opens=Betty's Magic Emporium)
  - [Choice]: Lo siento, no me gusta la magia.
    - **Player:** Lo siento, no me gusta la magia.
    - **Betty:** Bueno, si ves a alguien a quien le guste la magia, envíamelo.

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Betty:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Betty:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **Betty:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal]. o [Animal]
    - **Betty:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - **Betty:** Si completas esto, te daré: Runa de fuego x 250. ¡Estoy seguro de que también ganarás reputación en el gremio de agricultores!
    - **Betty:** ¡Tendrás que ser rápido!, solo estoy aquí por [número] días, [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - (Condition: Without the requested items:)
      - **Betty:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Betty:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **Betty:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal].
      - **Betty:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - (Condition: With the requested items:)
      - (removes=the requested items) (receives=250 fire runes and Brassica primer)
      - Por completar esta solicitud, recibió 1 imprimación para Brassica.
      - ((Repeated in a pop-up:))
        - (Pop-up: For completing this request you've received Brassica primer x 1.|colour=#EBE0BC|shadow=no)
        - (continue)
      - [Has recibido: Runa de fuego x 250<br>Y 5500 de reputación agrícola.]

##### Después de completar la solicitud

- **Betty:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time]{{Sic|..}}

#### Entregar solicitud mediana


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Betty:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Betty:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Betty:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal], o [Animal], o [Animal], o [Animal
- **Betty:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]

##### Con artículos solicitados

- (removes=the requested items) (receives=250 fire runes and Brassica primer)
- Por completar esta solicitud, recibió 1 imprimación para Brassica.
- ((Repeated in a pop-up:))
  - (Pop-up: For completing this request you've received Brassica primer x 1.|colour=#EBE0BC|shadow=no)
  - (continue)
- [Has recibido: Runa de fuego x 250<br>Y 5500 de reputación agrícola.]

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud bidiaria en [time]{{Sic|..}}
