# Captain Shanks

- **Original Wiki Page**: [Transcript:Captain Shanks](https://runescape.wiki/w/Transcript%3ACaptain%20Shanks)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### After completing Shilo Village

- **Captain Shanks:** ¡Hola compañero de barco! Navego hasta el puerto de Khazard y hasta Port Sarim. ¿A dónde estás atado?
- **Player:** Hmm, estoy interesado en un viaje en barco.
- (Condition: Without a ship ticket:)
  - **Captain Shanks:** Veo que no tienes billete para el barco, mi colega normalmente sólo los vende en Shilo village. Pero podría venderte uno por un pequeño cargo adicional. ¿Diremos [26-45] piezas de oro?
    - [Menu]: Compra un billete para piezas de oro [26-45]
      - [Choice]: Sí, compraré un billete para el barco.
        - **Player:** Sí, compraré un billete para el barco.
        - **Captain Shanks:** Es un buen negocio y no hay error. Aquí tienes, viejo compañero, aquí tienes tu billete.
        - (receives=Ship ticket) (removes=coins)
        - **Captain Shanks:** Ok, ahora tienes tu billete, ¿quieres navegar a algún lugar?
        - [Menu]: Captain Shanks pregunta: '¿Quieres navegar a algún lugar?'
          - [Choice]: Puerto Khazard, por favor.
            - **Player:** Puerto Khazard, por favor.{{anchor|Khazard}}
            - (removes=Ship ticket)
            - (el player viaja en el barco y llega a Port Khazard, cerca de Tindel Marchant.)
            - **Captain Shanks:** Muy bien, entonces mi viejo compañero de barco, tomaré tu boleto y luego zarparemos.
          - [Choice]: Port Sarim por favor.
            - **Player:** Port Sarim por favor.{{anchor|Sarim}}
            - **Captain Shanks:** Muy bien, entonces mi viejo compañero de barco, tomaré tu boleto y luego zarparemos.
            - (removes=Ship ticket)
            - (el player viaja en el barco y llega a Port Sarim, cerca de los monjes de Entrana.)
          - [Choice]: En ningún lado por el momento gracias.
            - **Player:** En ninguna parte por el momento, gracias.
            - **Captain Shanks:** Muy bien, entonces viejo compañero de barco. Avísame si cambias de opinión.
      - [Choice]: No gracias, no sólo por el momento.
        - **Player:** No, gracias, no sólo por el momento.
        - **Captain Shanks:** Muy bien, viejo compañero de barco, vuelve si cambias de opinión ahora.
- (Condition: With a ship ticket:)
  - [Menu]: Captain Shanks pregunta: "¿Adónde vas?"
    - [Choice]: Puerto Khazard, por favor.
      - (continuea|Khazard)
    - [Choice]: Port Sarim por favor.
      - (continuea|Sarim)
    - [Choice]: En ningún lado por el momento gracias.
      - **Player:** En ninguna parte por el momento, gracias.
      - **Captain Shanks:** Muy bien, entonces viejo compañero de barco. Avísame si cambias de opinión.
