# Bert

- **Original Wiki Page**: [Transcript:Bert](https://runescape.wiki/w/Transcript%3ABert)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### Después de La mano en la arena


##### Diálogo por primera vez

- **Player:** ¡Bert! ¡Albricias!
- **Bert:** Arrr... Las buenas noticias siempre están a mano.
- **Player:** ¡Arrestaron a Sandy por el asesinato del mago y el pozo de arena ahora se vuelve a llenar solo!
- **Bert:** ¡YO TRABAJO! ¡HE PERDIDO EL TRABAJO! ¿Cómo puedes decir que son buenas noticias? ¡Mi esposa me arrancará miembro por miembro!
- **Player:** No te preocupes, los Reyes Magos te van a pagar una cuantiosa pensión para que puedas jubilarte...
- **Bert:** ¡Pero qué haré conmigo hoy! Me encanta la arena.
- **Player:** ¿Qué harás con tu día? Bueno... ¡Podrías construir castillos de arena con tus propias manos!
- **Bert:** No lo creo... pero si alguna vez necesitas a alguien que transporte cubos de arena. ¡Déjame saber Player que puedo ayudarte!
- **Player:** ¡Guau! ¡Eso sería genial! ¿Cubos de arena directos a mi banco todos los días, dices? ¡Genial!

##### Diálogo posterior

- (Condition: If the player has not collected the daily sand from Bert:)
  - (Condition: If the player does not have enough free bank space:)
    - **Bert:** Eeee, no tienes espacio libre en ese banco, Player. Haz algo de espacio entre los peces y las botas antes de volver a mí.
    - **Player:** Está bien, haré algo de espacio en mi banco y volveré.
  - (Condition: If the player has enough free bank space:)
    - {{Trandom}}
      - (Diálogo 1 :)
        - **Bert:** ¡Buenos días Player!
        - **Player:** ¡Hola Bert!
        - **Bert:** ¡Me arriesgaré y supongo que hoy quieres tener tu arena!
        - **Player:** Sí, me gustaría la arena, por favor Bert.
        - **Bert:** ¡Me pondré manos a la obra!
      - (Diálogo 2 :)
        - **Bert:** '¡Hola, Player!
        - **Player:** ¡Espero que estés teniendo un buen día!
        - **Bert:** ¡Oh, claro, no es una lástima, aunque a veces me vendría bien un segundo par de manos! ¡Me pondré en marcha para trasladarlos en cubos de arena a tu banco!
        - **Player:** Gracias Bert, ¡hasta mañana!
      - (Diálogo 3 :)
        - **Bert:**Pensé que vendrías en Player. ¿Supongo que querrás tu arena hoy?
        - **Player:** Sí... quiero decir, ¡sí, por favor, Bert!
        - **Bert:** Seguiré moviéndolo. ¡Gracias por asegurarte de que Sandy lo haga en el cuello porque es un doble trato!
        - **Player:** ¡Excelente! Mientras tú mueves la arena a mi banco, yo haré otra cosa, ¡hasta luego!
      - (Diálogo 4 :)
        - **Bert:** '¡Hola de nuevo Player!
        - **Player:** Hola Bert, ¿podría darme mi arena hoy, por favor?
        - **Bert:** ¡Sí, dame un minuto porque me apuran!
        - **Player:** ¡Gracias por la arena Bert!
- (Condition: If the player has collected the daily sand from Bert:)
  - **Bert:** '¡Hola, Player! Espero que te diviertas. Estaré un poquito ocupado para "ayudar con esa arena". Vuelve [in [number] días/mañana].
  - **Player:** Está bien, Bert. Volveré por mi arena un poco más tarde.

### Sand


#### Después de La mano en la arena


##### Antes de haber recogido la arena diaria de Bert


##### Sin suficiente espacio bancario

- (above|no-bank-space)

##### Con suficiente espacio bancario

- **Bert:** Buenos días, Player. Llevaré tu arena a tu banco de inmediato.

##### Después de haber recogido la arena diaria de Bert

- (above|after-collect-sand)

### NPC Contact

- (ver|NPC Contact#Bert)
