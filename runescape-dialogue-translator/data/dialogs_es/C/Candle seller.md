# Candle seller

- **Original Wiki Page**: [Transcript:Candle seller](https://runescape.wiki/w/Transcript%3ACandle%20seller)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

- **Candle seller:** ¿Quieres una vela encendida por 1000 de oro?
- [Menu]: Selecciona una opción
  - [Choice]: Sí por favor.
    - **Player:** Sí, por favor.
    - (Condition: Si el player no tiene 1000 coins:)
      - **Player:** Pero no tengo esa cantidad de dinero conmigo.
      - **Candle seller:** ¡Pues entonces no hay vela para ti!
    - (Condition: Si el player tiene 1000 coins:)
      - (removes=1000 coins) (receives=unlit candle)
      - **Candle seller:** Aquí tienes entonces.
      - **Candle seller:** Sin embargo, debo advertirte que puede ser peligroso llevar una llama desnuda allí abajo. Sería mejor que hicieras una linterna.
      - [Menu]: Selecciona una opción
        - [Choice]: ¿Qué tiene de peligroso una llama desnuda?
          - **Player:** ¿Qué tiene de peligroso una llama desnuda?
          - **Candle seller:** Je, je... Lo descubrirás.
        - [Choice]: ¿Cómo se hacen las linternas?
          - (abajo)
        - [Choice]: Gracias, adiós.
          - **Player:** Gracias, adiós.
  - [Choice]: ¡¿Mil de oro?!
    - **Player:** ¡¿Mil de oro?!
    - **Candle seller:** Mira, no podrás sobrevivir en ese agujero sin una fuente de luz.
    - **Candle seller:** Así que podrías ir a la tienda de velas a comprar una más barata. Incluso podrías hacer tu propia linterna, que es mucho mejor.
    - **Candle seller:** Pero apuesto a que quieres saber qué hay ahí abajo ahora mismo, ¿no? ¡Y puedes pagarme 1000 de oro por el privilegio!
    - [Menu]: Selecciona una opción
      - [Choice]: Está bien, tú ganas, compraré una vela.
        - **Player:** Está bien, tú ganas, compraré una vela.
        - (continuea)
      - [Choice]: De ninguna manera.
        - **Player:** De ninguna manera.
  - [Choice]: No gracias, prefiero maldecir la oscuridad.
    - **Player:** No, gracias, prefiero maldecir la oscuridad.
  - [Choice]: ¿Cómo se hacen las linternas?
    - **Player:** ¿Cómo se hacen linternas?
    - **Candle seller:** Fuera de vidrio. Las linternas más avanzadas también tienen un componente metálico.
    - **Candle seller:** En primer lugar, puedes hacer un farol con vela sencillo con vidrio. Es como una vela, pero la llama no está expuesta, por lo que es más segura.
    - **Candle seller:** Luego puedes hacer una lámpara de aceite, que es más brillante pero tiene una llama expuesta. Pero si le haces un marco de hierro, puedes convertirlo en una lámpara de aceite.
    - **Candle seller:** Finalmente está la linterna de diana. Necesitarás hacer un marco de acero y agregarle una lente de vidrio.
    - **Candle seller:** Una vez que hayas hecho tu lámpara o linterna, necesitarás preparar aceite para lámparas. La farmacia cerca de Rimmington tiene una máquina para eso.
    - **Candle seller:** Para cualquier fuente de luz, necesitarás un yesquero para encenderla. ¡Mantén tu yesquero a mano en caso de que se apague!
    - **Candle seller:** Pero si todo eso es demasiado complicado, ¡puedes comprar una vela aquí mismo por 1000 de oro!
  - [Choice]: ¿Qué es ese campamento detrás de ti?
    - **Player:** ¿Qué es ese campamento detrás de ti?
    - **Candle seller:** ¿Puedes creerlo? Estaba ocupándome de mi pequeño negocio de venta de velas cuando, de repente, hordas de tropas zamorakias construyeron este estúpido campamento que está ahuyentando a mis clientes.
    - **Candle seller:** Pero de todos modos, ahora estás aquí, así que no hablemos de ellos. ¿Quieres una vela encendida por 1000 de oro?
    - (continuea|youwin)
