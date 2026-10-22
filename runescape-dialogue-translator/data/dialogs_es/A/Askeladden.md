# Askeladden

- **Original Wiki Page**: [Transcript:Askeladden](https://runescape.wiki/w/Transcript%3AAskeladden)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Rellekka


#### Hablar con


##### Antes de los juicios de Fremennik

- **Player:** Hola.
- **Askeladden:** Hola, amigo. Eres un extranjero, ¿eh? Realmente se supone que no debo hablar contigo.
- **Player:** ¿Por qué no?
- **Askeladden:** No lo sé, amigo. Alguna estúpida tradición u otra. Siempre se nos dice que no hablemos con los extranjeros a menos que el Cacique lo permita.
- **Player:** ¿El Cacique? ¿Quién es ese?
- **Askeladden:** Su nombre es Brundt, amigo. Es un tipo realmente aburrido. Puedes encontrarlo en el largo pasillo de allí.
- **Player:** ¿Puedes llevarme a verlo?
- **Askeladden:** Lo siento amigo, no tengo permitido entrar al pasillo largo. No te preocupes, es fácil de detectar. Él es el que lleva el casco elegante. Ah, y sólo tiene un ojo.
- **Player:** ¿Es un cíclope?
- **Askeladden:** No, no, no... ¡Solo lleva un parche en el ojo! Bueno, ¡nos vemos amigo!

##### Después de los juicios de Fremennik

- **Player:** Hola de nuevo Askeladden.
- **Askeladden:** ¡Hola amigo! ¡Ese ya no es mi nombre! ¡Mi nuevo nombre Fremennik es Larravak! ¿Cuál es el tuyo?
- **Player:** Mi nombre Fremennik es [Fremennik name].
- **Askeladden:** ¡Ja! ¡No es tan bueno como mi nombre, amigo! Entonces, ¿para qué puedo ayudarte?
- [Menu]: Elige una opción:
  - [Choice]: cond=After Hero's Welcome:|Preguntar por V
    - **Askeladden:** Sí, es triste. He oído que está muerto. Parecía un buen tipo.
    - **Askeladden:** ¡Un día seré un héroe como él!
  - [Choice]: Preguntar sobre cosas que hacer
    - **Player:** Entonces, Askeladd, lo siento, Larravak; ¿Qué hay que hacer por aquí ahora que ambos somos Fremenniks?
    - **Askeladden:** Supongo que podrías hacer algunas compras. Conseguimos pescado fresco en los muelles y algunas armaduras y armas en casa de Skulgrimen.
    - **Player:** Está bien, gracias.
  - [Choice]: Pide una nueva piedra para mascotas.
    - **Player:** ¿Puedo tener otra piedra como mascota? yo perdi el mio...
    - **Askeladden:** ¡Claro amigo! Yo diría que cuides mejor este, ¡pero es solo una roca! ¡Tengo cientos de ellos! ¡Vuélvete loco!

### Waterbirth Island


#### Hablar con


##### Antes de los juicios de Fremennik

- **Player:** Hola.
- **Askeladden:** Hola, amigo.<br>Eres un extranjero, ¿eh?
- **Askeladden:** ¡No pensé que el viejo Jarvald dejaría que un extranjero viniera a matar bocas de daga con él!
- **Player:** Bueno, obviamente lo hizo.<br>Entonces, ¿qué estás haciendo aquí arriba?
- **Askeladden:** Bueno, amigo, déjame decirte que matar a esos bocas de daga es un trabajo que da sed.
- **Askeladden:** ¡Si tienes un barril de cerveza contigo, te lo compraré por 500 gold coins, amigo!
- **Askeladden:** O si tienes partes de animales, ¡te cambio algo por ellas!
- (Condition: If the player does not have any kegs of beer nor any animal parts:)
  - **Player:** No... No tengo nada de eso conmigo...
  - **Askeladden:** Bueno, ¡no volveré allí hasta que consiga un compañero de bebida! ¡Ven a verme si me encuentras un barril, pago un buen dinero!
- (Condition: If the player has at least one keg of beer but no animal parts:)
  - **Askeladden:** ¿Quieres venderme barriles de cerveza a 500 gold coins cada uno?
  - **Player:** No lo sé... Parece un poco fuera de lugar venderle alcohol a un niño...
  - **Askeladden:** ¡Oye, no juzgues a nuestro extranjero de aduanas! ¿Ahora quieres el dinero o quieres molestarme?
  - **Askeladden:** ¿Ahora me venderás cerveza o llorarás por eso todo el día?
  - [Menu]: ¿Quieres vender tus barriles de cerveza?
    - [Choice]: SI
      - **Askeladden:** ¿Quieres venderme el lote, amigo, o uno a la vez?
      - [Menu]: Selecciona una opción
        - [Choice]: Vender todos los barriles
          - (removes=all kegs of beer in backpack)
          - (receives=500 coins per keg of beer)
          - Vendes Askeladden tus barriles de cerveza.
        - [Choice]: Vender un barril
          - (removes=keg of beer)
          - (receives=500 coins)
          - Vendes Askeladden un barril de cerveza.
          - [Menu]: ¿Vender otro barril?
            - [Choice]: SI
              - (Condition: If the player does not have at least one keg of beer:)
                - **Player:** Pero no tengo barriles de cerveza para vender...
              - (Condition: If the player has at least one keg of beer:)
                - (above|sell-one-keg1)
            - [Choice]: NO
              - (end)
    - [Choice]: NO
      - **Player:** Sin ofender Askeladden, y no es que no confíe en ti...<br>Er, en realidad es que no confío en ti.
      - **Askeladden:** Ay, amigo...<br>¿Qué te hice?
      - **Askeladden:** Bueno, si cambias de opinión, ¡estaré aquí esperando una bebida, amigo!
- (Condition: If the player has at least one animal part but no kegs of beer:)
  - **Askeladden:** Te cambiaré partes de animales por atún cocido, ¿estás interesado en el exterior?
  - [Menu]: ¿Te gustaría cambiar partes de animales por comida?
    - [Choice]: SI
      - **Askeladden:** ¿Quieres cambiarme el lote, amigo, o solo un tipo?
      - [Menu]: Selecciona una opción
        - [Choice]: Cambie todas las piezas
          - (removes=all animal parts in backpack)
          - (receives=one tuna per animal part)
          - Cambias Askeladden tus partes de animales por comida.
        - [Choice]: Vender un solo tipo
          - **Askeladden:** ¿Qué estás vendiendo, amigo?
          - [Menu]: Selecciona una opción
            - [Choice]: cond=If the player has at least one dagannoth hide:|Pieles oscurecidas
              - (removes=all dagannoth hides in backpack)
              - (receives=one tuna per dagannoth hide)
              - Cambias las piezas por comida.
            - [Choice]: cond=If the player has at least one fibula piece, ribcage piece, or skull piece:|Huesos de Wallasalki
              - (removes=all fibula pieces, ribcage pieces, and skull pieces in backpack)
              - (receives=one tuna per item)
              - Cambias las piezas por comida.
            - [Choice]: cond=If the player has at least one circular hide, flattened hide, or stretched hide:|Pieles aligeradas
              - (removes=all circular hides, flattened hides, and stretched hides in backpack)
              - (receives=one tuna per item)
              - Cambias las piezas por comida.
            - [Choice]: nada
              - (above|no-offence1)
    - [Choice]: NO
      - (above|no-offence1)
- (Condition: If the player has at least one keg of beer and at least one animal part:)
  - [Menu]: ¿Qué te gustaría negociar?
    - [Choice]: barriles por dinero
      - (above|sell-beer1)
    - [Choice]: Partes de animales para alimentación.
      - (above|sell-hides1)
    - [Choice]: nada
      - (above|no-offence1)

##### Después de los juicios de Fremennik

- **Askeladden:** ¡Hola amigo! ¿O quieres que te llame [Fremennik name] ahora?
- [Menu]: Selecciona una opción
  - [Choice]: Pregunta qué está haciendo Askeladden aquí
    - **Player:** Askeladden, ¿qué estás haciendo Gielinor aquí arriba? Y por cierto, el nombre es Player.
    - **Askeladden:** ¡Claro, amigo!
    - **Askeladden:** ¡Estaba en esa cueva matando bocas de daga! ¡Fue divertido! Pero luego tuve sed, así que vine aquí para descansar un poco...
    - **Askeladden:** Hola amigo, te diré una cosa, si tienes barriles de cerveza, ¡te los compraré por 700 gold coins cada uno!
    - **Askeladden:** Si encuentras partes de animales matando bocas de daga, ¡también te las cambiaré por ellas!
    - (Condition: If the player does not have any kegs of beer nor any animal parts:)
      - **Player:** No... No tengo nada de eso conmigo...
      - **Askeladden:** Bueno, ¡no volveré allí hasta que consiga un compañero de bebida! ¡Ven a verme si me encuentras un barril, pago un buen dinero!
    - (Condition: If the player has at least one keg of beer but no animal parts:)
      - **Askeladden:** ¿Quieres venderme barriles de cerveza a 700 gold coins cada uno, amigo?
      - **Player:** Um... ¿No eres un poco... ...joven para beber tanto?
      - **Askeladden:** ¡Oye, no me hables así amigo! ¡He hecho todas las pruebas que tienes y soy tan Fremennik como tú!
      - **Askeladden:** ¿Ahora me venderás cerveza o llorarás por eso todo el día?
      - [Menu]: ¿Quieres vender tus barriles de cerveza?
        - [Choice]: SI
          - **Askeladden:** ¿Quieres venderme el lote, amigo, o uno a la vez?
          - [Menu]: Selecciona una opción
            - [Choice]: Vender todos los barriles
              - (removes=all kegs of beer in backpack)
              - (receives=700 coins per keg of beer)
              - Vendes Askeladden tus barriles de cerveza.
            - [Choice]: Vender un barril
              - (removes=keg of beer)
              - (receives=700 coins)
              - Vendes Askeladden un barril de cerveza.
              - [Menu]: ¿Vender otro barril?
                - [Choice]: SI
                  - (Condition: If the player does not have at least one keg of beer:)
                    - **Player:** Pero no tengo barriles de cerveza para vender...
                  - (Condition: If the player has at least one keg of beer:)
                    - (above|sell-one-keg)
                - [Choice]: NO
                  - (end)
        - [Choice]: NO
          - **Player:** Sin ofender Askeladden, y no es que no confíe en ti... Er, en realidad es que no confío en ti.
          - **Askeladden:** Ay, amigo... ¿Qué te hice?
          - **Askeladden:** Bueno, si cambias de opinión, ¡estaré aquí esperando una bebida, amigo!
    - (Condition: If the player has at least one animal part but no kegs of beer:)
      - **Askeladden:** ¡Te cambiaré partes de animales por langostas cocidas si estás interesado, amigo!
      - [Menu]: ¿Te gustaría cambiar partes de animales por comida?
        - [Choice]: SI
          - **Askeladden:** ¿Quieres cambiarme el lote, amigo, o solo un tipo?
          - [Menu]: Selecciona una opción
            - [Choice]: Cambie todas las piezas
              - (removes=all animal parts in backpack)
              - (receives=one lobster per animal part)
              - Cambias Askeladden tus partes de animales por comida.
            - [Choice]: Vender un solo tipo
              - **Askeladden:** ¿Qué estás vendiendo, amigo?
              - [Menu]: Selecciona una opción
                - [Choice]: cond=If the player has at least one dagannoth hide:|Pieles oscurecidas
                  - (removes=all dagannoth hides in backpack)
                  - (receives=one lobster per dagannoth hide)
                  - Cambias las piezas por comida.
                - [Choice]: cond=If the player has at least one fibula piece, ribcage piece, or skull piece:|Huesos de Wallasalki
                  - (removes=all fibula pieces, ribcage pieces, and skull pieces in backpack)
                  - (receives=one lobster per item)
                  - Cambias las piezas por comida.
                - [Choice]: cond=If the player has at least one circular hide, flattened hide, or stretched hide:|Pieles aligeradas
                  - (removes=all circular hides, flattened hides, and stretched hides in backpack)
                  - (receives=one lobster per item)
                  - Cambias las piezas por comida.
                - [Choice]: nada
                  - (above|no-offence)
        - [Choice]: NO
          - (above|no-offence)
    - (Condition: If the player has at least one keg of beer and at least one animal part:)
      - [Menu]: ¿Qué te gustaría negociar?
        - [Choice]: barriles por dinero
          - (above|sell-beer)
        - [Choice]: Partes de animales para alimentación.
          - (above|sell-hides)
        - [Choice]: nada
          - (above|no-offence)
  - [Choice]: Pide una nueva piedra para mascotas.
    - **Player:** ¿Puedo tener otra piedra como mascota? yo perdi el mio...
    - (receives=pet rock)
    - **Askeladden:** Bueno, seguro que es un lugar extraño para pedirlo, amigo, ¡pero tengo cientos de ellos! ¡Vuélvete loco!
