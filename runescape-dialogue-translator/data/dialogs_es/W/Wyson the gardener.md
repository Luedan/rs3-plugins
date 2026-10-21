# Wyson the gardener

- **Original Wiki Page**: [Transcript:Wyson the gardener](https://runescape.wiki/w/Transcript%3AWyson%20the%20gardener)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Wyson the gardener:** Soy el jardinero jefe de aquí.<br>Si estás buscando hojas de glasto o si necesitas ayuda con algo, soy tu hombre.
- [Menu]: ¿De qué te gustaría hablar?
  - [Choice]: Pregunte por el inusual macizo de flores.
    - **Player:** ¿Qué pasa con el extraño macizo de flores?
    - **Wyson the gardener:** Oh, ¿los nuevos lirios? Sí, acabamos de empezar...
    - **Player:** No, me refiero a las plantas distorsionadas cuyas raíces expuestas se sumergen en una oscuridad incognoscible.
    - **Wyson the gardener:** Ah.
    - **Wyson the gardener:** Esperaba que no se notara tanto.
    - **Wyson the gardener:** Solo quería asegurarme de que Falador tuviera el mejor parque en Gielinor, pero me dejé llevar por un poco de la 'poción de crecimiento súper ultrafloral de Malignius Mortifer'.
    - **Wyson the gardener:** Para empeorar las cosas, ha afectado a uno de los topos locales y sigue arruinando mis parterres.
    - **Player:** ¿Hay algo que pueda hacer para ayudar?
    - **Wyson the gardener:** Tal vez alguien podría meterse allí y ocuparse de ella.
    - **Wyson the gardener:** ¿Podrías hacerlo? Puedo ofrecerte algunos nidos de pájaros a cambio de las garras o pieles que encuentres.
    - [Menu]: Selecciona una opción
      - [Choice]: Está bien.
        - **Player:** Está bien, pondré fin a esto.
        - **Wyson the gardener:** Gracias, aventurero.
      - [Choice]: ¿Por qué estás coleccionando garras de topo?
        - **Wyson the gardener:** La esposa los ama.
        - [Menu]: Selecciona una opción
          - [Choice]: ... Está bien.
            - **Player:** Está bien, pondré fin a esto.
            - **Wyson the gardener:** Gracias, aventurero.
          - [Choice]: salir
          - **Player:** Lo siento, pero no me interesa.
          - **Wyson the gardener:** Bastante bien.
      - [Choice]: Vete.
      - **Player:** Lo siento, pero no me interesa.
      - **Wyson the gardener:** Bastante bien.
  - [Choice]: Pregunte sobre el intercambio por nidos de pájaros.
    - (below|exchange-mole-bits)
  - [Choice]: Pregunta por las hojas de glasto.
    - **Player:** Sí, por favor, necesito hojas de glasto.
    - **Wyson the gardener:** ¿Cuánto estás dispuesto a pagar?
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Qué tal 5 coins?
        - **Player:** ¿Qué tal 5 coins?
        - **Wyson the gardener:** No, no, eso es muy poco. Las hojas de glasto son difíciles de conseguir. Solía ​​tener muchos pero alguien seguía robándomelos.
      - [Choice]: ¿Qué tal 10 coins?
        - **Player:** ¿Qué tal 10 coins?
        - **Wyson the gardener:** No, no, eso es muy poco. Las hojas de glasto son difíciles de conseguir. Solía ​​tener muchos pero alguien seguía robándomelos.
      - [Choice]: ¿Qué tal 15 coins?
        - **Player:** ¿Qué tal 15 coins?
        - **Wyson the gardener:** Mmmm... Está bien, eso suena justo.
        - (removes=15 coins)
        - (receives=woad leaf)
        - **Player:** Gracias.
        - Le compras una hoja de glasto a Wyson.
        - **Wyson the gardener:** Estaré cerca si tienes más necesidades de jardinería.
      - [Choice]: ¿Qué tal 20 coins?
        - **Player:** ¿Qué tal 20 coins?
        - **Wyson the gardener:** Ok, eso es más que justo.
        - **Wyson the gardener:** Toma, toma dos. Eres una persona generosa.
        - (removes=20 coins)
        - (receives=two woad leaves)
        - **Player:** Gracias.
        - Wyson te da un par de hojas de glasto.
      - [Choice]: Dime tu precio.
        - **Player:** Dime tu precio.
        - **Wyson the gardener:** Hmph. El arte del regateo está realmente perdido hoy en día. Bien. 25 coins la pieza.
        - {{AnchorText|How many would you like? (25 coins each)}}
        - ((Después de ingresar una cantidad positiva:))
          - (removes=coins)
          - (receives=woad leaves)
          - **Player:** Gracias.
          - Wyson te da un par de hojas de glasto.
          - Wyson te vende: [número] x Hoja de glasto
  - [Choice]: Pide consejo para luchar contra el topo gigante.
    - **Player:** ¿Podrías darme algún consejo para luchar contra el topo gigante?
    - **Wyson the gardener:** Muy bien. Te daré algunos consejos mientras estás ahí abajo.
  - [Choice]: Vete.
    - **Player:** Lo siento, pero no me interesa.
    - **Wyson the gardener:** Bastante bien.

### {{Anchor|exchange-mole-bits}}Exchange mole bits


#### Sin trocitos de topo

- **Wyson the gardener:** Si consigues garras, pieles o narices de topo de esa bestia gigante de ahí abajo, con gusto las cambiaré por algunos nidos de pájaros.
- **Player:** Está bien, volveré si encuentro alguno.

#### Con trocitos de topo


##### En un mundo gratuito

- Debes estar en un mundo de miembros para utilizar esta función.

##### En el mundo de los miembros, sin las tareas difíciles de Falador completadas

- **Wyson the gardener:** Si no me equivoco, ¡tienes algunos trozos de un topo grande ahí! Los cambiaré por nidos de pájaros, si quieres.
- [Menu]: Elige una opción:
  - [Choice]: cond=If the player has mole claws|Sí, cambiaré las garras de topo.
    - **Player:** Sí, cambiaré las garras de topo.
    - (removes=all mole claws in backpack)
    - (receives=a noted bird nest for each mole claw)
  - [Choice]: cond=If the player has mole skin|Está bien, cambiaré la piel de topo.
    - **Player:** Está bien, cambiaré la piel del topo.
    - (removes=all mole skin in backpack)
    - (receives=a noted bird nest for each mole skin)
  - [Choice]: cond=If the player has mole nose|¿Puedo cambiar la nariz de topo?
    - **Player:** ¿Puedo cambiar la nariz de topo?
    - (removes=all mole noses in backpack)
    - (receives=a noted bird nest for each mole nose)
  - [Choice]: cond=If the player has two types of mole bits|Me gustaría intercambiar ambos.
    - **Player:** Me gustaría intercambiar ambos.
    - (removes=all mole bits in backpack)
    - (receives=a noted bird nest for each mole claw, skin or nose)
  - [Choice]: cond=If the player has all three types of mole bits|Me gustaría cambiar los tres.
    - **Player:** Me gustaría intercambiar los tres.
    - (removes=all mole bits in backpack)
    - (receives=a noted bird nest for each mole claw, skin or nose)
  - [Choice]: En realidad, he cambiado de opinión.
    - (continuea|Talk to)

##### En un mundo de miembros, con las tareas difíciles de Falador completadas

- **Wyson the gardener:** Si no me equivoco, ¡tienes algunos trozos de topo ahí! Los cambiaré por nidos de pájaros, si quieres. También veo que eres portador de escudo; un campeón de Falador, ¿eh? Además, añadiré algunas semillas especiales.
- [Menu]: Elige una opción:
  - [Choice]: cond=If the player has mole claws|Sí, cambiaré las garras de topo.
    - **Player:** Sí, cambiaré las garras de topo.
    - (removes=all mole claws in backpack)
    - (receives=a noted bird nest for each mole claw)
  - [Choice]: cond=If the player has mole skin|Está bien, cambiaré la piel de topo.
    - **Player:** Está bien, cambiaré la piel del topo.
    - (removes=all mole skin in backpack)
    - (receives=a noted bird nest and a white lily seed for each mole skin)
    - **Wyson the gardener:** Si no planeas usar esas semillas, algunos de los otros jardineros pueden estar interesados en ellas.
  - [Choice]: cond=If the player has mole nose|¿Puedo cambiar la nariz de topo?
    - **Player:** ¿Puedo cambiar la nariz de topo?
    - (removes=all mole noses in backpack)
    - (receives=a noted bird nest for each mole nose)
  - [Choice]: cond=If the player has two types of mole bits|Me gustaría intercambiar ambos.
    - **Player:** Me gustaría intercambiar ambos.
    - (removes=all mole bits in backpack)
    - (receives=a noted bird nest for each mole claw, skin or nose, and a white lily seed for each mole skin)
    - (Condition: Si se recibieron semillas de lirio blanco:)
      - **Wyson the gardener:** Si no planeas usar esas semillas, algunos de los otros jardineros pueden estar interesados en ellas.
  - [Choice]: cond=If the player has all three types of mole bits|Me gustaría cambiar los tres.
    - **Player:** Me gustaría intercambiar los tres.
    - (removes=all mole bits in backpack)
    - (receives=a noted bird nest for each mole claw, skin or nose, and a white lily seed for each mole skin)
    - (Condition: Si se recibieron semillas de lirio blanco:)
      - **Wyson the gardener:** Si no planeas usar esas semillas, algunos de los otros jardineros pueden estar interesados en ellas.
  - [Choice]: En realidad, he cambiado de opinión.
    - (continuea|Talk to)

### Buy woad leaves

- (above|How many would you like? (25 coins each))
