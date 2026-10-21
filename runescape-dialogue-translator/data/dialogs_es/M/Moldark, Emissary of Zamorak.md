# Moldark, Emissary of Zamorak

- **Original Wiki Page**: [Transcript:Moldark, Emissary of Zamorak](https://runescape.wiki/w/Transcript%3AMoldark%2C%20Emissary%20of%20Zamorak)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Template:Incomplete|missing dialogue from after completing all tasks}}

### Standard dialogue

- {{anchor|initial}}**Moldark, Emissary of Zamorak:** Yo, mi amigo, soy Moldark: el principal seguidor de Zamorak. Soy su emisario.
- **Moldark, Emissary of Zamorak:** Estoy aquí para enseñarte los caminos del caos: ¡el camino del poder!
- **Moldark, Emissary of Zamorak:** ¡Únete conmigo y con Zamorak! Si lo haces, puede que tenga algo de trabajo para ti.
- [Menu]: Elige una opción:
  - [Choice]: Who are you?|cond=Si continúa con las opciones anteriores:
    - (continuea|initial)
  - [Choice]: ¿Puedes contarme sobre Zamorak?
    - **Moldark, Emissary of Zamorak:** ¿Qué quieres saber sobre Zamorak?
    - [Menu]: Elige una opción:
      - [Choice]: ¿Quién es Zamorak?
        - {{anchor|whoiszamorak}}**Moldark, Emissary of Zamorak:** Zamorak alguna vez fue un mortal, como tú y como yo. Pero conocía el valor del caos y buscó poder a través de él.
        - **Moldark, Emissary of Zamorak:** Cuando se le presentó la oportunidad de convertirse en dios, Zamorak la aprovechó con gusto.
        - **Moldark, Emissary of Zamorak:** Ahora es un dios poderoso, el dios del caos y la destrucción.
          - (otro)
      - [Choice]: ¿Por qué debería seguir Zamorak?
        - **Moldark, Emissary of Zamorak:** Una gran creación sólo puede seguir a una gran destrucción. Todos progresamos más rápidamente cuando reina el caos.
        - **Moldark, Emissary of Zamorak:** Pero seguir Zamorak también es una ganancia personal. Al igual que Zamorak, todos deberíamos estar preparados para tomar el poder cuando se nos ofrezca.
        - (otro)
      - [Choice]: ¿Qué quiere Zamorak ?
        - **Moldark, Emissary of Zamorak:** Zamorak ve el estancamiento debajo de la paz predicada por los otros dioses. Quieren ovejas pasivas para moler bajo sus pies.
        - **Moldark, Emissary of Zamorak:** Zamorak ve el verdadero camino hacia la grandeza. Es a través del caos y el conflicto que los mortales dan sus mayores pasos.
        - (otro)
      - [Choice]: Habla de otra cosa.
        - (previous)
  - [Choice]: ¡Quiero declarar mi apoyo a Zamorak!
  - **Moldark, Emissary of Zamorak:** ¡Eso es maravilloso! En nombre de los seguidores de Zamorak les doy la bienvenida.
  - (receives=Banner of Zamorak)
  - **Moldark, Emissary of Zamorak:** Por favor, lleve este banner para mostrar su apoyo.
  - **Moldark, Emissary of Zamorak:** Tengo un regalo para ti: un libro de historias sobre los dioses y sus seguidores. Por favor, léelo.
  - **Moldark, Emissary of Zamorak:** Tal vez arroje algo de luz sobre los delirios de orden y contingencia que tienen los demás.
  - **Moldark, Emissary of Zamorak:** Sin embargo, el libro aún no está completo. Cuando completes algunos trabajos te daré más páginas.
  - (receives=Book of the Gods)
  - [El emisario te entrega el Libro de los Dioses.]
  - (Condition: Si está en mundos gratuitos:)
    - [El libro está actualmente incompleto. Puedes ganar más páginas haciendo trabajos para el emisario, que solo están disponibles en los mundos de los miembros.]
    - (previous)

### Dialogue with the players supporting Zamorak

- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - (continuea|initial)
  - [Choice]: ¿Puedes contarme sobre Zamorak?
    - (continuea|whoiszamorak)
  - [Choice]: ¿Tienes algún trabajo para mí?
    - (Condition: Si está en mundos gratuitos:)
      - [¡Los trabajos de emisario de Dios solo se pueden realizar en los mundos de un miembro!]
      - (previous)
    - (ver|God Emissaries)
  - [Choice]: Habla de recompensas.
    - (ver|God Emissaries#Recompensas)

### Treasure Trails

- (Condition: Sólo la primera vez:)
  - **Moldark, Emissary of Zamorak:** ¿Qué quieres de mí?
  - **Player:** ¿Puedes ayudarme con este rastro del tesoro?
  - **Moldark, Emissary of Zamorak:** ¡Solo si demuestras tu valía respondiendo esta pregunta!
- (receives=challenge scroll (medium))
- [¡Moldark te ha dado un pergamino de desafío!]

##### Cuando hablé de nuevo

- **Moldark, Emissary of Zamorak:** Ingrese la respuesta a la pregunta.
- Ingrese la cantidad:<br>[Input field]
- (Condition: Cuando se le da la respuesta incorrecta:)
  - **Moldark, Emissary of Zamorak:** ¡Mal!
- (Condition: Cuando se le da la respuesta correcta:)
  - (removes=the clue scroll (medium) y desplazamiento de desafío (medio))
  - (Condition: Si el rastro continúa:)
    - (receives=a new clue scroll (medium))
    - [¡Moldark te ha dado otro pergamino de pistas!]
    - (continue)
  - (Condition: Si el sendero termina:)
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
    - (continue)
  - (Condition: Si la respuesta correcta fue 7 antes del Ritual del Mahjarrat:)
    - **Moldark, Emissary of Zamorak:** ¡Correcto!
  - (Condition: Si la respuesta correcta fue 7 después del Ritual del Mahjarrat:)
    - **Moldark, Emissary of Zamorak:** Así era, antes de la quema. ¿Sabes que? Lo contaré como un pase.
  - (Condition: Si la respuesta correcta fue 3 después del Ritual del Mahjarrat:)
    - **Moldark, Emissary of Zamorak:** Correcto. Eso es todo lo que queda ahora. Tanta muerte...
Categoría:God Emissaries
