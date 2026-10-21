# Father Aereck

- **Original Wiki Page**: [Transcript:Father Aereck](https://runescape.wiki/w/Transcript%3AFather%20Aereck)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- (Condition: Antes del Restless Ghost:)
  - **Father Aereck:** Bienvenido a la iglesia del santo Saradomin.
  - (continue)
- (Condition: Después del Restless Ghost:)
  - **Father Aereck:** ¡Bienvenido de nuevo a la iglesia del santo Saradomin, amigo mío! ¿Qué puedo hacer por ti hoy?
  - (continue)
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: cond=With a construction contract for Father Aereck:|Pregunta por tu construction contract.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué necesitas reparar?
        - **Father Aereck:** Déjame ver, ahora mismo necesito que repares el siguiente pieces of furniture.
        - **Father Aereck:** [Furniture 1], [Furniture 2], [Furniture 3], [Furniture 4], [Furniture 5]
        - (previous)
      - [Choice]: ¿Qué materiales necesito?
        - **Father Aereck:** Necesitas: Planks x [número], Steel nails x [número], [Additional material] x [número]
        - (previous)
      - [Choice]: [Leave]
        - (end)
  - [Choice]: cond=Before The Restless Ghost:|¡Estoy buscando una misión! {{anchor|quest}}
    - (ver|El Restless Ghost)
  - [Choice]: cond=After The Restless Ghost:|¿Puedes cambiar mi lápida ahora? {{anchor|gravestone}}
    - **Father Aereck:** Por supuesto. Todas las ganancias se donan al Fondo de Huérfanos y Viudas de los Guardias Varrockianos.
    - (Action: Se abre la interfaz de lápida)
  - {{anchor|saradomin}}
  - [Choice]: ¿Quién es Saradomin?
    - **Father Aereck:** ¿Seguro que has oído hablar de nuestro dios, Saradomin?
    - **Father Aereck:** ¿Quien creó las fuerzas de la bondad y la pureza en este mundo? ¡No puedo creer tu ignorancia!
    - **Father Aereck:** Este es el dios con más seguidores que cualquier otro... al menos en esta parte del mundo.
    - **Father Aereck:** ¡Derrotó al malvado Zamorak en la cercana batalla de Lumbridge y nos defiende del mal!
    - [Menu]: Selecciona una opción
      - [Choice]: Oh, ESE Saradomin.
        - **Father Aereck:** Sólo hay un Saradomin.
        - **Player:** Sí. Pensé que habías dicho algo más.
      - [Choice]: Oh, lo siento, no soy de este mundo.
        - **Father Aereck:** ...
        - **Father Aereck:** Eso es... extraño.
        - **Father Aereck:** Pensé que las cosas que no eran de este mundo eran todas, ya sabes, baba y tentáculos.
        - [Menu]: Selecciona una opción
          - [Choice]: Yo no.
            - **Father Aereck:** Bueno, puedo verlo. Aún así, hay algo especial en ti.
            - **Player:** Gracias, creo.
          - [Choice]: ¡Lo soy! ¿Te gusta mi disfraz?
            - **Father Aereck:** ¡Argh! ¡Criatura asquerosa y audaz de otra dimensión! ¡Avaunt! ¡Vete en nombre de Saradomin!
            - **Player:** Está bien, está bien, ¡solo estaba bromeando!
      - [Choice]: ¿Puedes hablarme sobre el campo de batalla?
        - (continue|battlefield)
  - [Choice]: Bonito lugar el que tienes aquí. {{anchor|place}}
    - **Father Aereck:** Lo es, ¿no? Fue construido hace más de dos siglos.
  - [Choice]: cond=With a clay ring:|¿Puedes bendecir mi anillo?
    - **Father Aereck:** Ah, ¿deseas mostrar tu devoción por Saradomin dedicándole un anillo? Muy bien, sería un placer ayudarte.
    - (removes=clay ring) (receives=ring of devotion)
    - (Condition: Si el logro Bless Is More no se ha completado:)
      - {{RSFontAchievement|Bless Is More}}
      - (continue)
    - [Father Aereck inscribe el símbolo de Saradomin en la cara del sello de su anillo y ofrece una breve bendición sobre él.]
  - [Choice]: ¿Puedes hablarme sobre el cráter? {{anchor|battlefield}}
    - **Father Aereck:** Ah, Lumbridge Battlefield: ¡el sitio del regreso de Saradomin! ¡Ese fue un día trascendental para la iglesia y yo estuve allí!
    - **Father Aereck:** En una batalla titánica que duró meses, el poderoso Saradomin hizo retroceder a las fuerzas de Zamorak al inframundo al que pertenecen.
    - **Father Aereck:** Y ahora que Saradomin está aquí, podemos estar seguros de que estaremos a salvo bajo su protección divina.
    - **Father Aereck:** ¡Todos los elogios para Saradomin!

### Historical dialogue during the Battle of Lumbridge

- (Condition: Antes del Restless Ghost:)
  - **Father Aereck:** Bienvenido a la iglesia del santo Saradomin.
  - (continue)
- (Condition: Después del Restless Ghost:)
  - **Father Aereck:** ¡Bienvenido de nuevo a la iglesia del santo Saradomin, amigo mío! ¿Qué puedo hacer por ti hoy?
  - (continue)
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¡Estoy buscando una misión!
    - (above|quest)
  - [Choice]: ¿Puedes cambiar mi lápida ahora?
    - (above|gravestone)
  - [Choice]: ¿Quién es Saradomin?
    - (above|saradomin)
  - [Choice]: Bonito lugar el que tienes aquí.
    - (above|place)
  - [Choice]: ¿Puedes hablarme sobre el campo de batalla?
    - **Father Aereck:** ¡El campo de batalla de Lumbridge es donde el propio Saradomin está luchando actualmente contra Zamorak! ¡Gracias a Dios que está aquí! Si no hubiera aparecido cuando lo hizo, ¡ahora todos seríamos esclavos de Zamorak! Pero vino a nosotros desde muy lejos en nuestro momento de necesidad, e incluso ahora lucha contra el mal en Lumbridge Battlefield. Oh, debes estar de camino al campamento de guerra de Saradomin para poder ayudar. Está al noroeste de aquí. ¡No podemos dejar que el mal venza! ¡Buena suerte! ¡Y que Saradomin esté contigo!
