# Arhein

- **Original Wiki Page**: [Transcript:Arhein](https://runescape.wiki/w/Transcript%3AArhein)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{transcript npc|Arhein}}

### Standard dialogue

- **Arhein:** ¡Hola! ¿Le gustaría negociar? ¡Tengo una variedad de productos a la venta, así como un suministro especial de piñas y algas!
- **Seleccione una opción**
  - [Choice]: Comerciemos.
    - **Player:** Intercambiemos.
    - (Action: abre=Tienda de Arhein)
  - [Choice]: ¿Es ese tu barco?
    - **Player:** ¿Es ese tu barco?
    - **Arhein:** Sí, lo uso para realizar entregas a mis clientes en toda la costa. Estas cajas aquí están todas listas para mi próximo viaje.
    - **Seleccione una opción**
      - [Choice]: ¿A dónde entregas?
        - **Player:** ¿A dónde hacen entregas?
        - **Arhein:** Oh, varios lugares a lo largo de la costa. Principalmente Karamja y Port Sarim.
        - **Seleccione una opción**
          - [Choice]: ¿Supongo que no podría conseguir que me lleven a ninguna parte?
            - **Player:** Supongo que no podría conseguir que me lleven a ninguna parte.
            - **Arhein:** Lo siento amigo, pero me temo que todavía no estoy listo para zarpar.
            - **Arhein:** Estoy esperando una gran entrega de velas que necesito entregar a lo largo de la costa.
          - [Choice]: Bueno, buena suerte con tu negocio.
            - **Player:** Bueno, buena suerte con tu negocio.
            - **Arhein:** ¡Gracias amigo!
      - [Choice]: ¿Eres rico entonces?
        - **Player:** ¿Eres rico entonces?
        - **Arhein:** El negocio va razonablemente bien... No diría que soy el comerciante más rico de todos los tiempos, pero me va bastante bien considerando todo.
  - [Choice]: No, gracias.
    - **Player:** No, gracias.

### Pineapples option

- ((Si el player no ha comprado todas las existencias de piñas de Arhein:))
  - **Arhein:** Tengo [#] [pineapple/pineapples] en stock, a 2 coins cada uno. ¿Cuantos quisieras?
  - ((Si el player no tiene al menos 2 coins:))
    - **Player:** Lo siento, no puedo permitirme ninguno.
    - (end)
  - Arhein tiene [#] [pineapple/pineapples]. Puedes permitirte [#].
    - ((A Player se le solicita un número))
  - ((Si se ingresó un número distinto de cero:))
    - (receives=noted pineapples)
    - {{tbox|pic=Pineapple detail.png|Arhein gives you [#] [pineapple/pineapples].}}
- ((Si a Arhein no le quedan piñas:))
  - **Arhein:** Se me acabaron las piñas. Vuelve mañana y debería tener un poco más.

### Seaweed option

- ((Si el player no ha comprado todas las existencias de algas de Arhein:))
  - **Arhein:** Tengo algas [#] en este momento y cuestan 2 coins cada una. ¿Cuantos quisieras?
  - ((Si el player no tiene al menos 2 coins:))
    - **Player:** Lo siento, no puedo permitirme ninguno.
    - (end)
  - Arhein tiene algas [#]. Puedes permitirte [#].
    - ((A Player se le solicita un número))
  - (receives=noted seaweed)
  - {{tbox|pic=Seaweed detail.png|Arhein gives you [#] seaweed.}}
- ((Si a Arhein no le quedan algas:))
  - **Arhein:** Me he quedado sin algas. Vuelve mañana y debería tener un poco más.

### Treasure Trails

- (removes=the old clue scroll (easy))
- ((Si el rastro continúa:))
  - (receives=a new clue scroll (easy))
  - {{tbox|pic=Clue scroll (easy) detail.png|Arhein has given you another clue scroll!}}
- ((Si el sendero termina:))
  - (receives=reward casket (easy))
  - {{tbox|pic=Casket (easy) detail.png|You've found a casket!}}
- **Arhein:** ¡Cosas increíbles!
