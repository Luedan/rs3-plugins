# Wizard Rosalina

- **Original Wiki Page**: [Transcript:Wizard Rosalina](https://runescape.wiki/w/Transcript%3AWizard%20Rosalina)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Primera vez

- **Wizard Rosalina:** ¡Creo que nunca había visto tu cara antes! Soy Wizard Rosalina.
- **Player:** ¡Encantado de conocerte! Soy Player.
- (continue|Rosalina-options)

#### Después


##### Normalmente

- **Wizard Rosalina:** ¡Hola, Player!
- [Menu]: Elige una opción:|anchor=Rosalina-options
  - [Choice]: ¿Qué tienes a la venta?
    - **Player:** ¿Qué tienes a la venta?
    - **Wizard Rosalina:** ¡Oh, todo tipo de adornos relacionados con mis estudios! Runas, gemas, telescopios, mejoras de Mining...
    - **Wizard Rosalina:** Debo tener en cuenta que solo acepto polvo de estrellas como pago. ¡Lo necesito más que oro!
    - [Menu]: ¿Abrir tienda de recompensas?
      - [Choice]: si
        - (opens=Shooting Star Reward Shop)
      - [Choice]: No
        - (previous|Rosalina-options)
  - [Choice]: ¿Qué estás haciendo?
    - **Player:** ¿Qué estás haciendo?
    - **Wizard Rosalina:** ¡Estoy estudiando los cielos, aprovechando el conocimiento del gran Scorpius que nos precedió!
    - **Player:** ¡Qué emocionante!
    - **Wizard Rosalina:** ¡Me alegra que tú también lo pienses! La astromancia ha recibido muchas críticas por parte de otros magos en el pasado.
    - **Wizard Rosalina:** Pero desde que mi compañero astromante, Wizard Chambers, lo usó para salvar a Gielinor de Tuska, poco a poco han ido reconociendo su legitimidad.
    - **Wizard Rosalina:** Sin embargo, mi especialidad particular son los duendes estelares.
    - (Condition: Antes de hablar con un star sprite:)
      - **Player:** ¿Qué son los duendes estelares?
      - (continue)
    - (Condition: Después de hablar con un star sprite:)
      - **Player:** ¿Los extraterrestres de aspecto extraño que se pueden encontrar en las estrellas fugaces? ¡He conocido a uno de esos antes! Estrella fugaz.
      - **Wizard Rosalina:** ¡Sí! ¡Encantadores, verdad!
      - (continue)
    - **Wizard Rosalina:** Desde que vi por primera vez a uno de los pequeños curiosos, me enamoré.
    - **Wizard Rosalina:** No pude encontrar ni una sola investigación sobre ellos, así que supe que tenía que ser yo quien cambiara eso.
    - (previous|Rosalina-options)
  - [Choice]: Hablando de estrellas fugaces.
    - [Menu]: Seleccione una opción|ancla=opciones-de-estrellas fugaces
      - [Choice]: ¿Qué son las estrellas fugaces?
        - **Player:** ¿Qué son las estrellas fugaces?
        - **Wizard Rosalina:** Las estrellas fugaces son grandes trozos de roca que ocasionalmente caen sobre Gielinor desde el cielo.
        - **Player:** Bueno, si aún no tenía miedo de ser eliminado por una roca espacial que aparece de la nada, ahora lo tengo.
        - **Wizard Rosalina:** ¡Estadísticamente no tienes nada de qué preocuparte!
        - **Player:** ...
        - **Wizard Rosalina:** Suponiendo que te topas con una estrella estrellada y logras evitar quedar inconsciente, puedes extraerla para liberar a su habitante en su núcleo.
        - **Player:** Ya veo, ¡gracias!
        - (previous|Shooting-stars-options)
      - [Choice]: ¿Cómo puedo encontrar estrellas fugaces?
        - **Player:** ¿Cómo puedo encontrar estrellas fugaces?
        - **Wizard Rosalina:** Puedes explorar los cielos en busca de estrellas fugaces cercanas usando un telescopio.
        - **Wizard Rosalina:** Se pueden construir telescopios en la casa de tu jugador, pero también puedes encontrar algunos telescopios públicos en la biblioteca del palacio Varrock y en el observatorio.
        - **Player:** ¿Qué pasa con tu telescopio de allí?
        - **Wizard Rosalina:** ¡Oh, desearía que esa belleza fuera mía! Por desgracia, pertenece a Wizard Rosalina.
        - **Wizard Rosalina:** Sin embargo, me dio permiso para usarlo, así que supongo que puedo pasarte ese permiso a ti.
        - **Wizard Rosalina:** También debo mencionar que no todos los telescopios están construidos de la misma manera. Es posible que algunos, debido a que fueron construidos con maderas de niveles inferiores, sean un poco menos precisos que otros.
        - **Player:** ¿Qué afecta su precisión?
        - **Wizard Rosalina:** Bueno, cuanto más preciso sea un telescopio, más corto será el plazo que indicará cuándo aterrizará la próxima estrella fugaz. También le dará una estimación más precisa del tamaño de la estrella.
        - **Player:** Es bueno saberlo.
        - (previous|Shooting-stars-options)
      - [Choice]: ¿Qué puedo obtener de las estrellas fugaces?
        - **Player:** ¿Qué puedo obtener de las estrellas fugaces?
        - **Wizard Rosalina:** Las estrellas estrelladas están repletas de polvo de estrellas. Yo uso polvo de estrellas en mis estudios, así que siéntete libre de traerme un poco y puedo cambiarte por algunas cosas que te puedan resultar útiles.
        - **Wizard Rosalina:** Si extraes la estrella hasta el núcleo, también he oído que el star sprite interior puede ayudarte con algún tipo de mejora temporal de Mining.
        - **Player:** ¡Intrigante!
        - (previous|Shooting-stars-options)
      - [Choice]: [Previous options]
        - (previous2|Rosalina-options)
  - [Choice]: cond=Having lost a portable telescope:|Me gustaría recuperar mi telescopio portátil.
    - (Condition: Sin espacio libre backpack:)
      - **Wizard Rosalina:** Tendrás que volver cuando tengas un espacio libre en tu backpack.
    - (Condition: Con espacio gratuito backpack:)
      - **Player:** He perdido mi telescopio portátil.
      - **Wizard Rosalina:** No te preocupes, ¡tengo muchos repuestos!
      - (receives=portable telescope)
      - [Wizard Rosalina le entrega un nuevo y brillante telescopio portátil.]
      - (previous|Shooting-stars-options)
  - [Choice]: ¿Sabes algo sobre las flores estelares?
    - **Player:** ¿Sabes algo sobre las flores estelares?
    - **Wizard Rosalina:** ¡Oh, flores de estrellas! Yo nunca he visto uno, pero una vez entrevisté a un star sprite que cultivaba campos de flores estelares en casa. Están llenos de magia y son muy bonitos.
    - **Wizard Rosalina:** Las flores de las estrellas, claro está. Los duendes de estrellas son más lindos que bonitos.
    - **Wizard Rosalina:** De todos modos, parte del polvo de estrellas que analicé mágicamente contenía trazas de polen de otro mundo. La mayor parte se quema cuando aterriza una estrella fugaz, pero con el tiempo, queda empapado en suelo gielinoriano.
    - **Wizard Rosalina:** Ese residuo orgánico luego es absorbido por otras semillas, o comido por monstruos, que son devorados por monstruos más grandes y desagradables, que expulsan los pedazos no digeribles de monstruos menos grandes y menos desagradables...
    - **Wizard Rosalina:** Y así es como se obtienen las semillas de flores estelares.
    - **Player:** ¿Entonces estás diciendo que puedo obtener semillas de flores estelares robando a los granjeros que llevan semillas y derrotando a monstruos particularmente desagradables?
    - **Wizard Rosalina:** Yo... ¿no estoy diciendo eso? Pero si así es como eliges interpretar lo que estoy diciendo, supongo que no puedo detenerte.
    - **Player:** Entonces, ¿cómo puedo cultivar semillas de flores estelares?
    - **Wizard Rosalina:** Bueno, no es mi área de especialización, pero las flores estelares provienen de una animasfera completamente diferente.
    - **Wizard Rosalina:** Para sintonizar las semillas de flores estelares con nuestra anima mundi, necesitarás conectarlas al campo mágico del paisaje rúnico de nuestro mundo.
    - **Player:** Entonces, ¿colocas un battlestaff en un parche de flores y la flor de estrella crecerá como un marco de vid?
    - **Wizard Rosalina:** Bueno... sí, en realidad. ¡Parece que sabes más sobre esto que yo!
    - (previous2|Rosalina-options)
  - [Choice]: Adiós.
    - **Player:** ¡Adiós!
    - **Wizard Rosalina:** ¡Hasta luego!

##### Durante la tarea de celebraciones del 25 Aniversario

- **Wizard Rosalina:** 'Star sprite, luz de las estrellas, primera estrella fugaz que veo esta noche...'
- **Player:** Hola, ¿qué estás haciendo?
- **Wizard Rosalina:** Oh, hola, ¡estoy siguiendo estrellas fugaces!
- **Wizard Rosalina:** ¡Estoy buscando ver si hay algún fallo, para poder enviar un mensaje y conseguir ayuda para los duendes de estrellas varados!
- {{RSFontAchievement|Wish Upon a Star|Talk to Wizard Rosalina on the second floor of the Wizards' Tower about Shooting Stars.}}
- ((Se muestra en una ventana emergente de finalización de tarea:))
  - {{Colour|#F0BE79| TAREA DEL 25 ANIVERSARIO |#181513}}
  - Deseo a una estrella
  - Habla con Wizard Rosalina en el segundo piso de Wizards' Tower sobre Shooting Stars.
  - (continue)
- **Player:** ¡Bien! Bueno, ¡sigan con el buen trabajo!
- (Condition: Si se han completado todas las tareas:)
  - **Player:** Parece que he completado todo. ¡Será mejor que vaya a ver a Hans sobre esa recompensa!

### Attempting to place a cannon on Zolarea

- **Wizard Rosalina:** ¿Player? ¿Qué estás haciendo?
- **Player:** ¿Rosalina? ¿Cómo me hablas?
- **Wizard Rosalina:** El hechizo de contacto. Hemos pasado por esto.
- **Player:** No estoy seguro de cómo funciona, pero está bien.
- **Wizard Rosalina:** Entonces, ¿qué estabas haciendo?
- **Player:** Simplemente, ejem, colocando este cañón aquí... Quería ver esas balas de cañón de meteorito...
- **Wizard Rosalina:** ¿En serio? Después de toda la hospitalidad que te mostraron los duendes estelares, ¿te dedicas a fotografiar su planeta?
- **Wizard Rosalina:** Esperaba algo mejor de ti. Si algún daño le ocurre a uno solo de ellos...
- **Player:** No, señora. Bajaré el cañón ahora mismo.
- (Condition: Primera vez que intento esto:)
  - {{RSFontAchievement|Gielinor Attacks!}}
