# Fancy-dress shop owner

- **Original Wiki Page**: [Transcript:Fancy-dress shop owner](https://runescape.wiki/w/Transcript%3AFancy-dress%20shop%20owner)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Fancy-dress shop owner:** Ahora pareces alguien que va a muchas fiestas de disfraces.
- **Player:** Errr... ¿qué estás diciendo exactamente?
- **Fancy-dress shop owner:** Sólo digo que quizás te gustaría examinar mi selección de prendas.
- **Fancy-dress shop owner:** O, si eso no te interesa, ¿quizás tengas algo más que ofrecer? Siempre estoy buscando materiales nuevos, interesantes o inusuales.
- [Menu]: Selecciona una opción
  - [Choice]: Bien, entonces veamos qué tienes.
    - **Player:** Bien, entonces veamos qué tienes.
    - (opens=Fancy Clothes Store)
  - [Choice]: *(Después de Eagles' Peak:)* ¿Podrías hacerme otro disfraz de pájaro?
    - **Player:** ¿Podrías hacerme otro disfraz de águila?
    - **Fancy-dress shop owner:** Por supuesto, si puedes proporcionar los materiales. Necesitaré plumas apropiadas, alquitrán de pantano y algo de yellow dye. También te costará 25 piezas de oro.
    - (Condition: If the player does not have the required items:)
      - **Player:** Veré qué puedo hacer.
    - (Condition: If the player has the required items:)
      - [Menu]: Selecciona una opción
        - [Choice]: Bien, aquí están los materiales. Águilame.
          - **Player:** Bien, aquí están los materiales. Águilame.
          - (Condition: If the player has less than 25 coins:)
            - **Player:** Me temo que no tengo tanto dinero conmigo.
            - No puedes permitirte eso.
          - (Condition: If the player has 25 coins:)
            - (removes=10 eagle feathers, yellow dye, swamp tar and 25 coins) (receives=eagle cape and fake beak)
            - **Fancy-dress shop owner:** Ahí vamos, un disfraz de águila. Deberías ser la envidia de todo el grupo usando eso.
            - **Player:** Gracias.
        - [Choice]: Pensándolo bien, eso es demasiado caro.
          - **Player:** Pensándolo bien, eso es demasiado caro.
          - **Fancy-dress shop owner:** Bueno, no dudes en volver si cambias de opinión.
  - [Choice]: Creo que podría dejar la lectura por ahora, gracias.
    - **Player:** Creo que podría dejar la lectura por ahora, gracias.
  - [Choice]: *(Si no tienes pieles adecuadas en tu inventario:)* ¿Puedes hacer ropa adecuada para cazar?
    - **Player:** ¿Puedes hacer ropa adecuada para cazar?
    - **Fancy-dress shop owner:** Por supuesto. Echa un vistazo a mi gama de artículos hechos a medida. Si puedes proporcionarme las pieles, con mucho gusto te haré cualquiera de estas.
    - (opens=Custom Fur Clothing)
  - [Choice]: *(Si tienes pelaje en tu inventario:)* ¿Podrías hacer algo con este pelaje que obtuve cazando?
    - **Player:** ¿Podrías hacer algo con este pelaje que obtuve cazando?
    - **Fancy-dress shop owner:** Por supuesto. Echa un vistazo a mi gama de artículos hechos a medida. Si puedes proporcionarme las pieles, con mucho gusto te haré cualquiera de estas.
    - (opens=Custom Fur Clothing)
  - [Choice]: ¿Qué tipo de materiales inusuales tenías en mente?
    - **Player:** ¿Qué tipo de materiales inusuales tenías en mente?
    - **Fancy-dress shop owner:** Bueno, algunas plumas más coloridas podrían ser útiles. Por alguna razón surrealista, lo único que normalmente me ofrecen son grandes cantidades de plumas de pollo de aspecto bastante desgastado.
    - **Fancy-dress shop owner:** La gente debe tener pasatiempos muy extraños por estos lares, eso es todo lo que puedo decir.
    - **Player:** Ok, veamos qué tienes entonces.
    - (opens=Fancy Clothes Store)
