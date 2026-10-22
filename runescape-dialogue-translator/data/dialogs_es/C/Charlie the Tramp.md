# Charlie the Tramp

- **Original Wiki Page**: [Transcript:Charlie the Tramp](https://runescape.wiki/w/Transcript%3ACharlie%20the%20Tramp)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Varrock


#### Diálogo estándar

- **Charlie the Tramp:** ¿Te ahorra algo de cambio, jefe?
- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Charlie the Tramp:** Carlos. Charles E. Trampin' a su servicio. Ahora, sobre ese cambio que me ibas a dar...
    - (initial)
  - [Choice]: ¿Qué gano yo con esto?
    - **Charlie the Tramp:** '¿Qué gano yo con esto?' ¿Qué pasó con la caridad? ¿No tienes consideración por los menos afortunados que tú?
    - (initial)
  - [Choice]: *(Solo antes de Shield of Arrav)* Lo siento, no tengo dinero.
    - **Charlie the Tramp:** Gracias de todos modos.
    - (initial)
  - [Choice]: *(Solo después de Shield of Arrav)* ¿Sabes dónde puedo encontrar el escondite de Black Arm Gang?
    - **Charlie the Tramp:** Poca memoria, ¿eh?
    - **Charlie the Tramp:** La despiadada y notoria Black Arm Gang tiene su cuartel general en el callejón al oeste de nosotros. Habla con una señora llamada Katrine. Pero no la molestes y no le digas que yo te envié. Ella es bastante peligrosa.
    - (initial)
  - [Choice]: *(Sólo después de Escudo de Arrav)* Estoy buscando el escondite de la pandilla Phoenix.
    - **Charlie the Tramp:** Sí, escuché que hablaste con Baraek. Es fácil perderse en las calles de Varrock. Ahora escucha atentamente...
    - **Charlie the Tramp:** Para llegar al escondite de Phoenix, camina hacia el este desde aquí. Es la calle que tiene el Blue Moon Inn en la esquina.
    - **Charlie the Tramp:** Toma el primer callejón que sale de la carretera hacia el sur y encontrarás el escondite al final de ese callejón. Se llama corporación VTAM.
    - **Player:** VTAM. Entiendo.
    - (initial)
  - [Choice]: ¡Consigue un trabajo!
    - **Charlie the Tramp:** ¿Estás empezando? ¡Espero que se te caiga la nariz!

#### Diálogo histórico previo al 13 de febrero de 2017

- **Charlie the Tramp:** ¿Te ahorra algo de cambio, jefe?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - (arriba)
  - [Choice]: Lo siento, no tengo ninguno.
    - (arriba)
  - [Choice]: ¡Ve a buscar trabajo!
    - (arriba)
  - [Choice]: Bien, aquí tienes.
    - (Condition: If the player has coins in their money pouch:)
      - (removes=1 coin)
      - **Charlie the Tramp:** ¡Oye, muchas gracias!
      - [Menu]: Selecciona una opción
        - [Choice]: No hay problema.
          - **Player:** No hay problema.
        - [Choice]: ¿No recibo algún tipo de pista de misión o algo así ahora?
          - **Player:** ¿No recibo algún tipo de pista de misión o algo así ahora?
          - **Charlie the Tramp:** ¿Eh? ¿Qué quieres decir? No fue por eso que te pedí dinero.
          - **Charlie the Tramp:** Sólo necesito comer...
    - (Condition: If the player does not have coins in their money pouch:)
      - **Player:** Oh, espera. No tengo ninguno, lo siento.
      - **Charlie the Tramp:** Gracias de todos modos.
  - [Choice]: ¿Hay algo en este callejón?
    - **Player:** ¿Hay algo en este callejón?
    - **Charlie the Tramp:** La despiadada y notoria banda criminal conocida como Black Arm Gang tiene su cuartel general allí.
    - [Menu]: Selecciona una opción
      - [Choice]: ¡Gracias por la advertencia!
        - **Player:** ¡Gracias por la advertencia!
        - **Charlie the Tramp:** No te preocupes por eso.
        - (continue|join)
      - [Choice]: ¿Crees que me dejarían unirme?
        - **Player:{{anchor|join}}** ¿Crees que me dejarían unirme?
        - (Condition: If the player has not yet joined either gang:)
          - **Charlie the Tramp:** Nunca se sabe. Encontrarás a una señora allí llamada Katrine. Habla con ella.
          - **Charlie the Tramp:** Pero no la molestes, es bastante peligrosa.
        - (Condition: If the player has joined the Black Arm Gang:)
          - **Charlie the Tramp:** Tenía la impresión de que ya eras miembro...
        - (Condition: If the player has joined the Phoenix Gang:)
          - **Charlie the Tramp:** No. Eres colaborador de la pandilla Phoenix. No hay forma de que te dejen unirte ahora.
          - [Menu]: Selecciona una opción
            - [Choice]: ¿Cómo supiste que estaba en la pandilla Phoenix?
              - **Player:** ¿Cómo supiste que estaba en la pandilla Phoenix?
              - **Charlie the Tramp:** En mi profesión actual paso mucho tiempo en la calle y a veces escuchas este tipo de cosas.
              - **Player:{{anchor|getin}}** ¿Alguna idea de cómo podría entrar allí entonces?
              - **Charlie the Tramp:** Mmmm. No se.
              - **Charlie the Tramp:** Tu mejor opción probablemente sería encontrar a alguien más... Alguien que NO sea miembro de la pandilla Phoenix, y lograr que se infiltre en las filas de Black Arm Gang por ti.
              - **Charlie the Tramp:** Si encuentras a alguien así, dile que venga a verme primero.
              - [Menu]: Selecciona una opción
                - [Choice]: Bien. ¡Buen plan!
                  - **Player:** Vale. ¡Buen plan!
                  - **Charlie the Tramp:** ¡No soy sólo una cara bonita!
                - [Choice]: ¿Como quién?
                  - **Player:** ¿Como quién?
                  - **Charlie the Tramp:** Hay muchos otros aventureros además de ti. Estoy seguro de que si le preguntaras amablemente a alguno de ellos, te ayudarían.
            - [Choice]: ¿Alguna idea de cómo podría entrar allí entonces?
              - (continuea|getin)

### In New Varrock

- **Charlie the Tramp:** ¿Te ahorras un zemomark, jefe?
- [Menu]: Elige una opción:
  - [Choice]: Aquí tienes un par de zemomarcas.
    - (Condition: If the player does not have enough zemomarks:)
      - **Player:** Oh, en realidad, no tengo tanto.
      - **Charlie the Tramp:** Es difícil saber cuál de nosotros es el vagabundo.
      - (initial)
    - (Condition: If the player has enough zemomarks:)
      - (removes=two zemomarks)
      - [Le das a Charlie 2 zemomarks.]
      - **Charlie the Tramp:** ¡Salud, jefe!
  - [Choice]: Lo siento, no tengo ninguno.
    - **Charlie the Tramp:** Me rompes el corazón de vagabundo zombi.
  - [Choice]: ¡Consigue un trabajo!
    - **Charlie the Tramp:** ¡Espero que se te caiga la nariz! <br>Entonces tendría algo para mordisquear.
