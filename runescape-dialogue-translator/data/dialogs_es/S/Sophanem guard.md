# Sophanem guard

- **Original Wiki Page**: [Transcript:Sophanem guard](https://runescape.wiki/w/Transcript%3ASophanem%20guard)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Sophanem guard (masculino/femenino):** ¿Cómo puedo ayudarte?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué estás haciendo aquí abajo?
    - **Player:** ¿Qué estás haciendo aquí abajo?
    - **Sophanem guard (hombre/mujer):** Estamos vigilando este lugar para asegurarnos de que nada salga por esa trampilla y que nadie baje allí innecesariamente.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué hay ahí abajo?{{anchor|whats-down}}
        - **Player:** ¿Qué hay ahí abajo?
        - **Sophanem guard (masculino):** ¡Las criaturas más desagradables que puedas imaginar!
        - **Sophanem guard (mujer):** Parecen ser un cruce entre humanos y escarabajos.
        - **Sophanem guard (masculino):** ¡Se rumorea que pueden estar conectados con la antigua Secta de Scabaras!
        - **Player:** ¿Qué sabes sobre esta secta?
        - **Sophanem guard (mujer):** Poco, aparte de algún que otro cuento de hadas de la infancia.
      - [Choice]: ¿Por qué impiden que la gente baje allí?{{anchor|why-stop}}
        - **Player:** ¿Por qué impiden que la gente baje allí?
        - **Sophanem guard (masculino):** Han muerto demasiadas personas allí como para que no tomemos medidas.
        - **Sophanem guard (mujer):** Hay trampas diabólicas y espantosos monstruos escarabajos ahí abajo.
        - **Sophanem guard (masculino):** Cuando nos enviaron aquí por primera vez, echamos un vistazo allí y apenas escapamos con vida.
        - **Player:** Dios, eso suena bastante aterrador. Podría investigar este lugar en el futuro.
        - **Sophanem guard (masculino):** Lamento ser grosero, pero realmente necesitamos volver a vigilar la puerta. Los escarabajos podrían regresar en cualquier momento.
  - [Choice]: ¿Tienes un yesquero?
    - **Player:** ¿Tienes un yesquero?
    - **Sophanem guard (hombre/mujer):** Sí, pero me gustaría conservarlo por ahora.
    - **Player:** Está bien; Tengo uno conmigo de todos modos.
  - [Choice]: ¿Tienes una antorcha?
    - **Player:** ¿Tienes una linterna?
    - **Sophanem guard (hombre/mujer):** Te venderé una antorcha apagada por 200 po.
    - [Menu]: Selecciona una opción
      - [Choice]: Yo lo tomaré.
        - **Player:** Lo aceptaré.
        - (Condition: If the player has no inventory space:)
          - **Player:** Dios mío; Parece que no tengo suficiente espacio en mis bolsos para llevarlo. Vuelvo enseguida.
          - **Sophanem guard (hombre/mujer):** Estaré aquí cuando regreses.
        - (Condition: If the player has less than 200 coins:)
          - No puedes permitirte eso.
          - **Player:** No tengo suficiente dinero encima. Volveré cuando tenga suficiente.
        - (Condition: If the player has 200 coins:)
          - (removes=200 coins)
          - (receives=unlit torch)
          - [El guardia te entrega una antorcha apagada a cambio de 200 po.]
      - [Choice]: Lo siento, eso es demasiado caro.
        - **Player:** Lo siento, es demasiado caro.
        - **Sophanem guard (hombre/mujer):** No hay problema; Vuelve si cambias de opinión.
  - [Choice]: ¿Cómo es que no tienes manchas?
    - **Player:** ¿Cómo es que no tienes manchas?
    - **Sophanem guard (masculino/femenino):** Ay, la plaga de manchas. Bueno, yo no estaba aquí cuando ocurrió el brote.
    - **Sophanem guard (hombre/mujer):** Estábamos fuera de la ciudad tratando de atrapar a un ladrón de antigüedades llamado Simon Templeton.
    - **Player:** ¿No tienes miedo de que la plaga sea contagiosa?
    - **Sophanem guard (masculino/femenino):** Sophanem es mi ciudad natal, por lo que se necesitaría mucho más que la amenaza de unos pocos lugares para mantenerme alejado.
  - [Choice]: ¿Qué es este lugar?
    - **Player:** ¿Qué es este lugar?
    - (Condition: Before Contact!)
      - **Sophanem guard (masculino/femenino):** Estos son los restos del Banco Sophanem.
      - **Player:** ¿Qué pasó con este lugar? Está todo destrozado...
      - **Sophanem guard (masculino/femenino):** Hace algún tiempo, estas criaturas escarabajos comenzaron a aparecer desde el sótano. Luchamos contra ellos, pero siguieron viniendo y viniendo y finalmente destruyeron el lugar. Ahora los hemos defendido de nuevo y hemos bloqueado la trampilla.
    - (Condition: After Contact!)
      - **Sophanem guard (masculino/femenino):** Este es el banco Sophanem recientemente renovado.
      - **Player:** Vaya, este lugar está todo arreglado.
      - **Sophanem guard (hombre/mujer):** Una vez que toda la gente del pueblo regresó, decidimos arreglar el lugar y devolverlo a la normalidad.
      - **Player:** ¿No tienes miedo de que los escarabajos vuelvan?
      - **Sophanem guard (hombre/mujer):** Supongo que es una preocupación, pero desde que la gente del pueblo regresó, los ataques de escarabajos se han vuelto más esporádicos y mucho menos organizados.
      - **Player:** Es cierto. También hay muchos aventureros pasando por la mazmorra ahora, lo que también tiene un efecto.
      - **Sophanem guard (hombre/mujer):** Eso debe estar reduciendo el número de escarabajos.

### Attempting to climb down the trapdoor


#### ¡Antes y durante el Contacto!

- **Sophanem guard (mujer):** ¡Alto! ¡No puedes bajar allí!
- **Player:** ¿Por qué no?
- **Sophanem guard (masculino):** ¡Estamos vigilando la trampilla, asegurándonos de que nada suba ni baje!
- **Sophanem guard (mujer):** Además, tal como lo hemos configurado, ¡dudo que puedas abrir esa trampilla!
- **Player:** ¿En serio? Me gustaría intentarlo.
- Intentas abrir la trampilla pero fallas.
- **Sophanem guard (hombre):** Si realmente quieres ir allí, deberías hablar primero con Jex.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué hay ahí abajo?
    - (above|whats-down)
  - [Choice]: ¿Por qué impiden que la gente baje allí?
    - (above|why-stop)
  - [Choice]: Gracias.
    - **Player:** Gracias.

#### ¡Después del contacto!

- **Sophanem guard (mujer):** ¡Ten cuidado ahí abajo!
- Entras por la trampilla una vez más.
- (Action: el player entra al nivel del laberinto de la mazmorra.)
