# Stiles

- **Original Wiki Page**: [Transcript:Stiles](https://runescape.wiki/w/Transcript%3AStiles)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At Musa Point


#### Hablando con él


##### Normalmente

- **Stiles:** Sí, es un gran día para pescar. ¿Querrás cambiar tu pescado por billetes?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: cond=If the player has used the Exchange option or asked "Which fish can you exchange?" before|Está bien, cambia todo mi pescado por billetes.
    - **Player:** Está bien, cambio todos mis peces por billetes.
    - (Condition: Con atún, bogavante o pez espada sin anotar en backpack:)
      - (removes=all unnoted tuna, lobster or swordfish in backpack) (receives=noted tuna, lobster and/or swordfish)
      - **Stiles:** Ahí va.
    - (Condition: Sin atún, langosta o pez espada desapercibidos en backpack:)
      - **Stiles:** Ahhh, no tienes nada que el viejo Stiles pueda intercambiar. Me encargaré de tus lobbys, de tus espadachines y de tu atún, eso es todo.
  - [Choice]: ¿Quién eres y por qué estás aquí?
    - **Player:** ¿Quién eres y por qué estás aquí?
    - **Stiles:** Ahhh, cuando era joven mi nombre era Nigel pero, hoy en día, la gente me llama principalmente Stiles.
    - **Stiles:** Hace mucho tiempo, en Draynor Village, había tres hermanos que cambiaban tus cosas por pedacitos de papel, como estos novedosos billetes que tenemos hoy. Niles, Miles y Giles se llamaban a sí mismos.
    - **Stiles:** Ya pasaron hace tiempo, como los días dorados, pero fueron una inspiración para mí, así que tomé este oficio yo mismo y cambié mi nombre a Stiles.
    - **Player:** ¿Pero por qué estás aquí, en este lugar?
    - **Stiles:** El olor de esos plátanos me estaba volviendo loco, así que no puedo acercarme demasiado a los lugares de pesca.
    - **Stiles:** Un vejete de aspecto rudo que se hace llamar slayer master intentó darme una clavija una vez, pero no puedo usar ninguna de esas cosas. Ol' Stiles tiene una nariz tierna.
    - **Stiles:** Entonces, ¿quieres que te cambie el pescado ahora?
    - (otro)
  - [Choice]: ¿Qué pescado puedes intercambiar?
    - **Player:** ¿Qué pez puedes intercambiar?
    - **Stiles:** Ahhh, el viejo Stiles tiene billetes para sus lobbys, sus espadachines y su atún. Es un gran servicio el que ofrezco aquí y no pido ni un centavo a cambio.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Por qué no intercambias otros peces?
        - **Player:** ¿Por qué no intercambias otros peces?
        - **Stiles:** Ahhh, no busco aprender un nuevo oficio a mi edad. Lobbies, espadachines y atún son suficientes para el viejo Stiles. ¿Quieres que te cambie el pescado ahora?
        - (otro)
      - [Choice]: Está bien, cambia todo mi pescado por billetes.
        - (above|exchange1)
      - [Choice]: ¿Quién eres y por qué estás aquí?
        - (above|background)
      - [Choice]: No gracias.
        - **Player:** No, gracias.
  - [Choice]: No gracias.
    - **Player:** No, gracias.

##### Sobre la búsqueda de huevos en la comunidad

- **Stiles:** Sí, es un gran día para pescar. ¿Querrás cambiar tu pescado por billetes?
- **Player:** Hola. No tengo tiempo para intercambiar en este momento. De hecho, estoy buscando algunos huevos de oro.
- **Stiles:** Ah-ha, entonces eres tú quien está buscando esto.
- [Stiles saca un huevo de oro del barril cercano y te lo entrega.]
- ¡Encontraste un huevo de oro! Al abrirlo, descubres la siguiente pista.
- (ventana emergente)
  - (Ventana emergente: ¡Encontraste un huevo de oro! Al abrirlo descubres la siguiente pista.|color=#00FF00)
  - (continue)
- Se ha agregado lo siguiente a su bolsa de divisas: 3 x puntos Egg.
- Se ha agregado lo siguiente a su bolsa de divisas: 10 x Puntos Treasure Trail.
- **Player:** Perfecto, ¡gracias Stiles!
- **Stiles:** {{Sic|ol'}} Stiles te desea buena suerte para encontrar al resto.

#### Opción de intercambio

- (Condition: Si el player no ha utilizado la opción Intercambio ni ha preguntado "¿Qué pez puedes intercambiar?" antes:)
  - **Stiles:** ¿Quieres que cambie todos tus lobbys, tus espadachines y tu atún por billetes?
    - (above|whichfish)
- (Condition: Si el player utilizó la opción Intercambiar o preguntó "¿Qué pez puedes intercambiar?" antes:)
  - (above|exchange2)
