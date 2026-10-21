# Alice's husband

- **Original Wiki Page**: [Transcript:Alice's husband](https://runescape.wiki/w/Transcript%3AAlice%27s%20husband)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At the farm by Port Phasmatys


#### Antes del magnetismo animal


##### Sin usar un amuleto de habla fantasma

- **Alice's husband:** ¡Guau, guau!

##### Mientras llevas un amuleto de habla fantasma

- **Player:** Tus animales no parecen muy sanos.
- **Alice's husband:** Es esa fuente en el templo al este. Los ha convertido a todos en zombies.
- **Player:** ¿Para qué sirven los animales zombies?
- **Alice's husband:** Ninguno en absoluto, amigo, excepto que los fieles de ese templo siguen viniendo y matándolos a todos por sus huesos. No me preguntes por qué.
- **Player:** Pero eres un fantasma; seguramente sabes algo al respecto.
- **Alice's husband:** No sé nada de nada. Oim un fantasma simple con necesidades simples. Lo único que sé es que, hace años, ese templo empezó a brillar de color verde y, unos meses después, me desperté muerto. Eso es todo lo que hay que hacer.

#### Después del magnetismo animal

- **Alice's husband:** Hola, ¿en qué puedo ayudarte? Lo vendo si tienes ecto-tokens.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Puedo comprar esos pollos ahora?
    - **Player:** ¿Puedo comprar esos pollos ahora?
    - **Alice's husband:** Puedo entregarte un pollo si me das 10 ecto-tokens por ave.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Puedo comprar 1 pollo ahora?
        - **Player:** ¿Puedo comprar 1 pollo ahora?
        - (Condition: Si el player tiene suficientes ecto-tokens:)
          - **Alice's husband:** Eh, algún día pronto tendré una bonita cama de muertos vivientes para dormir.
          - (removes=10 ecto-tokens) (receives=undead chicken)
        - (Condition: Si el player no tiene suficientes ecto-tokens:)
          - **Alice's husband:** Aquí no soy una organización benéfica, ¿sabes? Ya es bastante malo que todos ustedes, matadores de vacas, estén matándome bestias. Vuelve cuando tengas suficientes fichas.
        - (Condition: Si el player tiene suficientes ecto-tokens pero no tiene espacio en el inventario:)
          - **Alice's husband:** Nabo, vuelve cuando tengas espacio.
      - [Choice]: ¿Puedo comprar 2 pollos?
        - **Player:** ¿Puedo comprar 2 pollos?
        - (Condition: Si el player tiene suficientes ecto-tokens:)
          - **Alice's husband:** ¡Genial! Estoy guardando fichas para unas vacas asesinas. Eso les enseñará a los ladrones de huesos.
          - (removes=20 ecto-tokens) (receives=two undead chickens)
        - (Condition: Si el player no tiene suficientes ecto-tokens:)
          - (arriba)
        - (Condition: Si el player tiene suficientes ecto-tokens pero no tiene espacio en el inventario:)
          - **Alice's husband:** Tu saco es demasiado pequeño. Tira algo de esa basura que llevas.
      - [Choice]: Tus animales no se ven muy sanos, compraré en otro lado.
        - **Player:** Tus animales no parecen muy sanos, los compraré en otro lado.
        - **Alice's husband:** Ja ja, ¿cuántos granjeros fantasmas conoces entonces?
  - [Choice]: Tus animales no parecen muy sanos.
    - (por encima|estándar)
  - [Choice]: Estoy bien, gracias.
    - **Player:** Estoy bien, gracias.
  - [Choice]: ¿Dónde podría conseguir más de estos ecto-tokens?
    - **Player:** ¿Dónde podría conseguir más de estos ecto-tokens?
    - **Alice's husband:** Los fantasmas con los que hablo dicen que las fichas tienen algo que ver con la torre que se encuentra justo al este de aquí. Si necesitas recolectar algunos, lo intentaría allí.

##### Usando un pollo no-muerto sobre él

- **Alice's husband:** Vendo pero no compro.

##### Usando cualquier otro elemento sobre él

- **Alice's husband:** ¿De qué le sirven esas cosas a un fantasma como yo?
