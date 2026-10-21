# Lifeguard

- **Original Wiki Page**: [Transcript:Lifeguard](https://runescape.wiki/w/Transcript%3ALifeguard)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Cuando está demasiado lejos del noreste

- Necesitas acercarte al socorrista para hablar.

#### Cuando esté lo suficientemente cerca del noreste o cuando hable con cualquier otro socorrista

- (Condition: Si Clawdia está ausente:)
  - **Lifeguard:** Hola. ¿Cómo puedo ayudar?
  - (continue)
- (Condition: Si Clawdia está presente:)
  - **Lifeguard:** H-h-hola. ¿Cómo puedo ayudar?
  - (continue)
- **Player:** ¿Me pregunto cómo estás?
- (Condition: Si Clawdia está ausente:)
  - **Lifeguard:** Estoy muy bien. Esta playa está bajo mi control y me siento bien.
  - **Lifeguard:** Si estás en peligro, grita y estaré ahí para ayudarte.
- (Condition: Si Clawdia está presente:)
  - **Lifeguard:** Vas a hacer que esa cosa desaparezca, ¿no? Esa... esa criatura.
  - **Player:** Claro, haré que desaparezca.
  - **Lifeguard:** Oh, está bien, bien. Gracias.

### Title progress


#### Cuando está demasiado lejos del noreste

- Necesitas acercarte al salvavidas para hablar.

#### Cuando esté lo suficientemente cerca del noreste o cuando utilice cualquier otro salvavidas

- Clawdia mata: [número]/15<br>Helados comidos: [número]/10

### Announcing the portals (historical)

- *(La línea aplicable se ve cada vez que un portal se activa además de un mensaje general estándar:)*
  - {{Colour: A game of Flish Flingers just opened up!}}
  - {{Colour: A Guthixian cache has just opened up!}}
  - {{Colour: A shooting star just crash landed!}}
  - {{Colour: A sinkhole and big chinchompa entrance have just spawned!}}
  - {{Colour: It looks like something is about to happen in the Wilderness!}}
  - {{Colour: Looks like you're able to get through to the spirit plane now for some Familiarisation!}}
  - {{Colour: There's an evil tree causing total havoc!}}

### Beach stats (historical)

- Progreso del título de 2017<br />Termómetros llenos: [number or 25+]<br />Clawdia mata: [number or 50+]<br />Helados comidos: [number or 10+]
- Progreso del título de 2016<br />Termómetros llenos: [number or 50+]<br />Clawdia mata: [number or 50+]<br />Helados comidos: [number or 10+]
- Progreso del título de 2015<br />Termómetros llenos: [number or 50+]<br />Clawdia mata: [number or 50+]<br />Helados comidos: [number or 10+]

### Northern one with the Sandy Clue Scroll (historical)

- **Lifeguard:** Ah, encontré esto dentro de una de mis bebidas. ¡Tiene tu nombre!
- (Condition: Recibir un cuadro de desplazamiento:)
  - (removes=Sandy Clue Scroll) (receives=Sandy Scroll box)
  - [scrollbox].}}
- (Condition: Recibir ataúdes:)
  - (Condition: Sin espacio libre backpack:)
    - [Necesitas 1 espacio libre en tu backpack para recibir tus cofres de pistas.]
  - (Condition: Con espacio gratuito backpack:)
    - (removes=Sandy Clue Scroll) (receives=Sandy Casket and its red version)
    - [¡Te entregan un ataúd!]
