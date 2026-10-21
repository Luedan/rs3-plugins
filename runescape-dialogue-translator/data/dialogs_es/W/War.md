# War

- **Original Wiki Page**: [Transcript:War](https://runescape.wiki/w/Transcript%3AWar)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Outside of War's Retreat


#### Con un nivel de combate inferior a 60

- **War:** Lo siento, Player. No puedo permitir que te unas a mí en combate aquí hasta que seas más fuerte. No quisiera que salgas gravemente herido. ¡El nivel de combate 60 debería ser suficiente!
- **War:** ¡Asegúrate de regresar cuando seas lo suficientemente fuerte y te ayudaré a convertirte en un GUERRERO PODEROSO!

#### Con un nivel de combate inferior a 60, pero al menos 1000 habilidades en total

- **War:** Lo siento, Player. No puedo permitir que te unas a mí en combate aquí hasta que seas más fuerte. No quisiera que salgas gravemente herido. ¡El nivel de combate 60 debería ser suficiente!
- **War:** Hmm... Pensándolo bien, pareces muy hábil. ¿Quizás podría hacer una excepción?
- **War:** Sí, te dejaré entrar. Sin embargo, no asumiré ninguna responsabilidad si resultas herido.
- [Menu]: ¿Quieres entrar al Retiro de War sin al menos el nivel de combate 60?
  - [Choice]: Sí. Déjame entrar.
    - (Action: La pantalla desaparece y aparece cuando el player ingresa al Retiro de War.)
  - [Choice]: No. Primero me haré más fuerte.
    - (end)

### In War's Retreat


#### Diálogo inicial

- **War:** ¡Bienvenido Player! Me alegra ver que tu sed de batalla te ha llevado hasta mí.
- **Player:** ¿Quién eres?
- **War:** Soy War, jinete retirado, guerrero curtido en batalla, entusiasta de los deportes sangrientos y propietario de este encantador refugio.
- **Player:** Sí, puedo sentir la relajación invadiéndome.
- **War:** Me alegra que tú también lo sientas, Player, ¡veo que encajarás aquí!
- **Player:** Aparte de este encantador ambiente, ambos definitivamente coincidimos en que has creado, ¿para qué sirve este lugar?
- **War:** ¡GUERREROS!
- **War:** Fomentar el talento de combate del futuro es mi nuevo pasatiempo.
- **War:** Y tú eres mi próximo proyecto.
- **Player:** ¿Qué quieres decir? ¿Qué quieres de mí?
- **War:** Quiero que luches y crezcas como guerrero. Gánate mi favor derrotando a las criaturas más fuertes de Gielinor.
- **War:** Como mi nuevo proyecto necesitaré un nombre para ti. ¿Qué tal Proyecto?
- **Player:** Bueno, supongo que es un nombre funcional al menos.
- **Player:** ¿Qué gano con esto?
- **War:** Mi retiro cuenta con varias instalaciones para ayudar al guerrero ansioso.
- **War:** Si derrotas a suficientes enemigos para ganártelo, puedo ofrecerte un teletransporte para regresarte a este retiro cuando quieras.
- (Action: La cámara se desplaza hacia los portales.)
- **War:** Mis portales pueden ser dirigidos para llevarte a cualquier jefe con el que puedas luchar, si los has derrotado una vez antes y puedes pagar el precio.
- (Action: La cámara se desplaza hacia el portal del segador.)
- **War:** Si estás ayudando a Old Boney con su cosecha, el portal del segador te llevará al objetivo que te ha asignado.
- **Player:** ¿Te refieres a la Muerte?
- **War:** ¡Así es, Viejo Boney!
- (Action: La cámara se desplaza hacia Fateful Portal.)
- **War:** El portal final se activará si hay un nuevo enemigo contra el que luchar o un evento en el que participar.
- (Action: La cámara vuelve a el player.)
- **War:** ¡También puedo otorgarte acceso a una fogata y a un altar para revitalizarte después de una batalla y a cristales adrenaline para animarte a la siguiente!
- **War:** Finalmente, cada vez que luches contra criaturas poderosas, te daré puntos para gastar. Se pueden usar para comprar auras de combate y actualizaciones de aura y vida.
- **Player:** Todo eso suena bien, aunque un poco peligroso. Lo pensaré.
- **War:** No pienses en Proyecto.
- **War:** ¡LUCHA!
- (continue|NormalDialogue)

#### Diálogo normal

- **War:** ¡Bienvenido de nuevo a mi retiro, Proyecto!
- [Menu]: Elige una opción:
  - [Choice]: ¿Puedes hablarme de ti?
    - **Player:** ¿Puedes hablarme de ti?
    - **War:** Soy War. Fui uno de los cuatro jinetes del apocalipsis, antes de retirarme.
    - **Player:** ¿Por qué te jubilaste?
    - **War:** ¡Me hice viejo! Sólo hay un tiempo para que puedas mantener el ritmo al que yo monté.
    - **Player:** Entonces, ¿qué haces ahora?
    - **War:** Aparte de una batalla en la que Old Boney me ató, he estado sediento de combate.
    - **War:** ¡Pero es por eso que comencé este retiro! Todo el mundo necesita un pasatiempo.
    - (previous|NormalDialogue)
  - [Choice]: Me gustaría hablar sobre el dominio del combate.
    - [Menu]: Elige una opción:|anchor=Maestría-Combate
      - [Choice]: ¿Qué puedes decirme sobre el dominio del combate?
        - **War:** ¡Bienvenidos de nuevo a mi Proyecto de Retiro! Tengo nuevas tareas para ti.
        - **War:** He observado tu progreso con mucho interés, Proyecto. ¡Quiero llevar tu gloria al siguiente nivel!
        - **Player:** ¿Qué tenías en mente?
        - **War:** He ideado un nuevo conjunto de tareas para ti que pondrán a prueba tu temple. ¡Por una BATALLA GLORIOSA!
        - **War:** Cuantas más tareas completes, más recompensas te otorgaré.
        - (previous|Combat-Mastery)
      - [Choice]: Muéstrame las tareas de Maestría en combate que puedo realizar.
        - ((La interfaz de logros de combate se abre en el primer grupo de logros de Combat Master disponible.))
      - [Choice]: cond=If the player has unlocked War's Blessing 4 and has not claimed the rewards:|¿Tienes alguna recompensa para mí?
        - **War:** Bien hecho Player, he reservado algunas recompensas para ti.
        - (Condition: Si el player no tiene al menos dos espacios backpack libres:)
          - **War:** Pero lamentablemente no tienes espacio para ellos.
          - (previous|Combat-Mastery)
        - (Condition: Si el player tiene al menos dos espacios backpack libres:)
          - Gizmo Shell de armadura antigua de (receives=War's Ancient Weapon Gizmo Shell (Costless) y War (sin costo)
          - (previous|Combat-Mastery)
      - [Choice]: Adiós.
        - **Player:** ¡Adiós!
        - **War:** ¡Lucha en Project, sigue luchando!
  - [Choice]: ¿Qué quieres que haga?
    - **Player:** ¿Qué quieres que haga?
    - **War:** ¡BATALLA!
    - **Player:** ¿Luchar?
    - **War:** ¡BATALLA GLORIOSA!
    - **Player:** ¿Podrías ser un poco más específico?
    - (Condition: Si el player no mata a ningún jefe:)
      - **War:** Veo que eres bastante nuevo en esto, así que señalaré algunos buenos lugares para comenzar, Proyecto.
      - **War:** Los hermanos Barrows de Morytania llevan mucho tiempo muertos y enterrados, pero eso no significa que no puedan luchar.
      - **War:** Los jardineros del parque Falador han tenido problemas con un topo gigante; sería una buena primera cacería para un guerrero novato.
      - **War:** Si te aventuras al norte de Burthorpe hacia las tierras de los trolls, podrás encontrar el lugar de una antigua batalla de los dioses. Debería ser divertido entrenar con los generales de este llamado God Wars Dungeon.
      - (continue)
    - (Condition: Si el player ya tiene jefes eliminados:)
      - **War:** ¡Derrota a criaturas poderosas! ¡Gánate mi favor! ¡Sea recompensado!
      - (continue)
    - **War:** Lucha contra los jefes y te daré puntos, devuélvemelos para obtener recompensas.
    - **War:** Cuantos más jefes mates, más acceso te otorgaré a mis instalaciones.
    - (previous|NormalDialogue)
  - [Choice]: ¿Puedes explicarme las recompensas?
    - **Player:** ¿Puedes explicarme las recompensas?
    - **War:** ¿Sobre qué recompensas te interesa saber más?
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué son las marcas de la guerra?
        - **Player:** ¿Qué son las marcas de guerra?
        - **War:** Cuando derrotes a enemigos dignos, te daré puntos para gastar. Quiero que el combate se convierta en algo habitual para ti, por eso te daré hasta 1.000 marcos por hora. Cuanto más impresionante sea el enemigo, más puntos te otorgaré.
        - **War:** Estas marcas se pueden usar para comprar auras de combate y actualizaciones de aura y vida.
        - **War:** ¡También puedes usarlos con logs para mejorar la fogata, para que puedas calentar tu corazón y cantar canciones de tu destreza en la batalla!
        - (previous|RewardExplanations)
      - [Choice]: ¿Puedes contarme sobre las opciones de transporte aquí?
        - **Player:** ¿Puedes contarme sobre las opciones de transporte aquí?
        - **War:** Si derrotas a 10 enemigos, puedo ofrecerte un teletransporte para regresarte a este retiro cuando quieras.
        - (Action: La cámara se desplaza hacia los portales.)
        - **War:** Mis portales pueden ser dirigidos para llevarte a cualquier jefe con el que puedas luchar, si los has derrotado una vez antes y puedes pagar el precio de 100,000 coins.
        - **War:** El primer portal y la primera redirección son gratuitos. Te dejaré usar el segundo portal cuando hayas derrotado a 100 enemigos impresionantes.
        - **War:** Si has matado a un jefe específico al menos 100 veces, puedes redirigir un portal hacia él por 50 000 coins.
        - (Action: La cámara se desplaza hacia el portal del segador.)
        - **War:** Si estás ayudando a Old Boney con su cosecha, el portal del segador te llevará al objetivo que te ha asignado.
        - (Action: La cámara se desplaza hacia Fateful Portal.)
        - **War:** El portal final se activará si hay un nuevo enemigo contra el que luchar o un evento en el que participar.
        - (Action: La cámara vuelve a el player.)
      - (previous|RewardExplanations)
      - [Choice]: ¿Puedes hablarme sobre el altar y los cristales adrenaline?
        - **Player:** ¿Puedes hablarme sobre el altar y los cristales adrenaline?
        - (Action: La cámara se desplaza hacia el altar de War.)
        - **War:** Puedo otorgarte acceso a mi altar para revitalizar tu oración e invocación después de la batalla...
        - (Action: La cámara se desplaza hacia los cristales adrenaline.)
        - **War:** ... ¡y cristales que te animarán a la próxima recargando tu adrenaline!
        - (Action: La cámara vuelve a el player.)
        - **War:** Ambos se pueden obtener matando 200 y 1000 criaturas poderosas, respectivamente.
        - (previous|RewardExplanations)
      - [Choice]: ¿Puedes contarme sobre la fogata?
        - **Player:** ¿Puedes contarme sobre la fogata?
        - (Action: La cámara se desplaza hacia la fogata.)
        - **War:** La fogata se puede usar para calentar tu corazón y aumentar tus puntos de vida antes de una batalla {{Sic|upcomping}}.
        - **War:** También puedes usar 1000 marcas de guerra con 1000 logs para mejorar la fogata y mejorar sus efectos.
        - (Action: La cámara vuelve a el player.)
        - (previous|RewardExplanations)
      - [Choice]: ¿Podemos hablar de otra cosa?
        - **Player:** ¿Podemos hablar de otra cosa?
        - **War:** ¡Por supuesto, Proyecto!
        - (previous2|NormalDialogue)
  - [Choice]: [More...]
    - [Menu]: Elige una opción:
      - [Choice]: Me gustaría comprar algunas recompensas.
        - **Player:** Me gustaría comprar algunas recompensas.
        - **War:** Muy bien, Proyecto.
        - (opens=War's Wares)
      - [Choice]: cond=If warnings have been turned off for reattuning a portal|¿Puedes avisarme cuando intento reajustar un portal?
        - **Player:** ¿Puedes avisarme cuando intento reajustar un portal?
        - **War:** ¡MI GRITO DE ADVERTENCIA SERÁ TAN FUERTE QUE TUS ANCESTROS LO OIRÁN!
        - **Player:** Un simple sí hubiera sido suficiente.
        - (initial|NormalDialogue)
      - [Choice]: ¡Adiós!
        - **Player:** ¡Adiós!
        - **War:** ¡Lucha en Project, sigue luchando!
      - [Choice]: [More...]
        - (initial|NormalDialogue)

#### Sintonizando el portal del jefe oriental sin haberlo desbloqueado


##### Antes de haber matado a suficientes jefes para desbloquear la función

- Debes haber matado a 100 monstruos jefes para usar esto.
- **War:** Aún no puedes usar ese Proyecto, ¡aún no has matado a suficientes enemigos dignos!

##### Habiendo matado a suficientes jefes para desbloquear la función

- **War:** Proyecto, has sembrado el mundo con los cadáveres de tus enemigos caídos.
- **War:** ¡ES HERMOSO!
- **War:** No dudes en utilizar este portal.
- Ahora puedes sintonizar el portal oriental.

#### Orando en el Altar de War sin haberlo desbloqueado


##### Antes de haber matado a suficientes jefes para desbloquear la función

- Debes haber matado a 200 monstruos jefes para usar esto.
- **War:** ¡Aún no puedes usar ese Proyecto, no has matado suficientes enemigos dignos!

##### Habiendo matado a suficientes jefes para desbloquear la función

- **War:** Proyecto, has sembrado el mundo con los cadáveres de tus enemigos caídos.
- **War:** ¡ES HERMOSO!
- **War:** Siéntete libre de usar mi altar.
- Ahora puedes usar el altar de War para restaurar los puntos de oración e invocación.

#### Usando el Grimorio de War sin haberlo desbloqueado


##### Antes de haber matado a suficientes jefes para desbloquear la función

- Debes haber matado a 750 monstruos jefes para usar esto.
- **War:** ¡Aún no puedes usar ese Proyecto, no has matado suficientes enemigos dignos!

##### Habiendo matado a suficientes jefes para desbloquear la función

- **War:** Proyecto, has sembrado el mundo con los cadáveres de tus enemigos caídos.
- **War:** ¡ES HERMOSO!
- **War:** Siéntete libre de usar mi grimorio.
- ¡Felicidades! Has completado: 'Un cambio de ritmo': desbloquea la capacidad de cambiar tu libro de hechizos usando el Grimorio de War en el Retiro de War.
- Ahora puedes cambiar tu libro de hechizos del Grimorio de War.

#### Canalizando un cristal adrenaline sin haberlo desbloqueado


##### Antes de haber matado a suficientes jefes para desbloquear la función

- Debes haber matado a 1000 monstruos jefes para usar esto.
- **War:** ¡Aún no puedes usar ese Proyecto, no has matado suficientes enemigos dignos!

##### Habiendo matado a suficientes jefes para desbloquear la función

- **War:** Proyecto, has sembrado el mundo con los cadáveres de tus enemigos caídos.
- **War:** ¡ES HERMOSO!
- **War:** Siéntete libre de canalizar adrenaline desde los cristales.
- color = verde claro

#### Canalización de un cristal adrenaline con 2000 muertes de jefes sin actualización de poción adrenaline desbloqueada

- **War:** Proyecto, has sembrado el mundo con los cadáveres de tus enemigos caídos.
- **War:** ¡ES HERMOSO!
- **War:** Siéntete libre de canalizar adrenaline desde los cristales.
- ¡Felicitaciones! Has completado: 'Second Wind': desbloquea la capacidad de actualizar el tiempo de reutilización de las pociones adrenaline usando los cristales adrenaline en el Retiro de War.
- Ahora puedes restablecer los tiempos de reutilización de las pociones adrenaline desde los cristales del jardín.

#### Comprobar tiempo de reutilización


##### Si no se han obtenido marcas de War recientemente

- **War:** Proyecto, ¡deja de quedarte aquí y sal a luchar contra algunos jefes para empezar a ganar puntos!

##### Si se han obtenido menos de 1000 marcas de War en la última hora

- **War:** Aún queda más sangre por derramar, Proyecto. Has ganado X de 1000 puntos durante este llamado a la batalla.

##### Si se han obtenido 1000 marcas de War en la última hora

- **War:** ¡Bien peleado, Proyecto! Has obtenido la cantidad máxima de puntos durante este llamado a la batalla, puedes ganar más en X minutos.

#### Resucitar a el player después de morir dentro del Retiro de War

- **War:** ¡No te morirás bajo mi vigilancia! Recuerde conseguir más comida si la necesita.

### Historical dialogue


#### Diálogo normal antes del 17 de febrero de 2025

- **War:** ¡Bienvenido de nuevo a mi retiro, Proyecto!
- [Menu]: Elige una opción:
  - [Choice]: ¿Puedes hablarme de ti?
    - (arriba)
  - [Choice]: ¿Qué quieres que haga?
    - (arriba)
  - [Choice]: ¿Puedes explicarme las recompensas?
    - (arriba)
  - [Choice]: Me gustaría comprar algunas recompensas.
    - (arriba)
  - [Choice]: [More...]
    - [Menu]: Elige una opción:
      - [Choice]: cond=If warnings have been turned off for reattuning a portal|¿Puedes avisarme cuando intento reajustar un portal?
        - (arriba)
      - [Choice]: ¿Puedes decantarme algunas pociones o medusas?
        - (below|Decanting dialogue before 17 February 2025)
      - [Choice]: ¿Puedes venderme algunas gemas de desafío?
        - **Player:** ¿Puedes venderme algunas gemas de desafío?
        - **War:** ¡Por supuesto, Proyecto! ¿Cuantos quieres?
        - [Menu]: ¿Cuántos te gustaría comprar?
          - [Choice]: Uno.
            - ((Se abre la interfaz de compra de Challenge Gem (x1) por 10 RuneCoins))
          - [Choice]: Tres.
            - ((Se abre la interfaz de compra de Challenge Gem (x3) por 25 RuneCoins))
          - [Choice]: Seis.
            - ((Se abre la interfaz de compra de Challenge Gem (x6) por 40 RuneCoins))
          - [Choice]: Ninguno, cambié de opinión.
            - **Player:** Ninguno, he cambiado de opinión.
            - **War:** No temas, ahora sabes dónde encontrarlos Proyecto. ¿Algo más?
            - (initial|NormalDialogue)

#### Decantando el diálogo antes del 17 de febrero de 2025

- [Menu]: Selecciona una opción
  - [Choice]: Decantar viales
    - [Menu]: ¿En cuántas dosis quieres decantar?
      - [Choice]: una dosis
        - (Condition: Si el player no tiene viales viables de pociones para decantar:)
          - **War:** ¡No tienes nada que decantar!
        - (Condition: Si el player no tiene espacio backpack:)
          - Buscando...
          - **War:** Tu inventario está demasiado lleno para que pueda hacer algo por ti.
        - (Condition: Si el player tiene viales viables de pociones para decantar:)
          - Buscando...
          - (Condition: Si se compraron viales adicionales de War:)
            - (receives=vials) (removes=two coins for each vial)
            - (continue)
          - **War:** Ahí lo tienes, amigo.
      - [Choice]: Dos dosis
        - (above|decant-vials)
      - [Choice]: Tres dosis
        - (above|decant-vials)
      - [Choice]: Cuatro dosis
        - (above|decant-vials)
  - [Choice]: Decantar matraces
    - (Condition: Si el player tiene matraces para decantar:)
      - **War:** Veamos qué tienes. Decantaré sus frascos de poción nuevamente en 6 frascos dosificados. Puedo hacer uso de los frascos, así que los aceptaré como pago.
      - (Action: War decanta tantas como puede hasta llenar frascos de 6 dosis)
      - **War:** Aquí tienes. ¡Eso es lo mejor que puedo hacer! Si los matraces no se ven muy diferentes, les di un clean{{Sic}}
    - (Condition: Si el player no tiene frascos viables de pociones para decantar:)
      - **War:** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener 2 matraces que no estén completamente llenos!
  - [Choice]: Convertir viales en matraces
    - (Condition: Si el player tiene matraces vacíos en backpack:)
      - **War:** Veamos qué tienes. Decantaré los viales de poción y todos los frascos con hasta 4 dosis en frascos de 6 dosis. Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos.
      - (Action: War decanta tantas pociones como puede hasta llenar frascos de 6 dosis)
      - **War:** Aquí tienes. ¡Eso es lo mejor que puedo hacer!
    - (Condition: Si el player no tiene matraces vacíos en backpack:)
      - **War:** Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos. Puedes traérmelos anotados o sin anotaciones.
  - [Choice]: Convertir matraces en viales
    - (Condition: Si el player tiene frascos de pociones para decantar en viales:)
      - **War:** Por supuesto. Creo que puedo utilizar los matraces, así que te daré los viales gratis.
      - (Action: War decanta tantas pociones como puede en viales destacados.)
      - **War:** Ahí lo tienes, ¡eso es lo mejor que puedo hacer!
    - (Condition: Si el player no tiene frascos viables de pociones para decantar:)
      - **War:** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener al menos 1 matraz!
  - [Choice]: combinar medusas
    - (Condition: Si el player tiene medusas viables para combinar:)
      - (Action: Las medusas se combinan siempre que sea posible.)
      - **War:** Ahí lo tienes.
    - (Condition: Si el player no tiene medusas viables para combinar:)
      - **War:** Lo siento, no sé cómo combinar nada de lo que llevas.
  - [Choice]: Cancelar
    - (end)
