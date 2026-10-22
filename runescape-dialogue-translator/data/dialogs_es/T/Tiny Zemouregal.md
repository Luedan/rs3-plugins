# Tiny Zemouregal

- **Original Wiki Page**: [Transcript:Tiny Zemouregal](https://runescape.wiki/w/Transcript%3ATiny%20Zemouregal)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In New Varrock


#### Diálogo por primera vez, o haber perdido el libro o el amuleto de lengua gatuna.

- (receives=pocket book)
- **Tiny Zemouregal:** ¡TOMA EL LIBRO!<BR>¡HAZLO!
- [Tiny Zemouregal le ha regalado un libro de bolsillo.<br>Léalo para obtener información sobre las nuevas tareas y recompensas de Varrock.]
- (receives=catspeak amulet)
- **Tiny Zemouregal:** ¡TOMA A KITTY TALKER!<BR>SHOO ¡GATITOS!
- [Tiny Zemouregal te ha regalado un amuleto de lengua de gato.]
- (continue|Standard dialogue)

#### Diálogo estándar

- **Player:** ¿Qué es este libro tuyo?
- **Tiny Zemouregal:** ¡TAREAS DE ZEMO! <BR>Y ¡TU HACES!
- **Player:** ¿Estas son tus tareas?<br>¿Y quieres que las haga?<br>¿Por qué debería ayudarte?
- **Tiny Zemouregal:** ¡DAR MARCAS!
- **Player:** Me pagarás para que haga tus tareas por ti.
- **Tiny Zemouregal:** ¡SÍ!<BR>YES!<BR>YTÚ LO HACES!<BR>
- **Player:** Tengo algunas preguntas para ti...
- [Menu]: Elige una opción:
  - [Choice]: ¿Cuáles son estas tareas?
    - **Tiny Zemouregal:** ¡GRAN ZEMO, HAZLO!
    - **Tiny Zemouregal:** ¡LIMPIA Y ORDENADA!<BR>SPY Y EXTORSIONA!
    - **Tiny Zemouregal:** ¡TODOS ODIAN AL PEQUEÑO ZEMO! ¡<BR>NO ES MI CULPA!
    - **Player:** ¿Te obliga a hacer el trabajo sucio?
    - **Tiny Zemouregal:** ¡SÍ!
    - (initial)
  - [Choice]: ¿Hay alguna recompensa?
    - **Tiny Zemouregal:** ¡MARCAS!<BR>¡CADA TAREAS!
    - **Player:** Por cada tarea que hago, ¿me darás zemomarks?
    - **Tiny Zemouregal:** ¡MÁS MARCAS CADA FINALIZACIÓN!
    - **Player:** ¿Y cada vez que termine las misiones en este lugar, obtendré más zemomarks?
    - **Tiny Zemouregal:** ¡NUEVAS MEJORAS DE ARMADURA VARROCK!
    - **Player:** Ah, ¿y mejoras a mi armadura Varrock? ¿Qué, como una mejora por cada nivel de dificultad que complete?
    - **Tiny Zemouregal:** ¡SÍ!<BR>YES!<BR>YES!
    - **Tiny Zemouregal:** ¡FÁCIL OFRECE UNA MEJOR MINERÍA!
    - **Tiny Zemouregal:** ¡EL MEDIO DA MEJOR FUNDCIÓN!
    - **Tiny Zemouregal:** ¡DIFÍCIL DA MEJOR HERRERÍA!
    - **Tiny Zemouregal:** ¡ELITE HACE TRABAJO EN TODOS LOS HORNOS!
    - **Player:** ¿Algo más?
    - (Condition: If on a first-time playthrough:)
      - **Tiny Zemouregal:** ¡PREGUNTA MÁS TARDE!
      - (initial)
    - (Condition: If on a replay:)
      - **Tiny Zemouregal:** ¡COMPRAR LÁMPARA!<BR>¡ACTUALIZACIÓN DE LÁMPARA!
      - **Player:** ¿Te refieres a la lámpara de la tienda de recompensas de Aris? ¿Se hace más grande cada vez que completo un nivel de dificultad?
      - **Tiny Zemouregal:** ¡LÁMPARA PEQUEÑA PARA TODO FÁCIL!
      - **Tiny Zemouregal:** ¡ENTONCES MEDIO PARA TODO MEDIO!
      - **Tiny Zemouregal:** ¡ENTONCES GRANDE PARA TODO DURO!
      - **Tiny Zemouregal:** ¡ENTONCES ENORME PARA TODA LA ÉLITE!
      - **Player:** Así que tengo que completar niveles de tus tareas para poder obtener la actualización.
      - **Tiny Zemouregal:** ¡SÍ!
      - (initial)
  - [Choice]: ¿Qué eres?
    - {{anchor|ARGH}}**Tiny Zemouregal:** ¡ARGH!
    - **Player:** ¿Qué es?
    - **Tiny Zemouregal:** ¡ARGH!
    - **Player:** ¿Qué?
    - **Tiny Zemouregal:** ...
    - Tiny Zemouregal te está mirando sin parpadear. <br>Es más que un poco desconcertante.
    - **Player:** ¿Por qué me miras así?
    - **Tiny Zemouregal:** ¡ARGH!
    - **Player:** No importa.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Cuáles son estas tareas?
        - (arriba)
      - [Choice]: ¿Hay alguna recompensa?
        - (arriba)
      - [Choice]: ¿Qué eres?
        - (arriba)
      - [Choice]: No, en serio, ¿qué eres?
        - **Tiny Zemouregal:** ¡ARGH!
        - **Tiny Zemouregal:** ...
        - **Player:** Olvida que pregunté.
        - **Tiny Zemouregal:** ¡PEQUEÑO ZEMO!
        - **Tiny Zemouregal:** ¡O SIMPLEMENTE PEQUEÑO PARA BREVE!
        - **Player:** Ya lo entendí, pero ¿de dónde vienes y qué haces aquí?
        - **Tiny Zemouregal:** ¡GRAN ZEMO HACE PARA LAS TAREAS!
        - **Player:** ¿Te convirtió en un siervo para que le hicieras las tareas del hogar?
        - **Tiny Zemouregal:** ¡SÍ! <BR>¡TAMBIÉN MASCOTA!
        - **Player:** ¿Y me pides que haga tus tareas por ti?
        - **Tiny Zemouregal:** ¡SÍ!<BR>LAZY!
        - **Tiny Zemouregal:** ¡Tú lo haces! <BR>¡OBTENGA MARCAS!
        - **Player:** ¿No lo descubrirá 'Big Zemo'?
        - **Tiny Zemouregal:** ¡NO! ¡LO ODIO! <BR>...<BR> ¿SER AMIGO?
        - (initial)
      - [Choice]: No importa.
        - (abajo)
  - [Choice]: cond=Having lost the catspeak amulet, and having completed Mummy Returns|Necesito poder hablar con los gatos.
    - {{anchor|CATS}}(receives=catspeak amulet)
    - **Tiny Zemouregal:**¡LLEVA KITTY TALKER!<BR>¡DIVIÉRTETE!
    - [Tiny Zemouregal te ha regalado un amuleto de lengua de gato.]
    - (initial)
  - [Choice]: No importa.
    - {{anchor|ARGH!}}**Tiny Zemouregal:** ¡ARGH!
    - **Player:** ¡ARGH!
    - **Tiny Zemouregal:** ¡ARGH!
    - **Player:** ¡ARGH!
    - **Tiny Zemouregal:** ...
    - **Player:** No importa.

#### Diálogo aéreo

- {{trandom}}
  - **Tiny Zemouregal:** {{RSChat|OVER HERE!}}
  - **Tiny Zemouregal:** {{RSChat|NEED HELP!}}
  - **Tiny Zemouregal:** {{RSChat|HATE BIG ZEMO!}}
  - **Tiny Zemouregal:** {{RSChat|HATE CHORES!}}
  - **Tiny Zemouregal:** {{RSChat|I AM AWESOME!}}
  - **Tiny Zemouregal:** {{RSChat|GIMME BREW!}}

#### Usar cualquier artículo para Tiny Zemouregal (excepto el libro de bolsillo, el amuleto Catspeak y la cerveza Zemouregal)

- **Tiny Zemouregal:** ¡NO TIENE HAMBRE!

#### Usando el libro de bolsillo en Tiny Zemouregal

- **Tiny Zemouregal:** ¡Sigue! <BR>Y ¡LO HACES!
- **Tiny Zemouregal:** ¡LEER LIBRO!<BR>DO ¡TAREAS!

#### Usando el amuleto Catspeak en Tiny Zemouregal

- **Tiny Zemouregal:**¡Sigue! <BR> ¡GATITO SUSURRADOR!

#### Micro Brew: uso de Zemouregal Brew en Tiny Zemouregal

- **Tiny Zemouregal:** ¡OOH!<BR>GIMME ¡DAME DAME!
- (removes=Zemouregal brew)
- **Tiny Zemouregal:** {{RSChat|* hic *}}
- **Tiny Zemouregal:** ¡MMM, DELICIOSO!
- (Condition: If 'Micro Brew' hasn't been completed yet.)
  - {{RSFontAchievement|Micro Brew}}
- (continuea|Standard dialogue)

#### Banco-Z

- **Tiny Zemouregal:** JAJAJA!<BR>¡BUEN TRABAJO!
- **Tiny Zemouregal:** ¡GRAN CARA DE ESTÚPIDO DE ZEMO!

#### Al completar las tareas fáciles de New Varrock

- {{RSFontAchievement|New Varrock Set Tasks - Easy}}
- [¡Has completado todas las tareas de Simpleton! Habla con Tiny Zemouregal en el nuevo cuadrado Varrock para recibir tu recompensa.]

#### Reclamar las recompensas de la tarea fácil

- **Tiny Zemouregal:** ¡HE HECHO TODAS LAS TAREAS SIMPLES!
- **Tiny Zemouregal:** ACTUALIZO TU ARMADURA VARROCK - ¡ROPA OPCIONAL!
- [Has desbloqueado una mejora para la armadura Varrock. Ya no es necesario que lo uses para obtener los beneficios de Mining y Smithing.]
- (continuea|Standard dialogue)

#### Al completar las tareas medianas nuevas de Varrock

- {{RSFontAchievement|New Varrock Set Tasks - Medium}}
- [¡Has completado todas las tareas de Minion! Habla con Tiny Zemouregal en el nuevo cuadrado Varrock para recibir tu recompensa.]

#### Reclamar las recompensas de la tarea media

- **Tiny Zemouregal:** ¡HE HECHO TODAS LAS TAREAS DE LOS MINIONS!
- **Tiny Zemouregal:** ACTUALIZO TU ARMADURA VARROCK - ¡MÍA MÁS!
- [Has desbloqueado una mejora para la armadura Varrock que duplica tus posibilidades de extraer mineral adicional.]
- (continuea|Standard dialogue)

#### Al completar las nuevas tareas difíciles de Varrock

- {{RSFontAchievement|New Varrock Set Tasks - Hard}}
- [¡Has completado todas las tareas de Halfwit! Habla con Tiny Zemouregal en el nuevo cuadrado Varrock para recibir tu recompensa.]

#### Reclamar las recompensas de la tarea difícil

- **Tiny Zemouregal:** ¡HICISTE TODAS LAS TAREAS MEDIAS!
- **Tiny Zemouregal:** ACTUALIZÉ TU ARMADURA VARROCK - ¡OLÍA MÁS!
- [Has desbloqueado una mejora para la armadura Varrock que duplica tus posibilidades de duplicar la fundición.]
- (continuea|Standard dialogue)

#### Al completar las tareas Elite New Varrock

- {{RSFontAchievement|New Varrock Set Tasks - Elite}}
- [¡Has completado todas las tareas de Lackey! Habla con Tiny Zemouregal en el nuevo cuadrado Varrock para recibir tu recompensa.]

#### Reclamar las recompensas de la tarea Elite

- **Tiny Zemouregal:** ¡HICISTE TODAS LAS TAREAS DE LACA!
- **Tiny Zemouregal:** ACTUALIZO TU ARMADURA VARROCK - ¡SMITH MÁS!
- [Has desbloqueado una mejora para la armadura Varrock que duplica tus posibilidades de lograr el doble de progreso al forjar.]
- (continue|After completing all New Varrock tasks)

#### Después de completar todas las tareas nuevas de Varrock

- **Tiny Zemouregal:** ¡ME AYUDAS MUCHO!
- **Tiny Zemouregal:** ¡PEQUEÑO ZEMO TU AMIGO!
- [Menu]: Elige una opción:
  - [Choice]: Recuérdame las recompensas que he ganado.
    - **Tiny Zemouregal:** ¡MARCAS! <BR>¡CADA TAREAS!
    - **Player:** ¿Me diste zemomarks por cada tarea que hice?
    - **Tiny Zemouregal:** ¡MÁS MARCAS CADA FINALIZACIÓN!
    - **Player:** ¿Y cada vez que termine las misiones en este lugar, obtendré más zemomarks?
    - **Tiny Zemouregal:** ¡NUEVAS MEJORAS DE ARMADURA VARROCK!
    - **Player:** ¿Y he desbloqueado mejoras para mi armadura Varrock?
    - **Tiny Zemouregal:** ¡SÍ!<BR>YES!<BR>YES!
    - **Tiny Zemouregal:** ¡FÁCIL OFRECE UNA MEJOR MINERÍA!
    - **Tiny Zemouregal:** ¡EL MEDIO DA MEJOR FUNDCIÓN!
    - **Tiny Zemouregal:** ¡DIFÍCIL DA MEJOR HERRERÍA!
    - **Tiny Zemouregal:** ¡ELITE HACE TRABAJO EN TODOS LOS HORNOS!
    - **Player:** ¿Algo más?
    - **Tiny Zemouregal:** ¡COMPRAR LÁMPARA!<BR>¡ACTUALIZACIÓN DE LÁMPARA!
    - **Player:** ¿Te refieres a la lámpara de la tienda de recompensas de Aris? ¿Se hace más grande cada vez que completo un nivel de dificultad?
    - **Tiny Zemouregal:** ¡LÁMPARA PEQUEÑA PARA TODO FÁCIL!
    - **Tiny Zemouregal:** ¡ENTONCES MEDIO PARA TODO MEDIO!
    - **Tiny Zemouregal:** ¡ENTONCES GRANDE PARA TODO DURO!
    - **Tiny Zemouregal:** ¡ENTONCES ENORME PARA TODA LA ÉLITE!
    - **Player:** Así que ahora puedo comprarle una lámpara enorme a Aris cuando complete mi misión.
    - **Tiny Zemouregal:** ¡SÍ!
    - (initial)
  - [Choice]: ¿Qué eres?
    - (above|ARGH)
  - [Choice]: Necesito poder hablar con los gatos.
    - (above|CATS)
  - [Choice]: No importa.
    - (above|ARGH!)
