# Bartender (Blue Moon Inn)

- **Original Wiki Page**: [Transcript:Bartender (Blue Moon Inn)](https://runescape.wiki/w/Transcript%3ABartender%20%28Blue%20Moon%20Inn%29)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Varrock


#### Normalmente

- **Bartender:** ¿En qué puedo ayudarte?
- (Condition: Con un construction contract:)
  - [Menu]: Selecciona una opción
    - [Choice]: Preguntar por contracts
      - [Menu]: Selecciona una opción
        - [Choice]: ¿Qué necesitas reparar?
          - **Bartender:** Déjame ver, ahora mismo necesito que repares el siguiente pieces of furniture.
          - **Camarero:** [Furniture 1], [Furniture 2], [Furniture 3], [Furniture 4], [Furniture 5]
          - (previous)
        - [Choice]: ¿Qué materiales necesito?
          - **Bartender:** Necesitas: Planks x [número], Steel nails x [número]
          - (previous)
        - [Choice]: [Leave]
          - (end)
    - [Choice]: pregunta sobre otra cosa
      - (below|standard)
- (Condition: De lo contrario:)
  - {{anchor|standard}}[Menú]: Seleccione una opción
    - [Choice]: Un vaso de su mejor cerveza, por favor.
      - **Player:** Un vaso de tu mejor cerveza, por favor.
      - **Bartender:** No hay problema. Serán 2 coins.
      - (Condition: Si el player tiene suficiente dinero:)
        - (removes=2 coins) (receives=beer)
        - **Player:** Gracias, camarero.
      - (Condition: Si el player no tiene suficiente dinero:)
        - No puedes permitirte eso.
        - **Bartender:** ¡Dije 2 coins! ¡No tienes 2 coins!
        - **Player:** Lo siento, volveré otro día.
    - [Choice]: ¿Puedes recomendar dónde un aventurero podría hacer [his/her] fortuna?
      - **Player:** ¿Puedes recomendar dónde un aventurero podría hacer [his/her] fortuna?
      - **Bartender:** Oh, no sé si debería dar información, hace que el juego de computadora sea demasiado fácil.
      - [Menu]: Selecciona una opción
        - [Choice]: Ah, bueno...
          - **Player:** Ah, bueno...
        - [Choice]: ¿Juego de computadora? ¿De qué estás hablando?
          - **Player:** ¿Juego de ordenador? ¿De qué estás hablando?
          - **Bartender:** Este mundo que nos rodea... es un juego de computadora... llamado RuneScape.
          - **Player:** No, todavía no entiendo de qué estás hablando. ¿Qué es una computadora?
          - **Bartender:** Es una especie de caja mágica, que puede hacer todo tipo de cosas.
          - **Player:** Me rindo. ¡Obviamente estás completamente loco!
        - [Choice]: ¿Sólo una pequeña pista?
          - **Player:** ¿Solo una pequeña pista?
          - **Bartender:** Ve y habla con el bartender del Jolly Boar Inn, no parece importarle dar pistas.
    - [Choice]: ¿Sabes dónde puedo conseguir buenos equipos?
      - **Player:** ¿Sabes dónde puedo conseguir buenos equipos?
      - **Bartender:** Bueno, está la tienda de espadas al otro lado de la calle, o también hay todo tipo de tiendas alrededor del mercado.

#### Con el pergamino de pistas que requiere hablar con él.

- (removes=the old clue scroll (easy))
- ((Si el rastro continúa:))
  - (receives=a new clue scroll (easy))
  - [¡El barman te ha dado tu siguiente pergamino de pistas!]
  - (continue)
- ((Si el sendero termina:))
  - (receives=reward casket (easy))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Barman:** Perfecto.

#### Con un barril de hidromiel antes de realizar una entrega en Blue Moon Inn durante el evento The Need for Mead

- **Bartender:** ¿En qué puedo ayudarte?
- **Player:** Me enviaron aquí para ver si estaría interesado en probar y dar su opinión sobre este hidromiel. Tengo un barril entero para ti.
- **Bartender:** ¿Más hidromiel de Leslie? ¡Simplemente no se dan por vencidos!
- **Player:** Sí, ¿esperaban que tuvieras comentarios constructivos sobre este último lote?
- **Bartender:** Déjame intentarlo.
- (removes=keg of mead) (receives=50 nectar)
- (ver|néctar)
- ((Se muestra en una ventana emergente:))
  - (Ventana emergente: encontrarás 50 x néctar cuando entregas el barril de hidromiel.|color=#00FF00)
  - (continue)
- **Camarero:** Hmm...
- **Bartender:** Mejor que el último lote...
- **Bartender:** Aunque algo no está del todo bien...
- **Bartender:** Sí, hay un regusto desagradable. No almacenaría esto.
- **Player:** Está bien, se lo haré saber. Gracias.

### In New Varrock

- **Bartender:** ¿En qué puedo ayudarte?
- [Menu]: Selecciona una opción
  - [Choice]: Un vaso de tu mejor cerveza.
    - **Bartender:** Son dos zemomarks.
    - (Condition: Si el player no tiene suficientes zemomarks:)
      - **Bartender:** Sin dinero, sin cerveza.
      - (initial)
    - (Condition: Si el player tiene suficientes zemomarks:)
      - (removes=two zemomarks) (receives=beer)
      - **Barman:** Disfruten.
      - (initial)
  - [Choice]: ¿Dónde puede un aventurero hacer fortuna aquí?
    - **Bartender:** No.<br>Ya no.<br>No quedan aventureros.
    - (initial)
  - [Choice]: ¿Dónde puedo conseguir algún buen equipo aquí?
    - **Bartender:** Tiendas.<br>Carteristas.
    - (initial)
  - [Choice]: Nada, gracias.
  - (end)
