# Brimstail

- **Original Wiki Page**: [Transcript:Brimstail](https://runescape.wiki/w/Transcript%3ABrimstail)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Brimstail's cave


#### Antes del gran árbol

- **Brimstail:** Hola aventurero, ¿qué puedo hacer por ti?
- [Menu]: Elige una opción:
  - [Choice]: ¿Puedes teletransportarme a la Esencia Rúnica?
    - **Player:** ¿Puedes teletransportarme a la Esencia Rúnica?
    - **Brimstail:** Está bien. ¡Agarra tu sombrero!
    - **Brimstail:** {{RSChat|Senventior disthine molenko!}}
    - (Action: Brimstail te teletransporta a la mina Rune Essence)
  - [Choice]: Nada por ahora, gracias!
    - **Player:** Nada por ahora, ¡gracias!
    - **Brimstail:** Vale. ¡Solo recuerda que un amigo de un mago es amigo mío!

#### Después del gran árbol

- (ver | Los ojos de Gloufrie)

#### Después de Los ojos de Glouphrie

- **Brimstail:** Hola aventurero, ¿qué puedo hacer por ti?
- [Menu]: Elige una opción:
  - [Choice]: Hola, solo quería charlar.
    - **Player:** Hola, solo quería charlar.
    - **Brimstail:** ¡Siempre es un placer encontrarse con otro mago! ¡Especialmente uno que me ha ayudado tanto!
    - (Condition: Si el player ha perdido la pequeña semilla de cristal:)
      - **Brimstail:** Ah, por cierto, encontré esta cosa rara por ahí, ¿te pertenece?
      - [Brimstail te muestra una pequeña semilla de cristal.]
      - **Player:** Oh, sí. Me preguntaba a dónde había ido eso...
      - (receives=small crystal seed)
      - **Brimstail:** Deberías cuidar tus cosas con más cuidado, ¿sabes?...
      - **Player:** ¡Gracias!
    - (Condition: Si el player tiene la semilla de cristal pequeña:)
      - **Brimstail:** ¿Cómo van tus investigaciones?
      - **Player:** Oh, no está tan mal. Te haré saber si encuentro algo que creo que te resultará interesante...
      - **Brimstail:** ¡Gracias! Te lo agradecería.
      - (Condition: Si la semilla se ha convertido en un timbre:)
        - (end)
      - (Condition: Si la semilla sigue siendo una semilla:)
        - **Player:** ¿Qué hace esta semilla?
        - **Brimstail:** Fascinante... una semilla de cristal. Deberías echarle un vistazo al cuenco de cristal de la otra habitación, debe estar relacionado.
        - **Player:** Gracias, lo haré.
      - (Condition: Si la semilla ha sido convertida en sierra:)
        - **Player:** ¿Qué hace esta sierra de cristal?
        - (Condition: Antes Mientras Guthix Duerme:)
          - **Brimstail:** No tengo idea, debe haber sido de Oaknock, le gustaba hablar con los elfos.
          - **Player:** ¿Dónde puedo averiguar cómo funciona?
          - **Brimstail:** Errrm, no estoy seguro. Charle con Hazelmere, tal vez él lo sepa. Estuvo presente cuando Oaknock estaba vivo y podría haberlo visto usarlo.
          - **Player:** Excelente idea, lo haré. Gracias.
        - (Condition: Después de Mientras Guthix duerme:)
          - **Brimstail:** Recientemente leí que Oaknock usó algo como esto para ayudarlo a construir dispositivos que eran demasiado complicados para él solo con su habilidad. Quizás eso es lo que hace esta sierra.
          - [La sierra agregará tres niveles a su nivel Construction efectivo cuando esté construyendo algo que requiera una sierra.]
  - [Choice]: cond=After The Path of Glouphrie|He estado investigando a otro observador en Tree Gnome Village.
    - **Player:** He estado investigando a otro observador en Tree Gnome Village.
    - **Player:** Y, como consecuencia, encontré un complejo de cuevas subterráneas lleno de tortugas y pájaros terroríficos deformados. Parece estar debajo de Arposandra o, al menos, una ciudad con gnomos que usan pájaros terroríficos parlantes como guardias.
    - **Brimstail:** ¡Guau! Realmente has encontrado a Arposandra.
    - **Player:** Eso creo, aunque no puedo entrar. Está todo bloqueado. Pero encontraré una manera... eventualmente.
    - **Brimstail:** Bueno, ¡buena suerte!
  - [Choice]: Necesito extraer algo de esencia rúnica.
    - (arriba)

### Treasure Trails


#### Fácil

- **Brimstail:** ¡Bien hecho!
- (removes=the old clue scroll (easy))
- (Si el camino continúa:)
  - (receives=a new clue scroll (easy))
  - [¡Brimstail te ha dado otro pergamino de pistas!]
- (Si el sendero termina:)
  - (receives=reward casket (easy))
  - [¡Has encontrado un ataúd!]

#### Medio (reemplazo de Hazelmere)

- (Condition: Sólo la primera vez:)
  - **Brimstail:** Ah, sé para qué estás aquí.
  - **Player:** ¿Lo haces?
  - **Brimstail:** Sí. Pero antes de que te deje seguir adelante, debes ayudarme con este desafío.
- (receives=challenge scroll (medium))
- [¡Brimstail te ha dado un pergamino de desafío!]

##### Cuando hablé de nuevo

- **Brimstail:** ¿Sabes la respuesta a la pregunta?
- Ingrese la cantidad:<br>[Input field]
- (Condition: Cuando se le da la respuesta incorrecta:)
  - **Brimstail:** Esto no suena bien.
- (Condition: Cuando se le da la respuesta correcta:)
  - (removes=the clue scroll (medium) y desplazamiento de desafío (medio))
  - (Condition: Si el rastro continúa:)
    - (receives=a new clue scroll (medium))
    - [¡Brimstail te ha dado otro pergamino de pistas!]
  - (Condition: Si el sendero termina:)
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
  - **Brimstail:** ¡Gracias!
