# Jacquelyn

- **Original Wiki Page**: [Transcript:Jacquelyn](https://runescape.wiki/w/Transcript%3AJacquelyn)
- **Letter**: `J`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{ToC|limit=1}}

### In Lumbridge


#### Antes de realizar una tarea Slayer por primera vez

- **Jacquelyn:** 'Hola, ¿y qué buscas entonces?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Jacquelyn:** Soy aprendiz de Slayer Master.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué es un asesino?
        - **Player:** ¿Qué es un cazador?
        - **Jacquelyn:** Dios mío, ¿qué te enseñan en la escuela?
        - **Player:** Bueno... ejem...
        - **Jacquelyn:** Supongo que tendré que educarte entonces. Un asesino es alguien que está entrenado para luchar contra criaturas específicas. Saben que las criaturas tienen todas sus debilidades y fortalezas. Como puedes adivinar, hace que matarlos sea mucho más fácil.
        - [Menu]: Selecciona una opción
          - [Choice]: Vaya, ¿puedes enseñarme?
            - (abajo)
          - [Choice]: Me parece inútil.
            - (abajo)
      - [Choice]: Nunca he oído hablar de ti.
        - **Player:** Nunca había oído hablar de ti.
        - **Jacquelyn:** Eso es porque mi enemigo nunca vive para hablar de mí. Los cazadores somos un grupo peligroso.
        - [Menu]: Selecciona una opción
          - [Choice]: Vaya, ¿puedes enseñarme?
            - **Player:** Vaya, ¿puedes enseñarme?
            - **Jacquelyn:** Hmmm, bueno, no estoy tan seguro...
            - **Player:** ¡Por favor!
            - **Jacquelyn:** Oh, está bien, entonces, torciste a my arm. Tendrás que entrenar contra grupos específicos de criaturas.
            - **Player:** Bueno, entonces, ¿qué es lo primero?
            - [Menu]: ¿Cambiar su tarea Slayer asignada?
              - [Choice]: [First task] (predeterminado)
                - [Menu]: ¿Modificar su tarea Slayer asignada?
                  - [Choice]: [número] [monster's name] (predeterminado)
                    - (abajo)
                  - [Choice]: [número] [monster's name] (min)
                    - (abajo)
                  - [Choice]: [número] [monster's name] (máx.)
                    - **Jacquelyn:** Empezaremos cazando [monster]. Tendrás que matar a [número] de ellos.
                    - **Jacquelyn:** También necesitarás esta gema encantada, le permite a Slayer Masters, como a mí, contactarte y actualizarte sobre tu progreso. No te preocupes si lo pierdes; puedes comprar otro en cualquier Slayer Master.
                    - (receives=enchanted gem)
                    - [Menu]: Selecciona una opción
                      - [Choice]: ¿Tienes algún consejo para mí?
                        - (abajo2|Consejos de tarea)
                      - [Choice]: Ok genial!
                        - **Player:** ¡Vale, genial!
                        - **Jacquelyn:** ¡Buena suerte! No olvides volver cuando necesites una nueva tarea.
              - [Choice]: [Second task]
                - (above|modify)
          - [Choice]: Me parece inútil.
            - **Player:** Me parece inútil.
            - **Jacquelyn:** Haz lo que quieras.
  - [Choice]: ¿Tienes algo para intercambiar?
    - **Player:** ¿Tienes algo para intercambiar?
    - **Jacquelyn:** Tengo una amplia selección de equipos Slayer; ¡eche un vistazo!
    - (opens=Slayer Equipment)
  - [Choice]: Eh... nada...
    - **Player:** Eh... nada...

#### Después de obtener una tarea Slayer

- **Jacquelyn:** 'Hola, ¿y qué buscas entonces?
- [Menu]: Selecciona una opción
  - [Choice]: Necesito otra tarea.
    - **Player:** Necesito otra tarea.
      - (Condition: If you are currently on a Slayer assignment)
      - **Jacquelyn:**  Aún estás buscando a [assigned creatures]; Vuelve cuando hayas terminado tu tarea.
  - [Choice]: ¿Tienes algo para intercambiar?
    - **Player:** ¿Tienes algo para intercambiar?
    - **Jacquelyn:**  Tengo una amplia selección de equipos Slayer; ¡eche un vistazo!
      - (opens=Slayer Equipment)
  - [Choice]: Estoy aquí para discutir cualquier recompensa para la que pueda ser elegible.
    - Ver recompensas.
      - (opens=Slayer Rewards)
    - ¿Cómo gano puntos cooperativos para gastarlos en recompensas?
      - **Jacquelyn:**  Obtendrás puntos de recompensa cooperativa si completas al menos la mitad de tu contribución a una tarea con un amigo. Eso significa que debes estar en un grupo la mayor parte del tiempo que estés trabajando en la tarea, ¡pero no importa si tu amigo te gana en la mayoría de las muertes! Aún habrás estado en un grupo durante la mayor parte de tu contribución, por lo que aún tendrás derecho a un punto de recompensa cooperativa.
        - Ver recompensas.
          - (above|View rewards)
        - ¿Dónde puedo usar las recompensas cooperativas de comida y pociones?
          - (below|Where can I use the co-op food and potion rewards?)
        - Eso es todo, gracias.
          - (end)
    - ¿Dónde puedo usar las recompensas cooperativas de comida y pociones?
      - **Jacquelyn:**  Las recompensas se pueden usar en la mayoría de las áreas que comúnmente te enviamos para completar tus tareas.
        - Ver recompensas.
          - (above|View rewards)
        - ¿Cómo gano puntos cooperativos para gastarlos en recompensas?
          - (above|How do I earn co-op points to spend on rewards?)
        - Eso es todo, gracias.
          - (end)
  - [Choice]: Eh... nada...
    - **Player:** Eh... nada...
    - (end)

### Activating the enchanted gem


#### Si Chaeldar es tu Slayer Master actual

- **Jacquelyn:** Hola, Player, ¿en qué puedo ayudarte?
  - ¿Cómo estoy hasta ahora?
    - **Player:** ¿Cómo me va hasta ahora?
    - **Jacquelyn:** Actualmente estás asignado a matar a [assigned creatures]; sólo faltan X más.
      - ¿Quién eres?
        - (below|Who are you?)
      - ¿Dónde estás?
        - (below|Where are you?)
      - ¿Tienes algún consejo para mí?
        - (below|Got any tips for me?)
      - Eso es todo gracias.
        - **Player:** Eso es todo, gracias.
        - (end)
  - ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Jacquelyn:** Mi nombre es Jacquelyn; Soy un Slayer Master.
      - ¿Cómo estoy hasta ahora?
        - (above|How am I doing so far?)
      - ¿Dónde estás?
        - (below|Where are you?)
      - ¿Tienes algún consejo para mí?
        - (below|Got any tips for me?)
      - Eso es todo gracias.
        - (above|That's all thanks.)
  - ¿Dónde estás?
    - **Player:** ¿Dónde estás?
    - **Jacquelyn:** Me encontrarás en Lumbridge. Estaré aquí cuando necesites una nueva tarea.
      - ¿Cómo estoy hasta ahora?
        - (above|How am I doing so far?)
      - ¿Quién eres?
        - (above|Who are you?)
      - ¿Tienes algún consejo para mí?
        - (below|Got any tips for me?)
      - Eso es todo gracias.
        - (above|That's all thanks.)
  - ¿Tienes algún consejo para mí?
    - **Player:** ¿Tienes algún consejo para mí?
    - **Jacquelyn:** El último [assigned creature] que maté descubrí que [weapons] los derribó de manera efectiva.
    - (below|Assignment advice)
      - ¿Cómo estoy hasta ahora?
        - (above|How am I doing so far?)
      - ¿Quién eres?
        - (above|Who are you?)
      - ¿Dónde estás?
        - (above|Where are you?)
      - Eso es todo, gracias.
        - (above|That's all thanks.)
  - Nada realmente.
    - **Player:** Nada realmente.
    - (end)

### Casting NPC contact

- **Player:** ¿Hola?
- **Jacquelyn:** 'Hola, ¿quién es ese?
- **Player:** Soy Player. Estoy usando magia para comunicarme contigo.
- **Jacquelyn:** ¡Increíble! ¿Qué puedo hacer por ti?
- [Menu]: Selecciona una opción
  - [Choice]: Necesito otra tarea.
    - (above|I need another assignment.)
  - [Choice]: Eh... nada...
    - (above|Er...nothing...)

### {{Anchor|Assignment advice}}Assignment advice


#### Murciélagos

- **Jacquelyn:** Los murciélagos rara vez se encuentran en el suelo, por lo que tendrás que luchar contra ellos mientras están en el aire. Puedes encontrar algunos volando en las Catacumbas Lumbridge.

#### Aves

- **Jacquelyn:** Los pájaros no son las criaturas más inteligentes, pero ten cuidado con sus picos afilados y punzantes. Incluso las gallinas en Lumbridge buscan tu sangre, así que consíguelas antes de que te atrapen a ti.

#### Insectos de las cavernas

- **Jacquelyn:** Los insectos de las cavernas son como rastreadores de cuevas, excepto que son más pequeños y más fáciles de aplastar; aunque todavía sienten afición por las plantas. Acechan en la oscuridad debajo del pantano Lumbridge.

#### Limo de cueva

- **Jacquelyn:** Los limos de las cavernas son los primos menores de las jaleas. Pero no te dejes engañar: aún así pueden ser peligrosos, ya que a menudo son venenosos. Matar a los que están debajo del pantano Lumbridge podría ser un buen comienzo.

#### Vacas

- **Jacquelyn:** Las vacas son más grandes que tú y, a menudo, golpean fuerte pero reaccionan con bastante lentitud. Puedes masacrar a los de Lumbridge. Apuesto a que no traman nada bueno.

#### Ranas

- **Jacquelyn:** Las ranas atacarán y se moverán más rápido que el humano promedio, pero en general un guerrero experimentado puede lidiar con muchas de ellas con bastante rapidez. Puedes encontrarlos en el pantano del sur.

#### Fantasmas

- **Jacquelyn:** El último fantasma que maté lo encontré con armas arrojadizas que los derribaron de manera efectiva.
- Los fantasmas son muertos vivientes, por lo que no es lo más fácil de encontrar en zonas pobladas. Intenta buscar en el Draynor Manor abandonado.

#### duendes

- **Jacquelyn:** Los duendes en su mayoría son simplemente molestos, pero pueden ser crueles. Cuidado con las armas que a veces portan. Puedes encontrarlos en el lado este del río aquí en Lumbridge.

#### Ratas

- **Jacquelyn:** Las ratas vienen en diferentes tamaños si quieres un desafío o no. Puedes encontrar la variedad normal acechando en los terrenos del castillo o dirigirte hacia el sur, hacia el pantano, en busca de ratas gigantes.

#### Esqueletos

- **Jacquelyn:** Los esqueletos son muertos vivientes, por lo que Magic es tu mejor opción contra ellos. Los esqueletos se pueden encontrar en las catacumbas de Lumbridge.

#### Arañas

- **Jacquelyn:** Las arañas suelen ser venenosas y muchas variedades también se camuflan. He visto muchos al suroeste de Lumbridge.

#### Zombis

- **Jacquelyn:** Los zombis son muertos vivientes, así que ten cuidado. Puedes encontrar una variedad de luchadores de cadáveres en las catacumbas de Lumbridge o zombis en las alcantarillas en Draynor village.
