# Leprechaun (Evil Tree)

- **Original Wiki Page**: [Transcript:Leprechaun (Evil Tree)](https://runescape.wiki/w/Transcript%3ALeprechaun%20%28Evil%20Tree%29)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Strange sapling dialogue

- **Duende:** 'Hola, 'hola, piernas.
- [Menu]: Seleccione una opción{{anchor|init-sapling}}
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Duende:** ¿Yo? ¿Oo pregunta? No soy nadie más que un duende, ¿no?
    - **Player:** Suenas un poco diferente de otros duendes...
    - **Duende:** Eso se debe al hecho de que fui criado por diablillos, ¿no? Chicos adorables, diablillos. Vecinos correctos.
    - **Duende:** De todos modos, si me das un 'y, [lad/lass], puedo devolverte un favor.
    - **Duende:** Me encontré con esta raíz salvaje mientras deambulaba, así que pensé que me quedaría y les conseguiría a ustedes, viejos con piernas largas, para ayudar a nutrirla.
    - **Duende:** Este pequeño está creciendo rápido, pero acelerarías el proceso si lo animaras un poco.
    - (initial|init-sapling)
  - [Choice]: ¿Qué es esa cosa que crece cerca?
    - **Player:** ¿Qué es esa cosa que crece cerca?
    - **Duende:** ¿Eso? Eso es... eso es... es raro... eh... no.
    - **Player:** No sabes qué es, ¿verdad?
    - **Duende:** No, no con razón...
    - **Duende:** Pero vale la pena cuidar todas las creaciones de Madre Gielinor. Échanos una mano y anima al peque, ¿no? ¡Está creciendo rápido!
    - (initial|init-sapling)
  - [Choice]: ¿Cómo lo alimento?
    - **Player:** ¿Cómo lo alimento?
    - **Duende:** Eso es fácil, simplemente interactúa con él, como lo harías con cualquier cultivo de Farming. Eso le ayudará a crecer grande y fuerte. Incluso podrías conseguir algo de experiencia Farming.
    - **Player:** ¿Cuánto tiempo lleva nutrirlo?
    - (Condition: If the strange sapling hasn't transformed yet:)
      - **Duende:** No mucho. Mi ojo experimentado calcula que crecerá por completo en aproximadamente [2/3/4/5] minutos. Por supuesto, si consigues que algunos amigos te ayuden, el pequeño crecerá más rápido.
      - (initial|init-sapling)
    - (Condition: If the strange sapling is about to transform:)
      - **Duende:** No mucho. Mi ojo experimentado calcula que crecerá por completo en aproximadamente 1 minuto. Por supuesto, si consigues que algunos amigos te ayuden, el pequeño crecerá más rápido.
      - (initial|init-sapling)
    - (Condition: If the strange sapling has already transformed into an Evil Tree:)
      - **Duende:** No mucho. Mi ojo experimentado calcula que estaremos completamente desarrollados en aproximadamente...
      - **Duende:** ¡Crickey! ¡Qué es eso!
  - [Choice]: ¿Por qué debería ayudar?
    - **Player:** ¿Por qué debería ayudar?
    - **Duende:** Hay enormes recompensas cuidando la naturaleza, ayudando a que las cosas débiles se vuelvan fuertes. Podrías aprender sobre Farming ayudando a este pequeño retoño a convertirse en un árbol.
    - (initial|init-sapling)
  - [Choice]: Adiós
    - **Player:** Adiós.
    - **Duende:** ¡Nos vemos!

### Evil Tree dialogue

- **Duende:** ¿Aún no has notado el árbol? ¡Córtalo!
- [Menu]: Seleccione una opción{{anchor|init-options}}
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Duende:** ¿Yo? ¿Oo pregunta? No soy nadie más que un duende, ¿no?
    - **Player:** Suenas un poco diferente de otros duendes...
    - **Duende:** Eso se debe al hecho de que fui criado por diablillos, ¿no? Chicos adorables, diablillos. Vecinos correctos.
    - **Duende:** De todos modos, me encontré con esta raíz deambulando, así que os conseguí, viejos con piernas largas, para que me ayuden a salir.
    - **Duende:** Ahora mira lo que tengo en mis manos. ¡Por favor, muchacho!
    - **Duende:** Si me das una mano, puedo devolverte un favor.
    - (initial|init-options)
  - [Choice]: ¿Qué es esa cosa?
    - **Player:** ¿Qué es esa cosa?
    - **Duende:** Que hay un árbol malvado, ¿no? El viejo astuto comienza pareciendo un retoño inocente.
    - **Duende:** Más tarde, ¡oh! Se convierte en una bestia aterradora, todo raíces azotadas y '¡Mírame, desagradable teef!'
    - **Leprechaun:** Algunos de ellos, según me contó un compañero, son más fáciles de matar que otros.
    - (initial|init-options)
  - [Choice]: ¿Cómo puedo ayudar?
    - **Player:** ¿Cómo puedo ayudar?
    - **Duende:** No puedes acercarte al árbol mientras esas raíces se agitan, así que tendrás que cortarlas con un hacha. Una vez que se hayan ido, puedes atacar el árbol mismo. 'Porque es un árbol, no le gustan las hachas ni el fuego. Utilice cualquier leña que obtenga de las raíces para prender fuego en la base del árbol. Los incendios seguirán ardiendo y dañando el árbol mientras lo golpeas con un hacha.
    - **Duende:** ¿Necesitas más información?
    - [Menu]: Selecciona una opción
      - [Choice]: si
        - **Player:** Sí, me gustaría obtener más información.
        - [Menu]: ¿Sobre qué quieres saber más?{{anchor|knowmore}}
          - [Choice]: ¿Cómo corto el árbol?
            - **Player:** ¿Cómo corto el árbol?
            - **Duende:** Solo puedes cortar el árbol cuando ya no tenga raíces y si tienes un hacha. Cuanto mejor sea el hacha, más rápido cortarás el árbol.
            - **Leprechaun:{{anchor|hatchet}}** ¿Quieres un hacha? Creo que tengo uno en mi bolsa de botín en alguna parte...
            - [Menu]: Selecciona una opción
              - [Choice]: si
                - **Duende:** ¡Parece que ya tienes un hacha!
                - (initial|init-options)
              - [Choice]: No
                - **Player:** No, gracias.
                - **Duende:** Haz lo mismo, [lad/lass].
                - (initial|init-options)
          - [Choice]: ¿Cómo enciendo fuegos en el árbol?
            - **Player:** ¿Cómo enciendo fuegos en el árbol?
            - **Duende:** Solo puedes quemar el árbol cuando ya no tenga raíces. Cuando los hayas cortado, usa la leña de las raíces del árbol. Tienes que tener un yesquero para encender los fuegos.
            - **Duende:** ¿Necesitas un yesquero?
            - [Menu]: Selecciona una opción
              - [Choice]: si
                - (Condition: If the player does not have a tinderbox in inventory:)
                  - **Duende:** ¿Necesitas un yesquero? Aquí tienes, muchacho. ¡No te quemes!
                  - [Te entrega un yesquero.]
                  - (receives=tinderbox)
                  - (initial|init-options)
                - (Condition: If the player already has a tinderbox in inventory:)
                  - **Duende:** ¡Parece que ya tienes un polvorín!
                  - (initial|init-options)
              - [Choice]: No
                - **Player:** No, gracias.
                - **Duende:** Haz lo mismo, [lad/lass].
          - [Choice]: ¿Cómo trato las raíces?
            - **Player:** ¿Cómo trato las raíces?
            - **Duende:** Tienes que cortarlos para llegar al árbol. Un hacha o un machete deberían ser suficientes. Cuanta más gente los corte, más rápido caerán. Puedes conseguir leña de ellos, que querrás conservar para encender el fuego en el árbol.
            - **Duende:** ¿Quieres un hacha? Creo que tengo uno en mi bolsa de botín en alguna parte...
            - (continuea|hatchet)
          - [Choice]: ¿Cómo sé cuánto daño le estoy haciendo al árbol?
            - **Player:** ¿Cómo sé cuánto daño le estoy haciendo al árbol?
            - **Duende:** Si 'inspeccionas' el árbol, podrás descubrir cuánto daño has causado, así como algunos otros datos útiles.
            - **Duende:** También deberías ver la corteza volar al cortarla, y los incendios se encenderán cuando causen daño. Deberías ver que el árbol se ve más débil cuanto más daño le haces. Te haré saber cómo estás tan a menudo como pueda.
            - (initial|init-options)
          - [Choice]: ¿Cuánto tiempo llevará esto?
            - **Player:** ¿Cuánto tiempo llevará esto?
            - (Condition: When the tree has less than 100% health remaining:)
              - **Duende:** Todavía es grande. Calculo que podría durar media hora. ¡Si consigues que algunos compañeros te ayuden, podemos matarlo más rápido!
              - (continue)
            - (Condition: When the tree has less than 50% health remaining:)
              - **Duende:** Se está debilitando. Calculo que tardará menos de veinte minutos. ¡Si consigues que algunos compañeros te ayuden, podemos matarlo más rápido!
              - (continue)
            - (Condition: When the tree has less than 25% health remaining:)
              - **Duende:** Se está debilitando. No creo que pueda durar más de diez minutos. ¡Si consigues que algunos compañeros te ayuden, podemos matarlo más rápido!
              - (continue)
            - (initial|init-options)
      - [Choice]: No
        - **Player:** No, gracias.
        - **Duende:** Haz lo mismo, [lad/lass].
        - (initial|init-options)
      - [Choice]: ¿Puedo tomar prestadas algunas herramientas?
        - (below|borrow)
      - [Choice]: ¿Por qué debería ayudarte?
        - **Player:** ¿Por qué debería ayudarte?
        - **Leprechaun:** Hay un montón de botín para ti. Matar a uno de ellos te dará logs, por supuesto.
        - **Duende:** ¡Pero eso no es todo! Es posible que obtenga semillas o nidos, pistas del Treasure Trail y tal vez algunas otras sorpresas.
        - **Leprechaun:** Además, cualquier logs que obtengas te teletransportaré directamente a tu banco. Sincero, jefe.
        - **Duende:** También puedo hacer que sea menos probable que tales algunos árboles mientras los cortas, pero esto solo funcionará en árboles que no hayas cultivado tú mismo.
        - **Duende:** ¿Necesitas más información?
        - (previous|knowmore)
  - [Choice]: ¿Puedo tomar prestadas algunas herramientas?
    - **Player:{{anchor|borrow}}** ¿Puedo tomar prestadas algunas herramientas?
    - **Duende:** Creo que puedo prescindir de ellos.
    - [Menu]: Selecciona una opción
      - [Choice]: hacha
        - **Duende:** ¡Parece que ya tienes un hacha!
      - [Choice]: yesquero
        - (Condition: If the player does not have a tinderbox in inventory:)
          - **Duende:** ¿Necesitas un yesquero? Aquí tienes, muchacho. ¡No te quemes!
          - [Te entrega un yesquero.]
          - (receives=tinderbox)
          - (initial|init-options)
        - (Condition: If the player already has a tinderbox in inventory:)
          - **Duende:** ¡Parece que ya tienes un polvorín!
          - (initial|init-options)
      - [Choice]: ambos
        - **Duende:** ¡Parece que ya tienes un hacha!
        - (Condition: If the player does not have a tinderbox in inventory:)
          - **Duende:** ¿También necesitas un yesquero? Aquí tienes, muchacho. ¡No te quemes!
          - [Te entrega un yesquero.]
          - (receives=tinderbox)
          - (initial|init-options)
        - (Condition: If the player already has a tinderbox in inventory:)
          - **Duende:** ¡Y parece que ya tienes un polvorín!
          - (initial|init-options)
      - [Choice]: nada
        - (initial|init-options)
  - [Choice]: Adiós
    - **Player:** Adiós.
    - **Duende:** ¡Nos vemos!

### If the tree is dead

- **Duende:** ¡Caramba! ¡Fuiste y lo hiciste!
- [Menu]: Seleccione una opción{{anchor|init-options-2}}
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Duende:** ¿Yo? ¿Oo pregunta? No soy nadie más que un duende, ¿no?
    - **Player:** Suenas un poco diferente de otros duendes...
    - **Duende:** Eso se debe al hecho de que fui criado por diablillos, ¿no? Chicos adorables, diablillos. Vecinos correctos.
    - **Duende:** De todos modos, me encontré con esta raíz deambulando, así que os conseguí, viejos con piernas largas, para que me ayuden a salir.
    - **Leprechaun:** ¡Resulta que tengo un poquito más, porque tiene dientes rechinantes y raíces agitadas!
    - **Duende:** ¡Así que os pido que me ayuden cortando y quemando la pesadilla arbórea!
    - (initial|init-options-2)
  - [Choice]: ¿Qué es esa cosa que hay cerca?
    - **Player:** ¿Qué es esa cosa que hay cerca?
    - **Duende:** ¿Eso? Ése es un "árbol del mal", amigo.
    - **Duende:** Es un vejete astuto y comienza pareciendo un retoño inocente.
    - **Duende:** Más tarde, ¡oh! Se convierte en una bestia aterradora, todo raíces azotadas y '¡Mírame, desagradable teef!'
    - **Leprechaun:** Algunos de ellos, según me contó un compañero, son más fáciles de matar que otros.
  - [Choice]: ¿Habrá otro Árbol del Mal?
    - **Duende:** Eso es lo gracioso. Parecen aparecer cada dos horas en todo el mundo. Extraño, ¿no? Los árboles espirituales saben dónde están; pregúntales si estás dispuesto a ayudar.

### After taking rewards from the Dead Evil Tree

- **Duende:** ¡Gracias por tu ayuda, muchacho! Durante los próximos X minutos (dependiendo del tipo de árbol malvado talado), cualquier roble, sauce, arce, magia o anciano logs normal, te teletransportaré directamente a tu banco. ¡Honesto, jefe!
- **Duende:** También solucionaré un poco de magia, lo que hará que sea menos probable que tales árboles normales, robles, sauces, arces, tejos o mágicos, pero esto solo funcionará en algunos árboles que encuentres mientras deambulas, no en aquellos que hayas cultivado tú mismo.
- **Player:** ¡Gracias!

### Overhead dialogue

- (Condition: Upon the strange sapling turning into an Evil Tree:)
  - **Duende:** {{RSChat|Crikey! What's that!}}
- (Condition: Upon the Evil Tree reaching 50% health:)
  - **Duende:** {{RSChat|It's getting weaker!}}
- (Condition: Upon the Evil Tree dying:)
  - **Duende:** {{RSChat|Hurrah! The Evil Tree is dead!}}

#### Diálogo histórico general

- (Condition: When the health of the Evil Tree is above 25%, any of the following dialogue may occur:)
  - **Duende:** {{RSChat|Why does this always 'appen to me?!}}
  - **Duende:** {{RSChat|Ooh! 'E's a nasty one!}}
- (Condition: When the health of the Evil Tree is below 25%, any of the following dialogue may occur:)
  - **Duende:** {{RSChat|Don't stop choppin'!}}
  - **Duende:** {{RSChat|It's on its last legs! I mean... roots!}}
  - **Duende:** {{RSChat|The end is nigh!}}
  - **Duende:** {{RSChat|You can do it!}}
