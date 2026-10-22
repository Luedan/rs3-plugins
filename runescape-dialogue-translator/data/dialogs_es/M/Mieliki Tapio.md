# Mieliki Tapio

- **Original Wiki Page**: [Transcript:Mieliki Tapio](https://runescape.wiki/w/Transcript%3AMieliki%20Tapio)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Tree Gnome Stronghold

- **Mieliki Tapio:** ¿Qué quieres, humano? Mieliki está trabajando.
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Qué es este lugar?{{anchor|place}}
    - **Mieliki Tapio:** Esta es la tienda de Mieliki. La gente ayuda al estúpido marido de Mieliki a conseguir suministros para la alquimia. Se les otorgan puntos de competencia por trabajar. Aquí, en esta tienda, Mieliki intercambia puntos de competencia por recompensas. Mieliki admira la competencia y se complace en recompensar a quienes la poseen.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Qué estás haciendo?
        - (below|doing)
      - [Choice]: ¿Para qué sirven los portales?
        - (below|portal)
      - [Choice]: Tengo algunos puntos de competencia para intercambiar.
        - (below|points)
      - [Choice]: Me voy ahora.{{anchor|off}}
        - **Mieliki Tapio:** Muy bien, humano. Atarearse.
  - [Choice]: ¿Qué estás haciendo?{{anchor|doing}}
    - **Mieliki Tapio:** Mieliki está trabajando. Los humanos no tienen idea del trabajo. ¡Los humanos esperan cosas gratis! Pero Mieliki es un gran trabajador. Mieliki es un alquimista. Experimenta con productos químicos y trabaja duro. Algún día Mieliki espera inventar algo bueno y venderlo por mucho dinero. Cuando llegue ese día, Mieliki será recompensado por todo este trabajo. Así es como debe llegar el éxito: a través del trabajo duro.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Qué estás intentando inventar?
        - **Mieliki Tapio:** A Mieliki no le importa. Las grandes chinchompas químicas son buenas para las explosiones, pero a Mieliki no le gusta la violencia. El éxito debe llegar a través del trabajo duro, no de la violencia.
        - (otro)
      - [Choice]: ¿Qué es este lugar?
        - (above|place)
      - [Choice]: ¿Para qué sirven los portales?
        - (below|portal)
      - [Choice]: Tengo algunos puntos de competencia para intercambiar.
        - (below|points)
      - [Choice]: Me iré ahora.
        - (above|off)
  - [Choice]: ¿Para qué sirven los portales?{{anchor|portal}}
    - **Mieliki Tapio:** Primero, Mieliki hablará sobre el portal de Nyriki, el naranja. Conduce al lugar donde caza Nyriki. Los humanos pueden pasar a trabajar para él. Nyriki puede explicar qué ayuda quiere. Habla con él cuando lo veas. Otros portales conducen a lugares secretos, lugares a los que nadie puede llegar sin la magia de Mieliki. Mieliki pone criaturas en estos lugares para que el estúpido Nyriki practique su caza. Nyriki cree que es bueno cazando, pero se equivoca. Los humanos también pueden practicar la caza allí, si compran billetes. Cada boleto les permite atrapar una criatura.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Qué es este lugar?
        - (above|place)
      - [Choice]: ¿Qué estás haciendo?
        - (above|doing)
      - [Choice]: Tengo algunos puntos de competencia para intercambiar.
        - (below|points)
      - [Choice]: Me iré ahora.
        - (above|off)
  - [Choice]: cond=If the player has competence points:|Tengo algunos puntos de competencia para intercambiar.{{anchor|points}}
    - **Mieliki Tapio:** Oh, has estado ayudando a Nyriki. El tiempo es dinero; Nos has dado tu tiempo, por lo que mereces una recompensa. Ese es el camino.
    - (opens=Reward Shop (Big Chinchompa))
  - [Choice]: cond=If the player does not have any competence points:|¿Tiene alguna recompensa que ofrecer?
    - **Mieliki Tapio:** Mieliki tiene recompensas, sí, pero la gente debe ayudar a Nyriki a ganarlas. Mieliki no es un duende estúpido que da recompensas gratis.
    - (opens=Reward Shop (Big Chinchompa))
  - [Choice]: Nada, gracias.
    - **Mieliki Tapio:** ¿No quieres nada, humano? ¡Si no aspiras a nada, nada será tu recompensa! Tenga cuidado.

### Player-owned farm


#### Vender animales

- **Mieliki Tapio (coleccionista de chinchompas):** Tengo un pedido especial para [breed]. ¡Especialmente si tiene el rasgo [Trait]!
- **Mieliki Tapio (coleccionista de chinchompas):** También estoy detrás de algunas Chinchompas, de hecho compraré hasta [número] más mientras esté aquí.
- ((Repeated for each chinchompa in backpack:))
  - ¿Le gustaría vender [name] por frijoles [número]?
  - [Menu]: ¿Vender [name] por frijoles [número]?
    - [Choice]: Sí.
      - ((If the player has a million beans:))
        - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
        - **Mieliki Tapio (coleccionista de chinchompas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - (continue)
      - ((If transaction would take the player over a million beans:))
        - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
        - [Menu]: ¿Completar la transacción de todos modos?
          - [Choice]: Sí.
            - (Action: El animal está vendido.)
            - Frijoles [número] agregados a su bolsa de divisas.
            - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - [Choice]: No.
            - **Mieliki Tapio (coleccionista de chinchompas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
      - ((Otherwise:))
        - (Action: El animal está vendido.)
        - Frijoles [número] agregados a su bolsa de divisas.
        - (continue)
    - [Choice]: No.
      - (end)
- ((If animals were not sold:))
  - **Player:** Déjame comprobar qué animales tengo que coincidan con tu solicitud.
- ((If animals were sold:))
  - ((If Mieliki Tapio can still buy more:))
    - (end)
  - ((If Mieliki Tapio can't buy more:))
    - **Mieliki Tapio (coleccionista de chinchompas):** Ya compré todos los animales que necesito por ahora, ¡nos vemos luego!
    - (Action: Mieliki Tapio se teletransporta.)

#### Animales de venta rápida

- **Mieliki Tapio (coleccionista de chinchompas):** ¿Estás seguro de que quieres que me lleve todas las Chinchompas que tienes? No aceptaré ninguno de tus favoritos.
- [Menu]: ¿Vender todas tus chinchompas?
  - [Choice]: si
    - ((With chinchompas in backpack:))
      - ((If the player has a million beans:))
        - ((Repeated for each remaining animal, then continues below:))
          - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
          - **Mieliki Tapio (coleccionista de chinchompas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
        - No tienes animales para vender. ¡Cero animales, cero frijoles!
      - ((If transaction would take the player over a million beans:))
        - ((Repeated for each animal not surpassing the cap, then continues below:))
          - (Action: El animal está vendido.)
          - Frijoles [número] agregados a su bolsa de divisas.
        - ((Repeated for each animal left to sell, then continues below:))
          - Esta transacción le llevaría por encima del límite de un millón de frijoles. Al hacerlo, perdería beans [número].
          - [Menu]: ¿Completar la transacción de todos modos?
            - [Choice]: Sí.
              - (Action: El animal está vendido.)
              - Frijoles [número] agregados a su bolsa de divisas.
              - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
              - ((Repeated for each remaining animal, then continues below:))
                - ¡Tu bolsa de monedas está llena de frijoles! Necesitas gastar algunos frijoles antes de poder ganar más.
                - **Mieliki Tapio (coleccionista de chinchompas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - ((If multiple animals were sold:))
                - Has vendido animales [número] por un total de frijoles [número].
            - [Choice]: No.
              - **Mieliki Tapio (coleccionista de chinchompas):** No puedes aguantar más frijoles, no puedo comprarte este animal.
              - (continue)
        - ((If no animals were sold:))
          - No tienes animales para vender. ¡Cero animales, cero frijoles!
        - ((If multiple animals were sold:))
          - Has vendido animales [número] por un total de frijoles [número].
      - ((Otherwise:))
        - ((Repeated for each animal not surpassing the cap, then continues below:))
          - (Action: El animal está vendido.)
          - Frijoles [número] agregados a su bolsa de divisas.
        - ((If multiple animals were sold:))
          - Has vendido animales [número] por un total de frijoles [número].
    - ((Without chinchompas in backpack:))
      - No tienes animales para vender. ¡Cero animales, cero frijoles!
  - [Choice]: No
    - (end)
