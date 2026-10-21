# Heedi

- **Original Wiki Page**: [Transcript:Heedi](https://runescape.wiki/w/Transcript%3AHeedi)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- [Menu]: Elija una opción:|anchor=Heedi-options
  - [Choice]: ¿Quién eres?
    - **Heedi:** Soy Heedi el botánico. He trabajado mi vida, buscando una manera de superar la naturaleza moribunda de mi mundo.
    - **Heedi:** Había un árbol, sagrado para mi pueblo, pero con el paso de los años se volvió cada vez menos abundante.
    - **Heedi:** Pero ahora, mira, vuelve a vivir.<br>En esencia, al menos.<br>Fusionado con otro; un niño a dos padres.
    - **Heedi:** Qué cosa tan maravillosa, ¿no?
    - (previous|Heedi-options)
  - [Choice]: Sobre estos árboles.
    - [Menu]: Seleccione una opción|ancla=EstasTees
      - [Choice]: Háblame de estos árboles.
        - **Heedi:** ¿Supongo que estás familiarizado con el magic tree?
        - [Sin detenerse a esperar una respuesta, Heedi continúa con entusiasmo.]
        - **Heedi:** Un magic tree extrae energía de sitios de poder mágico para sostenerse... una relación fascinante con el suelo.<br>Casi parásito.
        - **Heedi:** Adaptable. Mudable. ¡Imbuido de poder robado! <br>No muy diferente a tus dioses en guerra.
        - [Heedi se ríe divertido.]
        - **Heedi:** Pero estoy divagando.
        - **Heedi:** Llamemos a este joven mágico el segundo hijo.<br>Lleno de vida y magia, enérgico y salvaje, pero desenfocado y distraído.
        - **Heedi:** Por el contrario, les presento, en su esplendor, a mi claro hijo favorito, el baobab de Iaian.
        - **Heedi:** Adansonia mysticata, a sus amigos.<br>Amigos como yo.
        - **Heedi:** Se necesitó mucha paciencia, algo de coerción, incluso un poco de crueldad, para cruzar los árboles de mi tierra pantanosa con tus árboles mágicos.
        - **Heedi:** ¡Pero he aquí el resultado!<br>Florecen, ¿no?<br>Y qué bonitos.
        - (previous|TheseTees)
      - [Choice]: ¿Puedo cortar estos árboles?
        - **Heedi:** Puedes cosechar su madera, si así lo deseas. El asalto de tus hachas sólo fortalecerá mis árboles mágicos eternos, y así hinchará mi corazón de orgullo.
        - **Heedi:** Sin embargo, su ladrido es duro. Necesitarás una herramienta formidable.
        - **Heedi:** Wilfred, el vendedor de Woodcutting skillcape cerca de Falador lodestone vende un medio para combinar un hacha de cristal y un hacha imcando, pero solo a un aventurero veterano que se ha ganado el respeto de los elfos y enanos.
        - **Heedi:** También escucho historias de un enano con visión diferente que vive en Ice Mountain. Él puede guiarte para mejorar ese hacha, por un precio.
        - (previous|TheseTees)
      - [Choice]: Atrás.
        - [Choice]: anterior|Heedi-opciones
  - [Choice]: Is there anything else I can do for you?|cond=Sin ramas:
    - **Heedi:** Si logras cortar una rama perfecta de un magic tree eterno, te compartiré algunos conocimientos de horticultura a cambio.
    - **Heedi:** Alternativamente, en manos suficientemente hábiles, un par de ramas (y un cubo de savia eterna de magic tree) serían excelentes extremidades para un arco poderoso.
    - (Condition: Sin 110 Woodcutting:)
      - [pic=Rama mágica eterna perfecta detail.png]
      - (continue)
    - (Condition: Con 110 Woodcutting:)
      - [pic=Rama mágica eterna perfecta detail.png]
      - (continue)
    - [pic=Rama mágica eterna perfecta detail.png]
    - (previous|Heedi-options)
  - [Choice]: Can I offer you a branch in this trying time?|cond=Con al menos una rama:
    - **Heedi:** Oh, qué excelente ejemplar. A cambio, compartiré algunos conocimientos sobre horticultura.
    - (Condition: Se muestra en una interfaz titulada "OFERTA SUCURSALES":)
      - Archivo:Woodcutting.png Tienes [número] eterno magic tree [branch/branches].<br><br>¿Te gustaría darle [it/them] a Heedi?<br><br>Recibirás [número] Woodcutting XP.
        - [Choice]: Cancelar
          - ((La interfaz se cierra.))
          - (previous|Heedi-options)
        - [Choice]: bien
          - ((La interfaz se cierra.))
          - (removes=all perfect eternal magic branches)
          - (Action: el player gana la cantidad correspondiente de experiencia Woodcutting.)
          - (previous|Heedi-options)
  - [Choice]: Can I plant these trees elsewhere?|cond=Habiendo completado el logro El Laúd del Amor:
    - **Player:** Creo que encontré un lugar donde estos árboles mágicos eternos florecerían. ¿Alguna posibilidad de que puedas ayudarme a plantar algo allí?
    - **Heedi:** Con mucho gusto enviaría a mis hijos al mundo.
    - **Heedi:** Ten estos retoños. Los preparé con sumo cuidado.
    - **Heedi:** Si el suelo del que hablas es realmente digno, crecerán rápidamente, incluso en manos de un granjero aficionado.
    - (Condition: Si el player ya tiene algún retoño en el banco o en el inventario:)
      - **Heedi:** Ah, pero todavía tienes algunos de mis árboles jóvenes. Vuelve si te quedas sin.
  - [Choice]: Adiós.
    - (end)

### Give branches to


#### Sin sucursales


##### Sin 110 Woodcutting

- [pic=Rama mágica eterna perfecta detail.png]

##### Con 110 Woodcutting

- [pic=Rama mágica eterna perfecta detail.png]
- [pic=Rama mágica eterna perfecta detail.png]

#### Con ramas

- ((Se muestra en una interfaz titulada "OFERTA SUCURSALES":))
  - Archivo:Woodcutting.png Tienes [número] eterno magic tree [branch/branches].<br><br>¿Te gustaría darle [it/them] a Heedi?<br><br>Recibirás [número] Woodcutting XP.
    - [Choice]: CANCELAR
      - ((La interfaz se cierra.))
    - [Choice]: bien
        - ((La interfaz se cierra.))
        - (removes=all perfect eternal magic branches)
        - (Action: el player gana la cantidad correspondiente de experiencia Woodcutting.)
