# King Bolren

- **Original Wiki Page**: [Transcript:King Bolren](https://runescape.wiki/w/Transcript%3AKing%20Bolren)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Tree Gnome Village


#### Antes del árbol Pueblo Gnome

- (ver|Árbol Pueblo Gnome)

#### Después del árbol Gnome Village

- **Player:** Hola de nuevo Bolren.
- **King Bolren:** Bueno, hola, es un placer verte de nuevo.
- (Condition: Si se ha perdido el amuleto del gnomo:)
  - **Player:** He perdido mi amuleto.
  - **King Bolren:** Dios mío. Toma, toma otro. Estamos realmente en deuda con usted.
  - (receives=gnome amulet)

#### Después de Los ojos de Glouphrie

- **Player:** Hola de nuevo Bolren.
- **King Bolren:** Bueno, hola, es un placer verte de nuevo.
- (Condition: Si se ha perdido el amuleto del gnomo:)
  - **Player:** He perdido mi amuleto.
  - **King Bolren:** Dios mío. Toma, toma otro. Estamos realmente en deuda con usted.
  - (receives=gnome amulet)
  - (continue)
- ((Se abre la interfaz de descripción general de misiones para The Path of Glouphrie.))
  - [Choice]: No ahora mismo
    - (end)
  - [Choice]: Aceptar misión
    - (Condition: Sin cumplir los requisitos de la misión:)
      - No cumples los requisitos para empezar: 'El Camino de Glouphrie'.
      - (ventana emergente)
        - (Ventana emergente: No cumples con los requisitos para comenzar: 'El Camino de Glouphrie'.|advertencia=yes)
    - (Condition: Cumplir con los requisitos de la misión:)
      - (ver | El camino de Gloufrie)

#### Después del camino de Glouphrie

- (Condition: Si se ha perdido el amuleto del gnomo:)
  - **Player:** He perdido mi amuleto.
  - **King Bolren:** Dios mío. Toma, toma otro. Estamos realmente en deuda con usted.
  - (receives=gnome amulet)
  - (continue)
- **Player:** ¡Creo que ya sé dónde está Arposandra!
- **King Bolren:** ¿En serio? ¿Has estado allí?
- **Player:** No exactamente. Encontré una manera de entrar, aunque todavía no puedo abrir el respiradero para entrar.
- **King Bolren:** Entonces, en realidad no has estado allí. Bueno, todavía no estoy convencido de que sea un lugar real. Hay algo en las ciudades perdidas que obsesiona a los exploradores y aventureros.
- **Player:** No estoy obsesionado, pero *encontraré* una manera de entrar. Con el tiempo.
- **King Bolren:** Por supuesto que sí.

#### Después del prisionero de Glouphrie

- (Condition: Si se ha perdido el amuleto del gnomo:)
  - **Player:** He perdido mi amuleto.
  - **King Bolren:** Dios mío. Toma, toma otro. Estamos realmente en deuda con usted.
  - (receives=gnome amulet)
  - (continue)
- **Player:** ¡Encontré a Arposandra!
- **King Bolren:** ¿En serio? ¿De verdad has estado allí?
- **Player:** Brevemente, sí. Realmente es un lugar peligroso.
- **King Bolren:** ¡No te creo! Tienes que estar bromeando.
- **Player:** Quizás algún día me creas.

#### Senderos del tesoro

- **King Bolren:** ¡Felicitaciones, humano!
- (removes=the old clue scroll (medium))
- ((Si el rastro continúa:))
  - (receives=a new clue scroll (medium))
  - [¡King Bolren te ha dado tu próximo pergamino de pistas!]
- ((Si el sendero termina:))
  - (receives=reward casket (medium))
  - [¡Has encontrado un ataúd!]

#### Gnome Entrega en restaurante

- **King Bolren:** Gracias. Aquí no tengo cocineros gnomos. Realmente debería hacer algo al respecto.
