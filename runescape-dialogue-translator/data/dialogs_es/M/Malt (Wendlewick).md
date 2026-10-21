# Malt (Wendlewick)

- **Original Wiki Page**: [Transcript:Malt (Wendlewick)](https://runescape.wiki/w/Transcript%3AMalt%20%28Wendlewick%29)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to

- **Malta:** Hola. ¿Necesitas ayuda con la elaboración de cerveza?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Cómo preparo cervezas?
    - **Player:** ¿Cómo preparo cervezas?
    - **Malta:** Bueno, primero debes llenar la tina con agua; dos cubos llenos deberían ser suficientes.
    - **Malta:** Luego tendrás que poner dos puñados de malta de cebada; por cierto, es cebada cocinada en la estufa.
    - **Malta:** Después de eso, agregarás el ingrediente principal; esto decidirá qué cerveza estás preparando.
    - **Malta:** Por último, viertes una olla llena de levadura de cerveza, lo que hará que comience a fermentar. ¡Entonces todo lo que tienes que hacer es esperar las cosas buenas!
    - **Player:** ¿Cómo puedo obtener levadura de cerveza?
    - **Malta:** ¡Pregúntame! Si me traes una olla puedo llenarla con levadura por 25 coins.
    - (previous)
  - [Choice]: ¿Cómo preparo sidra?
    - **Player:** ¿Cómo preparo sidra?
    - **Malta:** Primero, necesitarás algunas manzanas. Las triturarás con este prensador de sidra: con cuatro manzanas se obtiene un cubo lleno de puré de manzana. Coge cuatro cubos de papilla y llena la tina.
    - **Malta:** Después de eso, viertes una olla llena de levadura de cerveza, lo que hará que comience a fermentar. ¡Entonces todo lo que tienes que hacer es esperar las cosas buenas!
    - **Player:** ¿Cómo puedo obtener levadura de cerveza?
    - **Malta:** ¡Pregúntame! Si me traes una olla puedo llenarla con levadura por 25 coins.
    - (previous)
  - [Choice]: ¿Qué hago una vez que mi bebida ha madurado?
    - **Player:** ¿Qué hago una vez que mi bebida ha madurado?
    - **Malta:** Bueno, una vez que tengas una tina llena de cosas buenas, simplemente gira la válvula y tu barril se llenará con ocho rosas de la bebida que hayas elegido.
    - **Malta:** Una vez que el barril esté lleno, puedes escurrirlo en un vaso de cerveza vacío o en un barril de calquat.
    - (previous)
  - [Choice]: ¿Puedes venderme levadura de cerveza?
    - **Player:** ¿Puedes venderme levadura de cerveza?
    - (continue|Buy yeast)
  - [Choice]: Adiós.
    - **Player:** Adiós.

### Buy yeast


#### Sin 25 coins o un bote vacío

- **Malta:** Necesitarás un recipiente para poner la levadura y 25 coins para pagarme.

#### Con 25 coins pero sin bote vacío

- **Malta:** Necesitarás un recipiente para poner la levadura.

#### Con el bote vacío pero sin 25 coins

- **Malta:** Necesitarás 25 coins para pagarme por la levadura.

#### Con 25 coins y un bote vacío

- [Menu]: ¿Llena tu olla con años por 25 coins?
  - [Choice]: Llena tu olla
    - (removes=25 coins and empty pot) (receives=ale yeast)
  - [Choice]: No importa.
    - (end)
