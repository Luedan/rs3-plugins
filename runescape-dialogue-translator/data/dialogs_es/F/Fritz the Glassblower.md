# Fritz the Glassblower

- **Original Wiki Page**: [Transcript:Fritz the Glassblower](https://runescape.wiki/w/Transcript%3AFritz%20the%20Glassblower)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before learning about glassblowing

- **Fritz the Glassblower:** Hola aventurero, bienvenido al horno Entrana.
- **Fritz the Glassblower:** ¿Quieres que te explique mi oficio?
- [Menu]: Selecciona una opción
  - [Choice]: Sí por favor. Me fascinaría escuchar lo que haces.
    - **Player:** Sí, por favor. Me fascinaría escuchar lo que haces.
    - **Fritz the Glassblower:** ¡Me alegra muchísimo escuchar eso! Siempre quise un aprendiz. Déjame explicarte los secretos del soplado de vidrio.
    - {{anchor|glassblowing-tutorial}} **Fritz the Glassblower:** El vidrio está hecho de carbonato de sodio y sílice. Obtenemos nuestra carbonato de sodio recolectando algas de las rocas; las corrientes predominantes hacen que los rincones noreste y suroeste de la isla sean el mejor lugar para encontrarla; también se puede encontrar en
    - **Fritz the Glassblower:** tus redes a veces cuando estás pescando, en la isla Karamja o en la colonia Piscatoris Fishing en las redes de allí. Para convertir las algas en carbonato de sodio, todo lo que necesitas hacer es quemarlas al fuego. Siéntete libre de usar la estufa de mi casa para
    - **Fritz the Glassblower:** eso; es el que está directamente al oeste de aquí. A continuación recogemos arena del arenero que también encontrarás justo al oeste de aquí, hay otros ubicados en Yanille y Shilo Village.
    - (Condition: Si el player no ha recibido un depósito vacío de Fritz the Glassblower:)
      - (Condition: Si el player tiene un depósito vacío:)
        - **Fritz the Glassblower:** Veo que ya tienes un cubo que puedes usar para transportarlo.
        - (continue|bring-the-sand)
      - (Condition: Si el player no tiene un depósito vacío:)
        - **Fritz the Glassblower:** Necesitarás un balde para transportarlo. Te diré una cosa, puedes quedarte con este viejo mío.
        - (receives=empty bucket)
        - (continue|bring-the-sand)
    - (Condition: Si el player ya recibió un depósito vacío de Fritz the Glassblower:)
      - **Fritz the Glassblower:** Puedes usar el cubo que te di antes.
      - (Condition: Si el player tiene un depósito vacío:)
        - (continue|bring-the-sand)
      - (Condition: Si el player no tiene un depósito vacío:)
        - **Player:** Me temo que no tengo ese cubo conmigo. ¿Podrías darme otro, por favor?
        - **Fritz the Glassblower:** ¿Parece que estoy hecho de cubos? Sólo tendrás que comprar otro de un general store.
        - **Fritz the Glassblower:** Y no me interrumpas cuando hablo, es de mala educación. De todos modos, como decía...
        - (continue|bring-the-sand)
    - {{anchor|bring-the-sand}} **Fritz the Glassblower:** Trae la arena y el carbonato de sodio aquí y derrítelos en el horno, y ahí lo tienes: ¡vidrio fundido!
    - **Fritz the Glassblower:** Hay muchas cosas para las que puedes usar el vidrio fundido una vez que lo hayas hecho. Dependiendo de tu talento, puedes intentar convertirlo en algo, como una pecera, por ejemplo. Si quieres probar suerte en el
    - **Fritz the Glassblower:** el fino arte del soplado de vidrio, puedes usar mi pipa de soplado de vidrio de repuesto. Creo que lo dejé en la cómoda de mi casa esta mañana.
    - **Fritz the Glassblower:** Alternativamente, siempre estaré feliz de comprarte el vidrio fundido, así me ahorro tener que tener que hacerlo yo mismo.
    - **Player:** Eso suena bien. ¿Cuánto me pagarás?
    - **Fritz the Glassblower:** Te diré una cosa, como te has interesado en mi arte, te pagaré el precio premium de 20 piezas de oro por cada pieza de vidrio fundido que me traigas.
  - [Choice]: No, gracias, dudo que algún día me dedique al soplado de vidrio.
    - **Player:** No, gracias, dudo que algún día me dedique al soplado de vidrio.
    - **Fritz the Glassblower:** Ok, haz lo que quieras. Hoy en día nadie parece estar interesado en los oficios especializados.
    - **Fritz the Glassblower:** Si cambias de opinión, vuelve y habla conmigo.

### After learning about glassblowing

- **Fritz the Glassblower:** Ah Player, ¿has venido a venderme un poco de vidrio fundido?
- [Menu]: Selecciona una opción
  - [Choice]: Sí.
    - **Player:** Sí.
    - (Condition: Si el player no tiene vidrio fundido:)
      - **Fritz the Glassblower:** Umm, no tiene mucho sentido que intente pagarte por un vaso que no tienes, ¿verdad?
      - **Player:** Bueno, en realidad, si no te importa...
      - **Fritz the Glassblower:** Supongo que nunca has oído hablar de una pregunta retórica. Te lo haré sencillo. Tú traes vidrio, yo pago brillante gold coins.
    - (Condition: Si el player tiene vidrio fundido:)
      - **Fritz the Glassblower:** ¡Fantástico! A ver, por tanto vaso te podría pagar... ... ¡<number> piezas de oro!
      - [Menu]: Selecciona una opción
        - [Choice]: ¿Estás enojado? He corrido por toda la isla para hacer este vaso.
          - **Player:** ¿Estás enojado? He corrido por toda la isla para hacer este vaso.
          - **Fritz the Glassblower:** Lástima. Bueno, puedes encontrarme aquí si cambias de opinión.
        - [Choice]: Claro, parece un precio justo.
          - **Player:** Claro, parece un precio justo.
          - **Fritz the Glassblower:** Aquí estás entonces.
          - (removes=molten glass)
          - (receives=20 coins)
          - **Fritz the Glassblower:** Muchas gracias, Player. Compraré más que traigas.
  - [Choice]: No.
    - **Player:** No.
    - **Fritz the Glassblower:** Ah.
    - **Fritz the Glassblower:** ...errr, bueno, si consigues alguno, estaré encantado de pagarlo. Recuerda, te pagaré 20 piezas de oro por cada trozo de vidrio fundido que me consigas.
    - **Fritz the Glassblower:** Entonces, ¿de qué querías hablarme?
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Podrías decirme cómo volver a hacer vidrio fundido, por favor?
        - **Player:** ¿Podrías decirme cómo volver a hacer vidrio fundido, por favor?
        - **Fritz the Glassblower:** Bueno, estoy muy ocupado en este momento, pero supongo que puedo tomarme 5 minutos libres para mi estudiante favorito.
        - (continuea|glassblowing-tutorial)
      - [Choice]: Sólo pensé en pasar a saludar.
        - **Player:** Sólo pensé en pasar a saludar.
        - **Fritz the Glassblower:** Hola, entonces. Pero me temo que no tengo tiempo para charlar. Los druidas de Taverley han hecho un pedido enorme de viales de vidrio, así que estoy muy ocupado.
