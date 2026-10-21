# Rasolo

- **Original Wiki Page**: [Transcript:Rasolo](https://runescape.wiki/w/Transcript%3ARasolo)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Desert Treasure

- **Rasolo:** Saludos amigo. Soy Rasolo, el famoso comerciante. ¿Le importaría ver mis productos?
- [Menu]: Selecciona una opción
  - [Choice]: si
    - (opens=Rasolo the Wandering Merchant)
  - [Choice]: No
    - **Player:** No, en realidad no.
    - **Rasolo:** Como desees. Viajaré a donde me lleve el negocio.

### After Desert Treasure

- **Rasolo:** Muchas gracias por devolverme mi reliquia, aventurero. <br>¿Quieres comprar algo?
- [Menu]: Selecciona una opción
  - [Choice]: si
    - (opens=Rasolo the Wandering Merchant)
  - [Choice]: No
    - **Player:** No, en realidad no.
    - **Rasolo:** Como desees. Viajaré a donde me lleve el negocio.
  - [Choice]: Perdí ese anillo que me diste...
    - **Player:** Perdí ese anillo que me diste...
    - (Condition: Si el player realmente ha perdido el anillo de visibilidad:)
      - (receives=ring of visibility)
      - **Rasolo:** Entonces, por supuesto, toma otro. ¡Sólo un comerciante tonto regalaría sus únicas acciones!
    - (Condition: Si el player todavía tiene el anillo de visibilidad:)
      - **Rasolo:** ¿Estás seguro? ya no lo tengo...
