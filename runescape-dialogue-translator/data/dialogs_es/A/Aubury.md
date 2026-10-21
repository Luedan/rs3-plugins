# Aubury

- **Original Wiki Page**: [Transcript:Aubury](https://runescape.wiki/w/Transcript%3AAubury)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{External|os=Transcript:Aubury|rsc=Transcript:Aubury}}
{{dialogue|npc}}

### In Varrock

- **Aubury:** ¿Quieres comprar algunas runas?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, por favor.
    - (Action: opens=Tienda de runas de Aubury)
  - [Choice]: No gracias.
    - **Player:** No, gracias.
  - [Choice]: ¿Puedes teletransportarme a la esencia rúnica?
    - **Player:** ¿Puedes teletransportarme a la esencia rúnica?
    - **Aubury:** {{RSChat|Senventior disthine molenko!}}
    - (Action: Aubury te teletransporta a la mina Rune Essence)

### Manor Farm


#### Ayuda


##### Antes de completar la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Aubury:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Aubury:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **Aubury:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
    - **Aubury:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - **Aubury:** Si completas esto, te daré: Runa de naturaleza x 100. ¡Estoy seguro de que también ganarás reputación en el gremio de agricultores!
    - **Aubury:** ¡Tendrás que ser rápido! Solo estoy aquí por [time]. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - (Condition: Sin los artículos solicitados:)
      - **Aubury:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Aubury:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **Aubury:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
      - **Aubury:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - (Condition: Con los artículos solicitados:)
      - (removes=the requested items) (receives=100 nature rune and 3 Brassica primers)
      - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
      - ((Repetido en una ventana emergente:))
        - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
        - (continue)
      - {{tbox|pic=Nature rune detail.png|You've received : Nature rune x 100<br>And 13,750 farming reputation.}}

##### Después de completar la solicitud

- **Aubury:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time]{{Sic|..}}

#### Entregar solicitud dura


##### Antes de completar la solicitud


##### Sin artículos solicitados

- **Aubury:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Aubury:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Aubury:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
- **Aubury:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]

##### Con artículos solicitados

- (Condition: Sin los artículos solicitados:)
  - **Aubury:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
  - **Aubury:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
  - **Aubury:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
  - **Aubury:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
- (Condition: Con los artículos solicitados:)
  - (removes=the requested items) (receives=100 nature rune and 3 Brassica primers)
  - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
  - ((Repetido en una ventana emergente:))
    - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
    - (continue)
  - {{tbox|pic=Nature rune detail.png|You've received : Nature rune x 100<br>And 13,750 farming reputation.}}

##### Después de completar la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud semanal en [time]{{Sic|..}}

### In New Varrock

- **Aubury:** ¿Quieres comprar algunas runas?
- [Menu]: Selecciona una opción
  - [Choice]: Quiero comprar runas.
    - (Action: opens=Tienda de runas de Aubury (Nuevo Varrock))
  - [Choice]: ¿Puedo tener un orbe de oculus?
    - **Aubury:** Bueno, está bien. <br>Pero no dejes que Zemouregal te atrape.<br>Él hace la adivinación por aquí...
    - (receives=Orb of oculus)
    - {{tbox|pic=Orb of oculus detail.png|Aubury hastily tosses you an orb of mystical excellence.}}
  - [Choice]: No, adiós.
    - **Aubury:** Bueno, si encuentras a alguien que quiera runas, envíamelas.
