# Rug merchant

- **Original Wiki Page**: [Transcript:Rug merchant](https://runescape.wiki/w/Transcript%3ARug%20merchant)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to

- **Rug merchant:** Saludos, viajero del desierto. ¿Necesita los servicios de la flota de alfombras voladoras de Ali Morrisane?
- [Menu]: Elige una opción:
  - [Choice]: Háblame de Ali Morrisane.
    - {{anchor|ali}}**Player:** Háblame de Ali Morrisane.
    - **Rug merchant:** ¿Qué? ¿No has oído hablar de Ali Morrisane? ¿Posiblemente el mayor vendedor de todo Kharidian Desert, si no de todo RuneScape?
    - (Condition: If the player has not done The Feud:)
      - **Player:** No puedo decir que sí, pero debe ser del tipo ambicioso como para montar su propia aerolínea.
      - **Rug merchant:** Creo que está intentando enfrentarse a esos gnomos en su propio juego, y apostaría una buena cantidad de dinero a que probablemente ganará.
      - **Player:** ¿Eh? Me has perdido.
      - **Rug merchant:** Ya sabes, los pequeños... los que no son enanos.
      - **Player:** Sí, gnomos, hasta ahí estoy con vosotros.
      - **Rug merchant:** Bueno, ya han establecido Gnome Air...
      - **Player:** Continúa.
      - **Rug merchant:** De todos modos, creo que la configuración de Ali M aquí resultará realmente exitosa, y tal vez una vez que estemos establecidos adecuadamente podamos competir con esos gnomos.
      - **Player:** Vigilaré este espacio.
      - (continue)
    - (Condition: If the player has done the Feud:)
      - **Player:** Ah, sí, ahora lo recuerdo. Me embarqué en una búsqueda inútil buscando a su sobrino.
      - **Rug merchant:** ¡Ja! Sin duda el viejo Ali M. instigó todo el asunto.
      - **Player:** Aunque me divertí un poco. Todo el trabajo fue bastante divertido.
      - **Rug merchant:** Nunca hay un momento aburrido con ese hombre. Siempre está buscando una manera de ganar una moneda o dos rápidamente.
      - (continue)
    - **Rug merchant:**¿Puedo ayudarte con algo más?
    - {{anchor|question}}[Menú]: Seleccione una opción
      - [Choice]: ¿Cuéntame sobre Ali Morrisane?
        - (above|ali)
      - [Choice]: ¿Cuéntame sobre esta flota de alfombras mágicas?
        - (below|fleet)
      - [Choice]: Quiero viajar en alfombra mágica.
        - ((Magic Carpet Network interface opens.))
      - [Choice]: Tengo algunas otras preguntas.
        - (below|someother)
      - [Choice]: No gracias.
        - **Player:** No, gracias.
  - [Choice]: Háblame de esta flota de alfombras mágicas.
    - {{anchor|fleet}}**Player:** Háblame de esta flota de alfombras mágicas.
    - **Rug merchant:** La última idea del gran Ali Morrisane. Los viajes al desierto nunca volverán a ser los mismos.
    - **Player:** Entonces, ¿cómo funciona?
    - **Rug merchant:** ¿La alfombra o toda la empresa?
    - [Menu]: Selecciona una opción
      - [Choice]: La alfombra.
        - **Player:** Cuéntame cómo funciona la alfombra.
        - **Rug merchant:** No estoy muy seguro; En realidad, es solo una alfombra encantada, hecha de cabello especial Ugthanki. Vuela a cualquier destino que le ordene su dueño.
        - **Player:** ¿Están a la venta entonces?
        - **Rug merchant:** ¿Crees que estoy enojado? ¿Crees que Ali Morrisane tiraría por la borda su monopolio de la alfombra mágica?
        - **Player:** Bueno, tal vez si ofreciera el precio correcto.
        - **Rug merchant:** No es una esperanza. ¿Te imaginas el desorden que habría si la gente estuviera constantemente revisando Al Kharid y Pollnivneach? Sería un caos. De esta manera podemos mantener el tráfico de alfombras fuera de las ciudades y otros lugares concurridos.
        - **Player:** Supongo que quedar atrapado en un atasco de alfombras puede resultar un poco aburrido.
        - **Rug merchant:** Solo piense en las quemaduras por fricción que sufriría si tuviera un accidente con una alfombra.
        - **Rug merchant:** ¿Puedo ayudarte con algo más?
        - (continuea|question)
      - [Choice]: La empresa.
        - **Player:** Cuéntame sobre la empresa.
        - **Rug merchant:** En realidad, es bastante simple. Ali Morrisane nos contrató a mí y a algunas otras personas para instalar estaciones de alfombras en algunos de los lugares más poblados del desierto y realizar vuelos entre las estaciones.
        - **Player:** Entonces, ¿por qué ha limitado el servicio solo al desierto?
        - **Rug merchant:** No creo que Ali esté preparado para enfrentarse a Gnome Air todavía. Sus planeadores son mucho más rápidos que nuestras alfombras. Además de eso, creo que estamos en el negocio de las distancias cortas, algo que sólo funcionaría en condiciones duras como el desierto.
        - **Player:** ¿Por qué?
        - **Rug merchant:** Supongo que porque la gente simplemente caminaba. Perderse no es un gran problema en general, pero es diferente cuando estás en medio del Kharidian Desert con un odre de agua seco y sin idea de qué dirección tomar.
        - **Player:** Tienes razón, supongo. ¿Cómo va el negocio?
        - **Rug merchant:** No está tan mal. Los centros de conexión suelen estar bastante concurridos, pero a las estaciones de Uzer y Bedabin Camp les vendría bien un poco más de tráfico.
        - **Player:** Un mercado en crecimiento, supongo.
        - **Rug merchant:** ¿Puedo ayudarte con algo más?
        - (continuea|question)
  - [Choice]: Sí.
    - ((Magic Carpet Network interface opens.))
  - [Choice]: No, pero tenía algunas preguntas.
    - {{anchor|someother}}**Player:** Tengo algunas otras preguntas.
    - **Rug merchant:** Te ayudaré tanto como pueda.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué estás haciendo aquí?
        - **Player:** ¿Qué haces aquí?
        - (Condition: If the player is at Shantay Pass:)
          - **Rug merchant:** Bueno, esta es una buena posición para el tráfico del desierto. Shantay parece tener una pequeña y agradable configuración para generar dinero, pero creo que esto podría resultar aún mejor.
          - (continue)
        - (Condition: If the player is at the Bedabin Camp:)
          - **Rug merchant:** ¿Además de lo obvio de que yo cuide esta estación? Estoy tratando de descubrir cómo estos Tentis logran cultivar piñas tan deliciosas.
          - (continue)
        - (Condition: If the player is at Uzer:)
          - **Rug merchant:** Puede que no te des cuenta, pero ésta es una estación bastante concurrida.
          - **Player:** ¿Quién querría venir aquí?
          - **Rug merchant:** Bueno, tú por ejemplo, y además de eso, tenemos bastantes arqueólogos que pasan para examinar el golem.
          - (continue)
        - (Condition: If the player is at north Pollnivneach:)
          - **Rug merchant:** Bueno, Pollnivneach es el lugar ideal para instalar una estación de alfombras.
          - **Player:** ¿Por qué?
          - **Rug merchant:** Está ubicado a medio camino entre Al Kharid y las ciudades menafitas, y también cerca de Nardah, por lo que tenemos tráfico más que suficiente para mantener el negocio en funcionamiento.
          - (continue)
        - (Condition: If the player is at south Pollnivneach:)
          - **Rug merchant:** Trabajo aquí alquilando alfombras mágicas. Soy de Pollnivneach, por lo que es un trabajo útil. No tengo que viajar demasiado para ir a trabajar todos los días.
          - **Player:** ¿Cómo te llamas entonces?
          - **Rug merchant:** Malak. No es el nombre más notable, no es que importe, verás, todos en la ciudad me conocen como Flash.
          - **Player:** ¿En serio?
          - **Rug merchant:** No.
          - **Player:** ...
          - **Rug merchant:** ...
          - **Player:** Correcto.
          - (continue)
        - (Condition: If the player is at Nardah:)
          - **Rug merchant:** Preferiría administrar una de las estaciones de alfombras en un centro como Pollnivneach. Sin embargo, tardé un poco en conseguir ese trabajo. Aún así, el negocio en Nardah no está mal para un terminal. Al menos la gente viene aquí por el banco y por el herbolario.
          - (continue)
        - (Condition: If the player is at Menaphos:)
          - **Rug merchant:** Hasta hace poco estaba cuidando una de las estaciones de alfombras más concurridas, pero todo eso cambió una vez que Menaphos cerró sus puertas. Ahora tengo que ocupar mi día tratando de encontrar razones por las que Ali M debería mantener este lugar abierto.
          - **Player:** ¿Se te ha ocurrido alguna buena idea?
          - **Rug merchant:** En realidad, no. Me di cuenta de que se te permitió la entrada, así que sólo puedo esperar que el faraón esté cada vez más cerca de abrir las puertas nuevamente.
          - **Player:** ¿Sabes por qué se han cerrado las puertas?
          - **Rug merchant:** No tengo ni idea, aunque puede que tenga algo que ver con Sophanem. Se dice que han ocurrido algunos sucesos extraños allí, algo que tiene que ver con los sacerdotes de Icthlarin.
          - (continue)
        - (Condition: If the player is at Sophanem:)
          - **Rug merchant:** Aquí cuido la estación de alfombras. Aunque el lugar está un poco muerto. <br/>Ja! Hoho, soy demasiado.
          - **Player:** ¿Qué?
          - **Rug merchant:** Ya sabes, Sophanem, ¿la ciudad de los muertos y todo eso?
          - **Player:** ...
          - **Rug merchant:** Oh, vamos, el chiste no fue tan malo.
          - **Player:** ...
          - (continue)
        - **Rug merchant:** ¿Puedo ayudarte con algo más?
        - (continuea|question)
      - [Choice]: ¿Está cerca tu mono mascota?
        - **Player:** ¿Está cerca tu mono mascota?
        - **Rug merchant:** Es su propio mono, hace lo que le conviene, un total fastidio.
        - **Player:** Detecto cierto grado de hostilidad hacia el mono.
        - **Rug merchant:** No debería decir esto realmente, pero a veces empiezo a cuestionar algunas de las ideas de Ali Morrisane. Dice que asociar un mono con cualquier producto aumentará las ventas. ¡Simplemente no sé qué será lo próximo!
        - **Player:** ¿Ranas?
        - **Rug merchant:** Lo dudo; Los anfibios no tienen el mismo factor cursi que los monos.
        - **Player:** Estoy confundido. Pensé que no te gustaban los monos.
        - **Rug merchant:** No me desagradan los monos, es simplemente ESE mono. No lo sé, puede que esté paranoico, pero creo que él es, bueno... malvado.
        - **Player:** Mmmm, interesante.
        - (Condition: If the player has not completed Monkey Madness, or if the player has completed Monkey Madness but subsequently destroyed their monkeyspeak amulet:)
          - **Rug merchant:** ¿Puedo ayudarte con algo más?
          - (continuea|question)
        - (Condition: If the player has completed Monkey Madness, and has an amulet of monkeyspeak in their bank:)
          - **Player:** Espera un segundo, tengo un amuleto de mono en mi banco. Quizás pueda conseguirlo y ver qué tiene que decir por sí mismo.
          - (continue)
        - (Condition: If the player has completed Monkey Madness, and has an amulet of monkeyspeak in their backpack:)
          - **Player:** Espera un segundo, tengo un amuleto de mono en mi bolso. Quizás podría hablar con él.
          - (continue)
        - **Rug merchant:** ¿Lo harías? A veces me lanza estas miradas... <br/>~Un escalofrío visible recorre su espalda.
        - **Rug merchant:** Te agradecería mucho si pudieras quitarme ese mono de encima.
        - **Rug merchant:** ¿Puedo ayudarte con algo más?
        - (continuea|question)
      - [Choice]: ¿De dónde sacaste ese sombrero?
        - **Player:** ¿De dónde sacaste ese sombrero?
        - **Rug merchant:** ¿Mi fez? Lo obtuve de Ali Morrisane; es una especie de uniforme. Al parecer nos hace más visibles, pero no estoy muy seguro de ello.
        - **Player:** Bueno, es bastante distintivo.
        - **Rug merchant:** ¿Te gusta? Realmente todavía no me he decidido al respecto. Verá, no es tan práctico para las condiciones del desierto.
        - **Player:** ¿Cómo es eso?
        - **Rug merchant:** Bueno, no protege el sol de mis ojos y después de un rato sentados en el desierto, realmente empiezan a arder.
        - **Rug merchant:** ¿Puedo ayudarte con algo más?
        - (continuea|question)
  - [Choice]: *(Si el player ha completado al menos las tareas fáciles del Desierto)* Me gustaría ver qué se ha perdido y encontrado.
    - (Condition: If the player has not claimed their bag of lost items for the day:)
      - (receives=bag of lost items)
      - **Rug merchant:** Sí, he encontrado muchas cosas que no han sido reclamadas. Se caen de las mochilas de la gente cuando las alfombras se levantan. Toma, toma uno. ¡Vuelve mañana por más!
    - (Condition: If the player has claimed their bag of lost items for the day:)
      - **Rug merchant:** Lo siento, todavía no he encontrado nada. Vuelve mañana.

### Lost and found


#### Con las tareas fáciles del desierto completadas

- (receives=bag of lost items)
- **Rug merchant:** Sí, he encontrado muchas cosas que no han sido reclamadas. Se caen de las mochilas de la gente cuando las alfombras se levantan. Toma, toma uno. ¡Vuelve mañana por más!

#### Habiendo reclamado el día

- **Rug merchant:** Lo siento, todavía no he encontrado nada. Vuelve mañana.

#### Sin las tareas fáciles del Desierto completadas

- **Rug merchant:** Lo siento, no tengo nada que darte.
