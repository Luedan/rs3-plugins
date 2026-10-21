# Sanfew

- **Original Wiki Page**: [Transcript:Sanfew](https://runescape.wiki/w/Transcript%3ASanfew)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Taverley


#### Antes del ritual druídico

- **Sanfew:** ¿Qué puedo hacer por ti young 'un?
- **Player:** Entonces... He oído que ustedes, los druidas, podrían enseñarme Herblore...
- **Sanfew:** Herblore ¿eh? Probablemente sea mejor que hables con Kaqemeex sobre eso; es el mejor profesor de herblore que tenemos actualmente. Creo que en este momento está en nuestro círculo de piedras justo al norte de aquí.
- **Sanfew:** Por supuesto que es el mejor maestro. No necesitas que te muestre cómo funciona. No como en mis tiempos. En aquel entonces, tenías que correr por todos lados antes de aprender a limpiar la suciedad de una hoja.
- **Sanfew:** Aún así, así son todos los niños hoy en día. No hay tiempo para detenerse y escuchar a un maestro. Con su 'armadura rúnica', sus 'mascadores fríos' y su música a todo volumen...
- **Player:** Eh... ¿gracias?

#### Después del ritual druídico

- **Sanfew:** ¿Qué puedo hacer por ti young 'un?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Tienes más trabajo para mí?
    - (Condition: Habiendo aún no completado Troll Stronghold:)
      - **Sanfew:** Todavía no, young 'un.
    - (Condition: Habiendo completado Troll Stronghold, pero por debajo del nivel 31 Herblore:)
      - **Sanfew:** Me temo que aún no has aprendido lo suficiente en el arte de Herblore para poder ayudarme, aventurero...
    - (Condition: Habiendo completado Troll Stronghold y con nivel 31 Herblore:)
      - (ver | La artimaña de Eadgar)
  - [Choice]: En realidad, no necesito hablar contigo.
    - **Sanfew:** Bueno, todos cometemos errores a veces.
    - Sanfew gruñe.

#### Después de la artimaña de Eadgar

- **Sanfew:** ¿Qué puedo hacer por ti young 'un?
- [Menu]: Selecciona una opción
  - [Choice]: cond=Without goutweed in backpack|¿Dijiste que necesitabas más hierba gotosa?
    - **Player:** ¿Dijiste que necesitabas más hierba gotosa?
    - **Sanfew:** No necesito más hierba gotosa para el ritual, pero todavía me resulta bastante difícil conseguirla. Si alguna vez te encuentras con alguno, tráemelo; Lo cambiaré por otras hierbas.
  - [Choice]: cond=With goutweed in backpack|Tengo más hierba gotosa para ti.
    - (removes=goutweed) (receives=random herbs)
    - **Player:** Tengo más hierba gotosa para ti.
    - **Sanfew:** Ah, bien. Aquí hay algunas hierbas a cambio.
  - [Choice]: ¿Tienes más trabajo para mí para ayudar a recuperar el círculo?
    - **Player:** ¿Tienes más trabajo para ayudarme a recuperar el círculo de piedras?
    - **Sanfew:** Bueno, ahora no, no creo que young 'un. De hecho, necesito hacer algunos preparativos para el ritual. Tenga la seguridad de que si necesito más ayuda se la volveré a pedir.
  - [Choice]: En realidad, no necesito hablar contigo.
    - (arriba)

#### Con finalización parcial de Zogre Flesh Eaters

- **Sanfew:** ¿Qué puedo hacer por ti young 'un?
- [Menu]: Selecciona una opción
  - [Choice]: Pregunta por el suero Sanfew.
    - **Player:** Hola, ¿puedes decirme algo sobre este suero Sanfew, por ejemplo, cómo lo preparo y para qué sirve?
    - **Sanfew:** Por supuesto. Después de todo, era mi creación y sólo mía. Si alguien debería saber cómo hacerlo, ¡debería ser yo!
    - **Player:** ¡No puedo criticar esa lógica!
    - **Sanfew:** Ok, esencialmente esta poción es una mezcla de un veneno curativo y estadísticas de restauración, ¡todo en uno! Muy útil para los aventureros que buscan conservar el espacio en el inventario.
    - **Player:** Ok, ya estoy vendido... ¿Cómo se hace?
    - **Sanfew:** Bueno, la verdad es que es muy fácil. Tomas una poción de restauración de súper estadísticas estándar. Agrega un poco de cuerno de unicornio molido. Luego, añade un poco de hierba de serpiente de la isla de Karamja. Por último, añade un poco de bestia de uñas nails. Sólo puedes obtenerlos del
    - **Sanfew:** área de Morytania, específicamente, si te adentras en el pantano de Mort Myre.
    - **Player:** ¿Qué quieres decir con lo de lo profundo del pantano de Mort Myre?
    - **Sanfew:** Bueno, la mayoría de los aventureros evitan el profundo pantano de Mort Myre, mientras que la caminata Paterdomus y la caminata Burgh de Rott te llevan a través de las áreas más interesantes. Estas áreas a menudo permiten el paso más rápido, pero potencialmente más peligroso.
    - **Sanfew:** rutas, por Mort Myre. Aquí es donde es probable que te encuentres con una bestia de clavos.
    - **Player:** ¿Son muy peligrosos?
    - **Sanfew:** Pueden ser bastante peligrosos. Se defenderán durante mucho tiempo y luego atacarán de repente y aparentemente sin previo aviso, lanzando tres feroces ataques a la vez. Esto puede ser bastante letal. Sin embargo, las bestias ungueales pueden resultar dañadas por
    - **Sanfew:** el suero Sanfew en sí... es muy extraño que una poción hecha con sus garras tenga un efecto tan pronunciado en ellos.
    - **Player:** Ok, eso es muy útil. Muchas gracias por tu ayuda.
  - [Choice]: Haga preguntas generales.
    - (Condition: Antes del ritual druídico:)
      - (arriba2|Antes del ritual druídico)
    - (Condition: Después del ritual druídico:)
      - (arriba2|Después del ritual druídico)
    - (Condition: Después de la artimaña de Eadgar:)
      - (arriba2|Después de la artimaña de Eadgar)
