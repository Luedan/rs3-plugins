# Menaphite guard (Sophanem Slayer Dungeon)

- **Original Wiki Page**: [Transcript:Menaphite guard (Sophanem Slayer Dungeon)](https://runescape.wiki/w/Transcript%3AMenaphite%20guard%20%28Sophanem%20Slayer%20Dungeon%29)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Entering the dungeon for the first time

- **Menaphite guard:** ¡Alto ahí! Por delante de aquí sólo está la muerte.
- **Player:** ¿Qué hay ahí dentro?
- **Menaphite guard:** Criaturas antinaturales. Hay un poder allí que me da escalofríos con solo pensarlo. Me quedé aquí y puedo sentirlo arrastrándose sobre mí; Me dan ganas de levantarme, abandonar mi puesto y volver corriendo con mi familia.
- **Player:** No puede ser tan malo. ¿Puedo simplemente echar un vistazo?
- (Condition: Si los jugadores no alcanzan el nivel 88 Slayer:)
  - **Menaphite guard:** Puedes hacerlo si lo deseas, pero al observarte, siento que no estás lo suficientemente capacitado en el arte de Slayer para sobrevivir allí abajo.
  - [Necesitas el nivel 88 Slayer antes de poder dañar a cualquiera de los monstruos en la mazmorra Sophanem Slayer.]
- **Menaphite guard:** Hmm, sí, parece que puedes arreglártelas solo, pero no puedes entrar ahí todavía. Estas criaturas no caen como lo hacen las bestias normales, existen en el límite de la vida y la muerte. Eso dicen los sacerdotes, de todos modos.
- **Menaphite guard:** Pero hay un objeto: la pluma de Ma'at. Pueden parecer plumas normales, pero contienen algo de magia... o tal vez una maldición, no lo sé realmente. Con una pluma sobre ti, estas criaturas caerán ante tus golpes.
- **Player:** ¿Dónde puedo conseguir estas plumas?
- **Menaphite guard:** Hay dos lugares. La primera es mía: no pensaste que me dejarían vigilar sin ellos, ¿verdad? Puedo vendértelos, por supuesto, por un costo.
- **Menaphite guard:** Sin embargo, si quieres recogerlos tú mismo, he oído que los trabajadores los han estado recuperando de las tumbas debajo de Menaphos. Si pudiste acceder a Menaphos y sus tumbas, estoy seguro de que podrás encontrar algunas allí abajo.
- (continue|When talked to)

### Entering the dungeon after the first time without a feather of Ma'at

- **Menaphite guard:** ¡Alto ahí! Más adelante sólo está la muerte, especialmente si no tienes plumas de Ma'at. Estaré encantado de venderte algunos, por supuesto, por un coste.
- [Menu]: ¿Entrar a la mazmorra Sophanem Slayer de todos modos?
  - [Choice]: Sí.
    - (Action: el player entra al calabozo.)
  - [Choice]: No.
    - (end)

### When talked to

- **Menaphite guard:** ¡Alto ahí! Por delante de aquí sólo está la muerte.
- [Menu]: Elige una opción:
  - [Choice]: ¿Qué hay ahí dentro?
    - **Menaphite guard:** Criaturas antinaturales. Hay un poder allí que me da escalofríos con solo pensarlo. Me quedé aquí y puedo sentirlo arrastrándose sobre mí; Me dan ganas de levantarme, abandonar mi puesto y volver corriendo con mi familia.
    - **Player:** No puede ser tan malo. ¿Puedo simplemente echar un vistazo?
    - (Condition: Si los jugadores no alcanzan el nivel 88 Slayer:)
      - **Menaphite guard:** Puedes hacerlo si lo deseas, pero al observarte, siento que no estás lo suficientemente capacitado en el arte de Slayer para sobrevivir allí abajo.
      - [Necesitas el nivel 88 Slayer antes de poder dañar a cualquiera de los monstruos en la mazmorra Sophanem Slayer.]
    - (Condition: Si no se lleva una pluma de Ma'at:)
      - **Menaphite guard:** Hmm, sí, parece que puedes arreglártelas solo, pero no puedes entrar ahí todavía. Estas criaturas no caen como lo hacen las bestias normales, existen en el límite de la vida y la muerte. Eso dicen los sacerdotes, de todos modos.
      - **Menaphite guard:** Pero hay un objeto: la pluma de Ma'at. Pueden parecer plumas normales, pero contienen algo de magia... o tal vez una maldición, no lo sé realmente. Con una pluma sobre ti, estas criaturas caerán ante tus golpes.
      - **Player:** ¿Dónde puedo conseguir estas plumas?
      - **Menaphite guard:** Hay dos lugares. La primera es mía: no pensaste que me dejarían vigilar sin ellos, ¿verdad? Puedo vendértelos, por supuesto, por un costo.
      - **Menaphite guard:** Sin embargo, si quieres recogerlos tú mismo, he oído que los trabajadores los han estado recuperando de las tumbas debajo de Menaphos. Si pudiste acceder a Menaphos y sus tumbas, estoy seguro de que podrás encontrar algunas allí abajo.
      - *(Vuelve a las opciones anteriores.)*
    - (Condition: Si se porta una pluma de Ma'at:)
      - **Menaphite guard:** Hmm, sí, parece que puedes arreglártelas solo. Muy bien, continúa si lo deseas, pero no me hago responsable de ningún dolor, sufrimiento o pérdida de extremidades que pueda ocurrir mientras estés allí.
      - (previous)
  - [Choice]: Don't worry, this is my area of speciality.|cond=Si los jugadores tienen el nivel 88 Slayer
    - (Condition: Si no se lleva una pluma de Ma'at:)
      - **Menaphite guard:** Hmm, sí, parece que puedes arreglártelas solo, pero no puedes entrar ahí todavía. Estas criaturas no caen como lo hacen las bestias normales, existen en el límite de la vida y la muerte. Eso dicen los sacerdotes, de todos modos.
      - **Menaphite guard:** Pero hay un objeto: la pluma de Ma'at. Pueden parecer plumas normales, pero contienen algo de magia... o tal vez una maldición, no lo sé realmente. Con una pluma sobre ti, estas criaturas caerán ante tus golpes.
      - **Player:** ¿Dónde puedo conseguir estas plumas?
      - **Menaphite guard:** Hay dos lugares. La primera es mía: no pensaste que me dejarían vigilar sin ellos, ¿verdad? Puedo vendértelos, por supuesto, por un costo.
      - **Menaphite guard:** Sin embargo, si quieres recogerlos tú mismo, he oído que los trabajadores los han estado recuperando de las tumbas debajo de Menaphos. Si pudiste acceder a Menaphos y sus tumbas, estoy seguro de que podrás encontrar algunas allí abajo.
      - (previous)
    - (Condition: Si se porta una pluma de Ma'at:)
      - **Menaphite guard:** Hmm, sí, parece que puedes arreglártelas solo. Muy bien, continúa si lo deseas, pero no me hago responsable de ningún dolor, sufrimiento o pérdida de extremidades que pueda ocurrir mientras estés allí.
  - [Choice]: ¿Puedo comprar algunas plumas de Ma'at?
    - (opens=Sophanem Slayer Supplies)
  - [Choice]: Entonces estaré en camino.
    - **Menaphite guard:** Cuídate.
