# Charity

- **Original Wiki Page**: [Transcript:Charity](https://runescape.wiki/w/Transcript%3ACharity)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### First time

- **Charity:** Hola, soy Charity. ¡Solo por tiempo limitado, seré el anfitrión del juego de trivia interactivo, The Drop!
- **Player:** ¡Suena genial! ¿Cómo funciona?
- **Charity:** Se te harán una serie de preguntas temáticas de RuneScape. Responda todas las preguntas correctamente y obtendrá una buena recompensa. Cada vez que juegues, Jagex donará £1 a organizaciones benéficas, ¡hasta un máximo de £34,500! Sé lo que estás pensando. ¿Por qué me dan todo ese dinero?
- **Player:** ... En fin, ¿cómo participo?
- **Charity:** Lo anunciaré cada vez que se abra The Drop. Luego tendrás 2 minutos para unirte antes de que comience el juego.
- **Player:** ¡Gracias!
- **Charity:** ¡Habla conmigo nuevamente para obtener más información o usa la opción "Unirse rápidamente" para ingresar directamente al juego!

### Standard dialogue

- **Charity:** Hola de nuevo, ¿en qué puedo ayudarte?
- Seleccione una opción{{anchor|init}}
  - Pregunta por La Gota.
    - **Player:** ¿Podrías hablarme de The Drop?
    - **Charity:** ¡Por supuesto! The Drop es un juego de preguntas interactivo. Se le harán una serie de preguntas temáticas de RuneScape. Responda todas las preguntas correctamente y obtendrá una buena recompensa. Cada vez que juegues, Jagex donará £1 a organizaciones benéficas, ¡hasta un máximo de £34,500!
    - **Player:** ¡Genial, gracias!
    - (initial|init)
  - Introduzca La Gota.
    - ((If The Drop is not currently open:))
      - The Drop no está abierto actualmente.
    - ((If The Drop is open:))
      - ((If the player has a follower out or a Summoning pouch in backpack:))
        - **Charity:** Lo sentimos, ¡no se permiten mascotas, seguidores ni bolsas de invocación en The Drop!
      - ((If the player doesn't have space in backpack:))
        - **Charity:** Lo sentimos, no tienes suficiente espacio en el inventario para reclamar la recompensa si ganas.
      - (el player se lleva a The Drop).
      - Bienvenido a The Drop: ¡el próximo juego comenzará pronto!
  - Pregunta por las recompensas.
    - **Player:** ¿Hay alguna recompensa involucrada?
    - **Charity:** ¡Por supuesto! Si respondes todas las preguntas correctamente, obtendrás el título "Apart Together". También te llevarás algunas estrellas prismáticas y lámparas. Además, solo por participar, Jagex donará £1 a organizaciones benéficas, ¡hasta un máximo de £34,500!
    - **Player:** ¡Genial, gracias!
    - (initial|init)
  - Pregunte sobre donaciones caritativas.
    - **Player:** ¿Podrías darme más información sobre la caridad?
    - **Charity:** ¡Por supuesto! Soy Charity, paso mucho de mi tiempo... ¡Solo bromeo! Jagex hará una donación de £100 000 a nuestros socios benéficos de salud mental. ¡Los jugadores pueden ayudar a alcanzar este objetivo ingresando a The Drop! Por cada participación, se donará £1 a organizaciones benéficas.
    - ¿Quieres más información?
      - Sí, llévame al periódico.
        - ((Opens £100k+ for mental health - how to get involved!))
        - (initial|init)
      - No.
        - (initial|init)
  - Adiós
    - **Player:** Adiós.
    - **Charity:** Adiós por ahora.

### "Claim rewards" option

*Si el player no ha reclamado las recompensas:*
- **Charity:** Puedes ganar recompensas por este evento respondiendo correctamente las 12 preguntas en The Drop.
*Si el player ha reclamado las recompensas:*
- **Charity:** Ya recibiste todas las recompensas de este evento.

### Overhead dialogue


#### Cuando The Drop no está activo

- ((Every minute:))
  - **Charity:** {{RSChat|The Drop starts in [number] minute[s]!}}

#### Cuando The Drop está activo

- ((Every minute:))
  - **Charity:** {{RSChat|The Drop has started! Talk to me or use the 'Quick join' option to take part.}}
