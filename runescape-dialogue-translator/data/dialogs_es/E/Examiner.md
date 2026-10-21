# Examiner

- **Original Wiki Page**: [Transcript:Examiner](https://runescape.wiki/w/Transcript%3AExaminer)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Sin la pista Treasure Trails o la tarea de celebración del 25 aniversario en progreso


##### Antes del sitio de excavación

- (ver|El sitio de excavación#Comenzando)

##### Después del sitio de excavación

- **Examiner:** ¡Hola! Mi colega me dice que ayudaste a descubrir un altar oculto al dios Zaros.
- **Examiner:** ¡Un gran erudito y arqueólogo! Buena salud y prosperidad para ti.
- [Menu]: Selecciona una opción
  - [Choice]: Gracias.
    - **Player:** ¡Gracias!
  - [Choice]: He perdido mi paleta.
    - **Player:** He perdido mi paleta.
    - (Condition: Si el player no tiene llana:)
      - **Examiner:** Querido amigo. Esa también fue buena. Es un buen trabajo, tengo otro. Aquí tienes...
      - (receives=a trowel)
    - (Condition: Si el player ya tiene paleta:)
      - **Examiner:** ¿En serio? Mira en tu backpack y asegúrate primero.

#### Senderos del tesoro


##### Recibiendo la caja del rompecabezas

- **Examiner:** ¡Hola! Por favor complete esto.
- (receives=puzzle box)
- [¡El examinador te ha dado una caja de rompecabezas!]

##### Sin resolver el rompecabezas

- **Examiner:** Me temo que no has terminado el rompecabezas.

##### Con el rompecabezas resuelto

- (Si el camino continúa:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [¡El examinador te ha dado otro pergamino de pistas!]
  - (continue)
- (Si el sendero termina:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Examiner:** ¡Correcto! ¡Bien hecho!

#### Durante la tarea de celebraciones del 25 Aniversario

- **Examiner:** ¡Correcto! Hora de tu examen.
- **Player:** ¡Pero no he estudiado! ¡No estoy preparado!
- **Examiner:** ¡Ajá! Por supuesto, estoy bromeando. Aquí aprendemos haciendo.
- {{RSFontAchievement|You Dig?|Talk to an examiner at the Varrock Dig Site's Exam Centre.}}
- ((Se muestra en una ventana emergente de finalización de tarea:))
  - {{Colour|#F0BE79| TAREA DEL 25 ANIVERSARIO |#181513}}
  - ¿Excavas?
  - Hable con un examinador en el centro de exámenes del sitio de excavación Varrock.
  - (continue)
- **Examiner:** ¡Así que toma un azadón y quédate atrapado!
- (Condition: Si se han completado todas las tareas:)
  - **Player:** Parece que he completado todo. ¡Será mejor que vaya a ver a Hans sobre esa recompensa!
