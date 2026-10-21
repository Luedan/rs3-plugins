# Gardener Gunnhild

- **Original Wiki Page**: [Transcript:Gardener Gunnhild](https://runescape.wiki/w/Transcript%3AGardener%20Gunnhild)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Throne of Miscellania

- **Gardener Gunnhild:** Hola.
- [Menu]: ¿De qué te gustaría hablar?
  - [Choice]: Gardener Gunnhild.
    - **Player:** Buenos días. ¿Qué estás haciendo?
    - **Gardener Gunnhild:** Estoy quitando las malas hierbas de este jardín de hierbas. ¡Es un trabajo duro! También vendo algunos artículos de jardinería.
    - [Menu]: Selecciona una opción
      - [Choice]: Buena suerte con eso.
        - **Player:** Buena suerte con eso.
        - **Gardener Gunnhild:** Gracias.
      - [Choice]: ¿Qué tienes a la venta?
        - **Player:** ¿Qué tienes a la venta?
        - **Gardener Gunnhild:** Actualmente vendo rastrillos de jardín y hoces de hierro. Cuestan 15 po cada uno, ¿quieres uno?
        - [Menu]: Selecciona una opción
          - [Choice]: Quisiera un rastrillo, por favor.
            - **Player:** Me gustaría un rastrillo, por favor.
            - (Condition: Si el player tiene al menos 15 coins:)
              - (removes=15 coins)
              - **Gardener Gunnhild:** ¡Gracias! Aquí tienes.
              - (receives=rake)
          - [Choice]: Quisiera una hoz de hierro, por favor.
            - **Player:** Me gustaría una hoz de hierro, por favor.
            - (Condition: Si el player tiene al menos 15 coins:)
              - (removes=15 coins)
              - **Gardener Gunnhild:** ¡Gracias! Aquí tienes.
              - (receives=iron sickle)
          - [Choice]: No, gracias.
            - **Player:** No, gracias.
          - [Choice]: ¿Para qué sirven las hoces de hierro?
            - **Player:** ¿Para qué sirven las hoces de hierro?
            - **Gardener Gunnhild:** No puedo pensar en nada en este momento. ¡Pero puedes comprar uno si quieres!
            - (otro)
  - [Choice]: Su índice de aprobación.
    - **Player:** ¿Qué piensa la gente de mí por aquí?
    - (Condition: Si su índice de aprobación es inferior al 25%:)
      - **Gardener Gunnhild:** No has hecho muchos amigos desde que llegaste aquí. En la última encuesta, sólo le agradaste al [approval rating]% de la población.
    - (Condition: Si su índice de aprobación está entre 25% y 49%:)
      - **Gardener Gunnhild:** Realmente no te has ganado el corazón de los lugareños, si entiendes lo que quiero decir. En la última encuesta, sólo le agradaste al [approval rating]% de la población.
    - (Condition: Si su índice de aprobación está entre 50% y 74%:)
      - **Gardener Gunnhild:** No llevas mucho tiempo aquí, pero la gente te quiere razonablemente. En la última encuesta, le agradaste al [approval rating]% de la población.
    - (Condition: Si su índice de aprobación es del 75% o más:)
      - **Gardener Gunnhild:** Pareces muy popular para ser un recién llegado a estas tierras. En la última encuesta, le agradaste al [approval rating]% de la población.

#### Intentar rastrillar lino o hierbas

*Con un índice de aprobación inferior al 100%*
- **Gardener Gunnhild:** {{RSChat|Thanks!}}
*Con un índice de aprobación del 100%*
- **Gardener Gunnhild:** No te preocupes más, [Sir/Madam], ¡ya has hecho mucho!

### After [[Throne of Miscellania]]


#### Hablando con Gardener Gunnhild

- **Gardener Gunnhild:** Buenos días, Su Alteza Real
  - [Menu]: ¿De qué te gustaría hablar?
    - [Choice]: Gardener Gunnhild.
      - **Player:** Buenos días. ¿Qué estás haciendo?
      - **Gardener Gunnhild:** Estoy quitando las malas hierbas de este jardín de hierbas. ¡Es un trabajo duro! También vendo algunos artículos de jardinería.
        - [Choice]: Buena suerte con eso.
          - **Player:** Buena suerte con eso.
          - **Gardener Gunnhild:** Gracias, Su Alteza Real.
        - [Choice]: ¿Qué tienes a la venta?
          - **Player:** ¿Qué tienes a la venta?
          - **Gardener Gunnhild:** Actualmente vendo rastrillos de jardín y hoces de hierro. Si desea uno, Su Alteza Real, cuestan 15 po cada uno.
            - [Choice]: Quisiera un rastrillo, por favor.
              - **Player:** Me gustaría un rastrillo, por favor.
                - (Condition: Si tienes suficiente dinero contigo:)
                  - (Condition: Si el dinero a pagar se retira de su bolsa de dinero:)
                    - Se han eliminado 15 coins de tu bolsa de dinero.
                  - **Gardener Gunnhild:** ¡Gracias! Aquí tienes.
            - [Choice]: Quisiera una hoz de hierro, por favor.
              - **Player:** Me gustaría una hoz de hierro, por favor.
                - (Condition: Si tienes suficiente dinero contigo:)
                  - (Condition: Si el dinero a pagar se retira de su bolsa de dinero:)
                    - Se han eliminado 15 coins de tu bolsa de dinero.
                  - **Gardener Gunnhild:** ¡Gracias! Aquí tienes.
            - [Choice]: No, gracias.
              - **Player:** No, gracias.
            - [Choice]: ¿Para qué sirven las hoces de hierro?
              - **Player:** ¿Para qué sirven las hoces de hierro?
              - **Gardener Gunnhild:** No puedo pensar en nada en este momento. ¡Pero puede comprar uno si lo desea, alteza!
                - [Choice]: Quisiera un rastrillo, por favor.
                  - *(Igual que arriba)*
                - [Choice]: Quisiera una hoz de hierro, por favor.
                  - *(Igual que arriba)*
                - [Choice]: No, gracias.
                  - *(Igual que arriba)*
    - [Choice]: Su índice de aprobación.
      - **Player:** ¿Qué piensa la gente de mí por aquí?
      - (Condition: Si su índice de aprobación está entre 25% y 49%:)
        - **Gardener Gunnhild:** Su gente está cada vez más insatisfecha con el régimen, Su Alteza Real. En la última encuesta, sólo el [approval rating]% de la población lo apoyó.
      - (Condition: Si su índice de aprobación está entre 50% y 74%:)
        - **Gardener Gunnhild:** Usted es bien considerado, Su Alteza Real. En la última encuesta, el [approval rating]% de la población lo apoyó.
      - (Condition: Si su índice de aprobación es del 75% o más:)
        - **Gardener Gunnhild:** Usted es universalmente adorado, Su Alteza Real. En la última encuesta, el [approval rating]% de la población lo apoyó.

#### Intentar rastrillar lino o hierbas

*Con un índice de aprobación inferior al 100%*
- **Gardener Gunnhild:** {{RSChat|Thanks!}}
*Con un índice de aprobación del 100%*
- **Gardener Gunnhild:** No se preocupe más, Alteza, ¡ya ha hecho mucho!
