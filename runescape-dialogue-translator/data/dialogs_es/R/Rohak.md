# Rohak

- **Original Wiki Page**: [Transcript:Rohak](https://runescape.wiki/w/Transcript%3ARohak)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Under White Wolf Mountain


#### Antes de Recipe for Disaster

- **Viejo Enano:** Hola, jovencito.
- **Player:** ¿A quién llamas joven?
- **Viejo Enano:** ¿Por qué tú? ¡A menos que hayas visto el pequeño pueblo de Falador convertirse en una ciudad bulliciosa como yo, por supuesto!
- **Player:** Err... no...
- **Viejo Enano:** ¡Pues bien! Disfrute de su estancia en nuestra casa de montaña.

#### Después de Recipe for Disaster

- **Rohak:** Hola de nuevo, jovencito.
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: Sobre tu hijo...
    - **Player:** ¿Cómo le va a tu hijo ahora que lo rescaté de la burbuja del tiempo y del culinaromante?
    - **Rohak:** Mi hijo está bien. Aunque no estoy tan seguro de ti. Tal vez deberías acostarte en una habitación oscura hasta que deje de balbucear.
  - [Choice]: ¿Puedo comer otro pastel de roca?
    - **Rohak:** Sí, todavía tengo suficientes ingredientes de antes, pero quiero 100 coins.
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: Bien, 100 coins estarán bien.
        - (Condition: Without enough money:)
          - No puedes permitirte eso.
          - (pop-up)
            - (Pop-up: You can not afford that.|warning=yes)
        - (Condition: With enough money:)
          - (removes=100 coins)
          - [Entregas 100 de oro y Rohak te hornea un pastel de piedra.]
          - (Action: Un pastel de roca enano aparece en la mesa cercana.)
      - [Choice]: No gracias.
        - **Rohak:** No lo hago por menos, ni siquiera por un compañero.
