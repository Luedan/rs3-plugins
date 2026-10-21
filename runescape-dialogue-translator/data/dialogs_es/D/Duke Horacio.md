# Duke Horacio

- **Original Wiki Page**: [Transcript:Duke Horacio](https://runescape.wiki/w/Transcript%3ADuke%20Horacio)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Lumbridge Castle

- **Duke Horacio:** Saludos. Bienvenidos a mi castillo.
- (Condition: Si el player le habla por primera vez:)
  - {{RSFontAchievement|Hail to the Duke, Baby|Speak to Horacio, the Duke of Lumbridge.}}
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: cond=After Dragon Slayer:|Busco un escudo que me proteja del aliento de dragón.
    - (Condition: Sin escudo anti-dragón en backpack o en banco:)
      - **Duke Horacio:** Un caballero que va en busca de un dragón, ¿eh? ¿Qué dragón pretendes matar?
      - (continue)
    - (Condition: Con escudo anti-dragón en backpack o en banco:)
      - **Duke Horacio:** ¿Qué, otro? A ustedes, los aventureros, les gusta acumular reservas, ¿no?... ¿Tienen algún dragón en particular en mente?
      - (continue)
    - **Duke Horacio:** Por supuesto. Ahora que has matado a Elvarg, ¡te has ganado el derecho a hacerlo!
    - (Condition: Sin al menos un espacio backpack libre:)
      - **Duke Horacio:** Parece que no tienes suficiente espacio libre para tomar el escudo en este momento.
    - (Condition: Con al menos un espacio backpack libre:)
      - (receives=anti-dragon shield)
      - [El duque te entrega el escudo.]
  - [Choice]: ¿Tienes alguna misión para mí?
    - **Duke Horacio:** No, todo está bien.
  - [Choice]: ¿Dónde puedo encontrar dinero?
    - **Duke Horacio:** He oído que mucha gente local gana dinero aprendiendo una habilidad. Muchas personas se las arreglan en la vida convirtiéndose en herreros, cocineros, mineros y leñadores consumados.
  - [Choice]: cond=After partial completion of You Are It:|¿Qué puedes contarme sobre Uri?
    - **Duke Horacio:** ¿Hm? Uri fue la funeraria que ayudó a organizar la despedida de mi querida Oriana.
    - **Duke Horacio:** Fue muy complaciente; Admito que en mi dolor le pedí mucho pero él nunca se quejó.
    - **Duke Horacio:** Quizás el gesto más amable fue que me permitió organizar un ataúd con las pertenencias de Oriana para colocarlo con ella.
    - **Duke Horacio:** Una de esas cosas son las cartas que intercambiamos cuando nos conocimos. Oh, Ori, te extraño mucho.

#### Diálogo histórico

- **Duke Horacio:** Saludos. Bienvenidos a mi castillo.
- (Condition: Si el player le habla por primera vez:)
  - {{RSFontAchievement|Hail to the Duke, Baby|Speak to Horacio, the Duke of Lumbridge.}}
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: cond=After Dragon Slayer:|Busco un escudo que me proteja del aliento de dragón.
    - (arriba)
  - [Choice]: ¿Tienes alguna misión para mí?
    - (arriba)
  - [Choice]: ¿Dónde puedo encontrar dinero?
    - (arriba)
  - [Choice]: ¿Qué pasó con el castillo?
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Puedes darme un breve resumen de lo que pasó?
        - (Condition: Durante la Batalla de Lumbridge:)
          - **Player:** ¿Puedes darme un breve resumen de lo que pasó?
          - **Duke Horacio:** Sí, el castillo ha sufrido algunos... problemas últimamente. En caso de que no lo hayas notado, hay un gran cráter sobre donde están peleando Saradomin y Zamorak.
          - **Duke Horacio:** Justo después de llegar al mundo nuevamente, comenzaron a pelear y las fuerzas desatadas fueron demasiado para los muros. ¡Secciones enteras colapsaron por completo!
          - **Duque Hoarcio:** Afortunadamente, mis guardias estaban listos y eran capaces, e inmediatamente se pusieron a trabajar para ayudar a la gente de Lumbridge a mantenerse alejados del campo de batalla.
          - **Duke Horacio:** Están haciendo un buen trabajo, pero me preocupa que sean muy pocos para proteger a los ciudadanos, y a mí mismo, de las fuerzas que hacen estragos en el campo de batalla.
          - **Duke Horacio:** Pero no puedo hacer más para ayudarlos: ¡mi presupuesto no alcanza hasta ahora! Sólo nos queda esperar que Saradomin y Zamorak se centren el uno en el otro, y no aquí.
        - (Condition: Después de la Batalla de Lumbridge:)
          - **Duke Horacio:** Sí, el castillo sufrió mucho durante la reciente Batalla de Lumbridge: Saradomin y Zamorak estaban peleando en el cráter que se puede ver hacia el oeste.
          - **Duke Horacio:** Justo después de llegar al mundo nuevamente, comenzaron a pelear y las fuerzas desatadas fueron demasiado para los muros. ¡Secciones enteras colapsaron por completo!
          - **Duke Horacio:** Afortunadamente, mis guardias estaban listos y eran capaces, e inmediatamente se pusieron a trabajar para ayudar a la gente de Lumbridge a mantenerse alejados del campo de batalla.
          - **Duke Horacio:** Hicieron un excelente trabajo protegiéndonos y han sido ejemplares en su conducta. Estoy orgulloso de ellos.
          - (Condition: Durante el Lumbridge Rebuildathon:)
            - **Duke Horacio:** Ahora que la batalla ha terminado, viene gente de todo el mundo para ayudar a reconstruir Lumbridge. Estoy abrumado por su generosidad.
            - **Duke Horacio:** Si has venido a ayudar, debes hablar con Foreman George al norte del castillo.
            - **Duke Horacio:** Sin embargo, me alegro de que la batalla haya terminado.
          - (Condition: Después del Lumbridge Rebuildathon:)
            - **Duke Horacio:** Cuando terminó la batalla, vino gente de todo el mundo para ayudar a reconstruir Lumbridge. Me sentí abrumado por su generosidad.
            - **Duke Horacio:** Cuando los dioses empezaron a pelear, me preocupaba que significara el fin de Lumbridge, pero ahora la ciudad se ha recuperado.
      - [Choice]: ¿Puedes mostrarme lo que pasó de nuevo?
        - [Menu]: ¿Reproducir la escena inicial?
          - [Choice]: si
            - (Action: Reproducciones de escenas.)
          - [Choice]: No
            - (end)
  - [Choice]: [World Event] Hablar del castillo.
    - **Duke Horacio:** La situación en Lumbridge es catastrófica, pero creo que es posible hacer algo al respecto si la dividimos en partes pequeñas y manejables.
    - **Duke Horacio:** He desbloqueado oficialmente la tesorería de emergencia y planeo usarla para abordar problemas individuales que me lleguen.

### During summer events

- **Duke Horacio:** ¡Qué evento tan feliz tenemos aquí! Pero lo que nos falta es un castillo de arena Lumbridge, sí, eso terminaría bien el evento.
- **Player:** No eres muy sutil acerca de lo que quieres, ¿verdad?
pt:Transcrição:Duque Horacio
