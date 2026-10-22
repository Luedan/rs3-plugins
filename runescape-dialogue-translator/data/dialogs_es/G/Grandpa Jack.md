# Grandpa Jack

- **Original Wiki Page**: [Transcript:Grandpa Jack](https://runescape.wiki/w/Transcript%3AGrandpa%20Jack)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to

- **Grandpa Jack:** ¡Hola joven [man/woman]!<br/>¿Vienes a visitar al viejo Grandpa Jack? Puedo contaros historias con seguridad. ¡Solía ​​ser el mejor pescador que estos lugares han visto!
- [Menu]: Selecciona una opción
  - [Choice]: Cuéntame una historia entonces.
    - **Player:** Entonces cuéntame una historia.
    - **Grandpa Jack:** Bueno, cuando yo era joven solíamos hacer viajes de pesca a Catherby; La pesca allí... ¡eso sí que era algo!
    - **Grandpa Jack:** De todos modos, decidimos pescar un poco con nuestras redes, no estaba pasando el mejor de los días y no encontré nada más que botas viejas y trozos de algas. ¡Entonces mi red de repente se volvió muy pesada!
    - **Grandpa Jack:** Lo levanté...
    - **Grandpa Jack:** ¡Para mi sorpresa, había atrapado este cofrecito!
    - **Grandpa Jack:** ¡Aún más sorprendente fue que cuando lo abrí contenía un diamante del tamaño de un rábano! ¡Esa es la mejor captura que he tenido!
  - [Choice]: Lo siento, no tengo tiempo ahora.
    - **Player:** Lo siento, no tengo tiempo ahora.
    - **Grandpa Jack:** Suspiro...
    - **Grandpa Jack:** Jóvenes, siempre con tanta prisa.
  - [Choice]: ¿Puedo comprar una de sus cañas de pescar?
    - **Player:** ¿Puedo comprar una de sus cañas de pescar?
    - (Condition: If the player has a fishing rod in their backpack:)
      - **Grandpa Jack:** Pero joven [man/woman], tú tienes el tuyo propio. ¡No te venderé el mío cuando ya tengas uno!
    - (Condition: If the player does not have a fishing rod in their backpack:)
      - **Grandpa Jack:** Por supuesto que puedes, joven [man/woman]. Veamos ahora... Creo que 5 de oro es un precio justo por una caña que ha ganado el concurso Fishing antes, ¿no?
      - [Menu]: Selecciona una opción
        - [Choice]: Muy justo, compraré esa caña!
          - **Player:** Muy justo, ¡compraré esa caña!
          - **Grandpa Jack:** ¡Excelente elección!
          - (Condition: If the player does not have at least one free backpack space:)
            - **Player:** El único problema es que no tengo espacio para llevar uno en este momento. Déjame responderte sobre eso.
            - **Grandpa Jack:** Tienes razón. Estaré aquí.
          - (Condition: If the player has at least one free backpack space:)
            - (removes=5 coins) (receives=fishing rod)
            - [Entregas el dinero y recibes una caña de pescar.]
            - **Player:** ¡Gracias!
            - **Grandpa Jack:** De nada young 'un.
        - [Choice]: Eso es demasiado rico para mí, iré a Catherby.
          - **Player:** Eso es demasiado rico para mí, iré a Catherby.
          - **Grandpa Jack:** Si estás seguro.... estás dejando pasar la oportunidad de tu vida.
  - [Choice]: He olvidado cómo pescar, ¿puedes recordármelo?
    - **Player:** He olvidado cómo pescar, ¿puedes recordármelo?
    - **Grandpa Jack:** ¡Por supuesto! Déjame ver ahora... Necesitarás una caña y un cebo. También se puede pescar con red, pero no en competición.
    - **Player:** Ok... Creo que puedo conseguirlos en Catherby.
    - **Grandpa Jack:** Entonces simplemente busca un lugar para pescar, ya sea en la competencia cerca de aquí o donde puedas; te recomiendo pescar con red en Catherby. Red o atrae a los peces en el lugar de pesca haciendo clic en él y luego ten paciencia...
    - **Player:** ¿Es así de simple?
    - **Grandpa Jack:** ¡Sí! Ve a buscarlos tigre.
