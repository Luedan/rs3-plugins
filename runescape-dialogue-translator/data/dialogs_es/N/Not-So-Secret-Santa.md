# Not-So-Secret-Santa

- **Original Wiki Page**: [Transcript:Not-So-Secret-Santa](https://runescape.wiki/w/Transcript%3ANot-So-Secret-Santa)
- **Letter**: `N`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Verify Ironman dialogue for gift donation, claiming another gift with various time remaining, and daily reward progress}}

### Talk to

- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Not-So-Secret-Santa:** ¡Soy Santa, pero Ssshhhh! ¡Es un secreto!
    - **Player:** ¿Cómo es que es un secreto si estás vestida como él?
    - **Not-So-Secret-Santa:** ¡Esa es la idea! Si me visto como él, nadie debería sospechar que YO SOY él.
    - **Player:** Correcto.
    - **Player:** ¿Qué haces aquí?
    - **Not-So-Secret-Santa:** ¡Este año organizaré un gran juego de Secret Santa!
    - (initial)
  - [Choice]: ¿Puedes hablarme sobre el Santa Secreto?
    - **Not-So-Secret-Santa:** Hay dos fases para Secret Santa.
    - **Not-So-Secret-Santa:** Fase uno: Donar. Las personas pueden donar los artículos que tanto les costó ganar en mi bolso. Los distribuiré en la fase dos.
    - **Not-So-Secret-Santa:** No queremos ningún tatuaje, por lo que hay un valor mínimo de donación. Todo lo que des debe valer al menos 50.000 coins en Grand Exchange.
    - **Not-So-Secret-Santa:** También tengo recompensas especiales para cualquiera que vaya más allá. Cada día puedo regalarles una lámpara prismática mediana por donaciones por un valor total de 100.000 coins.
    - **Not-So-Secret-Santa:** ¡Si haces esto 15 veces, puedo darte el título de Secret Santa!
    - **Not-So-Secret-Santa:** Hay un título especial para aquellos que donan 200.000.000 coins de una vez: ¡el Papá Noel ultrasecreto!
    - **Not-So-Secret-Santa:** Fase dos: Regalo. Cualquiera puede pedirme un regalo y seleccionaré aleatoriamente un artículo de mis tiendas para entregárselo.
    - **Not-So-Secret-Santa:** Pero no te pongas codicioso, ¿eh? Sólo te dejaré recibir un regalo una vez cada 3 horas.
    - (initial)
  - [Choice]: Me gustaría hacer una donación al Santa Secreto.
    - (below|Donate gift)
  - [Choice]: Me gustaría reclamar un regalo del Papá Noel secreto.
    - (below|Claim gift)
  - [Choice]: ¿Puedes contarme sobre el progreso de mi recompensa diaria?
    - ((Habiendo donado hoy un valor de entre 50 000 y 99 000:))
      - **Not-So-Secret-Santa:** Debes donar artículos por un valor total de al menos [número] coins para recibir una recompensa diaria.
      - (continue)
    - ((No haber donado hoy o haber alcanzado el valor de 100.000 diarios:))
      - **Not-So-Secret-Santa:** Has donado suficiente riqueza para recibir tu recompensa diaria hoy. Si no lo has recibido de mí, puedes reclamarlo como reclamarías un regalo estándar de Secret Santa.
      - (continue)
    - ((Sin Secret Santa desbloqueado:))
      - **Not-So-Secret-Santa:** Debes donar lo suficiente para reclamar una recompensa diaria en [número] días más para recibir el título de Papá Noel Secreto.
      - (initial)
    - ((Con el Papá Noel secreto desbloqueado:))
      - **Not-So-Secret-Santa:** Has donado artículos de valor suficiente en suficientes días para recibir el título de Papá Noel Secreto.
      - (initial)

### Donate gift


#### Fuera del modo Ironman


##### Con elementos almacenados

- [Tienes recompensas que debes reclamar o abandonar antes de poder donar más artículos.]

##### Sin artículos almacenados

- ((Se abre la interfaz de donación de regalos.))
- (Condition: Intentar donar artículos con un valor inferior a 50 000 coins:)
  - No puedes donar artículos que valgan menos de 50.000 coins.
  - (ventana emergente)
    - (Ventana emergente: No puedes donar artículos que valgan menos de 50 000 coins.|advertencia=yes)
- ((Después de donar un regalo con un valor superior a 100 000 coins por primera vez del día:))
  - ((La interfaz de reclamo de regalo se abre con una lámpara prismática mediana.))
  - Por donar hoy artículos por valor de 100.000 coins, se le ha concedido una lámpara prismática mediana.
  - (ventana emergente)
    - (Ventana emergente: por donar 100 000 coins en artículos hoy, se le ha otorgado una lámpara prismática mediana.|color=#00FF00)
    - (continue)
  - ((Llevando la lámpara a backpack directamente:))
    - (receives=medium prismatic lamp)
    - ((La interfaz se cierra.))
    - El cofre ahora está vacío.
  - ((Intentar inclinar la lámpara directamente:))
    - El artículo no se pudo agregar a su banco.
  - ((Desechar la lámpara directamente:))
    - ((Lo siguiente se muestra en una interfaz titulada "ABANDONAR ARTÍCULO":))
      - ¿Estás seguro de que deseas descartar este artículo?
        - [Choice]: NO
          - ((La interfaz se cierra.))
        - [Choice]: SI
          - ((Se cierra toda la interfaz de Reclamo de regalo.))
  - [Choice]: BANCO TODO
    - ((Se muestra en una ventana emergente:))
      - (Ventana emergente: Los artículos no se pudieron agregar a su banco.|advertencia=yes)
  - [Choice]: TOMAR TODO
    - (receives=medium prismatic lamp)
    - ((La interfaz se cierra.))
    - Todos los artículos fueron movidos a su inventario.
    - (ventana emergente)
      - (Ventana emergente: Todos los artículos fueron movidos a su inventario.|color=#00FF00)
      - (continue)
    - El cofre ahora está vacío.
  - [Choice]: ABANDON ALL
    - ((Lo siguiente se muestra en una interfaz titulada "ABANDONAR ARTÍCULO":))
      - ¿Abandonar todos los elementos restantes en el cofre?
        - [Choice]: NO
          - ((La interfaz se cierra.))
        - [Choice]: SI
          - ((Both interfaces close.))

#### En modo Ironman

- Como Ironman no puedes participar de la mayor alegría de todas: dar regalos. Todas las donaciones de Ironmen serán destruidas en una explosión controlada de acuerdo con las reglas de enfrentamiento estándar de Ironman. Cualquier residuo restante será destruido en una segunda explosión, más grande. Tu riqueza no se transferirá a otros jugadores, pero podrás recibir títulos cosméticos por tus donaciones y progreso en tareas relacionadas con la pista de yak.
- ¿Aún te gustaría donar artículos?
  - Sí.
    - ((Se abre la interfaz de donación de regalos.))
  - Sí y no me vuelvas a preguntar.
    - ((Se abre la interfaz de donación de regalos.))
  - No.
    - (end)

### Claim gift


#### Sin haber reclamado un regalo en las últimas 3 horas

- ((Se abre la interfaz de reclamo de regalo.))
- ((Si el player se retira o cierra la interfaz de reclamo de obsequios sin aceptar ni depositar los obsequios:))
  - {{Colour|#003366|WARNING:}} Si cierras sesión, los artículos del cofre de recompensas se moverán a tu inventario o banco. Si ambos lugares están llenos, perderás los artículos.
- ((Llevando el regalo directamente a backpack:))
  - ((La interfaz se cierra.))
  - (receives=gift)
  - El cofre ahora está vacío.
- ((Depositar el regalo directamente:))
  - ((La interfaz se cierra.))
  - ((el player guarda el regalo o agrega coins a la bolsa de dinero si es coins.))
  - El cofre ahora está vacío.
- ((Descartar el regalo directamente:))
  - ((Lo siguiente se muestra en una interfaz titulada "ABANDONAR ARTÍCULO":))
    - ¿Estás seguro de que deseas descartar este artículo?
      - [Choice]: NO
        - ((La interfaz se cierra.))
      - [Choice]: SI
        - ((Se cierra toda la interfaz de Reclamo de regalo.))
- [Choice]: BANCO TODO
  - ((La interfaz se cierra.))
  - Todos los artículos fueron trasladados a su banco.
  - (ventana emergente))
    - (Ventana emergente: Todos los artículos se movieron a su banco.|color=#00FF00)
    - (continue)
  - El cofre ahora está vacío.
- [Choice]: TOMAR TODO
  - (Condition: Sin suficiente espacio backpack:)
    - (ventana emergente))
      - (Ventana emergente: Los artículos no se pudieron agregar a su inventario.|advertencia=yes)
  - (Condition: Con suficiente espacio backpack:)
    - ((La interfaz se cierra.))
    - (receives=gift)
    - Todos los artículos fueron movidos a su inventario.
    - (ventana emergente)
      - (Ventana emergente: Todos los artículos fueron movidos a su inventario.|color=#00FF00)
      - (continue)
    - El cofre ahora está vacío.
- [Choice]: ABANDONAR TODO
  - ((Lo siguiente se muestra en una interfaz titulada "ABANDONAR ARTÍCULO":))
    - ¿Abandonar todos los elementos restantes en el cofre?
      - [Choice]: NO
        - ((La interfaz se cierra.))
      - [Choice]: SI
        - ((Ambas interfaces se cierran.))

#### Haber reclamado un regalo en las últimas 3 horas

- Puedes recoger otro regalo en [time].
- (ventana emergente)
  - (Ventana emergente: Puedes recoger otro regalo en [time].|warning=yes)
