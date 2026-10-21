# Islwyn

- **Original Wiki Page**: [Transcript:Islwyn](https://runescape.wiki/w/Transcript%3AIslwyn)
- **Letter**: `I`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Isafdar


#### Antes de Roving Elves

- **Player:** Hola.
- **Islwyn:** Déjame en paz, no tengo tiempo para los orientales, ahora vete.

#### Teletransportarse


##### Antes de la luz interior

- **Islwyn:** {{RSChat|It is time we left.}}
- **Eluned:** {{RSChat|Yes, let us move on.}}

##### Después de la luz interior

- **Islwyn:** {{RSChat|It is time to leave.}}

#### Después de Roving Elves, antes de Plague's End

- **Player:** Hola de nuevo.
- (Condition: Si el player decidió obtener un arco de cristal de Islwyn al completar Roving Elves:)
  - **Islwyn:** Ah, me alegro de verte de regreso. ¿Buscas otro arco o uno de mis escudos?
- (Condition: Si el player elige obtener una protección de cristal de Islwyn al completar Roving Elves:)
  - **Islwyn:** Ah, me alegro de verte de regreso. ¿Buscas otro escudo o uno de mis arcos?
- [Menu]: Elige una opción:
  - [Choice]: Uno de tus arcos, por favor.
    - **Player:** Uno de tus arcos, por favor.
    - **Islwyn:** Son 1.000.000 coins cada uno para los nuevos.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Pagar 1.000.000 coins?
        - (Condition: Si el player tiene al menos 1.000.000 coins:)
          - **Player:** Aquí hay 1.000.000 coins.
          - Entregas 1.000.000 coins y recibes a cambio un lazo de cristal.
          - **Islwyn:** Buena caza.
          - **Player:** Gracias... adiós.
        - (Condition: Si el player no tiene al menos 1.000.000 coins:)
          - **Player:** Lo siento, pero no tengo tanto.
          - No puedes permitirte eso.
          - **Islwyn:** Bueno, lo siento, pero no puedo dejarlo pasar por menos.
          - **Islwyn:** Oh, bueno... hasta luego.
      - [Choice]: No, gracias.
        - (end)
  - [Choice]: Me gustaría comprar un escudo.
    - **Player:** Me gustaría comprar un escudo.
    - **Islwyn:** Son 1.000.000 coins cada uno para los nuevos.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Pagar 1.000.000 coins?
        - (Condition: Si el player tiene al menos 1.000.000 coins:)
          - **Player:** Aquí hay 1.000.000 coins.
          - Entregas 1.000.000 coins y obtienes a cambio una protección de cristal.
          - **Islwyn:** Cuídate.
          - **Player:** Gracias... adiós.
        - (Condition: Si el player no tiene al menos 1.000.000 coins:)
          - **Player:** Lo siento, pero no tengo tanto.
          - No puedes permitirte eso.
          - **Islwyn:** Bueno, lo siento, pero no puedo dejarlo pasar por menos.
          - **Islwyn:** Oh, bueno... no importa entonces.
      - [Choice]: No, gracias.
        - (end)
  - [Choice]: No, sólo estoy de paso.
    - **Player:** No, solo estoy de paso.
    - (Condition: Si el player aún no ha iniciado Mourning's End Parte I y no se ha negado a aceptar la misión de Eluned:)
      - **Islwyn:** Bueno, que bueno verte de nuevo...<br> Eluned me dice que Arianwyn te está buscando. Quizás ella sepa por qué.
    - (Condition: De lo contrario:)
      - **Islwyn:** Bueno, es bueno verte de nuevo. Espero que todo te vaya bien?
      - **Player:** Tan bien como se puede esperar.

#### Después del fin de la plaga

- **Player:** Hola de nuevo.
- (Condition: Si obtuviste un arco de cristal de Islwyn al completar Roving Elves:)
  - **Islwyn:** Ah, me alegro de verte de regreso. ¿Buscas otro arco o uno de mis escudos?
- (Condition: Si obtuviste una protección de cristal de Islwyn al completar Roving Elves:)
  - **Islwyn:** Ah, me alegro de verte de regreso. ¿Buscas otro escudo o uno de mis arcos?
- (Condition: Seleccione una opción:)
  - [Choice]: Uno de tus arcos, por favor.
    - (arriba)
  - [Choice]: Me gustaría comprar un escudo.
    - (arriba)
  - [Choice]: Deberías ser Lord Cadarn, no Arianwyn.
    - **Player:** Deberías ser Lord Cadarn, no Arianwyn.
    - **Islwyn:** ¿Por qué? ¿Qué he hecho yo para merecer tan gran honor?
    - **Player:** Pero eres nieto de la Reina Glarial... es tu derecho de nacimiento.
    - **Islwyn:** Rápidamente asumes que los elfos comparten tus costumbres. Mi sangre no me concede ningún privilegio especial. ¿Cómo podrían confiar en mí en una posición de poder si no he demostrado ser un líder sabio? Si King Lathas no hubiera heredado un trono, es probable que tus tierras del este se hubieran ahorrado muchas penas.
    - (Condition: Si perdonaste a King Lathas en Plague's End:)
      - **Islwyn:** Me sorprende que le hayas mostrado misericordia.
        - (continue)
    - (Condition: Si mataste a King Lathas en Plague's End:)
      - **Islwyn:** Siento que los humanos ponen demasiado poder en manos de los monarcas. Presumiblemente estás de acuerdo, King Slayer.
        - (continue)
    - **Islwyn:** Arianwyn ha demostrado ser notablemente apto para el señorío. Luchó contra la tiranía de Lord Iorwerth y, con no poca ayuda de su parte, llevó a nuestra gente de regreso a Prifddinas. Estoy orgulloso del logro de Lord Cadarn y se ha ganado mi respeto.
  - [Choice]: No, sólo estoy de paso.
    - (arriba)

### In Prifddinas, after The Light Within


#### Habla con

- **Player:** Hola Islwyn.
- **Islwyn:** Bien conocido Player.
- **Player:** ¿Dónde está Eluned? ¿No está ella normalmente aquí?
- (Condition: Si el player recibió la carta de Eluned y aún no la ha destruido:)
  - **Islwyn:** La carta debe cubrir todo.
- (Condition: Si el player no ha recibido o ha destruido la carta de Eluned:)
  - **Islwyn:** Sí... ella quería que te diera esto. Lo explica todo.
  - [Islwyn te entrega una carta de Eluned.]
  - **Islwyn:** Prifddinas es todo un espectáculo. Sin duda está a la altura de las expectativas.
  - **Player:** ¿Ya has hablado con tu abuelo?
  - **Islwyn:** No... todavía no... Estoy tratando de decidir qué decir.
  - **Player:** Probablemente él siente lo mismo, tal vez deberías... eh... ¿ambos no logran hablar juntos?
  - **Islwyn:** Eso... sí... eso realmente no tenía mucho sentido.
  - **Player:** De hecho, no... entonces... ¿canto de cristal?
  - **Islwyn:** Muéstrame una semilla de cristal o un objeto de cristal y veré qué puedo hacer con él.

#### Usando una semilla de cristal sintonizada en él

- **Islwyn:** Lo siento, no puedo hacer nada con cristales sintonizados. Están más allá de mi capacidad.

#### Usando una semilla de teletransporte con cargas sobre él

- **Islwyn:** Oh, ese cristal de teletransporte todavía está encantado.

#### Usando un azadón de cristal, un hacha o un pico sobre él

- **Islwyn:** ¡Nunca antes había visto una herramienta de cristal como esa! Ni siquiera pensé que fuera posible...
- **Islwyn:** Esto es obra de Lady Ithell, ¿no?
- **Islwyn:** Las tensiones armónicas infligidas a este instrumento son dolorosas para mis oídos. Me sorprende que no se haya hecho añicos. Mantenlo alejado de mí.

#### Usando una semilla de teletransporte descargada sobre él

- [Menu]: ¿Agregar 8 cargas a una semilla de teletransporte por 400 coins?
  - [Choice]: Cancelar
    - (end)
  - [Choice]: bien
    - (removes= 400 coins and Crystal teleport seed) (receives= Crystal teleport seed (8))

#### Usando múltiples semillas de teletransporte de cristal sobre él.

- ¿Agregar 8 cargas a las semillas de teletransporte [número] para [número] coins?
  - Cancelar
    - (end)
  - OK
    - (removes= [number] coins and crystal teleport seeds) (receives= Crystal teleport seeds (8))

#### Usando una semilla de herramienta de cristal sobre él.

- ''(Se abre la interfaz Elegir herramienta; consulte Semilla de herramienta Crystal para obtener una lista de opciones)

#### Usando una semilla de armadura de cristal sobre él.

- ''(Se abre la interfaz Elegir Escudo, consulte Semilla de armadura de cristal para obtener una lista de opciones)

#### Usando una semilla de arma de cristal sobre él.

- ''(Se abre la interfaz Elegir arma, consulte Semilla de arma de cristal para obtener una lista de opciones)

#### Usar un objeto hecho a partir de una semilla de cristal sintonizada o una semilla de cristal sobre él.

- ((Lo siguiente se muestra en una interfaz titulada "¿RECARGAR O REVERTIR?":))
  - (Condition: Con el artículo completamente cargado:)
    - Este artículo está completamente cargado.
      - [Choice]: RECARGAR
        - ((La opción está deshabilitada.))
  - (Condition: Con el artículo no completamente cargado:)
    - Artículo de recarga para [número] coins.
      - [Choice]: RECARGAR
        - (Condition: Sin suficiente coins:)
          - ((La interfaz se cierra.))
          - **Islwyn:** No tienes suficiente coins para cubrir ese costo, lo siento.
        - (Condition: Con suficiente coins:)
          - ((La interfaz se cierra.))
          - (Action: El artículo está recargado.)
          - (removes=coins corresponding to the cost)
          - (Condition: Si el coins fue sacado de la bolsa de dinero:)
            - [número] coins se han eliminado de su bolsa de dinero.
  - Revierta este artículo a semilla (pierde todos los cargos).
    - [Choice]: REVERTIR
      - {{Transcript missing}}
