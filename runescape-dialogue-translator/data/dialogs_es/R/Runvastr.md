# Runvastr

- **Original Wiki Page**: [Transcript:Runvastr](https://runescape.wiki/w/Transcript%3ARunvastr)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Love Story

- **Runvastr:** Oh, deja en paz a un viejo enano, ¿quieres?
- **Player:** ¿Por qué? ¿Qué pasa?
- **Runvastr:** Noventa años en las minas, y esto es todo lo que saqué de ello. Toda mi vida se desperdició.
- **Player:** Aún tienes una bonita casa, ¿no?
- **Runvastr:** Una casa vieja y de mala muerte en el este, eso es todo lo que representa mi vida.
- **Player:** Entonces te dejaré en paz.

### After Love Story

- **Runvastr:** ¿Por qué me molestas, humano? Trabajé en las minas durante noventa años y quiero un poco de paz ahora que estoy jubilado.
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: cond=If the player has not yet received the miner's diary|Cuéntame sobre tu vida como minero.
    - **Player:** Cuéntame sobre tu vida como minero.
    - **Runvastr:** Quieres que hable de minería, ¿eh? Ahhh, recuerdo balancear mi pico hora tras hora, día tras día, en las minas oscuras y húmedas.
    - **Runvastr:** El viejo Saggy-face, el supervisor, estaría allí con su pico más afilado, buscando vagos para empalar. Por supuesto, al final los trolls lo atraparon.
    - **Runvastr:** Pobre cara caída. Habíamos encontrado una tribu de trolls deambulando por los túneles: enormes trolls de las montañas.
    - **Runvastr:** Saggy-face intentó enfrentarse a ellos sin ayuda de nadie, y le arrancaron la cabeza de los hombros.
    - **Runvastr:** Afortunadamente, teníamos a esa humana loca, Dissy, quedándose en la ciudad en ese momento. Expulsó a esos trolls de las minas con su magia.
    - **Player:** Dissy, ¿eh? ¿Era su nombre completo Dionisio?
    - **Runvastr:** Todos los nombres humanos me suenan igual. Aquí tengo mi viejo diario de esa época. Tómalo y lee todo sobre esos días.
    - (receives=miner's diary)
    - [El viejo enano te regala un libro gastado.]
  - [Choice]: cond=If the player has already received the miner's diary before|Necesito otra copia de tu diario.
    - (Condition: If the player lost the diary:)
      - **Player:** Necesito otra copia de tu diario.
      - **Runvastr:** ¡Bah! Los jóvenes son tan descuidados. Supongo que tendré que darte otra copia.
      - (receives=miner's diary)
      - [El viejo enano te regala un libro gastado.]
    - (Condition: If the player had given the diary to the Wise Old Man:)
      - **Player:** Necesito otra copia de tu diario.
      - **Runvastr:** ¡Bah! Los jóvenes son tan descuidados.
      - **Player:** Se lo di a Dionysius, el mago que te ayudó a expulsar a los trolls de tus minas.
      - **Runvastr:** Me alegro de no ser la única persona de aquellos días que sigue viva. Toma, te daré otra copia.
      - (Condition: If the player has no backpack space:)
        - **Player:** Mi inventario está demasiado lleno.
        - **Runvastr:** Ah, ustedes, los jóvenes, siempre tienen tantas cosas. En mis tiempos solo llevábamos un pico y eso nos bastaba.
      - (Condition: If the player has at least one backpack space:)
        - (receives=miner's diary)
        - [El viejo enano te regala un libro gastado.]
  - [Choice]: ¿Puedes darme algo gratis?
    - **Player:** ¿Puedes darme algo gratis?
    - **Runvastr:** ¡Bah! En mi época, la gente trabajaba para ganarse la vida, y cualquiera que no quisiera trabajar recibía un golpe corto y fuerte con un pico. Así fue. Ahhh.
    - **Player:** Entonces, ¿eso es "no"?
    - **Runvastr:** ¡Vete!
  - [Choice]: Lo siento, te dejaré en paz.
    - **Player:** Lo siento, te dejaré en paz.
    - **Runvastr:** ¡Bien!
