# Sir Amik Varze

- **Original Wiki Page**: [Transcript:Sir Amik Varze](https://runescape.wiki/w/Transcript%3ASir%20Amik%20Varze)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|Unknown conditionals for when talking to him about A Void Dance - his responses vary}}

### In the White Knights' Castle

- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Sir Amik Varze:** Soy el líder de los Caballeros Blancos de Falador. ¿Por qué buscas mi audiencia?
    - (initial|init)
  - [Choice]: cond=Before starting Recruitment Drive|¡Busco una búsqueda!
    - (ver|Campaña de reclutamiento)
  - [Choice]: cond=After A Void Dance|Habla sobre la misión A Void Dance.
    - {{Transcript missing|unknown conditional - }}
      - **Sir Amik Varze:** Bueno, Player, ahora que eres un Caballero Blanco, ¡espero que deberías estar cazando a Black Knights para nosotros!
      - (continue)
    - {{Transcript missing|unknown conditional - }}
      - **Sir Amik Varze:** ¿Cómo te encuentra la vida hoy, Player?
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Puedes volver a explicar el sistema de honor del Caballero Blanco?
        - **Sir Amik Varze:** Lamentablemente ya no somos tan ricos como antes, y hay muchos Caballeros Blancos que tontamente pierden su equipo de combate.
        - **Sir Amik Varze:** No creemos que sea justo obtener ganancias de nuestros hermanos, por lo que les venderemos el equipo al costo y lo recompraremos al mismo costo, pero solo venderemos el equipo a aquellos que consideremos lo suficientemente responsables como para manejarlo correctamente.
        - **Sir Amik Varze:**Al matar a Black Knights, aumentarás tu reputación con nosotros, al matar a White Knights obviamente pensaremos menos en ti.
        - **Sir Amik Varze:**¡Puedes comprobar tu nivel de reputación de Caballero Blanco consultando tu diario de misiones de Se busca! Quest o Sir Vyvin te permitirán saber en qué nivel te encuentras cuando vayas a comprar equipo.
        - **Sir Amik Varze:** Sir Vyvin se puede encontrar en el Castillo Falador y te venderá cualquier equipo apropiado para tu nivel de reputación.
        - **Sir Amik Varze:** ¡Diviértete y ve a matar Black Knights por mí!
        - **Player:** Está bien Amik, ¡gracias por explicarlo!
      - [Choice]: ¿Sabes algo sobre el asedio de Falador?
        - (below|siege)
    - [Choice]: ¡Está bien, adiós!
      - **Player:** Está bien, ¡adiós Amik!
  - [Choice]: Háblame de los Caballeros del Templo.
    - **Sir Amik Varze:** No puedo decirte mucho... <br> Se llaman los Caballeros del Templo y son una organización que fue fundada personalmente por Saradomin hace muchos siglos.
    - **Sir Amik Varze:** Existen muchos rumores y fábulas sobre sus obras y acciones, pero los registros oficiales de su presencia son inexistentes.
    - **Sir Amik Varze:** Es una organización secreta de extraordinario poder e ingenio...
    - **Sir Amik Varze:** Déjame decirlo de esta manera: <br> Si decides aceptar su generosa oferta de unirte, te encontrarás en una posición ventajosa que muchos en este mundo envidiarían y que pocos están llamados a ocupar.
    - **Player:** Bueno, eso no fue tan útil como pensé que sería... pero gracias de todos modos, supongo.
    - (initial|init)
  - [Choice]: ¿Sabes algo sobre el asedio de Falador?
    - {{anchor|siege}} **Player:** ¿Sabes algo sobre el asedio de Falador?
    - **Sir Amik Varze:** Ah, sí, el asedio de Kinshra fue realmente un asunto reñido.
    - **Sir Amik Varze:** Toda esperanza parecía perdida. Luego regresó - Kara-Meir - con Sir Theodore a su lado.
    - **Player:** ¿Señor Theodore? No he visto a nadie con ese nombre por aquí.
    - **Sir Amik Varze:** No, no lo habrías hecho. Él... ya no está con nosotros.
    - **Player:** Oh, lo siento.
    - **Sir Amik Varze:** Yo también, joven [man/woman]. Yo también.
  - [Choice]: cond=Historical, during the Battle of Lumbridge|¿Tienes alguna noticia?
    - **Player:** ¿Tienes alguna noticia?
    - **Sir Amik Varze:** Es una época gloriosa para los Caballeros Blancos: ¡Saradomin ha regresado!
    - **Sir Amik Varze:** ¡Nos está defendiendo de la malvada hechicería de Zamorak al oeste del castillo Lumbridge y nos ha pedido ayuda a nuestra orden!
    - **Sir Amik Varze:** Así que es deber de todos los Caballeros Blancos atender el llamado y tomar las armas contra el antiguo enemigo.
    - **Sir Amik Varze:** ¡Por la gracia de Saradomin, saldremos victoriosos!
  - [Choice]: Adiós.
    - (end)

### Manor Farm


#### Ayuda


##### Antes de haber completado la solicitud

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregunta sobre su solicitud.
    - **Player:** ¿Qué pides hoy?
    - **Sir Amik Varze:** ¡He estado trabajando en mi propia granja recientemente y necesito algunos artículos para aumentar mi productividad!
    - **Sir Amik Varze:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
    - **Sir Amik Varze:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
    - **Sir Amik Varze:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - **Sir Amik Varze:** Si completas esto, te daré: 15 armaduras de caballero blanco. ¡Estoy seguro de que también ganarás reputación en el gremio de agricultores!
    - **Sir Amik Varze:** ¡Tendrás que ser rápido!, solo estoy aquí por [número] días, [número] horas y [número] minutos. Para ser exactos.
  - [Choice]: Dales los artículos y animales que soliciten.
    - ((Sin los artículos solicitados:))
      - **Sir Amik Varze:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
      - **Sir Amik Varze:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
      - **Sir Amik Varze:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
      - **Sir Amik Varze:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]
    - ((Con los artículos solicitados:))
      - (removes=the requested items) (receives=the reward)
      - Por completar esta solicitud, recibió 3 imprimadores para Brassica.
      - ((Repetido en una ventana emergente:))
        - (Ventana emergente: por completar esta solicitud, recibió 3 imprimadores para Brassica.|color=#EBE0BC)
        - (continue)
      - [Has recibido: [Reward] x 15<br>Y 13,750 reputación agrícola.]

##### Después de haber completado la solicitud

- **Sir Amik Varze:** ¡Gracias por tu ayuda!
- Una nueva solicitud estará disponible en [time]{{Sic|..}}

#### Entregar solicitud dura


##### Antes de haber completado la solicitud


##### Sin artículos solicitados

- **Sir Amik Varze:** No tienes suficientes artículos para cumplir con mi solicitud. No aceptaré animales favoritos.
- **Sir Amik Varze:** Estoy intentando conseguir algunos cultivos adicionales, así que necesitaré: [Seed] x [número]
- **Sir Amik Varze:** También estoy buscando un nuevo animal. Actualmente busco uno de los siguientes: [Animal] o [Animal].
- **Sir Amik Varze:** También estoy buscando algunos productos, así que necesitaré: [Produce] x [número]

##### Con artículos solicitados

- (Condition: Con múltiples animales aplicables:)
  - [Menu]: ¿Qué animal te gustaría entregar?
    - ((Repetido para cada animal aplicable:))
      - [Choice]: [Animal name]
        - (continue)
- (removes=the requested items) (receives=the reward)
- Por completar esta solicitud, recibió 3 imprimadores para Brassica.
- (ventana emergente)
  - (Ventana emergente: por completar esta solicitud, recibió 3 imprimadores para Brassica).
  - (continue)
- [Has recibido: [Reward] x 15<br>Y 13,750 reputación agrícola.]

##### Después de haber completado la solicitud

- Ya has completado esta solicitud, habrá una nueva solicitud semanal en [time]{{Sic|..}}
