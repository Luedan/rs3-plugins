# Herald of Varrock

- **Original Wiki Page**: [Transcript:Herald of Varrock](https://runescape.wiki/w/Transcript%3AHerald%20of%20Varrock)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Herald of Varrock:** Bienvenido a Varrock, mi [fine fellow/good lady]. ¿Cómo puedo ser de utilidad?
- **Player:** Hola; un placer conocerte. ¿Qué haces aquí?
- **Herald of Varrock:** Me alegra que lo hayas preguntado, porque tengo el gran honor de ser el heraldo de Varrock.
- **Herald of Varrock:** Es mi deber solemne defender y mantener los estándares y prácticas de la corte real, ya sean eventos reales o capas de heraldo.
- ((If you don't have a Varrock herald cape:))
  - **Player:** ¿Capa Herald? ¿Qué es eso?
  - **Herald of Varrock:** ¡No hay nada más preciado y buscado que una capa de heraldo Varrock! Otorgado sólo a aquellos en quienes se confía para mantener el honor y el deber de Varrock, alguien como usted, por supuesto.
  - **Herald of Varrock:** ¡Incluso puedes personalizar la capa si tus hazañas dentro del reino han sido de ayuda para la ciudad!
  - **Herald of Varrock:** ¿Te importaría llevarte una de estas finas capas?
  - **¿Aceptas esta capa de heraldo Varrock?**
    - si
      - **Player:** ¡Claro, lo aceptaré!
      - **Herald of Varrock:** ¡Excelente! Echemos un vistazo a las personalizaciones que podemos hacer...
      - (opens=Customisation)
    - No
      - **Player:** No, gracias.
      - **Herald of Varrock:** Como desees. Estaré aquí si vuelves en sí.
- ((If you have a Varrock herald cape:))
  - **Player:** Oh, ya tengo uno de esos.
  - **Herald of Varrock:** ¡Por supuesto que sí! Y debo agregar que no hay ninguno mejor en todo el país. ¿Quizás te gustaría personalizar aún más tu capa?
  - **¿Personalizar tu capa de heraldo Varrock?**
    - si
      - (opens=Customisation)
    - No
      - (end)
- ((If you have a herald cape from another city:))
  - **Player:** Aunque ya tengo una capa de heraldo de otra ciudad.
  - **Herald of Varrock:** Bastante. Veo que otras ciudades están, nuevamente, siguiendo los audaces pasos de Varrock.
  - **Herald of Varrock:** ¿No puedo interesarte por el honor de esta capa de heraldo de Varrock?
  - **¿Cambiar tu capa de heraldo a Varrock?**
    - si
      - **Player:** ¡Claro, lo aceptaré!
      - **Herald of Varrock:** ¡Excelente! Echemos un vistazo a las personalizaciones que podemos hacer...
      - (opens=Customisation)
    - No
      - **Player:** No gracias, me quedaré con la capa que tengo.
      - **Herald of Varrock:** Dios mío; tiempos tan tristes en los que vivimos. Estaré aquí si vuelves en sí.

### Customise

- ((If you're not affiliated with Varrock:))
  - **Herald of Varrock:** Me temo que esa capa de heraldo no sirve, solo puedo dejarte cambiar una capa de heraldo Varrock aquí. ¿Quieres cambiarte a una capa de heraldo Varrock?
  - **¿Cambiar a capa de heraldo Varrock?**
    - si
      - (continue|Affiliated)
    - No
      - (end)
- ((If you are affiliated with Varrock:))
  - **Herald of Varrock:** ¡Excelente! Echemos un vistazo a las personalizaciones que podemos hacer...
  - (opens=Customisation)
