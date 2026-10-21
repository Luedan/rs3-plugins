# Caroline

- **Original Wiki Page**: [Transcript:Caroline](https://runescape.wiki/w/Transcript%3ACaroline)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Witchaven


#### Antes de la babosa de mar

- (ver|Babosa de mar#Preocupado Caroline)

#### Entre Sea Slug y The Slug Menace

- **Player:** Hola de nuevo.
- **Caroline:** Hola viajero, ¿cómo estás?
- **Player:** No está mal, ¿gracias?
- **Caroline:** Estoy bien. Ocupado como siempre cuidando a Kent y Kennith, pero no tengo quejas.

#### Después de la amenaza de las babosas

- **Player:** Hola Caroline.
- **Caroline:** Valiente Player, ¿tienes alguna noticia sobre mi hijo y su padre?
- **Player:** Estoy trabajando en ello ahora Caroline.
- **Caroline:** Por favor, tráelos de vuelta sanos y salvos.

#### Después de las preocupaciones de Kennith

- **Player:** Hola de nuevo, Caroline. ¿Están todos descansados ​​después de su terrible experiencia?
- **Caroline:** Sí, me siento mucho mejor, gracias. A Kennith también le está yendo bien en la plataforma.
- **Player:** Me alegra oírlo. ¡Espero que se esté portando bien!
- **Caroline:** Oh, sí, Bailey lo tiene trabajando tratando de limpiar la plataforma de babosas marinas. ¡Incluso empezó a escribir cartas a Kimberly!
- **Player:** ¿En serio? ¿Cómo ha reaccionado ella ante eso?
- **Caroline:** No creo que ella esté lista para perdonarlo todavía, pero tampoco creo que Kennith esté lista para darse por vencido. A decir verdad, ¡creo que está enamorado de ella! ¡Quién lo hubiera pensado!
- **Player:** Sí, es toda una revelación. Bueno, espero que le funcione. Podría ir a la plataforma Fishing para visitarlo pronto.
- **Caroline:** Oh, creo que eso le gustaría: ¡siempre está hablando de ti!
- **Player:** Haré lo mejor que pueda.

#### Después de la sal en la herida

- **Player:** Hola de nuevo, Caroline. ¿Has visto Kennith últimamente?
- **Caroline:** ¡Oh, crecen tan rápido!
- **Player:** Parece que algunos son más rápidos que otros.

#### Senderos del tesoro

- (Condition: Sólo la primera vez:)
  - **Caroline:** Disculpe, ¿pueden ayudarme con esta pregunta?
  - **Player:** Haré lo mejor que pueda.
  - **Caroline:** ¡Genial! Lo escribí para ti.
  - (continue)
- (receives=challenge scroll (medium))
- [¡Caroline te ha dado un pergamino de desafío!]

##### Cuando hablé de nuevo

- **Caroline:** Ingrese la respuesta a la pregunta.
- Ingrese la cantidad:<br>[Input field]
- ((Cuando se le da la respuesta incorrecta:))
  - (Condition: Si la respuesta no fue 11 (antes de las Preocupaciones de Kennith) o 0 (después de las Preocupaciones de Kennith):)
    - **Caroline:** ¿Estás seguro? Eso me suena un poco raro.
  - (Condition: Si la respuesta fue 11 (después de las Preocupaciones de Kennith):)
    - **Caroline:** Tal vez tuviste razón una vez, pero creo que el número ha bajado recientemente.
- (Condition: Cuando se le da la respuesta correcta:)
  - (removes=the clue scroll (medium) y desplazamiento de desafío (medio))
  - (Condition: Si el rastro continúa:)
    - (receives=a new clue scroll (medium))
    - [¡Caroline te ha dado otro pergamino de pistas!]
  - (Condition: Si el sendero termina:)
    - (receives=reward casket (medium))
    - [¡Has encontrado un ataúd!]
  - (Condition: Antes de las preocupaciones de Kennith:)
    - **Caroline:** ¡Muchas gracias!
  - (Condition: Después de las preocupaciones de Kennith:)
    - **Caroline:** ¡Un recuento actualizado! ¡Muchas gracias!
