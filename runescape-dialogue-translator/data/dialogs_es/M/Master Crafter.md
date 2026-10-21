# Master Crafter

- **Original Wiki Page**: [Transcript:Master Crafter](https://runescape.wiki/w/Transcript%3AMaster%20Crafter)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Attempting to enter the Crafting Guild with under 40 Crafting

- **Master Crafter:** Lo sentimos, solo se permiten artesanos experimentados aquí. Debes tener nivel 40 o superior para ingresar.

### Entering the Crafting Guild with 40 Crafting

- **Master Crafter:** Bienvenido al Gremio de Maestros Artesanos.

### Standard dialogue

- **Master Crafter:** Hola y bienvenido al gremio Crafting. Artesanos consumados de todo el país vienen aquí para utilizar nuestros talleres de primer nivel.
- [Menu]: ¿Qué te gustaría preguntar?
  - [Choice]: ¿Qué puedo hacer aquí?
    - **Master Crafter:** El rellano superior del gremio de artesanos tiene todo lo que necesitas para adaptar armaduras.
    - **Master Crafter:** En resumen, hilas fibras vegetales en hilo en una rueca y luego tejes el hilo en tela en el telar.
    - **Master Crafter:** A continuación, elige un diseño para tu tela en la mesa de patrones, redacta tu proyecto en la mesa de dibujo y termínalo en un muñeco de sastre.
    - **Master Crafter:** Cuando hayas mejorado completamente tu armadura, podrás adornar un conjunto completo en la exhibición del sastre. Es una experiencia admirable.
    - **Master Crafter:** Pero primero, necesitarás semillas para plantar en parches de flores y obtener las flores que hilarás.
    - **Master Crafter:** No sé mucho sobre las flores estelares. Quizás puedas descubrir más en el gran telescopio del Wizards' Tower.
    - **Player:** Muy bien, le preguntaré a Wizard Rosalina. Quizás tenga algo que ver con las estrellas fugaces.
    - **Master Crafter:** Otra cosa que quizás te gustaría probar es crear y encantar joyas de platino.
    - [Puedes extraer mineral de platino al norte de Uzer y al sur de Piscatoris.]
    - **Master Crafter:** Si eres muy bueno fabricando, también podrías tener una oportunidad con una armadura mágica de gran calidad. Puedes encontrar la receta en la mesa de patrones a mi lado.
    - **Master Crafter:** Recuerda, tela en telar. Hilo en una rueca. En cuanto a las piedras de unión, quizás pruebes con el Gremio de Magos en Yanille.
    - **Master Crafter:** Y necesitarás esencia tectónica y praesúlica para empezar a elaborar placas nacaradas. El platino normalmente no sería adecuado para armaduras, pero la imbución lo niega.
    - (initial)
  - [Choice]: Intercambio de piezas de enfoque de Summoning.
    - (below|Trade Summoning Focus Parts)
  - [Choice]: Armadura maestra hecha a medida.
    - **Master Crafter:** Si tienes un conjunto completamente equipado de obra maestra cuerpo a cuerpo recortada, obra maestra a distancia o magia maestra, puedo personalizarlo para ti. Si está aumentado, permanecerá aumentado y lo repararás de la misma manera que reparas una obra maestra recortada.
    - **Player:** ¿Qué hace el ajuste personalizado?
    - **Master Crafter:** Se volverá intransferible.
    - **Master Crafter:** Se degradará un 50 % más lento, por lo que durará más.
    - **Master Crafter:** Tampoco se degradará nunca cuando sea dañado por tu objetivo actual Slayer/Reaper.
    - **Master Crafter:** Pero el proceso es irreversible. Una vez hecha a medida, su obra maestra siempre estará hecha a medida.
    - (Condition: Mientras no uses un conjunto maestro completo de cuerpo a cuerpo, a distancia o mágico:)
      - [Debes llevar un conjunto completo de obra maestra cuerpo a cuerpo recortada, obra maestra a distancia o magia maestra para adaptarlo a la medida.]
    - (Condition: Mientras usas un conjunto de magia de obra maestra completa:)
      - [¿Estás seguro de que quieres personalizar tu armadura maestra? Este proceso los hará permanentemente intransferibles, hará que se degraden un 50% más lento y nunca se degradarán cuando sean dañados por tu objetivo actual Slayer/Reaper.]
      - [Menu]: ¿Perfeccionar tu armadura maestra a la medida?
        - [Choice]: si
          - ((toda la armadura usada de obra maestra está hecha a medida))
      - [Choice]: No
          - (end)
    - (Condition: Mientras llevas un conjunto a distancia de obra maestra completa:)
      - [¿Estás seguro de que quieres personalizar tu armadura maestra? Este proceso los hará permanentemente intransferibles, hará que se degraden un 50% más lento y nunca se degradarán cuando sean dañados por tu objetivo actual Slayer/Reaper.]
      - [Menu]: ¿Perfeccionar tu armadura maestra a la medida?
        - [Choice]: si
          - ((toda la armadura usada de obra maestra está hecha a medida))
      - [Choice]: No
          - (end)
  - [Choice]: Skillcapes.
    - [Menu]: ¿Qué pasa con skillcapes?
      - [Choice]: Skillcape de Crafting.
        - (Condition: Si el player no tiene 99 Crafting:)
          - **Player:** Oye, ¿qué es esa capa que llevas puesta? No lo reconozco.
          - **Master Crafter:** ¿Esto? Este es un Skillcape de Crafting. Es un símbolo de mi habilidad y de mi posición aquí en el Gremio Crafting. Si alguna vez alcanzas 99 Crafting, ven y habla conmigo y veremos si podemos solucionarlo con uno.
        - (Condition: Si el player tiene 99 Crafting y tiene un ring of charos(a) equipado:)
          - **Master Crafter:** No hago esto por nadie, ¡pero hoy tengo una oferta especial! Normalmente necesito 99.000 coins por este prestigioso artículo, pero para ti es la mitad de precio. ¡Solo 92.000 coins!
          - [Menu]: Elige una opción:
            - [Choice]: ¿92.000 coins? Eso es demasiado caro.
              - **Player:** Sé dónde encontrarte si cambio de opinión.
            - [Choice]: De hecho, creo que tengo el dinero aquí.
              - (Condition: Si el player no tiene espacio backpack:)
                - **Master Crafter:** Lamentablemente, todos los skillcapes solo están disponibles con una capucha gratuita, es parte de un acuerdo de promoción de habilidades; Compra uno y llévate otro gratis, ya sabes. Por lo tanto, necesitarás liberar algo de espacio en backpack antes de que pueda venderte uno.
              - (Condition: Si el player no tiene suficiente dinero:)
                - **Player:** Pero desafortunadamente me equivoqué.
                - **Master Crafter:** Bueno, vuelve a verme cuando lo hagas.
              - (Condition: Si el player tiene suficiente dinero:)
                - (receives=Crafting cape and Crafting hood) (removes=92,000 coins)
                - **Master Crafter:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
            - [Choice]: cond=If the player has 120 Crafting|He dominado esta habilidad. ¿Hay algo más?
              - **Master Crafter:** Hay algo... aunque lo he mantenido en secreto durante mucho tiempo. Es algo que sólo puede ser usado por un verdadero maestro.
              - **Master Crafter:** Ni siquiera yo puedo usarlo, así de difícil es lograrlo.
              - **Master Crafter:** Dices que eres un maestro. Ponte derecho, déjame echarte un vistazo...
              - **Master Crafter:** Tú... realmente lo dominas. ¡Qué honor! Sería un placer venderle un Crafting master cape.
              - [Menu]: ¿Comprar Crafting master cape por 120.000 coins?
                - [Choice]: Sí.
                  - (Condition: Si el player no tiene espacio backpack:)
                    - **Master Crafter:** No tienes suficiente espacio en tu backpack. Por favor regresa cuando tengas más.
                  - (Condition: Si el player no tiene suficiente dinero:)
                    - No tienes suficiente dinero para comprar esta capa.
                  - (Condition: Si el player tiene suficiente dinero:)
                    - (receives=Crafting master cape) (removes=120,000 coins)
                    - (Action: Suena música Master cape.)
                - [Choice]: No.
                  - (end)
        - (Condition: Si el player tiene 99 Crafting pero no tiene un ring of charos(a) equipado:)
          - [Menu]: Elige una opción:
            - [Choice]: ¿99.000 coins? Eso es demasiado caro.
              - **Player:** Sé dónde encontrarte si cambio de opinión.
            - [Choice]: De hecho, creo que tengo el dinero aquí.
              - (Condition: Si el player no tiene espacio backpack:)
                - (arriba)
              - (Condition: Si el player no tiene suficiente dinero:)
                - (arriba)
              - (Condition: Si el player tiene suficiente dinero:)
                - (receives=Crafting cape and Crafting hood) (removes=99,000 coins)
                - **Master Crafter:** ¡Excelente! Lleva esa capa con orgullo, amigo mío.
            - [Choice]: cond=If the player has 120 Crafting|He dominado esta habilidad. ¿Hay algo más?
              - (arriba)
      - [Choice]: cond=If the player has 99 Crafting|He notado que hay un par de versiones de cada skillcape.
        - **Master Crafter:** ¡Sí! ¡Nosotros, los maestros de habilidades, hemos creado nuevas versiones de todos los skillcapes! Sentimos que era hora de un cambio.
        - (Condition: Si el player utiliza el modelo antiguo:)
          - **Master Crafter:** Parece que actualmente estás usando el modelo anterior para tu Crafting skillcape. ¿Quieres cambiar a uno más nuevo?
          - (continue)
        - (Condition: Si el player está utilizando el nuevo modelo:)
          - **Master Crafter:** Aún puedes elegir usar el modelo antiguo skillcape si lo deseas. ¿Le gustaría cambiar el modelo que está utilizando actualmente?
          - (continue)
        - [Menu]: Selecciona una opción
          - [Choice]: Sí, me gustaría usar la versión [new/old] del skillcape.
            - **Master Crafter:** ¿Te gustaría usar el modelo [old/newer] solo para esta capa, o para el Quest Cape y todos los skillcapes que tienes?
            - [Menu]: Selecciona una opción
              - [Choice]: Solo me gustaría cambiar el Crafting skillcape.
                - **Master Crafter:** No hay problema, ahora utilizarás el modelo [older/newer] para tu Crafting skillcape.
              - [Choice]: Me gustaría cambiar todos mis skillcapes.
                - **Master Crafter:** ¡No hay problema, ahora usarás el modelo [older/newer] para todos tus skillcapes!
              - [Choice]: ¡He cambiado de opinión!
                - (end)
          - [Choice]: No, gracias.
            - **Master Crafter:** ¡Genial! ¡Me alegra que sigas disfrutando de la versión [old/new]!
            - (Condition: Si el player usa el nuevo modelo para cualquier otro skillcape:)
              - **Master Crafter:** Si quieres, puedo hacerlo para que uses el modelo antiguo para todos los skillcapes que tengas.
              - [Menu]: Selecciona una opción
                - [Choice]: Ok, me gustaría usar la versión antigua para todos mis skillcapes.
                  - **Master Crafter:** ¡Genial, ahora usarás el modelo antiguo para todos tus skillcapes!
                - [Choice]: No, gracias.
                  - (end)

### Trade Summoning Focus Parts


#### Sin partes de enfoque o en un mundo gratuito

- **Master Crafter:** No tienes ninguna parte de enfoque de Summoning contigo. Puede obtenerlos utilizando un catalizador Crafting. Si consigues alguna pieza te la puedo cambiar.

#### Con partes de enfoque

- **Player:** Me gustaría intercambiar algunas partes del enfoque de Summoning, por favor.
- {{anchor|exchange}} **Master Crafter:** ¿Qué pieza te gustaría intercambiar?
- [Menu]: Seleccionar parte
  - [Choice]: Funda de cuero
    - **Master Crafter:** Vale, ¿y por cuál te gustaría cambiarlo?
    - [Menu]: Seleccionar parte
      - [Choice]: Funda de cuero
        - **Master Crafter:** Es el mismo que ya tienes.
        - (continuea|exchange)
      - [Choice]: Enfoque de gema
        - **Master Crafter:** ¿Cuántos te gustaría intercambiar?
        - {{tinput|Enter amount:}}
          - (Condition: Si se ingresa cero:)
            - (end)
          - ((Después de ingresar una cantidad positiva:))
            - ((Player recibe un foco de gema por cada estuche de cuero entregado.))
            - **Master Crafter:** Ahí lo tienes, ¿te gustaría intercambiar algo más?
            - {{anchor|anything-else}} [Menú]: seleccione una opción
              - [Choice]: Sí por favor.
                - (continuea|exchange)
              - [Choice]: No, gracias.
                - (end)
      - [Choice]: Engaste de metales
        - **Master Crafter:** ¿Cuántos te gustaría intercambiar?
        - {{tinput|Enter amount:}}
          - (Condition: Si se ingresa cero:)
            - (end)
          - ((Después de ingresar una cantidad positiva:))
            - ((Player recibe un engaste de metal por cada estuche de cuero entregado.))
            - **Master Crafter:** Ahí lo tienes, ¿te gustaría intercambiar algo más?
            - (continuea|anything-else)
  - [Choice]: Enfoque de gema
    - **Master Crafter:** Vale, ¿y por cuál te gustaría cambiarlo?
    - [Menu]: Seleccionar parte
      - [Choice]: Funda de cuero
        - **Master Crafter:** ¿Cuántos te gustaría intercambiar?
        - {{tinput|Enter amount:}}
          - (Condition: Si se ingresa cero:)
            - (end)
          - ((Después de ingresar una cantidad positiva:))
            - ((Player recibe un estuche de cuero por cada foco de gema entregado.))
            - **Master Crafter:** Ahí lo tienes, ¿te gustaría intercambiar algo más?
            - (continuea|anything-else)
      - [Choice]: Enfoque de gema
        - **Master Crafter:** Es el mismo que ya tienes.
        - (continuea|exchange)
      - [Choice]: Engaste de metales
        - **Master Crafter:** ¿Cuántos te gustaría intercambiar?
        - {{tinput|Enter amount:}}
          - (Condition: Si se ingresa cero:)
            - (end)
          - ((Después de ingresar una cantidad positiva:))
            - ((Player recibe un engaste de metal por cada foco de gema entregado.))
            - **Master Crafter:** Ahí lo tienes, ¿te gustaría intercambiar algo más?
            - (continuea|anything-else)
  - [Choice]: Engaste de metales
    - **Master Crafter:** Vale, ¿y por cuál te gustaría cambiarlo?
    - [Menu]: Seleccionar parte
      - [Choice]: Funda de cuero
        - **Master Crafter:** ¿Cuántos te gustaría intercambiar?
        - {{tinput|Enter amount:}}
          - (Condition: Si se ingresa cero:)
            - (end)
          - ((Después de ingresar una cantidad positiva:))
            - ((Player recibe un estuche de cuero por cada engaste de metal entregado.))
            - **Master Crafter:** Ahí lo tienes, ¿te gustaría intercambiar algo más?
            - (continuea|anything-else)
      - [Choice]: Enfoque de gema
        - **Master Crafter:** ¿Cuántos te gustaría intercambiar?
        - {{tinput|Enter amount:}}
          - (Condition: Si se ingresa cero:)
            - (end)
          - ((Después de ingresar una cantidad positiva:))
            - ((Player recibe un foco de gema por cada engaste de metal entregado.))
            - **Master Crafter:** Ahí lo tienes, ¿te gustaría intercambiar algo más?
            - (continuea|anything-else)
      - [Choice]: Engaste de metales
        - **Master Crafter:** Es el mismo que ya tienes.
        - (continuea|exchange)
  - [Choice]: Cancelar
    - (end)

### Custom-fit Trimmed Masterwork

- (above|custom-fit-dialogue)

### During the Master Crafting event


#### Ingresando al gremio Crafting

- **Master Crafter:** Bienvenido al Gremio de Maestros Artesanos.
- **Master Crafter:** ¡Actualmente estamos organizando un evento de artesanía maestra! Ven y habla conmigo para más información.

#### Obteniendo un nivel Crafting

- **Master Crafter:** {{RSChat|Congratulations for advancing a crafting level, Player!}}

#### Intentar usar el cofre del banco temporal antes de desbloquearlo

- **Master Crafter:** Lo sentimos, no puedes usar ese cofre del banco hasta que lo hayas desbloqueado como parte del evento Master Crafting. Si me entregas al menos 800 parches Master Crafting, los desbloquearé.

#### Habla con

- **Master Crafter:** Hola y bienvenido al gremio Crafting. Actualmente estamos organizando un evento de artesanía magistral, ¡estamos invitando a artesanos de todo el país a venir aquí y utilizar nuestros talleres de primer nivel!
- [Menu]: ¿Sobre qué te gustaría preguntar?
  - [Choice]: ¡El evento de artesanía magistral!
    - **Master Crafter:** Sí, ¡bienvenido al gremio de artesanía y a nuestro evento de artesanía maestra!
    - **Master Crafter:** ¿En qué puedo ayudarte?
    - [Menu]: ¿Qué te gustaría preguntar?
      - [Choice]: ¿Cómo funciona este evento?
        - **Player:** ¿Cómo funciona esto?{{anchor|how}}
        - **Master Crafter:** Bueno, he abierto las puertas del gremio de artesanía a todos los aventureros, para que todos puedan participar.
        - **Master Crafter:** En todo el mundo puedes encontrar parches de creación mientras realizas habilidades, actividades de combate o desafíos diarios.
        - **Master Crafter:** ¡Si me traes estos parches, puedo otorgarte increíbles recompensas y beneficios!
        - [Menu]: ¿Qué te gustaría preguntar?
          - [Choice]: ¿Qué increíbles recompensas?
            - **Master Crafter:** Recompensas, ¡ah, sí!{{anchor|rewards}}
            - **Master Crafter:** ¡Tengo toda una selección de cosméticos para regalar!
            - **Master Crafter:** ¡Como estas increíbles botas que estoy usando!
            - **Master Crafter:** ¡Y estos guantes excepcionales!
            - **Player:** ¿Todo tu conjunto?
            - **Master Crafter:** Sí.
            - Puedes desbloquear el conjunto master crafter que contiene: gafas, peto, pantalones, guantes y botas.
            - **Player:** ¿Puedo conseguir algo más?
            - **Master Crafter:** ¡Por supuesto! ¡Tengo una variedad de herramientas que puedes usar para todas tus necesidades de matar monstruos!
            - **Master Crafter:** Un destornillador que podría usarse como un dagger.
            - **Master Crafter:** Un martillo, que podría usarse como una maza.
            - **Master Crafter:** ¡Una sierra que podría usarse como una scimitar!
            - **Master Crafter:** Y un hacha, que sabes que podría usarse para hacer hachas.
            - Puedes desbloquear varias anulaciones de armas maestras: una sierra, un hacha, un destornillador y un martillo.
            - [Menu]: ¿Qué te gustaría preguntar?
              - [Choice]: ¿Cómo funciona este evento?
                - (above|how)
              - [Choice]: ¿Hay otros beneficios?
                - **Player:** ¿Hay algún otro beneficio que pueda obtener de este evento?{{anchor|benefits}}
                - **Master Crafter:** ¡Por supuesto! ¡Me las arreglé para organizar todo tipo de beneficios para el gremio de artesanía que estarán vigentes durante todo el evento!
                - **Master Crafter:** Si estás dentro del gremio, ¡me las arreglé para obtener un beneficio de experiencia para todas las habilidades de +5 % de XP, durante todo el evento!
                - **Master Crafter:** También logré obtener un beneficio de +10% de XP para la elaboración, ¡y se acumulan!
                - **Master Crafter:** Si has donado al menos 800 monedas, puedes usar este útil cofre del banco que llevé al gremio.
                - **Master Crafter:** Sin embargo, lo retiraré después del evento, ¡está prestado y no puedo permitirme el lujo de conservarlo aquí!
                - **Master Crafter:** ¡Si has donado al menos 5000 monedas, recibirás una mejora en la elaboración de joyas!
                - Mejora de la elaboración de joyas (dentro del gremio de artesanía):
                - +250% XP al fundir lingotes de oro y plata
                - Fundición de oro y plata un 50% más rápida
                - +33 % más rápido en el lanzamiento de oro y plata.
                - **Master Crafter:** ¡Si has donado al menos 10 000 monedas, recibirás un beneficio minero!
                - Mejora Mining (dentro del gremio de artesanos):
                - +50% XP al extraer rocas de oro y plata
                - Mining Clay ahora proporciona arcilla blanda.
                - **Master Crafter:** ¡Si has donado al menos 20 000 monedas, recibirás una mejora en la elaboración de urnas!
                - Mejora de la elaboración de urnas (dentro del gremio de artesanía):
                - +50% más rápido en la elaboración del torno de alfarería
                - Elaboración de hornos de cerámica un 80% más rápido
                - +100% XP al fabricar urnas
                - **Master Crafter:** Realmente espero que disfrutes de estos beneficios, sin embargo, desaparecerán una vez finalizado el evento, solo he logrado asegurarlos por un corto tiempo.
                - **Master Crafter:** ¿Hay algo más en lo que pueda ayudarte?
                - [Menu]: ¿Qué te gustaría preguntar?
                  - [Choice]: ¿Cómo funciona este evento?
                    - (above|how)
                  - [Choice]: ¿Qué recompensas puedo obtener?
                    - (above|rewards)
          - [Choice]: ¿Qué increíbles beneficios?
            - (above|benefits)
          - [Choice]: ¡Me gustaría entregar moneda!
            - (below|Hand in)
          - [Choice]: Espera, ¿cómo consigo esos parches?
            - **Master Crafter:** Obtienes los parches del combate, las habilidades o los desafíos diarios.
            - [Menu]: ¿Qué te gustaría preguntar?
              - [Choice]: ¿Qué recompensas puedo obtener?
                - (above|rewards)
              - [Choice]: ¿Hay otros beneficios?
                - (above|benefits)
              - [Choice]: ¡Me gustaría entregar moneda!
                - (below|Hand in)
              - [Choice]: ¿Pero cómo?
                - **Player:** ¿Pero cómo?
                - *(Sólo la primera vez:)*
                  - **Player:** ¿Cómo tienen los monstruos estos parches? ¿Cómo aparecen mientras estoy creando?
                  - (continue)
                - *(Se muestra una de las siguientes opciones y luego regresa a las opciones anteriores:)*
                  - **Master Crafter:** Porque tengo una muy, muy, muy buena amistad con el guardián del mundo.
                  - **Master Crafter:** Porque yo lo dije.
                  - **Master Crafter:** Porque pasé mucho tiempo dándole a cada monstruo.
                  - **Master Crafter:** Porque no he tenido nada mejor que hacer durante los últimos 11 años.
                  - **Master Crafter:** Porque alguien te está siguiendo, sutilmente lanzando parches en tu backpack.
                  - **Master Crafter:** Porque los creadores así lo dijeron.
                  - **Master Crafter:** ¿Porque los crearás accidentalmente?
                  - **Master Crafter:** Porque los encontrarás.
                  - **Master Crafter:** Magic.
                  - **Master Crafter:** Por favor, no vuelvas a preguntarme cómo.
                  - **Master Crafter:** Razones.
                  - **Master Crafter:** ¿Sabes que a veces compras una camisa y solo viene con dulces extra? Es así pero con parches.
      - [Choice]: ¿Qué recompensas puedo obtener?
        - (above|rewards)
      - [Choice]: ¿Hay otros beneficios?
        - (above|benefits)
      - [Choice]: ¡Me gustaría entregar moneda!
        - (below|Hand in)
  - [Choice]: Skillcape de Crafting.
    - *(Diálogo sin evento.)*
  - [Choice]: He notado que hay un par de versiones de cada skillcape.
    - *(Diálogo sin evento.)*
  - [Choice]: Un enfoque Summoning.
    - *(Diálogo sin evento.)*

#### Entregar


##### Durante el evento


##### Sin parches de elaboración maestra

- No tienes nada que entregar.

##### Con parches de artesanía maestros


##### Aún quedan recompensas por desbloquear

- Canjear moneda
- Entregar la moneda del evento aumentará tu progreso en este evento y desbloqueará recompensas únicas. Esto eliminará moneda hasta la cantidad necesaria para completar el evento.
- [Menu]: ¿Quieres continuar?
  - [Choice]: No
    - (end)
  - [Choice]: si
    - Entregas los parches de elaboración de [número] Master. Debes entregar [numberK or number] más para completar el evento.
    - ((Si las recompensas no se desbloquearon y no se han desbloqueado recompensas anteriormente:))
      - **Master Crafter:** Debes traerme más parches de artesanía si quieres reclamar más recompensas.
    - ((Si las recompensas estuvieran desbloqueadas:))
      - ((Si el cofre del banco está desbloqueado:))
        - Felicitaciones, has desbloqueado la capacidad de usar el cofre del banco dentro del gremio de artesanos durante la duración del evento.
        - (continue)
      - ((Si las gafas master crafter están desbloqueadas:))
        - Felicitaciones, ha desbloqueado la anulación de las gafas Master Crafter. Puede encontrar esto en la interfaz de personalizaciones.
        - (continue)
      - ((Si la sierra master crafter está desbloqueada:))
        - Felicitaciones, ha desbloqueado la anulación de la sierra Master Crafter. Puede encontrar esto en la interfaz de personalizaciones.
        - (continue)
      - ((Si los beneficios de joyería están desbloqueados:))
        - Tienes los siguientes beneficios de fundición de joyas dentro del gremio de artesanos durante la duración del evento.
        - +250% XP al fundir lingotes de oro y plata.
        - Fundición de Oro y Plata +50% más rápida.
        - +33 % más rápido en el lanzamiento de oro y plata.
        - (continue)
      - ((Si los guantes master crafter están desbloqueados:))
        - Felicitaciones, ha desbloqueado la anulación de guantes Master Crafter. Puedes encontrarlos en la interfaz de personalizaciones.
        - (continue)
      - ((Si las botas master crafter están desbloqueadas:))
        - Felicitaciones, ha desbloqueado la anulación de botas Master Crafter. Puedes encontrarlos en la interfaz de personalizaciones.
        - (continue)
      - ((Si los beneficios mineros están desbloqueados:))
        - Tienes los siguientes beneficios de fundición de joyas dentro del gremio de artesanos durante la duración del evento.
        - +50% XP al extraer rocas de oro y plata.
        - Mining Clay ahora proporciona arcilla blanda.
        - (continue)
      - ((Si los pantalones master crafter están desbloqueados:))
        - Felicitaciones, ha desbloqueado la anulación de pantalones Master Crafter. Puedes encontrarlos en la interfaz de personalizaciones.
        - (continue)
      - ((Si la campana master crafter está desbloqueada:))
        - Felicitaciones, ha desbloqueado la anulación de la campana Master Crafter. Puedes encontrarlos en la interfaz de personalizaciones.
        - (continue)
      - ((Si el martillo master crafter está desbloqueado:))
        - Felicitaciones, ha desbloqueado la anulación del martillo Master Crafter. Puede encontrar esto en la interfaz de personalizaciones.
        - (continue)
      - ((Si el destornillador master crafter está desbloqueado:))
        - Felicitaciones, ha desbloqueado la anulación del destornillador Master Crafter. Puede encontrar esto en la interfaz de personalizaciones.
        - (continue)
      - ((Si el hacha master crafter está desbloqueada:))
        - Felicitaciones, ha desbloqueado la anulación del hacha Master Crafter. Puede encontrar esto en la interfaz de personalizaciones.
        - (continue)
      - ((Si los beneficios de la urna están desbloqueados:))
        - ¡Has completado el evento!
        - Tienes los siguientes beneficios de elaboración de urnas dentro del gremio de artesanía durante la duración del evento.
        - Elaboración un 50 % más rápida con el torno de alfarero.
        - Elaboración un 80 % más rápida con el horno de cerámica.
        - +100% XP al fabricar urnas.
        - (continue)
      - (continue)
    - ((Si algunas de las recompensas han sido desbloqueadas:))
      - Has desbloqueado [número]/13 de las recompensas del evento Master Crafter.
      - ((Si aún quedan recompensas por desbloquear y no hay ninguna recompensa o el cofre del banco acaba de desbloquearse:))
        - **Master Crafter:** Tenemos más recompensas que ofrecer, si me traes más fichas de habilidad.
      - ((Si se acaba de desbloquear una recompensa distinta al cofre del banco:))
        - **Master Crafter:** ¡Ahí estás!

##### Con todas las recompensas desbloqueadas

- Has entregado tanta moneda como puedas en este evento. Puedes convertir cualquier moneda restante en recompensas consumibles.

##### Después del evento

- El evento master crafter ha finalizado, sin embargo, aún puedes convertir los tokens sobrantes en cajas misteriosas.
- ((Continúa con el diálogo normal.))

#### Evento abierto


##### Durante el evento

- (abre=Maestría en artesanía{{!)Event}}

##### Después del evento

- El evento master crafter ha finalizado, sin embargo, aún puedes convertir los tokens sobrantes en cajas misteriosas.
- ((Continúa con el diálogo normal.))
