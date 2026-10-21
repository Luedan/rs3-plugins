# Jarvald

- **Original Wiki Page**: [Transcript:Jarvald](https://runescape.wiki/w/Transcript%3AJarvald)
- **Letter**: `J`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before The Fremennik Trials


#### En Rellekka


##### Hablar con

- **Jarvald:** ¿Qué quieres de mí, outsider? Es nuestra política no asociarnos con personas que no sean de nuestra tribu.
- [Menu]: ¿Sobre qué te gustaría preguntar?
  - [Choice]: ¿Dónde está tu jefe?
    - **Player:** ¿Dónde está tu jefe? Considero muy discriminatorio negarse a hablar con alguien alegando que no forma parte de su tribu.
    - **Jarvald:** No entiendo bien tu discurso externo, pero mi lealtad está con el cacique Brundt. Él reside en nuestro largo salón; es el gran edificio de allí, deberías hablar con él porque él habla por todos nosotros.
  - [Choice]: Qué está haciendo Jarvald.
    - **Player:** Entonces, ¿qué estás haciendo aquí?
    - **Jarvald:** Esto no debería preocuparte, extranjero. Estoy esperando que otros Fremenniks se unan a mí en una expedición a la Isla Waterbirth.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Isla del nacimiento del agua?
        - **Jarvald:** Es una pequeña isla en forma de media luna justo al noroeste de aquí, outsider. Tenemos muchas leyendas al respecto, como el cuento del cielo roto y el día de los mares verdes. Sin embargo, el motivo por el que viajo allí es un asunto más serio de Fremennik. Dudo que un extranjero esté interesado.
      - [Choice]: ¿Puedo venir?
        - (Condition: Primera vez que elige esta opción:)
          - **Player:** Oye, tipo bárbaro aterrador, ¿crees que puedo unirme a ti en esta expedición?
          - **Jarvald:** ¿¿Un extranjero se une a nosotros en una cacería honorable??? Bueno... supongo... que podría permitirte unirte a nosotros, aunque es una violación de muchas de nuestras costumbres...
          - **Player:** Oh, ¿por favor? ¡Realmente AMO matar cosas!
          - **Jarvald:** Bueno... Sigo sin estar convencido de que sería prudente permitir que un extranjero se una a nosotros en una batalla tan peligrosa, pero tu entusiasmo parece bastante genuino... Te permitiré escoltarnos, pero primero debes pagarme una suma de dinero.
          - **Player:** ¿Qué? Eso es indignante, ¿por qué cobrarme dinero? ¿Y cuánto me cuesta?
          - **Jarvald:** Ah, los extranjeros le han robado a mi gente durante muchos años, de esta manera puedes ayudar a mi comunidad con una pequeña cantidad de dinero... Digamos... 1000 coins. A pagar por adelantado, por supuesto. Para ello, te llevaré a la isla Waterbirth en mi barco y te traeré de regreso aquí cuando te hayas saciado de la caza. Suponiendo que todavía estés vivo para desear irte, por supuesto.
        - {{anchor|pay-trip}}**Jarvald:** Entonces, ¿tienes los 1000 coins para mi servicio y estás listo para partir ahora?
        - [Menu]: Selecciona una opción
          - [Choice]: SI
            - (Condition: Si el player no tiene suficiente coins:)
              - No puedes permitirte eso.
              - **Jarvald:** Ah, extranjero... Voy más allá de mi deber al permitirte que me acompañes, ¿y tú intentas estafarme con una tarifa razonable? Esta no es forma de comportarse ni siquiera para un extranjero...
            - (Condition: Si el player tiene suficiente coins:)
              - (removes=1,000 coins)
              - {{anchor|back-to-waterbirth}}Saliendo de Rellekka hacia la isla Waterbirth.
              - (Action: La pantalla se desvanece y luego aparece. el player aparece en Waterbirth Island, en la costa noreste.)
              - (Condition: Primera vez que viaja a la isla Waterbirth:)
                - (Condición: si el player no ha completado Las Pruebas Fremennik:)}
                  - **Jarvald:** Te sugiero que te dirijas a la cueva con cierta urgencia, extranjero, el aire frío aquí afuera podría ser demasiado para personas como tú...
                - (Condition: Si el player ha completado Las Pruebas Fremennik:)
                  - **Jarvald:** Me dirigiría directamente a la cueva y no me demoraría demasiado [Fremennik name], los vientos fríos de esta isla pueden atravesarte si pasas demasiado tiempo en ellos.
          - [Choice]: NO
            - {{anchor|decline-travel-waterbirth}}**Player:** No, en realidad tengo algunas cosas que hacer aquí primero.
            - **Jarvald:** Como desees. Ven a verme cuando tu sed de sangre necesite saciar.
      - [Choice]: ¡Bonito sombrero!
        - **Player:** Oye, tengo que decir que el sombrero que llevas ahí luce muy bien.
        - **Jarvald:** En realidad es un timón, outsider, pero de todos modos se agradece el sentimiento.
      - [Choice]: Vale, adiós.
        - {{anchor|know-how-to-party}}**Player:** Vaya, ustedes los Fremenniks saben cómo divertirse. Bueno, nos vemos por ahí.
  - [Choice]: nada
    - {{anchor|nothing}}**Player:** En realidad, no creo que tenga nada de qué hablar contigo...

##### Viaje-Nacimiento en el agua


##### Antes de pedir viajar a Waterbirth Island

- **Jarvald:** No, extranjero, no te llevaré allí.

##### Después de pedir viajar a Waterbirth Island

- (arriba2|viaje de pago)

#### En la isla Waterbirth


##### Hablar con

- **Jarvald:** ¡Ah, aún vives, extranjero! ¿Se ha hartado de la caza y desea volver, o todavía siente la alegría del sacrificio?
- {{anchor|leave-waterbirth}}[Menú]: ¿Salir de la isla?
  - [Choice]: si
    - **Jarvald:** Entonces déjanos ir; ¡Habrá muerte que traerá aquí otro día!
    - {{anchor|back-to-rellekka}}Saliendo de la Isla Waterbirth para Rellekka.
    - (Action: La pantalla se desvanece y luego aparece. el player aparece en Rellekka, en el muelle más al noroeste.)
  - [Choice]: No
    - **Jarvald:** ¡Ja, ja, ja! ¡Un verdadero cazador de corazón!
    - **Jarvald:** Yo mismo he matado a más de cien bocas de daga, ¡y no pensé que fueran demasiados!

##### Viajes-Rellekka

- (arriba2|volver a-rellekka)

### After The Fremennik Trials


#### En Rellekka


##### Hablar con

- **Jarvald:** ¡Saludos, [Fremennik name]!
- (Condition: Si el nombre Fremennik de el player es Jarvald:)
  - **Jarvald:** ¡Ah, y qué nombre tan glorioso es ese! ¡Digno sólo de los mejores guerreros!
  - **Player:** Je. Sí, tienes razón.
- **Jarvald:** Entonces, ¿qué te trae de vuelta a la feria Rellekka? ¡Ha pasado demasiado tiempo desde que bebiste en el gran salón con nosotros y cantaste sobre tus batallas!
- [Menu]: ¿Sobre qué te gustaría preguntar?
  - [Choice]: Qué está haciendo Jarvald.
    - **Player:** Entonces, ¿qué estás haciendo aquí?
    - **Jarvald:** ¿No te has enterado, [Fremennik name]? ¡Estoy liderando una expedición a la isla Waterbirth!
    - {{anchor|expedition-options}}[Menú]: Seleccione una opción
      - [Choice]: ¿Isla del nacimiento del agua?
        - **Jarvald:** ¿Nunca has viajado a Waterbirth Island, [Fremennik name]? Me sorprende, es un lugar de una belleza natural excepcional.
        - **Jarvald:** ¡O al menos así era! Pero ahora las cosas han cambiado...
        - **Player:** ¿Cambiado? ¿Qué quieres decir con cambiado?
        - **Jarvald:** Parece que las bestias marinas que conocemos como bocas de daga han comenzado a eclosionar una vez más... Y puede que haya otras de su calaña allí también.
        - **Player:** ¿Bocas de daga?
        - **Jarvald:** ¡Sí, los bocas de daga! Estas viles criaturas vivieron cerca de aquí una vez, pero pensábamos que todas habían sido expulsadas a las profundidades del océano hace muchas lunas.
        - **Jarvald:** Solo puedo imaginar que una reina boca de daga haya anidado en algún lugar cercano y haya engendrado su loque bajo el mar una vez más, y algunas de ellas hayan migrado a la hermosa Isla Waterbirth.
        - **Player:** ¿Entonces tienes miedo de que ataquen a Rellekka?
        - **Jarvald:** ¿Asustado? ¡Ja, ja, ja!
        - **Jarvald:** ¡Nos hieres con tu interrogatorio, [Fremennik name]!
        - **Jarvald:** ¡Nos alegra que los boca de daga hayan regresado a estas costas, porque eso significa que tendremos la oportunidad de cazarlos una vez más como lo hicieron nuestros antepasados!
        - **Jarvald:** ¡Cuando se tratan de la manera correcta, los restos de las criaturas se pueden usar para fabricar excelentes armaduras dignas de batalla!
        - (otras|opciones-de-expedición)
      - [Choice]: ¿Puedo venir?
        - **Player:** ¿Puedo ir?
        - **Jarvald:** ¡Por supuesto, [Fremennik name]! ¡Su presencia es más que bienvenida en este sacrificio! ¿Quieres irte ahora?
        - [Menu]: Selecciona una opción
          - [Choice]: SI
            - (continuea|back-to-waterbirth)
          - [Choice]: NO
            - (continuea|decline-travel-waterbirth)
      - [Choice]: ¡Bonito sombrero!
        - **Player:** Oye, tengo que decir que el sombrero que llevas ahí luce muy bien.
        - **Jarvald:** ¡Sí, que es [Fremennik name]! ¡Skulgrimen lo creó para mí a partir del cadáver de uno de los monstruos de la isla Waterbirth después de nuestra última cacería! ¡Espero matar suficientes criaturas para crear algunas armaduras finas la próxima vez que nos vayamos!
        - (otras|opciones-de-expedición)
      - [Choice]: Vale, adiós.
        - (continuea|know-how-to-party)
  - [Choice]: nada
    - (continuea|nothing)

##### Viaje-Nacimiento en el agua

- (above|back-to-waterbirth)

#### En la isla Waterbirth


##### Hablar con

- **Jarvald:** ¡Ah, [Fremennik name]! Una batalla tan gloriosa te hace sentir feliz por la vida, ¿no es así?
- **Jarvald:** Entonces, ¿qué te parece, quedarte aquí para cazar o regresar a casa, al dulce Rellekka, para darte un festín y beber con tu tribu?
- (continuea|leave-waterbirth)

##### Viajes-Rellekka

- (above|back-to-rellekka)
