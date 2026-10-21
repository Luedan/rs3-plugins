# Charming imp

- **Original Wiki Page**: [Transcript:Charming imp](https://runescape.wiki/w/Transcript%3ACharming%20imp)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

*Comienza con una de las siguientes líneas:*
- **Charming imp:** ¡Hola Player! Siempre es un honor pasar tiempo contigo. ¿Le puedo ayudar en algo?
- **Charming imp:** Es un placer verte, Player. ¿Le puedo ayudar en algo?
- **Charming imp:** ¡Hoy te ves absolutamente radiante! ¿Le puedo ayudar en algo?
- **Charming imp:** ¡Verte, Player, siempre me alegra el día! ¿Le puedo ayudar en algo?
*Continúa con:*
- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Charming imp:** Soy un charming imp. ¡Es encantador verte! Tengo muchas ganas de trabajar con alguien tan talentoso como tú.
    - [Menu]: Selecciona una opción
      - [Choice]: ¡Es un placer conocerte también!
        - **Charming imp:** Entonces ambos ya estamos teniendo un buen día. Entonces, ¿cómo puedo ayudarte?
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Qué haces?
            - (below|role)
          - [Choice]: No necesito nada ahora.
            - (below|bye)
      - [Choice]: ¿Qué haces?
        - (below|role)
      - [Choice]: Tengo que irme ahora.
        - (below|bye)
  - [Choice]: ¿Qué haces? {{anchor|imp-role}}
    - **Charming imp:** Como todos los diablillos encantadores, soy un coleccionista... mejor dicho, un conocedor de los encantos. Podría contarte todo tipo de historias y hechos fascinantes sobre los amuletos... ¡Ah, mis disculpas! Puedo dejarme llevar un poco hablando de encantos, ¡y aún quedan aventuras por vivir! Sin embargo, a medida que usted cumple con sus deberes, ¡puedo ayudarlo y usted puede ayudarme! Si matas a alguna bestia vil que suelta un amuleto, lo traeré directamente a tu backpack. Sin embargo, no puedo recogerlos por ti si no tienes dónde guardarlos, así que asegúrate de que haya espacio en tu backpack.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué hay para ti? {{anchor|imp-goal}}
        - **Charming imp:** ¡Me encantan los dijes! Es un placer poder tenerlos en mis manos por un tiempo. Sólo experimentarlos... ya sabes, sostenerlos, catalogarlos, contarlos, sentarme en baños llenos de ellos... esa es suficiente recompensa para mí.
        - **Player:** Um... ¿Baños?
        - **Charming imp:** ¡Sí, por supuesto baños! De todos modos, si me dejas quedarme con algunos, bueno, ¡mi día estaría completo! Si me dejas quedarme con alguno, también te impartiré un poco de mis conocimientos sobre invocación para cada uno. ¿Hay algo más que necesites?
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Qué amuletos conservas?
            - (below|keep-charms)
          - [Choice]: ¿Puedes contarme más sobre los amuletos?
            - (below|about-charms)
          - [Choice]: ¿No es estrecho en mi backpack?
            - (below|backpack)
          - [Choice]: ¡Eso suena genial! ¡Gracias!
            - (below|thanks)
      - [Choice]: ¿Conservas alguno de los amuletos? {{anchor|keep-charms}}
        - **Charming imp:** Tomo los que no quieras. Confío en tu criterio.
        - (opens=Charming imp)
      - [Choice]: ¿Puedes contarme más sobre los amuletos? {{anchor|about-charms}}
        - **Charming imp:** Los amuletos son la esencia de un ser vivo; podrías considerarlos como parte del alma de una criatura. Sin el vínculo con una criatura de este plano, sería imposible convocar una criatura espiritual aquí. Pero para mí son más que simples fichas utilizadas para invocar. ¡Son un apasionante mundo de coleccionismo! Sin embargo, es muy difícil expresar la alegría de los amuletos a alguien que no es coleccionista.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Qué hay para ti?
            - (above|imp-goal)
          - [Choice]: ¿Conservas alguno de los amuletos?
            - (above|keep-charms)
          - [Choice]: ¿No es estrecho en mi backpack?
            - (below|backpack)
          - [Choice]: ¡Correcto! Bueno, tengo que irme ahora.
            - (below|bye)
      - [Choice]: ¿No está apretado en mi backpack? {{anchor|backpack}}
        - **Charming imp:** ¡Es mejor que estar afuera! Realmente no me gustan los espacios abiertos. Además, puedo estar cerca de los amuletos que colecciono de esta manera. Ah, y no olvides que si no hay espacio en tu backpack, ¡no podré coleccionar ningún charm! ¿Hay algo más que necesites?
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Qué hay para ti?
            - (above|imp-goal)
          - [Choice]: ¿Conservas alguno de los amuletos?
            - (above|keep-charms)
          - [Choice]: ¿Puedes contarme más sobre los amuletos?
            - (above|about-charms)
          - [Choice]: ¡Correcto! Bueno, tengo que irme ahora.
            - (below|bye)
      - [Choice]: Eso suena genial. ¡Gracias! {{anchor|thanks}}
        - **Charming imp:** ¡Siempre es un placer!
  - [Choice]: No necesito nada ahora {{anchor|bye}}
    - **Charming imp:** ¡Espero que tengas un buen día! ¡Adiós!

### Attempting to add to tool belt

- ((Si el player no ha aprendido a hacerlo desde un slayer master:))
  - Un slayer master le debe enseñar cómo agregar esto a su cinturón de herramientas.
  - (ventana emergente)
    - {{Popup|You need to be taught how to add this to your tool belt by a slayer master.|warning=yes}}
  - (end)
- ((Lo siguiente se muestra en una interfaz titulada 'AÑADIR AL CINTURÓN DE HERRAMIENTAS':))
  - ¿Está seguro de que desea agregar esto a su cinturón de herramientas?<br><br>No podrá reclamarlo.
    - [Choice]: CANCELAR
      - (end)
    - [Choice]: bien
      - (removes=the charming imp)
      - Agrega el charming imp a su cinturón de herramientas. Puede configurarlo a través del cinturón de herramientas.
      - (ventana emergente)
        - {{Popup|You add the charming imp to your tool belt. You can configure it via the tool belt.|colour=#ebe0bc}}

### Attempting to destroy

- **Charming imp:** ¡No me eches! Tengo miedo del gran mundo que hay ahí fuera.
- **¿Estás seguro de que quieres destruir este objeto?** Si te deshaces del charming imp, no hay forma de recuperarlo excepto comprándolo nuevamente con 100,000 tokens Dungeoneering.
  - [Choice]: si
    - **Charming imp:** ¡Pensé que éramos un equipo!
  - [Choice]: No
    - **Charming imp:** ¡Por favor, no vuelvas a asustarme así!

### Consuming a charm

- El charming imp encuentra el siguiente charm[s] y te enseña cómo invocar: Charm [número]x [Type].  <!-- filtered -->

### Collecting a charm

- El charming imp encuentra el siguiente charm[s] y coloca [it/them] en su backpack: [número]x [Type] charm. <!-- filtered -->
Categoría: Transcripciones de artículos
