# Velrak the explorer

- **Original Wiki Page**: [Transcript:Velrak the explorer](https://runescape.wiki/w/Transcript%3AVelrak%20the%20explorer)
- **Letter**: `V`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In his cell in the Black Knights' Base


#### Antes de reclamar la llave polvorienta

- **Velrak the explorer:** ¡Gracias por rescatarme! <br>No es muy cómodo en esta celda.
- [Menu]: Selecciona una opción
  - [Choice]: Entonces... ¿conoces algún lugar bueno para explorar?
    - **Velrak the explorer:** Bueno, esta mazmorra era bastante buena para explorar... hasta que me capturaron, de todos modos. ¡Un misterioso extraño encapuchado me dio la llave de una parte interior de esta mazmorra!
    - **Velrak the explorer:** Sin embargo, es bastante difícil para mí llegar tan lejos en la mazmorra. ¡Sigo siendo capturado!
    - **Velrak the explorer:** ¿Te gustaría intentarlo?
    - [Menu]: Selecciona una opción
      - [Choice]: ¡Sí, por favor!
        - (Condition: Sin espacio en backpack:)
          - **Velrak the explorer:** Te daría la clave, pero tu backpack está lleno.
        - (Condition: Con espacio en backpack:)
          - (receives=dusty key)
          - [Velrak llega a algún lugar misterioso y te pasa una llave.]
          - (initial)
      - [Choice]: No, es demasiado peligroso para mí también.
        - **Velrak the explorer:** ¡No te culpo!
  - [Choice]: ¿Recibo una recompensa por liberarte?
    - **Velrak the explorer:** Bueno, en realidad no. <br>¡El Black Knights tomó todas mis cosas antes de arrojarme aquí para que me pudriera!
    - (initial)

#### Después de reclamar la llave polvorienta

- **Player:** ¿Sigues aquí?
- **Velrak the explorer:** Sí... <br>I todavía estoy reuniendo el coraje para escapar de esos Black Knights.
- **Player:** Oh, continúa. Puedes hacerlo. <br>I cuidaré tu espalda.
- **Velrak the explorer:** Bueno, lo intentaré. Si lo logro, podrás encontrarme en la entrada de la mazmorra Taverley.
- (Action: La pantalla se desvanece y vuelve a aparecer; Velrak ha escapado.)
- {{RSFontAchievement|Fly You Fool}}

### At the entrance to Taverley dungeon

- **Velrak the explorer:** ¡Luz del sol! La maravilla de una suave brisa acariciando mi piel. Oh, es glorioso.
- **Velrak the explorer:** Estuve atrapado tanto tiempo en esa mazmorra de Kinshra que había olvidado lo colorido y brillante que es Taverley. ¡Huela ese aire fresco!
- **Player:** Realmente no estás tan fresco como crees. Quizás sea hora de darse un baño.
- **Velrak the explorer:** Sí, sí. Pronto. Primero quiero contemplar por un momento el resplandeciente esplendor del río Taverley.
- (Condition: Si el player ha perdido la llave polvorienta:)
  - **Player:**Oye, ¿recuerdas esa llave polvorienta que me diste?
  - **Velrak the explorer:** ¿Sí?
  - **Player:**Lo perdí.
  - **Velrak the explorer:**¿Y?
  - **Player:**Espero que lo tengas.
  - **Velrak the explorer:**¿Por qué iba a tenerlo?<br> Te di la clave.
  - **Player:**Bueno, a veces, cuando pierdo cosas, otras personas las encuentran por mí.
  - **Velrak the explorer:** Vaya. ¿De verdad crees que otras personas no tienen nada mejor que hacer que ocuparse de ti? Tu narcisismo se está mostrando.
  - **Velrak the explorer:** Ya es bastante malo que ni siquiera te molestes en conservar los regalos que te damos. ¿De verdad crees que el mundo gira a tu alrededor?
  - **Player:**Mira, solo revisa tus bolsillos. Confía en mí.
  - (Condition: Sin espacio en backpack:)
    - **Velrak the explorer:** Revisas tus bolsillos. Ni siquiera tienes suficiente espacio en tu backpack para guardar una llave.
  - (Condition: Con espacio en backpack:)
    - (receives=dusty key)
    - [Velrak se palpa y saca una llave polvorienta. Parpadea sorprendido y te lo entrega, desconcertado.]
