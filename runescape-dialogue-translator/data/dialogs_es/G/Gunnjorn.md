# Gunnjorn

- **Original Wiki Page**: [Transcript:Gunnjorn](https://runescape.wiki/w/Transcript%3AGunnjorn)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talking to Gunnjorn at the Barbarian Agility course

- [Menu]: ¿Qué quieres decir?
  - [Choice]: Hola. ¿Qué es este lugar?
    - **Player:** Hola. ¿Qué es este lugar?
    - **Gunnjorn:** ¡Ajá! Bienvenidos a mi carrera de obstáculos. Diviértete, pero recuerda que esto no es un parque infantil. Aquí ha muerto gente.
    - **Gunnjorn:** Este curso comienza en los columpios hacia el este. Cuando hayas hecho el swing, cruza el tronco resbaladizo hacia el edificio. Cuando hayas atravesado los obstáculos del interior, saldrás por el otro lado. Desde allí, cruza la zona baja.
    - **Gunnjorn:** paredes por terminar. Si has superado todos los obstáculos como te he descrito y en orden, obtendrás una bonificación por vuelta.
  - [Choice]: ¿Qué le pasa a la pared después del equilibrio del tronco?
    - **Player:** ¿Qué le pasa a la pared después del equilibrio del tronco?
    - **Gunnjorn:** ¿El muro después del equilibrio del tronco? Nada, de verdad. Simplemente le puse un material resistente, dándole a la gente algo a lo que agarrarse.
    - **Player:** ¿Por qué harías eso?
    - (Condition: With at least 90 Agility:)
      - **Gunnjorn:** Para que personas como tú puedan tener una ruta más difícil en este campo.
      - **Gunnjorn:** Un compañero y yo nos reunimos y planteamos un nuevo desafío que solo los verdaderamente ágiles podrán conquistar.
      - **Gunnjorn:** Las cosas extra comienzan en esa pared; Entonces, si crees que estás preparado para ello, te sugiero que subas allí después del saldo del registro.
      - **Player:** Suena interesante. ¿Algo más que deba saber?
      - **Gunnjorn:** Nada, en realidad. Solo asegúrate de completar los otros obstáculos antes de hacerlo. Si terminas una vuelta completa, obtendrás una bonificación mayor por realizar la ruta más difícil.
      - **Gunnjorn:** Si logras hacer 250 vueltas de esta ruta avanzada sin un solo error, te dejaré un artículo especial. Mantendré un registro de tus vueltas, para que puedas comprobar cómo te va conmigo en cualquier momento.
    - (Condition: Without at least 90 Agility:)
      - **Gunnjorn:** Entonces, los jugadores que son realmente ágiles pueden tener una ruta más desafiante. Le sugiero que siga la ruta normal por ahora y regrese cuando tenga más experiencia.
      - Necesita un nivel Agility de 90 o más para intentar el curso mejorado de Gunnjorn.
    - (continue)
- (Condition: If the advanced course has been discussed and completed at least once:)
  - [Choice]: ¿Puedo hablar de recompensas?
    - **Player:** ¿Puedo hablar sobre recompensas?
    - (Condition: If the player has not completed 250 perfect laps of the advanced barbarian agility course:)
      - **Gunnjorn:** Aún no hay recompensa para ti. Tu recuento de vueltas es solo [0-249]. Son 250 vueltas exitosas o ninguna recompensa.
    - (Condition: If the player has completed 250 perfect laps of the advanced barbarian agility course:)
    - ¡Has completado 250 vueltas perfectas! Habla con Gunnjorn para cobrar tu recompensa.
      - (Condition: First time:)
        - **Gunnjorn:** ¡Claro, y felicidades, Player! Fue necesaria dedicación y gran destreza para completar tantas vueltas.
        - **Gunnjorn:** Como prometí, te daré un artículo que puede resultarte útil: un top Agile. Te sentirás más ligero de lo habitual mientras lo uses.
        - **Gunnjorn:** Nosotros, los bárbaros, somos gente dura, como sabes, por lo que incluso te mantendrá a salvo si te involucras en el combate.
        - (receives=Agile top)
        - **Gunnjorn:** Ahí lo tienes. ¡Disfrutar!
      - (Condition: Afterwards:)
        - **Gunnjorn:** Por supuesto. ¿Cómo puedo ayudar?
        - **Player:** ¿Alguna posibilidad de otro top Agile?
        - (receives=Agile top)
        - **Gunnjorn:** Aquí tienes.
  - [Choice]: Eso es todo lo que necesito por ahora. Adiós.
    - **Player:** Eso es todo lo que necesito por ahora. Adiós.
    - **Gunnjorn:** Adiós por ahora. Vuelve si necesitas ayuda.
