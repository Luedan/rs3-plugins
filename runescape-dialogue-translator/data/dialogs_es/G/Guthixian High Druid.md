# Guthixian High Druid

- **Original Wiki Page**: [Transcript:Guthixian High Druid](https://runescape.wiki/w/Transcript%3AGuthixian%20High%20Druid)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Guthixian High Druid:** Bienvenido. ¿En qué puedo ayudarte?
- **ELIGE UNA OPCIÓN:**
  - ¿Qué hay que hacer aquí?
    - *Si el player no ha completado todas las actividades en la cámara principal:*
      - **Guthixian High Druid:** El santuario es un lugar de duelo. Hay actividades que puede realizar para presentar sus respetos, que pueden resultarle gratificantes. También nos vendría bien tu ayuda en caso de una amenaza desde la cámara principal.
    - *Si el player ha completado todas las actividades en la cámara principal:*
      - **Guthixian High Druid:** Has presentado tus respetos aquí. No necesitas hacer más. Por supuesto, aún nos vendría bien tu ayuda ante una amenaza desde la cámara principal.
    - **SELECCIONA UNA OPCIÓN:**
      - *Si el player no ha encendido las cinco antorchas:*
        - {{Transcript missing}}
      - *Si el player no ha presentado sus respetos al monumento:*
        - ¿Qué puedo hacer para presentar mis respetos?
          - **Guthixian High Druid:** Te agradecemos que hayas encendido las antorchas. También hemos construido un monumento a Guthix. Quizás le resulte beneficioso contemplar su paso por allí.
      - ¿Qué está pasando en la cámara principal?
        - **Guthixian High Druid:** Hay una gran cantidad de autómatas sueltos en la cámara. Desde la muerte de Cres, se han vuelto cada vez más inestables.
        - **Guthixian High Druid:** Es triste decirlo, sin su maestro se vuelven contra cualquiera que entre.
        - **Guthixian High Druid:** Si se siente con ganas, nos vendría bien su ayuda para reducir su número. Después de todo, debemos preservar la santidad del santuario.
        - (continue|ask)
      - ¿Crees que Guthix aprobaría este santuario?
        - **Guthixian High Druid:** Lo importante aquí es aprender de los eventos que sucedieron.
        - **Guthixian High Druid:** Con el conocimiento que tenemos ahora, estamos tratando de evitar reverenciar a Guthix como un dios poderoso, pero siempre habrá quienes lo alabarán de esta manera.
        - **Guthixian High Druid:** Aquí en el santuario, tenemos el mayor respeto por Guthix. En honor a sus últimas palabras, sólo intentamos continuar con nuestra creencia en el equilibrio y en lo que enseñó Guthix, en lugar del propio Guthix.
        - **Guthixian High Druid:** No podemos ignorar la importancia de los hechos ocurridos aquí, y este espacio nos brinda un ambiente para reflexionar sobre ellos.
        - (continue|ask)
  - ¿Puedes teletransportarme a la cámara principal?
    - *Si el player no cumple con los requisitos para las recompensas adicionales:*
      - **Guthixian High Druid:** Lamentablemente, no creo que tengas suficiente experiencia para enfrentar esta amenaza en este momento.
      - **Guthixian High Druid:** Por favor, entrena más y vuelve. Necesitamos mucho su ayuda.
      - **{{anchor|ask}}SELECCIONA UNA OPCIÓN**
        - Pregunta por otra cosa.
          - (initial|initial-options)
        - Eso es todo, gracias.
          - (end)
    - *Si el player cumple con los requisitos para las recompensas adicionales:*
      - (Action: El Guthixian High Druid lanza un hechizo sobre el player, quien es teletransportado a la cámara principal.)
  - *Si el player todavía tiene el regalo de Azzanadra/Juna/Zilyana:*
    - Me gustaría cambiar mi top.
      - **Guthixian High Druid:** Si realmente has cambiado de opinión, te proporcionaré una alternativa. ¿Cuál te gustaría?
      - *(Se muestran todas las opciones excepto el regalo que posee el player :)*
        - **ELIGE UNA OPCIÓN:**
          - El regalo de Azzanadra
            - (continue)
          - El regalo de Juna
            - (continue)
          - El regalo de Zilyana
            - (continue)
      - (removes=current gift) (receives=chosen gift)
      - **Guthixian High Druid:** Como desees.
      - (continuea|ask)
  - *Si el player ha perdido el regalo de Azzanadra/Juna/Zilyana:*
    - He perdido algunas de mis recompensas.
      - **¿QUÉ TE GUSTARÍA RECUPERAR?**
        - Lámparas antiguas
          - Recibes una lámpara antigua.
        - Circuito Sexta Edad{{Sic}}
          - Recibes un circuito de la Sexta Edad {{Sic}}.
        - Lámparas estáticas
          - {{Transcript missing}}
        - Lámpara pálida
          - Recibes una lámpara pálida.
        - Lámpara brillante
          - Recibirás una lámpara brillante.
        - El regalo de [Azzanadra/Juna/Zilyana]
          - (receives=gift)
          - Recibes el regalo de [Azzanadra/Juna/Zilyana].
      - **Guthixian High Druid:** Parece que tienes todo lo que necesitas.
      - (initial|initial-options)
  - *Si el player no ha reclamado las recompensas adicionales:*
    - ¿Soy elegible para recibir más recompensas todavía?
      - *Si el player no es elegible para reclamar recompensas adicionales:*
        - **Guthixian High Druid:** Me temo que aún no eres lo suficientemente fuerte como para obtener la bendición completa de Guthix. Ten esperanza, aventurero.
        - (continuea|ask)
      - *Si el player es elegible para reclamar recompensas adicionales:*
        - El Guthixian High-Druid{{Sic}} te entrega un Circuito de la Sexta Edad{{Sic}}.
        - {{Transcript missing}}

### Claim rewards option

- *Si el player tiene recompensas para reclamar:*
  - (above|reclaim-rewards)
- *Si el player no tiene recompensas para reclamar:*
  - **Guthixian High Druid:** Parece que tienes todo lo que necesitas.
  - (initial|initial-options)

### Teleport option

- *Si el player no cumple con los requisitos para las recompensas adicionales:*
  - (above|teleport-fail)
- *Si el player cumple con los requisitos para las recompensas adicionales:*
  - **EL RESTO DE CÁMARAS SON PELIGROSAS. ¿ESTÁS SEGURO QUE DESEAS ENTRAR?**
    - si
      - (Action: El Guthixian High Druid lanza un hechizo sobre el player, quien es teletransportado a la cámara principal.)
    - En realidad, no...
      - (end)

### Reminisce option

- **¿QUÉ MEMORIA TE GUSTARÍA VER?**
  - Reunión Cres
    - (Action: Reproduce la escena.)
  - Zilyana enfrentándose a Cres
    - (Action: Reproduce la escena.)
  - Sliske dando su golpe final
    - (Action: Reproduce la escena.)
  - El regreso de Saradomin
    - (Action: Reproduce la escena.)
  - no quiero ver un recuerdo
    - (end)
