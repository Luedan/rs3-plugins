# Apothecary

- **Original Wiki Page**: [Transcript:Apothecary](https://runescape.wiki/w/Transcript%3AApothecary)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{External|os|rsc}}

### In Varrock


#### Diálogo estándar

- **Apothecary:{{anchor|brew}}** Soy el Apothecary. Preparo pociones. ¿Necesitas algo específico?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Puedes hacer una poción de fuerza?
    - **Player:** ¿Puedes hacer una poción de fuerza?
    - (Condition: Sin los ingredientes:)
      - **Apothecary:** Sí, pero los ingredientes son un poco difíciles de encontrar. Si alguna vez los consigues, lo haré por ti, pagando una tarifa.
      - **Player:** Entonces, ¿cuáles son los ingredientes?
      - **Apothecary:** Necesitarás encontrar los huevos de la mortal araña roja y una raíz de limpwurt.
      - **Apothecary:** Ah, y tendrás que pagarme 5 coins.
      - **Player:** Ok, los cuidaré.
    - (Condition: Con los ingredientes:)
      - **Apothecary:** Por supuesto. Veo que tienes huevos de araña y raíz de limpwurt. Entrégamelos, págame 5 coins por poción y empezaré.
      - [Menu]: Selecciona una opción
        - [Choice]: Vale, eso suena bien.
          - **Player:** Vale, eso suena bien.
          - (removes=red spiders' eggs, limpwurt root and 5 coins) (receives=strength potion (4))
          - (Condition: Si es la primera vez que preparan una poción de fuerza en la botica:)
            - {{RSFontAchievement|Double-strength Weaksauce}}
            - (continue)
          - {{tbox|pic=Strength potion (4) detail.png|The Apothecary gives you a strength potion.}}
        - [Choice]: No, olvídalo.
          - **Player:** No, olvídalo.
  - [Choice]: ¿Conoces una poción para hacer que el cabello se caiga?
    - **Player:** ¿Conoces una poción para hacer que el cabello se caiga?
    - **Apothecary:** Así es. Se lo di a mi madre. Por eso ahora vivo solo.
  - [Choice]: ¿Tienes alguna buena poción para regalar?
    - **Player:** ¿Tienes alguna poción buena para regalar?
    - (Condition: Con una poción para el acné en el backpack:)
      - **Apothecary:** Sólo esa crema para manchas. Espero que lo disfrutes.
    - (Condition: Sin poción para el acné en el backpack:)
      - (Condition: Si Apothecary acepta la solicitud de el player:)
        - **Apothecary:** Bueno, entonces. Prueba esta poción.
        - (receives=acne potion)
      - (Condition: Si Apothecary rechaza la solicitud de el player:)
        - **Apothecary:** Lo siento, la caridad no es mi punto fuerte.
  - [Choice]: ¿Puedes hacer una poción que haga que parezca que estoy muerto?
    - **Player:** ¿Puedes hacer una poción que haga que parezca que estoy muerto?
    - **Apothecary:** ¡Qué petición más extraña y morbosa! Puedo como sucede. La baya del arbusto cadava, preparada adecuadamente, inducirá un coma tan profundo que parecerá que estás muerto. Es muy peligroso.
    - **Apothecary:** Tengo los demás ingredientes, pero necesitaré que me traigas un manojo de cadava berries.
    - (Condition: Sin cadava berries en el backpack:)
      - **Player:** Lo tendré en cuenta.
    - (Condition: Con cadava berries en backpack:)
      - [Menu]: Selecciona una opción
        - [Choice]: Toma estos cadava berries.
          - **Player:** Toma estos cadava berries.
          - {{tbox|You hand over the berries, which the Apothecary shakes up in a vial of strange liquid.}}
          - (Action: El boticario mezcla la poción.)
          - **Apothecary:** ¡Uf! Esto es lo que necesitas.
          - (removes=cadava berries) (receives=cadava potion)
          - {{tbox|pic=cadava potion detail.png|The apothecary gives you a Cadava potion.}}
        - [Choice]: No gracias.
          - **Player:** No, gracias.
  - [Choice]: cond=After Rat Catchers:|No podrías hacer ninguna otra poción para gatos, ¿verdad?
    - **Player:** No podrías hacer ninguna otra poción para gatos, ¿verdad?
    - **Apothecary:** No tengo planes de expandirme al mercado de pociones para gatos en este momento, pero si hubiera suficiente demanda, podría cambiar de opinión.

#### Usando el diario de Herbi Flax en él

- {{tbox|pic=Diary (Shades of Mort'ton) detail.png|You show the Serum book to the Apothecary.}}
  - (Condition: Si aún no se ha proporcionado:)
    - **Apothecary:** ¿Quieres cambiar el diario todavía? Me gustaría pasar la información a la comunidad científica de Varrock.
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, lo cambiaré por entrenamiento en herblore.
        - **Player:** Sí, lo cambiaré por entrenamiento en herblore.
        - **Apothecary:** Genial...
        - {{tbox|The apothecary trains you in herblore.}}
        - (Action: A el player se le elimina el Diario (Sombras de Mort'ton) y obtiene 335 de experiencia Herblore.)
        - ¡Felicitaciones! Has completado: 'Herbi Flax': entrega el diario de Herbi Flax al boticario de Varrock.
        - **Apothecary:** Ok, eso es todo lo que puedo enseñarte. Muchas gracias por el diario.
      - [Choice]: No gracias, quiero conservarlo un poco más.
        - **Player:** No, gracias, quiero conservarlo un poco más.
        - **Apothecary:** Oh, es una pena... Vuelve si cambias de opinión.
  - (Condition: Si ya se ha dado:)
    - **Apothecary:** Hmm, este es un tomo interesante... Pero ya me vendiste uno, ¡gracias!

#### Si el player ha perdido su gorro de enfermera o médico

- [Menu]: Elige una opción:
  - [Choice]: Pida otro gorro de Enfermera o Médico.
    - **Player:** Hola Apothecary, perdí ese sombrero que me diste.
    - **Apothecary:** No hay problema, compro muchos de estos en Gielinorian Hospital Supplies.
    - [Menu]: Elige un sombrero
      - [Choice]: Gorro de enfermera
        - {{tbox|pic=Nurse hat detail.png|The Apothecary has given you a Nurse's Hat.}}
        - (receives=nurse hat)
        - **Apothecary:** Entonces todo lo que tienes que hacer es darle un frasco de agua y él lo tomará pensando que es una poción curativa.
        - **Player:** ¡Jaja! ¡Siempre quise ser enfermera!
      - [Choice]: Gorro de médico
        - {{tbox|pic=Doctors hat detail.png|The Apothecary has given you a Doctor's Hat.}}
        - (receives=doctors hat)
        - **Apothecary:** Entonces todo lo que tienes que hacer es darle un frasco de agua y él lo tomará pensando que es una poción curativa.
        - **Player:** ¡Jaja! ¡Siempre quise ser médico!
  - [Choice]: Habla de otra cosa.
    - (Action: arriba|preparar)

### In New Varrock

- **Apothecary:{{anchor|brew}}** Soy el Apothecary. Preparo pociones. <br>¿Necesitas algo específico?
- [Menu]: Elige una opción:
  - [Choice]: ¿Puedes hacer una poción de fuerza?
    - (Condition: Antes de la Dimensión del Desastre: Demonio Slayer:)
      - **Apothecary:** Normalmente, estaría encantado de hacerlo, pero algunos de mis ingredientes más peligrosos han sido incautados en el campamento de demonios de Delrith.
      - **Apothecary:** Si alguna vez logras entrar allí y encuentras mi alijo de huevos de araña roja y raíces de limpwurt, tráemelos.
      - **Apothecary:** Como agradecimiento, ¡te daré la tarifa de "amigo especial" de cinco zemomarks por poción de fuerza!
      - **Player:** Lo tendré en cuenta.
      - (initial)
    - (Condition: Después de Dimensión del desastre: Demon Slayer:)
      - **Apothecary:** Estaría encantado de hacerlo, pero algunos de mis ingredientes más "peligrosos" han sido incautados en el campamento de demonios de Delrith.
      - **Apothecary:** He oído que puedes entrar allí. Si encuentras mi alijo de huevos de araña roja y raíces de limpwurt, tráemelos. Sólo cobraré cinco zemomarks por poción de fuerza.
      - **Apothecary:** Sin embargo, solo tenía un puñado de ingredientes; esas cosas son difíciles de conseguir en el nuevo Varrock. Una vez que se han ido, se han ido.
      - (initial)
    - (Condition: Con huevos de araña roja y raíces de limpwurt en backpack:)
      - **Apothecary:** ¿Quieres que los use para mezclar algunas pociones de fuerza? Sólo cinco zemomarks por poción.
      - [Menu]: Selecciona una opción
        - [Choice]: Sí.
          - (removes=three red spiders' eggs, three limpwurt roots and 15 zemomarks)
          - (receives=three strength potions)
          - (initial)
        - [Choice]: No.
          - (end)
  - [Choice]: ¿Puedes hacer una poción que haga que parezca que estoy muerto?
    - **Apothecary:** ¡Qué petición más extraña y morbosa! Puedo, da la casualidad. La baya del arbusto cadava, preparada adecuadamente, inducirá un coma tan profundo que parecerá que estás muerto. Es muy peligroso.
    - **Apothecary:** Tengo los demás ingredientes, pero necesitaré que me traigas un manojo de cadava berries.
    - (Condition: Sin cadava berries en backpack:)
      - **Player:** Lo tendré en cuenta.
      - (initial)
    - (Condition: Con cadava berries en backpack:)
      - [Menu]: Selecciona una opción
        - [Choice]: Toma estos cadava berries.
          - [Le entregas el berries, que el boticario agita en un frasco de un líquido extraño.]
          - **Apothecary:** ¡Uf!<br>Esto es lo que necesitas.
          - (removes=cadava berries)
          - (receives=cadava potion)
          - [El boticario te da una poción de cadava.]
        - [Choice]: No, gracias.
          - (initial)
  - [Choice]: Nada, gracias.
    - (end)
