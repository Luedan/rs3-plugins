# Clan representative

- **Original Wiki Page**: [Transcript:Clan representative](https://runescape.wiki/w/Transcript%3AClan%20representative)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to option

- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Clan representative:** Soy uno de los representantes del clan War. Pidió ayuda con algunos de sus pasatiempos menos centrados en la batalla, por lo que los jinetes me enviaron para ayudarlo.
    - **Player:** ¿Qué puedes hacer?
    - **Clan representative:** Bueno, soy hábil con las pociones, así que puedo ayudarte a decantar cualquier poción o frasco que tengas.
    - **Clan representative:** War también me dio acceso a su suministro de Challenge Gems. Puedo venderte algunos, si estás interesado.
    - **Clan representative:** ¿Hubo algo más?
    - (initial)
  - [Choice]: ¿Puedes decantarme algunas pociones o medusas?
    - (below|Decant option)
  - [Choice]: ¿Puedes venderme algunas gemas de desafío?
    - **Player:** ¿Puedes venderme algunas gemas de desafío?
    - **Clan representative:** ¡Por supuesto! ¿Cuantos quieres?
    - (continue|Challenge gems option)
  - [Choice]: Adiós.
    - **Player:** ¡Adiós!
    - **Clan representative:** ¡Sigue luchando!

### Decant option

- [Menu]: Selecciona una opción
  - [Choice]: Decantar viales
    - [Menu]: ¿En cuántas dosis quieres decantar?
      - [Choice]: una dosis
        - (Condition: If the player has no viable vials of potions to decant:)
          - **Clan representative:** Lo siento, no sé cómo decantar nada de lo que llevas.
        - (Condition: If the player has no backpack space:)
          - [Buscando...]
          - **Clan representative:** Tu inventario está demasiado lleno para que pueda hacer algo por ti.
        - (Condition: If the player has viable vials of potions to decant:)
          - [Buscando...]
          - (Condition: If additional vials were purchased from the clan representative:)
            - (receives=vials) (removes=two coins for each vial)
            - (continue)
          - **Clan representative:** Ahí lo tienes, amigo.
      - [Choice]: Dos dosis
        - (above|decant-vials)
      - [Choice]: Tres dosis
        - (above|decant-vials)
      - [Choice]: Cuatro dosis
        - (above|decant-vials)
  - [Choice]: Decantar matraces
      - **Clan representative:** Veamos qué tienes. Decantaré sus frascos de poción nuevamente en 6 frascos dosificados. Puedo hacer uso de los frascos, así que los aceptaré como pago.
      - (Action: El clan representative decanta tantas como puede hasta llenar frascos de 6 dosis.)
      - **Clan representative:** Aquí tienes. ¡Eso es lo mejor que puedo hacer! Si los matraces no se ven muy diferentes, les di un clean{{Sic}}
    - (Condition: If the player has no viable flasks of potions to decant:)
      - **Clan representative:** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener 2 matraces que no estén completamente llenos!
  - [Choice]: Convertir viales en matraces
    - (Condition: If the player has empty flasks in backpack:)
      - **Clan representative:** mira lo que tienes. Decantaré los viales de poción y todos los frascos con hasta 4 dosis en frascos de 6 dosis. Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos.
      - (Action: El clan representative decanta tantas pociones como puede hasta llenar frascos de 6 dosis.)
      - **Clan representative:** Aquí tienes. ¡Eso es lo mejor que puedo hacer!
    - (Condition: If the player has no empty flasks in backpack:)
      - **Clan representative:** Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos. Puedes traérmelos anotados o sin anotaciones.
  - [Choice]: Convertir matraces en viales
    - (Condition: If the player has flasks of potions to decant to vials:)
      - **Clan representative:** Por supuesto. Creo que puedo utilizar los matraces, así que te daré los viales gratis.
      - (Action: El clan representative decanta tantas pociones como puede en viales destacados.)
      - **Clan representative:** Ahí lo tienes, ¡eso es lo mejor que puedo hacer!
    - (Condition: If the player has no viable flasks of potions to decant:)
      - **Clan representative:** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener al menos 1 matraz!
  - [Choice]: combinar medusas
    - (Condition: If the player has viable jellyfish to combine:)
      - (Action: Las medusas se combinan siempre que sea posible.)
      - **Clan representative:** Ahí lo tienes.
    - (Condition: If the player has no viable jellyfish to combine:)
      - **Clan representative:** Lo siento, no sé cómo combinar nada de lo que llevas.
  - [Choice]: Cancelar
    - (end)

### Challenge gems option

- [Menu]: ¿Cuántos te gustaría comprar?
  - [Choice]: Uno.
    - ((Purchase interface opens up for Challenge Gem (x1) for 10 RuneCoins))
  - [Choice]: Tres.
    - ((Purchase interface opens up for Challenge Gem (x3) for 25 RuneCoins))
  - [Choice]: Seis.
    - ((Purchase interface opens up for Challenge Gem (x6) for 40 RuneCoins))
  - [Choice]: Ninguno, cambié de opinión.
    - **Player:** Ninguno, he cambiado de opinión.
    - **Clan representative:** No temas, ahora sabes dónde encontrarlos. ¿Algo más?
    - (initial)
