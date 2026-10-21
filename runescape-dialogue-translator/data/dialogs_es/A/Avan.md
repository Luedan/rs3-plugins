# Avan

- **Original Wiki Page**: [Transcript:Avan](https://runescape.wiki/w/Transcript%3AAvan)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Family Crest


#### Opciones de hablar con o cambiar guanteletes

- **Avan:** ¿Qué? ¿No ves que estoy ocupado?
- **Player:** Bueno, muchísimo...

### After Family Crest


#### Con los guanteletes familiares intactos

- **Avan:** He recibido noticias de mi padre sobre su ayuda a nuestra familia en este asunto. Tienes mi agradecimiento por restaurar nuestro honor.
- **Player:** Tu padre mencionó que podrías mejorar estos guanteletes de alguna manera para mí...
- **Avan:** De hecho, puedo. En mi larga búsqueda del oro "perfecto" aprendí mucho sobre la fundición de metales. Puedo mejorar estos guanteletes para que envíen barras al banco de metal a medida que los fundes. Puedo modificarlos fácilmente para usted.
- **Seleccione una opción**
  - Eso suena bien, mejóralos.
    - **Player:** Eso suena bien. ¡Mejóralos por mí!
    - ''Avan toma tus guanteletes, saca un pequeño martillo, los golpea hasta darles una forma ligeramente nueva y luego te los devuelve.
    - (removes=family gauntlets) (receives=smelting gauntlets)
  - Creo que comprobaré mis otras opciones con tus hermanos.
    - **Player:** Creo que comprobaré mis otras opciones con tus hermanos antes de comprometerme.
    - **Avan:** Si sientes que realmente debes relacionarte con gente como ellos. Espero tu decisión.

#### Con los guanteletes familiares imbuidos o sin ninguno de los guanteletes


##### Opción de hablar con

- **Avan:** He recibido noticias de mi padre sobre su ayuda a nuestra familia en este asunto. Tienes mi agradecimiento por restaurar nuestro honor.
- **Player:** No hay problema.
- **Avan:** Sí, bueno... ¿Hay algo en lo que pueda ayudarte?
- Elige una opción:
  - ¿Puedes cambiar mis guanteletes por mí?
    - **Player:{{anchor|change-gauntlets}}** ¿Puedes cambiarme los guanteletes?
    - *(Si el player tiene los guanteletes:)*
      - **Avan:** Sí, claro, aunque te costará 25.000 coins.
      - Seleccione una opción
        - ¡Muchas gracias!
          - *(Si el player tiene al menos 25,000 coins:)*
            - (removes=family gauntlets and 25,000 coins) (receives=smelting gauntlets)
            - ''Avan toma tus guanteletes, saca un pequeño martillo, los golpea hasta darles una forma ligeramente nueva y luego te los devuelve.
          - *(Si el player tiene menos de 25,000 coins:)*
            - **Avan:** Desafortunadamente no tienes suficiente coins contigo, regresa con 25,000 y te cambiaré esos guanteletes.
        - No, está bien, gracias.
          - (end)
    - *(Si el player ya tiene guanteletes de fundición en el inventario:)*
      - **Avan:** Tus guanteletes ya han sido forjados.
    - *(Si el player no tiene los guanteletes:)*
      - **Avan:** No tienes ningún guantelete que pueda imbuirte.
  - *(Después de encantar los guanteletes familiares por primera vez :)*
    - ¿Tu familia posee más guanteletes?
      - **Player:** ¿Tu familia posee más guanteletes? Realmente aprecio la habilidad y el esfuerzo que tú y tus hermanos habéis puesto en esos guanteletes y, para demostrarlo, me gustaría tener uno de cada par.
      - **Avan:** Tengo mi propio par, tal como me lo entregó mi padre antes de partir. Son una reliquia familiar y muy valiosa para mí. No me separaría de ellos así.
      - **Player:** ¿Cuánto pedirías por ellos?
      - **Avan:** Tienen mucho valor sentimental y los uso todos los días. Es difícil ponerle precio a eso.
      - **Player:** ¿Pero si fuera necesario?
      - **Avan:** ¿1 millón?
      - Seleccione una opción
        - Me gustaría comprarlos por 1 millón.
          - **Avan:** ¿Estás seguro? ¡Eso es mucho dinero!
          - Seleccione una opción
            - **Player:**¡Sí!
              - (removes=1,000,000 coins) (receives=smelting gauntlets)
            - **Player:**Supongo que no.
              - (end)
          - **Player:** Supongo que será mejor que los guardes.
          - **Avan:** ¡Gracias!
  - No gracias.
    - **Player:** No, gracias.

##### Opción de cambio de guanteletes

- (Action: above2|cambio-guanteletes)
