# Doric

- **Original Wiki Page**: [Transcript:Doric](https://runescape.wiki/w/Transcript%3ADoric)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### North of Falador


#### Antes de que lo mío sea tuyo


##### Primera vez hablando con Doric

- [What's Mine is Yours está completamente interpretado por voz y presenta música y efectos atmosféricos. Le sugerimos que active el sonido para aprovecharlo al máximo.]
- **Doric:** Se acabó, se acabó...
- **Player:** ¿Estás bien? ¿Qué ha terminado?
- **Doric:** Mi negocio, mi vida... ¡todo! Está todo en ruinas.
- **Player:** Cálmate y cuéntame qué pasó.
- **Doric:** Nurmof debería haber enviado su pedido de picos esta semana, pero no he oído nada. Ha sido mi cliente más leal durante años y no es el único que deja de hacerlo. ¡Estoy arruinado!
- [Menu]: Selecciona una opción
  - [Choice]: No te preocupes, te ayudaré.
    - (Condition: Without 5 Smithing:)
      - **Doric:** Quizás deberías adquirir más experiencia primero. Me encantaría recibir ayuda, pero necesito a alguien que pueda ayudarme si vamos a hacer esto.
      - [Esta misión requiere el nivel 5 Smithing.]
    - (Condition: With 5 Smithing:)
      - (ver|Lo que es mío es tuyo)
  - [Choice]: Estoy demasiado ocupado para ayudar ahora.
    - **Doric:** No te preocupes aventurero, tú sigue con tus asuntos. No espero que nadie se esfuerce por mí.
    - **Doric:** Adiós aventurero.
  - [Choice]: Quería usar tu yunque.
    - **Doric:** Tengo problemas mayores que permitir que aventureros aleatorios usen mi yunque en este momento. Si me ayudas, tal vez pueda permitirte trabajar con él en ese momento.
    - [Menu]: Selecciona una opción
      - [Choice]: Yo te ayudaré.
        - (above|doric-accept-quest)
      - [Choice]: Estoy demasiado ocupado ahora.
        - (above|doric-too-busy)
  - [Choice]: ¿Tiene algún consejo para los aspirantes a aventureros?
    - **Player:** ¿Tienes algún consejo para los aspirantes a aventureros?
    - **Doric:** Sí, sé sobre aventuras, jovencito.
    - **Doric:** ¡Luché contra Kinshra junto a Kara-Meir y la acompañé a las tierras oscuras de Morytania!
    - **Player:** ¿Joven?
    - **Doric:** Todos ustedes, los humanos, son jóvenes para mí.
    - **Player:** Supongo que es cierto. Cuéntame más sobre Kara-Meir y Falador.
    - **Doric:** Kara rompió el asedio de Kinshra y desafió a su líder. Pero el costo fue alto.
    - **Player:** ¿Qué pasa con Morytania?
    - **Doric:** Esa es una historia oscura. ¿Cómo podría alguno de nosotros haber adivinado la verdad sobre Gar'rth?
    - **Player:** ¡Cuéntame más!
    - **Doric:** No, no todas las aventuras terminan bien. Reldo, el bibliotecario de Varrock, podría estar dispuesto a contarle más.

##### Hablando con Doric nuevamente antes de aceptar la misión

- **Doric:** ¿De nuevo, aventurero? Lamentablemente, el negocio no pinta mejor que la última vez que hablamos.
- (continuea|starting)

#### Después de lo mío es tuyo

- **Doric:** Hola viajero, ¿qué te trae por mi humilde herrería?
- [Menu]: Elige una opción:
  - [Choice]: ¿Tienes más tareas de Smithing para mí?
    - (ver|tareas Doric y Boric)
  - [Choice]: cond=If either the Gofannon amulet, task list or wizard's diary has been lost|Perdí un artículo que me diste.
    - (Condition: If only one item has been lost:)
      - (Condition: Without space in backpack:)
        - **Doric:** Sin embargo, no tienes espacio para guardarlo. Vuelve conmigo una vez que tengas espacio.
      - (Condition: With space in backpack:)
        - (receives=Gofannon amulet, task list or wizard's diary)
        - **Doric:** Afortunadamente, uno de nuestros trabajadores lo encontró. Ten más cuidado la próxima vez.
      - (Condition: If two or more items have been lost:)
        - **Doric:** ¿Qué artículo querías recuperar?
        - [Menu]: Elige una opción:
          - [Choice]: Amuleto de Gofannon
            - (above|careful)
          - [Choice]: lista de tareas
            - (above|careful)
          - [Choice]: diario del mago
            - (above|careful)
  - [Choice]: ¿Cómo va el negocio?
    - (Condition: Up to Doric's Task III:)
      - **Doric:** Cómo llegar. Realmente estoy empezando a imaginar un nuevo futuro ahora; uno que nunca habría vivido si no hubiera sido por Boric.
      - (continue)
    - (Condition: After Doric's Task III and before Doric's Task VI:)
      - **Doric:** Bueno, en este momento, Boric no puede dejar de sonreír como un tonto. Eso es algo bueno, ¿verdad?
      - (continue)
    - (Condition: After Doric's Task VI and before Doric's Task VIII:)
      - **Doric:** Nuestro negocio se ha extendido por todo el mundo, recibimos pedidos de todo tipo de personas y nuestro futuro nunca ha parecido más brillante.
      - (continue)
    - **Doric:** ¿Había algo más que quisieras?
    - (initial)
  - [Choice]: Quería usar tus yunques.
    - **Doric:** Continúe. Lo menos que puedo hacer después de la ayuda que me brindaste.
  - [Choice]: ¿Tiene algún consejo para los aspirantes a aventureros?
    - (above|doric-advice)

#### Después de la tarea VIII de Doric

- **Doric:** Hola viajero, ¿qué te trae por mi humilde herrería?
- [Menu]: Elige una opción:
  - [Choice]: ¿Tienes más tareas de Smithing para mí?
    - **Doric:** No por el momento, ya lo tenemos todo bajo control. Gracias por toda la ayuda para ayudarnos a crecer.
  - [Choice]: cond=If either the Gofannon amulet, monkey's note or wizard's diary has been lost|Perdí un artículo que me diste.
    - (Condition: If only one item has been lost:)
      - (Condition: Without space in backpack:)
        - **Doric:** Sin embargo, no tienes espacio para guardarlo. Vuelve conmigo una vez que tengas espacio.
      - (Condition: With space in backpack:)
        - (receives=Gofannon amulet, monkey's note or wizard's diary)
        - **Doric:** Afortunadamente, uno de nuestros trabajadores lo encontró. Ten más cuidado la próxima vez.
      - (Condition: If two or more items have been lost:)
        - **Doric:** ¿Qué artículo querías recuperar?
        - [Menu]: Elige una opción:
          - [Choice]: Amuleto de Gofannon
            - (above|careful2)
          - [Choice]: diario del mago
            - (above|careful2)
          - [Choice]: nota del mono
            - (above|careful2)
  - [Choice]: ¿Cómo va el negocio?
    - **Doric:** No creerías lo bien que lo estamos haciendo. Todo es gracias a que me diste ese empujón inicial. ¿Había algo más que quisieras?
    - **Doric:** ¿Había algo más que quisieras?
    - (initial)
  - [Choice]: Quería usar tus yunques.
    - **Doric:** Continúe. Lo menos que puedo hacer después de la ayuda que me brindaste.
  - [Choice]: ¿Tiene algún consejo para los aspirantes a aventureros?
    - (above|doric-advice)
  - [Choice]: Tengo alguna información sobre esa nota.
    - **Player:** No estoy seguro de que lo creas, pero en su lugar solo había un montón de cáscaras de plátano.
    - **Doric:** Estás bromeando.  ¿Qué crees que querrían los monos con las armas?
    - **Player:** Quizás estén planeando invadir.
    - **Doric:** Jaja ¡bueno!
    - **Player:** Estaba hablando en serio.  Esas eran unas espeluznantes grandes hachas que les di.  ¿Cómo podían los monos empuñar armas tan enormes?
    - **Player:** Deben ser más fuertes de lo que pensamos.  ¿Quién sabe qué estragos podrían causar los monos?
    - **Player:** ¿Nos he condenado a todos?
    - **Doric:** ¡Para, me estás haciendo reír!

#### Intentando bajar las escaleras en la casa de Doric (solo antes de What's Mine is Yours)

- **Doric:** ¡Aléjate de allí! No es seguro bajar allí.

#### Intentando subir la escalera en la casa de Doric

- **Doric:** ¿Adónde crees que vas?
- **Player:** Sólo quería ver qué había aquí arriba.
- **Doric:** ¡Esta es mi casa! Si quisiera que subieras allí, te habría invitado. Ahora por favor aléjate.
