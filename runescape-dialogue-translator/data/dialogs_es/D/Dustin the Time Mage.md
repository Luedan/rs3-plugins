# Dustin the Time Mage

- **Original Wiki Page**: [Transcript:Dustin the Time Mage](https://runescape.wiki/w/Transcript%3ADustin%20the%20Time%20Mage)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Durante el evento

- (Condition: Sólo la primera vez:)
  - {{#vardefineecho:Dustin|**Dustin {{Colour|#d1be88|the Time Mage}}:**}} Hola. ¡Qué bueno conocerte!
  - {{#var:Dustin}} Supongo que no podría pedir un favor. Verás, es posible que haya creado una grieta en el tiempo mismo...
  - **Player:** ¿Qué has hecho?
  - {{#var:Dustin}} Déjame explicarte. ¿Has oído la hora en que se descubrió el altar?
  - {{#var:Dustin}} ¡Por supuesto que estaba entusiasmado con el concepto de una nueva runa y con ella los nuevos hechizos que podemos lanzar!
  - {{#var:Dustin}} Pero pensé: ¿y si pudiéramos lograr aún más con esta nueva magia? Entonces comencé a experimentar...
  - {{#var:Dustin}} Sin embargo, las cosas se salieron de control y... bueno... puede que haya creado una grieta en el reino del altar del tiempo. Nada demasiado serio. Sólo un pequeño agujero.
  - {{#var:Dustin}} ¡Sin embargo, a través de ese agujero, las Arenas del Tiempo parecen estar escapando! Me vendría bien una mano amiga para recuperarlo todo mientras tapo el agujero.
  - {{#var:Dustin}} Mientras trabajemos juntos, estoy seguro de que nada terrible sucederá mientras tanto, como el fin del universo.
  - **Player:** Déjame recapitular. ¿Quieres que encuentre y recoja las Arenas del Tiempo y te las devuelva mientras reparas el 'agujero' para detener el posible fin del universo?
  - {{#var:Dustin}} ¡Exactamente eso! ¡Me alegro de que me sigas! ¡Ahora ponte en marcha! ¿O tienes más preguntas?
  - (continue|1)
- (Condition: Después:)
  - {{#var:Dustin}} Qué bueno verte de nuevo, Player.
  - (continue|1)
- [Menu]: Elige una opción:
  - [Choice]: ¿Qué está pasando?
    - (continuea|Let-me-explain)
  - [Choice]: ¿Cómo recojo Arenas del Tiempo?
    - {{#var:Dustin}} Es muy sencillo. Las Arenas del Tiempo parecen sentirse atraídas por el trabajo duro: si practicas alguna de esas habilidades y matas a los aventureros que parecen gustarles, las arenas encontrarán su camino hacia ti.
    - {{#var:Dustin}} Parece que le gustan especialmente los que entrenan a Runecrafting por lo que allí encontrarás arena en mayores cantidades. Me imagino que siente que está en casa.
    - {{#var:Dustin}} Parece que no le gustan tanto aquellos que se pasan todo el día en los bancos. Realmente tiene sentido. Si yo fuera una arena mágica, lo más probable es que también navegaría en la dirección opuesta.
    - {{#var:Dustin}} Trae la arena aquí y con gusto te recompensaré por ello.
    - (previous|1)
  - [Choice]: ¿Qué recompensas puedo obtener?
    - ¿Recompensas {{#var:Dustin}}? ¡Recompensas! Por supuesto, no es posible hacer algo a cambio de nada. Hm... déjame ver... Oh, lo sé. Puedo darte una recomendación para un sastre. Ese traje no te hace nada.
    - **Player:** ¿Qué tipo de recompensa es esa?
    - {{#var:Dustin}} ¿No es lo suficientemente bueno? Hm... está bien, ¿qué tal este mismo conjunto? Tengo un repuesto que puedes tener.
    - {{#var:Dustin}} Y... tengo algunas cajas misteriosas por ahí que nunca pude abrir. No preguntes qué contienen porque no lo sé; eso es lo que lo convierte en un misterio, pero estoy seguro de que valen la pena.
    - **Player:** Supongo que será suficiente.
    - (previous|1)
  - [Choice]: Me gustaría entregar algunas Arenas del Tiempo.
    - (below|Hand-in for rewards)
  - [Choice]: Adiós.
    - {{#var:Dustin}} Hasta la próxima.

#### Después del evento

- {{#var:Dustin}} ¡Las Arenas del Tiempo han vuelto a donde pertenecen! Gracias por tu ayuda.
- [Menu]: Elige una opción:
  - [Choice]: Me gustaría entregar algunas Arenas del Tiempo.
    - (below|Hand-in for rewards)
  - [Choice]: Adiós.
    - {{#var:Dustin}} Hasta la próxima.

### Hand-in for rewards


#### Sin Arenas del Tiempo

- No tienes nada que entregar.
- (ventana emergente)
  - (Ventana emergente: No tienes nada que entregar.|advertencia=yes)

#### Con Arenas del Tiempo


##### Aún quedan recompensas por desbloquear

- ((Lo siguiente se muestra en una interfaz titulada "Canjear moneda":))
  - Entregar la moneda del evento aumentará tu progreso en este evento y desbloqueará recompensas únicas. Esto eliminará moneda hasta la cantidad necesaria para completar el evento.
  - ¿Quieres continuar?
    - [Choice]: No
      - ((La interfaz se cierra.))
    - [Choice]: si
      - ((La interfaz se cierra y el diálogo continúa a continuación.))
- (removes=smaller number of all and as many Sands of Time as are missing from handing in 20,000)
- (Condition: Si el player no ha entregado 10.000 Arenas del Tiempo:)
  - Entregas [número] Sands of Time. Debes entregar [número]K más para completar el evento.
  - (ventana emergente)
    - (Ventana emergente: entregas [número] Sands of Time. Debes entregar [número]K más para completar el evento).
    - (continue)
- (Condition: Si el player ha entregado entre 10.000 y 19.999 Arenas del Tiempo:)
  - Entregas [número] Sands of Time. Debes entregar [número] más para completar el evento.
  - (ventana emergente)
    - (Ventana emergente: entregas [número] Sands of Time. Debes entregar [número] más para completar el evento).
    - (continue)
- (Condition: Si el player ha entregado 20.000 Arenas del Tiempo:)
  - ¡Has completado el evento!
  - (continue)
- (Condition: Dependiendo de cuánta arena haya entregado el player, se muestran algunas de estas, y luego continúa a continuación:)
  - ¡Felicitaciones! Has desbloqueado: Botas de mago del tiempo. Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
  - (ventana emergente)
    - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: Botas de mago del tiempo. Tus nuevos elementos se pueden encontrar en la interfaz de personalizaciones.|color=#00FF00)
    - (continue)
  - ¡Felicitaciones! Has desbloqueado: Guantes de mago del tiempo. Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
  - (ventana emergente)
    - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: Botas de mago del tiempo. Tus nuevos elementos se pueden encontrar en la interfaz de personalizaciones.|color=#00FF00)
    - (continue)
  - (Condition: Sin espacio backpack para una caja misteriosa de evento:)
    - No tienes suficiente espacio backpack para algunas de las recompensas. Por favor, deja algo de espacio e inténtalo de nuevo.
    - (ventana emergente)
      - (Ventana emergente: No tienes suficiente espacio backpack para algunas de las recompensas. Crea algo de espacio e inténtalo de nuevo.|advertencia=yes)
      - (continue)
  - (Condition: Con espacio backpack para una caja misteriosa de eventos:)
    - (receives=event mystery box)
    - Felicitaciones, ha recibido: 1 x Caja misteriosa del evento.
    - (continue)
  - ¡Felicitaciones! Has desbloqueado: Parte inferior de la túnica del mago del tiempo. Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
  - (ventana emergente)
    - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: Parte inferior de la túnica del mago del tiempo. Tus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.|color=#00FF00)
    - (continue)
  - ¡Felicitaciones! Has desbloqueado: Top de túnica de mago del tiempo. Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
  - (ventana emergente)
    - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: Top de túnica de mago del tiempo. Tus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.|color=#00FF00)
    - (continue)
  - ¡Felicitaciones! Has desbloqueado: Time Mage Hood. Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
  - (ventana emergente)
    - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: Top de túnica de mago del tiempo. Tus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.|color=#00FF00)
    - (continue)
  - (Condition: Sin espacio backpack para una caja misteriosa de evento:)
    - No tienes suficiente espacio backpack para algunas de las recompensas. Por favor, deja algo de espacio e inténtalo de nuevo.
    - (ventana emergente)
      - (Ventana emergente: No tienes suficiente espacio backpack para algunas de las recompensas. Crea algo de espacio e inténtalo de nuevo.|advertencia=yes)
      - (continue)
  - (Condition: Con espacio backpack para una caja misteriosa de eventos:)
    - (receives=event mystery box)
    - Felicitaciones, ha recibido: 1 x Caja misteriosa del evento.
    - (continue)
  - Has desbloqueado el título: 'Player {{ColourZZCMD0ZZ'}}|color=#00FF00}}
  - Puede activar esto a través de la pestaña 'Títulos' en la interfaz 'Personalizaciones'.
  - (Condition: Sin espacio backpack para dos cajas misteriosas de grandes eventos:)
    - No tienes suficiente espacio backpack para algunas de las recompensas. Por favor, deja algo de espacio e inténtalo de nuevo.
    - (ventana emergente)
      - (Ventana emergente: No tienes suficiente espacio backpack para algunas de las recompensas. Crea algo de espacio e inténtalo de nuevo.|advertencia=yes)
      - (continue)
  - (Condition: Con espacio backpack para dos cajas misteriosas para grandes eventos:)
    - (receives=two big event mystery boxes)
    - Felicitaciones, ha recibido: 2 x Caja misteriosa del gran evento.
    - (continue)
  - ¡Felicitaciones! Has desbloqueado: Traje de mago del tiempo cambiante. Sus nuevos artículos se pueden encontrar en la interfaz de personalizaciones.
  - (ventana emergente)
    - (Ventana emergente: ¡Felicitaciones! Has desbloqueado: Atuendo de mago en el tiempo cambiante. Tus nuevos elementos se pueden encontrar en la interfaz de personalizaciones.|color=#00FF00)
    - (continue)
- (Condition: Sin tener ninguna recompensa desbloqueada:)
  - {{#var:Dustin}} Tendrás que ayudarme un poco más antes de que pueda ofrecerte alguna recompensa.
- (Condition: Con algunas de las recompensas desbloqueadas:)
  - Has desbloqueado [number claimed]/10 de las recompensas del evento Shifting Sands.
  - (Condition: Si se acaban de reclamar algunas recompensas nuevas:)
    - {{#var:Dustin}} Gracias por tu ayuda. El tiempo ya se siente un poco más estable.
  - (Condition: Si no se acaban de reclamar nuevas recompensas:)
    - {{#var:Dustin}} Tengo recompensas adicionales para ofrecer si puedes encontrar más Arenas del Tiempo.

##### Sin recompensas por desbloquear

- Has entregado tanta moneda como puedas en este evento. Puedes convertir cualquier moneda restante en recompensas consumibles.
- (ventana emergente)
  - (Ventana emergente: has entregado toda la moneda que puedas en este evento. Puedes convertir cualquier moneda restante en recompensas consumibles.|color=#FFC800)

### Claim rewards


#### Aún quedan recompensas por desbloquear

- (above|claim)

#### Sin recompensas por desbloquear

- {{#var:Dustin}} Ya has reclamado todas las recompensas que tengo para ofrecer. Sin embargo, puedes convertir cualquier Arena del Tiempo adicional que encuentres en cajas misteriosas.
- Has desbloqueado todas las recompensas disponibles para este evento. Puedes convertir las Arenas del Tiempo restantes en cajas misteriosas.

### Open event


#### Durante el evento

- (opens=Shifting Sands)

#### Después del evento

- (abre=Interfaz#Comunidad{{!)Community}}
