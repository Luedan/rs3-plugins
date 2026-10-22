# Bartender (Jolly Boar Inn)

- **Original Wiki Page**: [Transcript:Bartender (Jolly Boar Inn)](https://runescape.wiki/w/Transcript%3ABartender%20%28Jolly%20Boar%20Inn%29)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### Normalmente

- **Barman:** ¿Puedo ayudarte?
- [Menu]: Selecciona una opción
  - [Choice]: Tomaré una cerveza, por favor.
    - **Player:** Tomaré una pinta de cerveza, por favor.
    - **Bartender:** Ok, serán dos coins, por favor.
    - (Condition: If the player has enough money:)
      - (removes=2 coins) (receives=beer)
      - **Player:** Gracias, camarero.
    - (Condition: If the player does not have enough money:)
      - No puedes permitirte eso.
      - **Bartender:** ¡Dije 2 coins! ¡No tienes 2 coins!
      - **Player:** Lo siento, volveré otro día.
  - [Choice]: ¿Alguna pista sobre dónde puedo ir de aventuras?
    - **Player:** ¿Alguna pista sobre dónde puedo ir de aventuras?
    - **Camarero:** Oh, ahora. Déjame ver...
    - **Bartender:** Bueno, ahí están las alcantarillas Varrock. Hay historias de horrores indecibles que salen de noche y roban bebés de las casas.
    - **Player:** ¡Suena perfecto! ¿Dónde está la entrada?
    - **Bartender:** Está justo al este del palacio.
  - [Choice]: ¿Escuchaste algún buen chisme?
    - **Player:** ¿Has oído algún chisme?
    - **Camarero:** No estoy muy al tanto de los chismes aquí. He oído que el barman del Blue Moon Inn se ha vuelto un poco loco, sigue afirmando que es parte de algo llamado juego de computadora.
    - **Bartender:** Lo que eso significa, no lo sé. Aunque probablemente ya sean noticias viejas.

#### Con un barril de hidromiel antes de realizar una entrega en Jolly Boar Inn durante el evento The Need for Mead

- **Barman:** ¿Puedo ayudarte?
- **Player:** Leslie me envió aquí para preguntarme si podía darme su opinión sobre su último lote de hidromiel.
- **Bartender:** ¡Por Leslie, felizmente!
- (removes=keg of mead) (receives=50 nectar)
- (ver|néctar)
- ((Shown in a pop-up:))
  - (Pop-up: You find 50 x Nectar as you hand over the keg of mead.|colour=#00FF00)
  - (continue)
- **Player:** No esperaba que te lo bebieras todo.
- **Bartender:** Es la mejor manera.
- **Player:** De alguna manera lo dudo.
- **Bartender:** ¡Eso estuvo bastante bien!
- **Bartender:** La intensidad es la adecuada. ¡El sabor es bueno pero sabe demasiado débil!
- **Bartender:** Sé que siempre buscan la perfección. ¡Esto es bueno, pero no perfecto!
- **Player:** Gracias, se lo haré saber.
