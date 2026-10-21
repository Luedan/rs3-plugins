# Explorer Jack

- **Original Wiki Page**: [Transcript:Explorer Jack](https://runescape.wiki/w/Transcript%3AExplorer%20Jack)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Lumbridge


#### Antes de los Mitos de las Tierras Blancas

- **Explorer Jack:** Ahora, ¿tiene alguna pregunta sobre el sistema de tareas? O tal vez conozco una misión que podría interesarte.
- [Menu]: ¿Qué deseas decir?
  - [Choice]: Me gustaría preguntar sobre los logros y las recompensas de las tareas.
    - (below|Task System)
  - [Choice]: ¿Mencionaste una misión?
    - **Explorer Jack:** ¡Lo hice, lo hice! Entonces, ¿estás interesado? ¡Escupiendo! ¡Puedo ver la fibra exploradora en ti!
    - **Player:** Eh...
    - **Explorer Jack:** ¡Oh, esas llamas exploradoras en tus ojos! Como yo en mi juventud: ansioso por descubrir y asumir nuevos desafíos, ¿eh?
    - **Player:** Um... ¿entonces me vas a dar una misión?
    - **Explorer Jack:** ¿Una misión? ¡Pero efectivamente! Una historia de riquezas es lo que necesitas, ¿qué?
    - **Player:** ¿Lo es?
    - **Explorer Jack:** Sí, y tengo justo lo que necesitas. Un día, un diablillo de las nieves entró por mi puerta y yo, curioso por las tierras extranjeras, como debe ser todo buen explorador, le pedí historias de su tierra natal.
    - (ver|Mitos de las Tierras Blancas)
  - [Choice]: Nada.
    - (end)

#### Después de Mitos de las Tierras Blancas

- **Explorer Jack:** Entonces, ¿en qué puedo ayudarte?
- [Menu]: ¿Qué deseas decir?
  - [Choice]: Me gustaría preguntar sobre los logros y las recompensas de las tareas.
    - (below|Task System)
  - [Choice]: Sobre Mitos de las Tierras Blancas...
    - (continue|Post-quest dialogue)
  - [Choice]: Nada.
    - (end)

#### Sistema de tareas

- (Condition: Si el player ha completado las tareas para principiantes en el conjunto Lumbridge y Draynor y las recompensas no han sido reclamadas:)
  - **Player:** Creo que terminé todas las tareas para principiantes del conjunto Lumbridge.
  - **Explorer Jack:** ¿Tienes? ¡Ah, bien hecho! Todavía haremos de ti un explorador.
  - **Player:** Gracias. ¿Hay una recompensa?
  - **Explorer Jack:** Ah, sí, claro.
  - (receives=Explorer ring 1 and Antique lamp (Beginner Lumbridge Tasks))
  - **Explorer Jack:** Después de completar las tareas para principiantes, se te ha otorgado la posibilidad de usar el gesto Explorer para mostrárselo a tus amigos.
  - **Explorer Jack:** También te he regalado un anillo de explorador. Ahora, esto es más que cualquier anillo viejo. Además de verse bien, también tiene propiedades mágicas que le brindan un pequeño pero útil impulso a su Magic y Prayer.
  - **Explorer Jack:** Tu anillo tiene la capacidad de restaurar parte de tu energía de carrera.
  - **Explorer Jack:** Por cada una de las tres primeras secciones del diario que completes, tu anillo obtendrá una carga adicional, por lo que el anillo que recibas de las tareas de nivel medio tendrá 3 cargas, por ejemplo.
  - **Explorer Jack:** Si se agotan, el anillo se recarga con el sol cada día, por lo que podrás volver a usarlo mañana y así sucesivamente.
  - **Explorer Jack:** Como recompensa adicional, puedes tener esta antigua lámpara mágica para ayudarte con tus habilidades. Iba a usarlo yo mismo, pero realmente no lo necesito.
  - **Player:** Muchas gracias.
  - **Explorer Jack:** Si pierdes tu anillo, vuelve a verme y seguro que tendré otro. Ahora, ¿tenías algo más que preguntar?
  - (continue)
- (Condition: Si el player ha perdido su anillo de Explorador 1:)
  - **Explorer Jack:** ¡Qué carajo! ¿Cómo te va ese anillo?
  - **Player:** Lo perdí.
  - (receives=Explorer ring 1)
  - **Explorer Jack:** Lo perdiste, ¿eh? Bueno, tengo otro aquí que puedes tener. Intenta no perder este; No sirve que exploradores como nosotros vayamos perdiendo cosas, ¿qué?
  - (continue)
- {{anchor|cheevos}} [Menú]: Elija una opción:
  - [Choice]: Háblame del Sistema de Logros.
    - **Explorer Jack:** Bueno, el Sistema de Logros es un método para guiarte mientras exploras el mundo.
    - **Explorer Jack:** Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de mi parte.
    - **Explorer Jack:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
    - [Menu]: Elige una opción:
      - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
        - **Explorer Jack:** Por completar el conjunto Lumbridge y Draynor, se te presenta un anillo de explorador.
        - **Explorer Jack:** Este anillo será cada vez más útil con cada nivel de dificultad del conjunto que completes.
        - **Explorer Jack:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
        - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
        - (previous2|cheevos)
      - [Choice]: ¿Cómo reclamo estas recompensas?
        - **Player:** ¿Cómo reclamo estas recompensas?
        - **Explorer Jack:** Debes completar todas las tareas del conjunto de una dificultad particular y luego podrás reclamar tu recompensa. La mayoría de las tareas del conjunto Lumbridge son sencillas, aunque es posible que algunas requieran que se inicien, si no se terminan.
        - **Explorer Jack:** Para reclamar la recompensa del conjunto Lumbridge, habla con Bob en Bob's Axes en Lumbridge, Ned en Draynor Village o conmigo mismo.
        - (previous2|cheevos)
      - [Choice]: Lo siento, me estaba yendo.
        - (end)
  - [Choice]: ¿Puedo reclamar alguna recompensa de usted?
    - (below|Claim-rewards option)
  - [Choice]: cond=If you have completed any difficulty level of the Lumbridge set tasks:|¿Puedo comprar un repuesto de la recompensa?
    - [Menu]: Elige una opción:
      - [Choice]: Anillo del explorador 1
        - **Explorer Jack:** ¿Anillo 1 del explorador? Sí, pero me temo que te costaría 500 coins.
        - [Menu]: ¿Comprar otro por 500 coins?
          - [Choice]: si
            - [Te entregan el anillo de otro Explorador 1.]
            - (receives=Explorer's ring 1) (removes= 500 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Anillo del explorador 2
        - **Explorer Jack:** ¿Anillo del explorador 2? Sí, pero me temo que te costaría 1.000 coins.
        - [Menu]: ¿Comprar otro por 1.000 coins?
          - [Choice]: si
            - [Te entregan el anillo de otro Explorador 2.]
            - (receives=Explorer's ring 2) (removes= 1,000 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Anillo del explorador 3
        - **Explorer Jack:** ¿Anillo del explorador 3? Sí, pero me temo que te costaría 2000 coins.
        - [Menu]: ¿Comprar otro por 2000 coins?
          - [Choice]: si
            - [Te entregan el anillo de otro Explorador 3.]
            - (receives=Explorer's ring 3) (removes= 2,000 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Anillo del explorador 4
        - **Explorer Jack:** ¿Anillo del explorador 4? Sí, pero me temo que te costaría 10.000 coins.
        - [Menu]: ¿Comprar otro por 10.000 coins?
          - [Choice]: si
            - [Te entregan el anillo de otro Explorador 4.]
            - (receives=Explorer's ring 4) (removes= 10,000 coins)
          - [Choice]: No
            - **Player:** No, gracias.
  - [Choice]: Lo siento, me estaba yendo.
    - (end)

#### Reclamar recompensas

- (Condition: Sin recompensas para reclamar:)
  - **Explorer Jack:** Lo sentimos, no se te debe ninguna recompensa por logros en este momento. Mire su sistema de logros para saber qué hacer para ganar más.
- (Condition: Con recompensas para reclamar:)
  - **Explorer Jack:** Entonces llenaré tu inventario con lo que necesitas.
  - (receives=rewards)
  - (Condition: Sin suficiente espacio backpack:)
    - **Explorer Jack:** Ahí lo tienes. No tenías suficiente espacio para todo lo que te debían, así que me quedé con el resto.
  - (Condition: Con suficiente espacio backpack:)
    - **Explorer Jack:** Ahí lo tienes.

#### Intentando abrir la trampilla

- (ver|Trampilla (Explorer Jack))

#### Diálogo posterior a la misión


##### Antes de reclamar la recompensa en efectivo del estiércol de yeti

- **Explorer Jack:** Eh, no he avanzado nada con las piedras. Por favor vuelve más tarde.

##### Reclamar la recompensa en efectivo del estiércol de yeti, si el player no le dice a Explorer Jack la verdad

- **Explorer Jack:** Dejé que esas piedras se descongelaran, haciendo un descubrimiento muy maloliente.
- **Player:** Lo siento.
- **Explorer Jack:** ¿Lo sabías?
- **Player:** Lo hice. Cuando salí de la cueva con las 'piedras' me encontré con unos diablillos de nieve, que me contaron un secreto. Toda esta búsqueda fue una broma para ti, ya que te consideraron entrometido, codicioso y molesto. Estaba destinado a enseñarte una lección. No me dejaron mucha opción más que completar su plan.
- **Explorer Jack:** Jaja, ¡esa es buena, amigo! Supongo que lo merezco. Entrometido, jaja!
- **Player:** Me alegra ver que te lo estás tomando a la ligera.
- **Explorer Jack:** ¡Eh, tengo buenas noticias! Mientras no estabas, logré vendérselos a una bruja errante por una buena suma. Lo identificó como estiércol de yeti y dijo que era un ingrediente clave en algunas pociones antiguas muy avanzadas.
- **Player:** ¿En serio?
- **Explorer Jack:** ¡Sí, claro! He guardado parte del dinero para ti. Ahí tienes.
- (receives=5,000 coins)
- **Player:** ¡Gracias!

##### Después de reclamar la recompensa en efectivo del estiércol de yeti

- [Choice]: Sobre Mitos de las Tierras Blancas...
  - **Explorer Jack:** He estado en esa cueva de hielo que mencionó el diablillo de las nieves. ¡Deslizarse es muy divertido! Deberías volver allí alguna vez.
  - (Si el player ha descubierto algunas pero no todas las pinturas murales:)
    - **Explorer Jack:** ¡Ah, y hice un descubrimiento fascinante! en algunos lugares hay pinturas en las paredes que parecen haber sido realizadas por una civilización primitiva.
    - **Player:** Sé a quién te refieres. Así es como descubrí cómo derrotar al yeti. También encontré más en las otras habitaciones.
    - (Si no se han encontrado pinturas:)
      - **Explorer Jack:** ¡Ja, pero hay otros! Pude ver algo detrás de las raíces y esas cosas. Ve y echa un vistazo alguna vez.
    - (Si se han encontrado todas las pinturas menos una:)
      - **Explorer Jack:** Por lo que parece, hay uno que no has visto.

#### Diálogo histórico


##### Después del Lumbridge Rebuildathon

- **Explorer Jack:** ¡Estupendo! ¡Mira lo que han hecho Foreman George y su equipo de constructores! ¡Esta casa es perfecta!
- **Explorer Jack:** Sólo necesito una alfombra y algunas decoraciones y esos meses de dormir a la intemperie en las ruinas de mi casa se convertirán en un recuerdo lejano.
- ((Continúa con un diálogo regular.))

##### Durante el Lumbridge Rebuildathon

- **Explorer Jack:** Desde que comenzó la batalla entre Saradomin y Zamorak, ¡mi casa ha sido un completo desastre!
- **Explorer Jack:** Pero Foreman George y su equipo ahora están en el caso. No puedo esperar a ver qué le hacen.
- **Explorer Jack:** Una cosa es segura: ¡no puede ser peor que la ruina que me dejó la batalla!
- ((Continúa con un diálogo regular.))

##### Durante la batalla de Lumbridge y antes del Lumbridge Rebuildathon

- **Explorer Jack:** ¡Mi casa! Allí estaba yo, sentado en la sala de estar, tomando una buena taza de té y ocupándome de mis propios asuntos, y ¡BANG! ¡Mi casa se derrumba a mi alrededor!
- **Explorer Jack:** Fui a buscar, después de todo soy un explorador, y allí, justo afuera de mi casa, encontré a Saradomin y Zamorak peleando.
- **Explorer Jack:** Parece que su batalla tuvo un efecto bastante desafortunado en mis cimientos. Entonces, volví adentro y preparé otra taza de té.
- **Explorer Jack:** ¡Pensé para mis adentros que se necesitaría más que una batalla de destrucción mundial entre dos dioses gigantescos y todopoderosos para detenerme!
- **Explorer Jack:** Así que no dejaré que eso me deprima. ¡Todavía soy un capataz y tengo un trabajo que hacer!
- **Explorer Jack:** Me alegra ver que la batalla ya terminó. No estoy seguro de cómo se recuperará Zamorak de esa derrota.
- ((Continúa con un diálogo regular.))
