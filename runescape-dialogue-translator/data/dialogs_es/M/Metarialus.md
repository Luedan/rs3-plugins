# Metarialus

- **Original Wiki Page**: [Transcript:Metarialus](https://runescape.wiki/w/Transcript%3AMetarialus)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Metarialus:** Hola. ¿Necesitas ayuda con la elaboración de cerveza?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Cómo preparo cervezas?
    - **Player:** ¿Cómo preparo cervezas?
    - **Metarialus:** Bueno, primero que nada debes llenar la tina con agua; dos cubos llenos deberían ser suficientes. Luego tendrás que añadir dos puñados de malta de cebada (por cierto, cebada tostada).
    - **Metarialus:** Después de eso, pondrás el ingrediente principal; esto decidirá qué cerveza estás preparando. Debería haber algunas buenas guías con recetas.
    - **Metarialus:** Por último, viertes una olla llena de levadura de cerveza, lo que hará que comience a fermentar. Entonces todo lo que tienes que hacer es esperar las cosas buenas.
    - (initial)
  - [Choice]: ¿Cómo preparo sidra?
    - **Player:** ¿Cómo preparo sidra?
    - **Metarialus:** Primero necesitarás algunas manzanas. Tendrás que triturarlas con este prensador de sidra: con cuatro manzanas se obtiene un cubo lleno de puré de manzana. Coge cuatro cubos de papilla y llena la tina.
    - **Metarialus:** Después de eso, viertes una olla llena de levadura de cerveza, lo que hará que comience a fermentar. Entonces todo lo que tienes que hacer es esperar las cosas buenas.
    - (initial)
  - [Choice]: ¿Qué hago una vez que mi cerveza ha madurado?
    - **Player:** ¿Qué hago una vez que mi cerveza haya madurado?
    - **Metarialus:** Bueno, una vez que tengas una tina llena de cosas buenas, simplemente gira la válvula y tu barril se llenará con ocho pintas de la bebida que hayas elegido. Eso sí, ten en cuenta que es un barril vacío.
    - (initial)
  - [Choice]: ¿Puedes venderme levadura de cerveza?
    - **Player:** ¿Puedes venderme levadura de cerveza?
    - *(Si el player no tiene el bote vacío:)*
      - **Metarialus:** Me temo que necesitarás un recipiente para poner la levadura.
    - *(Si el player tiene el bote vacío:)*
      - **Metarialus:** Querré 5 ectotokens por cada bote de levadura.
      - '''¿Llenar tu olla con levadura por 5 ectotokens?
        - [Choice]: Llena tu olla
          - (removes=empty pot and five ecto-tokens)
          - (receives=ale yeast)
          - **Metarialus:** ¿Puedo ayudarte con algo más?
          - (initial)
        - [Choice]: pregunta sobre otra cosa
          - (initial)
  - [Choice]: ¡Nada, gracias!
    - **Player:** ¡Nada, gracias!
