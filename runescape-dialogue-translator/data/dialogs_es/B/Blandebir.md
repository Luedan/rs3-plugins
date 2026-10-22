# Blandebir

- **Original Wiki Page**: [Transcript:Blandebir](https://runescape.wiki/w/Transcript%3ABlandebir)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Laughing Miner pub in Keldagrim

- **Blandebir:** Hola. ¿Necesitas ayuda con la elaboración de cerveza?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Cómo preparo cervezas?
    - **Player:** ¿Cómo preparo cervezas?
    - **Blandebir:** Bueno, primero que nada debes llenar la tina con agua; dos cubos llenos deberían ser suficientes. Luego tendrás que añadir dos puñados de malta de cebada (por cierto, cebada tostada).
    - **Blandebir:** Después de eso, pondrás el ingrediente principal; esto decidirá qué cerveza estás preparando. Debería haber algunas buenas guías con recetas.
    - **Blandebir:** Por último, viertes una olla llena de levadura de cerveza, lo que hará que comience a fermentar. Entonces todo lo que tienes que hacer es esperar las cosas buenas.
    - (initial)
  - [Choice]: ¿Cómo preparo sidra?
    - **Player:** ¿Cómo preparo sidra?
    - **Blandebir:** Primero necesitarás algunas manzanas. Tendrás que triturarlas con este prensador de sidra: con cuatro manzanas se obtiene un cubo lleno de puré de manzana. Coge cuatro cubos de papilla y llena la tina.
    - **Blandebir:** Después de eso, viertes una olla llena de levadura de cerveza, lo que hará que comience a fermentar. Entonces todo lo que tienes que hacer es esperar las cosas buenas.
    - (initial)
  - [Choice]: ¿Qué hago una vez que mi cerveza ha madurado?
    - **Player:**¿Qué hago una vez que mi cerveza ha madurado?
    - **Blandebir:** Bueno, una vez que tengas una tina llena de cosas buenas, simplemente gira la válvula y tu barril se llenará con ocho pintas de la bebida que hayas elegido. Eso sí, ten en cuenta que es un barril vacío.
    - (initial)
  - [Choice]: ¿Puedes venderme levadura de cerveza?
    - **Player:**¿Puedes venderme levadura de cerveza?
    - (Condition: With no empty pots in backpack:)
      - **Blandebir:** Me temo que necesitarás un recipiente para poner la levadura.
    - (Condition: With less than 25 coins:)
      - **Blandebir:** Me temo que necesitarás 25 coins para pagarme por la levadura.
    - (Condition: With empty pots in backpack:)
      - **Blandebir:** Querré 25 coins por cada bote de levadura.
      - [Menu]: ¿Llenar una olla con levadura por 25 coins?
        - [Choice]: Llena tu olla
          - (removes=one pot and 25 coins) (receives=one pot of ale yeast)
          - (initial)
        - [Choice]: cond=With multiple pots in backpack|Llena todas tus ollas
          - (Condition: With enough money for only some pots:)
            - (removes=pots and 25 coins for each pot) (receives=one pot of ale yeast for each pot)
            - No puedes permitirte eso.
            - **Blandebir:** Me temo que parece que te has quedado sin dinero. ¿Puedo ayudarte con algo más?
            - (initial)
          - (Condition: With enough money for all pots:)
            - (removes=pots and 25 coins for each pot) (receives=one pot of ale yeast for each pot)
            - (initial)
        - [Choice]: Pregunta por otra cosa.
          - (initial)
  - [Choice]: ¡Nada, gracias!
    - **Player:** ¡Nada, gracias!
