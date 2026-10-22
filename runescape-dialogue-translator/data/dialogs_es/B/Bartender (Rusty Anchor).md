# Bartender (Rusty Anchor)

- **Original Wiki Page**: [Transcript:Bartender (Rusty Anchor)](https://runescape.wiki/w/Transcript%3ABartender%20%28Rusty%20Anchor%29)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### Normalmente


##### Antes de completar la misión Visiones de Havenhythe

- [Menu]: Selecciona una opción
  - [Choice]: Charla sobre 'Visiones de Havenhythe'
    - (ver | Visiones de Havenhythe)
  - [Choice]: Habla de otra cosa.
    - (below|After completing the Visions of Havenhythe quest)

##### Después de completar la misión Visiones de Havenhythe

- **Player:** ¡Buenos días para ti!
- **Barman:** ¡Hola!
- (Condition: If the player has completed A Void Dance:)
  - **Bartender:** Gracias por ordenar mi bodega.
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: ¿Puedo comprar una cerveza, por favor?
    - **Player:** ¿Puedo comprar una cerveza, por favor?
    - **Bartender:** Claro, serán dos gold coins, por favor.
    - (Condition: If the player has enough money:)
      - (removes=2 coins) (receives=beer)
      - **Player:** Gracias, camarero.
    - (Condition: If the player does not have enough money:)
      - No puedes permitirte eso.
      - **Bartender:** ¡Dije 2 coins! ¡No tienes 2 coins!
      - **Player:** Lo siento, volveré otro día.
  - [Choice]: cond=After Rocking Out|Pregunta por el 'ron'.
    - **Player:** ¿Cómo van las cosas?
    - **Barman:** ¡No está bien! La demanda de la solución limpiadora de desagües de Braindeath ha disminuido por completo.
    - **Player:** ¡Guau! Debe haber sido uno de esos picos de marketing de los que oyes hablar.
    - **Camarero:** Sea lo que sea, ahora tengo un contrato de 10 años para almacenar la bazofia nociva de ese viejo chacal.
    - **Bartender:** No querrás un poco, ¿verdad?
    - [Menu]: Selecciona una opción
      - [Choice]: Ah, está bien.
        - **Player:** Oh, está bien.
        - (Condition: If the player has enough money:)
          - (removes=30 coins) (receives=Braindeath 'rum')
          - **Barman:** ¡Gracias! Sé que está mal aprovechar tu adicción paralizante a esta sustancia peligrosa, pero tengo un obstáculo que gestionar.
          - **Player:** Qué mentalidad comunitaria de tu parte.
        - (Condition: If the player does not have enough money:)
          - No puedes permitirte eso.
          - **Camarero:** ¡Oh, pobre pilluelo adicto al ron! No tienes el dinero para ello, pero aún quieres las cosas.
          - **Bartender:** *Sniff* Es triste ver a alguien tan bajo.
          - **Player:** ¡Oye! ¡NO soy un pilluelo!
      - [Choice]: Lo siento. No ahora mismo.
        - **Player:** Lo siento. No ahora mismo.
        - **Camarero:** ¡Pah! Nunca debí haberte escuchado.
  - [Choice]: Adiós entonces.
    - **Player:** Adiós, entonces.
    - **Bartender:** ¡Vuelve pronto!

#### Senderos del tesoro

- **Barman:** ¡Felicitaciones! Aquí tienes.
- (removes=the old clue scroll (easy))
- ((If the trail continues:))
  - (receives=a new clue scroll (easy))
  - [El camarero te ha dado otro pergamino de pistas.]
- ((If the trail ends:))
  - (receives=reward casket (easy))
  - [¡Has encontrado un ataúd!]

#### Con un barril de hidromiel antes de realizar una entrega a Rusty Anchor durante el evento The Need for Mead

- **Player:** Me preguntaba si podrías darnos algún comentario sobre este hidromiel.
- **Bartender:** ¿Dónde se preparó? ¿Quién es el cervecero?
- **Player:** No tengo idea de dónde se elaboró, pero la cervecería se llama Leslie.
- **Bartender:** No volveré a probar nada de lo que hacen, nunca más. No después de la última vez...
- **Player:** ¿Qué pasó la última vez?
- **Bartender:** Eso no es para que tú lo sepas.
- **Bartender:** En realidad, ¿sabes qué? Entrégalo. Déjame echar un vistazo.
- (removes=keg of mead) (receives=50 nectar)
- (ver|néctar)
- ((Shown in a pop-up:))
  - (Pop-up: You find 50 x Nectar as you hand over the keg of mead.|colour=#00FF00)
  - (continue)
- **Player:** ¡Vaya! No lo desperdicies todo.
- **Bartender:** Le estoy haciendo justicia a Gielinor al asegurarme de que nadie más tenga que beber esto.
- **Player:** Bueno, entonces...
- **Player:** Sr. Gruñón...
- **Barman:** ¡¿Qué dijiste?!
- **Player:** ¡Adiós!

#### Diálogo histórico

- [Menu]: Selecciona una opción
  - [Choice]: ¿Puedo comprar una cerveza, por favor?
    - (arriba)
  - [Choice]: ¿Has oído algún rumor aquí?
    - **Player:** ¿Has oído algún rumor aquí?
    - (Condition: Before Goblin Diplomacy:)
      - **Camarero:** Bueno, antes hubo un tipo aquí que dijo que los duendes de la montaña están discutiendo de nuevo, sobre todo sobre el color de su armadura.
      - **Camarero:** Conociendo a los duendes, fácilmente podría convertirse en una guerra en toda regla, lo cual no sería bueno. Las guerras de duendes ensucian el campo.
      - **Player:** Bueno, si tengo tiempo, iré a ver si puedo darles algo de sentido común.
    - (Condition: After Goblin Diplomacy:)
      - **Bartender:** No, no ha estado muy ocupado últimamente.
