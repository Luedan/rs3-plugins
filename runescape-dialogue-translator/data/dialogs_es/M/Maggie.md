# Maggie

- **Original Wiki Page**: [Transcript:Maggie](https://runescape.wiki/w/Transcript%3AMaggie)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|dialogue for when the broomstick is only partially enchanted or not enchanted at all}}

### Before Swept Away

- (ver|Barrido)

### After Swept Away

- (Condition: If the player has lost their broomstick from the quest:)
  - **Maggie:** Lo primero es lo primero. ¿Dónde está esa escoba que te di?
  - **Player:** Uh, en realidad, no estoy seguro de dónde está.
  - **Maggie:** Bastante. Eso es porque lo tengo aquí. Tienes suerte de que alguien lo haya encontrado en sus andanzas y haya pensado en devolverlo.
  - (receives=broomstick)
  - **Maggie:** Aquí tienes, pero cuídalo de ahora en adelante. Este es un pequeño trabajador bastante especial.
  - **Maggie:** Ahora que hemos solucionado eso, ¿qué puedo hacer por ti en este buen día, cha?
  - (continue)
- (Condition: If the player still has their broomstick from the quest:)
  - **Maggie:** ¡Bienvenido, viajero! ¿Qué puedo hacer por ti en este buen día, cha?
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: Quiero hablar de recompensas.
    - **Player:** Quiero hablar sobre recompensas.
    - [Menu]: Selecciona una opción
      - [Choice]: *(Si al gulash todavía le quedan diez porciones)* Bueno, sobre este gulash.
        - **Player:** Entonces, sobre este gulash.
        - **Maggie:** ¡Cha! Es realmente espléndido; deberías intentarlo.
        - **Maggie:** Hay suficiente para 10 tazones llenos; solo usa un tazón para tomar un poco del caldero y luego disfruta, ¡pero agárrate al sombrero!
        - **Maggie:** Después de todo, eso es mágico. No es mi propia intención, ¡pero un solo cuenco puede mejorar casi cualquier aspecto de tu vida!
        - (receives=bowl)
        - **Maggie:** Aquí tienes un cuenco que puedes usar.
        - **Player:** Gracias, Maggie.
      - [Choice]: *(Si el gulash se ha consumido al menos parcialmente)* Entonces, ¿te queda más de ese gulash?
        - **Player:** Entonces, ¿te queda algo más de ese gulash?
        - (Condition: If there is still some goulash left:)
          - **Maggie:** Claro, ¡sírvete tú mismo! Solo usa un bol con el caldero. Debería quedar suficiente para tener [número] más tazones llenos.
          - **Maggie:** Sin embargo, agárrate al sombrero; Después de todo, eso es mágico. No es mi propia intención, ¡pero un solo cuenco puede mejorar casi cualquier aspecto de tu vida!
          - (receives=bowl)
          - **Maggie:** Aquí tienes un cuenco que puedes usar.
          - **Player:** Excelente, gracias.
        - (Condition: If there is no more goulash left:)
          - **Maggie:**¡Cha! Eres un descarado, ¿no has tenido suficiente?
          - **Player:** Bueno, estuvo bastante bien.
          - **Maggie:** ¡Por supuesto que es bueno! Esa receta se ha perfeccionado a lo largo de no sé cuántos años de experimentación con brujas.
          - **Player:** ...
          - **Maggie:** ...
          - **Player:** ¿Y entonces?
          - **Maggie:** ¿Y qué?
          - **Player:** Entonces, ¿te queda más gulash?
          - **Maggie:** Me queda algo, cha, pero me temo que no es suficiente para compartir.
          - (initial)
      - [Choice]: ¿Qué encantamientos hay disponibles para esta escoba?
        - **Player:** ¿Qué encantamientos hay disponibles para esta escoba?
        - (Condition: If the broomstick has not been enchanted at all:)
          - **Maggie:** Bueno, recomendaría hablar con el aprendiz de Sorceress en Al Kharid. Ella sabe más de lo que deja entrever sobre la teletransportación.
          - **Maggie:** Y, para los usuarios de Magic, hay algunas brujas que pueden darle un pequeño impulso a su experiencia Magic.
          - **Maggie:** Maysa the Hag en Pollniveach puede encantar tu escoba si tienes un nivel de Magic de 33 o superior.
          - **Maggie:** Netty cerca de la Torre Slayer puede encantar tu escoba si tienes un nivel Magic de 53 o superior.
          - **Maggie:** Baba Yaga en Lunar Isle puede encantar tu escoba si tienes un nivel de Magic de 73 o superior.
          - **Maggie:** Es posible que Kardia en Underground Pass no te hable, pero podría encantar tu escoba si tienes un nivel de Magic de 93 o superior.
        - (Condition: If the broomstick is enchanted only by the apprentice so far:)
          - **Maggie:** Bueno, ya tienes la escoba encantada por el aprendiz de Sorceress en Al Kharid.
          - **Maggie:** Y, para los usuarios de Magic, hay algunas brujas que pueden darle un pequeño impulso a su experiencia Magic.
          - **Maggie:** Maysa the Hag en Pollnivneach puede encantar tu escoba si tienes un nivel de Magic de 33 o superior.
          - **Maggie:** Netty cerca de la Torre Slayer puede encantar tu escoba si tienes un nivel Magic de 53 o superior.
          - **Maggie:** Baba Yaga en Lunar Isle puede encantar tu escoba si tienes un nivel de Magic de 73 o superior.
          - **Maggie:** Es posible que Kardia en Underground Pass no te hable, pero podría encantar tu escoba si tienes un nivel de Magic de 93 o superior.
        - (Condition: If the broomstick is fully enchanted:)
          - **Maggie:** Bueno, ya tienes la escoba encantada por el aprendiz de Sorceress en Al Kharid.
          - **Maggie:** También tienes la escoba encantada por Maysa the Hag, la vieja bruja cerca de la torre Slayer, Baba Yaga y Kardia.
  - [Choice]: Tu casa parece estar sobre ruedas.
    - **Maggie:** ¡Qué observador eres, cha! Por supuesto que va sobre ruedas. ¿Cómo podría desplazarme si no?
    - **Player:** ¿Moverse?
    - **Maggie:** Oh, sí, me gusta seguir moviéndome, no lo sé. No hay nada que odio más que estar atrapado en el mismo lugar por mucho tiempo.
    - (otro)
  - [Choice]: Entonces, sobre esos bueyes.
    - **Maggie:** Sí, pobre Babe, cap. Espero que se le pase pronto el resfriado.
    - **Maggie:** Después de todo, difícilmente podría pedirle que tirara de esta vieja caravana en las condiciones en las que se encuentra, ¡cha!
    - (otro)

#### Usando un objeto en ella

- **Maggie:** Gracias por la oferta, pero realmente no la necesito. ¿Por qué no te lo quedas?
