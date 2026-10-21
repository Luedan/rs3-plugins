# Demon butler

- **Original Wiki Page**: [Transcript:Demon butler](https://runescape.wiki/w/Transcript%3ADemon%20butler)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Servants' Guild

- **Demon butler:** ¡Saludos! ¡Soy Alathazdar, mayordomo de los Demon Lords, y te ofrezco mis servicios por un simple [número] coins!
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué puedes hacer?
    - **Player:** ¿Qué puedes hacer?
    - **Demon butler:** Aprendí mi oficio bajo la dirección de algunos de los maestros más duros de las Dimensiones Demoníacas. Puedo cocinar para satisfacer los estómagos más infernales y volar con alas de fuego para depositar tus cosas en el banco o traer planks del aserradero en segundos.
  - [Choice]: Cuéntame sobre tus trabajos anteriores.
    - **Player:** Cuéntame sobre tus trabajos anteriores.
    - **Demon butler:** Durante milenios he servido y atendido a los poderosos Señores Demonio de las Dimensiones Infernales. Comencé como un humilde lacayo en la casa de Lord Thammaron, y durante varios siglos fui el ayuda de cámara privado de Delrith. También he trabajado en Grim Underworld, escoltando las almas de los muertos hasta sus moradas finales. Pero las incesantes sombras y el fuego del infierno me desconfían, por eso he venido a servir a amos mortales en los reinos de la luz.
  - [Choice]: ¡Estás contratado!
    - **Demon butler:** Tan divertido como dar vueltas a través de sonidos de dimensiones de bolsillo, me quedaré quieto.

#### Diálogo histórico

- **Demon butler:** ¡Saludos! ¡Soy Alathazdar, mayordomo de los Demon Lords, y te ofrezco mis servicios por un simple [número] coins!
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué puedes hacer?
    - (arriba)
  - [Choice]: Cuéntame sobre tus trabajos anteriores.
    - (arriba)
  - [Choice]: ¡Estás contratado!
    - (Condition: Si el player no tiene servidor:)
      - (Condition: Si el player no tiene un segundo dormitorio:)
        - [Necesitas un segundo dormitorio con una cama para que duerma tu sirviente.]
      - **Player:** ¡Estás contratado!
      - (removes=some coins)
      - **Demon butler:** Dedicaré todas mis artes a tu servicio, mi Maestro.
      - (Action: Demon butler desaparece del Gremio de Sirvientes)
    - (Condition: Si el player ya tiene un servidor:)
      - [Ya tienes un sirviente.]

### In a player-owned house

- **Demon butler:** Estoy a tus órdenes, mi maestro.
- [Menu]: Selecciona una opción
  - [Choice]: Ir al banco/aserradero...
    - [Menu]: Selecciona una opción
      - [Choice]: llevar algo al banco
      - **Player:** ¿Puedes llevarme algo al banco?
        - **Demon butler:** Entrégame cualquier artículo y lo llevaré rápidamente al banco, donde estará a salvo de ladrones y daños.
      - [Choice]: Trae algo del banco
        - [Menu]: ¿Qué te gustaría del banco?
          - [Choice]: cond=If previously fetched some items|Recuperar [another/another [amount]] [item name].
            - (abajo)
          - [Choice]: planks de madera.
            - [Ingrese la cantidad: [amount]]
              - (Condition: Si hay suficientes artículos en el banco:)
                - El sirviente va al banco.
                - (Action: Demon butler desaparece de la casa)
                - (Action: Demon butler aparece en la casa.)
                - **Demon butler:** Maestro, he regresado con lo que me pediste que recuperara.
              - (Condition: Si no hay suficiente artículo en el banco:)
                - **Demon butler:** Mi Señor, no puedo conjurar objetos del aire. ¡No tienes ninguno de esos artículos en tu banco!
          - [Choice]: Roble planks.
            - (arriba)
          - [Choice]: Teca planks.
            - (arriba)
          - [Choice]: Más...
            - [Menu]: ¿Qué te gustaría del banco?
              - [Choice]: Caoba planks.
                - (arriba)
              - [Choice]: Arcilla blanda.
                - (arriba)
              - [Choice]: Ladrillo de piedra caliza.
                - (arriba)
              - [Choice]: Barra de acero.
                - (arriba)
              - [Choice]: Más...
                - [Menu]: ¿Qué te gustaría del banco?
                  - [Choice]: Tela.
                    - (arriba)
                  - [Choice]: Pan de oro.
                    - (arriba)
                  - [Choice]: Bloque de mármol.
                    - (arriba)
                  - [Choice]: Magic vivienda de piedra.
                    - (arriba)
                  - [Choice]: Más...
                    - (previous)
      - [Choice]: Lleva algo al aserradero.
        - **Demon butler:** ¡Dame un poco de logs y llegaré al aserradero con poderosas zancadas demoníacas!
  - [Choice]: Varios...
    - [Menu]: Selecciona una opción
      - [Choice]: hacer té
        - **Demon butler:** ¡Probarás el mismísimo té de los Señores Demonio!
        - (Action: Demon butler aparece en la cocina y prepara té.)
        - (Action: Demon butler aparece delante de el player)
        - **Demon butler:** He aquí, tu bebida está completa. ¿Quieres que su oscuro corazón se ablande con la leche de vaca?
        - [Menu]: Selecciona una opción
          - [Choice]: si por favor
            - **Player:** Sí, por favor.
            - (receives=Cup of tea with milk)
          - [Choice]: No gracias
            - **Player:** No, gracias.
            - (receives=Cup of tea)
          - [Choice]: En realidad no quiero ninguno
            - {{Transcript missing}}
      - [Choice]: servir la cena
        - **Demon butler:** ¡Te prepararé un banquete digno de los señores del Pandemonium!
        - **Demon butler:** Mis poderes no se extienden a hacer levitar comida, Maestro. No puedo servir comida a menos que tengas una mesa de comedor.
      - [Choice]: servir bebidas
        - **Player:** Sirva bebidas, por favor.
        - **Demon butler:** ¡Mantendré fluyendo la bebida, Maestro!
        - (Action: Demon butler aparece en la cocina)
        - (Action: Demon butler aparece delante de el player)
        - **Demon butler:** ¿Deseas una bebida, mi Señor?
        - [Menu]: Selecciona una opción
          - [Choice]: si por favor
            - **Player:** ¡Sí, por favor!
            - (receives=a drink)
            - **Demon butler:** ¡Disfruta tu bebida!
          - [Choice]: No gracias
            - **Player:** No, gracias.
          - [Choice]: algo mas
            - (initial)
      - [Choice]: Saludar a los invitados
        - **Player:** Quédese en la entrada y salude a los invitados.
        - **Demon butler:** Sí, Maestro. ¡Difundiré el aura de tu hospitalidad a todos los visitantes!
  - [Choice]: deja de seguirme
    - (end)
  - [Choice]: estas despedido
    - {{Transcript missing}}
