# Cam the Camel

- **Original Wiki Page**: [Transcript:Cam the Camel](https://runescape.wiki/w/Transcript%3ACam%20the%20Camel)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Al Kharid


#### En mundos gratuitos

- ((The player says one of the following at random:))
  - *Diálogo 1:*
    - **Player:** Si me acerco a ese camello, probablemente me arrancará la mano de un mordisco.
    - (continue|glare)
  - *Diálogo 2:*
    - **Player:** Mmm... Parece que ese camello sería un buen kebab.
    - (continue|glare)
  - *Diálogo 3:*
    - **Player:** Me pregunto si ese camello tendrá pulgas...
    - (continue|glare)
- (Action: El camello hace un ruido.)
- ((One of the following messages plays at random:))
  - *Diálogo 1:*
    - El camello te escupe y saltas hacia atrás apresuradamente.
  - *Diálogo 2:*
    - El camello gira la cabeza y te mira fijamente.
  - *Diálogo 3:*
    - El camello intenta pisotearte el pie, pero lo retiras rápidamente.

#### En los mundos de los miembros, sin camuleto ni cramulet

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregúntale al camello por su estiércol.
    - **Player:** Lamento molestarte, pero ¿podrías <br> ahorrarme un poco de estiércol?
    - El camello no pareció apreciar esa pregunta.
  - [Choice]: Di algo desagradable.
    - (above|On free-to-play worlds)
  - [Choice]: Ninguno de los dos, soy una persona educada.
    - Decides no ser grosero.

#### Con camuleto o cramulet

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Pregúntale al camello por su estiércol.
    - **Player:** Lamento molestarte, pero ¿podrías <br> ahorrarme un poco de estiércol?
    - **Cam the Camel:** ¿Hablas en serio?
    - **Player:** Ah, sí. Si fueras tan amable...
    - **Cam the Camel:** Bueno, primero cierra los ojos.<br> ¡No lo haré mientras me miras!
    - (Action: La pantalla se vuelve negra momentáneamente.)
    - (Cierras los ojos...|color=#FF0000)
    - **Cam the Camel:** ¡Espero que eso sea lo que querías!
    - **Player:** Ohhh, sí. Hermoso.
  - [Choice]: Di algo desagradable.
    - ((The player says one of the following at random:))
      - *Diálogo 1:*
        - **Player:** Si me acerco a ese camello, probablemente me arrancará la mano de un mordisco.
        - **Cam the Camel:** ¿Qué fue eso?
      - (continue|important)
      - *Diálogo 2:*
        - **Player:** Mmm... Parece que ese camello sería un buen kebab.
        - **Cam the Camel:** ¿Qué fue eso?
        - (continue|important)
      - *Diálogo 3:*
        - **Player:** Me pregunto si ese camello tendrá pulgas...
        - **Cam the Camel:** ¿Qué fue eso?
        - (continue|important)
    - **Player:** Nada importante.
    - **Cam the Camel:** Hace mucho calor, ¿no crees?
    - **Player:** No le gustan los camellos, ¿verdad?
    - **Cam the Camel:** ¿Estás bromeando? ¡Hace mucho calor aquí afuera! Sentarse junto al oasis es la única forma de mantenerse fresco.
    - **Player:** Pensé que los camellos llevaban su propia agua en sus jorobas.
    - **Cam the Camel:** Nunca es suficiente. Y siempre hace demasiado calor para ir a cualquier parte del desierto.
    - **Cam the Camel:** A veces desearía poder viajar a lugares más frescos, como todos esos aventureros que veo pasar por aquí.
    - **Player:** Bueno, las aventuras también son un trabajo sediento.
    - **Cam the Camel:** Oh, es una lástima.
    - **Cam the Camel:** En ese caso, me quedaré en este agradable y fresco oasis.
  - [Choice]: Ninguno de los dos, soy una persona educada.
    - Decides no ser grosero.

### Treasure Trails


#### Recibiendo la caja del rompecabezas

- (Condition: Without a camulet or cramulet:)
  - **Cam the Camel:** ¡Grrrrrr!
  - (continue)
- (Condition: With a camulet or cramulet:)
  - **Cam the Camel:** ¡Aquí está tu caja de rompecabezas!
  - (continue)
- (receives=puzzle box)
- [Cam the Camel te ha dado una caja de rompecabezas... ¡de alguna manera!]

#### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- (Condition: Without a camulet or cramulet:)
  - Cam the Camel no está impresionado.
- (Condition: With a camulet or cramulet:)
  - **Cam the Camel:** Eso no es exactamente lo que estaba buscando.

#### Cuando se le habla con el rompecabezas resuelto

- (Si el camino continúa:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [Cam the Camel te ha dado otro pergamino de pistas... ¡de alguna manera!]
  - (continue)
- (Si el sendero termina:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- (Condition: Without a camulet or cramulet:)
  - **Cam the Camel:** ¡Grrronk!
- (Condition: With a camulet or cramulet:)
  - **Cam the Camel:** ¡Esa es tu recompensa!
