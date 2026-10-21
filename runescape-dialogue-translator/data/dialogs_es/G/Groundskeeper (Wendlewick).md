# Groundskeeper (Wendlewick)

- **Original Wiki Page**: [Transcript:Groundskeeper (Wendlewick)](https://runescape.wiki/w/Transcript%3AGroundskeeper%20%28Wendlewick%29)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Wendlewick


#### En un mundo gratuito

- **Guardian:** Hola, aventurero. ¿Estás aquí para aprender sobre los pájaros y las abejas?
- **Player:** ¿Perdón?
- **Jardinero:** Puedo ayudarte con la captura de aves y la apicultura. ¿No quedó eso claro?
- **Jardinero:** La apicultura y la captura de casas de pájaros solo están disponibles para miembros.

#### En el mundo de los miembros

- **Guardian:** Hola, aventurero. ¿Estás aquí para aprender sobre los pájaros y las abejas?
- **Player:** ¿Perdón?
- **Jardinero:** Puedo ayudarte con la captura de aves y la apicultura. ¿No quedó eso claro?
- [Menu]: Selecciona una opción
  - [Choice]: Cuéntame sobre la captura de aves.
    - **Player:** Háblame de pájaros.
    - **Jardines:** Los pájaros son una molestia. Se comen las abejas, desentierran semillas y no hacen ni la mitad de ruido con un incesante *chirrido*.
    - **Jardinero:** ¡Ahí es donde entra en juego la captura de cajas para pájaros! Así es como lo manejo efectivamente.
    - **Jardines:** ¿Puedo enseñarte si quieres? Me ahorraría tener que caminar hasta el santuario y más allá todos los días para restablecer las trampas. También podrás quedarte con todo lo que encuentres.
    - **Player:** Cuéntame más.
    - **Jardinero:** Es muy fácil de entender: tomas un tronco de cualquier tipo y un mecanismo de relojería, lo conviertes en una trampa para pájaros, lo colocas en un lugar y luego lo llenas con suficiente semilla...
    - **Jardinero:** ...vuelve un rato después y *puf*. Has atrapado algunos pájaros y, si tienes suerte, también algunos nidos de pájaros.
    - (Condition: Antes de completar Cuando un pájaro mamá ama a un pájaro papá:)
      - (Condition: Antes de pasar a "¿Tiene algún material de apicultura?" diálogo:)
        - Estás a mitad de camino de completar: Cuando una mamá pájaro ama a un papá pájaro
      - (Condition: Después de leer "¿Tiene algún material de apicultura?" diálogo:)
        - {{RSFontAchievement|When a Mummy Bird Loves a Daddy Bird}}
    - (Condition: Primera vez:)
      - **Guardian:** Dado que estás tan dispuesto a ayudar, déjame comenzar con lo primero.
      - (Condition: Sin espacio en backpack:)
        - **Guardián:** Pero primero querrás dejar espacio para 3 artículos en tu backpack.
      - (Condition: Con espacio en backpack:)
        - [pic2=Mecanismo de relojería detail.png]
        - (receives=logs, clockwork and 10 potato seeds)
        - **Jardinero:** Conviértalo en una pajarera y luego colóquelo {{fact}} en esa parcela justo al lado de la cerca.
        - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Importa el tipo de semilla?
        - **Player:** ¿Importa el tipo de semilla?
        - **Jardinero:** ¡Para nada! Para los pájaros, todas las semillas son iguales. Sólo una pizca ligera de digamos... uno para tu pajarera básica.
      - [Choice]: ¿Importa el tipo de madera?
        - **Player:** ¿Importa el tipo de madera?
        - **Jardinero:** ¡Solo por experiencia adquirida! ¡Cuanto mejor sea la madera, mejor será la casa, mejor será el pájaro!
        - **Jardinero:** Las casas de mayor calidad también requerirán más semillas para llenarse, pero también se atraparán más rápido. ¡Se cosecha lo que se siembra y todo eso!
      - [Choice]: ¿Dónde consigo un mecanismo de relojería?
        - **Player:** ¿Dónde consigo un mecanismo de relojería?
        - **Jardines:** Se puede fabricar en un banco de trabajo de tu casa.
        - **Jardinero:** Alternativamente, te venderé algunos, pero con una prima.
        - [Menu]: ¿Comprar algunos suministros?
          - [Choice]: Compraré algunos ahora.
            - (opens=The Birds and the Bees)
          - [Choice]: Tengo más preguntas.
            - (previous)
      - [Choice]: ¿Dónde puedo encontrar otras parcelas para pajareras?
        - **Player:** ¿Dónde puedo encontrar otras parcelas para pajareras?
        - **Jardinero:** Si te diriges hacia el este desde aquí, hay tres repartidos por Marigold Farm.
        - **Jardinero:** Luego, si te diriges hacia el sureste, encontrarás otro en la granja Eastfold.
        - **Guardian:** Si te diriges hacia el sur desde allí, podrás encontrar uno cerca del anillo de hadas y otro en la casa del encargado del santuario.
        - **Jardinero:** La parcela final está al oeste, cerca de las áreas de árboles de Dalia.
      - [Choice]: ¡Suena bien!
        - (end)
  - [Choice]: ¿Tiene algún material de apicultura?
    - **Player:** ¿Tiene algún material de apicultura a la venta?
    - **Jardinero:** ¡De hecho, sí!
    - (opens=The Birds and the Bees)
    - (Condition: Antes de completar Cuando una mamá pájaro ama a un papá pájaro)
      - (Condition: Antes de pasar a 'Cuénteme sobre la captura de aves'. diálogo:)
        - Estás a mitad de camino de completar: Cuando una mamá pájaro ama a un papá pájaro
      - (Condition: Después de leer 'Cuénteme sobre la captura de aves'. diálogo:)
        - {{RSFontAchievement|When a Mummy Bird Loves a Daddy Bird}}
  - [Choice]: Estoy bien por ahora.
    - **Player:** Estoy bien por ahora.
    - **Jardinero:** Ah, tal vez en otro momento.
