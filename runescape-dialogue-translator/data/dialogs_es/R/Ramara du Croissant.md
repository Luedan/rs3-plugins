# Ramara du Croissant

- **Original Wiki Page**: [Transcript:Ramara du Croissant](https://runescape.wiki/w/Transcript%3ARamara%20du%20Croissant)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Ramara du Croissant:** ¿Puedo ayudarle, señor?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¡Tienes un acento interesante!
    - **Player:** ¡Tienes un acento interesante!
    - **Ramara du Croissant:** Sí, he perfeccionado este acento cuando trabajaba para mi padre en Ardougne. Es panadero en el mercado y cree que los clientes pensarán que el pan es de mayor calidad si lo elabora un extranjero.
    - **Player:** ¿Y eso funciona?
    - **Ramara du Croissant:** Quizás. No me gusta el pan; es el pescado que será mi futuro.
    - **Player:** ¡Buena suerte con eso!
  - [Choice]: ¿Por qué trabajas en una colonia de pescadores?
    - **Player:** ¿Por qué trabajas en una colonia de pescadores?
    - **Ramara du Croissant:** Ahh, es porque amo el mar. Las aguas que corren, el horizonte infinito: ¡es hermoso! Además, me gusta el pescado fresco.
    - **Player:** Parece un trabajo bastante duro. ¿No puedes simplemente conseguir una casa en la playa en Karamja?
    - **Ramara du Croissant:** Me temo que Zat no es una opción para mí. Además, he leído sobre la isla de Karamja: está llena de grandes arañas verdes, ¡y no me gustan!
    - **Player:** Muy bien.
  - [Choice]: No gracias, estoy bien.
    - **Player:** No, gracias, estoy bien.
    - **Ramara du Croissant:** Ahh, adiós.

### Treasure Trails


#### Recibiendo la caja del rompecabezas

- **Ramara du Croissant:** Tengo este rompecabezas para que lo resuelvas.
- (receives=puzzle box)
- [¡Ramara te ha regalado una caja de rompecabezas!]

#### Cuando se vuelve a hablar con él sin resolver el rompecabezas

- **Ramara du Croissant:** ¡Puedes hacerlo mejor que zat!

#### Cuando se le habla con el rompecabezas resuelto

- (Condition: If the trail continues:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives= the new clue scroll (hard))
  - [¡Ramara te ha dado otro pergamino de pistas!]
  - (continue)
- (Condition: If the trail ends:)
  - (removes=the old clue scroll (hard) y caja de rompecabezas) (receives=reward casket (hard))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Ramara du Croissant:** ¡Zat es maravilloso!
