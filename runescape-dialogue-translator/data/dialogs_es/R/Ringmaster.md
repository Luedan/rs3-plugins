# Ringmaster

- **Original Wiki Page**: [Transcript:Ringmaster](https://runescape.wiki/w/Transcript%3ARingmaster)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{incomplete|missing dialogue for Summer Sweepstakes; missing dialogue when completing performances and unlocking outfits}}

### In Balthazar's Big Top Bonanza


#### Diálogo por primera vez

- **Ringmaster:** Ah, una cara nueva. ¿Podrías ser nuestro nuevo intérprete?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, lo soy.
    - **Ringmaster:** ¡MARAVILLOSO! Maravilloso. ¿Pero eres humano? Bueno, los mendigos no pueden elegir.
    - **Player:** ¿Qué pasa con-?
    - **Ringmaster:** Ahora, tenemos varios actos que necesitan un artista. ¿En qué acto te gustaría actuar?
    - [Menu]: Elige una opción:
      - [Choice]: Agility
        - (below|agility)
      - [Choice]: Magic
        - (below|magic)
      - [Choice]: Ranged
        - (below|ranged)
      - [Choice]: Firemaking {{clarify|Does this only appear if the Firemaking act has been unlocked?}}
        - (below|firemaking)
      - [Choice]: Thieving {{clarify|Does this only appear if the Thieving act has been unlocked?}}
        - (below|thieving)
  - [Choice]: Eh, no. Estaba simplemente echando un vistazo a mi alrededor.
    - **Ringmaster:** Ah, muy bien. Supongo que no todos están destinados a ser el centro de atención.

#### Diálogo posterior

- **Ringmaster:** Ah, mi pequeño intérprete. ¿Qué puedo hacer por ti?
- [Menu]: ¿Podrías hablarme de...?
  - [Choice]: las actuaciones
    - {{anchor|performances-opts}}[Menú]: Elige una opción:
      - [Choice]: ¿Qué actuaciones he hecho?
        - (Condition: If the player has only done the one performance:)
          - **Ringmaster:** Has hecho tu _____ actuación.
          - (continue|tell-me-about)
        - (Condition: If the player has done all the performances:)
          - **Ringmaster:** Has hecho todas tus actuaciones de esta semana. Que dedicación tienes.
          - (continue|tell-me-about)
      - [Choice]: Agility.{{anchor|agility}}
        - **Ringmaster:** ¡Ah, este es un acto verdaderamente temible! Debes caminar por la cuerda floja y realizar atrevidas hazañas de agilidad. Volteretas, giros, malabarismos con chinchompas; Realmente es sólo para los valientes.
        - **Player:** ¿Chinchompas? ¿Malabarismo?
        - **Ringmaster:** Te proporcionaremos un disfraz; simplemente diríjase a la tienda para cambiarse junto a la escalera. Te cambiarás allí y te llevarán a la plataforma. Puede comenzar de inmediato o hablar con el asistente en la plataforma en la parte superior de la escalera, quien le explicará los detalles.
        - {{anchor|whats-in-it}}[Menú]: Seleccione una opción
          - [Choice]: ¿Qué gano yo con esto?
            - (below|rewards)
          - [Choice]: ¿Cómo salgo del circo?
            - (below|leave)
      - [Choice]: Magic.{{anchor|magic}}
        - **Ringmaster:** Ah, una práctica antigua, ideal para ser el centro de atención. Deslumbra al público con tus demostraciones de hazañas imposibles. No necesitarás ninguna runa. Habla con el hada vestida de mago y ella te explicará los detalles, o si sientes que ya estás listo, ¡puedes quedarte atrapado!
        - (continuea|whats-in-it)
      - [Choice]: Ranged.{{anchor|ranged}}
        - **Ringmaster:** Un lugar perfecto para poner a prueba tu habilidad de tiro. Debes alcanzar con éxito 10 objetivos desde la distancia que elijas. Pero no mates a tu asistente, ya que importar hadas es caro. Nosotros te proporcionaremos el equipo, por lo que no habrá ningún coste para ti. Habla con el hada del traje verde cerca de la diana para obtener más información o comienza de inmediato.
        - (continuea|whats-in-it)
      - [Choice]: Más. {{clarify|Does this only appear if either the Firemaking/Thieving acts have been unlocked?}}
        - [Menu]: Elige una opción:
          - [Choice]: Firemaking.{{anchor|firemaking}}{{clarify|Does this only appear if the Firemaking act has been unlocked?}}
            - **Ringmaster:** ¡Por supuesto! ¿Cuál te gustaría saber sobre?
            - [Menu]: Selecciona una opción
              - [Choice]: poi de fuego
                - **Ringmaster:** ¡Ah, ten cuidado con ese! ¡Debes realizar con éxito 6 trucos de poi en llamas! Tenga cuidado de no encender nada... no queremos que eso vuelva a suceder.
                - **Player:** ¿Otra vez?
                - **Ringmaster:** ¡No importa eso, mi pequeño artista! Habla con Emmett en el área de los fogoneros y él te explicará los detalles, o puedes comenzar de inmediato tomando tu lugar en la estrella cerca de él.
                - (continuea|whats-in-it)
              - [Choice]: escupe fuego
                - **Ringmaster:** ¡Un evento atrevido y colorido! ¡Debes escupir fuego con éxito 6 veces, en multitud de colores!
                - **Ringmaster:** Habla con Sera en el área de los fogoneros y ella te explicará los detalles, o puedes comenzar de inmediato tomando tu lugar en la estrella cerca de ella.
                - (continuea|whats-in-it)
          - [Choice]: Thieving.{{anchor|thieving}}{{clarify|Does this only appear if the Thieving act has been unlocked?}}
            - **Ringmaster:** ¿Quieres poner a prueba tus habilidades de prestidigitación, verdad? En un mundo lleno de hazañas imposibles, a menudo las más simples son las más sorprendentes.
            - **Ringmaster:** Puedes hablar con Teddy, el oso polar, para obtener más detalles, o puedes comenzar de inmediato tomando tu posición en la estrella cercana a él.
            - (continuea|whats-in-it)
          - [Choice]: Atrás
            - (previous)
  - [Choice]: Mejorando mi rendimiento{{anchor|improve-performance}}
    - **Ringmaster:** ¡Ah, hay tantas cosas que implica ser un verdadero virtuoso! El público es clave para cualquier gran actuación. Debes escuchar lo que quieren y apaciguarlos. Les encanta ver realizados sus pedidos. También odian la repetición, así que no sigas haciendo el mismo movimiento seguro. ¡Sé peligroso! Prueba movimientos más difíciles y quién sabe, tal vez lo consigas. Todo lo que puedes hacer aquí está clasificado por dificultad en relación a tu skill levels, pero solo son niveles recomendados. Eres bienvenido a intentar lo que quieras, pero es más probable que tengas éxito si tienes el skill level correspondiente.
    - **Player:** ¿Qué pasa si no puedo hacer movimientos más difíciles? ¡No puedo evitar repetir!
    - **Ringmaster:** ¡Entonces realiza un gesto entre movimientos! Eso hará feliz al público; sin embargo, no los repita. Nuestras audiencias son muy volubles y ODIAN la repetición. Además, sólo te damos un bono de puntos por los primeros 10 que realices.
    - **Player:** ¿No existe una forma más sencilla de mejorar mi rendimiento? El público puede ser muy exigente.
    - **Ringmaster:** Por supuesto. Usa disfraces locos: ¡cuanto más locos, mejor! No te diré qué ropa usar, ya que es del gusto del artista, pero experimenta. Vea qué funciona mejor para usted. Por razones de seguridad, solo puedes usar el disfraz que te proporcionamos para la presentación de Agility. Además, esté atento a dónde se mueve el vendedor de entradas y quiénes forman parte de nuestra audiencia. Diferentes ubicaciones tienen diferentes preferencias y eso te dará una ventaja.
    - **Player:** ¡Gracias por el consejo!
    - **{{anchor|tell-me-about}}Ringmaster:** ¿Le gustaría saber algo más?
    - {{anchor|tell-me-about2}}[Menú]: Háblame de...
      - [Choice]: las actuaciones
        - (above|performances-opts)
      - [Choice]: Mejorando mi desempeño
        - (above|improve-performance)
      - [Choice]: las recompensas
        - (below|rewards)
      - [Choice]: el circo
        - (below|circus)
      - [Choice]: No importa
        - **Player:** No importa.
  - [Choice]: Las recompensas{{anchor|rewards}}
    - [Menu]: Selecciona una opción
      - [Choice]: Quiero recuperar un disfraz.
        - (opens=Circus Rewards)
      - [Choice]: Quiero saber más sobre las recompensas.
        - **Player:** No es que actuar no sea genial en sí mismo, pero ¿qué gano por hacerlo? No puedes esperar que trabaje gratis.
        - **Ringmaster:** ¿Qué pasó con los días en que la emoción de actuar era suficiente? Por supuesto, recompenso a mis artistas, pero trabajo con un método de pago relacionado con el desempeño. Cuanto mejor lo hagas, mejor te recompensaré. Tu actuación en sí es una recompensa, porque obtienes más experiencia de la que normalmente obtendrías en la habilidad que desempeñas. Al final de tu actuación, reviso qué tan bien lo hiciste y te recompensaré con experiencia extra y una parte de un disfraz.
        - **Player:** ¿Qué disfraz?
        - **Ringmaster:** ¡No solo uno, sino varios! Para aquellos que simplemente... ponen el mínimo esfuerzo, los premio con piezas de disfraces de campesinos y alguna que otra mano gigante. Para aquellos que se esfuerzan cada vez más, consiguen trajes de actuación. Reparto piezas para un disfraz de acróbata, un disfraz de payaso y, para aquellos que son realmente increíbles (como yo), ¡reparto un disfraz de maestro de ceremonias!
        - **Player:** Eso no está tan mal, supongo. Espero que el mío encaje mejor que el tuyo.
        - **Ringmaster:** ¡Me gustaría verte encontrar un sastre que pueda hacer pantalones talla 115!
        - (continuea|tell-me-about)
      - [Choice]: No importa.
        - **Player:** No importa.
  - [Choice]: El circo{{anchor|circus}}
    - **Player:** Háblame del circo. Es un poco extraño.
    - **Ringmaster:** Es un circo. *Se supone* que es extraño. ¿Qué te gustaría saber?
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Por qué hay tan poca gente aquí?
        - **Player:** ¿Por qué casi no hay nadie aquí? ¿Y por qué soy tu único intérprete?
        - **Ringmaster:** No somos más que un negocio nuevo y aún no hemos atraído a muchos clientes. Por eso hay tan poca gente en las gradas. Pero con un artista tan bueno como usted, esperamos atraer más clientes y más artistas.
        - (continuea|tell-me-about2)
      - [Choice]: ¿Dónde estamos?
        - **Ringmaster:** Ah, existimos dentro del vendedor de boletos. Doblamos el espacio sobre sí mismo para que quepa algo más pequeño que el espacio que ocupamos. Es todo muy complejo, pero las hadas me dicen que es bastante fácil.
        - **Player:** Entonces, ¿actualmente estoy plegado en el espacio? ¿Va a doler desplegarse?
        - **Ringmaster:** No, por supuesto que no. No es diferente a teletransportarse normalmente.
        - (continuea|tell-me-about)
      - [Choice]: ¿Cómo salgo del circo?{{anchor|leave}}
        - **Player:** ¿Cómo salgo del circo? Todas las salidas están acordonadas.
        - **Ringmaster:** Pequeño artista tonto, te dieron un boleto dorado cuando entraste al Big Top Bonanza de Balthazar Beauregard, ¿no?
        - **Player:** Sí, lo hice.
        - **Ringmaster:** Bueno, ¡léelo! Dice que sólo necesitas romperlo para salir del circo. Rompe el billete y 'POOF', te has ido. Así de simple.
        - **Player:** Gracias.
  - [Choice]: No importa
    - **Player:** No importa.

#### Opción de recompensas

- **Ringmaster:** Ah, pequeño artista. ¿Has perdido una de tus recompensas?
- [Menu]: Selecciona una opción
  - [Choice]: si
    - **Ringmaster:** Muy bien, vamos a conseguirte algunos reemplazos.
    - (opens=Circus Rewards)
  - [Choice]: No
    - **Player:** No.

### Balthazar's Big Raffle


#### Durante el sorteo


##### Líneas aéreas

- {{Trandom}}
  - **Baltasar:** {{RSChat|Come get your RuneScape raffle tickets while they're hot!}}
  - **Baltasar:** {{RSChat|Roll up! Roll up! This month only the RuneScape Raffle!}}
  - **Baltasar:** {{RSChat|Win prizes in the RuneScape Raffle today!}}
  - **Baltasar:** {{RSChat|You've got to be in it to win it!}}

##### Cuando se habla con

- (Condition: If the daily ticket hasn't been claimed:)
  - **Balthazar:** Ahh, no has tenido multa. ¡Arremangar! ¡Arremangar! ¡Consigue tu entrada mientras hace calor!
    - (Condition: If the player has space in their backpack:))
      - Recibes un boleto gratis para el sorteo.
      - (Continues below)
    - (Continues below)
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué es todo esto de una rifa?
    - **Player:** ¿Qué es todo esto de una rifa?
    - **Baltasar:** ¡Enróllate! ¡Arremangar! ¡Participa en mi sorteo! ¡Gana premios!
    - **Balthazar:** Hablame diariamente y te daré un boleto. Puedes conseguir otro del payaso Gilly Willikers una vez al día o realizando un desafío diario.
    - **Balthazar:** Si te perdiste uno o dos boletos, ¡puedes usar un bono para poder reclamar los que te perdiste! ¡Y cualquiera que te puedas perder en el futuro!
    - **Balthazar:** Ingresa tus boletos de inmediato o guárdalos: ¡habrá un sorteo diario!
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Dónde está Gilly Willikers ahora?
        - *(Continúa con la pista.)*
      - [Choice]: ¡Gracias!
        - (initial)
  - [Choice]: Me gustaría participar en el sorteo de hoy.
    - **Player:** Me gustaría participar en el sorteo de hoy.
    - (opens RS Raffle interface)
  - [Choice]: ¿Cuáles son las recompensas del sorteo?
    - **Player:** ¿Cuáles son las recompensas del sorteo?
    - **Balthazar:** Los premios del sorteo cambian cada día. Si está interesado en algo específico, querrá regresar e ingresar ese día.
    - **Balthazar:** ¡Asegúrate de llegar todos los días para que pueda darte tu boleto!
    - (initial)
  - [Choice]: ¿Cuántas entradas han entrado hasta el momento en el sorteo de hoy?
    - (Condition: If the player hasn't entered today's raffle:)
      - **Balthazar:** Hoy se ingresaron un total de boletos [número] con premios totales [número] disponibles. No has participado en el sorteo de hoy. ¿Le gustaría?
      - [Menu]: Selecciona una opción
        - [Choice]: Me gustaría participar en el sorteo.
          - (opens RS Raffle interface)
        - [Choice]: No gracias.
          - (initial)
    - (Condition: If the player has entered today's raffle:)
      - **Balthazar:** Has participado en [número] [ticket/tickets] en el sorteo de hoy y ha habido un total de boletos [número] ingresados hoy con premios totales [número] disponibles.
      - (initial)
  - [Choice]: Adiós
    - **Player:** Adiós.
    - **Baltasar:** ¡Vuelve pronto!

##### Intentar utilizar boletos de rifa de años anteriores antes de 2019

- **Baltasar:** ¿Qué es eso ahí? ¡Parecen falsificaciones! ¡Dame esos!
- **Baltasar:** {{RSChat|Don't trust Player! They tried to scam me with their dodgy tickets!}}

##### Obteniendo pista

- **Player:** ¿Dónde está Gilly Willikers en este momento?
  - (Condition: If Gilly is in Al Kharid:)
    - **Balhazar:** Parece que fue visto por última vez en Al Kharid.
    - **Player:** ¡Gracias!
  - (Condition: If Gilly is in Draynor Village:)
    - **Balhazar:** Creo que actualmente está visitando Draynor.
    - **Player:** ¡Gracias!
  - (Condition: If Gilly is in Edgeville:)
    - **Balhazar:** Aparentemente está en Edgeville.
    - **Player:** ¡Gracias!
  - (Condition: If Gilly is in Falador:)
    - **Balhazar:** Hmm, recientemente lo vieron deambulando por la puerta principal de Falador.
    - **Player:** ¡Gracias!
  - (Condition: If Gilly is in Lumbridge:)
    - **Balhazar:** No hace mucho estaba explorando el castillo Lumbridge.
    - **Player:** ¡Gracias!
  - (Condition: If Gilly is in Taverley:)
    - **Balhazar:** Fue visto en Taverley no hace mucho.
    - **Player:** ¡Gracias!
  - (Condition: If Gilly is in Varrock:)
    - **Balhazar:** He escuchado informes de que está en Varrock.
    - **Player:** ¡Gracias!

#### Después del sorteo


##### Cuando se habla con

- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué es todo esto de una rifa?
    - **Player:** ¿Qué es todo esto de una rifa?
    - **Balthazar:** Lamento que el sorteo de RuneScape haya terminado.
    - **Balthazar:** Sólo estoy aquí para repartir los últimos premios.
    - **Player:** ¿Tienes un premio para mí?
      - (Condition: If there are unclaimed prizes:)
        - (opens the RS Raffle interface)
      - (Condition: If there are no unclaimed prizes:)
        - **Baltasar:** No, nada para ti. Avanzar.
  - [Choice]: ¿Cuáles son las recompensas del sorteo?
    - **Player:** ¿Cuáles son las recompensas del sorteo?
    - **Balthazar:** Los premios del sorteo cambian cada día. Si está interesado en algo específico, querrá regresar e ingresar ese día.
    - **Balthazar:** Desafortunadamente, la rifa ya no existe. Prueba suerte la próxima vez.
    - (initial)

##### Al abrir el sorteo

- El sorteo ya ha finalizado.

##### Al recibir una pista

- **Balthazar:** La parte principal del sorteo no se realiza en este momento, por lo que Gilly ya no repartirá boletos.

### During Summer Sweepstake

- {{Transcript missing}}
