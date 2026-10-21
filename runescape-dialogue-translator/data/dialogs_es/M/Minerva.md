# Minerva

- **Original Wiki Page**: [Transcript:Minerva](https://runescape.wiki/w/Transcript%3AMinerva)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Player:** ¿De quién es esta tumba? Debe haber sido alguien especial para que la ciudad de Falador los honre con tal lugar de descanso.
- **Minerva:** La historia de mi familia está profundamente arraigada en los cimientos mismos de Falador, mucho antes de que existiera un castillo.
- **Minerva:** Ella sirvió fielmente al rey Raddallin y viajó a cada rincón de cada reino para ayudar con la unificación de lo que luego se convirtió en el Reino de Asgarnia.
- **Minerva:** Durante sus viajes, aprendió todo lo que pudo de las diversas tribus y pueblos por los que pasó, dominando todo lo que le enseñaron.
- **Minerva:** Mientras Asgarnia florecía, continuó sirviendo a su rey antes de pasar finalmente a la luz de Saradomin. Para siempre ser recordado.
- **Player:** ¿Cómo se llamaba?
- **Minerva:** Su nombre era Meira.
- **Minerva:** Antes de su fallecimiento, para marcar su lugar en la historia y como gesto de todo lo que hizo por el rey, fue honrada con una capa hecha del hilo más mágico.
- **Minerva:** La capa fue encantada por alguien perdido en los libros de historia. Sin embargo, el encantamiento que lanzan impide que personas indignas usen la capa.
- **Player:** ¿Pero puedes usarlo?
- **Minerva:** El dominio de Meira sobre todas las habilidades del mundo se convirtió en una especie de credo para nuestra familia, por lo que continuamos su legado transmitiendo lo que ella comenzó.
- **Minerva:** Luego llegó un momento en el que honramos a quienes no pertenecen a nuestra familia con tal bendición.
- (Condition: Si pregunta por la tumba después de haber insertado la piedra angular:)
  - (continue|After inserting the blurite keystone)
- **Player:** Si domino todas las habilidades, ¿puedo usar la capa?
- **Minerva:** Si dominas todas las habilidades y eres capaz de crear una piedra angular hecha de rubíes, esmeraldas y zafiros engastados en un poco de blurita, entonces coloca dicha piedra angular en la ranura que ves en la tumba.
- **Minerva:** La tumba misma decidirá si eres digno. Entonces, y sólo entonces, te ofreceré la oportunidad de usar la capa.
- **Player:** ¡Lo intentaré!
- **Minerva:** Ah, y hay una condición.
- **Player:** ¿Mmm?
- **Minerva:** Si algún día logras ganarte la capa. No debes venderlo ni donarlo al Museo Varrock. Hace tiempo que intentan hacerse con esto. No es una prenda para dejarla sin usar y acumulando polvo.
- [Una piedra angular de Blurita se puede fundir en un horno utilizando Blurita, zafiros, rubíes y esmeraldas.]

### After inserting the blurite keystone

- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Cuál es tu nombre?
    - **Minerva:** Mi nombre es Minerva. Un placer conocerte finalmente, Player.
    - **Player:** Pero no te dije mi nombre.
    - **Minerva:** Te has ganado bastante reputación y los rumores tienden a viajar rápidamente por estos lugares.
    - **Player:** ¡Simplemente hago lo que hago! Encantado de conocerte.
    - (previous)
  - [Choice]: ¿Soy lo suficientemente digno para comprar esa capa?
    - **Minerva:** ¡Gracias! Fue un camino largo, pero eso es porque quiero asimilar todo lo que hay que saber.
    - **Player:** ¡He dominado todas las habilidades!
    - **Minerva:** Así que sí, Player. Este increíble logro significa que eres digno de usar la capa. Aunque la elaboración artesanal de una capa de este tipo requiere tiempo y esfuerzo, tendrá un costo.
    - **Minerva:** Parece justo ofrecerte la capa por {{fe|{{globals|total skills}} * 120000}} coins - 120.000 por cada habilidad que hayas dominado.
    - [Menu]: ¿Pagar {{fe|{{globals|total skills * 120000}} coins por una verdadera capa de maestría?}}
      - [Choice]: ¡Claro!
        - **Player:** Eso sería genial, gracias.
        - (removes={{fe|{{globals|total skills) * 120000}} coins}} (receives=a master max cape and hood)
        - **Minerva:** ¡Aquí tienes! Disfrútalo y por favor, cuídalo.
        - **Minerva:** ¡No vayas a venderlo al museo Varrock!
      - [Choice]: No, gracias.
        - **Player:** Tendré que dejar pasar esa oferta por ahora. ¡Aunque gracias!
  - [Choice]: ¿Qué es esta tumba?
    - (above|Standard dialogue)
  - [Choice]: ¿Cuál es el símbolo en la parte superior de la tumba?
    - **Minerva:** Es una piedra angular muy simple que creaste para demostrar que dominas todas las habilidades de RuneScape.
    - **Player:** Pero fue muy fácil de hacer. Sólo un trozo de metal y un puñado de gemas. Cualquiera con un martillo sin filo y un cincel sin filo podría haberlo hecho.
    - **Minerva:** Todo este tiempo has pasado practicando habilidades y todavía no crees en la magia, ¿eh?
    - **Player:** Supongo. Sin embargo, no se sintió muy mágico.
    - **Minerva:** Eso es porque la magia está en ti, Player. Tú mismo lo dijiste, es sólo un trozo de metal y algunas gemas. Pero TÚ fuiste quien lo logró.
    - (previous)
