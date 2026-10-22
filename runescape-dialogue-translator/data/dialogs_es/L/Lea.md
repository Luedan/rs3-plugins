# Lea

- **Original Wiki Page**: [Transcript:Lea](https://runescape.wiki/w/Transcript%3ALea)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Sólo la primera vez

- **Player:** Hola, creo que no te había visto por aquí antes.
- El extraño te mira de arriba abajo.
- **Lea:** No. No lo has hecho.
- **Player:** Bueno, ¿qué te trae a esta parte del mundo?
- **Lea:** Estoy esperando a un individuo con algún talento de creación.
- **Player:** He hecho algunas cosas en mi tiempo, tal vez pueda ser de alguna ayuda.
- (Condition: Without 22 Invention:)
  - **Lea:** No. No, no podrías.
  - **Lea:** Al menos no todavía.
  - [Necesitas 22 Invention para ayudar.]
- **Lea:** Mmmm. Por lo que he visto de ti por aquí creo que podrías ser de alguna utilidad.
- **Player:** Excelente, siempre me gusta ayudar...
- **Player:** Espera. ¿Qué quieres decir con que me has visto? No te he visto en ningún otro lugar excepto aquí.
- **Lea:** Ven ahora. La vista no es necesariamente una relación simétrica. Ahora volvamos al asunto que nos ocupa.
- **Lea:** Conozco tus talentos, perfeccionados en la cueva detrás de mí y estaría dispuesto a encargarte algún trabajo.
- **Player:** Oh, eso podría ser un poco problemático, ya que mis inventos se agotan...
- **Lea:** Sí, sí, quemar los recuerdos desgarrados de un dios muerto para tus propios fines.
- **Lea:** Qué ingenioso y ético de tu parte.
- **Lea:** Un evento, que algunos dirían, fue culpa tuya.
- **Player:** ¡Eso no es lo que pasó!
- **Player:** Intenté guardarlos.
- **Player:** ...
- **Player:** Fallé.
- **Lea:** No importa, el resultado fue el mismo.
- **Lea:** De todos modos, mi poder sobre tales elementos no es de tu incumbencia.
- **Player:** Si tú lo dices...
- **Player:** Entonces, ¿qué buscas?
- **Lea:** Bueno, encuentro que cuando dejo caer coins en mi bolsa de monedas hace bastante ruido.
- [El desconocido agita su monedero a modo de ejemplo.]
- **Lea:** Me gustaría que fuera más silencioso.
- **Player:** Tengo algunas ideas sobre cómo hacerlo...
- **Player:** ...y para qué más podría ser útil...
- **Lea:** Excelente. Espero ansiosamente su regreso con el artículo solicitado.

#### Durante la tarea de robar bolsas

- **Lea:** Nos volvemos a encontrar, ¿tienes el bolso para mí?
- (Condition: Without a pickpocketing bag:)
  - **Player:** Bueno, no, todavía no.
  - **Lea:** Entonces no me molestes hasta que tengas un bolso nuevo. Nada especial, un bolso básico es todo lo que te pido.
- (Condition: With a pickpocketing bag:)
  - **Player:** De hecho, sí.
  - **Lea:** Excelente.
  - (Condition: If the pickpocketing bag has been worn:)
    - [Le ofreces la bolsa.]
    - **Lea:** No me interesan artículos de segunda mano. Quiero un bolso nuevo, nada más y nada menos.
    - **Player:** Bien. Iré a buscar uno nuevo.
  - (removes=pickpocketing bag)
  - [Le entregas la bolsa.]
  - **Lea:** ...
  - **Player:** ...
  - **Player:** ... ... ...
  - **Player:** ¿Y bien?
  - **Lea:** ¿Y bien qué?
  - **Player:** Ya tienes tu nuevo monedero...
  - **Lea:** Sí.
  - **Player:** ¿Y pareces contento con ello?
  - **Lea:** Mucho.
  - **Player:** Entonces esta es la parte en la que me pagas.
  - **Lea:** Dios mío. Lamentablemente parece que has olvidado algo.
  - **Player:** ¿Qué?
  - **Lea:** Acordar los términos de nuestro acuerdo antes de entregar el bolso. Nunca acepté darte nada por el bolso.
  - **Lea:** Simplemente dije que estaría dispuesto a encargarte el trabajo, aparentemente asumiste la tarea como un gesto caritativo. Por lo cual estoy muy agradecido.
  - **Player:** Eso es... Pero yo...
  - **Player:** ¿Por qué eres astuto...?
  - **Lea:** Oh, vamos, no es como si no hubieras obtenido nada de tu trabajo. Considérame tu musa. Ahora tienes la experiencia para hacer más bolsas de esas para tu propia colección de monedas.
  - **Player:** Supongo que entendí algo de todo esto...
  - **Lea:** Muy bien. Ahora que el asunto está resuelto, me gustaría proponerle otra solicitud, si usted lo desea.
  - **Player:** Supongamos que lo fuera, ¿qué buscarías tú? Y lo más importante, ¿qué me darías a cambio?
  - (Condition: Without 82 Invention:)
    - **Lea:** No creo que seas de más ayuda en este momento. Necesito alguien con habilidades más refinadas que las que puedes ofrecer actualmente.
    - [Necesitas 82 Invention para seguir ayudando.]
  - **Lea:** Ya que preguntaste, me interesaría algo para canalizar energías mágicas.
  - **Player:** ¿Como una varita mágica? Estoy seguro de que podría hacer uno con bastante facilidad.
  - **Lea:** No, no. No canalizar las energías mágicas hacia afuera, sino hacia adentro. Para capturarlo y atarlo.
  - **Player:** Entonces, ¿para crear runas? ¿Algún tipo de varita inversa?
  - **Lea:** En pocas palabras. Sí.
  - (Condition: If the player hasn't researched the binding rod:)
    - **Player:** He anotado algunas ideas sobre cómo abordar un problema similar por mí mismo.
    - (continue)
  - (Condition: If the player has already researched the binding rod:)
    - **Player:** Ya sé cómo hacer una herramienta como esa, la llamo 'Varilla vinculante'.
    - (continue)
  - **Lea:** Estoy al tanto de tus avances pero me interesaría algo menos...
  - **Lea:** ...básico.
  - **Player:** No, por supuesto que no. Una herramienta nueva, nunca antes vista, no es suficiente para usted.
  - **Lea:** Precisamente. No es mi culpa que tenga estándares.
  - **Player:** Entonces dime: ¿qué haría que esto fuera menos básico?
  - **Lea:** ¿Estás familiarizado con los elfos del oeste?
  - (Condition: If the player hasn't completed Plague's End or Extinction:)
    - {{Transcript missing}}
  - (Condition: If the player has completed Plague's End but not The Light Within:)
    - **Player:** Sí, de hecho, los he ayudado mucho y se me ha concedido acceso a su ciudad de Prifddinas.
    - **Lea:** Todo un aventurero con amigos en las altas esferas. Entonces, en respuesta a mi pregunta: sí.
    - (continue)
  - (Condition: If the player has competed The Light Within but not Extinction:)
    - **Player:** Sí, de hecho, los he ayudado mucho y no solo se me ha concedido acceso a su ciudad de Prifddinas, sino que también les he ayudado a recuperar a su dios Seren.
    - **Lea:** Todo un viajero. Entonces, en respuesta a mi pregunta: sí.
    - (continue)
  - (Condition: If the player has completed both The Light Within and Extinction:)
    - **Player:** ¡Sí, muchísimo!
    - **Player:** Encontré un camino debajo de la montaña, resolví muchos de sus problemas y obtuve acceso a su ciudad de Prifddinas.
    - **Player:** Luego ayudó a traer de vuelta a su dios Seren. Visitó su mundo natal. Conocí a la madre de Seren y a su...
    - **Player:** ...tías y primas, más o menos... Supongo...
    - **Player:** Antes de dejar lo que quedaba de todos ellos en un mundo que intenté salvar.
    - **Player:** Un mundo muerto que no pude salvar. Pero no había nada más que pudiera hacer; lo intenté...
    - **Lea:** Bastante. Y tiene mi agradecimiento por esos esfuerzos.
    - (continue)
  - **Lea:** Tienen acceso a un cristal muy versátil, que puede funcionar como todo, desde extremidades de arco hasta escudos.
  - **Lea:** Y como varitas.
  - **Player:** Interesante... Me pregunto si...
  - **Lea:** Precisamente mi opinión, así que si considerarías traerme uno hecho con este cristal te lo agradecería mucho.
  - **Player:** Hmmm... sí... Podría...
  - **Player:** Espera un momento. Antes de hacerlo, debemos acordar el pago de esta herramienta.
  - **Lea:** De hecho. Es bueno ver que aprendiste algo de la última vez. Entonces, ¿qué me pedirías?
  - **Player:** Errm, no estoy seguro. Por lo general, la gente me ofrece cosas al azar que tienen a mano, como lámparas viejas, libros o llaveros.
  - **Lea:** Cosas raras para hacer favores. Me temo que no tengo lámparas de aceite encima. Creo que tengo un libro sobre mí si te interesa.
  - **Player:** Sí, eso servirá. Un nuevo artilugio de cristal a cambio de un libro. ¿Trato?
  - **Lea:** Oferta. Espero ansiosamente su regreso con el artículo.

#### Nuevamente antes de recibir la tarea de la varilla de unión de cristal.

- **Lea:** Como decía. Ahora que el asunto está resuelto, me gustaría proponerle otra solicitud, si usted lo desea.
- (above|Suppose)

#### Durante la tarea de la varilla de unión de cristal

- **Lea:** Me alegro de verte por aquí. ¿Tienes el artículo que acordamos?
- (Condition: Without a crystal binding rod:)
  - **Player:** Bueno, no, todavía no.
  - **Lea:** Entonces no me molestes hasta que tengas la caña nueva. Realizado con cristal según lo solicitado.
- (Condition: With a crystal binding rod:)
  - **Player:** De hecho, sí.
  - **Lea:** Excelente.
  - (removes=crystal binding rod)
  - [Cambias la varilla de encuadernación de cristal por el libro.]
  - **Lea:** Excelente. Esto debería funcionar bien.
  - **Lea:** Disfruta de tu nuevo libro. Adiós hasta la próxima vez que nos encontremos.
  - (Action: Lea se teletransporta.)
  - **Player:** Qué persona más extraña.
  - **Player:** Pero ahora tengo este libro.
  - ((In the following the images are only shown with full-screen dialogue boxes toggled off:))
    - [Abres el libro. El libro está vacío salvo una sola frase en la primera página.]
    - ["Tanto en los negocios como en la vida, vale la pena ser específico".]
    - [El libro se convierte en polvo.]
    - (continue)
  - ¡Felicitaciones! Has completado: 'El regalo más grande de todos': aprende una lección de Lea fuera del gremio Invention.
