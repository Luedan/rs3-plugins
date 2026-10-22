# Rich Bunny

- **Original Wiki Page**: [Transcript:Rich Bunny](https://runescape.wiki/w/Transcript%3ARich%20Bunny)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- (Condition: Initially:)
  - **Rich Bunny:** ¡Bueno, hola, Player!
  - **Player:** ¿Cómo sabes mi nombre?
  - **Rich Bunny:** Oh, me he enterado de todos los aventureros que vienen a visitar nuestra maravillosa Madriguera. ¿Has venido a maravillarte con las maravillas de los barcos zanahoria?
  - **Player:** ¿Creo que sí?
  - (continue|Rich-Bunny-options)
- (Condition: Afterwards:)
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
    - ((Boat customisations interface opens with the following tooltips.))
      - (Condition: Locked customisations:)
        - ((Bronze:))
          - {{Interface tooltip|Bronze skin<br>{{Colour|#EB2F2F|This can be unlocked by completing a boat race in 2 minutes.}}}}
        - ((Silver:))
          - {{Interface tooltip|Silver skin<br>{{Colour|#EB2F2F|This can be unlocked by completing a boat race in 1 minute 45 seconds.}}}}
        - ((Gold:))
          - {{Interface tooltip|Gold skin<br>{{Colour|#EB2F2F|This can be unlocked by completing a boat race in 1 minute 30 seconds.}}}}
        - ((Ornament:))
          - {{Interface tooltip|Ornament decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
        - ((Bunting:))
          - {{Interface tooltip|Bunting decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
        - ((Flowers:))
          - {{Interface tooltip|Flowers decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
        - ((Eggs:))
          - {{Interface tooltip|Eggs decoration<br>{{Colour|#EB2F2F|This can be unlocked from The Grand Eggs-change.}}}}
      - (Condition: Unlocked customisations:)
        - ((Bronze:))
          - {{Interface tooltip|Bronze skin}}
        - ((Silver:))
          - {{Interface tooltip|Silver skin}}
        - ((Gold:))
          - {{Interface tooltip|Gold skin}}
        - ((Ornament:))
          - {{Interface tooltip|Ornament decoration}}
        - ((Bunting:))
          - {{Interface tooltip|Bunting decoration}}
        - ((Flowers:))
          - {{Interface tooltip|Flowers decoration}}
        - ((Eggs:))
          - {{Interface tooltip|Eggs decoration}}
  - [Choice]: Adiós.
    - **Player:** Me voy ahora.
    - **Rich Bunny:** Buenos días, Player.

### Customise boat

- (above|customise-boat)

### Blooming Burrow race

- ((The following are also shown as regular chat overhead messages:))
  - (Condition: Every minute before the race starts:)
    - {{Colour: {{Colour|#99FF99|The Blooming Burrow race is due to start in [1–5] [minutes/minute]!}}}}
  - (Condition: When the race is starting:)
    - {{Colour: {{Colour|#99FF99|Get ready in...}}}}
    - {{Colour: {{Colour|#99FF99|3...}}}}
    - {{Colour: {{Colour|#99FF99|2...}}}}
    - {{Colour: {{Colour|#99FF99|1...}}}}
    - {{Colour: {{Colour|#99FF99|GO!}}}}
