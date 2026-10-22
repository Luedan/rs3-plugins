# Sir Rebrum

- **Original Wiki Page**: [Transcript:Sir Rebrum](https://runescape.wiki/w/Transcript%3ASir%20Rebrum)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Sir Rebrum:** ¡Alto, aventurero! ¡No vayas más lejos! ¡Dentro de esta cueva se esconde un peligro mortal y lleno de gusanos!
- [Menu]: Elige una opción:
  - [Choice]: ¿Gusanero?
    - **Sir Rebrum:** ¡Realmente gusano! ¡Los gusanos más desagradables, espantosos y malolientes que puedas imaginar han surgido repentinamente de una red oculta de cuevas subterráneas!
    - **Sir Rebrum:** ¡Pero no temas! ¡Nosotros, los Caballeros Blancos de Falador, hemos sido enviados oficialmente en una misión para hacer frente a esta amenaza deslizante!
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Puedes decirme qué está pasando dentro de esta cueva?
        - **Sir Rebrum:** Bueno, verás, mi unidad fue enviada para asegurar el área después de que los lugareños emitieran una alerta. Aparecieron gusanos gigantes, ¿sabes?
        - **Sir Rebrum:** Rápidamente me uní, hice lo que había que hacer y ahora la gente está a salvo. Hemos contenido con éxito a las criaturas.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Has estado realmente dentro de estas cuevas?
            - **Sir Rebrum:** ¡Por supuesto! ¡Lideramos valientemente una carga hacia el interior, seguida de una retirada táctica inmediata!
            - **Sir Rebrum:** Sin embargo, no confundas esto con huir. Simplemente convoqué una reunión estratégica tras ligeras pérdidas.
            - **Sir Rebrum:** ¡Después de todo, perder el 70% de la fuerza de combate te hace reconsiderar tu situación!
            - (previous2|wormy-options)
          - [Choice]: Gracias por su servicio, Sir Rebrum. Me tengo que ir ahora.
            - **Sir Rebrum:** ¡Adiós!
      - [Choice]: ¿Qué puedes decirme sobre los enemigos que hay dentro?
        - **Sir Rebrum:** ¡Gusanos! Muchos de ellos. Escupen una especie de ácido corrosivo. Podemos encargarnos de los que están cerca de la entrada.
        - **Sir Rebrum:** Sin embargo, si profundizas en las cuevas, empezarás a encontrarte con cuevas más grandes y con mandíbulas. ¡No son ninguna broma!
        - **Sir Rebrum:** Por cierto, nunca llegué al final de las cuevas, así que quién sabe qué hay en el fondo.
        - (previous|wormy-options)
      - [Choice]: Me tengo que ir ahora.
        - **Sir Rebrum:** ¡Adiós!
  - [Choice]: ¿Quién eres tú otra vez?
    - **Sir Rebrum:** Soy el famoso Sir Rebrum: ¡héroe de la justicia extraordinaria y destructor de todo lo malo!
    - **Sir Rebrum:** Sé que te encantaría conocer todas mis aventuras, pero estoy de servicio aquí.
    - (continuea|wormy-options)
  - [Choice]: No te preocupes, como peligro en el desayuno.
    - **Sir Rebrum:** ¡Muy impresionante! Continúe entonces.
  - [Choice]: *(Después de Song from the Depths, si el player ha destruido su ballesta de coral:)* ¿Habrías encontrado una ballesta de coral?
    - **Sir Rebrum:** ¡Sí, sí! The Raptor pasó antes. Dijo que podrías necesitarlo.
    - (Condition: If the player does not have at least one free backpack space:)
      - **Sir Rebrum:** Vuelve cuando estés menos agobiado y te lo daré.
    - (Condition: If the player has at least one free backpack space:)
      - (receives=coral crossbow)
      - [Recibes la ballesta de coral.]
  - [Choice]: *(Después de Song from the Depths, si el player ha destruido el collar de Remora:)* ¿Supongo que no habrás visto un collar tirado por ahí?
    - **Sir Rebrum:** ¡Sí, sí! The Raptor pasó antes. Dijo que podrías necesitarlo.
    - (Condition: If the player does not have at least one free backpack space:)
      - (above|come-back)
    - (Condition: If the player has at least one free backpack space:)
      - (receives=Remora's necklace)
      - [Recibes el collar de la sirena.]
