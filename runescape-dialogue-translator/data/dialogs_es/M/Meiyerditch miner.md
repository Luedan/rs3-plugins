# Meiyerditch miner

- **Original Wiki Page**: [Transcript:Meiyerditch miner](https://runescape.wiki/w/Transcript%3AMeiyerditch%20miner)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Dialogue

- **Player:** Hola.
- (Condition: Antes de las misiones de Myreque:)
  - **Meiyerditch miner:** Oh, hola, debes ser nuevo aquí.
- (Condition: Después de las misiones de Myreque:)
  - **Meiyerditch miner:** Oh, hola.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Dónde estamos?
    - **Player:** ¿Dónde estamos?
    - **Meiyerditch miner:** ¿Qué? ¿No puedes decir por lo que te rodea que estás en una mina? Debes haber recibido un fuerte golpe en la cabeza para no darte cuenta.
    - (previous)
  - [Choice]: ¿Qué haces aquí?
    - **Player:** ¿Qué haces aquí?
    - (Condition: Antes de Río de Sangre:)
      - **Meiyerditch miner:** Somos mineros, ¡tal vez eso pueda darte una pista! Nos vemos obligados a extraer esos apestosos vyres. Una vez que hemos llenado el carro, a veces nos dejan volver a Meiyerditch, pero luego cobramos el diezmo. ¡No sé si lo prefiero aquí o fuera!
    - (Condition: Después de Río de sangre:)
      - **Meiyerditch miner:** Somos mineros. Solíamos vernos obligados a extraer aquí los vyres, pero ahora decidimos hacerlo. Resulta que esto que estamos extrayendo les hace tener menos hambre. ¿Quién sabía, verdad? De todos modos, necesitamos muchas de estas cosas.
    - (previous)
  - [Choice]: Do you have a spare pick?|cond=Si los jugadores no tienen pico en el backpack o equipado
    - **Player:** ¿Tienes una púa de repuesto?
    - **Meiyerditch miner:** Claro, aquí tienes uno que puedes usar.
    - (receives=Bronze pickaxe)
    - [El minero te entrega un pico de aspecto rústico.]
    - (previous)
  - [Choice]: How do you get out of here?|cond=Si los jugadores tienen un pico en el backpack o equipado
    - **Player:** ¿Cómo sales de aquí?
    - (Condition: Antes de Río de Sangre:)
      - **Meiyerditch miner:** No pueden retenerte aquí para siempre porque tienen que diezmarte, así que una vez que hayas llenado el carro, te dejarán ir. Se necesitan unas quince cargas para llenar el carro.
    - (Condition: Después de Río de sangre:)
      - **Meiyerditch miner:** Aquí te mostraré la salida...
      - (Action: La cámara se desvanece y aparece. el player aparece en la entrada de la mina.)
  - [Choice]: What is it that you're mining?|cond=
    - **Player:** ¿Qué es lo que estás extrayendo?
    - (Condition: Antes de Río de Sangre:)
      - **Meiyerditch miner:** Estamos extrayendo daeyalt. No sé exactamente qué hace (no hacemos demasiadas preguntas), pero lo he estado haciendo desde que era niño. Los carros se siguen llenando y ellos siguen avanzando por las vías. Va a una enorme refinería, es enorme, como otra ciudad bajo tierra.
      - **Player:** ¿Qué? ¿Has visto este lugar?
      - **Meiyerditch miner:** No yo, pero otras personas que conozco lo han visto y no mentirían.
      - **Juvinate guard:** ¡Ustedes dos cállense y vuelvan al trabajo!
    - (Condition: Después de Río de sangre:)
      - **Meiyerditch miner:** Estamos extrayendo daeyalt. Los nuevos líderes dicen que esto incluso hace que los vyres que solían ser humanos vuelvan a la normalidad. Y para aquellos que siempre han sido vyres, aparentemente les hace tener menos hambre, por lo que ya no necesitan alimentarse de nosotros, o con menos frecuencia, o algo así.
      - **Meiyerditch miner:** Así que ahora estamos felices de extraer carros llenos de estas cosas. Todo ayuda, ¿verdad?
  - [Choice]: Bien, gracias.
    - **Player:** Está bien, gracias.

### Mining

Antes de que se complete River of Blood, mientras minan dirán ciertas frases, quejándose de estar esclavizados. Estas frases no aparecen en el cuadro de chat y sólo son visibles en la ventana principal del juego. En orden alfabético las frases que pueden decir son:
- No puedo pensar con claridad, estoy muy cansada.
- Me siento tan débil que podría desmayarme.
- Odio esos vyres.
- Soy rico en experiencia, pobre en riqueza.
- Estoy harto de este lugar.
- Estoy tan cansada que podría dormir de pie.
- Oh, mis brazos.
- Oh, mi espalda.
- Lo que daría por un buen descanso nocturno.
- Trabajo, trabajo, trabajo, eso es todo lo que hago.
