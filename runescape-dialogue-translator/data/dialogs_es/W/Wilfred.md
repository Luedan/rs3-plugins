# Wilfred

- **Original Wiki Page**: [Transcript:Wilfred](https://runescape.wiki/w/Transcript%3AWilfred)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|Dialogue for attempting to buy shard without having completed While Guthix Sleeps}}

### Standard dialogue


#### Antes de alcanzar el nivel 99 de Woodcutting

- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Wilfred:** ¡Mi nombre es Wilfred y soy el mejor leñador de Asgarnia! He pasado mi vida estudiando los mejores métodos para cortar madera. Por eso tengo esta capa, la Skillcape de Woodcutting.
  - [Choice]: ¿Qué es esa capa que llevas?
    - **Wilfred:** Este es un Skillcape de Woodcutting. Sólo una persona que haya alcanzado el nivel más alto posible en una habilidad puede usar uno.
  - [Choice]: ¿Puedes ayudarme con los trajes de centinela?
    - **Player:** ¿Puedes ayudarme con los trajes de centinela?
    - (Condition: If the player can't receive sentinel fragments and hasn't unlocked the blueprint required to make the outfit pieces:)
      - **Wilfred:** En el nivel 70 puedes comenzar a recolectar fragmentos para crear trajes de habilidades de élite. Cuando llegues a ese nivel, automáticamente comenzarás a recolectar fragmentos. Luego puedes usarlos con un plano para hacerte las piezas restantes del atuendo de élite para esta habilidad.
    - (Condition: If the player can receive sentinel fragments but hasn't unlocked the blueprint required to make the outfit pieces:)
      - **Wilfred:** Estás configurado para recibir fragmentos. Cuando llegues al nivel 80 podrás crear prendas de vestir.
    - (Condition: If the player can receive sentinel fragments and has unlocked the blueprint required to make the outfit pieces:)
      - **Wilfred:** Estás configurado para recibir fragmentos. Cuando tengas 3600 fragmentos, podrás usarlos para crear una pieza de atuendo de élite.
      - **Wilfred:** Simplemente vaya a un banco de trabajo Invention para crear las piezas.
    - (Condition: If the player owns the full nature's sentinel outfit or all of the outfit pieces required to craft it:)
      - **Wilfred:** Ya has creado todas las prendas posibles. Me aseguraré de que no reciba más fragmentos.
      - **Wilfred:** Recuerda que puedes combinar las piezas del atuendo básico para crear las versiones de nivel alto y obtener beneficios adicionales.
  - [Choice]: Pregunta por otra cosa.
    - (continue|More information)

#### Después de alcanzar el nivel 99 de Woodcutting

<!-- commented-out dialogue below is (temporarily?) missing in-game, likely due to bugs introduced with The Spirit of Accomplishment -->
- **Wilfred:** ¡Guau! ¡No es frecuente que conozca a alguien tan exitoso como tú en Woodcutting! Dado que eres tan hábil, ¿quizás estés interesado en comprar un Skillcape o un Woodcutting?
- [Menu]: Selecciona una opción
  - [Choice]: No, gracias.
    - **Player:** No, gracias.
    - **Wilfred:** Está bien. Vuelve conmigo si cambias de opinión.
  - [Choice]: Sí, por favor.
    - (Condition: If the player has a ring of charos (a) equipped:)
      - **Wilfred:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins para este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
    - ((Otherwise:))
<!--**** **Wilfred:** Anybody who has spent as much time cutting trees as you deserves the right to own one. That'll be 99,000 coins, please.-->
      - ((The price of the cape is 99,000 coins.))
    - [Menu]: Elige una opción:
      - [Choice]: [99,000/92,000] coins? Eso es demasiado caro.
<!--***** **Wilfred:** Not at all; there are many other adventurers who would love the opportunity to purchase such a prestigious item! You can find me here if you change your mind.-->
        - **Player:** Sé dónde encontrarte si cambio de opinión.
      - [Choice]: De hecho, creo que tengo el dinero aquí.
        - [99,000/92,000] coins se han eliminado de su bolsa de dinero.
        - capa (receives=a (trimmed or untrimmed) Woodcutting y capucha Woodcutting)
        - **Wilfred:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
      - [Choice]: cond=If the player has virtual level 120 Woodcutting:|He dominado esta habilidad. ¿Hay algo más?
        - **Wilfred:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
        - **Wilfred:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
        - **Wilfred:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo...
        - **Wilfred:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle un Woodcutting master cape.
        - [Menu]: ¿Comprar Woodcutting master cape por 120.000 coins?
          - [Choice]: Sí.
            - (Condition: Without free backpack space:)
              - **Wilfred:** No tienes suficiente espacio en tu backpack. Por favor regresa cuando tengas más.
            - (Condition: With free backpack space:)
              - (Condition: Without 120,000 coins:)
                - No tienes suficiente dinero para comprar esta capa.
                - (pop-up)
                  - (Pop-up: You do not have enough money to purchase this cape.)
              - (Condition: With 120,000 coins:)
                - Se han eliminado 120.000 coins de su bolsa de dinero.
                - (removes=120,000 coins) (receives=Woodcutting master cape)
                - (Action: Suena música Master cape.)
          - [Choice]: No.
            - (end)
  - [Choice]: He notado que hay un par de versiones de cada skillcape.
    - **Wilfred** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
    - (Condition: If the player is currently using the newer version of the Woodcutting skillcape:)
      - **Wilfred:** Aún puedes optar por usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, me gustaría usar la versión antigua del skillcape.
          - **Wilfred:** ¿Te gustaría usar el modelo antiguo solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
          - [Menu]: Selecciona una opción
            - [Choice]: Solo me gustaría cambiar el Woodcutting skillcape.
              - **Wilfred:** No hay problema, ahora utilizarás el modelo anterior para tu Woodcutting skillcape.
            - [Choice]: Me gustaría cambiar todos mis skillcapes.
              - **Wilfred:** No hay problema, ¡ahora usarás el modelo anterior para todos tus skillcapes!
            - [Choice]: ¡He cambiado de opinión!
              - (end)
        - [Choice]: No, gracias.
          - **Wilfred:** ¡Genial! ¡Me alegra que estés disfrutando de nuestra nueva versión!
    - (Condition: If the player is currently using the old version of the Woodcutting skillcape:)
      - **Wilfred:** Parece que actualmente estás usando el modelo anterior para tu Woodcutting skillcape. ¿Quieres cambiar a uno más nuevo?
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, me gustaría usar la nueva versión del skillcape.
          - **Wilfred:** ¿Te gustaría usar el modelo más nuevo solo para esta capa o para todos los skillcapes que tienes?
          - [Menu]: Selecciona una opción
            - [Choice]: Solo me gustaría cambiar el Woodcutting skillcape.
              - **Wilfred:** No hay problema, ahora utilizarás el modelo más nuevo para tu Woodcutting skillcape.
            - [Choice]: Me gustaría cambiar todos mis skillcapes.
              - **Wilfred:** No hay problema, ¡ahora usarás el modelo más nuevo para todos tus skillcapes!
            - [Choice]: ¡He cambiado de opinión!
              - (end)
        - [Choice]: No, gracias.
          - **Wilfred:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión anterior!
          - (Condition: If the player does not have all their skillcapes set to the old version:)
            - **Wilfred:** ¡Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas!
            - [Menu]: Selecciona una opción
              - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
                - **Wilfred:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
              - [Choice]: No, gracias.
                - (end)
  - [Choice]: ¿Puedes ayudarme con los trajes de centinela?
    - (above|outfits)
  - [Choice]: Pregunta por otra cosa.
    - (continue|More information)

#### Más información

- [Menu]: ¿Puedes contarme sobre...?
  - [Choice]: Árboles mayores.
    - **Player:** ¿Puedes hablarme de los árboles de saúco?
    - **Wilfred:** Ciertamente, sería un placer compartir contigo lo que he reunido durante mis años estudiando árboles.
    - **Wilfred:** Hay un puñado de árboles saúcos que conozco y han existido por mucho más tiempo del que puedo recordar.
    - **Wilfred:** La corteza exterior del tronco principal es muy dura, pero algunas de las ramas más altas son más fáciles de cortar con suficiente habilidad.
    - **Wilfred:** Crecen muy lentamente y tardan un poco más que la mayoría de los otros árboles en volver a crecer.
    - **Wilfred:** El saúco más cercano que conozco desde aquí está justo al sureste de Falador, cerca de la hiedra.
    - **Wilfred:** En el pasado, corté ese árbol de saúco y, mientras esperaba que volviera a crecer, corté otros árboles cercanos y la hiedra.
    - **Wilfred:** Dicho esto, si encontraste otros árboles de saúco, es posible que te resulte más efectivo moverte entre ellos, dándoles a los demás que ya cortaste la oportunidad de volver a crecer.
    - **Player** Gracias, ha sido muy útil.
  - [Choice]: Árboles de cristal.
    - **Player** ¿Puedes hablarme sobre los árboles de cristal?
    - **Wilfred:** Claro, aunque los árboles de cristal son algo diferentes a los árboles normales, eso es seguro.
    - **Wilfred:** Del árbol de cristal que conozco justo al oeste de Falador, cerca de la torre del Mago Oscuro, parece que le crecen fragmentos de cristal a su alrededor en varios momentos.
    - **Wilfred:** El árbol principal no se puede cortar con ningún hacha que haya probado, pero los fragmentos de cristal que ocasionalmente crecen alrededor de los bordes se pueden romper con un hacha decente.
    - **Wilfred:** Después de años de estudiarlo, también he notado que cuando los fragmentos están presentes, el árbol apunta directamente hacia arriba.
    - **Wilfred:** Sin embargo, tras una inspección más cercana, cuando los fragmentos no crecen a su alrededor, el árbol se inclina muy ligeramente en varias direcciones diferentes.
    - **Wilfred:** Quizás puedas descubrir por qué los fragmentos solo aparecen ocasionalmente y qué significan las diferentes direcciones.
    - **Wilfred:** En ocasiones incluso logré romper algunas geodas de cristal que estaban encerradas dentro de los fragmentos para encontrar algunas gemas escondidas en su interior.
    - **Wilfred:** Algunos de los que abrí también tenían otros objetos extraños, tal vez puedas arrojar algo de luz sobre el asunto si encuentras alguno.
    - **Player:** Qué interesante, gracias.
  - [Choice]: Hacha de brasas y claro.
    - (Condition: If the player doesn't meet the requirements:)
      - **Wilfred:** Tengo en mi poder un poderoso artefacto que fusionará un hacha imcando con un hacha de cristal, combinando los mejores elementos de la artesanía enana y élfica.
      - **Wilfred:** Sin embargo, solo se lo legaré a alguien que sea campeón tanto de los enanos como de los elfos.
      - **Wilfred:** Algún día, preveo que serás un hacedor de reyes en medio del caos.
      - **Wilfred:** Pero aún no ha llegado tu momento.
    - (Condition: If the player has purchased Shard of the Lumberjack before:)
      - **Player:** ¿Tienes más fragmentos del leñador?
      - **Wilfred:** ¿Otra vez? ¿Cuántas varitas mágicas cuestionables puede necesitar una persona?
      - (continue|BuyShard)
    - **Player** ¿Conoce alguna forma de mejorar mi hacha imcando?
    - **Wilfred:** Qué fortuito. Tengo en mi poder el Fragmento del Leñador. Este poderoso artefacto fusionará un hacha imcando con un hacha de cristal, combinando los mejores elementos de la artesanía enana y élfica.
    - **Player** Y me vas a dar este artefacto gratis, ¿no? ¿Dado que he salvado heroicamente al mundo en múltiples ocasiones?
    - **Wilfred:** Te venderé el fragmento del leñador por exactamente un millón de coins.
    - [Menu]: Seleccione una opción|ancla=Comprar fragmento
      - [Choice]: Comprar Fragmento del leñador: 1.000.000 (1M) coins.
        - (Condition: Without 1,000,000 coins:)
          - **Wilfred:** Lo siento, amigo. No pareces tener suficientes monedas.
        - (Condition: With at least 1,000,000 coins:)
          - (Condition: Without backpack space:)
            - **Wilfred:** Lo siento, amigo. Tu backpack está lleno.
          - (Condition: With backpack space:)
            - (removes=1,000,000 coins) (receives=Shard of the Lumberjack)
            - (Condition: Without having bought a Shard of Lumberjack before:)
              - [pic=Fragmento del leñador detail.png]
            - (Condition: Having bought a Shard of Lumberjack before:)
              - [pic=Fragmento del leñador detail.png]
      - [Choice]: Lo dejaré por ahora, gracias.
        - Usted decide no realizar una compra.
        - (previous2|More information)
  - [Choice]: No importa.
    - (end)
