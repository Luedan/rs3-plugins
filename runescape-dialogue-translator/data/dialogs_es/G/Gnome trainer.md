# Gnome trainer

- **Original Wiki Page**: [Transcript:Gnome trainer](https://runescape.wiki/w/Transcript%3AGnome%20trainer)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Tree Gnome Stronghold


#### Diálogo estándar

- {{trandom}}
  - [Choice]: Diálogo 1
    - **Gnome trainer:** Esto es entrenamiento, soldado. ¡Poco tiempo para charlar! ¿Qué deseas?
    - (continue)
  - [Choice]: Diálogo 2
    - **Gnome trainer:** Esta es un área de entrenamiento seria. ¿Qué deseas?
    - (continue)
  - [Choice]: Diálogo 3
    - **Gnome trainer:** Esta no es una fiesta de té de abuelas. ¿Qué deseas?
    - (continue)
- [Menu]: ¿Qué quieres decir?
  - [Choice]: ¿Qué es este lugar?
    - **Player:** ¿Qué es este lugar?
    - **Gnome trainer:** Aquí, amigo mío, es donde entrenamos y mejoramos nuestro Agility. Es una habilidad esencial.
    - **Player:** Parece bastante fácil.
    - **Gnome trainer:** Si completas el recorrido, desde el tronco resbaladizo hasta el final, tu Agility aumentará más rápidamente que repitiendo solo un obstáculo.
  - [Choice]: Entonces, ¿qué tiene de especial este curso?
    - **Player:** Entonces, ¿qué tiene de especial este curso?
    - **Gnome trainer:** Bueno, es donde la mayoría de la gente tiende a empezar a entrenar. También hemos creado una extensión para aquellos que estén dispuestos a aceptar el desafío.
    - **Player:** ¿Una extensión?
    - (Condition: If the player's Agility level is at least 85:)
      - **Gnome trainer:** Bueno, parece que puedes manejarlo, así que te informaré.
      - **Gnome trainer:** Si sigues el recorrido normalmente, verás una nueva rama antes de la cuerda de equilibrio. Este es el camino hasta la nueva ruta.
      - **Gnome trainer:** Te ha llevado un tiempo fortalecer la rama, pero deberías encontrarte lo suficientemente ágil para pasar al siguiente nivel. Te sugiero que lo compruebes.
      - **Player:** Podría hacer eso. ¿Algo más que necesito saber?
      - **Gnome trainer:** Sí. Si sigues la ruta más difícil, obtendrás una bonificación de experiencia mucho mayor al final. ¡Solo asegúrate de haber completado todos los obstáculos que conducen a la rama!
      - **Gnome trainer:** Oh, casi lo olvido: si logras hacer 250 vueltas de la ruta avanzada sin fallar, te daremos un artículo especial. Mantendremos un recuento de tus vueltas, para que siempre puedas comprobar tu progreso.
    - (Condition: If the player's Agility level is below 85:)
      - **Gnome trainer:** Es un desafío que creo que está un poco fuera de tu alcance. Te daré más información cuando tengas un poco más de experiencia.
      - Necesitas un nivel Agility de 85 para intentar el curso mejorado de gnomos.
  - [Choice]: cond=If at least one lap of the Advanced Gnome Stronghold Course has been completed:|¿Puedo hablar de recompensas?
    - **Player:** ¿Puedo hablar sobre recompensas?
    - (Condition: If the player has claimed the Agile legs:)
      - **Gnome trainer:** Por supuesto. ¿Cómo puedo ayudar?
      - **Player:** ¿Alguna posibilidad de tener más piernas ágiles?
      - (receives=agile legs)
      - **Gnome trainer:** Aquí tienes, intenta no perderlos.
    - (Condition: If the player has not yet claimed the Agile legs:)
      - (Condition: If the player has completed 250 perfect advanced route laps:)
        - **Gnome trainer:** Bueno, ¡parece que has completado nuestro desafío!
        - **Gnome trainer:** Llévate esto como recompensa: unas piernas ágiles. Te sentirás mucho más ligero de lo habitual mientras los uses.
        - **Gnome trainer:** Están hechos del material más resistente que los gnomos pudimos encontrar, por lo que incluso podrían protegerte en combate.
        - (receives=agile legs)
        - **Gnome trainer:** Ahí lo tienes. ¡Disfrutar!
      - (Condition: If the player has not completed 250 perfect advanced route laps yet:)
        - **Gnome trainer:** Bueno, todavía tienes trabajo por hacer. Tu recuento de vueltas es *<number of laps completed>*. ¡Son 250 vueltas exitosas para la recompensa!
  - [Choice]: Ya terminé por ahora.
    - **Player:** Ya terminé por ahora. Adiós.
    - **Gnome trainer:** Adiós por ahora. Vuelve si necesitas ayuda.

#### En la ruta avanzada

- **Gnome trainer:** Vaya, es agradable ver a personas con experiencia llevarlo al siguiente nivel de formación.
- **Player:** Gracias. ¿Entonces esta es la ruta avanzada de la que hablan los otros gnomos?
- **Gnome trainer:** Seguro que lo es. Ya has subido hasta aquí, ahora todo lo que necesitas hacer es cruzar este cartel aquí.
- **Player:** ¿En serio?
- **Gnome trainer:** Oh, sí, totalmente. Cuando hayas cruzado, busca los columpios para llegar a la sección norte. Cuando aterrices desde ellos, intenta saltar las ramas hacia la tubería y deberías deslizarte hasta la línea de meta.
- **Player:** ¿Y seguiré teniendo mis piernas intactas cuando haya hecho todo esto?
- **Gnome trainer:** Sí. Por supuesto.

#### Senderos del tesoro


##### Recibiendo la caja del rompecabezas

- **Gnome trainer:** ¡Aún no has terminado! ¡Haz esto por mí!
- (receives=puzzle box)
- [¡El gnome trainer te ha regalado una caja de rompecabezas!]

##### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- **Gnome trainer:** ¡Mi hermanita puede hacer rompecabezas mejor que eso!

##### Cuando se volvió a hablar con él después de resolver el rompecabezas

- (Condition: If the trail continues:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [¡El gnome trainer te ha dado otro pergamino de pistas!]
  - (continue)
- (Condition: If the trail ends:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Gnome trainer:** ¡Bien hecho!

#### Diálogo aéreo


##### Caminando por el saldo del registro

- **Gnome trainer:** {{RSChat|Okay get over that log, quick quick!}}

##### Saltando la primera red de obstáculos

- **Gnome trainer:** {{RSChat|Move it, move it, move it!}}

##### Subiendo a la rama del árbol

- **Gnome trainer:** {{RSChat|That's it - straight up}}

##### Caminando sobre la cuerda de equilibrio

- **Gnome trainer:** {{RSChat|Come on scaredy cat, get across that rope!}}

##### Subiendo por encima de la segunda red de obstáculos

- **Gnome trainer:** {{RSChat|My Granny can move faster than you.}}

##### Subiendo al árbol que conduce a la ruta avanzada.

- **Gnome trainer:** {{RSChat|Terrorbirds could climb faster than that!}}

##### Corriendo a través del cartel

- **Gnome trainer:** {{RSChat|Come on! I'd be over there by now.}}
