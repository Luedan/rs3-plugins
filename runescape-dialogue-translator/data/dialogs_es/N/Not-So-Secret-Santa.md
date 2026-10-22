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
    - ((Having donated 50,000–99,000 value today:))
      - **Not-So-Secret-Santa:** Debes donar artículos por un valor total de al menos [número] coins para recibir una recompensa diaria.
      - (continue)
    - ((Not having donated today or having reached the daily 100,000 value:))
      - **Not-So-Secret-Santa:** Has donado suficiente riqueza para recibir tu recompensa diaria hoy. Si no lo has recibido de mí, puedes reclamarlo como reclamarías un regalo estándar de Secret Santa.
      - (continue)
    - ((Without Secret Santa unlocked:))
      - **Not-So-Secret-Santa:** Debes donar lo suficiente para reclamar una recompensa diaria en [número] días más para recibir el título de Papá Noel Secreto.
      - (initial)
    - ((With Secret Santa unlocked:))
      - **Not-So-Secret-Santa:** Has donado artículos de valor suficiente en suficientes días para recibir el título de Papá Noel Secreto.
      - (initial)

### Donate gift


#### Fuera del modo Ironman


##### Con elementos almacenados

- [Tienes recompensas que debes reclamar o abandonar antes de poder donar más artículos.]

##### Sin artículos almacenados

- ((Gift Donation interface opens.))
- (Condition: Attempting to donate items worth less than 50,000 coins:)
  - No puedes donar artículos que valgan menos de 50.000 coins.
  - (pop-up)
    - (Pop-up: You cannot donate items that are worth less than 50,000 coins.|warning=yes)
- ((After donating a gift with a value over 100,000 coins for the first time of the day:))
  - ((Gift Claim interface opens with a medium prismatic lamp.))
  - Por donar hoy artículos por valor de 100.000 coins, se le ha concedido una lámpara prismática mediana.
  - (pop-up)
    - (Pop-up: For donating 100,000 coins worth of items today, you have been awarded a medium prismatic lamp.|colour=#00FF00)
    - (continue)
  - ((Taking the lamp to backpack directly:))
    - (receives=medium prismatic lamp)
    - ((The interface closes.))
    - El cofre ahora está vacío.
  - ((Attempting to bank the lamp directly:))
    - El artículo no se pudo agregar a su banco.
  - ((Discarding the lamp directly:))
    - ((The following is shown in an interface titled "ABANDON ITEM":))
      - ¿Estás seguro de que deseas descartar este artículo?
        - [Choice]: NO
          - ((The interface closes.))
        - [Choice]: SI
          - ((The whole Gift Claim interface closes.))
  - [Choice]: BANCO TODO
    - ((Shown in a pop-up:))
      - (Pop-up: The items could not be added to your bank.|warning=yes)
  - [Choice]: TOMAR TODO
    - (receives=medium prismatic lamp)
    - ((The interface closes.))
    - Todos los artículos fueron movidos a su inventario.
    - (pop-up)
      - (Pop-up: All the items were moved to your inventory.|colour=#00FF00)
      - (continue)
    - El cofre ahora está vacío.
  - [Choice]: ABANDON ALL
    - ((The following is shown in an interface titled "ABANDON ITEM":))
      - ¿Abandonar todos los elementos restantes en el cofre?
        - [Choice]: NO
          - ((The interface closes.))
        - [Choice]: SI
          - ((Both interfaces close.))

#### En modo Ironman

- Como Ironman no puedes participar de la mayor alegría de todas: dar regalos. Todas las donaciones de Ironmen serán destruidas en una explosión controlada de acuerdo con las reglas de enfrentamiento estándar de Ironman. Cualquier residuo restante será destruido en una segunda explosión, más grande. Tu riqueza no se transferirá a otros jugadores, pero podrás recibir títulos cosméticos por tus donaciones y progreso en tareas relacionadas con la pista de yak.
- ¿Aún te gustaría donar artículos?
  - Sí.
    - ((Gift Donation interface opens.))
  - Sí y no me vuelvas a preguntar.
    - ((Gift Donation interface opens.))
  - No.
    - (end)

### Claim gift


#### Sin haber reclamado un regalo en las últimas 3 horas

- ((Gift Claim interface opens.))
- ((If the player walks away or otherwise closes the gift claim interface without taking or banking the gifts:))
  - {{Colour|#003366|WARNING:}} Si cierras sesión, los artículos del cofre de recompensas se moverán a tu inventario o banco. Si ambos lugares están llenos, perderás los artículos.
- ((Taking the gift to backpack directly:))
  - ((The interface closes.))
  - (receives=gift)
  - El cofre ahora está vacío.
- ((Banking the gift directly:))
  - ((The interface closes.))
  - ((The player banks the gift, or has coins added to money pouch if it's coins.))
  - El cofre ahora está vacío.
- ((Discarding the gift directly:))
  - ((The following is shown in an interface titled "ABANDON ITEM":))
    - ¿Estás seguro de que deseas descartar este artículo?
      - [Choice]: NO
        - ((The interface closes.))
      - [Choice]: SI
        - ((The whole Gift Claim interface closes.))
- [Choice]: BANCO TODO
  - ((The interface closes.))
  - Todos los artículos fueron trasladados a su banco.
  - (ventana emergente))
    - (Pop-up: All of the items were moved to your bank.|colour=#00FF00)
    - (continue)
  - El cofre ahora está vacío.
- [Choice]: TOMAR TODO
  - (Condition: Without sufficient backpack space:)
    - (ventana emergente))
      - (Pop-up: The items could not be added to your inventory.|warning=yes)
  - (Condition: With sufficient backpack space:)
    - ((The interface closes.))
    - (receives=gift)
    - Todos los artículos fueron movidos a su inventario.
    - (pop-up)
      - (Pop-up: All the items were moved to your inventory.|colour=#00FF00)
      - (continue)
    - El cofre ahora está vacío.
- [Choice]: ABANDONAR TODO
  - ((The following is shown in an interface titled "ABANDON ITEM":))
    - ¿Abandonar todos los elementos restantes en el cofre?
      - [Choice]: NO
        - ((The interface closes.))
      - [Choice]: SI
        - ((Both interfaces close.))

#### Haber reclamado un regalo en las últimas 3 horas

- Puedes recoger otro regalo en [time].
- (pop-up)
  - (Pop-up: You can collect another gift in [time].|warning=yes)
