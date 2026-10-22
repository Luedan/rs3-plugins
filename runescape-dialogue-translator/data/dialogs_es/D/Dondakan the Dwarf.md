# Dondakan the Dwarf

- **Original Wiki Page**: [Transcript:Dondakan the Dwarf](https://runescape.wiki/w/Transcript%3ADondakan%20the%20Dwarf)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### South of Keldagrim


#### Antes Entre una Roca...

- **Player:** ¡Hola!
- **Dondakan the Dwarf:** ¿Qué?
- **Player:** ¡Dije hola!
- **Dondakan the Dwarf:** ¡Hola!
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Dondakan the Dwarf:** ¡Vaya, soy Dondakan, por supuesto!
    - (initial)
  - [Choice]: ¿Por qué disparas un cañón contra una pared?
    - **Player:** ¿Por qué disparas un cañón a una pared?
    - **Dondakan the Dwarf:** ¡No te lo puedo decir!
    - **Player:** ¿Por qué no?
    - (Condition: If the player has not completed Fishing Contest - this takes priority over not completing Dwarf Cannon:)
      - **Dondakan the Dwarf:** ¡Eres un humano! ¡Esto es cosa de enanos!
      - **Player:** ¿No hay nada que pueda hacer para que me lo digas?
      - **Dondakan the Dwarf:** Quizás si pudieras ayudar a algunos de mis compañeros enanos...
      - **Dondakan the Dwarf:** He oído que hay una competición de pesca que algunos de mis parientes lejanos están interesados en ganar, por ejemplo.
      - **Player:** ¿Una competición de pesca? ¿Qué hacen los enanos en una competición de pesca?
      - **Dondakan the Dwarf:** ¡No están en esto! ¡No podrían pescar aunque sus vidas dependieran de ello!
      - **Dondakan the Dwarf:** ¡Ahí es donde entras tú! ¡Corre ahora!
      - (initial)
    - (Condition: If the player has completed Fishing Contest but not Dwarf Cannon:)
      - **Dondakan the Dwarf:** Bueno... eres el campeón de Fishing... pero todavía no puedo hablar de esto.
      - **Dondakan the Dwarf:** El cañón es un proyecto enano ultrasecreto, ¿sabes?
      - **Player:** No me parece muy secreto estar ahí afuera.
      - **Dondakan the Dwarf:** Ser descarado, ¿eh?
      - **Dondakan the Dwarf:** Quizás deberías hablar con Lawgof, el comandante de Black Guard en Kandarin.
      - (initial)
    - (Condition: If the player has completed both Fishing Contest and Dwarf Cannon:)
      - (ver|Entre una Roca...#Una Roca Irrompible)
  - [Choice]: Un poco ruidoso aquí, ¿no?
    - **Player:** Un poco ruidoso aquí, ¿no?
    - **Dondakan the Dwarf:** ¿Acogedor? No, realmente no, ¡está húmedo y frío!
    - **Player:** ¡No! ¡Dije que es ruidoso!
    - **Dondakan the Dwarf:** ¡Entonces deja de gritar!
    - (initial)
  - [Choice]: ¡Adiós!
    - **Player:** ¡Adiós!

#### Después Entre una Roca...

- **Player:** ¿Cómo estás, Dondakan?
- **Dondakan the Dwarf:** ¡Oh, muy bien, muy bien! ¡Este oro ciertamente está creando un flujo constante de ingresos para mí! Después de que la empresa se lleve parte del recorte, por supuesto.
- [Menu]: Seleccione una opción{{anchor|normal}}
  - [Choice]: ¿Puedes dispararme contra la roca otra vez?
    - **Player:** ¿Puedes dispararme contra la roca otra vez?
    - (Condition: With golden helmet equipped:)
      - **Dondakan the Dwarf:** Por supuesto, un segundo, déjame ajustar mi cañón nuevamente.
    - (Condition: Without golden helmet equipped:)
      - **Dondakan the Dwarf:** Necesitas usar ese casco dorado... a menos que quieras abrirte el cráneo contra la roca.
  - [Choice]: ¿Estás vendiendo esas botas tuyas?
    - **Player:** ¿Estás vendiendo esas botas tuyas?
    - **Dondakan the Dwarf:** ¿Qué? ¿Te refieres a estas botas de granito?
    - **Player:** Sí, ¡estaría encantado de pagar bastante dinero por ellos!
    - **Dondakan the Dwarf:** Jaja, apuesto que lo harías, ¡apuesto a que lo harías!
    - **Dondakan the Dwarf:** Pero ya no necesito el dinero, ¡esta piedra está generando mucho! Además, ahora les tengo bastante cariño... ¡las mejores botas que he tenido!
    - [Menu]: Selecciona una opción
      - [Choice]: Ah por favor...
        - **Player:** Oh, por favor...
        - **Dondakan the Dwarf:** No, no los venderé.
      - [Choice]: ¿Bonita por favor?
        - **Player:** ¿Bonita, por favor?
        - **Dondakan the Dwarf:** ¡No!
        - **Player:** ¡¡¡Oh, vamos!!!
        - **Dondakan the Dwarf:** Bueno...
        - **Player:** ¿Sí?
        - **Dondakan the Dwarf:** ¿Cuánto oro estarías dispuesto a pagar por él? No es que esté vendiendo mis botas, solo tengo curiosidad.
        - {{tinput|Enter amount:}}
          - (Condition: If 0-999 is entered:)
            - **Dondakan the Dwarf:** ¿Qué? ¿Estás intentando estafar al viejo Dondakan? ¿Quieres que venda estas botas por un mísero [número] coins?
            - **Dondakan the Dwarf:** No los venderé de todos modos.
          - (Condition: If 1,000-74,999 is entered:)
            - **Dondakan the Dwarf:** Si estuviera vendiendo mis botas de granito, lo cual claramente no es así, ciertamente no aceptaría ni un simple [número] coins por ellas.
          - (Condition: If 75,000 or more is entered:)
            - **Dondakan the Dwarf:** Jaja, ¡buen intento con Player!
            - **Dondakan the Dwarf:** Lástima que no vendo mis botas, ni por ningún precio ni por ningún artículo. ¡Solo quiero ver qué tan alto llegarías!
            - **Player:** Bah, muchas gracias.
          - (Condition: If a figure greater than the amount in money pouch is entered:)
            - **Dondakan the Dwarf:** Oye, eso es bastante dinero. Que no tienes contigo. Bueno, de todos modos no iba a vender mis botas.
      - [Choice]: No importa, ya no los quiero.
        - **Player:** No importa, ya no los quiero.
        - **Dondakan the Dwarf:** Genial, porque no quiero venderlos.
        - **Player:** Está bien.
        - **Dondakan the Dwarf:** Correcto.
  - [Choice]: Eso es genial, pero tengo que irme ahora.
    - **Player:** Eso es genial, pero tengo que irme ahora.
    - **Dondakan the Dwarf:** ¡Vuelve cuando quieras!

#### Después de la primogenitura de los enanos


##### Si Veldaban es el rey

- **Dondakan the Dwarf:** Supongo que debería estar orgulloso de lo incorruptible que es mi hijo... pero ¿le mataría usar sus poderes reales para ayudar al negocio de su padre?
- **Dondakan the Dwarf:** Oh, bueno... Supongo que esta roca todavía me proporciona un flujo constante de ingresos. Después de que la empresa reciba su parte, por supuesto.
- (continuea|normal)

##### Si Veldaban abdicó

- **Dondakan the Dwarf:** ¡Así que mi hijo llegó a ser rey y luego renunció! Es como siempre he dicho: ¡la generación actual carece de ambición!
- **Dondakan the Dwarf:** ¡Sus poderes reales podrían habernos hecho a ambos tan ricos!
- (continuea|normal)

##### Si Veldaban está muerto

- **Dondakan the Dwarf:** Ojalá hubiera pasado más tiempo con Veldaban cuando estaba vivo, en lugar de estar obsesionado con esta roca. Mi único hijo y yo lo ignoramos porque se convirtió en Black Guard en lugar de minero.
- **Dondakan the Dwarf:** Desde que me ayudaste a extraer la roca, he tenido todas las riquezas que pude desear... pero ni todo el oro del mundo traerá a mi hijo de vuelta.
- [Menu]: Selecciona una opción
  - [Choice]: Lamento tu pérdida.
    - **Player:** Lamento tu pérdida.
    - **Dondakan the Dwarf:** Gracias.
  - [Choice]: ¿Puedes dispararme contra la roca otra vez?
    - (arriba)
  - [Choice]: ¿Estás vendiendo esas botas tuyas?
    - (arriba)
  - [Choice]: Eso es genial, pero tengo que irme.
    - (arriba)
