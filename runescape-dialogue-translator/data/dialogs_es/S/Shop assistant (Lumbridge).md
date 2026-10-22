# Shop assistant (Lumbridge)

- **Original Wiki Page**: [Transcript:Shop assistant (Lumbridge)](https://runescape.wiki/w/Transcript%3AShop%20assistant%20%28Lumbridge%29)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Lumbridge

- **Shop assistant:** ¿Puedo ayudarte en algo?
- [Menu]: Selecciona una opción
  - [Choice]: Sí por favor. ¿Qué estás vendiendo?
    - (opens=Lumbridge General Store)
  - [Choice]: ¿Cómo debo utilizar su tienda?
    - **Shop assistant:** ¡Me alegra que lo preguntes! Puede comprar tantos artículos almacenados como desee. También puedes vender la mayoría de los artículos en la tienda.
  - [Choice]: No, gracias.
    - (end)

#### Diálogo histórico

- **Shop assistant:** ¿Puedo ayudarte en algo?
- [Menu]: Selecciona una opción
  - [Choice]: Sí por favor. ¿Qué estás vendiendo?
    - (opens=Lumbridge General Store)
  - [Choice]: ¿Cómo debo utilizar su tienda?
    - (above|howshouldi)
  - [Choice]: ¿Qué pasó con tu edificio?
    - (Condition: During the Battle of Lumbridge:)
      - **Shop assistant:** Sí, tuvimos algunos problemas con la llegada de Zamorak y Saradomin; el piso de arriba está un poco dañado.
      - **Shop assistant:** Pero nos fue mucho mejor que a Hank o Jack, ¡así que estamos agradecidos! Sin embargo, la batalla no es buena para los negocios.
      - **Shop assistant:** Sin embargo, ¡todavía estamos abiertos al público! ¿Quieres ver nuestros productos?
      - (continue|see)
    - (Condition: Before the Lumbridge Rebuildathon:)
      - **Shop assistant:** Sí, sufrimos algunos daños al comienzo de la batalla de Lumbridge. ¡Sin embargo, nos fue mejor que a Hank y Jack!
      - **Shop assistant:** ¡Me alegra que todo esto haya terminado y que podamos volver a reconstruir nuestro negocio! ¿Quieres ver nuestros productos?
      - (continue|see)
    - (Condition: During the Lumbridge Rebuildathon, before rebuilding:)
      - **Shop assistant:** Sí, sufrimos algunos daños al comienzo de la batalla de Lumbridge. Nos fue mejor que a Hank y Jack, ¡aunque Foreman George y su equipo están arreglando sus casas!
      - **Shop assistant:** ¡Pronto nosotros también podremos volver a reconstruir nuestro negocio! ¿Quieres ver nuestros productos?
      - (continue|see)
    - (Condition: During the Lumbridge Rebuildathon, during rebuilding:)
      - **Shop assistant:** Sufrimos algunos daños al comienzo de la batalla de Lumbridge, pero Foreman George y su fantástico equipo están trabajando para solucionarlo. ¡Perdón por el ruido, por cierto!
      - **Shop assistant:** Mientras tanto, todo sigue igual. ¿Quieres ver nuestros productos?
      - (continue|see)
    - (Condition: After the Lumbridge Rebuildathon:)
      - **Shop assistant:** Sufrimos algunos daños al comienzo de la batalla de Lumbridge, pero Foreman George y su equipo hicieron un trabajo fantástico y repararon el daño perfectamente.
      - **Shop assistant:** Ahora que volvemos a estar en funcionamiento, ¿le gustaría ver nuestros productos?
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, por favor.
          - (opens=Lumbridge General Store)
        - [Choice]: ¿Cómo debo utilizar su tienda?
          - (above|howshouldi)
        - [Choice]: No, gracias.
          - (end)
  - [Choice]: No, gracias.
    - (end)
