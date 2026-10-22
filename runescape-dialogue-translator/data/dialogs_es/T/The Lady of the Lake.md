# The Lady of the Lake

- **Original Wiki Page**: [Transcript:The Lady of the Lake](https://runescape.wiki/w/Transcript%3AThe%20Lady%20of%20the%20Lake)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Check initial dialogue before earning Excalibur, check dialogue for 'Excalibur' option after destroying it}}

### Talk to

- **The Lady of the Lake:** Buenos días, [sir/madam].
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: cond=With Excalibur in the backpack and without previously enhancing it:|Sir Kay dijo que me recompensarías.
    - **Player:** Sir Kay dijo que me recompensarías.
    - **The Lady of the Lake:** De hecho, he oído que te has ganado su confianza. ¡Serás recompensado generosamente!
    - (removes=Excalibur|receives=enhanced Excalibur)
    - [The Lady of the Lake extiende la mano y toca la espada Excalibur que parece vibrar con nuevo poder.]
    - **Player:** ¿Qué hace eso entonces?
    - **The Lady of the Lake:** La Excalibur mejorada se empuña con la mano izquierda, no con la derecha, y su espada es mucho más poderosa.
    - **Player:** ¡Gracias!
  - [Choice]: cond=With Excalibur in the backpack and having previously enhanced it:|¿Puedes encantar Excalibur por mí, por favor?
    - **Player:** ¿Puedes encantar Excalibur por mí, por favor?
    - (removes=Excalibur|receives=enhanced Excalibur)
    - [The Lady of the Lake extiende la mano y toca la espada Excalibur que parece vibrar con nuevo poder.]
  - [Choice]: cond=With Excalibur having previously been obtained:|¿Quién eres?
    - **Player:** ¿Quién eres?
    - **The Lady of the Lake:** Soy the Lady of the Lake.
  - [Choice]: cond=If Excalibur was destroyed or lost:|Busco la espada Excalibur.
    - **Player:** Busco la espada Excalibur.
    - **The Lady of the Lake:** Recuerdo que ya has demostrado que eres digno de empuñarlo. Te lo devolveré si puedes demostrar que aún eres digno.
    - **Player:** ¿Y cómo puedo hacer eso?
    - **The Lady of the Lake:** Bueno, demostrando que estás por encima de los bienes materiales.
    - **Player:** ... ¿Y cómo puedo hacer eso?
    - **The Lady of the Lake:** 500 coins deberían ser suficientes.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Bien, aquí tienes.
        - **Player:** Bien, aquí tienes.
        - **The Lady of the Lake:** ¡Gracias por el dinero! Estoy ahorrando para un vestido nuevo.
        - [Menu]: ¿Qué versión de Excalibur te gustaría recuperar?
          - [Choice]: Excalibur - el original.
            - (removes=500 coins|receives=Excalibur)
            - [The Lady of the Lake te entrega Excalibur.]
          - [Choice]: Excalibur mejorada.
            - (removes=500 coins|receives=enhanced Excalibur)
            - [The Lady of the Lake te entrega la versión mejorada de Excalibur.]
      - [Choice]: 500 coins? ¡No, gracias!
        - **Player:** ¿500 coins? ¡No, gracias!
        - **The Lady of the Lake:** Tu actitud materialista me entristece.
  - [Choice]: Buen día.
    - **Player:** Buenos días.

### Excalibur

- (Condition: With Excalibur in the backpack:)
  - (above|rewardme)
- (Condition: Having lost Excalibur:)
  - {{Transcript missing}}
- (Condition: If the player's backpack is full:)
  - **The Lady of the Lake:** ¡Lo dejarás caer si intento entregártelo mientras tu inventario está lleno!
- [Menu]: ¿Pagar 500 coins por Excalibur?
  - [Choice]: Compra Excalibur.
    - (removes=500 coins|receives=Excalibur)
    - [The Lady of the Lake te entrega Excalibur.]
  - [Choice]: Cancelar.
    - (end)
