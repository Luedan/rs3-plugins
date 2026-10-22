# Freda

- **Original Wiki Page**: [Transcript:Freda](https://runescape.wiki/w/Transcript%3AFreda)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Death Plateau

- **Player:** ¡Hola!
- **Freda:** Bueno, ¡hola! ¡Dios mío, eres alegre! ¿Le puedo ayudar en algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Freda:** Soy Freda, ¡bienvenido a mi humilde hogar!
    - **Freda:** Mi esposo, Sabbot, y yo vinimos aquí para iniciar un puesto comercial. Ya sabes, vender armas enanas a la Guardia.
    - **Freda:** Luego vinieron los trolls y se apoderaron de la meseta antes de que pudiéramos establecernos, así que vine a vivir aquí.
    - **Player:** ¿Qué pasa con tu marido?
    - **Freda:** ¡Esa vieja mula testaruda no sale de la cueva en la que estábamos! Preferiría morir antes que dejar que los trolls ganen.
    - **Freda:** Le envío sopa y cartas de vez en cuando, y esos buenos hombres de la ciudad se aseguran de que esté bien.
    - **Freda:** ¿Hay algo más que quieras?
    - (otro)
  - [Choice]: ¿No les tienes miedo a los trolls de aquí?
    - **Freda:** Para nada. Solía ​​haber algunos por aquí, pero pronto me ocupé de ellos.
    - **Player:** ¿Cómo? ¿No son los trolls realmente feroces en combate?
    - **Freda:** Sí, ¡pero soy más feroz!
    - **Freda:** Debes saber que no he sido comerciante en toda mi vida. Sé qué extremo de un hacha le hará más daño a un troll.
    - **Freda:** Además, algunos de esos jóvenes simpáticos del pueblo me echan una mano si los trolls vienen en gran número. Pero después de la última vez, los trolls parecen haber captado la indirecta.
    - **Freda:** ¡Es sorprendente lo que puede hacer agitar un hacha a la altura de la ingle para romper la voluntad incluso del troll más grande!
    - **Player:** Entonces, ¿por qué no vives con tu marido?
    - **Freda:** Bueno, puedo enfrentarme a algún troll errante ocasional, pero una horda entera de ellos es algo completamente distinto.
    - **Freda:** Puede que este lugar no sea tan seguro, pero al menos no está en medio de una zona de guerra.
    - **Freda:** ¿Puedo ayudarte con algo más?
    - (otro)
  - [Choice]: Eso es todo, gracias.
    - **Freda:** ¿Ah? Bueno, cuídate en el camino de regreso.

### After Death Plateau

- **Player:** Hola, Freda.
- **Freda:** Hola. ¡Escuché de algunos de los chicos de la ciudad que realmente les diste una paliza a esos trolls!
- **Freda:** Sigue así. Todo ayuda.
- **Player:** ¡Lo haré!
- **Freda:** ¿Necesitas algo más?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - (arriba)
  - [Choice]: ¿No les tienes miedo a los trolls de aquí?
    - (arriba)
  - [Choice]: ¿Puedo comprar unas botas de escalada?
    - **Freda:** No veo por qué no. Déjame ver lo que tengo en tu talla.
    - [Menu]: Selecciona una opción
      - [Choice]: Compra botas estándar por 12 po.
        - (Condition: With climbing boots already in backpack or bank:)
          - (opens=Freda's Boots)
        - (Condition: Without space in backpack:)
          - **Freda:** Lo sentimos, no tienes ningún lugar donde colocarlos.
          - (opens=Freda's Boots)
        - (Condition: Without 12 gold:)
          - No puedes permitirte eso.
          - (pop-up)
            - (Pop-up: You can not afford that.|warning=yes)
          - **Freda:** Vaya, parece que te falta un poco. Son 12 de oro lo que necesitas para comprar estas botas.
          - (opens=Freda's Boots)
        - (Condition: With at least 12 gold:)
          - [Compras las botas de montaña.]
          - (removes=12 coins) (receives=climbing boots)
          - (opens=Freda's Boots)
      - [Choice]: Ver gama completa de stock.
        - (opens=Freda's Boots)
  - [Choice]: Eso es todo, gracias.
    - (arriba)
