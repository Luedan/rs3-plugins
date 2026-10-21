# Rich Bunny

- **Original Wiki Page**: [Transcript:Rich Bunny](https://runescape.wiki/w/Transcript%3ARich%20Bunny)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- (Condition: Inicialmente:)
  - **Rich Bunny:** ¡Bueno, hola, Player!
  - **Player:** ¿Cómo sabes mi nombre?
  - **Rich Bunny:** Oh, me he enterado de todos los aventureros que vienen a visitar nuestra maravillosa Madriguera. ¿Has venido a maravillarte con las maravillas de los barcos zanahoria?
  - **Player:** ¿Creo que sí?
  - (continue|Rich-Bunny-options)
- (Condition: Después:)
  - **Rich Bunny:** ¡Buenos días, Player! ¿Vienes a dar una vuelta con mis botes de zanahoria?
  - (continue|Rich-Bunny-options)
- [Menu]: Seleccione una opción|ancla=Rich-Bunny-options
  - [Choice]: ¿Qué está pasando aquí?
    - **Player:** ¿Qué está pasando aquí?
    - **Rich Bunny:** He venido a visitar a mi querido hermano mayor durante la temporada de primavera y pensé que esta sería la oportunidad más fabulosa para probar mi última creación: ¡los botes de zanahorias!
    - **Rich Bunny:** El suelo ultranutritivo aquí permite iteraciones rápidas de nuevos modelos, y las franjas de aventureros de ojos tupidos son marineros de prueba maduros.
    - **Player:** Espera, ¿marineros de prueba? ¿Barcos hechos con vegetales podridos? No estoy seguro de estar de acuerdo con esto.
    - **Rich Bunny:** ¡Oh, Player! Realmente hay poco de qué preocuparse. Mi equipo ha realizado muchas pruebas rigurosas de durabilidad y seguridad al principio del desarrollo. ¡Nunca promocionaría nada que no usaría yo mismo!
    - **Player:** Muy bien, eso fue suficiente para convencerme. ¡Inscríbeme!
    - **Rich Bunny:** ¡Maravilloso!
    - (previous|Rich-Bunny-options)
  - [Choice]: Cuéntame más sobre la navegación.
    - **Player:** Entonces, ¿qué implica navegar?
    - **Rich Bunny:** Para empezar, mi equipo y yo nos hemos esforzado en colocar algunos obstáculos alrededor del lago. Hay aros, slaloms, rampas y halfpipes, en todos los cuales puedes entrenar a Agility.
    - **Rich Bunny:** ¡Pero eso no es todo! Cada 30 minutos, también podrás participar en la carrera Blooming Burrow. Empiezo a configurarlos a la hora y media, y las carreras comienzan correctamente cinco minutos más tarde.
    - (previous|Rich-Bunny-options)
  - [Choice]: ¿Qué puedo obtener a cambio?
    - **Player:** ¿Qué puedo obtener a cambio? Preferiría no ser un conejito de laboratorio en uno de tus carros zanahoria gratis.
    - **Rich Bunny:** ¡Oh, querido Player! ¡Nunca te pediría mano de obra gratis!
    - **Rich Bunny:** Además de la experiencia Agility, personalmente me aseguraré de que te paguen en fichas de primavera por tus esfuerzos.
    - **Rich Bunny:** También he encargado algunos títulos únicos de oro, plata y bronce, y diseños para tu bote zanahoria, en caso de que termines una regata a tiempo.
    - (previous|Rich-Bunny-options)
  - [Choice]: ¿Puedo personalizar mi barco?
    - **Player:** ¿Puedo personalizar mi barco?
    - **Rich Bunny:** ¡Por supuesto! Puedes ser el navegante de zanahorias más elegante que existe con mis decoraciones para barcos hechas a medida.
    - ((La interfaz de personalización del barco se abre con la siguiente información sobre herramientas.))
      - (Condition: Personalizaciones bloqueadas:)
        - ((Bronce:))
          - {{Interface tooltip|Bronze skin<br>{{Colour|#EB2F2F|This can be unlocked by completing a boat race in 2 minutes.}}}}
        - ((Plata:))
          - {{Interface tooltip|Silver skin<br>{{Colour|#EB2F2F|This can be unlocked by completing a boat race in 1 minute 45 seconds.}}}}
        - ((Oro:))
          - {{Interface tooltip|Gold skin<br>{{Colour|#EB2F2F|This can be unlocked by completing a boat race in 1 minute 30 seconds.}}}}
        - ((Adorno:))
          - {{Interface tooltip|Ornament decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
        - ((Empavesado:))
          - {{Interface tooltip|Bunting decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
        - ((Flores:))
          - {{Interface tooltip|Flowers decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
        - ((Huevos:))
          - {{Interface tooltip|Eggs decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
      - (Condition: Personalizaciones desbloqueadas:)
        - ((Bronce:))
          - {{Interface tooltip|Bronze skin}}
        - ((Plata:))
          - {{Interface tooltip|Silver skin}}
        - ((Oro:))
          - {{Interface tooltip|Gold skin}}
        - ((Adorno:))
          - {{Interface tooltip|Ornament decoration}}
        - ((Empavesado:))
          - {{Interface tooltip|Bunting decoration}}
        - ((Flores:))
          - {{Interface tooltip|Flowers decoration}}
        - ((Huevos:))
          - {{Interface tooltip|Eggs decoration}}
  - [Choice]: Adiós.
    - **Player:** Me voy ahora.
    - **Rich Bunny:** Buenos días, Player.

### Customise boat

- (above|customise-boat)

### Blooming Burrow race

- ((Los siguientes también se muestran como mensajes generales de chat habituales:))
  - (Condition: Cada minuto antes del inicio de la carrera:)
    - {{Colour: {{Colour|#99FF99|The Blooming Burrow race is due to start in [1–5] [minutes/minute]!}}}}
  - (Condition: Cuando comienza la carrera:)
    - {{Colour: {{Colour|#99FF99|Get ready in...}}}}
    - {{Colour: {{Colour|#99FF99|3...}}}}
    - {{Colour: {{Colour|#99FF99|2...}}}}
    - {{Colour: {{Colour|#99FF99|1...}}}}
    - {{Colour: {{Colour|#99FF99|GO!}}}}
