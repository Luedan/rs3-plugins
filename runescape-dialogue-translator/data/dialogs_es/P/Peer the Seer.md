# Peer the Seer

- **Original Wiki Page**: [Transcript:Peer the Seer](https://runescape.wiki/w/Transcript%3APeer%20the%20Seer)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before The Fremennik Trials


#### Hablando con él

- **Peer the Seer:** Uuuh... ¿Qué fue esa presencia oscura que sentí?
- **Peer the Seer:** !
- **Peer the Seer:** Ejem, lo siento.
- (Condition: Si el player ha completado los logros fáciles de Fremennik:)
  - [Menu]: ¿Sobre qué te gustaría preguntar?
    - [Choice]: Servicio de deposito
      - **Player:** Hola, compañero. ¿Podrías depositar algunas cosas por mí, por favor?
      - **Peer the Seer:** Te lo agradeceré, pero me duele que todavía seas un extranjero.
      - (Action: Se abre la interfaz de depósitos de Peer the Seer.)
    - [Choice]: Los juicios de Fremennik
      - **Peer the Seer:** No tengo ningún interés en hablar contigo ahora, outsider.
- (Condition: Si el player no ha completado los logros fáciles de Fremennik:)
  - **Peer the Seer:** No tengo ningún interés en hablar contigo ahora, outsider.

#### Opción de depósito

- (Condition: Si el player ha completado los logros fáciles de Fremennik:)
  - (Action: Se abre la interfaz de depósitos de Peer the Seer.)
- (Condition: Si el player no ha completado los logros fáciles de Fremennik:)
  - **Peer the Seer:** ¡No me molestes, extranjero! ¡Solo depositaré artículos en los bancos de aquellos que hayan ganado Fremennik sea boots!

#### Intentando abrir la puerta de su casa.

- **Peer the Seer:** ¡Oye! ¡Exterior! ¡Esa es mi casa! ¿Quién te crees que eres para irrumpir en mi casa sin preguntar?
- **Player:** Um... Mi nombre es Player.
- **Peer the Seer:** Fue una pregunta retórica, outsider. Ahora piérdete. No aprecio los intrusos en mi casa.

### After The Fremennik Trials


#### Hablando con él

- **Peer the Seer:** Uuuh... ¿Qué fue esa presencia oscura que sentí?
- **Peer the Seer:** !
- **Peer the Seer:** Ejem, lo siento.
- [Menu]: ¿Sobre qué te gustaría preguntar?
  - (Condition: Si el player ha completado los logros fáciles de Fremennik:)
    - [Choice]: Servicio de deposito
      - **Player:** Hola, compañero. ¿Podrías depositar algunas cosas por mí, por favor?
      - **Peer the Seer:** Por supuesto, [Fremennik name]. Siempre estaré feliz de ayudar a aquellos que se han ganado el derecho a usar Fremennik sea boots.
      - (Action: Se abre la interfaz de depósitos de Peer the Seer.)
  - (Condition: Si el player tiene al menos una pieza de cráneo, caja torácica o peroné en su inventario:)
    - [Choice]: Armadura de hueso Wallasalki
      - **Player:** Hola. Tengo algunos fragmentos de hueso de wallasalki y tengo entendido que es posible que puedas usarlos para hacerme una armadura...
      - **Peer the Seer:** Como quieras, [Fremennik name]. ¿En qué tipo de armadura estabas pensando exactamente?
      - [Menu]: Selecciona una opción
        - [Choice]: Un buen timón
          - **Peer the Seer:** Me temo que te costará 5000 coins hacerlo para ti... ¿Te parece bien?
          - [Menu]: Selecciona una opción
            - [Choice]: SI
              - ((Si el player no cuenta con los materiales requeridos:))
                - **Peer the Seer:** Mis disculpas [Fremennik name], pero necesitaré que me traigas 1 trozo de piel de boca de daga oscura, 1 trozo de calavera y 5000 coins antes de poder hacerte este yelmo.
                - (end)
              - (removes=1 dagannoth hide, 1 skull piece, and 5,000 coins) (receives=a skeletal helm)
              - **Peer the Seer:** ¡Ah, un yelmo que enorgullecería a cualquier vidente! ¿Quieres que te haga otro mientras lo hago?
              - (continuea|skelehelm)
            - [Choice]: NO
              - (continuea|armour)
        - [Choice]: Armadura resistente
          - **Peer the Seer:** Me temo que te costará 10 000 coins hacerlo para ti... ¿Te parece bien?
          - Seleccione una opción
            - [Choice]: SI
              - ((Si el player no cuenta con los materiales requeridos:))
                - **Peer the Seer:** Lo siento [Fremennik name], pero necesito 3 piezas de piel de boca de daga oscura, 1 pieza de caja torácica y 10,000 coins para hacerte esta armadura...
                - (end)
              - (removes=3 dagannoth hides, 1 ribcage piece, and 10,000 coins) (receives=a skeletal top)
              - **Peer the Seer:** ¡Todos los videntes de la leyenda llevaban esa armadura! ¿Quieres que te haga otra pieza?
              - (continuea|skeletop)
            - [Choice]: NO
              - (continuea|armour)
        - [Choice]: Potente armadura para las piernas
          - **Peer the Seer:** Me temo que te costará 7.500 coins hacerlo para ti... ¿Te parece bien?
          - [Menu]: Selecciona una opción
            - [Choice]: SI
              - ((Si el player no cuenta con los materiales requeridos:))
                - **Peer the Seer:** Lo siento mucho [Fremennik name], pero necesitaré 2 piezas de piel de boca de daga oscura, 1 pieza de peroné y 7500 coins para hacer este tipo de armadura para las piernas.
                - (end)
              - (removes=2 dagannoth hides, 1 fibula piece, and 7,500 coins) (receives=a skeletal bottoms)
              - **Peer the Seer:** Ah, solía usar esa pieza de armadura para luchar en mi juventud... ¿Quieres que te haga otro par de piernas mientras lo hago de todos modos?
              - (continuea|skeleleg)
            - [Choice]: NO
              - (continuea|armour)
        - [Choice]: nada
          - **Player:** En realidad, no quiero nada.
          - **Peer the Seer:** {{Sic|AS}} que desees.
  - [Choice]: Los juicios de Fremennik
    - **Player:** Hola compañero.
    - **Peer the Seer:** ¡Saludos a ti, [brother/sister] [Fremennik name]! ¿Qué te trae a verme de nuevo?
    - [Menu]: Elige una opción:
      - [Choice]: ¿Puedes decir mi futuro?
        - **Player:** Me preguntaba si podrías darme una lectura sobre mi futuro...
        - **Peer the Seer:** Ah, ¿te gustaría una predicción? No veo que eso sea tan difícil... espera un momento...
        - *(Se da una de las siguientes predicciones y la palabra seleccionada dentro de [] se elige aleatoriamente :)*
          - *(Predicción 1 :)*
            - **Peer the Seer:** Aquí está tu predicción: Hoy encontrarás suerte con el número [one/two/three/four/five/six/seven/eight/nine/ten].
          - *(Predicción 2 :)*
            - **Peer the Seer:** Aquí está tu predicción: El color [black/blue/brown/cyan/green/pink/purple/red/yellow] te traerá suerte este día.
          - *(Predicción 3 :)*
            - **Peer the Seer:** Aquí está tu predicción: El enemigo llamado [fire giant/ghosts/giant/goblin/green dragon/hobgoblin/lesser demon/moss giant/ogre/zombie] es tu tótem de la suerte este día.
          - *(Predicción 4 :)*
            - **Peer the Seer:** Aquí está tu predicción: Merecerá la pena visitar el lugar llamado [Al Kharid/Ardougne/Burthorpe/Canifis/Catherby/Falador/Karamja/Varrock/The Wilderness/Yanille].
          - *(Predicción 5 :)*
            - **Peer the Seer:** Aquí está tu predicción: Las estrellas me dicen que hoy deberías usar un [battleaxe/crossbow/dagger/javelin/long sword/mace/scimitar/short sword/spear/warhammer] en combate.
          - *(Predicción 6 :)*
            - **Peer the Seer:** Aquí está tu predicción: sería prudente entrenar la habilidad [Agility/Cooking/Crafting/Fishing/Fletching/Herblore/Mining/Runecrafting/Smithing/Thieving] hoy.
      - [Choice]: Nada realmente.
        - **Player:** Nada realmente, solo pasé a saludar.
        - **Peer the Seer:** Bueno, ¡hola a ti también!
