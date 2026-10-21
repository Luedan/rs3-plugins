# Hermit

- **Original Wiki Page**: [Transcript:Hermit](https://runescape.wiki/w/Transcript%3AHermit)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Hermit Cave, after Hermit Permits

- [Menu]: Selecciona una opción
  - [Choice]: ¿Puedes imbuirme otro amuleto de cangrejo?
  - (Condition: Con cangrejo en backpack, banco o en cramulet:)
    - **Hermit:** Siento que ya tienes un cangrejo. Este es un regalo precioso que no debe entregarse a nadie ni a todos. Uno es suficiente.
  - (Condition: De lo contrario:)
    - (Condition: Sin amuleto de cangrejo en backpack:)
      - **Hermit:** No tienes un amuleto de cangrejo para imbuir.
    - (Condition: Con amuleto de cangrejo en backpack:)
      - (removes=crab amulet) (receives=crabulet)
      - **Hermit:** Ahí. Otro cangrejo encantado para ti.
      - (initial)
  - [Choice]: ¿Cómo aprendiste el lenguaje de los cangrejos?
    - **Player:** ¿Cómo aprendiste el lenguaje de los cangrejos?
    - **Hermit:** Mi madre era un cangrejo. Ella me lo enseñó desde que nací.
    - **Player:** ¿En serio? Eso suena como un milagro médico.
    - **Hermit:** ¡Ja! Ojalá, pero no.
    - **Hermit:** En mi vida pasada fui marinero. Después de un desagradable incidente con un banco de tiburones, terminé varado. Finalmente, apareció varado en las costas de Wendlewick, muerto de hambre y con frío.
    - **Hermit:** Logré arrastrarme hasta el cadáver de una ballena, donde una grasa de ballena que se calentaba pero se pudría me salvó del borde de la muerte.
    - **Player:** La grasa de ballena podrida probablemente me enviaría al borde de la muerte.
    - **Hermit:** Los cangrejos me trajeron unas sardinas frescas para comer. ¿Quizás pensaron que yo era uno de ellos por mi cabello? No sé.
    - **Hermit:** De todos modos, los seguí hasta esta cueva y me enamoré. ¡Todos los aislamientos que puedas soñar! ¡Sin impuestos! La vida sencilla.
    - **Hermit:** Todos los mariscos que pude imaginar, pero nunca comí cangrejo. Con el tiempo aprendieron a confiar en mí y me concedieron el regalo.
    - (initial)
  - [Choice]: ¿Saben los aldeanos que vives aquí?
    - **Player:** ¿Saben los aldeanos que vives aquí?
    - **Hermit:** Eh, algunos de ellos. El olor los mantiene alejados principalmente.
    - **Hermit:** ¡Excepto Esther! Ah, Esther. Mujer encantadora. Estaba muy intrigada por mi situación.
    - **Player:** No quiero ser grosero, pero ¿has considerado bañarte?
    - **Hermit:** ¡Me baño! Con los cangrejos por supuesto.
    - **Player:** Correcto. Entonces te bañas en agua rancia de cueva, llena de cangrejos.
    - **Hermit:** Exactamente. ¡Limpio como una patena!
    - (initial)
  - [Choice]: Adiós.
    - **Player:** Nos vemos, Hermit.
    - **Hermit:** Adiós, Player.

#### Usando un amuleto de cangrejo en el Hermit

- [Menu]: ¿Imbuir otro amuleto de cangrejo?
  - [Choice]: Sí.
    - (above|imbue)
  - [Choice]: No importa.
    - (end)

#### Usando un cangrejo en el Hermit

- **Hermit:** Uno de los objetos más poderosos del universo. Cuídalo bien.
