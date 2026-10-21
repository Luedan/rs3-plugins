# Trader Stan

- **Original Wiki Page**: [Transcript:Trader Stan](https://runescape.wiki/w/Transcript%3ATrader%20Stan)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Port Sarim


#### Diálogo estándar

- **Trader Stan:** ¿Puedo ayudarte?
- [Menu]: Elige una opción:
  - [Choice]: Sí, ¿quién eres?
    - **Player:** Sí, ¿quién eres?
    - **Trader Stan:** ¡Soy Trader Stan, propietario y operador de la mayor flota de barcos mercantes y embarcaciones fletadas que jamás haya surcado los mares!
    - **Trader Stan:** Si quieres llegar a un puerto rápidamente, puedes alquilar uno de mis barcos para que te lleve allí, si el precio es correcto...
    - **Player:** Entonces, ¿adónde puedo ir exactamente con sus barcos?
    - **Trader Stan:** Llevamos barcos desde Port Phasmatys hasta Port Tyras, parando en Port Sarim, Catherby, Brimhaven, Musa Point, Oo'glog y Port Khazard.
    - **Trader Stan:** Quizás también atraquemos en Mos Le'Harmless de vez en cuando, si entiendes lo que quiero decir...
    - **Player:** Vaya, son muchos puertos. ¿Supongo que tienes algunas cosas exóticas para intercambiar?
    - **Trader Stan:** ¡Por supuesto que sí! Mis tripulantes y yo tenemos acceso a artículos comprados y vendidos en todo el mundo.
    - **Trader Stan:** ¿Te gustaría echar un vistazo?
    - [Menu]: Selecciona una opción
      - [Choice]: si
        - **Player:** Sí.
        - (opens=Trader Stan's Trading Post)
      - [Choice]: No
        - **Player:** No.
        - **Trader Stan:** Bueno, está bien. ¿Te gustaría alquilar un barco?
        - [Menu]: Selecciona una opción
          - [Choice]: Sí, me gustaría alquilar un barco.
            - (below|charter)
          - [Choice]: No.
            - (end)
  - [Choice]: Habla sobre el Skulls pirate, Jed.
    - (Condition: Antes de impresionar a los lugareños:)
      - (ver|Impresionando a los lugareños)
    - (Condition: Después de impresionar a los lugareños:)
      - **Trader Stan:** ¡Vaya a buscarlo, capitán!
    - (Condition: Después de Jed Hunter:)
      - **Player:** Jed está muerto, Stan. Jed está muerto.
    - (Condition: Después de Ojo por Ojo:)
      - **Player:** El no-muerto de Jed, Stan. Y ahora también muerto. De nuevo. Bien esta vez, creo.
  - [Choice]: Habla de barcos chárter.
    - **Player:{{anchor|charter}}** Sí, me gustaría alquilar un barco.
    - **Trader Stan:** Por supuesto [sir/madam], ¿adónde te gustaría ir?
    - ((Se abre la interfaz de destino de Charter Ship.))

#### Senderos del tesoro


##### Recibiendo la caja del rompecabezas

- **Trader Stan:** ¡Aquí tienes!
- (receives=puzzle box)
- [¡Trader Stan te ha regalado una caja de rompecabezas!]

##### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- **Trader Stan:** No, eso aún no está completo.

##### Cuando se le habla con el rompecabezas resuelto

- (Si el camino continúa:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [¡Trader Stan te ha dado otro pergamino de pistas!]
  - (continue)
- (Si el sendero termina:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Trader Stan:** ¡Eso es genial, te mereces tu tesoro!
