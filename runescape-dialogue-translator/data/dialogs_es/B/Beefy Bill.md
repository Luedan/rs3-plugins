# Beefy Bill

- **Original Wiki Page**: [Transcript:Beefy Bill](https://runescape.wiki/w/Transcript%3ABeefy%20Bill)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Beefy Bill:** ¡Beefy Bill a tu servicio! <br/>I puedo almacenar tu carne, tus pieles de vaca y tu harina, y tengo otras cosas para intercambiar. ¿Qué será?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: Comerciemos.
  - (opens=Beefy Bill's Supplies)
  - [Choice]: Quiero que guardes cosas en el banco por mí.
    - **Beefy Bill:** Excelente. Sólo dame los artículos y te calcularé el precio. Cobro una comisión del 10%.
  - [Choice]: ¿Quién eres?
    - **Beefy Bill:** Soy Beefy Bill, transportista especializado en carne y comerciante en general.
    - **Beefy Bill:** La gente me trae carne de res, pieles de vaca y harina, y yo lo transporte todo al banco y me quedo con sólo el 10% por mis servicios. También tengo cosas a la venta.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Quiero que guardes cosas en el banco por mí.
        - (arriba)
      - [Choice]: Comerciemos.
        - (arriba)
      - [Choice]: ¿Cómo tiras tu carro?
        - **Beefy Bill:** ¡Oh, no lo hago yo mismo! <br/>I uso ganado para tirarlo por mí.
        - [Menu]: ¿Qué te gustaría decir?
          - [Choice]: ¿No es eso repugnante?
            - **Beefy Bill:** ¡Oh, deja de ser ingenuo! No permitiré que su mezquina ética personal se interponga en mi derecho a dirigir un negocio exitoso.
            - **Beefy Bill:** Ahora, ¿quieres mis servicios o no?
            - (otro)
          - [Choice]: Quiero que guardes cosas en el banco por mí.
            - (arriba)
          - [Choice]: Comerciemos.
            - (arriba)
          - [Choice]: Lo pensaré.
            - (abajo)
      - [Choice]: Lo pensaré.
        - (abajo)
  - [Choice]: Lo pensaré.
    - **Beefy Bill:** No pierdas demasiado tiempo pensando; el tiempo es dinero.

### Using items on Bill


#### Cueros de vaca, carne de res cruda o ollas de harina

- [Menu]: Bill se queda con 1 artículo de cada 10:
  - (Condition: If the player has less than 11 of the relevant item:)
    - [Choice]: Banco [número], Bill se queda con 1.
      - **Beefy Bill:** ¡Es un placer hacer negocios contigo, amigo!
    - [Choice]: Olvídalo.
      - (end)
    - [Choice]: cond=With a ring of charos(a) equipped|[Charm] Banco [número], Bill mantiene 0.
      - **Beefy Bill:** Um... está bien, supongo que lo haré gratis.
  - (Condition: If the player has 12 to 22 of the relevant item:)
    - [Choice]: Banco [número], Bill se queda con 1.
      - **Beefy Bill:** ¡Es un placer hacer negocios contigo, amigo!
    - [Choice]: Banco [número], Bill se queda con 2.
      - **Beefy Bill:** ¡Es un placer hacer negocios contigo, amigo!
    - [Choice]: Olvídalo.
      - (end)
    - [Choice]: cond=With a ring of charos(a) equipped|[Charm] Banco [número], Bill mantiene 0.
      - **Beefy Bill:** Um... está bien, supongo que lo haré gratis.
  - (Condition: If the player has 23 or greater of the relevant item:)
    - [Choice]: Banco [número], Bill se queda con 2.
      - **Beefy Bill:** ¡Es un placer hacer negocios contigo, amigo!
    - [Choice]: Banco [número], Bill se queda con 3.
      - **Beefy Bill:** ¡Es un placer hacer negocios contigo, amigo!
    - [Choice]: Olvídalo.
      - (end)
    - [Choice]: cond=With a ring of charos(a) equipped|[Charm] Banco [número], Bill mantiene 0.
      - **Beefy Bill:** Um... está bien, supongo que lo haré gratis.

#### Cualquier otro artículo

- **Beefy Bill:** Lo siento, no transporte ese tipo de cosas.
