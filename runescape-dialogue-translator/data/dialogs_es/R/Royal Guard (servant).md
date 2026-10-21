# Royal Guard (servant)

- **Original Wiki Page**: [Transcript:Royal Guard (servant)](https://runescape.wiki/w/Transcript%3ARoyal%20Guard%20%28servant%29)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Servants' Guild

- **Guardia Real:** ¡Encantado de conocerte!
- **Player:** ¿Qué haces aquí?
- **Guardia Real:** ¡Ah, visité a Su Alteza Real para el Jubileo de Diamante y me gustó tanto que nunca me fui! Sin embargo, me encuentro sin ingresos. ¿Quieres contratarme solo por [número] coins?
- [Menu]: Selecciona una opción
  - [Choice]: cond=Only if not asked last|¿Qué puedes hacer?
    - **Player:** ¿Qué puedes hacer?
    - **Guardia Real:** Tengo algo de experiencia cocinando y estaré encantado de llevar artículos hacia y desde el banco.
    - (previous)
  - [Choice]: cond=Only if not asked last|Cuéntame sobre tus trabajos anteriores.
    - **Player:** Cuéntame sobre tus trabajos anteriores.
    - **Guardia Real:** He trabajado al servicio de la Reina, casi desde que era un muchacho. Allí se espera una alta calidad de servicio, ¡déjame decirte!
    - (previous)
  - [Choice]: ¡Estás contratado!
    - **Guardia Real:** Mi querido señor, nos han disuadido de realizar más trabajo por ahora.

#### Diálogo histórico

- **Guardia Real:** ¡Encantado de conocerte!
- **Player:** ¿Qué haces aquí?
- **Guardia Real:** ¡Ah, visité a Su Alteza Real para el Jubileo de Diamante y me gustó tanto que nunca me fui! Sin embargo, me encuentro sin ingresos. ¿Quieres contratarme solo por [número] coins?
- [Menu]: Selecciona una opción
  - [Choice]: cond=Only if not asked last|¿Qué puedes hacer?
    - (arriba)
  - [Choice]: cond=Only if not asked last|Cuéntame sobre tus trabajos anteriores.
    - (arriba)
  - [Choice]: ¡Estás contratado!
    - (Condition: Si el player no tiene servidor:)
      - {{Transcript missing}}
    - (Condition: Si el player ya tiene un servidor:)
      - Ya tienes un sirviente.

### In a player-owned house

- {{Transcript missing}}
- **Guardia Real:** ¿Qué puedo hacer por ti?
- [Menu]: Selecciona una opción
  - [Choice]: Ir al banco/aserradero...
    - [Choice]: llevar algo al banco
    - **Player:** ¿Puedes llevarme algo al banco?
    - **Guardia Real:** Esas tareas parecen bastante inferiores a las de una guardia al servicio de la Reina, pero lo haré. Dame el artículo.
    - [Choice]: Trae algo del banco
    - (Condition: Si el artículo está en su banco:)
    - **Guardia Real:** Aquí tienes. Servicio digno de un monarca, debo decir.
    - (Condition: Si el artículo no está en su banco:)
    - **Guardia Real:** No tienes ninguno de esos en tu banco.
    - [Choice]: Lleva algo al aserradero.
    - **Guardia Real:** Me temo que no puedo ir al aserradero; Necesitaría un seguro adicional, ya ves.
  - [Choice]: Varios...
    - [Choice]: hacer té
    - **Guardia Real:** ¡Una excelente elección! Una taza de té, próximamente.
    - **Guardia Real:** ¿Tomas leche con tu té?
      - [Menu]: Selecciona una opción
        - [Choice]: si por favor
        - **Player:** Sí, por favor.
        - [Choice]: No gracias
        - **Player:** No, gracias.
        - [Choice]: En realidad no quiero ninguno
        - **Player:** En realidad no quiero ninguno.
    - [Choice]: servir la cena
    - **Guardia Real:** Por supuesto.
    - [Choice]: servir bebidas
    - **Player:** Sirva bebidas, por favor.
    - **Guardia Real:** Siempre y cuando todo se mantenga en orden.
    - **Guardia Real:** ¿Puedo ofrecerles una bebida?
      - [Menu]: Selecciona una opción
        - [Choice]: si por favor
        - **Player:** Sí, por favor.
        - **Guardia Real:** Disfrútalo.
        - [Choice]: No gracias
        - **Player:** No, gracias.
        - [Choice]: Algo más.
    - (Condition: Vuelve al anterior.)
    - [Choice]: Saludar a los invitados
    - **Player:** Quédese en la entrada y salude a los invitados.
    - **Guardia Real:** Si quieres. Después de todo, estoy altamente capacitado en etiqueta de saludo.
  - [Choice]: deja de seguirme
    - (Condition: La conversación termina.)
  - [Choice]: estas despedido
    - [Menu]: ¿De verdad quieres despedir a tu sirviente?
      - [Choice]: Sí.
        - **Player:** ¡Estás despedido!
        - **Guardia Real:** Volveré con mi monarca. Ha sido un placer.
      - [Choice]: No.
- (Condition: Si usas huesos/cenizas en ellos)
- **Guardia Real:** Como miembro de la Guardia de la Reina, no se me puede ver manipulando tales... objetos.
- **Guardia Real:** Disculpe amigo, ¡no trabajo gratis! Si quieres que siga trabajando para ti, tendrás que pagarme 500 coins.
  - [Menu]: Selecciona una opción
    - [Choice]: Pague al servidor 500 coins.
    - **Guardia Real:** Gracias.
    - [Choice]: Pague al servidor 500 coins y no vuelva a preguntar.
    - **Guardia Real:** Gracias.
    - [Choice]: No pagues.
      - (Condition: La conversación termina.)
    - [Choice]: Servidor de bomberos.
- (Condition: Después de la historia de amor)
  - **Guardia Real:** Disculpe amigo, ¡no trabajo gratis! Si quieres que siga trabajando para ti, tendrás que pagarme 375 coins.
