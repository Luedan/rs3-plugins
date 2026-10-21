# Pretzel Bert

- **Original Wiki Page**: [Transcript:Pretzel Bert](https://runescape.wiki/w/Transcript%3APretzel%20Bert)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before the Oktoberfest event

- **Pretzel Bert:** Me estoy preparando ahora mismo, ¿podrías volver más tarde?

### During the Oktoberfest event

- **Pretzel Bert:** ¡Saluda a Dios, joven Herr/Fräulein!
- **Player:** ¿Saludar a Dios? Qué manera más extraña de saludar a alguien.
- **Pretzel Bert:** Es un saludo común del Oktoberfest, amigo mío. No te preocupes, es acogedor. ¿Qué puedo hacer por ti?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Pretzel Bert:** Pretzel Bert, ¡y es un placer conocerte! ¿Quién podrías ser?
    - **Player:** Nombre de Player. Estoy encantado de conocerte también.
    - (previous)
  - [Choice]: ¿Qué estás haciendo aquí?
    - **Player:** ¿Qué haces aquí?
    - **Pretzel Bert:** La Oficina de Turismo de Varrock me ha contratado para vender pretzels y difundir el Oktoberfest. Grundgüttiger, ¡no se me ocurre un trabajo mejor!
    - (previous)
  - [Choice]: ¿Qué es el Oktoberfest?
    - **Player:** ¿Qué es el Oktoberfest?
    - **Pretzel Bert:** El Oktoberfest es un gran festival tradicional en el que se vende una cerveza especial llamada oktoberbrew. También organizamos multitud de eventos en los que cualquiera puede participar.
    - **Pretzel Bert:** Lo mejor es consultar los foros si quieres información sobre cómo participar.
    - (previous)
  - [Choice]: Más...
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Cómo empezó el Oktoberfest?
        - **Player:** ¿Cómo empezó el Oktoberfest?
        - **Pretzel Bert:** El Oktoberfest tiene siglos de tradición a sus espaldas. Los festivales de la cerveza siempre se han celebrado en esta época del año, por lo que la cerveza se puede beber antes de que comience la nueva temporada de elaboración.
        - **Pretzel Bert:** El Oktoberfest se basa en un festival que originalmente se celebraba para la boda de la reina Teresa y el rey Luis, regentes ancestrales de mi pueblo.
        - (previous)
      - [Choice]: ¿Puedo comprar un pretzel?
        - **Player:** ¿Puedo comprar un pretzel?
        - **Pretzel Bert:** ¡Por supuesto! Cuestan 1 po cada uno. ¿Cuantos quisieras?
        - {{Tinput|Enter amount:}}
          - (Condition: Si intenta comprar no más de 24 pretzels:)
            - **Pretzel Bert:** ¡X pretzels! Ese será Xgp, por favor.
              - [Menu]: Selecciona una opción
                - [Choice]: Está bien.
                  - **Player:** ¡Está bien!
                    - (Condition: Sin suficiente espacio backpack:)
                      - **Player:** Oh, parece que no tengo suficiente espacio en mi bolso. Tendré que volver.
                      - **Pretzel Bert:** ¡Vuelve pronto, antes de que se enfríen!
                    - (Condition: Con suficiente espacio backpack:)
                      - **Pretzel Bert:** ¡Cuidado! Son picantes y muy, muy sabrosos.
                      - ((Player recibe X pretzels. X coins se elimina de el player.))
                    - (Condition: Sin suficiente dinero:)
                      - {{Transcript missing}}
                - [Choice]: Eso es más de lo que pensaba. No, gracias.
                  - {{Transcript missing}}
          - (Condition: Si intenta comprar más de 24 pretzels:)
            - **Pretzel Bert:** ¿Cuántos pretzels? Están muy buenos, ¡pero no creo que puedas comer tantos!
      - [Choice]: ¿Te das cuenta de lo tonto que pareces?
        - **Player:** ¿Te das cuenta de lo tonto que pareces?
        - **Pretzel Bert:** ¡Du geh! ¡Cuidado con no tirarte de las orejas tanto que puedas colgar pretzels de ellas!
        - (previous)
      - [Choice]: Atrás.
        - (initial)
