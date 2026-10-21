# Johnathon

- **Original Wiki Page**: [Transcript:Johnathon](https://runescape.wiki/w/Transcript%3AJohnathon)
- **Letter**: `J`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Family Crest

- **Johnathon:** Estoy muy cansada... Déjame en paz... para descansar...

### After Family Crest


#### Con los guanteletes familiares intactos

- **Johnathon:** Hola de nuevo. Mi familia ahora te considera un héroe.
- **Player:** Tu padre me dice que puedes mejorar estos guanteletes para mí...
- **Johnathon:** Y tiene razón en eso. Aunque mi habilidad con las magias de las Runas de la Muerte no fue lo suficientemente grande como para derrotar a Chronozon, tengo habilidades adecuadas con las magias de las Runas del Caos. Si me das tus guanteletes, les otorgaré parte de mi poder y haré que cualquier hechizo de rayo que desees lanzar sea más efectivo.
- Seleccione una opción
  - Eso me suena bien.
    - **Player:** ¡Eso me parece bien!
    - Johnathon te quita los guanteletes y comienza un canto bajo sobre ellos. Los ves comenzar a brillar y brillar, antes de que él te los devuelva.
    - (removes=family gauntlets) (receives=chaos gauntlets)
  - Primero veré qué opciones pueden ofrecerme tus hermanos.
    - **Player:** Creo que comprobaré mis otras opciones con tus hermanos antes de comprometerme.
    - **Johnathon:**Dudo que ofrezcan algo tan útil como mi impulso mágico, pero como desees.

#### Con los guanteletes familiares imbuidos o sin ninguno de los guanteletes


##### Opción de hablar con

- **Johnathon:** Hola de nuevo. Mi familia ahora te considera un héroe.
- **Player:** Quizás porque… lo soy.
- **Johnathon:** Sí, bueno... ¿Hay algo en lo que pueda ayudarte?
- Elige una opción:
  - ¿Puedes cambiar mis guanteletes por mí?
    - **Player:** ¿Puedes cambiarme los guanteletes? {{anchor|change-gauntlets}}
    - *(Si el player no tiene guanteletes:)*
      - **Johnathon:** No tienes ningún guantelete que pueda imbuirte.
    - *(Si el player actualmente tiene guanteletes del caos en su inventario:)*
      - **Johnathon:** Tus guanteletes ya están imbuidos de mis poderes. No tienes ningún guantelete que pueda imbuirte.
    - *(Si el player tiene los guanteletes:)*
      - **Johnathon:** Sí, claro, aunque te costará 25.000 coins.
      - Seleccione una opción
        - ¡Muchas gracias!
          - *(Si el player tiene al menos 25,000 coins:)*
            - (removes=family gauntlets and 25,000 coins) (receives=chaos gauntlets)
            - **Johnathon:** Tus guanteletes ya están imbuidos de mis poderes.
          - *(Si el player tiene menos de 25,000 coins:)*
            - **Johnathon:** Desafortunadamente no tienes suficiente coins contigo, regresa con 25,000 y te cambiaré esos guanteletes.
        - No, está bien, gracias.
          - (end)
  - *(Después de encantar los guanteletes familiares por primera vez :)*
    - ¿Tu familia posee más guanteletes?
      - **Player:** ¿Tu familia posee más guanteletes? Realmente aprecio la habilidad y el esfuerzo que tú y tus hermanos habéis puesto en esos guanteletes y, para demostrarlo, me gustaría tener uno de cada par.
      - **Johnathon:** Tengo un par que me regaló mi padre, pero son una reliquia familiar y se supone que no debo separarme de ellos. Sin embargo, si mi padre considerara oportuno darte el suyo, podría convencerme.
      - **Player:** ¿Cuánto pedirías por ellos?
      - **Johnathon:** 1 millón de coins.
      - Seleccione una opción
        - Me gustaría comprarlos por 1 millón.
          - **Player:** Me gustaría comprarlos por 1 millón.
          - **Johnathon:** ¿Estás seguro? ¡Eso es mucho dinero!
          - Seleccione una opción
            - **Player:**¡Sí!
              - (removes=1,000,000 coins) (receives=chaos gauntlets)
            - **Player:**Supongo que no.
              - (end)
        - Supongo que será mejor que los conserves.
          - **Player:** Supongo que será mejor que los guardes.
          - **Johnathon:** ¡Gracias!
  - No gracias.
    - **Player:** No, gracias.

##### Opción de cambio de guanteletes

- (arriba2|cambio-guanteletes)
