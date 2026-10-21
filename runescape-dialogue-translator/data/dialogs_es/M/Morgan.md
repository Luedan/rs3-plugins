# Morgan

- **Original Wiki Page**: [Transcript:Morgan](https://runescape.wiki/w/Transcript%3AMorgan)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Draynor Village


#### Antes de Vampyre Slayer

- **Morgan:** ¡Alabado sea Saradomin! ¡Él te ha traído aquí para salvarnos a todos!
- **Player:** ¿Qué?
- **Morgan:** ¡Él ha guiado tus pasos hasta mi puerta, para que pueda suplicarte que salves mi aldea de una terrible amenaza!
- [Menu]: Elige una opción:
  - [Choice]: ¿Por qué no salvas tu propia aldea?
    - (ver|Vampyre Slayer)
  - [Choice]: ¿Qué terrible amenaza?
    - (ver|Vampyre Slayer)
  - [Choice]: cond=Historical, only during the Battle of Lumbridge|¿No se está librando una batalla cerca?
    - **Player:** ¿No se está librando una batalla cerca?
    - **Morgan:** Bueno, el propio Saradomin está en el campo de batalla, así que no veo por qué debería preocuparme por mi seguridad. ¡Él nos protegerá!
  - [Choice]: cond=With clay rings in backpack|Te he traído anillos de arcilla.
    - **Player:** Te traje anillos de arcilla.
    - (continue|clayrings)
  - [Choice]: ¿Algo más que pueda hacer por ti?
    - **Player:** ¿Puedo hacer algo más por ti?
    - **Morgan:** En realidad puedes, si tienes alguna habilidad como artesano. He oído que se pueden bendecir anillos de arcilla para defenderse de los enemigos; Me vendrían bien algunos de esos. ¡Compraré tantos como puedas proporcionar!
    - [Menu]: Selecciona una opción
      - [Choice]: Te he traído anillos de arcilla.
        - **Player:** Te traje anillos de arcilla.
          - (Condition: Si el player no tiene anillos de arcilla:)
            - **Morgan:** No, no lo has hecho. Sin embargo, siéntete libre de regresar con uno.
          - (Condition: Si el player tiene un anillo de arcilla:)
            - **Morgan:** Ah, excelente. Nunca se es demasiado cuidadoso, ¿sabes?
            - (removes=clay ring) (receives=10 coins)
            - [Morgan cambia tu anillo por una pequeña pila de coins y lo guarda de forma segura para más adelante.]
          - (Condition: Si el player tiene varios anillos de arcilla:)
            - **Morgan:** Ah, excelente. Nunca se es demasiado cuidadoso, ¿sabes?
            - **Morgan:** ¿Puedo comprar todos los anillos que tienes contigo?
            - [Menu]: Selecciona una opción
              - [Choice]: Sólo uno.
                - (above|one-ring)
              - [Choice]: Todo.
                - (removes=clay rings) (receives=10 coins for each ring)
                - [Morgan cambia tus anillos por una pequeña pila de coins y la guarda de forma segura para más adelante.]
      - [Choice]: Correcto. Bueno, nos vemos.
        - **Player:** Correcto. Bueno, nos vemos.

#### Después de Vampyre Slayer

- **Morgan:** No puedo agradecerte lo suficiente, Player. Mi esposa y yo realmente podemos comenzar una nueva vida aquí en Draynor, ahora que la amenaza del vampyre ha desaparecido.
- [Menu]: Elige una opción:
  - [Choice]: Me alegro de poder ayudar.
    - **Player:** Me alegra poder ayudar.
  - [Choice]: ¡La próxima vez estarás solo!
    - **Player:** ¡La próxima vez estarás solo! No quiero tratar más con vampyres.
    - **Morgan:** Sé que fue una tarea ardua y que nunca podremos recompensarte del todo.
  - [Choice]: cond=Historical, only during the Battle of Lumbridge|¿No se está librando una batalla cerca?
    - (arriba)
  - [Choice]: cond=With clay rings in backpack|Te he traído anillos de arcilla.
    - **Player:** Te traje anillos de arcilla.
    - (continuea|clayrings)
  - [Choice]: ¿Algo más que pueda hacer por ti?
    - **Player:** ¿Puedo hacer algo más por ti?
    - **Morgan:** En realidad puedes, si tienes alguna habilidad como artesano. He oído que se pueden bendecir anillos de arcilla para defenderse de los enemigos; Me vendrían bien algunos de esos. ¡Compraré tantos como puedas proporcionar!
    - **Player:** Pero maté al vampyre... ¿contra qué puedo defenderme?
    - **Morgan:** Esté siempre preparado para lo peor, digo.
    - (continuea|prepared)

#### Opción de anillos de venta

- **Player:** Te traje anillos de arcilla.
- (continuea|clayrings)
