# Advisor Ghrim

- **Original Wiki Page**: [Transcript:Advisor Ghrim](https://runescape.wiki/w/Transcript%3AAdvisor%20Ghrim)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{transcript npc|Advisor Ghrim}}

### Before Throne of Miscellania

- **Advisor Ghrim:** Saludos, [Sir/Madam].
- (Action: Si el player ha matado previamente a alguien en Miscellania:)
  - **Advisor Ghrim:** Puedo decirte de inmediato que matar a alguien no te hará popular entre nadie.
  - (continue)
- **Advisor Ghrim:**  El rey necesita a alguien que se haga cargo del gobierno del reino. Si yo fuera usted, debería considerar el puesto.
- [Menu]: Elige una opción:
  - [Choice]: Háblame del Sistema de Logros.
    - (Action: abajo)
  - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
    - (Action: abajo)
  - [Choice]: Lo siento, me estaba yendo.
    - (end)

### After Throne of Miscellania


#### Hablando con Advisor Ghrim

- **Advisor Ghrim:** Saludos, Su Alteza Real.
- (Action: Si el player ha matado previamente a alguien en Miscellania:)
  - **Advisor Ghrim:** Su Alteza Real, debo decirle de inmediato que matar a la gente de este reino no le hará popular entre nadie.
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: ¿Cómo le va al reino?
    - **Player:** ¿Cómo le va al Reino?
      - (Condition: Si el índice de aprobación de el player es suficientemente alto:)
        - **Advisor Ghrim:** Sus súbditos están contentos, Su Alteza.
        - (continue)
    - **Advisor Ghrim:** Tu índice de aprobación es [número]%. ¿Le gustaría recopilar los recursos recopilados por sus sujetos?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, por favor.
        - **Player:** Sí, por favor.
        - **Advisor Ghrim:** Aquí hay una lista de lo que tus sujetos han recopilado.
        - *(Se abre la interfaz de Recursos del Reino.)*
        - (Condition: Después de recolectar los recursos:)
          - **Advisor Ghrim:** Le diré a sus súbditos que entreguen sus recursos a su banco de inmediato, Su Alteza Real.
          - **Advisor Ghrim:** Así es como tus súbditos están distribuyendo su esfuerzo.
          - *(Se abre la interfaz del Reino de Miscellania.)*
      - [Choice]: No, gracias.
        - **Player:** No, gracias.
        - **Advisor Ghrim:** Muy bien, Su Alteza Real.
        - **Advisor Ghrim:** Así es como tus súbditos están distribuyendo su esfuerzo.
        - *(Se abre la interfaz del Reino de Miscellania.)*
  - [Choice]: cond=Between Glorious Memories and Blood Runs Deep|¿Qué pasó con King Vargas?
    - **Player:** ¿Qué pasó con King Vargas?
    - **Advisor Ghrim:** Su Majestad acaba de emprender su última gran aventura. No sé cuándo regresará, Su Alteza Real {{Sic}}.
  - [Choice]: cond=After Blood Runs Deep|Es bueno tener de vuelta a King Vargas.
    - **Player:** Es bueno tener de vuelta a King Vargas.
    - **Advisor Ghrim:** Ciertamente lo es, y entiendo que tiene que agradecerle a usted, Su Majestad.
    - **Advisor Ghrim:** Quizás, ahora que Queen Sigrid se ha mudado, no se sentirá tentado a emprender más "aventuras".
  - [Choice]: ¿Cómo administro el reino?
    - **Player:** ¿Cómo administro el reino?
    - **Advisor Ghrim:** Tus súbditos leales trabajan duro para recolectar recursos para ti. Todos los días traen al castillo lo que han recogido. Los recursos que recolectan son carbón de las rocas del norte, maple logs de los árboles del este, hierbas del jardín a las afueras del castillo y atún y pez espada pescados en el puerto del sur.
    - (Condition: Antes del problema real:)
      - **Advisor Ghrim:** Se les paga con el dinero que hay en las arcas; cada día se les distribuye una décima parte del dinero de las arcas. Se paga un máximo de 75.000 a tus súbditos y las arcas pueden almacenar hasta 7,5 millones de po.
      - (continue)
    - (Condition: Después del problema real:)
      - **Advisor Ghrim:** Etceteria también le ha prometido teca y caoba logs de sus árboles al norte, y semillas de su granja al sur. Se les paga con el dinero de las arcas; cada día se les distribuye una décima parte del dinero de las arcas. Se paga un máximo de 75.000 a tus súbditos y a los etceterianos, y las arcas pueden almacenar hasta 7,5 millones de po.
      - (continue)
    - **Advisor Ghrim:** Otra cosa que afecta la cantidad de recursos recopilados es su índice de aprobación. Cuanto más te amen tus súbditos, más motivados estarán para trabajar duro. King Vargas solía ir a ayudar a sus súbditos en sus tareas diarias, cuando todavía podía hacerlo, y lo querían mucho por ello. Finalmente, puedes elegir cuánto esfuerzo dedican tus sujetos a cada recurso; Por supuesto, cuanto más trabajen para recolectar uno, menos tiempo tendrán para recolectar los demás.
    - (Condition: Si el player no tiene una copia del libro de Ghrim:)
      - **Advisor Ghrim:** ¿Tienes una copia de mi libro? Explica todo con más detalle.
      - **Player:** No, no lo hago...
      - **Advisor Ghrim:** Toma, puedes quedarte con este, tengo muchos de repuesto.
      - **Player:** ¡Gracias!
      - (receives=Ghrim's book)
  - [Choice]: ¿Qué se supone que debo hacer de nuevo?
    - **Player:** ¿Qué se supone que debo hacer de nuevo?
    - **Advisor Ghrim:** Gobernando el reino, Su Alteza Real.
    - **Advisor Ghrim:** Y asegurándonos de que el rey no cause más problemas.
  - [Choice]: Acerca del sistema de tareas...
    - (Action: abajo2|Sistema de tareas)

### Collect

- **Advisor Ghrim:**  Aquí tienes una lista de lo que tus sujetos han recopilado.
- *(Se abre la interfaz de Recursos del Reino.)*
- **Advisor Ghrim:**  Les diré a sus súbditos que entreguen sus recursos a su banco de inmediato, Su Alteza Real.
- **Advisor Ghrim:** Así es como tus súbditos están distribuyendo su esfuerzo.
- *(Se abre la interfaz del Reino de Miscellania.)*

##### Si no hay recursos para recolectar

- **Advisor Ghrim:** Me temo que tus súbditos no han recopilado nada.

### Manage

- **Advisor Ghrim:**  Así es como tus sujetos distribuyen su esfuerzo.
- *(Se abre la interfaz del Reino de Miscellania.)*

### Task System

- ((Si el player ha completado los logros difíciles de Fremennik y no se han reclamado las recompensas:))
  - **Player:** He completado todas las tareas difíciles del conjunto Fremennik.
  - **Advisor Ghrim:** Sí, alteza, ya lo veo. Tengo aquí unas botas viejas que descubrí en el tesoro y que quizás deberías llevarte.
  - (receives=Fremennik sea boots 3 and Antique lamp (Hard Fremennik Tasks))
    - (Condition: Si el player no tiene suficiente espacio en backpack:)
      - **Advisor Ghrim:** Desafortunadamente, no puedes llevarlos en este momento.
    - (Condition: Si el player tiene suficiente espacio en backpack:)
      - **Advisor Ghrim:** Ahí lo tienes. Deberías mirar con atención para ver qué pueden hacer.
      - **Advisor Ghrim:** Por ejemplo, si tienes furniture de repuesto en paquete plano, podría comprártelo y poner el oro en las arcas. Estamos ampliando los asentamientos en las mazmorras y el furniture de repuesto podría resultar muy útil.
      - **Player:** ¡Gracias!
      - (continue)
- ((Si el player ha completado los logros de élite de Fremennik y no se han reclamado las recompensas:))
  - **Player:** He completado todas las tareas de élite del conjunto Fremennik.
  - **Advisor Ghrim:** Sí, alteza, ya lo veo. Tengo aquí unas botas viejas que descubrí en el tesoro y que quizás deberías llevarte.
  - (receives=Fremennik sea boots 4, four Antique lamps (Elite Fremennik Tasks, 30k) y lámpara antigua (Elite Fremennik Tasks, 40k))
  - **Advisor Ghrim:** Ahí lo tienes. Deberías mirar con atención para ver qué pueden hacer.
  - **Advisor Ghrim:** Por ejemplo, esa lira bárbara podría llevarte a más lugares; habla con Rimae Sirsalis para intercambiar piel y dientes de suqah por esencia de run; usa el hechizo NPC contact para cambiar tu libro de hechizos de Lunar al libro de hechizos estándar y usa el sello Sello de paso para teletransportarte a Lunar Isle una vez al día.
  - **Player:** ¡Gracias!
  - (continue)
- (Condition: Si el player ha perdido su Fremennik sea boots 3:)
  - **Advisor Ghrim:** Su Alteza, ¿cómo están las botas?
  - **Player:** Los perdí.
  - **Advisor Ghrim:** ¿En serio? Aquí encontré algo más en el tesoro.
  - (receives=Fremennik sea boots 3)
  - {{tbox|pic=Fremennik sea boots 3 detail.png|Advisor Ghrim hands you another pair of boots.}}
  - (continue)
- (Condition: Si el player ha perdido su Fremennik sea boots 4:)
  - **Advisor Ghrim:** ¿Cómo están las botas, Alteza?
  - **Player:** Los perdí.
  - **Advisor Ghrim:** ¿En serio? Aquí encontré algo más en el tesoro.
  - (receives=Fremennik sea boots 4)
  - {{tbox|pic=Fremennik sea boots 4 detail.png|Advisor Ghrim hands you another pair of boots.}}
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: Háblame del Sistema de Logros.
    - **Advisor Ghrim:** Muy bien: el Sistema de Logros es una colección de hazañas que quizás desees completar mientras viajas por el mundo.
    - **Advisor Ghrim:**Puedes ganar recompensas especiales por completar ciertos logros; como mínimo, cada uno vale una recompensa en efectivo de Explorer Jack en Lumbridge.
    - **Advisor Ghrim:** Algunos también ofrecen elementos que ayudarán a completar otros logros y muchos cuentan como progreso hacia el conjunto del área en la que se encuentran.
    - [Menu]: Elige una opción:
      - [Choice]: Cuéntame sobre la recompensa establecida para esta localidad.
        - **Player:** Cuéntame sobre la recompensa establecida para esta área.
        - **Advisor Ghrim:** Su Alteza, la recompensa del conjunto Fremennik es un par de botas de mar.
        - **Advisor Ghrim:** Estas botas serán cada vez más útiles con cada nivel de dificultad del conjunto que completes.
        - **Advisor Ghrim:** Cuando se le presenten sus recompensas, se le informará sobre sus usos.
        - También puedes ver qué recompensas proporciona un elemento determinado al pasar el cursor sobre el ícono de Recompensas de su Logro de exploración establecido en la interfaz de Logros.
        - (Action: anterior2)
      - [Choice]: ¿Cómo reclamo estas recompensas?
        - **Player:** ¿Cómo reclamo las recompensas?
        - **Advisor Ghrim:** Debes completar todas las tareas en un conjunto de una dificultad particular, luego podrás reclamar tu recompensa.
        - **Advisor Ghrim:** Algunas de las tareas del conjunto Fremennik son simples, algunas requerirán cierto skill levels y otras pueden requerir que se inicien o completen misiones.
        - **Advisor Ghrim:** Para reclamar las recompensas del conjunto Fremennik, habla con council workman en el puente al sur de Rellekka, Yrsa en Rellekka o conmigo mismo.
        - (Action: anterior2)
      - [Choice]: Lo siento, me estaba yendo.
        - (end)
  - [Choice]: ¿Puedo comprar un repuesto de la recompensa?
    - [Menu]: Elige una opción:
      - [Choice]: Fremennik sea boots 1
        - **Advisor Ghrim:** Fremennik sea boots 1? Sí, pero me temo que te costaría 1.500 coins.
        - [Menu]: ¿Comprar otro por 1.500 coins?
          - [Choice]: si
            - {{tbox|pic=Fremennik sea boots 1 detail.png|You're handed another Fremennik sea boots 1.}}
            - (receives=Fremennik sea boots 1) (removes= 1,500 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Fremennik sea boots 2
        - **Advisor Ghrim:** Fremennik sea boots 2? Sí, pero me temo que te costaría 2500 coins.
        - [Menu]: ¿Comprar otro por 2500 coins?
          - [Choice]: si
            - {{tbox|pic=Fremennik sea boots 2 detail.png|You're handed another Fremennik sea boots 2.}}
            - (receives=Fremennik sea boots 2) (removes= 2,500 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Fremennik sea boots 3
        - **Advisor Ghrim:** Fremennik sea boots 3? Sí, pero me temo que te costaría 7.500 coins.
        - [Menu]: ¿Comprar otro por 7.500 coins?
          - [Choice]: si
            - {{tbox|pic=Fremennik sea boots 3 detail.png|You're handed another Fremennik sea boots 3.}}
            - (receives=Fremennik sea boots 3) (removes= 7,500 coins)
          - [Choice]: No
            - **Player:** No, gracias.
      - [Choice]: Fremennik sea boots 4
        - **Advisor Ghrim:** Fremennik sea boots 4? Sí, pero me temo que te costaría 15.000 coins.
        - [Menu]: ¿Comprar otro por 15.000 coins?
          - [Choice]: si
            - {{tbox|pic=Fremennik sea boots 4 detail.png|You're handed another Fremennik sea boots 4.}}
            - (receives=Fremennik sea boots 4) (removes= 15,000 coins)
          - [Choice]: No
            - **Player:** No, gracias.
  - [Choice]: Lo siento, me estaba yendo.
    - (end)

#### Usando paquetes planos en Ghrim (requires the hard Fremennik achievements)

- **Advisor Ghrim:** ¡Ah, justo lo que necesitamos! Siempre podemos utilizar el nuevo furniture. Los pondré en las arcas ahora, si quieres.
- [Menu]: ¿Cuántos te gustaría donar?
  - [Choice]: Donar-1.
    - **Advisor Ghrim:** Por 1 de esos, pondré [número] coins en las arcas. ¿Es eso aceptable?
    - {{anchor|flatpack}} [Menú]: seleccione una opción
      - [Choice]: Sí.
        - (removes=flatpack(s))
      - [Choice]: No.
        - (end)
  - [Choice]: Donar-5.
    - **Advisor Ghrim:** Por 5 de ellos, pondré [número] coins en las arcas. ¿Es eso aceptable?
    - (Action: continuar|paquete plano)
  - [Choice]: Donar todo.
    - **Advisor Ghrim:** Para [número] de esos, pondré [número] coins en las arcas. ¿Es eso aceptable?
    - (Action: continuar|paquete plano)
  - [Choice]: Donar-X.
    - {{tinput|Enter amount:}}
    - (Action: (Después de ingresar una cantidad positiva:))
      - **Advisor Ghrim:** Para [número] de esos, pondré [número] coins en las arcas. ¿Es eso aceptable?
      - (Action: continuar|paquete plano)
    - (Condition: Si se ingresa cero:)
      - **Advisor Ghrim:** Por 0 de ellos, pondré 0 coins en las arcas. ¿Es eso aceptable?
      - (Action: continuar|paquete plano)
