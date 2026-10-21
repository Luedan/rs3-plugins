# Bob Barter (herbs)

- **Original Wiki Page**: [Transcript:Bob Barter (herbs)](https://runescape.wiki/w/Transcript%3ABob%20Barter%20%28herbs%29)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before doing the Grand Exchange tutorial

- **Player:{{anchor|hello}}** Hola.
- **Bob Trueque (hierbas):** Amigo, todavía no tengo tiempo para ti. Te sugiero que hables con Brugsen Bursen o Grand Exchange Tutor cerca de la entrada para recibir una lección. Brugsen dará una lección interesante sobre Grand Exchange y el Tutor dará una lección más sencilla y sencilla.

#### Opción de información-hierba

- **Bob Trueque (hierbas):** Primero necesitarás un poco de entrenamiento, amigo. Te sugiero que hables con Brugsen Bursen o Grand Exchange Tutor cerca de la entrada para recibir una lección. Brugsen dará una lección interesante sobre Grand Exchange y el Tutor dará una lección más breve y sencilla.

#### Opción de decantar

- (arriba2|hola)

### After doing the Grand Exchange tutorial

- **Player:** Hola.
- **Bob Trueque (hierbas):** Hola, amigo, ¿te apetece comprar joyas de diseño? ¡Vienen desde Ardougne! ¡Más pukka!
- **Player:** ejem, no. Estoy listo, gracias.
- **Bob Trueque (hierbas):** Está bien, amigo, entonces, ¿qué puedo hacer por ti? Puedo decirte los últimos precios de las hierbas, o tal vez pueda ayudarte a decantar tus pociones.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Bob Trueque (hierbas):** ¡Vaya, soy Bob! ¡Tu amigable vendedor de productos sensacionales!
    - **Player:** Entonces, ¿qué tienes para vender?
    - **Bob Trueque (hierbas):** Oh, no mucho por el momento. Porque, ya sabes. El negocio va muy bien y cómodo.
    - **Player:** Realmente no parece que estés teniendo tanto éxito.
    - **Bob Trueque (hierbas):** ¡Plonka! ¡Es todo un espectáculo, no! ¡Si le hago saber a la gente que estoy en un buen negocio, querrán una parte del dinero!
    - **Player:** Convenientemente tienes una respuesta para todo.
    - **Bob Trueque (hierbas):** Esa es la manera Ardougne, hijo mío.
    - (initial)
  - [Choice]: ¿Puedes...?
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Puedes decantarme algunas pociones?
        - (abajo2|Decantar opción 2)
      - [Choice]: ¿Ayudame con los precios de las hierbas?
        - ((Precios indicativos: se abren las hierbas.))
      - [Choice]: Dime el costo para decantar pociones?
        - **Bob Trueque (hierbas):** Si quieres pociones decantadas en versiones de 4, 3, 2 o 1 dosis, cobro 2 coins por cada vial normal, 2 coins por cada vial de juju y 2 coins por cada vial de powerburst.
      - [Choice]: ¿Dime qué puedo hacer con los viales vacíos?
        - **Player:** ¿Puedes decirme qué puedo hacer con los viales vacíos?
        - **Bob Trueque (hierbas):** ¡Por qué seguro! Cuando termine su última dosis, puede conservar el vial o simplemente tirarlo.
        - [Menu]: Al terminar la última dosis, ¿qué le gustaría hacer?
          - [Choice]: Guarde el vial.
            - color = blanco
          - [Choice]: Deseche el vial.
            - color = blanco
      - [Choice]: Lo siento, tengo que irme.
        - (below|split)
  - [Choice]: Lo siento, tengo que irme.
    - **Player:** Lo siento, tengo que irme.
    - **Bob Trueque (hierbas):** ¿Comprar plátanos, entonces?
    - **Player:** ¿Qué?
    - **Bob Trueque (hierbas):** Ya sabes, ¿dividir? ¿Banana? ¿Banana split?
    - **Player:** Jajaja. No esperes. Eso no es gracioso.

#### Opción de información-hierbas

- ((Precios indicativos: se abren las hierbas.))

#### Opción de decantar

- ((Lo siguiente se muestra en una interfaz titulada "Opciones de Decantación":))
  - [Choice]: Decantar viales
    - [Menu]: ¿En cuántas dosis quieres decantar?
      - [Choice]: una dosis
        - (Condition: Con pociones decantables en backpack:)
          - **Bob Trueque (hierbas):** Ahí lo tienes, amigo.
        - (Condition: Sin pociones decantables en backpack:)
          - **Bob Trueque (hierbas):** Lo siento, no puedo hacer nada con [that potion/those potions].
        - (Condition: Sin suficiente dinero para viales adicionales:)
          - **Bob Trueque (hierbas):** Lo sentimos, no tienes suficiente dinero para pagar suficientes viales vacíos.
        - (Condition: Sin espacio en backpack para viales extra:)
          - **Bob Trueque (hierbas):** Tu inventario está demasiado lleno para que pueda hacer algo por ti.
      - [Choice]: Dos dosis
        - (arriba)
      - [Choice]: Tres dosis
        - (arriba)
      - [Choice]: Cuatro dosis
        - (arriba)
  - [Choice]: Decantar matraces
    - (Condition: Sin frascos viables de pociones para decantar:)
      - **Bob Trueque (hierbas):** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener 2 matraces que no estén completamente llenos!
    - (Condition: Con matraces para decantar:)
      - **Bob Trueque (hierbas):** A ver qué tienes. Decantaré sus frascos de poción nuevamente en 6 frascos dosificados. Puedo hacer uso de los frascos, así que los aceptaré como pago.
      - (Action: Bob decanta tantas como puede hasta llenar frascos de 6 dosis)
      - **Bob Trueque (hierbas):** Aquí tienes. ¡Eso es lo mejor que puedo hacer! Si los matraces no se ven muy diferentes, los limpié.
  - [Choice]: Convertir viales en matraces
    - (Condition: Sin matraces vacíos en backpack:)
      - **Bob Trueque (hierbas):** Tendrás que suministrar los frascos vacíos tú mismo; no son baratos. Puedes traérmelos anotados o sin anotaciones.
    - (Condition: Con matraces vacíos en backpack:)
      - **Bob Trueque (hierbas):** A ver qué tienes. Decantaré los viales de poción y todos los frascos hasta 4 dosis en frascos de 6 dosis. Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos.
      - (Condition: Con pociones para decantar en matraces:)
        - (Action: Bob decanta tantas pociones como puede hasta llenar frascos de 6 dosis)
        - **Bob Trueque (hierbas):** Aquí tienes. ¡Eso es lo mejor que puedo hacer!
      - (Condition: Sin pociones que decantar:)
        - **Bob Trueque (hierbas):** ¡Lo siento, parece que no tienes nada en lo que pueda ayudarte! Asegúrate de tener las pociones correctas y algo de espacio libre en tu inventario y podré intentarlo de nuevo.
  - [Choice]: Convertir matraces en viales
    - (Condition: Sin frascos viables de pociones para decantar:)
      - **Bob Trueque (hierbas):** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener al menos 1 matraz!
    - (Condition: Con frascos de pociones para decantar a viales:)
      - **Bob Trueque (hierbas):** Por supuesto. Creo que puedo utilizar los matraces, así que te daré los viales gratis.
      - (Action: Bob decanta tantas pociones como puede en viales destacados.)
      - **Bob Trueque (hierbas):** Ahí lo tienes, ¡eso es lo mejor que puedo hacer!
  - [Choice]: Cancelar
    - ((La interfaz se cierra.))

### Overhead dialogue

- {{Trandom}}
- **Bob Trueque (hierbas):** {{RSChat|Now, what should I buy?}}
- **Bob Trueque (hierbas):** {{RSChat|I'm in the money!}}
- **Bob Trueque (hierbas):** {{RSChat|I could have sworn that would have worked.}}
- **Bob Trueque (hierbas):** {{RSChat|Hope this item sells well.}}
- **Bob Trueque (hierbas):** {{RSChat|Please, please, please work.}}
