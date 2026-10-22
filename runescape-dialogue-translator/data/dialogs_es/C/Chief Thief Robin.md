# Chief Thief Robin

- **Original Wiki Page**: [Transcript:Chief Thief Robin](https://runescape.wiki/w/Transcript%3AChief%20Thief%20Robin)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Thieves' Guild


#### Hablando con él


##### Ante compradores y bodegas

- **Player:** Hola.
- **Chief Thief Robin:** Saludos. Soy Robin, el asistente de Guildmaster.
- **Chief Thief Robin:** Ahora, ¿qué puedo hacer por ti?
- [Menu]: Selecciona una opción
  - [Choice]: Ese es un nombre apropiado.
    - **Player:** Ese es un nombre apropiado.
    - **Chief Thief Robin:** Sí, nunca había oído eso antes.
    - **Chief Thief Robin:** Aún así, no es tan malo... Si no se hubieran burlado de mí por mi nombre cuando era niño, tal vez nunca habría decidido, en un ataque de resentimiento irónico, aprender a robar a los ricos y dárselo a los pobres.
    - **Player:** ¿Es usted el pobre en cuestión?
    - **Chief Thief Robin:** Bueno, lo era.
    - **Chief Thief Robin:** Después de haberme entregado los bienes robados a varias personas ricas, ahora tengo medios limitados pero cómodos.
    - **Chief Thief Robin:** Ahora, ¿qué puedo hacer por ti?
    - (initial|init-options-robin-1)
  - [Choice]: ¿Hace cuánto que conoces el Guildmaster?
    - **Player:** ¿Hace cuánto que conoces a Guildmaster?
    - **Chief Thief Robin:** Oh, hace algún tiempo. Empezamos a trabajar juntos cuando él era un estafador, convenciendo a la gente para que entregara los objetos de valor que tanto les costó ganar con mentiras y vagas promesas de recompensa.
    - **Chief Thief Robin:** Obviamente, todo eso ya quedó atrás.
    - **Chief Thief Robin:** Ahora, ¿qué puedo hacer por ti?
    - (initial|init-options-robin-1)
  - [Choice]: Adiós por ahora.
    - **Player:** Adiós por ahora.

##### Después de compradores y bodegas

- **Player:** Hola.
- **Chief Thief Robin:** Ah, nuestra estrella en ascenso.
- **Chief Thief Robin:** Ahora, ¿qué puedo hacer por ti?
- [Menu]: Selecciona una opción
  - [Choice]: Ese es un nombre apropiado.
    - (above|appropriate)
  - [Choice]: ¿Hace cuánto que conoces el Guildmaster?
    - (above|known)
  - [Choice]: ¿Dónde puedo practicar mi arte?
    - **Player:** ¿Dónde puedo practicar mi arte?
    - **Chief Thief Robin:** He oído que hay un compañero en Al Kharid que necesita a alguien para un trabajo de infiltración.
    - (Condition: With 40 Agility:)
      - **Chief Thief Robin:** Hay rumores sobre una pirámide en lo profundo del desierto llena de trampas y objetos de valor.
      - (continue)
    - (Condition: With 50 Agility and 50 Thieving:)
      - **Chief Thief Robin:** Y un colega nuestro ha creado un juego de laberinto en Burthorpe, si te sientes ligero de pies.
      - (continue)
    - **Player:** Gracias, Robin.
    - **Chief Thief Robin:** Ahora, ¿qué puedo hacer por ti?
    - (initial|init-options-robin-2)
  - [Choice]: ¿Podrías ayudarme a vender estos artículos?
    - (below|Fence items)
  - [Choice]: Adiós por ahora.
    - **Player:** Adiós por ahora.

#### Artículos de valla


##### Ante un gremio propio

- **Chief Thief Robin:** Tendrás que ayudar más al gremio antes de que pueda cercar objetos para ti.

##### Antes de recibir una bolsa de botín de safe-cracking trainer

- **Chief Thief Robin:** Tendrás que hablar con el tutor de seguridad antes de que pueda ayudarte a cercar tus artículos.

##### Después de un gremio propio

- (Condition: Without a loot bag in backpack:)
  - **Chief Thief Robin:** Tendrás que traer tu bolsa de botín si quieres que eche un vistazo y vea qué podemos cercar.
- (Condition: With an empty loot bag in backpack:)
  - **Chief Thief Robin:** No parece que tengas nada que podamos cercar en este momento. Vuelve cuando hayas llenado esa bolsa tuya.
- (Condition: With a filled loot bag in backpack:)
  - Has recibido puntos de robo [número] xp, oro [número] y puntos de robo [número].<br>Ahora tienes puntos de robo [número].
- (Condition: With a filled loot bag in backpack but with 60,000 pilfer points in currency pouch:)
  - No puedes recibir más puntos de robo. Por favor, vaya a gastar algo en Dirty Deals de Dodgy Derek.
