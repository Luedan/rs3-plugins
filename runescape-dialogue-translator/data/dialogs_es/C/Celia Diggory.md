# Celia Diggory

- **Original Wiki Page**: [Transcript:Celia Diggory](https://runescape.wiki/w/Transcript%3ACelia%20Diggory)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At the Varrock Dig Site


#### Hablando con ella

- **Celia Diggory:** Hola aventurero. ¿Has venido a ayudar con el esfuerzo de excavación?
- (Condition: Si el player lleva pergaminos Senntisten:)
  - **Celia Diggory:** ¡Veo que has encontrado algo especial entre los escombros!
  - **Celia Diggory:** Realmente pertenece a un museo. ¿Podría trabajar en una traducción y darte una copia?
  - (Condition: Si el jugador tiene un pergamino:)
    - [Menu]: {{transcript missing}}
      - [Choice]: Sí, toma mi pergamino para estudiarlo.
        - **Celia Diggory:** ¡Gracias! Me aseguraré de que esto llegue sano y salvo al museo Varrock.
        - [Celia spends a few minutes reading the scroll and scribbling in a notebook.] <!-- unchecked but probably tbox -->
        - **Celia Diggory:** ¿Quieres una copia de la traducción?
        - [Menu]: {{transcript missing}}
          - [Choice]: Sí, por favor.
            - (continue|transcript)
          - [Choice]: No, gracias.
            - (continue)
      - [Choice]: No, me gustaría conservarlo.
        - (continue)
  - (Condition: Si el jugador tiene varios pergaminos:)
    - [Menu]: {{transcript missing}}
      - [Choice]: Sí, toma mis pergaminos para estudiarlos.
        - **Celia Diggory:** ¡Gracias! Me aseguraré de que lleguen sanos y salvos al museo Varrock.
        - [Celia spends a few minutes reading the scroll and scribbling in a notebook.] <!-- unchecked but probably tbox -->
        - **Celia Diggory:** ¿Quieres una copia de la traducción?
        - [Menu]: {{transcript missing}}
          - [Choice]: Sí, por favor.
            - (continue|transcript)
          - [Choice]: No, gracias.
            - (continue)
      - [Choice]: No, me gustaría conservarlo.{{fact|Does this say 'it', not 'them'?}}
        - (continue)
- [Menu]: Elige una opción:
  - {{anchor|excavation}} [Elección]: ¿Esfuerzo de excavación?|Primera vez que ves estas opciones:
    - **Celia Diggory:** Uno de nuestros equipos de excavación desenterró recientemente una puerta antigua. La entrada prácticamente ha cedido, de ahí el ascensor, pero esta cámara parece prácticamente intacta.
    - **Celia Diggory:** La arquitectura definitivamente refleja el estilo zarosiano de la segunda edad, lo que sugiere que esto era parte de la antigua ciudad de Senntisten.
    - **Celia Diggory:** Parece ser una cámara de gran importancia. ¡Sospechamos que esta sala habría servido como sala del trono de Zaros!
    - **Celia Diggory:** ¡Parece haber una gran cantidad de energía divina residual alrededor, lo que sugiere que aquí tuvo lugar un evento divino importante!
    - (previous)
  - [Choice]: ¿Qué hay ahí abajo?|Solo arriba, y después de haber visto estas opciones antes: <!-- i.e. also after returning here from another option, don't have to go through the 'excavation' option dialogue -->
    - (above|excavation)
  - [Choice]: ¿Qué es este lugar?|Solo a continuación, y después de haber visto estas opciones antes:
    - (above|excavation)
  - {{anchor|help}} [Elección]: ¿Hay alguna forma de ayudar?|cond=Solo afuera:
    - **Celia Diggory:**Hemos estado extrayendo cristales del sitio de excavación. Hay depósitos de mineral de animica oscura que puedes extraer, ya que se interpone en nuestro camino.
    - **Celia Diggory:** A continuación, si eres lo suficientemente hábil en Agility, necesitamos transportar los cristales hasta aquí. Hay bicicletas que puedes usar para moverlo.
    - **Celia Diggory:** Finalmente, si has practicado tu Divination, estamos pidiendo a la gente que intente transmutar los cristales.
    - **Celia Diggory:** ¡Parece haber una gran cantidad de energía divina residual alrededor, lo que sugiere que aquí tuvo lugar un evento divino importante!
    - **Celia Diggory:** Hemos notado que esta energía se mueve por la habitación, incluso interactuando con algunos de nuestros equipos. Al menos parece estar teniendo un efecto positivo, por lo que le sugiero que dirija su atención hacia ello.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Por qué estás extrayendo los cristales?
        - **Celia Diggory:** Parecían estar creciendo de alguna manera. Deberías haber visto el estado del lugar cuando lo encontramos por primera vez. Estaban por todas partes.
        - **Celia Diggory:** Hemos decidido asegurarnos de eliminarlos por completo; es la única forma de asegurarnos de que no seguirán creando problemas a medida que continúa la restauración.
        - (otro)
      - [Choice]: ¿Por qué estás transmutando los cristales?
        - **Celia Diggory:** Para volverlos inertes. Uno de nuestros patrocinadores solicitó las diferentes coloraciones. Debería enviar a alguien a recogerlos.
        - (otro)
      - [Choice]: Pregunta por otra cosa.
        - (previous)
  - [Choice]: How can I help out here?|cond=Sólo dentro:
    - (above|help)
  - [Choice]: Weren't you just outside?|cond=Sólo dentro:
    - **Celia Diggory:** Bajé en el ascensor. Estaba parado justo a tu lado. ¿No lo recuerdas?
    - (previous)
  - {{anchor|transcript}} [Elección]: ¿Puedes darme una copia de las cartas traducidas?{{fact|Does this say 'letter' with only a single one handed in?|cond=After having returned a Senntisten scroll:}}
    - [Menu]: ¿Qué transcripción te gustaría?
      - [Choice]: Pergamino 1 - Carta firmada 'Pontifex Madromurt'.
        - [pic=Carta firmada 'Pontifex Madromurt' detail.png]
        - (previous)
      - [Choice]: Scroll 2 - Letter signed 'Pontifex Nabor'.|cond=Con el segundo pergamino entregado:
        - [pic=Carta firmada 'Pontifex Nabor' detail.png]
        - (previous)
      - [Choice]: Scroll 3 - Letter signed 'Pontifex Bilrach'.|cond=Con el tercer pergamino entregado:
        - [pic=Carta firmada 'Pontifex Bilrach' detail.png]
        - (previous)
      - [Choice]: [More...]
        - [Choice]: Scroll 4 - Damaged letter.|cond=Con el cuarto pergamino entregado:
          - [pic=Letra dañada detail.png]
          - (initial)
        - [Choice]: Todos ellos.
          - [pic=Letra dañada detail.png]
          - (initial)
        - [Choice]: No importa.
          - (initial)
        - [Choice]: [More...]
          - (previous)
  - [Choice]: Adiós.
    - **Player:** Adiós.

#### Verificar progreso

- Hasta ahora has adquirido {{Colour/800,000 experience in Agility, and ZZCMD0ZZ[number]}}/800.000 de experiencia en Divination.}}
- También has entregado {{Colour out of 4 Senntisten scrolls.}}

#### Senderos del tesoro

- {{transcript missing}}
