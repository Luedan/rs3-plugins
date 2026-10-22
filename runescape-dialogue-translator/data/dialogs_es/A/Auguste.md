# Auguste

- **Original Wiki Page**: [Transcript:Auguste](https://runescape.wiki/w/Transcript%3AAuguste)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{transcript npc|Auguste}}

### Before Enlightened Journey

- (Action: ver|Viaje Iluminado#Comenzando)

### First time after completing Enlightened Journey

- **Auguste:** Hola, Player. Es bueno verte de nuevo. Mi empresa ha crecido desde la última vez que nos vimos. ¡Me he expandido por todo Gielinor!
- **Auguste:** Si quieres ir a una nueva ubicación, tendrás que ayudar a volar el globo nuevamente. ¡Algunas de las rutas son muy peligrosas!
- **Auguste:** Pero cada ruta que completes te otorgará experiencia Firemaking.
- **Auguste:** Una vez que hayas abierto una ruta, solo cuesta 1 registro del tipo correspondiente viajar allí nuevamente, ¡desde cualquier ubicación que ya hayas abierto!
- **Auguste:** También he contratado asistentes para vigilar los globos en cada nuevo lugar al que vamos. Ellos te ayudarán a llegar a donde quieres ir.
- **Auguste:** ¿Quieres usar el globo? Para que lo sepas, algunas ubicaciones requieren logs especiales y altas habilidades de Firemaking.
- (continue)

### Standard dialogue

- **Auguste:** ¿Quieres usar el globo? Para que lo sepas, algunas ubicaciones requieren logs especiales y altas habilidades de Firemaking.
- [Menu]: Elige una opción:
  - [Choice]: Sí.
    - (opens=Balloon transport system)
  - [Choice]: No.
    - **Player:** No.
  - [Choice]: ¿Podrías decirme cómo hacer un globo de origami?
    - **Player:** ¿Podrías decirme cómo hacer un globo de origami?
    - **Auguste:** Primero, usa el papiro en el ovillo de lana. El papiro se dobla formando una caja de origami y el hilo servirá de soporte para la fuente de calor.
    - **Auguste:** Luego, agrega la vela apagada a la estructura del globo. Actuará como fuente de calor.
    - **Auguste:** ¡Ahora tienes un globo de origami!
    - **Auguste:** Si usas tu globo de origami con cualquier dye, puedes cambiar el color.
    - **Auguste:** Puedes soltar el globo y verlo flotar en el aire, solo usa un yesquero.
  - [Choice]: cond=If the player has a bomber cap and gnome goggles in their backpack|¿Podrías combinar mi gorra y mis gafas?
    - (removes=bomber cap and gnome goggles)
    - (receives=cap and goggles)
    - **Auguste:** ¡Ahí lo tienes! Ahora pareces un verdadero piloto de dirigible.
  - [Choice]: cond=If the player has lost their bomber cap or jacket|¿Podrías reemplazar algunos artículos por mí?
    - (Condition: If the player still has their bomber cap:)
      - **Auguste:** Parece que todavía tienes tu gorra.
    - (Condition: If the player is missing their bomber cap:)
      - (receives=bomber cap)
      - **Auguste:** Aquí tienes tu gorra. Intente realizar un mejor seguimiento.
  - (Condition: If the player still has their bomber jacket:)
    - **Auguste:** No necesitas una chaqueta nueva; Todavía tienes el original.
  - (Condition: If the player is missing their bomber jacket:)
    - (receives=bomber jacket)
    - **Auguste:** Aquí tienes tu chaqueta, para mantenerte abrigado durante el vuelo.

#### Opción Tienda-logs

- [Menu]: ¿Darle a Auguste todo tu logs?
  - [Choice]: Entrega tu logs.
    - (Condition: If the player has logs in backpack:)
      - (removes=all logs in backpack)
      - **Auguste:** ¡Gracias! Ahora tienes cargos [número].
    - (Condition: If the player does not have logs in backpack:)
      - **Auguste:** No tienes ningún logs que pueda almacenar. Actualmente tienes cargos [número].
  - [Choice]: Cancelar
    - (end)

#### Opción volar

- (opens=Balloon transport system)

#### Consultar opción de cargos

- Tienes cargos [número].
