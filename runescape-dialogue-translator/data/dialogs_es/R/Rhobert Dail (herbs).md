# Rhobert Dail (herbs)

- **Original Wiki Page**: [Transcript:Rhobert Dail (herbs)](https://runescape.wiki/w/Transcript%3ARhobert%20Dail%20%28herbs%29)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Prifddinas


#### Hablando con él

- **Rhobert Dail (hierbas):** La Torre de las Voces es un lugar maravilloso para hacer negocios, cautivados por la Voz de Seren como estamos.
- **Rhobert Dail (hierbas):** Mi especialidad es todo lo relacionado con hierbas y pociones. ¿Puedo ayudarte con algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Puedes decantarme algunas pociones?
    - (below|Decant option)
  - [Choice]: ¿Me pueden ayudar con los precios de las hierbas?
    - **Rhobert Dail (hierbas):** ¡Estaría encantado de hacerlo!
    - ((Precios indicativos: se abren las hierbas.))
  - [Choice]: ¿Cuanto cobran por decantar pociones?
    - **Rhobert Dail (hierbas):** Si quieres pociones decantadas en versiones de 4, 3, 2 o 1 dosis, cobro 2 coins por cada vial normal, 2 coins por cada vial de juju y 15 coins por cada vial de powerburst.
  - [Choice]: Lo siento, tengo que irme.
    - **Rhobert Dail (hierbas):** Está bien, estaré aquí si alguna vez me necesitas, hipnotizado por la voz de la dama.

#### Opción de decantar

- ((Lo siguiente se muestra en una interfaz titulada "Opciones de Decantación":))
  - [Choice]: Decantar viales
    - [Menu]: ¿En cuántas dosis quieres decantar?
      - [Choice]: una dosis
        - (Condition: Con pociones decantables en backpack:)
          - **Rhobert Dail (hierbas):** Ahí lo tienes, amigo.
        - (Condition: Sin pociones decantables en backpack:)
          - **Rhobert Dail (hierbas):** Lo siento, no sé cómo decantar nada de lo que llevas.
        - (Condition: Sin suficiente dinero para viales adicionales:)
          - **Rhobert Dail (hierbas):** Lo sentimos, no tienes suficiente dinero para pagar suficientes viales vacíos.
        - (Condition: Sin espacio en backpack para viales extra:)
          - **Rhobert Dail (hierbas):** Tu inventario está demasiado lleno para que pueda hacer algo por ti.
      - [Choice]: Dos dosis
        - (arriba)
      - [Choice]: Tres dosis
        - (arriba)
      - [Choice]: Cuatro dosis
        - (arriba)
  - [Choice]: Decantar matraces
    - (Condition: Sin frascos viables de pociones para decantar:)
      - **Rhobert Dail (hierbas):** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener 2 matraces que no estén completamente llenos!
    - (Condition: Con matraces para decantar:)
      - **Rhobert Dail (hierbas):** Veamos qué tienes. Decantaré sus frascos de poción nuevamente en 6 frascos dosificados. Puedo hacer uso de los frascos, así que los aceptaré como pago.
      - (Action: Rhobert decanta tantas como puede hasta llenar frascos de 6 dosis)
      - **Rhobert Dail (hierbas):** Aquí tienes. ¡Eso es lo mejor que puedo hacer! Si los matraces no se ven muy diferentes, los limpié.
  - [Choice]: Convertir viales en matraces
    - (Condition: Sin matraces vacíos en backpack:)
      - **Rhobert Dail (hierbas):** Tendrás que proporcionar los frascos vacíos tú mismo; no son baratos. Puedes traérmelos anotados o sin anotaciones.
    - (Condition: Con matraces vacíos en backpack:)
      - **Rhobert Dail (hierbas):** Veamos qué tienes. Decantaré los viales de poción y todos los frascos hasta 4 dosis en frascos de 6 dosis. Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos.
      - (Condition: Con pociones para decantar en matraces:)
        - (Action: Rhobert decanta tantas pociones como puede hasta llenar frascos de 6 dosis.)
        - **Rhobert Dail (hierbas):** Aquí tienes. ¡Eso es lo mejor que puedo hacer!
      - (Condition: Sin pociones que decantar:)
        - **Rhobert Dail (hierbas):** ¡Lo siento, parece que no tienes nada en lo que pueda ayudarte! Asegúrate de tener las pociones correctas y algo de espacio libre en tu inventario y podré intentarlo de nuevo.
  - [Choice]: Convertir matraces en viales
    - (Condition: Sin frascos viables de pociones para decantar:)
      - **Rhobert Dail (hierbas):** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener al menos 1 matraz!
    - (Condition: Con frascos de pociones para decantar a viales:)
      - **Rhobert Dail (hierbas):** Por supuesto. Creo que puedo utilizar los matraces, así que te daré los viales gratis.
      - (Action: Rhobert decanta tantas pociones como puede en viales destacados.)
      - **Rhobert Dail (hierbas):** Ahí lo tienes, ¡eso es lo mejor que puedo hacer!
  - [Choice]: Cancelar
    - ((La interfaz se cierra.))
