# Barlak

- **Original Wiki Page**: [Transcript:Barlak](https://runescape.wiki/w/Transcript%3ABarlak)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Missing dialogue regarding trading (perfect) snail shells to Barlak, and dialogue regarding trading long and curved bones without the level 30 Construction requirement.}}

### In Dorgesh-Kaan

- **Barlak:** ¡Huesos!
- **Player:** ¿Qué?
- **Barlak:** ¡No tengo huesos!
- [Menu]: Selecciona una opción
  - [Choice]: Entonces ¿cómo te pones de pie?
    - **Player:** Entonces, ¿cómo te pones de pie?
    - **Barlak:** ¿Qué?
    - **Player:** ¿Cómo te pones de pie si no tienes huesos? ¿No deberías colapsar y convertirte en una masa gelatinosa?
    - **Barlak:** ¡Ja, ja, ja, ja, ja!
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Para qué necesitas huesos?
        - (below|need)
      - [Choice]: ¿Qué tipo de huesos necesitas?
        - (below|kind)
      - [Choice]: ¿Comprarás algo además de huesos?
        - (below|anything)
      - [Choice]: Adiós.
        - **Player:** Adiós.
        - **Barlak:** Adiós.
  - [Choice]: ¿Para qué necesitas huesos?
    - **Player:** ¿Para qué necesitas huesos?
    - **Barlak:** Para ponerse de pie correctamente. ¡De lo contrario, me convertiría en una masa gelatinosa!
    - **Barlak:** ¡Ja, ja, ja, ja, ja!
    - **Barlak:** No, en serio, necesito huesos para usarlos como material de Construction. Siempre necesitamos huesos grandes para apuntalar los pozos de las minas y para construir otras estructuras temporales.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué tipo de huesos necesitas?
        - (below|kind)
      - [Choice]: ¿Comprarás algo además de huesos?
        - (below|anything)
      - [Choice]: Adiós.
        - (above|goodbye)
  - [Choice]: ¿Comprarás algo además de huesos?
    - **Player:** ¿Comprarás algo además de huesos?
    - **Barlak:** Bueno, algunas personas me han traído algunas conchas gigantes interesantes. Dicen que provinieron de caracoles gigantes y tortugas gigantes.
    - **Barlak:** Por supuesto, al igual que los huesos, algunas conchas son mejores que otras. Te daré 250 po por proyectiles normales, pero lo que realmente necesito son proyectiles perfectos. Pagaré el doble por ellos y también te daré algunos consejos sobre Crafting.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Para qué necesitas huesos?
        - (above|need)
      - [Choice]: ¿Qué tipo de huesos necesitas?
        - (below|kind)
      - [Choice]: Adiós.
        - (above|goodbye)
  - [Choice]: ¿Qué tipo de huesos necesitas?
    - **Player:** ¿Qué tipo de huesos necesitas?
    - **Barlak:** Huesos enormes, tan grandes como puedas conseguir. No bastará con cualquier hueso grande.
    - **Barlak:** A veces es posible que encuentres un hueso particularmente largo y recto. Ese es el tipo de cosas que necesito; Te daré 1.000 po por uno de ellos.
    - **Barlak:** De vez en cuando, es posible que encuentres un hueso largo y curvo. Estos son especialmente valiosos. Te daré 2000 po por ellos.
    - **Barlak:** También te enseñaré un poco sobre cómo usamos los huesos en Construction, si quieres.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué tipo de huesos necesitas?
        - (above|kind)
      - [Choice]: ¿Comprarás algo además de huesos?
        - (above|anything)
      - [Choice]: Adiós.
        - (above|goodbye)

#### Con caparazones de tortuga en backpack

- **Barlak:** Ese caparazón gigante... ¿qué es?
- **Player:** ¡Es un caparazón de tortuga de batalla gigante!
- (Condition: Si el player solo lleva caparazones de tortuga normales:)
  - **Barlak:** Hmmm... Creo que podría hacer algo con ellos.
  - **Barlak:** Te daré [amount]gp por el caparazón de tortuga que llevas
  - (continue)
- (Condition: Si el player lleva uno o más caparazones perfectos:)
  - **Barlak:** Hmmm... Creo que podría hacer algo con ellos, especialmente ese perfecto.
  - **Barlak:** Te daré [amount]gp por el caparazón de tortuga que llevas e intentaré darte algunos consejos sobre Crafting mientras estoy en ello.
  - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: Está bien.
    - **Player:** Está bien.
    - (removes=tortoise shell and/or perfect shell)
    - (receives=coins and experience)
    - **Barlak:** ¡Gracias! Ahora, no creo que pueda usar eso para Construction, pero tal vez podría hacer algo...
    - Barlak te ofrece una breve conferencia y aprendes más sobre Crafting.
  - [Choice]: No gracias.
    - **Player:** No, gracias.

#### Con huesos largos o curvos en backpack

- **Barlak:** ¡Esos huesos! ¡Ese es exactamente el tipo de cosas que necesito! ¿Los venderás? Te daré [amount]gp por los huesos que llevas.
- **Barlak:** Intentaré enseñarte algo sobre Construction también, pero es muy técnico, por lo que no lo entenderás si aún no tienes el nivel 30 de Construction.
- [Menu]: Selecciona una opción
  - [Choice]: Está bien.
    - **Player:** Está bien.
    - (removes=long bone and/or curved bone)
    - (receives=coins and experience)
    - **Barlak:** ¡Gracias! Ahora déjame explicarte...
    - Barlak te ofrece una breve conferencia y aprendes más sobre Construction.
  - [Choice]: No, me quedaré con los huesos.
    - **Player:** No, gracias.
