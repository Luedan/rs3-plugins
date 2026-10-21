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
        - (Condition: Si el player no tiene viales viables de pociones para decantar:)
          - **Clan representative:** Lo siento, no sé cómo decantar nada de lo que llevas.
        - (Condition: Si el player no tiene espacio backpack:)
          - [Buscando...]
          - **Clan representative:** Tu inventario está demasiado lleno para que pueda hacer algo por ti.
        - (Condition: Si el player tiene viales viables de pociones para decantar:)
          - [Buscando...]
          - (Condition: Si se compraron viales adicionales en clan representative:)
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
    - (Condition: Si el player no tiene frascos viables de pociones para decantar:)
      - **Clan representative:** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener 2 matraces que no estén completamente llenos!
  - [Choice]: Convertir viales en matraces
    - (Condition: Si el player tiene matraces vacíos en backpack:)
      - **Clan representative:** mira lo que tienes. Decantaré los viales de poción y todos los frascos con hasta 4 dosis en frascos de 6 dosis. Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos.
      - (Action: El clan representative decanta tantas pociones como puede hasta llenar frascos de 6 dosis.)
      - **Clan representative:** Aquí tienes. ¡Eso es lo mejor que puedo hacer!
    - (Condition: Si el player no tiene matraces vacíos en backpack:)
      - **Clan representative:** Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos. Puedes traérmelos anotados o sin anotaciones.
  - [Choice]: Convertir matraces en viales
    - (Condition: Si el player tiene frascos de pociones para decantar en viales:)
      - **Clan representative:** Por supuesto. Creo que puedo utilizar los matraces, así que te daré los viales gratis.
      - (Action: El clan representative decanta tantas pociones como puede en viales destacados.)
      - **Clan representative:** Ahí lo tienes, ¡eso es lo mejor que puedo hacer!
    - (Condition: Si el player no tiene frascos viables de pociones para decantar:)
      - **Clan representative:** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener al menos 1 matraz!
  - [Choice]: combinar medusas
    - (Condition: Si el player tiene medusas viables para combinar:)
      - (Action: Las medusas se combinan siempre que sea posible.)
      - **Clan representative:** Ahí lo tienes.
    - (Condition: Si el player no tiene medusas viables para combinar:)
      - **Clan representative:** Lo siento, no sé cómo combinar nada de lo que llevas.
  - [Choice]: Cancelar
    - (end)

### Challenge gems option

- [Menu]: ¿Cuántos te gustaría comprar?
  - [Choice]: Uno.
    - ((Se abre la interfaz de compra de Challenge Gem (x1) por 10 RuneCoins))
  - [Choice]: Tres.
    - ((Se abre la interfaz de compra de Challenge Gem (x3) por 25 RuneCoins))
  - [Choice]: Seis.
    - ((Se abre la interfaz de compra de Challenge Gem (x6) por 40 RuneCoins))
  - [Choice]: Ninguno, cambié de opinión.
    - **Player:** Ninguno, he cambiado de opinión.
    - **Clan representative:** No temas, ahora sabes dónde encontrarlos. ¿Algo más?
    - (initial)
