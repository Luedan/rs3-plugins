# Beekeeper

- **Original Wiki Page**: [Transcript:Beekeeper](https://runescape.wiki/w/Transcript%3ABeekeeper)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Missing non-quest dialogue before/during Troll Romance quests. Missing some random event dialogue pre-2012, possibly unchanged in OSRS.}}

### Standard dialogue

- **Beekeeper:** ¡Hola! ¿Qué opinas de mi apiario? Bonito, ¿no?
- **Player:** ¿Te refieres a todas estas colmenas?
- **Beekeeper:** ¡Sí! Están llenos de abejas. ¡También cera y deliciosa miel también! Puedes servirte tanta cera y miel como quieras.
- (Condition: If the player doesn't have insect repellent in their tool belt or backpack:)
  - **Beekeeper:** Ah, pero necesitarás un poco de repelente de insectos, aquí.
  - El apicultor te entrega un repelente de insectos.
  - (receives=Insect repellent)
  - **Player:** ¡Gracias!
  - (continue)
- **Beekeeper:** Pero deja las abejas. ¡Las abejas son mías! ¡Me encantan las abejas!
- {{anchor|beekeepoptions}}[Menú]: Selecciona una opción
  - [Choice]: ¿Para qué sirve la miel?
    - **Beekeeper:** Ah, bueno, lo que querrás es más bien el panal. ¡He oído que algunas personas lo usan para infundir bolsas para invocar al temido tejón de miel! Siempre que lleves repelente, puedes coger tanto como quieras.
    - (previous|beekeepoptions)
  - [Choice]: Sobre la cera de abejas...
    - **Beekeeper:** Hmm, bueno, necesitarás un balde vacío para recolectar un poco de cera de abejas. Hay un cubo de repuesto por aquí en algún lugar que puedas tener. Es más complicado de conseguir que el panal. De hecho, tendrás que usar algún repelente en la colmena antes de llenar el balde con cera. Sin embargo, no estoy seguro de para qué lo querrías: no tiene muchos usos.
    - (previous|beekeepoptions)
  - [Choice]: Hasta luego.
    - **Beekeeper:** Está bien, pero "abeja" está bien. ¡Ja ja! ¿Geddit? Ya sabes, porque las 'abejas'...

### Beekeeper's random event

*Al participar en el evento aleatorio Beekeeper antes de su eliminación en la actualización del 24 de octubre de 2012.*
- **Beekeeper:** Ah, Player. Lamento arrastrarte así, pero necesito ayuda para construir una nueva colmena para mis abejas.
- **Player:** ¿Qué quieres que haga?
- **Beekeeper:** Todos los componentes de la colmena están mezclados. Tienes que ponerlos en el orden correcto para construir una colmena.
- **Player:** Oh, muy bien. Echemos un vistazo...
- (Action: Se abre la interfaz de eventos aleatorios Beekeeper)
- (Condition: If the player attempts to finish the puzzle without moving all pieces into a slot:)
  - sombra=si
- (Condition: If the player doesn't complete the puzzle correctly:)
  - **Beekeeper:** No, eso no se ve bien. Tienes que poner los componentes en el orden correcto, de lo contrario no servirá como colmena. Te dejaré hacer (cantidad entre 5 y 1) intentos más.
  - (Action: La interfaz de eventos aleatorios Beekeeper se abre nuevamente con cada pieza eliminada)
- (Condition: If the player completes the puzzle correctly:)
  - **Beekeeper:** ¡Eso es perfecto! Haré que instalen algunas abejas inmediatamente. Ahora, estoy seguro de que debo tener algo que ofrecerte por toda tu ayuda...
  - (Action: El diálogo termina y el player es teletransportado fuera del evento y reciben un regalo del evento aleatorio.)
- (Condition: If the player fails to complete the puzzle and has no more tries left:)
  - {{transcript missing|The bees attack the player before beekeeper teleports him away -- }}
- (Condition: If the player exits out of the dialogue and then speaks to the beekeeper again:)
  - {{transcript missing|The beekeeper would remind the player what to do with unique dialogue --}}

#### Hablando con el apicultor de otra persona

(Condition: Attempting to talk to a beekeeper that is after another player:)
- **Beekeeper:** Lo siento, no eres la persona que necesito.
