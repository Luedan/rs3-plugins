# Hirko

- **Original Wiki Page**: [Transcript:Hirko](https://runescape.wiki/w/Transcript%3AHirko)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Keldagrim marketplace


#### Hablando con Hirko

- **Hirko:** ¡Hola!
- **Player:** Hola, ¿qué hay en esas cajas?
- **Hirko:** Ajá, ¿estás interesado en mis ballestas, verdad?
- **Player:** ¿Son buenos?
- **Hirko:** Son ingeniería enana en su máxima expresión. Si tienes suficiente habilidad en artesanía, forja y emplumado, incluso puedes hacerlos tú mismo. Puedes comprar algunas de las piezas aquí y hacer el resto tú mismo.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Cómo hago uno para mí?
    - **Player:** ¿Cómo hago uno para mí?
    - **Hirko:** Bueno, primero tendrás que cortar un poco de madera y luego usar un cuchillo en la madera para tallar una buena culata de ballesta como estas aquí.
    - **Player:** Madera emplumada en stock... comprobar.
    - **Hirko:** Luego, consigue algo de metal y un martillo y forja algunas extremidades para el arco. Ten en cuenta que utilizas los metales y las maderas adecuados, ya que algunas maderas son demasiado livianas para usarlas con otros metales y viceversa.
    - **Player:** ¿Cuál va con cuál?
    - **Hirko:** Madera y Bronce como materiales básicos, Roble y Blurita, Sauce y Hierro, Acero y Teca, Mithril y Arce, Adamante y Caoba y finalmente Runa y Tejo.
    - **Player:** Ok, ya tengo mis acciones y un par de extremidades... ¿y ahora qué?
    - **Hirko:** Simplemente toma un martillo y golpea las extremidades firmemente contra la culata. Luego necesitarás una cuerda, solo que no son iguales que los arcos normales. Necesitarás secar la carne de algún animal grande para obtener tendones y luego girarla en una rueca; es lo único que hemos encontrado que es lo suficientemente fuerte como para una ballesta.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué pasa con magic logs?
        - **Player:** ¿Qué pasa con magic logs?
        - **Hirko:** Bueno... no lo sé muy bien... nosotros los enanos no trabajamos con magia, preferimos el oro y la roca. Mucho más estable. Supongo que podrías preguntarles a los humanos del gremio de guardabosques para ver si pueden hacer algo, ¡pero no quiero tener nada que ver con eso!
        - **Player:** Gracias por decírmelo. ¡Adiós!
        - (continue|thanks)
      - [Choice]: Gracias por decírmelo. ¡Adiós!
        - (below|thanks)
  - [Choice]: ¿Qué pasa con la munición?
    - **Player:** ¿Qué pasa con la munición?
    - **Hirko:** Puedes fabricar muchos tornillos diferentes, aunque no olvides volarlos con plumas como lo haces con las flechas. También existe la opción de inclinar cualquier perno sin punta con gemas y luego encantarlo con runas. Esto puede tener algunos efectos bastante poderosos.
    - **Player:** ¡Oh, pobre banco mío! ¿Cómo guardaré todo eso?
    - **Hirko:** No te preocupes, aquí tengo justo lo que necesitas: una bolsa para virotes diseñada especialmente para guardar 4 tipos diferentes de virotes de ballesta.
    - **Player:** Vaya, ¿cuánto?
    - (Condition: Si el player aún no posee una bolsa de cerrojo:)
      - **Hirko:** Bueno, veamos ahora... ¿para ti? 1500 piezas de oro deberían ser suficientes.
      - [Menu]: ¿Quieres comprar una bolsa?
        - [Choice]: Sí, pagaré los 1500 gp.
          - **Player:** Sí, pagaré los 1500 po.
          - **Hirko:** Entrégalo entonces.
          - (Condition: Si el player no tiene suficiente dinero:)
            - **Player:** Oh, no tengo tanto encima.
            - **Hirko:** Entonces será mejor que vayas a ganar algo de dinero, no debería llevarte mucho tiempo.
          - (Condition: Si el player tiene suficiente dinero:)
            - (removes=1,500 coins) (receives=a bolt pouch)
            - [Entregas tu oro y recibes una bolsa de cuero bien hecha.]
        - [Choice]: Gracias por decírmelo. ¡Adiós!
          - (below|thanks)
    - (Condition: De lo contrario:)
      - **Hirko:** Hmm... ¿no te vi aquí abajo comprando uno el otro día? Me temo que sólo puedes tener uno a la vez.
  - [Choice]: Gracias por decírmelo. ¡Adiós!
    - {{anchor|thanks}} **Player:** Gracias por decírmelo. ¡Adiós!
    - **Hirko:** Cuídate, dispara directo.

#### Ser atrapado mientras intentaba robar en su puesto

- **Hirko:** {{RSChat|Hey! Get your hands off there!}}

#### Intercambiar o hablar con él después de robar en su puesto

- **Hirko:** {{RSChat|Halt, thief!}}
- **Hirko:** {{RSChat|Guards, catch that thief!}}
