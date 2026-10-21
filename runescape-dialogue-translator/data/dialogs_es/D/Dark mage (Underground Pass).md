# Dark mage (Underground Pass)

- **Original Wiki Page**: [Transcript:Dark mage (Underground Pass)](https://runescape.wiki/w/Transcript%3ADark%20mage%20%28Underground%20Pass%29)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In West Ardougne

- **Player:** Hola.
- (Condition: Antes de Underground Pass:)
  - **Dark mage:** ¿Por qué me interrumpes, viajero?
  - (continue)
- (Condition: Después de Underground Pass: esto es un descuido de Jagex)
  - **Dark mage:** Oh, es el liberador de Ardougne. ¿Por qué me interrumpes?
  - (continue)
- **Player:** Me preguntaba ¿qué estás haciendo?
- **Dark mage:** Experimento con magia oscura. Es una embarcación peligrosa.
- (Condition: Con un staff de Iban roto en backpack:)
  - **Player:** ¿Podrías arreglar este staff?
  - **Dark mage:** ¡Todopoderoso Zamorak! ¡El Staff de Iban!
  - **Player:** ¿Puedes arreglarlo?
  - **Dark mage:** Esta es una magia realmente peligrosa, viajero. Puedo arreglarlo, pero te costará. El proceso podría matarme.
  - **Player:** ¿Cuánto?
  - **Dark mage:** 200.000 piezas de oro. Ni un centavo menos.
  - [Menu]: Selecciona una opción
    - [Choice]: Bien entonces.
      - (Condition: Con 200.000 coins:)
        - Le das al mago 200.000 coins y el staff.
        - (removes=200,000 coins and Iban's staff (broken)) (receives=Iban's staff)
        - [El mago repara el staff y te lo devuelve.]
        - **Player:** Gracias. Se lo agradezco.
        - **Dark mage:** ¡Ten cuidado con esa cosa!
      - (Condition: Sin 200.000 coins:)
        - **Player:** ¡Ups! Soy un poco bajo.
        - No puedes permitirte eso.
        - (ventana emergente)
          - {{popup|You can not afford that.|warning=yes}}
    - [Choice]: No hay posibilidad. eso es
      - **Dark mage:** ...Bien por mí.
