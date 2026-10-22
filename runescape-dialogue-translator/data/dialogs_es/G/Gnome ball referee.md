# Gnome ball referee

- **Original Wiki Page**: [Transcript:Gnome ball referee](https://runescape.wiki/w/Transcript%3AGnome%20ball%20referee)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### First-time dialogue

- **Player:** Hola.
- **Gnome ball referee:** Hola, bienvenido a Gnomeball. En realidad, es bastante simple: me quitas el balón, cargas contra la defensa de los gnomos e intentas lanzar el balón a través de la red usando tu habilidad a distancia. Es un juego duro pero muy divertido. También es excelente para mejorar la agilidad. ¿Te apetece un juego?
- [Menu]: Selecciona una opción
  - [Choice]: ¡Parece demasiado peligroso para mí!
    - **Player:** ¡Parece demasiado peligroso para mí!
    - **Gnome ball referee:** Quizás tengas razón, hemos visto morir humanos en este campo.
  - [Choice]: Ok, entonces lo intentaré.
    - **Player:** Ok, entonces lo intentaré.
    - **Gnome ball referee:** ¡Excelente material! Gnomeball tiene pocas reglas, por lo que puede resultar un poco complicado.
    - **Gnome ball referee:** Puedes pasar a los gnomos extremos verdes. Entonces puedes correr y te devolverán el pase. De lo contrario, si te sientes valiente, puedes cargar y esquivar.
    - **Player:** Suena bastante fácil.
    - **Gnome ball referee:** El objetivo principal es salir sin extremidades rotas. Creo que deberías estar bien.
    - **Gnome ball referee:** {{RSChat|Peeeeeeeeeep}}
    - (receives=Gnomeball)

### Subsequent dialogue


#### Cuando no empuñas una Gnomeball

- **Player:** Hola.
- **Gnome ball referee:** Hola, bienvenido de nuevo a Gnomeball. ¿Te gustaría escuchar las reglas nuevamente?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, por favor.
    - **Gnome ball referee:** En realidad, es bastante simple: me quitas el balón, cargas contra la defensa de los gnomos e intentas lanzar el balón a través de la red usando tu habilidad a distancia. Es un juego duro pero muy divertido. También es excelente para mejorar la agilidad.
    - **Gnome ball referee:** Puedes pasar a los gnomos extremos verdes. Entonces puedes correr y te devolverán el pase. De lo contrario, si te sientes valiente, puedes cargar y esquivar.
    - **Player:** Suena bastante fácil.
    - **Gnome ball referee:** El objetivo principal es salir sin extremidades rotas. Creo que deberías estar bien.
    - **Gnome ball referee:** {{RSChat|Peeeeeeeeeep}}
    - (receives=Gnomeball)
  - [Choice]: Sólo quiero jugar.
    - **Player:** Sólo quiero jugar.
    - **Gnome ball referee:** Ok... ¡Juguemos GNOMEBALL!
    - **Gnome ball referee:** {{RSChat|Peeeeeeeeeep}}
    - (receives=Gnomeball)
  - [Choice]: No, no quiero jugar.
    - **Player:** No, no quiero jugar.
    - **Gnome ball referee:** Ok, no importa. ¿Tal vez la próxima vez?

#### Al empuñar una Gnomeball

- **Gnome ball referee:** Tienes una pelota en juego. ¿Necesitas volver a escuchar las reglas?
- [Menu]: Selecciona una opción
  - [Choice]: Sí por favor.
    - **Gnome ball referee:** En realidad, es bastante simple: me quitas el balón, cargas contra la defensa de los gnomos e intentas lanzar el balón a través de la red usando tu habilidad a distancia. Es un juego duro pero muy divertido. También es excelente para mejorar la agilidad.
    - **Gnome ball referee:** Puedes pasar a los gnomos extremos verdes. Entonces puedes correr y te devolverán el pase. De lo contrario, si te sientes valiente, puedes cargar y esquivar.
    - **Player:** Suena bastante fácil.
    - **Gnome ball referee:** El objetivo principal es salir sin extremidades rotas. Creo que deberías estar bien.
    - **Gnome ball referee:** Está bien jugar con la pelota que tienes en la mano... Empieza el juego.
  - [Choice]: No, gracias.
    - **Player:** No, gracias.
    - **Gnome ball referee:** Vale, buena suerte.

#### Después de marcar un gol

- **Gnome ball referee:** ¡Ten una pelota nueva!
- **Gnome ball referee:** {{RSChat|Peeeeeeeeeep}}
- (receives=Gnomeball)

#### Después de ganar el juego

- (receives=Gnomeball)
- **Gnome ball referee:** ¡Ganaste! Toma, toma una bola de gnomo.

### Treasure Trails


#### Recibiendo el pergamino de desafío

- (Condition: Only the first time:)
  - **Gnome ball referee:** Bien, aún no has terminado.
  - **Player:** Uf.
  - **Gnome ball referee:**Respóndeme esto.
- (receives=challenge scroll (medium))
- ¡[ref] te ha dado un pergamino de desafío!}}

#### Cuando hablé de nuevo

- **Gnome ball referee:** Ingrese la respuesta a la pregunta.
- Ingrese la cantidad:<br>[Input field]
- (Condition: When given the wrong answer:)
  - **Gnome ball referee:** ¡Respuesta incorrecta!
- (Condition: When given the correct answer:)
  - (removes=the clue scroll (medium) y desplazamiento de desafío (medio))
  - (Condition: If the trail continues:)
    - (receives=a new clue scroll (medium))
    - [¡El árbitro te ha dado otro pergamino de pistas!]
    - (continue)
  - (Condition: If the trail ends:)
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
    - (continue)
  - **Gnome ball referee:** ¡Bien hecho!
