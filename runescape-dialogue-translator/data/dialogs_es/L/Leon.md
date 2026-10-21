# Leon

- **Original Wiki Page**: [Transcript:Leon](https://runescape.wiki/w/Transcript%3ALeon)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Yanille

- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué es este lugar?
    - **Player:** ¿Qué es este lugar?
    - **Leon:** Este es el emporio Hunter de Aleck. Básicamente, es sólo una tienda con un nombre elegante; Puedes comprar varias armas y trampas aquí.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Puedo comprar algún equipo entonces?
        - **Player:** ¿Puedo comprar algún equipo entonces?
        - **Leon:** Oh, esta no es mi tienda; El dueño es Aleck que está detrás del mostrador.
        - **Leon:** Experimento con diseños de armas. Estoy aquí porque he estado tratando de convencer a la gente para que respalde mi investigación y tal vez venda algunos de mis productos, como este que tengo, en sus tiendas.
        - **Leon:** Sin embargo, Aleck no parece estar interesado.
        - (otro)
      - [Choice]: ¿Puedo intentarlo con tu ballesta?
        - (below|crossbow)
      - [Choice]: ¿Qué es eso que estás sosteniendo?
        - (below|holding)
  - {{anchor|crossbow}}[Elección]: ¿Puedo probar con tu ballesta?
    - **Player:** ¿Puedo probar con tu ballesta?
    - **Leon:** Me temo que, al tratarse de un prototipo, solo tengo unos pocos para mis propios fines de prueba.
    - **Leon:** Por supuesto, por el precio correcto, podría valer la pena hacer otro prototipo.
    - **Player:** ¿Cuánto?
    - **Leon:** Para ti, 1300 piezas de oro.
    - [Menu]: Selecciona una opción
      - [Choice]: Bien, aquí tienes.
        - **Player:** Ok, aquí tienes.
        - (Condition: Sin ningún espacio libre en backpack:)
          - **Leon:** Bueno, pareces un poco sobrecargado en este momento. Quizás deberías liberar algo de espacio para transportarlo primero.
        - (Condition: Sin 1300 coins:)
          - No puedes permitirte eso.
          - **Player:** Oh, en realidad no tengo suficiente dinero conmigo.
        - (Condition: Con espacio backpack y 1300 coins:)
          - (removes=1,300 coins) (receives=Hunters' crossbow)
          - Entregas el dinero y el diseñador del arma te presenta un prototipo de ballesta.
          - **Leon:** Toma, también podrías tomar este. Aleck de allí no parece interesado y te ahorrará la espera.
      - [Choice]: Lo echaré de menos, gracias.
        - **Player:** Lo dejaré pasar, gracias.
        - **Leon:** Tu pérdida; Probablemente se volverán muy valiosos y buscados una vez que convenza a alguien para que los comercialice.
      - {{anchor|bolts}}[Elección]: ¿Utiliza virotes de ballesta normales?
        - **Player:** ¿Utiliza virotes de ballesta normales?
        - **Leon:** Ah, lo admito, como resultado de su er... construcción única, no se necesitan tornillos viejos.
        - **Leon:** Si puedes proporcionarme los materiales y una tarifa simbólica, estaré encantado de hacerte algunos.
        - **Player:** ¿Qué materiales necesitas?
        - **Leon:** Picos de Kebbit. Muchos de ellos. No todos los kebbits tienen púas, eso sí. Tendrás que buscar kebbits espinosos o, mejor aún, kebbits con lomo de cuchillas para obtener material lo suficientemente duro.
        - [Menu]: Selecciona una opción
          - [Choice]: Veamos qué puedes hacer entonces.
            - ''(Se abre la interfaz de Hunting Bolts.)
          - [Choice]: Lo echaré de menos, gracias.
            - **Player:** Lo dejaré pasar, gracias.
            - **Leon:** Bueno, si alguna vez necesitas esa ventaja innovadora, ya sabes a quién contactar.
            - **Player:** Er, sí, por supuesto.
          - [Choice]: ¿No puedo hacer el mío propio?
            - **Player:** ¿No puedo hacer el mío propio?
            - **Leon:** Sí, supongo que podrías, aunque necesitarás mano firme con el cuchillo y el cincel.
            - **Leon:** Los pernos tienen un diámetro inusual, pero básicamente solo necesitarás poder tallar púas de kebbit en ejes rectos.
            - **Player:** Genial; gracias.
  - {{anchor|holding}}[Elección]: ¿Qué tienes ahí?
    - **Player:** ¿Qué sostienes ahí?
    - **Leon:** ¿Esto? Este es un prototipo de un nuevo tipo de ballesta que he estado diseñando.
    - **Player:** Parece bastante extraño.
    - **Leon:** Está bueno, ¿no? Incluye huesos de varios animales en su construcción.
    - **Leon:** También es bastante más rápida que una ballesta normal; Te llevará mucho menos tiempo recargar entre disparos.
    - [Menu]: Selecciona una opción
      - [Choice]: ¡Eso es una locura, nunca funcionará!
        - **Player:** ¡Eso es una locura, nunca funcionará!
        - **Leon:** Eso es lo que también dijeron sobre mis trampas para ratones que funcionan con viento.
        - **Player:** ¿Y funcionaron?
        - **Leon:** Bueno, solo tuvieron problemas porque la gente seguía insistiendo en intentar usarlos en interiores.
      - [Choice]: ¿Podría intentarlo?
        - (above|crossbow)
      - [Choice]: ¿Utiliza virotes de ballesta normales?
        - (above|bolts)
  - [Choice]: cond=With a Hunters' crossbow in backpack|¿Dónde puedo conseguir flechas adecuadas para la ballesta que me vendiste?
    - **Player:** ¿Dónde puedo conseguir pernos adecuados para la ballesta que me vendiste?
    - (continuea|bolts)
