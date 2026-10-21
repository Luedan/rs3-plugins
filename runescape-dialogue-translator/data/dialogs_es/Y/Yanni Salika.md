# Yanni Salika

- **Original Wiki Page**: [Transcript:Yanni Salika](https://runescape.wiki/w/Transcript%3AYanni%20Salika)
- **Letter**: `Y`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before completing Shilo Village


#### Hablando con Yanni Salika

- **Yanni Salika:** Lo sentimos, la tienda aún no está abierta. Todavía lo estamos preparando.

#### Usando cualquier elemento en Yanni Salika

- **Yanni Salika:** Me voy de aquí Bwana, el lugar está infestado de zombies.

### After completing Shilo Village


#### Hablando con Yanni Salika

- [Menu]: Elige una opción:
  - [Choice]: Háblame de este negocio de antigüedades.
    - **Yanni Salika:** Compro antigüedades y otros artículos interesantes. Si tienes algún artículo interesante que quieras venderme, déjame verlo y te ofreceré un precio justo. ¿Quieres que eche un vistazo a tus artículos y te dé
    - **Yanni Salika:** ¿Tienes una cita?
    - [Menu]: Selecciona una opción
      - [Choice]: ¡Sí, por favor!
        - **Player:** ¡Sí, por favor!
        - **Yanni Salika:** ¡Qué bien Bwana!
        - (Condition: Si el player tiene la clave ósea:)
          - **Yanni Salika:** Te daré 100 de oro por la llave de hueso.
          - (continue)
        - (Condition: Si el player tiene la placa de piedra:)
          - **Yanni Salika:** Te daré 100 de oro por la placa de piedra.
          - (continue)
        - (Condition: Si el player tiene el pergamino hecho jirones:)
          - **Yanni Salika:** Te daré 100 de oro por el pergamino hecho jirones.
          - (continue)
        - (Condition: Si el player tiene el pergamino arrugado:)
          - **Yanni Salika:** Te daré 100 de oro por el pergamino arrugado.
        - (Condition: Si el player tiene las notas de Bervirius:)
          - **Yanni Salika:** Te daré 100 de oro por el pergamino arrugado.
          - (continue)
        - (Condition: Si el player tiene el cristal de localización:)
          - **Yanni Salika:** Te daré 500 de oro por tu cristal de localización.
          - (continue)
        - (Condition: Si el player tiene las cuentas de los muertos:)
          - **Yanni Salika:** Te daré 1000 de oro por tus 'Cuentas de los muertos'.
          - (continue)
        - *(Si el player tiene el prisma negro:)*
          - **Yanni Salika:** Te daré 5000 de oro por tu Prisma Negro.
        - (Condition: Si el player tiene varios artículos elegibles:)
          - **Yanni Salika:** Esos son los artículos que me interesan en Bwana.
          - **Yanni Salika:** Si quieres venderme esos artículos, simplemente muéstramelos.
        - (Condition: Si el player solo tiene un artículo elegible:)
          - **Yanni Salika:** Y ese es el único elemento que me interesa.
          - **Yanni Salika:** Si quieres venderme ese artículo, simplemente muéstramelo.
        - (Condition: Si el player no tiene artículos elegibles:)
          - **Yanni Salika:** Lo siento Bwana, no tienes nada que me interese.
      - [Choice]: ¿Quizás en otro momento?
        - **Player:** ¿Quizás en otro momento?
        - **Yanni Salika:** Claro. Que tengas un buen día Bwana.
      - [Choice]: ¿Hay algo más interesante que hacer por aquí?
        - (ver|Un pequeño favor)
      - [Choice]: Mmmm, lo siento, no me interesa.
        - **Player:** Hmm, lo siento, no estoy interesado.
        - **Yanni Salika:** Es justo, vuelve si cambias de opinión.
  - [Choice]: ¿Hay algo más interesante que hacer por aquí?
    - (ver|Un pequeño favor)
- (Condition: Sin la llave de hueso ni el collar de cuentas de los muertos:)
  - [Choice]: ¿Tiene algún artículo interesante a la venta?
    - **Player:** ¿Tiene algún artículo interesante a la venta?
    - (Condition: Sin la llave de hueso ni Beads of the Dead:)
      - **Yanni Salika:** ¡Tengo un collar de cuentas muy atractivo y una llave inusual!
      - [Menu]: Selecciona una opción
        - [Choice]: Pregunta por el collar.
          - **Yanni Salika:** Sí, [sir/madam], un collar de cuentas muy atractivo, aparentemente ayuda a los aventureros de muchas maneras diferentes.{{anchor|beads}}
          - [Yanni te muestra el collar. De alguna manera te parece familiar.]
          - **Yanni Salika:** ¡Una auténtica ganga a 1200 gold coins!
          - [Menu]: Selecciona una opción
            - [Choice]: ¡Me lo llevo!
              - **Player:** ¡Lo aceptaré!
              - **Yanni Salika:** ¡Muy bien [Sir/Madam]!
              - [Yanni te entrega las cuentas y te quita el dinero.]
              - (receives=beads of the dead) (removes=1200 coins)
            - [Choice]: ¡No gracias, no estoy interesado!
              - **Player:** No gracias, no estoy interesado
              - **Yanni Salika:** Muy bien [sir/madam], vuelve si cambias de opinión.
        - [Choice]: ¡Pregunta por la llave!
          - **Yanni Salika:** Sí [sir/madam], una llave muy inusual, aparentemente permite acceder a un peligroso complejo subterráneo.{{anchor|bonekey}}
          - [Yanni te muestra la clave. De alguna manera te parece familiar.]
          - **Yanni Salika:** ¡Una auténtica ganga a 100 gold coins!
            - [Choice]: ¡Yo lo tomaré!
              - **Player:** ¡Lo aceptaré!
              - **Yanni Salika:** ¡Muy bien [Sir/Madam]!
              - [Yanni te entrega la llave y te quita el dinero.]
              - (receives=bone key (Shilo Village)) (removes=100 coins)
            - [Choice]: ¡No gracias, no estoy interesado!
              - **Player:** Hmm, lo siento, no estoy interesado.
              - **Yanni Salika:** Es justo, vuelve si cambias de opinión.
    - (Condition: Sin las cuentas de los muertos:)
      - (continuea|beads)
    - (Condition: Sin la llave de hueso)
      - (continuea|bonekey)

#### Uso de elementos en Yanni Salika


#### Llave de hueso

- **Yanni Salika:** Esa es una gran clave ósea. aquí tienes 100 de oro por ello.
- Vendes la llave de hueso por 100 de oro.
- (removes=bone key (Shilo Village)) (receives=100 coins)

#### Placa de piedra

- **Yanni Salika:** Esa es una gran placa de piedra. aquí tienes 100 de oro por ello.
- Vendes la placa de piedra por 100 de oro.
- (removes=stone-plaque) (receives=100 coins)

#### Pergamino andrajoso

- **Yanni Salika:** Es un pergamino muy andrajoso. aquí tienes 100 de oro por ello.
- Vendes el pergamino andrajoso por 100 de oro.
- (removes=tattered scroll) (receives=100 coins)

#### Pergamino arrugado

- **Yanni Salika:** Es un pergamino arrugado fantástico. aquí tienes 100 de oro por ello.
- Vendes el pergamino arrugado por 100 de oro.
- (removes=crumpled scroll) (receives=100 coins)

#### notas de Bervirio

- **Yanni Salika:** Esa es una gran copia de las notas de Bervirius. aquí tienes 100 de oro por ello.
- Vendes los billetes de Bervirius por 100 de oro.
- (removes=Bervirius notes) (receives=100 coins)

#### Localizando cristal

- **Yanni Salika:** Es un gran cristal de localización. Aquí tienes 500 de oro por ello.
- Vendes el cristal de localización por 500 de oro.
- (removes=locating crystal) (receives=500 coins)

#### Cuentas de los muertos

- **Yanni Salika:** Impresionante collar, aquí tienes 1000 de oro por él.
- Vendes las 'Cuentas de los Muertos' por 1000 de oro.
- (removes=beads of the dead) (receives=1000 coins)

#### Prisma negro

- Le muestras el prisma negro a Yanni.
- **Yanni Salika:**Ah, ¿te gustaría venderme esto, verdad? ¡Puedo ofrecerte 5000 coins!
- **¿VENDER EL PRISMA POR 5000 COINS?**
  - Si, lo vendo por 5000{{Sic}}
    - **Player:**Sí, lo venderé por 5000 coins.
    - **Yanni Salika:**Muy bien amigo mío, déjame contar tu recompensa.
    - Vendes el prisma negro por 5000 coins.
    - **Yanni Salika:**¡Gracias!
  - No, creo que lo aguantaré un poco más todavía.
    - **Player:**No, creo que lo aguantaré un poco más todavía.
    - **Yanni Salika:**Muy bien amigo, vuelve si cambias de opinión.
