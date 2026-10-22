# Shopkeeper (Lumbridge)

- **Original Wiki Page**: [Transcript:Shopkeeper (Lumbridge)](https://runescape.wiki/w/Transcript%3AShopkeeper%20%28Lumbridge%29)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{External|os=Transcript:Shop keeper|rsc=Shopkeeper/Dialogue}}

### In Lumbridge


#### Con un construction contract

- **Shopkeeper:** ¿Puedo ayudarte en algo?
- [Menu]: Selecciona una opción
  - [Choice]: Preguntar por contracts
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué necesitas reparar?
        - **Shopkeeper:** Déjame ver, ahora mismo necesito que repares el siguiente pieces of furniture.
        - ((Only the unrepaired out of the following are listed:))
          - **Shopkeeper:** [Furniture 1], [Furniture 2], [Furniture 3], [Furniture 4], [Furniture 5]
        - (previous)
      - [Choice]: ¿Qué materiales necesito?
        - ((Only the materials still required for repairs are listed in the following:))
          - **Shopkeeper:** Necesitas: Planks x [número], Steel nails x [número], [Additional material] x [número]
        - (previous)
      - [Choice]: [Leave]
        - (end)
  - [Choice]: pregunta sobre otra cosa
    - (below|standard)

#### Diálogo estándar

- **Shopkeeper:** ¿Puedo ayudarte en algo?
- [Menu]: Selecciona una opción
  - [Choice]: Sí por favor. ¿Qué estás vendiendo?
    - (opens=Lumbridge General Store)
  - [Choice]: ¿Cómo debo utilizar su tienda?
    - **Shopkeeper:** ¡Me alegra que lo preguntes! La tienda tiene dos secciones: 'Stock principal' y 'Artículos de muestra gratuitos'.
    - **Shopkeeper:** Desde 'Stock principal' puedes comprar tantos artículos en stock como desees. También ofrezco muestras gratuitas para ayudarle a comenzar y hacer que regrese. Una vez que tomes una muestra gratis, no te daré otra hasta dentro de media hora. ¡No estoy hecho de dinero, sabes!
    - **Shopkeeper:** También puedes vender la mayoría de los artículos en la tienda.
    - **Player:** Gracias.
  - [Choice]: No, gracias.
    - (end)

#### Diálogo histórico

- **Shopkeeper:** ¿Puedo ayudarte en algo?
- [Menu]: Selecciona una opción
  - [Choice]: Sí por favor. ¿Qué estás vendiendo?
    - (opens=Lumbridge General Store)
  - [Choice]: ¿Cómo debo utilizar su tienda?
    - (above|howshouldi)
  - [Choice]: ¿Qué pasó con tu edificio?
    - (Condition: During the Battle of Lumbridge:)
      - **Shopkeeper:** Sí, tuvimos algunos problemas con la llegada de Zamorak y Saradomin; el piso de arriba está un poco dañado.
      - **Shopkeeper:** Pero nos fue mucho mejor que a Hank o Jack, ¡así que estamos agradecidos! Sin embargo, la batalla no es buena para los negocios.
      - **Shopkeeper:** Sin embargo, ¡todavía estamos abiertos al público! ¿Quieres ver nuestros productos?
      - (continue|see)
    - (Condition: Before the Lumbridge Rebuildathon:)
      - **Shopkeeper:** Sí, sufrimos algunos daños al comienzo de la batalla de Lumbridge. ¡Sin embargo, nos fue mejor que a Hank y Jack!
      - **Shopkeeper:** ¡Me alegra que todo esto haya terminado y que podamos volver a reconstruir nuestro negocio! ¿Quieres ver nuestros productos?
      - (continue|see)
    - (Condition: During the Lumbridge Rebuildathon, before rebuilding:)
      - **Shopkeeper:** Sí, sufrimos algunos daños al comienzo de la batalla de Lumbridge. Nos fue mejor que a Hank y Jack, ¡aunque Foreman George y su equipo están arreglando sus casas!
      - **Shopkeeper:** ¡Pronto nosotros también podremos volver a reconstruir nuestro negocio! ¿Quieres ver nuestros productos?
      - (continue|see)
    - (Condition: During the Lumbridge Rebuildathon, during rebuilding:)
      - **Shopkeeper:** Sufrimos algunos daños al comienzo de la batalla de Lumbridge, pero Foreman George y su fantástico equipo están trabajando para solucionarlo. ¡Perdón por el ruido, por cierto!
      - **Shopkeeper:** Mientras tanto, todo sigue igual. ¿Quieres ver nuestros productos?
      - (continue|see)
    - (Condition: After the Lumbridge Rebuildathon:)
      - **Shopkeeper:** Sufrimos algunos daños al comienzo de la batalla de Lumbridge, ¡pero Foreman George y su equipo hicieron un trabajo fantástico y repararon el daño perfectamente!
      - **Shopkeeper:** Ahora que volvemos a estar en funcionamiento, ¿le gustaría ver nuestros productos?
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, por favor.
          - (opens=Lumbridge General Store)
        - [Choice]: ¿Cómo debo utilizar su tienda?
          - **Shopkeeper:** ¡Me alegra que lo preguntes! Puede comprar tantos artículos almacenados como desee. También puedes vender la mayoría de los artículos en la tienda.
        - [Choice]: No, gracias.
          - (end)
  - [Choice]: No, gracias.
    - (end)
