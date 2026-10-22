# Juna

- **Original Wiki Page**: [Transcript:Juna](https://runescape.wiki/w/Transcript%3AJuna)
- **Letter**: `J`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

Después de completar la misión Tears of Guthix, los jugadores tienen la opción de recolectar lágrimas una vez a la semana. Para hacerlo, los jugadores primero deben contarle a Juna una historia de sus viajes y aventuras. Cada historia se puede vincular a una misión realizada en el pasado.

### Dialogue

Tenga en cuenta que estos diálogos pueden estar relacionados con una historia o no. Los diálogos relacionados con las historias se enumeran en la sección Lista de historias, mientras que los que aparecen a continuación son para diálogos no relacionados con las historias.
- **Juna:** Cuéntame... una historia...
- [Menu]: Elige una opción:
  - [Choice]: Está bien...
    - **Player:** Está bien...
    - Le cuentas a Juna algunas historias de tus aventuras.
    - *Consulta la sección Lista de historias a continuación*
    - (Condition: If the player can go in:)
      - **Juna:** Tus historias me han entretenido. Te dejaré entrar a la cueva por un corto tiempo.
      - (Condition: If the player is not under the effect of Enlightenment:)
      - (Condition: If a light creature is summoned and the player has a Light creature scroll (Enlightenment) in their inventory:)
        - **Juna:** Veo que actualmente no estás iluminado, pero tienes una criatura de luz invocada, así como un pergamino que puedes usar en tu inventario.
        - (continue)
      - (Condition: If a light creature is summoned and the player has at least one Light creature scroll (Enlightenment) stored in their light creature:)
        - **Juna:** Veo que actualmente no estás iluminado, pero tienes una criatura de luz convocada y la criatura de luz sostiene un pergamino que puede usar.
        - (continue)
      - (Condition: If a light creature is not summoned but the player has the ability:)
        - **Juna:** Veo que actualmente no estás iluminado, pero tienes en tu inventario una bolsa de criatura ligera y un pergamino que puedes usar.
        - (continue)
        - [Menu]: ¿Quieres recoger las lágrimas de todos modos?
          - [Choice]: Sí, entiendo que ninguna de las lágrimas que recolecte será duplicada.
            - **Player:** Sí, entiendo que ninguna de las lágrimas que recoja se duplicará.
            - (Continues below)
          - [Choice]: No, gracias, primero me gustaría transmitir la iluminación.
            - **Player:** No, gracias. Primero me gustaría transmitir la iluminación.
            - **Juna:** Como desees, Player.
            - (end)
    - **Juna:** Recoge todo lo que puedas de las corrientes azules. Si dejas entrar agua de los arroyos verdes, se la quitará a los azules. Porque Guthix es el dios del equilibrio, y el equilibrio reside en la yuxtaposición de los opuestos.
  - (Condition: If the player cannot go in due to already having collected tears that week:)
    - **Juna:** Tus historias me han entretenido. Pero no permitiré que ningún aventurero acceda a las lágrimas más de una vez por semana. Vuelve en # días.
  - (Condition: If the player cannot go in due to Clan Avatar is summoned:)
    - **Juna:** Tus historias me han entretenido, pero la creación de Armadyl que te sigue no entrará en mi cueva. Deséchalo y regresa a mí.
  - [Choice]: cond=If the player is eligible to make an ornate bowl and has talked to Juna about it:|¿Cómo hago el cuenco mejorado?
    - (abajo2|instrucciones-de-tazón-adornado)
  - [Choice]: ¿Una historia?
    - **Player:** ¿Una historia?
    - **Juna:** He estado esperando aquí durante tres mil años, guardando las Lágrimas de Guthix. Sirvo fielmente a mi amo, pero estoy aburrido.
    - **Juna:** Un aventurero como tú debe tener muchas historias que contar. Si puedes entretenerme, te dejaré entrar a la cueva por un tiempo.
    - **Juna:** Cuanto más disfrute tu historia, más tiempo te daré en la cueva.
    - **Juna:** Entonces podrás beber el poder del equilibrio, que te hará más fuerte en cualquier área en la que estés más débil.
      - **Player:** Está bien... (ver arriba)
        - **Player:** Ahora no.
      - **Player:** ¿Qué son las Lágrimas de Guthix?
        - **Juna:** La Tercera Edad del mundo fue una época de gran conflicto, de destrucción nunca vista antes ni después, cuando todos los dioses, excepto Guthix, lucharon por el control.
        - **Juna:** Los colosales wyrms, de los cuales los dragones de hoy son un pálido reflejo, convirtieron todo el cielo en fuego, mientras que en tierra ejércitos de soldados de infantería (duendes, trolls y humanos) llenaron de sangre los valles y llanuras.
        - **Juna:** En el momento en que el ruido del conflicto despertó a Guthix de Su profundo sueño, se levantó y se paró en el centro del campo de batalla para que el esplendor de Su ira llenara el mundo, ¡y pidió que cesara el conflicto!
        - **Juna:** Se hizo el silencio, porque los dioses sabían que nadie podía desafiar el poder del poderoso Guthix; porque su poder es el de la naturaleza misma, a la que, en última instancia, están sujetas todas las demás cosas.
        - **Juna:** Guthix reclamó lo que le había sido robado, volvió a dormir bajo tierra y continuó atrayendo el poder del mundo hacia sí mismo.
        - **Juna:** Pero en Su camino hacia las profundidades de la tierra, se sentó y descansó en esta cueva; y, pensando en el desierto marcado por la batalla que ahora se extendía de un lado a otro de Su mundo, lloró.
        - **Juna:** Y tan grande era Su dolor, y tan grande era Su poder vivificante, que las rocas mismas comenzaron a llorar con Él.
        - **Juna:** Más tarde, Guthix notó que las rocas seguían llorando y que sus lágrimas estaban impregnadas de una pequeña parte de Su poder.
        - **Juna:** Entonces Él me puso a mí, Su sirviente, para custodiar la cueva, y me confió la tarea de juzgar quién era y quién no era digno de acceder a las lágrimas.
  - [Choice]: Ahora no.
    - **Player:** Ahora no.
  - [Choice]: Cuéntame una historia.
    - **Player:** Cuéntame una historia.
    - **Player:** Háblame de las Lágrimas de Guthix. (ver arriba)
    - **Player:** Cuéntame una nueva historia.
      - **Juna:** Te contaré la historia de las criaturas de luz.
      - **Juna:** Innumerables y hermosas fueron las criaturas y civilizaciones de las primeras edades del mundo. Gielinor fue una obra de arte, moldeada con amor a lo largo de milenios por la mente creativa de Guthix.
      - **Juna:** Sólo las razas más resistentes sobrevivieron a las Guerras de Dios, e incluso entonces abandonaron su alta cultura y orientaron a las sociedades hacia la guerra. De las razas más delicadas ya no queda rastro, y casi ningún recuerdo.
      - **Juna:** Una de esas razas tenía cuerpos tan frágiles como los copos de nieve, pero construyeron ciudades de cristal que duraron mil años.
      - **Juna:** El viento susurraría a través de las agujas y las llenaría con armonías callejeras, y el sol naciente brillaría a través de las gemas preciosas que tachonaban las torres y crearía juegos de luces como si los arcoíris estuvieran bailando.
      - **Juna:** De hecho, tan maravilloso fue este espectáculo de luces en su apogeo que los propios patrones de luz cobraron vida, y las grandes bandadas de criaturas luminosas cabalgaban a lo largo de los rayos de gemas, cada una atraída por su propio color.
      - **Juna:** Las criaturas que ves flotando en este abismo son los últimos restos lamentables de esa época. No sé cómo llegaron hasta aquí y sobrevivieron hasta este momento, pero estoy agradecido por su compañía.
    - **Player:** Cuéntame una nueva historia.
      - **Juna:** No después del comienzo de mi vigilia, apareció un grupo de duendes en mi cueva. Eran los feos brutos de los ejércitos de los dioses, pero sus armaduras tenían un parche descolorido donde se había eliminado el símbolo de un dios.
      - **Juna:** Miraron a su alrededor vacilantes, entrecerrando los ojos a la luz de toscas antorchas, pero tan pronto como me vieron levantaron sus lanzas y cargaron.
      - **Juna:** Nadie puede acceder a las Lágrimas de Guthix por la fuerza. Los envié al abismo.
      - **Juna:** Doscientos años después, otro duende me encontró. Esta estaba desarmada y, aunque estaba muy cautelosa, logré entablar conversación con ella.
      - **Juna:** Desde entonces he recibido muchas más visitas de los descendientes de esos guerreros perdidos y, a lo largo de los siglos, los he visto cambiar.
      - **Juna:** Se han vuelto más tímidos que agresivos, y he visto crecer la luz de la inteligencia en sus ojos saltones.
      - **Juna:** Sus historias son repetitivas y sombrías, sobre cómo ganarse la vida a partir de la dura roca a través del ingenio y el trabajo duro para convertirla en un hogar.
      - **Juna:** He seguido el progreso de su carrera, pero sus historias individuales tienen poco interés para mí.

#### Durante la actualización [[ornate bowl]]

- **Juna:** Dime... espera un momento.
- **Player:** ¿Qué pasa?
- **Juna:** Siento que posees una gran habilidad; lo suficientemente grande como para obtener todo el poder de las lágrimas.
- {{anchor|ornate-bowl-instructions}}**Juna:** Si regresas a través del abismo hacia las rocas, deberías poder extraer otro trozo de piedra.
- **Juna:** Usa tu gran habilidad para hacer un cuenco más adornado. El patrón te llegará a medida que trabajes.
- **Juna:** Tráeme el cuenco y podrás usarlo para recoger las lágrimas y obtener todo el poder que contienen.
- **Juna:** Ahora, cuéntame... una historia...
- [Menu]: Selecciona una opción
  - [Choice]: Dejar hacer el bol.
    - **Juna:** Muy bien. Vuelve pronto...
  - [Choice]: Sigue hablando.
    - (continuea|Return-to-options)

##### Después de recogerlo en el bol

- **Juna:** ¿Tienes el cuenco para mí?
- **Player:** Lo tengo aquí.
- (removes=ornate bowl)
- {{RSFontAchievement|Ornate Crockery}}
- **Juna:** Muy bien. Con este cuenco más grande obtendrás un beneficio cada vez mayor de las lágrimas.
- **Juna:** Guardaré este cuenco conmigo y podrás usarlo de ahora en adelante para beber profundamente de las lágrimas.
- **Juna:** Ahora, cuéntame una historia...
- (continuea)

#### Después de que el mundo despierte

- **Player:** Me gustaría hablar sobre la muerte de Guthix.
- **Juna:** No puedo decir que sea algo en lo que desee pensar.
- **Player:** Lo siento Juna, pero no podemos ignorarlo. Sólo quería hacer algunas preguntas.
  - **Player:** Me gustaría recibir algún consejo sobre cómo ser un guardián de Guthix.
    - **Juna:**Guthix te eligió como Guardián porque ya podía verlo en ti.
    - **Juna:** Fuiste elegido para ser uno de nosotros porque demostraste no solo un gran talento, sino también una comprensión del equilibrio y el potencial para ser mucho más.
    - **Juna:** Con la muerte de Guthix y el conocimiento que te impartió, claramente tiene la intención de que nos convirtamos en un ejército contra los dioses jóvenes.
    - **Juna:** Deberías pensar en lo que te dijo; Recuerda sus intenciones al darte su poder. Él quiere que lideres la defensa de este mundo.
    - **Player:** ¿Seguramente los otros Guardianes pueden ayudar? ¿A dónde fueron?
    - **Juna:** Por supuesto. Estaremos a tu lado siempre que nos necesites, pero mientras tanto todos debemos continuar con nuestras funciones anteriores. No puedo dejar estas cuevas desatendidas, la Muerte no puede abandonar su papel... Puede que Guthix se haya ido, pero eso no significa que debamos abandonar nuestros puestos.
  - **Player:** ¿Qué crees que pasará ahora?
    - **Juna:** Ya lo hemos visto comenzar. Saradomin ya ha regresado.
    - **Juna:** Los demás vendrán. Nada ha cambiado, Player, serán tan decididos y codiciosos como lo fueron hace miles de años.
    - **Juna:** Estamos al borde de otra Guerra de Dioses. Si no actuamos, el mundo quedará devastado. Guthix no está aquí para detenerlos esta vez. Depende de nosotros.
  - **Player:** ¿Cómo te sientes?
    - **Juna:** Es muy difícil hablar de ello. No puedo creer...
    - **Juna:** Lo siento, no estoy listo para discutir esto con nadie. Es demasiado doloroso.

#### Después del pájaro y the Beast

- **Player:** Me gustaría hablar sobre la muerte de Guthix.
- **Juna:** No puedo decir que sea algo en lo que desee pensar.
- **Player:** Lo siento Juna, pero no podemos ignorarlo. Sólo quería hacer algunas preguntas.
  - **Player:** ¿Qué crees que pasará ahora?
    - **Juna:** Ya lo hemos visto comenzar. Saradomin y Zamorak ya regresaron. Armadyl y Bandos se han enfrentado y el nuevo Dios War ha reclamado su primera víctima divina.
    - **Juna:** Vendrán más. Nada ha cambiado, jugador. Serán tan decididos y codiciosos como lo fueron hace miles de años.
    - **Juna:** Estamos al borde de otra Guerra de Dioses. Si no actuamos, el mundo quedará devastado. Guthix no está aquí para detenerlos esta vez. Depende de nosotros.

#### Opción de diálogo Zanik y Bandos

- [Menu]: Selecciona una opción
  - [Choice]: Quiero hablar de Zanik y Bandos.
    - **Player:** Quiero hablar sobre Zanik y Bandos.
    - **Juna:** Mis sentimientos sobre este asunto han cambiado. ¿Quieres saber cómo me sentí en ese momento o cómo me siento ante la muerte de mi señor Guthix?
    - [Menu]: Selecciona una opción
      - [Choice]: Quiero saber cómo te sentiste entonces.
        - **Juna:** Player, espero que te des cuenta de la magnitud de tus acciones. Al ayudar a Zanik a expulsar a Bandos, has traicionado a todos los dioses.
        - [Menu]: Selecciona una opción
          - [Choice]: Pensé que tú y Zanik eran amigos.
            - **Player:** Pensé que tú y Zanik eran amigos.
            - **Juna:** Lo estábamos, pero ya no. Nunca volveré a tratar con ese blasfemo. Ha hecho más que traicionar a su dios: ha traicionado a todos los dioses.
            - (previous)
          - [Choice]: ¿Qué quieres decir con traicionar a todos los dioses?
            - **Player:** ¿Qué quieres decir con traicionar a todos los dioses?
            - **Juna:** ¡Traicionaste el principio de la soberanía de los dioses! Bandos trajo los duendes a Gielinor, por lo que son su propiedad legítima. No tienen más derecho a desafiarlo que el que tu propia arma tiene a atacarte. Por eso Guthix permitió que Zanik resucitara de entre los muertos. No sólo estaban en juego los intereses de Bandos, {{Sic}}. Al desafiarlo te enfrentaste a todos los dioses.
            - (previous)
          - [Choice]: Todavía era lo correcto.
            - **Player:** Aún así era lo correcto.
            - **Juna:** La voluntad de los dioses es la medida de lo que es correcto.
          - [Choice]: ¿Entonces ahora soy un enemigo de los dioses?
            - **Player:** ¿Entonces ahora soy un enemigo de los dioses?
            - **Juna:** No. No siento eso en ti. Por alguna razón, Guthix no desea castigarte. Quizás sienta que servirás bien a los dioses en el futuro.
            - [Menu]: Selecciona una opción
              - [Choice]: No me gusta cómo suena eso.
                - **Player:** No me gusta cómo suena eso.
                - **Juna:** Lo que quieras o no quieras no tiene importancia para los dioses. En cualquier caso, Guthix todavía desea que me ocupe de usted. ¿Me contarás una historia?
                - (Continues as usual Tears of Guthix dialogue)
              - [Choice]: Eso es un alivio.
                - **Player:** Eso es un alivio.
                - **Juna:** Me alegra saber que todavía estás en el camino correcto. En cualquier caso, Guthix todavía desea que me ocupe de usted. ¿Me contarás una historia?
                - (Continues as usual Tears of Guthix dialogue)
      - [Choice]: Quiero saber cómo te sientes ahora.
        - **Juna:** Serví a Guthix durante más tiempo del que existe la mayoría de las dinastías mortales. Pasé la mayor parte de ese tiempo solo, cumpliendo pacientemente la tarea que me asignó. En ese momento, mis pensamientos y sentimientos se volvieron... retorcidos.
        - **Juna:** Durante siglos, mi único pensamiento fue el amor por mi señor Guthix. Anhelaba que regresara y me bendijera con su mirada divina, para decirme que había sido un buen y fiel servidor. Amaba a Guthix no porque fuera el dios más poderoso o benévolo (aunque era ambas cosas), sino porque era mi dios y me había elegido para ser su sirviente.
        - **Juna:** Cuando vi que Zanik había sido elegida por su dios para ser su sirvienta, y que ella se negó, eso me pareció la mayor blasfemia posible. Ahora veo que, en mi aislamiento, había construido un ídolo falso en mi mente y ya no adoraba al verdadero Guthix. Al desafiar al dios de la guerra, Zanik siguió el verdadero camino de Guthix, y al oponerme a ella... me equivoqué.
        - **Juna:** No he tenido noticias de Zanik desde que murió Guthix. Quizás si la volviera a ver podría perdonarme... pero no sé dónde está ni cuál será su lugar en esta nueva era.
        - **Juna:** No deseo pensar más en esto... ¿Me cuentas una historia?
        - (Continues as usual Tears of Guthix dialogue)

### List of stories

{| clase="wikitabla"
! Búsqueda
! final de la historia
! La respuesta de Juna
|-
| Secuelas
| "Derroté a Zamorak y me despedí de los dioses antes de que fueran desterrados de Gielinor".
|
|-
| Todo encendido
| "...Y así fue como aprendí a mantener las balizas de vigilancia de King Roald".
|
|-
| Alfa vs Omega
| "Finalmente me sentí listo para enfrentarme a Rasial en un combate inmortal y destruí su cuerpo físico. Al menos cumplió su palabra y liberó a su ejército de almas cautivadas de regreso a Um".
|
|-
| Antiguo despertar
| "Dirigí una expedición a la isla de Ungael y fui testigo de cómo Zemouregal reanimaba al dragón Vorkath".
|
|-
| Magnetismo animal
| "...y así el atractor funciona usando un pollo no-muerto y un imán."
| "Qué extraño."
|-
| Otra rebanada de H.A.M.
| "... así que rescaté a Zanik de Sigmund y se abrió el ferrocarril".
|(Ante el Comandante Elegido)
(Después de El Comandante Elegido) "Ella vivió, sólo para rebelarse contra su destino. Hubiera sido mejor si hubiera muerto".
|-
| Como primer recurso
| "...¡Así que ahora el spa Oo'glog está abierto!"
|
|-
| De vuelta a mis raíces
| "... Así que derroté a la vid salvaje y aprendí a cuidar mi propia Jade Vine".
| "El cuidado de la naturaleza es importante, pero las plantas silvestres son criaturas de Guthix tanto como las cultivadas."
|-
| De vuelta al congelador
| "...Y evité que los pingüinos enviaran a Gielinor a una Edad de Hielo".
| "¡Una hazaña verdaderamente gigantesca! ¡Esos pingüinos algún día podrían volverse más poderosos de lo que podríamos imaginar!"
|-
| Batalla de Forinthry
| "Defendí Fort Forinthry contra una invasión de Zemouregal y Vorkath."
|
|-
| Rastreo de bares (minimisión)
| "Completé mi tarjeta de rastreo de bares y obtuve acceso al curso de agilidad de Barbarian Outpost".
|
|-
| Batalla del monolito
| "Luché en la Batalla del Monolito".
|
|-
| Debajo de las mareas malditas
| "Descubrí el verdadero destino de Tutorial Island y ayudé a romper la maldición que habían caído sobre los tutores".
|
|-
| Debajo de las arenas de Scabaras
| "Localicé al dios Scabaras y vi cómo se frustraba el plan de Osman para matarlo".
|
|-
| Gira mundial de Benedict (minimisión)
| "Visité todos los lugares del álbum de recortes de Benedict Encumberyak".
|
|-
| Entre una roca...
| "...¡Tuve que ser disparado desde un cañón hacia una roca! Pero, finalmente, desterré el espíritu de la roca y Dondakan pudo extraer su oro".
|
|-
| Gran caza Chompy Bird
| "...el pobre Rantz era tan torpe que no podía disparar a nada, pero logré matar al Chompy bird".
|
|-
| Biohazard
| "... ¡Resultó que después de todo no había ninguna plaga!"
| "El engaño del pueblo por parte de sus gobernantes es algo terrible".
|-
| Patrimonio de los enanos
| "...y así fue como finalmente derrotamos al Hacha Roja."
| "El espectro de los enanos del caos se ha cernido sobre todos los enanos desde la Tercera Edad. Me alegra que hayas detenido a aquellos que buscaban crear más de esas abominaciones".
|-
| Fortaleza de Black Knights (eliminada)
| "...¡al final los Black Knights fueron derrotados por un repollo!"
| "Nunca se deben subestimar las verduras de Guthix."
|-
| El pacto de sangre
| "... así que rescaté al prisionero, pero la muerte del último cultista completó el ritual. La tumba de Dragith Nurn se abrió para revelar una escalera al nivel inferior de las catacumbas".
|
|-
| La sangre corre profunda
| "Después de sellar a la madre dagganoth, celebramos un funeral para Prince Brand y Princess Astrid".
| "La muerte es una parte natural de la vida. Celebrenla tanto como la lloren."
|-
| Tarea I de Boric (minimisión)
| "Completé otra tarea Mining para Boric".
|
|-
| Tarea II de Boric (minimisión)
| "Completé otra tarea Mining para Boric".
|
|-
| Tarea III de Boric (minimisión)
| "Completé otra tarea Mining para Boric".
|
|-
| Las ramas de Darkmeyer
| "...y, cuando volví con Veliaf, me dijo que simplemente pondría al Myreque en mayor peligro".
|
"Aún no sabemos qué sucederá debido a tus acciones. Tenías buenas intenciones y, por lo tanto, aún puede salir algo bueno de ello".
|-
| Llevar el tocino a casa
| "...y así es como logré ayudar a preservar la población porcina."
| "Un equilibrio así agradaría a Guthix. Sin embargo, no puedo evitar preguntarme qué pasó con esos adictos al tocino. Espero que ellos también encuentren el equilibrio".
|-
| El borde de la extinción
| "...Y entonces TzHaar me declaró su gran campeón. Después de que vencí a TokHaar-Hok hasta someterlo, se retiró al Elder Kiln para recuperarse".
| "Me entristece que los TokHaar recurran a un acto de genocidio para purificar su antigua raza. Habéis establecido un equilibrio precario entre los TokHaar y sus hermanos TzHaar".
|-
| Hogar roto
| "...y así fue como rompí la maldición sobre Senecianus y puse a descansar al fantasma de Ormod Gulvas".
| "Una historia de locura y hombres con problemas. Qué triste. Me alivia que hayas restaurado el equilibrio del mundo, héroe".
|-
| Compradores y bodegas
| "Con sigilo y desvío, conseguí los fondos para poner en funcionamiento el Gremio de Ladrones de Lumbridge".
|
|-
| Fiebre de cabina
| "...así que agujereé el barco enemigo con otro disparo de cañón, ¡y el Adventurous navegó triunfalmente hacia Mos Le'Harmless!"
|
|-
| Llamado de los Ancestros
| "Descubrí un Goebie verdaderamente antiguo y ayudé a tres jóvenes goebs a aprovechar los poderes de Mazcab".
|
|-
| Levantamiento carnilleano
| "... ¡Así que ahora Philipe Carnilean viaja por el mundo en busca de aventuras!"
| "Una carrera digna, por cierto. Es bueno que el niño se haya hecho cargo de su propia vida en lugar de vivir a la sombra de sus padres".
|-
| Catapulta Construction
| "...Y así fue como reparé la catapulta en el campamento de Tyras."
| "Las catapultas son dispositivos terribles. Mueven rocas desde las posiciones apropiadas asignadas por Guthix".
|-
| asistente de chef
| "Seguí las instrucciones de Head Chef y aprendí a hacer tarta de queso".
|
|-
| hijos de mah
| "...Y así es como Mah sucedió y los mahjarrat fueron liberados de sus rituales".
| "¡Una gran historia! Sólo espero que traten a Gielinor con respeto ahora que están libres de su maldición".
|-
| El comandante elegido
| "...¡Así que Zanik y yo derrotamos al Avatar Bandos!"
| "Sé lo que pasó. Tus acciones fueron una afrenta a la autoridad de los dioses. Puedes redimirte ante los ojos de Guthix, pero Zanik ya no es bienvenido aquí".
|-
| Ciudad de Senntisten
| "Trabajé con Azzanadra para recuperar y asegurar la catedral de Senntisten en preparación para nuestra defensa contra los dioses mayores".
|
|-
| Torre del Reloj
| "... entonces, fui yo quien reparó la torre del reloj".
|
|-
| Una jeringa mecánica
| "...y luego hundí la flota de zombos y protegí a Mos Le'Harmless de la aniquilación".
| "¿Piratas no muertos mejorados por maquinaria? Si alguna vez existiera una afrenta más abominable al equilibrio..."
|-
| Frío War
| "...Estuve cerca, pero logré descubrir los planes de los pingüinos y escapar de su base".
| "¿Pingüinos? Esas criaturas no deben subestimarse."
|-
| ¡Contacto!
| "...Y cuando salí del templo encontré el lugar enormemente cambiado. Los puestos de comida desiertos y las calles vacías fueron reemplazadas por una ciudad saludable llena de vida, color y comercio".
|
|-
| Cook's Assistant
| "...Y, al final, encontré todos los ingredientes, así que, después de todo, el duque de Lumbridge tenía un pastel de cumpleaños".
| "Ah, un final feliz. No sería bueno que un aniversario así quedara sin marcar".
|-
| Criatura de Fenkenstrain
| "...Pero al final impidí que Fenkenstrain continuara con sus horribles experimentos".
|
|-
| Crocodile Lágrimas
| "... así que seguí diciéndole que no, y ella escupió su corrupción en la forma de un demonio cocodrilo, con el cual me ocupé".
| "Restaurar Crondis no es más que una inclinación de la balanza para traer equilibrio al desierto. Aún así, es una inclinación en la dirección correcta".
|-
| La maldición de Arrav
| "...Y así escapé con el corazón de Arrav."
| "Esta separación del corazón del hombre no es natural. Es bueno que busquen resolver estos asuntos".
|-
| Maldición de la Piedra Negra
| "Derroté a the Ambassador y salvé a Gielinor de una horrible presencia oculta".
|
|-
| La maldición del Señor Vacío (minimisión)
| "Me comuniqué con seis espíritus y aprendí más sobre una entidad antigua cuyo nombre probablemente no debería pronunciar en voz alta. También adquirí túnicas fantasmales".
|
|-
| Control de daños (minimisión)
| "Rescaté materiales de la isla de Goshima para reparar el Sarim's Revenge".
|
|-
| La oscuridad de Hallowvale
| "...Le di a Safalaan el libro sobre hemalquimia y él me recomendó para un puesto en el Myreque".
| "Estoy seguro de que tendrás muchas más aventuras en nombre del Myreque. Entonces, tal vez, tendrás aún más historias que contarme".
|-
| hija del caos
| "Seguí a Moia a través de Wilderness y fui testigo del punto de inflexión del War civil de Zamorak".
|
|-
| Muerto y enterrado
| "The Raptor y yo profundizamos en la cripta al norte de Fort Forinthry y descubrimos el nefasto complot de Zemouregal".
|
|-
| Captura más mortal
| "...y regresamos al Gremio Fishing donde Jones instaló una tienda vendiendo su propia Crema Protectora Miracle Thalassus".
| "Es una pequeña bendición que la criatura pueda seguir existiendo".
|-
| Lidiando con Scabaras
| "...Y así fue como lidié con el High Priest of Scabaras".
| "Los dioses del desierto son extraños, pero debes asegurarte de mostrarles el debido respeto".
|-
| La muerte de la caballería
| "...Saradomin devolvió la vida a Sir Owen, pero el brazo espada del caballero resucitado estaba corrupto y esquelético".
| "Espero que ahora aprecies el poder que los dioses buscan ejercer, a cualquier precio".
|-
| Meseta de la muerte
| "... Entonces, a partir de ese momento, la Guardia Imperial pudo acceder a la Meseta de la Muerte de manera segura y tomar a los trolls por sorpresa".
|
|-
| Muerte al Dorgeshuun
| "...¡Sigmund escapó de nuevo, pero Zanik y yo destruimos la máquina y Dorgesh-Kaan se salvó!"
|(Antes de The Chosen Commander) "Zanik todavía tiene su destino que cumplir, y tengo la sensación de que tú tendrás parte en eso".
(Después de The Chosen Commander) "Salvado, solo para luego rebelarse contra su legítimo gobernante. Pero todo eso ya pasó".
|-
| Defensor de Varrock
| "...El Escudo de Arrav brillaba con un rayo, y Dimintheis lo usó para derrotar al ejército zombie".
|
|-
| Demonio Slayer
| "... ¡así que destruí al demonio Delrith y salvé a Varrock!"
| "Recuerdo a Delrith. Un personaje muy desagradable; me alegro de que lo hayan enviado".
|-
| Mazmorra del Desierto Slayer (minimisión)
| "En la mazmorra Pollnivneach Slayer, derroté a un monstruoso rastreador de cuevas, al jefe basilisco, al turoth más poderoso y al señor supremo kurask".
|
|-
| Desert Treasure
| "...¡En la pirámide descubrí un conjunto completamente nuevo de hechizos mágicos!"
| "Te sugiero que pienses en el origen de esos hechizos. No se debe jugar con la magia antigua".
|-
| Medidas desesperadas
| "Rastreé a Kerapac y frustré su plan para destruir Gielinor. Ahora ha vuelto a caer bajo el control de Jas, esta vez atado a la Aguja".
|
|-
| Tiempos desesperados
| "Es posible que accidentalmente haya ayudado a un dragonante a tomar el control de un artefacto antiguo, poniendo en peligro toda la vida en Gielinor. Ups".
|
|-
| Mentes tortuosas
| "... ¡Fui yo quien accidentalmente trajo una baliza de teletransporte a Entrana! Pero los Caballeros del Templo están investigando, así que todo debería estar bien".
|
|-
| Diamante en bruto
| "¡Resultó que Lady Keli era en realidad la diosa del desierto Amascut disfrazada! Ella escapó con el corazón y nos dejó a Ozan y a mí para derrotar a sus guardaespaldas".
| "Es bueno que el príncipe haya regresado sano y salvo a casa para mantener el equilibrio de la paz, pero el coste puede resultar elevado".
|-
| El sitio de excavación
| "...Y el examinador quedó muy impresionado de que hubiera descubierto un antiguo altar de Zaros".
| "¿Zaros? No había oído ese nombre en mil años, incluso antes del comienzo de mi estancia aquí."
|-
| Dimensión del desastre
| "...y así regresé a Varrock, el héroe de dos mundos".
| "Fascinante. Una ciudad de villanos, en un mundo donde Guthix todavía duerme. Tu historia me intriga".
|-
| Dimensión del desastre: moneda del reino
| "Abrí el camino hacia el nuevo Varrock".
|
|-
| Dimensión del desastre: La maldición de Arrav
| "Derroté a Zemouregal en New Varrock".
|
|-
| Dimensión del Desastre: Escudo de Arrav
| "Devolví el escudo de Arrav al nuevo museo Varrock".
|
|-
| Dimensión del desastre: Defensor de Varrock
| "Debilité el control de Zemouregal sobre Arrav en New Varrock".
|
|-
| Dimensión del desastre: Demonio Slayer
| "Derroté a los demonios Delrith y Agrith Naar en New Varrock".
|
|-
| Deshonra entre ladrones (del lado de Zamorak)
| "... ¡y luego Zamorak y yo atacamos simultáneamente a Sliske, dándole un golpe que lo obligó a retirarse al Reino de las Sombras con la Piedra de Jas!"
| "Otro paso más hacia God Wars. Guthix lloraría por la anarquía que está arrasando Gielinor, los otros Guardianes y yo debemos hacer todo lo que esté a nuestro alcance para evitarlo".
|-
| Deshonra entre ladrones (neutral)
| "...y después de extraer poder de la Piedra de Jas, Zamorak atacó a Sliske, obligándolo a retirarse al Reino de las Sombras con la piedra.
| "Otro paso más hacia God Wars. Guthix lloraría ante la anarquía que está arrasando Gielinor, los otros Guardianes y yo debemos hacer todo lo que esté a nuestro alcance para evitarlo."
|-
| Deshonra entre ladrones (del lado de Sliske)
| "...luego canalicé la Piedra de Jas y lancé a Zamorak para salvar a Sliske, ¡dándole tiempo suficiente para trasladarnos a ambos al Reino de las Sombras junto con la Piedra!"
| "Otro paso más hacia God Wars. Guthix lloraría ante la anarquía que está arrasando Gielinor, los otros Guardianes y yo debemos hacer todo lo que esté a nuestro alcance para evitarlo."
|-
| No hacer el mal
| "...y así la colonia de monos prospera y Apmeken se restablece."
| "Restaurar Apmeken no es más que una inclinación de la balanza para lograr el equilibrio en el desierto. Aún así, es una inclinación en la dirección correcta".
|-
| Tarea I de Doric (minimisión)
| "Completé otra tarea Smithing para Doric".
|
|-
| Tarea II de Doric (minimisión)
| "Completé otra tarea Smithing para Doric".
|
|-
| Tarea III de Doric (minimisión)
| "Completé otra tarea Smithing para Doric".
|
|-
| Tarea IV de Doric (minimisión)
| "Completé otra tarea Smithing para Doric".
|
|-
| Tarea V de Doric (minimisión)
| "Completé otra tarea Smithing para Doric".
|
|-
| Tarea VI de Doric (minimisión)
| "Completé otra tarea Smithing para Doric".
|
|-
| Tarea VII de Doric (minimisión)
| "Completé otra tarea Smithing para Doric".
|
|-
| Tarea VIII de Doric (minimisión)
| "Completé otra tarea Smithing para Doric".
|
|-
| La misión de Doric (eliminada)
| "... así que una vez que obtuve todos los minerales que quería, Doric me dejó usar sus yunques".
| "Una tarea tan pequeña difícilmente merece el término 'búsqueda'."
|-
| Dragon Slayer
| "... así que con Elvarg el dragón muerto, el maestro de Champions' Guild me dejó entrar y ¡pude usar una armadura de placas rúnicas!"
|
|-
| Mentor de sueños
| "... Así que al final viajé al País de los Sueños de Cyrisus y derroté su miedo al combate".
|
|-
| Ritual druídico
| "... entonces Kaqemeex me enseñó cómo usar la habilidad Herblore".
| "Una recompensa generosa en verdad."
|-
| Búsqueda del pato
| "Ayudé a reunir a un patito perdido con su familia y, en el camino, aprendí la filosofía del pato".
|
|-
| Cañón enano
| "...y así fue como arreglé el multicañón enano."
| "Entonces, ¿la guerra todavía hace estragos en el mundo de arriba? ¿Nunca te cansarás de crear máquinas de destrucción?"
|-
| La artimaña de Eadgar
| "... ¡La artimaña de Eadgar fue absurda, pero funcionó! Los trolls se comieron a un humano falso y yo conseguí la hierba para el ritual de los druidas".
|
|-
| Pico de las Águilas
| "...¡al final tuve que disfrazarme de águila para conseguirle al zoológico un nuevo hurón!"
| "No debes tomar a la ligera tu alteración del equilibrio de la naturaleza. Trata siempre el mundo natural con respeto".
|-
| Eclipse of the Heart
| "... ¡y así fue como reuní a los semidioses del panteón del desierto, detuve la destrucción de Amascut y salvé a Menaphos!"
| "Hiciste bien en no acabar con la vida de Amascut. Con su regreso del borde del abismo, se ha restablecido el equilibrio en el desierto".
|-
| El horno mayor
| "...Ga'al-Xox se fue sin decir una palabra más, no puedo evitar pensar que los recuerdos del campeón TzHaar muerto pesan mucho en su mente."
| "Los recuerdos de los muertos son sagrados. Canalizarlos a través de los vivos es una afrenta para Guthix. Los TzHaar deberían haberse mantenido alejados de ese horno".
|-
| Taller Elemental I
| "...una vez que reparé el Taller Elemental, pude hacer un escudo elemental".
|
|-
| Taller Elemental II
| "...¡así que inculqué el poder de mi mente en la barra preparada y la forjé en un yelmo mental elemental!"
| "Debes tener cuidado de no entrometerte en tu propia cabeza".
|-
| Taller Elemental III
| "...al presionar el botón se encendió la barra elemental. Entonces pude crear un cuerpo".
| "Suena como una tarea ardua".
|-
| Taller Elemental IV
| "...al presionar el botón se encendió la barra elemental. Luego pude hacer algunas botas del caos".
| "Este taller suena complejo".
|-
| El lamento de Enakhra
| "...entonces Akthanakos y Enakhra se fueron al norte para seguir luchando."
| "Una batalla entre dos seres tan poderosos llevará mucho tiempo y liberará mucha energía. ¡Espero que el mundo natural no resulte dañado en este conflicto!"
|-
| Viaje iluminado
| "...aterrizamos el globo en Taverley y Auguste me agradeció por ayudarlo a hacer despegar su idea".
|
|-
| Entra en el abismo (minimisión)
| "Obtuve acceso al Abismo".
|
|-
| Ernesto el Chicken
| "...Así que, una vez que encontré todas las piezas de la máquina, el pobre Ernest pudo volver a ser él mismo."
| "Esa fue una buena acción. Es algo terrible que uno se quede fuera de su forma natural".
|-
| El gran día de Evil Dave
| "De alguna manera cambié de cuerpo con Evil Dave y sobreviví suficientes tareas y gritos de Doris para encontrar una manera de volver a cambiar".
|
|-
| extinción
| "... ¡y así es como evité que los Dioses Mayores destruyeran Gielinor, de una vez por todas!"
| "Guthix sabía que los Ancianos eran la mayor amenaza que Gielinor podría enfrentar. Vio que este día llegaría... y que tú te levantarías para enfrentarlo. Llora el destino de Iaia, Guardiana Mundial. Las mayores victorias requieren los mayores sacrificios".
|-
| Ojo por ojo (minimisión)
| "Ayudé a los habitantes tuertos de Cyclosis y envié a Jed no-muertos".
|
|-
| Ojo de Het I
| "Ayudé a Icthlarin a recuperar una reliquia de valor incalculable tras la destrucción del Duel Arena".
|
|-
| Ojo de Het II
| "Resolví el misterio de la destrucción del Duel Arena".
|
|-
| Los ojos de Gloufrie
| "... ¡la máquina reveló que las lindas criaturas eran en realidad espías arposandranos! Los destruí y el rey Narnode me dio una semilla de cristal que pertenecía a Oaknock el Ingeniero".
|
|-
| Un cuento de Fairy I - Dolores de crecimiento
| "... así que derroté al pie enredado y devolví las tijeras de podar encantadas de Fairy Queen al Padrino de Fairy".
| "Estas hadas parecen conocer bien los poderes de la naturaleza."
|-
| A Fairy Tale II - Cura a una reina
| "...¡la Fairy Queen despertó y nos dimos cuenta de que el Padrino la había traicionado!"
| "La política nunca es sencilla".
|-
| A Fairy Tale III - Batalla en Ork's Rift
| "...y cuando el Padrino de Fairy fue absorbido por la grieta, su poder creció tan inmenso que la grieta explotó y destruyó un área entera de Zanaris. ¡Los orkos de Marfil Malditos ahora deambulan por esa área, rebrotando continuamente de las parcelas agrícolas malditas!"
|
"Eso es realmente preocupante, Player".
A lo que usted responde: "Sin embargo, la Fairy Queen ha vuelto a ocupar el trono que le corresponde, ¡y el padrino de Fairy no volverá a molestar a nadie!".
A lo que Juna responde: "Parece que realmente eres una fuerza para el bien, Player. El propio Guthix aprobaría que devuelvas el equilibrio al reino de Zanaris".
|-
| Escudo familiar
| "...Así que las tres partes del escudo familiar se reunieron".
|
|-
| Destino de los Dioses (regresando Zaros con toda su fuerza)
| "... ¡Y entonces Zaros ha regresado a Gielinor con toda su fuerza, y tiene la intención de convertirse en un dios anciano! "
| "Si bien sus intenciones pueden parecer nobles, sus métodos son cuestionables y su historia está empañada. Sea lo que sea, no es Guthix".
|-
| Destino de los dioses (saboteando a Zaros)
| "...y entonces Zaros ha regresado a Gielinor en un estado debilitado, ¡pero todavía tiene la intención de convertirse en un dios mayor!
| "Si bien sus intenciones pueden parecer nobles, sus métodos son cuestionables y su historia está empañada. Sea lo que sea, no es Guthix."
|-
| Padre e hijo (minimisión)
| "Le pasé un mensaje a Sigli de Irwinsson y le di a Irwinsson un arco creado por su padre.
|
|-
| The Feud
| "... Entonces, a pesar del fracaso de mi tarea original, Ali Morrisane estaba muy contento con la suerte de su sobrino".
|
|-
| Arena de lucha
| "... ¡Vencí a General Khazard en su propia arena y le gané a los Servils su libertad!"
|
|-
| Destino final (minimisión)
| "Derroté al Capitán Cora y facilité el paso del Khan de Goshima hasta su destino final".
|
|-
| La maldición del bombero
| "...así que Char todavía está allí, supuestamente planeando el regreso de Zaros."
| "El regreso de Zaros no es algo que pueda ver con buenos ojos, pero debemos admirar la devoción de Char. Se necesita fuerza para permanecer leal durante tantos siglos".
|-
| Concurso Fishing
| "...Y después de ganar el concurso de pesca, los enanos me dejaron ir bajo la Montaña del Lobo Blanco".
| "¿Fishing? ¡Una extraña prueba de dignidad para pasar por un túnel subterráneo!"
|-
| Caída de bandera (minimisión)
| "Aprendí a viajar a islas inexploradas y reclamé una isla propia".
|
|-
| Historia olvidable de un Drunken Dwarf
| "...Creo que hice algo con drunken dwarf, pero no recuerdo qué."
| "¡Debes tener cuidado de no dejar que la bebida enturbie tu cerebro!"
|-
| El perdón de un enano del caos
| "...Y resultó que Hilda había sido el enano del caos que matamos en la torre. Veldaban estaba devastado".
| "Perder la identidad es peor que la muerte".
|-
| Las islas Fremennik
| "... Maté a muchos trolls y traje la cabeza del Rey Troll a Neitiznot como trofeo".
|
|-
| Los juicios de Fremennik
| "...Y así fue como me convertí en miembro honorario del Fremennik, y me dieron mi nombre de Fremennik, <small>*(nombre de Fremennik del jugador)*</small>".
|
|-
| De Tiny Acorns (minimisión)
| "Completé otra travesura para el gremio de ladrones Lumbridge".
|
|-
| Fur 'n buscar
| "... Entonces, ¡busqué todas las pieles que quería el Odd Old Man y él me dio una recompensa!"
| "Este Odd Old Man tiene algunas solicitudes desconcertantes. Me pregunto cuáles son las motivaciones de sus acciones".
|-
| Jardín de la Tranquilidad
| "... ¡así que el jardín del palacio Varrock es todo mi trabajo!"
| "Es bueno que puedas tomarte el tiempo de matar y aventurarte para cultivar un hermoso jardín".
|-
| La sombra del general (minimisión)
| "Miré hacia el reino de las sombras y me encontré con General Khazard. Completé su tarea y obtuve la espada de las sombras.
|
|-
| El gato de Gertrude
| "... ¡Devolví Fluffs sano y salvo a Gertrude y ella me dio mi propio gato!"
| "Los gatos son una de las criaturas más misteriosas de Guthix. Espero que tomes en serio tu responsabilidad".
|-
| Fantasmas a la vista
| "...así que la gente de Port Phasmatys finalmente pudo descansar."
|
|-
| Fantasmas del pasado (minimisión)
| "Visité las islas que alguna vez fueron tortugas y descubrí más de lo que nadie preferiría saber sobre la vida personal de Quartermaster Gully".
|
|-
| El enano gigante
| "...la estatua en Keldagrim fue reconstruida y fui testigo de una reunión del Consorcio Mining."
| "Tengo la sensación de que Keldagrim será el escenario de muchas grandes aventuras para ti".
|-
| Recuerdos gloriosos
| "Tan pronto como King Vargas recuperó su forma humana, se embarcó en otra aventura".
|
|-
| Diplomacia duende
| "...¡y así los goblins terminaron usando el color de armadura con el que tenían que empezar!"
| "¡Pobres y tontos duendes! Su raza tenía mucho potencial; si tan solo pudieran superar sus pequeñas disputas."
|-
| El Golem
| "...Y tuve que reprogramar el golem antes de que creyera que el demonio estaba muerto."
| "Recuerdo bien la batalla de Uzer".
|-
| Búsqueda de Gower
| "...y así es como los Gowers repararon el altar de la vida con mi ayuda y salvaron Detrás de Escenas".
| "Creer que existe un lugar así. Me pregunto si quizás alguna vez tendré la oportunidad de visitarlo".
|-
| El gran árbol
| "...Glough huyó como el cobarde que realmente es, ¡y el Gran Árbol se salvó!"
|
|-
| El gran robo de cerebros
| "...pero después de que los cerebros de los monjes fueron restaurados, ¡tuve que luchar contra una enorme abominación llamada Barrelchest!"
| "¿Zombis e intercambio de cerebros? Es bueno que hayas puesto fin a esta falta de respeto por la naturaleza".
|-
| Cuentos sombríos
| "... así que encontré al duende dorado y corté el tallo de habichuelas, ¡y ese fue el final de esa sombría historia!"
|
|-
| Un gremio propio (minimisión)
| Completé otra travesura para el gremio de ladrones Lumbridge.
|
|-
| Tierra de Gunnar
| "...y el cacique accedió a establecerse en la tierra que sus antepasados ​​habían ganado."
| "Estos militantes fremennik creen que sirven a Guthix, pero sólo se sirven a sí mismos".
|-
| La mano en la arena
| "... ¡Así fue como le di una mano a Bert para resolver el asesinato y le devolví la cabeza al mago, resolviendo el enigma de los siempre llenos pozos de arena!"
| "La víctima muere y el asesino es castigado: eso es equilibrio."
|-
| Heraldo (minimisión)
| "Me embarqué en un viaje a la erudita isla de Tuai Leit. No salió del todo según lo planeado y mi barco resultó gravemente dañado por un nuevo y misterioso adversario".
|
|-
| Mina embrujada
| "...Y de los cristales legendarios corté un fragmento de ungüento para luchar contra los no-muertos".
|
|-
| Culto Hazeel (lado de Ceril)
| "...así fue como frustré a los cultistas en su plan de resucitar a Hazeel."
| "Los Mahjarrat son una raza vil. Harías bien en mantenerte alejado de ellos".
|-
| Culto Hazeel (lado de Hazeel)
| "... Así fue como ayudé a que Hazeel regresara a sus seguidores".
| "Los Mahjarrat son una raza vil. Harías bien en mantenerte alejado de ellos".
|-
| Jefe de familia (minimisión)
| "Ayudé a los moai de Waiko y Aminishi a resolver su problemática relación a larga distancia".
|
|-
| Heart of Stone
| "...y cuando el abisal prehistórico volvió a caer en el portal, supimos que es posible que Xenia ya haya iniciado el despertar de los dioses mayores".
| "Me entristece que hayamos perdido a Xenia. Ella era una buena mujer a su manera. Pero tal vez hiciste bien en detenerla".
|-
| Corazones de sangre
| "Con la ayuda de un vampyre llamado Anya, destruí el corazón sanguíneo cerca de Wendlewick y salvé a la aldea de la plaga que se estaba propagando".
|
|-
| ladrón de corazones
| "Puede que no hayamos robado un rubí de valor incalculable, pero ayudé a Annette a robar el corazón de Caelyn".
|
|-
| Heraldos de carmesí
| "... ¡y así nos unimos para derrotar a los Caballeros de Sangre Ghrazi! Desafortunadamente, uno de ellos escapó y cerró el portal, dejando varado a Anya en Gielinor".
| "Haces algunos amigos cuestionables, pero me alegra saber que Havenhythe está bien protegida".
|-
| Permisos Hermit
| "Ayudé a los aldeanos de Wendlewick a resolver el problema de los cangrejos".
|
|-
| Ayudando a Laniakea (minimisión)
| "Ayudé a Laniakea a encontrar un Fugu para que pudiera producir un veneno muy potente".
|
|-
| Bienvenida del héroe
| "...pero al final V sigue muerto, a pesar de que Tarshak pagó el precio".
| "El mundo es más seguro tras la muerte de ese monstruo. Estoy seguro de que V estaría orgulloso".
|-
| Búsqueda de héroes
| "...así que, después de haber recuperado todos los artículos, ¡me convertí en miembro de Heroes' Guild!"
|
|-
| Santo Grial
| "...y de todos los Caballeros de la Mesa Redonda, fui yo quien encontró el Santo Grial."
|
|-
| Voluntad de Hopespear (minimisión)
| "Enterré a cinco sacerdotes duendes para el fantasma de Hopespear, haciendo descansar sus almas".
|
|-
| Terror desde las profundidades
| "... ¡Y ese fue el fin del horror de las profundidades!"
|
|-
| Vivienda del Parlamento
| "Limpié la lechucería de City of Um y atraje a algunas lechuzas a la ciudad".
|
|-
| Caza del Raktuber rojo
| "...y luego Larry fue secuestrado por los pingüinos y tuve que nadar sobre un oso polar para regresar al continente".
| "Esos pingüinos son personajes astutos".
|-
| La caza de Surok (minimisión)
| "Perseguí a Surok Magis en los Túneles del Caos y me encontré con un gran orko".
|
|-
| El pequeño ayudante de Icthlarin
| "... ¡Y con el amuleto que recibí, pude entender el lenguaje de los gatos!"
| "Es un raro privilegio entender el lenguaje de esos seres. Hay que escuchar atentamente todo lo que tienen que decir, pero no creer demasiado en ello".
|-
| Cazador de diablillos
| "...me tomó algo de tiempo, pero finalmente recuperé las cuatro cuentas y Mizgog me dio mi recompensa".
| "¡Diablillos! Recuerdo la época de las grandes guerras, cuando los ejércitos de diablillos de Zamorak ensangrentaban los tobillos de las criaturas de los otros dioses".
|-
| Impresionando a los lugareños
| "...y ahora soy el capitán del Sarim's Revenge, con una tripulación heterogénea bajo mi mando".
| "Guthix visitó estas islas Wushanko cuando llegó por primera vez, pero no me contó mucho sobre su tiempo allí".
|-
| En ayuda del Myreque
| "...Veliaf quedó muy impresionado con la Vara de Ivandis, ¡y puedo usarla para matar a los juves y a los juvinates!"
|
|-
| En Memoria del Myreque (minimisión)
| "Construí un monumento al Myreque".
|
|-
| En necesidad de pira
| "... ¡Y así fue como ayudé al fénix a renacer!"
| "Has prestado un servicio a una de las criaturas de Guthix, y te lo agradezco".
|-
| En busca del Myreque
| "...entonces, supongo que fue mi culpa que los jóvenes miembros del Myreque fueran asesinados por Vanstrom."
|
|-
| La jota de espadas
| "...pero era sólo Ozan disfrazado, y él sólo quería encontrarse lejos de miradas atentas y mostrarme la corrupción en Menaphos".
| "Las almas de los humanos se corrompen muy fácilmente, especialmente las de aquellos que no tienen amigos."
|-
| Jed Hunter (minimisión)
| "Perseguí y derroté a Jed, y reclamé venganza para la gente de Port Sarim".
|
|-
| Poción de la selva
| "...y una vez que reuní todas las hierbas, Trufitus Shakaya pudo comunicarse con sus dioses".
|
|-
| Preocupaciones de Kennith
| "...Y mi último paso fue traerle a Kennith su tren de juguete".
|
|-
| Fila Kili
| "Conocí al herrero de City of Um y aprendí a mejorar mi equipo de nigromante".
|
|-
| Espíritus afines
| "Escapé del retorcido juego de Sliske con los hermanos Barrows. Lamentablemente, Linza se convirtió en un monstruo en el proceso".
|
|-
| rey de los enanos
| "...Así que ahora Veldaban es el rey de los enanos"
| "...Puede que hayas tenido motivos nobles, pero le has robado el trono al legítimo rey. Esta acción no es equilibrada".
|-
| El rescate del rey
| "...Y después de haber usado el hechizo para liberar a King Arthur, lo disfrazé de guardia para que pudiera escapar".
|
|-
| La espada del caballero
| "... así fue como encontré a los Enanos Imcando y le conseguí al caballero una nueva espada".
|
|-
| Los problemas de Koschei (minimisión)
| "Descubrí el misterioso origen de Koschei el Inmortal."
|
|-
| Guarida de Tarn Razorlor (minimisión)
| "Derroté a Tarn Razorlor y aprendí su conocimiento secreto leyendo el diario en su vivienda".
|
|-
| Tierra de los duendes
| "...Oldak y yo escapamos de Yu'biusk antes de que se cerrara el portal, pero Zanik quedó atrapado en la caja".
| (Ante el comandante elegido)
(Después de The Chosen Commander) "Sólo para luego regresar y traicionar al autor de su destino. Ojalá nunca hubiera encontrado esa caja".
|-
| El legado de la mirada vidente
| "... Maté un Vyrewatch, como me había pedido Safalaan, y llevé el cadáver al Columbario Paterdomus para cremarlo. En agradecimiento, el espíritu dejó una llave que me permitió acceder a sus riquezas mundanas. ¡Mi primer premio fue un talismán de sangre!"
| "Con tu mente tan concentrada en la riqueza material, me preocupa si las intrigas que ensombrecen tus descubrimientos están siendo investigadas adecuadamente. Me temo que Drakan es todo un mundo de problemas para los cuales no estás preparado".
|-
| Búsqueda de leyendas
| "...y cuando hube completado todas las tareas, ¡me convertí en miembro de Legends' Guild!"
|
|-
| Déjalos comer pastel
| "...y al final las tiendas de alimentos de Rolo fueron entregadas a la gente de Burthorpe para que las disfrutara".
| "Así que los hambrientos se alimentaron y los sobrealimentados quedaron... bueno, vacíos. Puede que Guthix no apruebe los métodos utilizados, pero se ha logrado un equilibrio".
|-
| La luz interior
| "Ayudé a devolver la luz de Seren al mundo reformando su cuerpo y su alma".
|
|-
| El Señor del Vampyrium
| "... así que con la mayoría de los Myreque asesinados por Lord Drakan, Veliaf ha perdido la esperanza y Ivan ha regresado a Paterdomus. Los Myreque están rotos".
| "Incluso en la muerte, los Myreque iluminan el camino para la gente de Morytania. Todo lo que se pierde se puede encontrar de nuevo, incluso la esperanza. Mantente fuerte, Player".
|-
| ciudad perdida
| "...Y cuando entré por la puerta llevando el Dramen Staff, fui transportado a un mundo completamente nuevo: ¡un mundo poblado por hadas mágicas!"
|
|-
| Perdió sus canicas (minimisión)
| "Completé otra travesura para el gremio de ladrones Lumbridge".
|
|-
| Los juguetes perdidos (minimisión)
| "Busqué y abracé 13 peluches de vampyre escondidos por todo Morytania".
|
|-
| La tribu perdida
| "...Sigmund fue despedido, y el duque y el gobernante de los duendes de las cavernas firmaron un tratado de paz".
| "Los duendes Dorgueshuun han sido buenos vecinos durante mi vigilia aquí. Son una raza tímida, pero no cobarde, y me alegro de que tengan la paz que desean".
|-
| Historia de amor
| "...así que Wise Old Man y Zenevivia viven felices para siempre, ¡pero aun así no me dieron ese sombrero!"
|
"Un sombrero es sólo un sombrero Player."
A lo que respondes: "¡Grr!"
|-
| Diplomacia lunar
| "... así que derroté a mi imagen reflejada, me gané el respeto del Clan de la Luna y los persuadí para que se comunicaran con los Fremennik".
| "La dependencia del Clan de la Luna en la magia no es más equilibrada que el odio de los Fremennik hacia ella."
|-
| Haciendo historia
| "...así que el puesto de avanzada se convirtió en un museo".
| "La historia es la historia más grande de todas y es muy bueno que hayan ayudado a preservarla".
|-
| Recuerdos de Mahjarrat (minimisión)
| "Ayudé a Kharshai el Mahjarrat a recuperar 15 recuerdos de sus parientes".
|
|-
| Historial de reuniones
| "...Y así fue como viajé al pasado y conocí a la primera familia que llegó a Gielinor".
| "Has sido realmente bendecido por Guthix. Sólo puedo soñar con tal honor".
|-
| El cristal de Merlín
| "...y cuando le dije a King Arthur que yo solo había liberado a Merlín de su prisión de cristal, ¡me nombró caballero de la Mesa Redonda!"
|
|-
| La poderosa caída (ahorrando a Zanik)
| "...y luego derroté a Graardor, y así Zanik se convirtió en líder de los bandosianos. Ella condujo a muchos de ellos en un éxodo a Yu'biusk, con la esperanza de encontrar la paz o la muerte".
| "Extrañaré a Zanik. Me avergüenza haberla condenado. Al final, su heroísmo brilló. Entre ustedes, habéis neutralizado el desequilibrio bandosiano restante".
|-
| La poderosa caída (matando a Zanik)
| "...y luego, eh, Zanik murió, y así Graardor se convirtió en líder de los bandosianos. Algunos de ellos regresaron a Gielinor y otros permanecieron en Yu'biusk"
| "Extrañaré a Zanik. Me avergüenza haberla condenado. Al menos parece que has neutralizado el desequilibrio bandosiano. Graardor no será un gran líder".
|-
| Extrañando a mi mamá
| "... Entonces, pude restaurar la momia lo suficiente como para darle sentido a lo que estaba diciendo".
| "Tener tu cuerpo, espíritu y sombra esparcidos por el tiempo debe ser algo terrible. Es bueno que hayas ayudado a aliviar el tormento de la momia restaurándola".
|-
| Desaparecido, presunta muerte
| "...y así fue como Icthlarin y yo salvamos a la Muerte. Pero no antes de que Sliske pudiera cumplir su desafío: que la persona que matara a la mayor cantidad de dioses recibiría la Piedra de Jas".
| "Me alegro de que hayas encontrado a la Muerte. Es un devoto guardián de Guthix. Por desgracia, parece que con Guthix desaparecido y sus edictos ya no vigentes, otra Guerra de Dios está en el horizonte".
|-
| Amigo del monje
| "... entonces los monjes organizaron una fiesta de borracheras para celebrar el cumpleaños del niño".
|
"La alegría no debe llevarse al exceso. Estos saradoministas nunca han entendido la importancia del equilibrio".
A lo que usted responde: "Además, aunque habían traído mucho alcohol, nunca los vi trayendo nada para que bebiera el niño".
|-
| Monkey Madness
| "... Así que derroté al Demonio de la Selva y detuve el complot de los Monos para apoderarse de Karamja".
|
"¡Veo que no podrían convertirte en un mono!"
A lo que respondes: "Bueno, en realidad, fui mono por un tiempo".
|-
| Hija de la montaña
| "... Llegué demasiado tarde para salvar a la hija del cacique, pero al menos le di un entierro adecuado".
| "Breve es la vida, pero más preciosa si se honra adecuadamente su paso."
|-
| Mourning's End Parte I
| "...después de haberle dicho al Jefe Mourner que había envenenado la ciudad, él me habló del templo perdido en las montañas que estaban buscando".
|
|-
| Mourning's End Parte II
| "... ¿A qué clase de mente retorcida se le ocurriría el rompecabezas del rayo de luz en ese templo?"
|
|-
| Asesinato en la frontera
| "Resolví el misterio detrás del asesinato de Duke Hoarse y desentrañé un complot para asesinar a King Roald".
|
|-
| Misterio del asesinato
| "...Y así es como resolví el asesinato de Lord Sinclair."
|
|-
| La gran aventura de My Arm
| "...¡My Arm todavía está en esa azotea, cultivando gota en su pequeño huerto!"
| "Es bueno que un troll desee estudiar la compleja habilidad que es Farming".
|-
| Mitos de las Tierras Blancas
| "...Pasé por la broma de los diablillos de nieve. ¡Explorer Jack no tenía idea de que las 'riquezas' eran en realidad estiércol de yeti congelado!"
| "Es agradable saber que los diablillos de las nieves siguen haciendo sus viejos trucos."
|-
| Nadir (saga)
| "Escuché la saga de Skaldrun sobre Moia, la hija medio Mahjarrat de Lucien, y su descenso a Daemonheim".
|
|-
| Naturaleza Spirit
| "...y así fue como ayudé a Filliman Tarlock a transformarse en un espíritu de la naturaleza".
| "Es bueno que hayas ayudado a descansar a un sirviente de Guthix".
|-
| Necromancy!
| "Después de ser asesinado por una espada animada y de una rápida visita a la oficina de la Muerte, la Muerte me llevó al City of Um. Allí fuimos testigos de Rasial, the first necromancer, robando todas sus almas".
|
|-
| La aguja salta
| "...y así fue como aprendí los secretos de la Aguja y el impacto en esa pobre familia."
| "Los artefactos antiguos pueden ser cosas peligrosas, en más formas que las físicas".
|-
| Nuevas fundaciones
| "Ayudé a King Roald a establecer un nuevo Ducado en Wilderness que ahora administro".
|
|-
| Elegía del nómada
| "...permitiendo que las almas de los muertos sigan adelante sin ser robadas por Nomad."
| "Un objetivo noble. Su falso Guthix y su perverso plan trajeron un gran desequilibrio al inframundo".
|-
| Réquiem del nómada
| "...Y, finalmente, Nomad cayó ante mí."
| "Impresionante...Muy impresionante."
|-
| Búsqueda del Observatorio
| "...y, cuando hube arreglado el telescopio, miré a través de él y vi las estrellas."
| "Hace mucho que no veo las estrellas."
|-
| Oda del Devorador
| "Con la ayuda de Icthlarin y Zemouregal, limpié la Puerta de Elidinis y salvé a Bill y a los ciudadanos de Al Kharid de la maldición de Amascut".
|
|-
| La búsqueda de Olaf
| "...No fue fácil, pero logré convencer a la familia de Olaf de que era un buen navegante".
|
|-
| Érase una vez un limo
| ""Ayudé a Peter a eliminar la amenaza King Slime.";"
|
|-
| Érase una vez en Gielinor
| "...y así fue como Relomia pasó de ser el emisario de Sliske a un reconocido heroico aventurero".
| "Esto demuestra el poder transformador de las historias. Gracias por compartir esto conmigo".
|-
| Un pie en la tumba (minimisión)
| "Le presté otra mano al gremio de magos de Yanille al encontrar (la mayoría de) las partes restantes del cuerpo de Clarence. Logramos poner todos menos un pie en la tumba, y tuve que entregárselo a los magos de Yanille... fue un funeral bastante conmovedor".
|
|-
| Único en su clase (del lado de Kerapac)
| "...y después de derrotar al Eco de un Dios Antiguo, animé a Hannibus a regresar con Kerapac y soportar la estasis para tener la oportunidad de salvar a su pueblo".
| "¿Luchaste contra la voluntad de un Dios anciano y permitiste que los Dragonkin experimentaran con el último de los Jinetes de Dragón? Me temo que podría haber repercusiones imprevistas Player".
|-
| Único en su clase (del lado de Sharrigan)
| "...y después de derrotar al Eco de un Dios Antiguo, animé a Hannibus a regresar con su gente y permitirse descansar entre los de su propia especie".
| "Los Ilujanka parecen una especie noble, es una pena que estén desapareciendo. Sin embargo, me pregunto si será la última vez que los veremos."
|-
| Una nota penetrante
| "...y así fue como atrapé al asesino de Citharede Abbey".
| "Por supuesto, descubrí quién era el asesino a mitad de tu historia".
|-
| Un pequeño favor
| "...¡Todavía no puedo creer cuánto tiempo me tomó ese 'un pequeño favor'!"
|
|-
| Óseo Rex
| "...y así fue como ayudé a resucitar a la vieja matriarca, Osseous".
| "Un gran ser camina entre nosotros una vez más."
|-
| Nuestro hombre en el norte
| "...y ahora todo el mundo sabe que Osman es el gobernante legítimo de Menaphos, pero también ha sido exiliado de Al Kharid".
| "Si bien en algunas culturas la sangre puede decretar el derecho a gobernar, rara vez sugiere capacidad o competencia".
|-
| El camino de Gloufrie
| "...La habitación se llenó de gas y casi muero, pero Hazelmere vino a rescatarme".
| "Una historia realmente emocionante sobre el fracaso y la necesidad de ser rescatados."
|-
| Peligros de la montaña de hielo
| "... Así que ahora la máquina pico de Nurmof funciona con un molino de viento".
| "Actuaste como un verdadero servidor de Guthix en este asunto".
|-
| La locura del faraón
| "...y así es como ayudé a derrocar al faraón de Menaphos. Otra vez".
| "Podemos esperar que se rompa el ciclo de destrucción en Menaphos".
|-
| 'Club de Fito
| "...y luego derroté al Faraón y le arranqué la máscara, revelando la corrupción que había debajo".
| "Pero el problema es que la corrupción no terminó en el faraón..."
|-
| pedazos de odio
| "...y luego conecté el portal. Literalmente".
| "Más allá se esconde un horror indescriptible, pero, al menos por ahora, no tendrás gatitos".
|-
| El tesoro de Pirate
| "... ¡Y cuando cavé en medio del parque en Falador, encontré el tesoro del pirata!"
| "Esa es siempre la locura de los piratas: enterrar su botín en la tierra para que otro pueda desenterrarlo".
|-
| Plague City
| "...Y así fue como rescaté a Elena de West Ardougne".
|
|-
| El fin de la plaga
| "... ¡así que por fin el Señor Oscuro estaba muerto, Ardougne estaba libre de la plaga y los elfos podían volver a hacer crecer su ciudad!"
|
"Ese fue el final de, quizás, tu aventura más épica, Player".
"Lo que comenzó como el rescate de una mujer te llevó a través de las montañas y te hizo participar en el destino de los reinos".
"Sólo puedo admirar tu perseverancia".
|-
| Sacerdote en peligro
| "...pero con la ayuda de Drezel pude purificar el río Salve."
|
|-
| Rescate del Príncipe Ali (eliminado)
| "... ¡Y tuve que disfrazar al Príncipe Ali de mujer para poder sacarlo clandestinamente!"
|
|-
| La princesa y el mendigo
| "Llevé a Princess a dar un paseo lleno de acontecimientos por Varrock".
|
|-
| El prisionero de Glouphrie
| "...y así fue como Bolrie se reunió con su familia."
| "Reunir a las familias es una causa noble; sin embargo, lo que me cuentas de la ciudad de Arposandra es un crimen contra la naturaleza y el equilibrio, y me preocupa mucho."
|-
| Gato Púrpura (minimisión)
| "A cambio de ayudar a la bruja Wendy y a su mejor amiga, Lottie, aprendí a hacer dye permanentemente de color morado a mi gato".
|
|-
| Tranquilo ante el enjambre
| "...y desbloqueé los recuerdos de Korasi y supe lo que pasó en el barco".
| "Los Caballeros del Vacío caminan sobre una delgada línea mientras buscan el equilibrio".
|-
| Hombre de trapo y hueso
| "... ¡Conseguí todos los huesos que Odd Old Man quería y me dio una recompensa!"
| "¿Para qué podría haber querido ese hombre todos esos huesos? Recolectar tantos huesos no puede ser una actividad equilibrada".
|-
| Cazadores de ratas
| "...esos cazadores de ratas son gente rara, pero, al final, ¡había atrapado una gran cantidad de ratas por todo RuneScape!"
| "Las ratas son criaturas muy desequilibradas y es correcto controlar su número".
|-
| Reconstrucción de Edgeville (minimisión)
| "Ayudé a Mandrith a limpiar Edgeville después de que fuera atacado por los dragonantes".
|
|-
| Recipe for Disaster
| "...después de haber liberado a todos los invitados a la cena, ¡finalmente pude enfrentar al Culinaromancer y poner fin a sus locos planes!"
| "Los hechizos de tiempo de ese mago malvado enviaron una onda a través del tejido del equilibrio. ¡Me alegro de que ya no esté suelto!"
|-
| Recipe for Disaster: La búsqueda de otro cocinero
| "Ayudé al cocinero de Lumbridge a preparar un banquete centenario en el salón de banquetes del castillo. Aris congeló a los miembros del consejo a tiempo para detener a un mago malvado del pasado. Esto me dio tiempo para buscar algunas recetas especiales para protegerlos".
|
|-
| Recipe for Disaster: Derrotando al Culinaromancer
| "Le di al Culinaromancer sus postres justos y la fiesta del Duque puede continuar sin obstáculos".
|
|-
| Recipe for Disaster: Liberando Evil Dave
| "Liberé a Evil Dave".
|
|-
| Recipe for Disaster: Liberando al Rey Awowogei
| "Liberé al rey Awowogei".
|
|-
| Recipe for Disaster: Liberando Pirate Pete
| "Liberé a Pirate Pete".
|
|-
| Recipe for Disaster: Liberando Sir Amik Varze
| "Liberé a Sir Amik Varze".
|
|-
| Recipe for Disaster: Liberando a Skrach Uglogwee
| "Liberé a Skrach Uglogwee".
|
|-
| Transcripción:Recipe for Disaster: Liberando el Goblin Generals
| "Liberé el Goblin generals".
|
|-
| Recipe for Disaster: Liberando el Lumbridge Sage
| "Liberé el Lumbridge Sage".
|
|-
| Recipe for Disaster: Liberando al enano de la montaña
| "Liberé a Vestri, el enano de la montaña".
|
|-
| Campaña de reclutamiento
| "... ¡Así que descubrí sus extraños acertijos y los Caballeros del Templo me pidieron que me uniera como miembro iniciado!"
| "He oído historias sobre estos 'Caballeros del Templo' de muchos años atrás. Ten cuidado, sus motivaciones no son las que podrían hacerte creer".
|-
| Regicide
| "... Regresé para decirle a King Lathas que el asesinato fue un éxito y él me recompensó".
|
|-
| Restos del Necroseñor
| "Trabajé con un antiguo alumno de Rasial, el infame Lord Yudura, y aprendí cómo se puede consolidar el poder a partir de los rituales".
|
|-
| El Restless Ghost
| "...y una vez que le devolví el cráneo, el fantasma pudo descansar."
| "Un extraño apego a un objeto que no tiene utilidad después de la muerte."
|-
| Réquiem por un dragón
| "Me enfrenté a Vengeance y Bilrach. Aunque no pude detener su ritual, pude salvar una parte del alma de Vorkath y dejarlo descansar".
|
|-
| Ritual del Mahjarrat
| "...y, después de que los dragonantes mataron a Lucien, escondimos la Piedra de Jas nuevamente".
| "Es bueno que la piedra esté escondida una vez más, pero el daño ya está hecho. Lucien era peligroso, pero estos dragonantes podrían terminar destruyendo todo".
|-
| río de sangre
| "...y así mi aventura con el Myreque en Morytania finalmente ha llegado a su titánica conclusión. Muchos han muerto, muchos más han sufrido, pero yo salí victorioso de esas tierras oscuras."
| "No puedo evitar notar que tu viaje terminó como comenzó... con King Roald en Varrock. Pensar que tu humilde búsqueda de un sacerdote en peligro podría terminar al borde de la guerra entre Misthalin y Morytania".
|-
| Rockeando
| "...Y así fue como escuché la historia de la muerte del pirata Rabid Jack."
| "Las vidas de los piratas a menudo dan lugar a buenas historias."
|-
| Romeo y Julieta (eliminado)
| "...Le di el mensaje a Romeo, pero él no lo entendió, así que nunca estuvieron juntos".
| "Nunca hubo una historia más triste que la de Juliet y su Romeo".
|-
| Roving Elves
| "...y cuando planté el fragmento, ¡se convirtió en un árbol de cristal!"
|
|-
| Problema real
| "...Mostré que la guerra se basó en un malentendido, ¡y ahora Miscellania y Etceteria están en paz nuevamente!"
|
"¿War? ¿Para qué sirve?"
A lo que usted responde: "Absolutamente nada".
|-
| Oferta de ron
| "...¡Así fue como ayudé a mantener borrachos a los piratas zombies!"
| "¿Piratas zombis borrachos? ¿A dónde está llegando el mundo?"
|-
| Mecánica de runas
| "...Así que Clerval y yo creamos con éxito una mascota Rune Guardian".
| "Hmm, ten cuidado con esos poderes; es mejor dejarlos en manos de los dioses".
|-
| Recuerdos rúnicos
| N/A
| N/A
|-
| Misterios de runas
| "... entonces Ariane y yo atrapamos las anomalías en las ruinas debajo del Wizards' Tower, pero no descubrimos quién las había liberado ni qué eran".
| "Me temo que es mejor dejar algunas cosas en el pasado".
|-
| Mitos de las runas
| "Aprendí a crear esencias impuras, crear runas necróticas y utilizar encantamientos de nigromancia".
| "Me temo que es mejor dejar algunas cosas en el pasado."
|-
| Rune Mysteries (histórico) (eliminado)
| "... Entonces, le llevé las notas de Aubury a Sedridor, el mago principal, y, a partir de ese momento, pude extraer esencia rúnica".
| "Entonces, ¿los mortales de arriba han descubierto la magia una vez más? Muy interesante".
|-
| Sal en la herida
| "...y, cuando desperté, la reina estaba muerta y los aldeanos de Witchaven estaban libres".
| "Esto simplemente demuestra el poder del trabajo en equipo".
|-
| Cazador de escorpiones
| "... ¡Nunca hubiera pensado que tres escorpiones tomarían tanto tiempo para encontrarlos!"
|
|-
| babosa de mar
| "...y así fue como rescaté a la familia de Caroline de las babosas marinas."
|
|-
| Secretos de Amberfell
| "Conocí a Inanna en Havenhythe y salvé al pueblo de Amberfell de la plaga sanguínea".
|
|-
| Tonos de Mort'ton
| "...así que Mort'ton volvió prácticamente a la normalidad y pude poner las cortinas en reposo".
|
|-
| Sombra de la tormenta
| "... ¡Denath fue Agrith-Naar todo el tiempo! Pero logré convocar al demonio nuevamente y matarlo".
| "Agrith-Naar fue uno de los demonios que mi maestro desterró al final de la gran guerra. Parece que encontró una manera de evitar la prohibición de la intervención directa".
|-
| Una sombra sobre Ashdale
| "... Derroté a Agoroth, el líder de los crassianos, y liberé a los aldeanos".
| "Hay muchos terrores que duermen bajo la superficie del mundo. La gente de Ashdale tiene suerte de contar con un protector así".
|-
| Sheep Pastor
| "...así que las ovejas fueron sacrificadas e incineradas de forma segura".
|
|-
| Sheep Esquilador (minimisión)
| "Con mucho trabajo logré esquilar algunas ovejas para el granjero Fred. Luego me puse a girar y creé algunos ovillos de lana".
|
|-
| Escudo de Arrav
| "... así es como ayudé a devolver el Escudo de Arrav".
|
|-
| Shilo Village
| "... entonces, lo que Rashiliyia siempre quiso fue reunirse con su hijo en el más allá".
|
|-
| Sliske's Endgame
| "...y así fue como la Piedra de Jas fue destruida y Sliske encontró su fin".
| "Como guardián, debo permanecer al margen, sin embargo, no estoy triste de que Sliske esté muerto".
|-
| La amenaza de las babosas
| "... cuando le dije a Sir Tiffy que había liberado accidentalmente a la Madre Mallum, él me ascendió al rango de Prosélito dentro de los Caballeros del Templo".
| "Esa fue una respuesta extraña a un acontecimiento tan desafortunado. Pero los motivos de los Caballeros del Templo siempre han estado incomprensiblemente desequilibrados".
|-
| Fumar mata
| "... ¿quién hubiera pensado que había tantos monstruos en el pozo de Pollnivneach?"
| "Descubrirás que los monstruos pueden esconderse en los lugares más sorprendentes. De hecho, aquellos con caras amigables pueden ser lo más parecido a un monstruo. Ten mucho cuidado en tus aventuras en el desierto".
|-
| A algunos les gusta el frío
| "...y luego el huevo eclosionó y salió un pingüino bebé. Deberías haber visto la expresión en el rostro de Larry".
| "El camino de Larry nunca fue fácil, pero esto complicará las cosas.
|-
| Canción desde las profundidades
| "... entonces las almas de las personas dormidas fueron devueltas, pero Remora, la Sirena, fue asesinada por la Reina Dragón Negro durante nuestro escape".
| "Bueno, al menos su muerte evitará que la Reina se haga más fuerte y robe las almas de otras personas".
|-
| La pesadilla de un alma
| "... así que derroté a todos los monstruos en el subconsciente de Tolna y él escapó de la grieta".
| "Los monstruos más temibles se encuentran en la oscuridad de nuestras propias mentes.
|-
| Búsqueda del alma
| "Trabajé con Icthlarin para obtener acceso al Santuario del Renacimiento; un templo extraño en el inframundo".
|
|-
| Spirit de Verano
| "...Atrapé a la Bestia Spirit y la familia pudo volver a hablar, pero dijeron que solo la había hecho más poderosa".
| "He oído hablar de esa Bestia Spirit. Lo hiciste muy bien incluso para sobrevivir a tu encuentro con ella".
|-
| El Spirit de War
| "Me puse a prueba contra Hermod, the Spirit of War (y el guardaespaldas fantasma de Rasial). A pesar de ganar, Rasial acaba de regenerar a Hermod. Me queda mucho por aprender".
|
|-
| Espíritus de los Elid
| "... entonces resultó que la gente de Nardah se estaba muriendo de sed porque los espíritus de los Elid los habían maldecido por alejarse de su diosa".
| "Es terrible que la gente se aparte de su religión. Creo que los espíritus le dieron una lección a la ciudad".
|-
| Iluminación espiritual (minimisión)
| "Subí el camino hacia la iluminación en la isla de Aminishi".
|
|-
| Nacido estelar
| "Trabajé con algunos astromantes para ayudar a un star sprite a regresar a su planeta de origen y descubrí qué estaba agotando sus poderes".
|
|-
| Corazones robados
| "...pero Ozan y yo fuimos atrapados tratando de robar el diamante, y mientras intentábamos convencer al emir de que lo cambiara por su hijo, ¡su propio corazón se rindió!"
| "La vida está llena de pequeñas ironías, pero no asumas que tales coincidencias no tienen una causa deliberada."
|-
| Sucesión
| "Me asocié con Adrasteia para una última aventura antes de su coronación. Juntos rastreamos a Bilrach hasta lo más profundo del Wilderness y terminamos su plan".
|
|-
| El fin del verano
| "...y después de que derroté a la Bestia Spirit, Summer y su familia finalmente pudieron morir".
| "Se ha restablecido el equilibrio entre la vida y la muerte. Es bueno".
|-
| Canción del cisne
| "... entonces el Wise Old Man dijo que era hora de que se retirara, dejó la colonia y se fue a casa. ¡Me enseñó mucho, pero no me dejó tener su sombrero!"
|
"Un sombrero es sólo un sombrero, Player."
A lo que respondes: "¡Grrr!"
|-
| barrido
| "...Y así fue como ayudé a las brujas a preparar su gulash."
|
|-
| Trío Tai Bwo Wannai
| "... así fue como ayudé a la gente de Tai Bwo Wannai a regresar".
|
|-
| Una cola de dos gatos
| "...¡ahora Bob y Neite están muy felices juntos!"
| "¿Bob el gato? He oído hablar de esa extraña criatura, pero nunca he podido comprenderlo. No es un logro pequeño para ti poder hacerlo".
|-
| Cuentos de las Guerras de Dios (minimisión)
| "Descubrí historias de las rivalidades entre los generales de facciones dentro del Corazón de Gielinor".
|
|-
| El cuento del Muspah
| "...Y así, con Jhallan hibernando nuevamente, logré conseguir un trofeo para Erjolf".
| "Debo reflexionar si tus acciones han interferido con el equilibrio o lo han preservado. Quizás todavía haya muy poca información para decidir".
|-
| Cuentos de Nomad (minimisión)
| "Experimenté las historias de la génesis de Nomad explorando escenas crípticas y estáticas de su pasado".
|
|-
| El Temple at Senntisten
| "...Y con el portal de comunicación restaurado, Azzanadra pudo hablar con Zaros nuevamente."
|
"Finalmente, el orden cambia nuevamente hacia el equilibrio. Sabes, por supuesto, que Zamorak es simplemente un dios pretendiente. Que un mortal asuma tal poder realmente no es bueno para el equilibrio".
(después de The World Wakes) A lo que respondes "¿Qué quieres decir con un dios pretendiente? ¿No obtuvo Guthix su poder de la misma manera?"
A lo que Juna responde: "Guthix obtuvo su poder por medios honestos. No sabía lo que lograrían con sus acciones. Zamorak, sin embargo, tenía intenciones desequilibradas que no pueden ser respetadas".
|-
| Templo de Ikov (Ayudando a Lucien)
| "...Lucien dijo que el Staff o Armadyl que le di lo había hecho más poderoso".
|
|-
| Templo de Ikov (contra Lucien)
| "Me negué a darle a Lucien el Staff de Armadyl y tuve que pelear con él".
|
|-
| Ese viejo negro Magic
| "Ayudé a reunir la banda de jazz de City of Um".
|-
| Thok a ellos (saga)
| "Escuché la primera saga de Thok, el propietario (pero no el usuario) de Daemonheim skillcape. Contó una gran historia sobre cómo atravesar una mazmorra llena de enormes bestias, todo en nombre de la familia, el amor y la afición por matar criaturas de formas sorprendentemente novedosas".
|
|-
| Thok Your Block Off (saga)
| "Escuché la segunda saga de Thok, el maestro de Dungeoneering, mientras intentaba derrotar a su hermano en una batalla de fuerza".
|
|-
| Trono de Miscellania
| "...¡Así fue como me convertí en Rey/Reina de Miscellania! <ref name="gender">Si un jugador cambia de género después de la misión, el player dirá su género actual en lugar del que solía casarse en la misión, a pesar de que el NPC con el que se casa el player reconoce que el player es de un género diferente.</ref>"
|
|-
| Compañía de tres (saga)
| "Escuché la saga de Skaldrun sobre la misión de Sir Owen, Ariane y Ozan en Daemonheim en busca de un criminal que había escapado de sus garras".
|
|-
| TokTz-Ket-Eneldo
| "...y así es como derroté al TokTz-Ket-Dill y ayudé a escribir una obra de Tzhaar".
| "Ojalá hubiera podido ver tu obra, Player. Siempre me alegra escuchar tus historias".
|-
| Tomos del brujo
| "Rastreé una serie de libros escritos por Orcus, un nigromante de la Segunda Edad. A partir de ellos, aprendí algunos secretos antiguos de la nigromancia".
|
|-
| Combate Tortle (minimisión)
| "Ayudé a algunas tortugas a montar un dojo en Varrock Sewers".
|
|-
| La trampa para turistas
| "... ¡Ana no estaba muy feliz de estar encerrada en ese barril! Pero al menos la saqué del campamento minero".
|
|-
| Torre de la vida
| "...Entonces, resultó que los alquimistas habían creado un Homúnculo - una mezcla de lógica y magia."
| "Ah, eso es bueno. Siempre deben crearse nuevas formas de vida de acuerdo con un equilibrio entre diferentes principios".
|-
| Árbol Gnome Pueblo
| "...Y King Bolren me agradeció por derrotar al señor de la guerra y devolver los orbes al pueblo gnomo".
|
|-
| Tótem tribal
| "...Devolví el tótem y la tribu Rantuki me recompensó por mi ayuda."
|
|-
| Romance trol
| "...así que Ug y Aga vivieron felices para siempre."
|
|-
| Fortaleza troll
| "...y, después de rescatar a Godric, ¡Dunstan me dio dos lámparas mágicas como recompensa!"
|
|-
| El propio Tuai Leit (minimisión)
| "Exploré la isla de Tuai Leit en busca de una cura para Ekahi".
|
|-
| Crepúsculo de los dioses
| "Me preparé para restablecer los Edictos para evitar que Zamorak se hiciera cargo de Gielinor".
|
|-
| Underground Pass
| "... ¡No sé quién puso todas esas trampas en el underground pass!"
|
|-
| Invitados no deseados
| "Encontré la fuente de los no-muertos que atacaban a Fort Forinthry y ayudé a the Raptor a establecer un frente defensivo".
|
|-
| Vampyre Slayer
| "...Y una vez que el vampyre estuvo muerto, la gente de Draynor ya no vivió con miedo".
|
|-
| Venganza (saga)
| "Escuché la saga de Skaldrun sobre un guerrero olvidado, vengativo y envenenado".
|
|-
| Vasija del Heraldo
| "Trabajé con un antiguo alumno de Rasial, Necrovarus de Port Phasmatys, y aprendí más sobre las naves nigrománticas".
|
|-
| Violet es azul
| "...y así fue como logré escoltar a Violet a través del País de la Nieve hasta el festival".
| "¡Qué historia tan edificante! Es una pena que no me traigas más como estas".
|-
| Violet también es azul
| "Con la ayuda de Violet, encontramos al diablillo de nieve perdido y ayudamos a salvar la ciudad de Yeti consiguiendo nuevas decoraciones navideñas y logramos decorar la ciudad a tiempo para el día de Navidad".
|
|-
| Visiones de Havenhythe
| "Recibí una visión que me llamaba a la antigua y hermosa tierra de Havenhythe y ayudé a los aldeanos de Wendlewick a construir un lodestone".
|
|-
| Una danza del vacío
| "...y cuando finalmente localicé a Void Leech desaparecido, lo solucioné apropiadamente".
| "Tus decisiones y elecciones son un asunto de tu propia conciencia."
|-
| El vacío te devuelve la mirada
| "... así que derroté a la Reina Pest, pero perdí a un buen amigo".
| "Los caballeros no han estado unidos desde hace mucho tiempo."
|-
| ¡Buscado!
| "...y, después de que finalmente logré localizarlo, ¡déjame decirte que Solus Dellagar era casi tan poderoso como loco!"
| "Sí, parece que sacrificó su cordura por el poder. El poder a menudo tiene un costo, y el costo más alto suele ser el que no se ve de inmediato".
|-
| Ga'al errante (minimisión)
| "Encontré un explorador de Ga'al que desapareció gracias a una serie de circunstancias muy específicas. Quienquiera que los haya concebido seguramente debe poseer un corazón de descaro."
|
|-
| Atalaya
| "...y con el generador de escudo funcionando, los ogros nunca más podrían amenazar a Yanille".
|
|-
| Búsqueda de la cascada
| "...Y así fue como recuperé el Cáliz de la Eternidad de la cascada."
|
|-
| Lo que hay debajo
| "...pero después de que derroté a King Roald, Rat pudo quitarle el hechizo de control mental de Surok".
| "Veo que los servidores de Zamorak todavía desempeñan su papel en el equilibrio del mundo entre el bien y el mal".
|-
| Lo que es mío es tuyo
| "...y así fue como convencí a Doric para que volviera al negocio."
| "Una historia edificante; te deseo lo mejor en tus futuros proyectos".
|-
| Mientras Guthix duerme
| "... ¡Pero Lucien tomó la Piedra de Jas y se teletransportó!"
| "Deberías saber que no debes interferir. Sin tu participación, la piedra aún permanecería donde mi maestro la había puesto. Pero aún puede salir algo bueno de esto. Ya veremos".
|-
| Casa de la bruja
| "... ¡Todos esos problemas sólo para sacar una pelota del jardín de alguien!"
| "A menudo es difícil saber cuánto tiempo llevará una tarea cuando la iniciamos".
|-
| Poción de bruja (eliminada)
| "...Y una vez que le conseguí todos los ingredientes, ¡la poción de Hetty aumentó mi poder mágico!"
| "Veo que estás en camino de volverte fuerte en las artes mágicas".
|-
| Poción de bruja (minimisión)
| "¡Tengo los ingredientes de una bruja de primera clase! Creé un brebaje de bruja con un poco de ayuda de Hetty".
|
|-
| Within the Light
| "...Y eso es lo que pasó within the light.
| "Debe haber sido necesario un gran poder para contener tal área dentro de la propia luz. Intrigante."
|-
| niño mago
| "Fui mentor de un joven aspirante a mago, Ben, en los caminos de las runas".
|
|-
| Silbato de lobo
| "...Y así fue como logré evitar que los trolls hicieran sopa de druida."
|
|-
| Wolf Whistle (histórico) (eliminado)
| "...Y así fue como aprendí los secretos de la invocación."
|
|-
| El mundo despierta
|...Pero ya era demasiado tarde. Sliske había dado el golpe mortal. Antes de que Guthix muriera, me mostró cómo será el mundo si los dioses regresan y me dio poder para defenderme de ellos.
| "Estos eventos han allanado el camino para una nueva era. La muerte de Guthix eliminó los edictos de este mundo, permitiendo que los dioses regresen. Debes recordar lo que te dijo, Player".
|-
| tu lo eres
| "...y así fue como superé la maldición del cumplidor de deseos y restauré Uri.
| "Las baratijas de Charos parecen tener más poder de lo que habíamos sospechado anteriormente".
|-
| Devoradores de carne de Zogre
| "... ¡Esos Zogres eran asquerosos! Pero aprendí a luchar contra ellos con flechas brutales y bálsamos contra enfermedades".
| "¿¡Ogros zombis!? Algunas de las criaturas más repugnantes de Zamorak. En las grandes guerras, los ejércitos de zogre repelerían a las fuerzas de Saradomin sólo con su hedor."
|}
<references />

### In Lumbridge during the 25th Anniversary celebrations

- **Player:** Hola, ¿qué haces aquí?
- **Juna:** Celebrando el aniversario, pero también lamentando todo lo que hemos perdido.
- **Juna:** Estos últimos diez años han estado llenos de tiempos difíciles e historias tristes.
- **Juna:** Me ha parecido como si el mundo estuviera fuera de equilibrio, desde entonces...
- **Player:** No es necesario que lo digas. Yo también lo he sentido. Creo que todos lo hemos hecho.
- **Juna:** Fue el regreso de los dioses, que comenzó aquí mismo con la Batalla de Lumbridge, que causó ese cráter justo encima de donde está mi nido.
- **Juna:** La gente ha estado peleando entre sí desde entonces, dividida en facciones y sus corazones invadidos por la codicia.
- **Juna:** Las Lágrimas de Guthix han estado llorando copiosamente desde entonces, y yo con ellas...
- **Juna:** Pero uno no puede permanecer perdido en el dolor para siempre, y finalmente comienza a sentir como si el estado de ánimo estuviera cambiando.
- **Player:** Muy cierto.
- **Juna:** Por eso vine de visita: para honrar el pasado, pero también para mirar hacia el futuro, y ¿qué mejor momento para reinventarse que un aniversario? Se acerca el cambio.
- **Player:** ¿Qué cambia?
- **Juna:** ¿No viste que el cráter desapareció? ¡No sólo ha sanado, sino que ha rejuvenecido!
- **Juna:** Tampoco es sólo el cráter. He escuchado muchas historias de cambios positivos en nuestro mundo.
- **Juna:** E incluso aquí puedes ver a personas dispares volver a unirse: viejas amistades se renuevan.
- **Juna:** Su alegría también es palpable. Ya no se siente que cada uno está en esto por sí mismo. La codicia está dando paso a la generosidad.
- **Juna:** Es cierto, hay muchas heridas que sanar y muchas amistades que reavivar, pero realmente parece que la esperanza está regresando a Gielinor una vez más y el equilibrio con ella.
- **Player:** Sabes, creo que has descubierto algo. ¡Aquí está el futuro!
