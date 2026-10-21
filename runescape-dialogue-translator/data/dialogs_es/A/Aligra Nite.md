# Aligra Nite

- **Original Wiki Page**: [Transcript:Aligra Nite](https://runescape.wiki/w/Transcript%3AAligra%20Nite)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{dialogue|npc}}

### Before [[Desert achievements|Elite Desert tasks]]

- **Aligra Nite:** Ay, effendi, me temo que no puedo confiar en alguien como tú hasta que hayas demostrado tu valía ante la gente.
- Debes reclamar la recompensa Elite por el conjunto de tareas del desierto.

### Standard dialogue after [[Desert achievements|Elite Desert tasks]]

*Al hablar con Aligra Nite en Desert Quarry.*
- **Aligra Nite:** Saludos, effendi. ¿Tienes granito para venderme?
- **Player:** No... ¿por qué? ¿Cuánto pagarías?
- *Si el player tiene granito en su inventario:*
  - **Player:** Tengo granito, sí... ¿Por qué debería vendértelo?
  - **Aligra Nite:** ¡Ah, excelente! ¡Por supuesto que quieres vendérmelo! De esa manera, no tendrás que enviarlo hasta los mercados del norte. Mi fiel camello y yo lo haremos, después de comprártelo, por supuesto.
  - **Player:** ¿Cuánto?
  - (continue)
- **Aligra Nite:** Ahh, solo los mejores precios. Por supuesto, tengo que deducir mis gastos generales y de viaje... pero puedo ofrecerle un precio de 1726 para el mediano, 818 para el pequeño y 269 para el pequeño. Estoy seguro de que estará de acuerdo en que es muy razonable, teniendo en cuenta mis gastos.
- **Player:** ¡Eso es extorsión! ¡Podrías venderlos por cinco veces el precio!
- **Aligra Nite:** Sí, sí podrías, si estuvieras dispuesto a enviarlo todo allí. Yo, sin embargo, te lo aceptaré de forma rápida y sin complicaciones.

### Direct selling options

*Cuando se utilizan las opciones de clic derecho para "Vender todo" o "Tipo de venta" con Aligra Nite en Desert Quarry.*
- *Si usas "Vender todo" con Aligra Nite:*
  - ¿Vender todo el granito?
    - si
      - (receives=coins) (removes=all granite)
      - **Aligra Nite:** Me alegro de que pudiéramos hacer negocios, effendi.
    - No
      - (end)
  - *Si el jugador no tiene granito en el inventario:*
    - **Aligra Nite:** Por desgracia, effendi, no tienes granito para vender.
- *Si usa "Tipo de venta" con Aligra Nite:*
- Elija una opción *(Solo se mostrarán opciones para los tipos de granito que el reproductor tiene en el inventario, si el player solo tiene un tipo, no se mostrarán opciones y el granito se venderá automáticamente)*
  - Vendo todo el granito mediano.
    - (receives=coins) (removes=all 5kg granite)
    - **Aligra Nite:** Me alegro de que pudiéramos hacer negocios, effendi.
  - Vendo todo el granito pequeño.
    - (receives=coins) (removes=all 2kg granite)
    - **Aligra Nite:** Me alegro de que pudiéramos hacer negocios, effendi.
  - Vender todo el granito pequeño.
    - (receives=coins) (removes=all 500g granite)
    - **Aligra Nite:** Me alegro de que pudiéramos hacer negocios, effendi.
