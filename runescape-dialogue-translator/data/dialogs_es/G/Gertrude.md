# Gertrude

- **Original Wiki Page**: [Transcript:Gertrude](https://runescape.wiki/w/Transcript%3AGertrude)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### West of Varrock


#### Normalmente

- [Menu]: Elige una opción:
  - [Choice]: ¿Tienes más gatitos?
    - **Player:** ¿Tienes más gatitos?
    - (Condition: Si el player ya tiene un gatito:)
      - **Gertrude:** ¿No sigues criando a ese otro gatito? Sólo una vez que haya crecido por completo y ya no necesite tu atención, te dejaré tener otro gatito.
    - (Condition: Si el player no tiene un gatito:)
      - **Gertrude:** De hecho, sí. Son 100 coins cada uno, ¿quieres uno?
      - (Condition: Si el player no tiene 100 coins:)
        - **Player:** Vaya, parece que soy un poco bajo. Volveré más tarde.
      - (Condition: Si el player tiene 100 coins:)
        - [Menu]: Selecciona una opción
          - [Choice]: Acepta el gatito ofrecido.
            - (removes=100 coins)
            - (receives=pet kitten)
            - Gertrude te regala otro gatito.
          - [Choice]: No compres un gatito.
            - **Player:** No, gracias.
          - [Choice]: cond=With a ring of charos (a) equipped|[Charm] Pide elegir tu propio gatito.
            - **Gertrude:** Bueno, está bien, pero todos son igual de tiernos entre sí.
            - (abre=Gato#Galería{{!)Kitten selection}}
            - (removes=100 coins)
            - (receives=pet kitten)
            - Gertrude te regala otro gatito.
  - [Choice]: ¿Puedes decirme cómo cuidar a mi gato?
    - **Player:** ¿Puedes decirme cómo cuidar a mi gato?
    - **Gertrude:** Me alegra mucho que lo hayas preguntado. ¿Qué es lo que necesitas saber?
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué debo alimentar a mi gato?{{anchor|cat-food}}
        - **Player:** ¿Qué debo alimentar a mi gato?
        - **Gertrude:** Descubrirás que la mayoría de los tipos de peces ayudarán a que tu gato siga creciendo y feliz, aunque no creo que a Fluffs le gusten mucho las anguilas. En cuanto a bebida, lo mejor son los cubos de leche. Recuerde, si no alimenta a su gato, es probable que se escape; es comprensible, de verdad.
        - **Player:** Gracias por el consejo.
        - **Gertrude:** ¿Hay algo más que necesites saber?
        - [Menu]: Selecciona una opción
          - [Choice]: No, gracias. Me voy ahora.{{anchor|im-off}}
            - **Player:** No, gracias. Me iré ahora.
          - [Choice]: ¿Cómo puedo mantener feliz a mi gato?
            - (below|happy-cat)
          - [Choice]: ¿Qué tipos de gatos hay?
            - (below|cat-types)
      - [Choice]: ¿Cómo puedo mantener feliz a mi gato?{{anchor|happy-cat}}
        - **Player:** ¿Cómo puedo mantener feliz a mi gato?
        - **Gertrude:** Puedes acariciarlo, por supuesto. A todos los gatos les gusta que los acaricien. Si te sientes con un poco más de energía puedes jugar con ovillos de lana; los gatos disfrutan jugando con ellos.
        - **Gertrude:** También he oído que los artesanos expertos pueden hacer ratones mecánicos como juguetes para gatos. <br>Si todo esto te parece demasiado esfuerzo, recuerda que un gato aburrido huirá en busca de aventuras.
        - **Player:** Gracias por el consejo.
        - **Gertrude:** ¿Hay algo más que necesites saber?
        - [Menu]: Selecciona una opción
          - [Choice]: No, gracias. Me iré ahora.
            - (above|im-off)
          - [Choice]: ¿Qué debo alimentar a mi gato?
            - (above|cat-food)
          - [Choice]: ¿Qué tipos de gatos hay?
            - (below|cat-types)
      - [Choice]: ¿Qué tipo de gato hay?{{anchor|cat-types}}
        - **Player:** ¿Qué tipo de gato hay?
        - **Gertrude:** Bueno, sabes que un gatito se convertirá en gato si lo alimentas y lo tratas bien. Sin embargo, puedes ir un poco más lejos y terminar con un gato demasiado grande.
        - **Gertrude:** He oído que existen métodos secretos para entrenar a un gato demasiado grande para que se convierta en un gato astuto. Sin embargo, debes mantener a los gatos astutos alerta, o pueden convertirse fácilmente en gatos perezosos. Aún más extremos son los hellcats; Si tu gato come demasiadas ratas infernales, ¡se convertirán en una! Por suerte, un trago de leche soluciona este problema.
        - **Player:** Gracias por el consejo.
        - **Gertrude:** ¿Hay algo más que necesites saber?
        - [Menu]: Selecciona una opción
          - [Choice]: No, gracias. Me iré ahora.
            - (above|im-off)
          - [Choice]: ¿Cómo puedo mantener feliz a mi gato?
            - (above|happy-cat)
          - [Choice]: ¿Con qué debo alimentar a mi gato?
            - (above|cat-food)
  - [Choice]: cond=After catching 100 rats and without a cat training medal:|Dile a Gertrude que tu gato ha atrapado 100 ratas.
    - **Player:** ¡Hola de nuevo Gertrude!
    - **Gertrude:** Bueno, ¡hola aventurero! ¿Cómo estás?
    - **Player:** ¡Mi gato ha atrapado 100 ratas!
    - **Gertrude:** ¡Bien, bien! ¡Eres bueno con los gatos!
    - **Gertrude:** Aquí tengo un pequeño regalo para ti.
    - (receives=Cat training medal)
    - Gertrude te entrega una pequeña medalla.
    - (Condition: Si es la primera vez que reclamas la medalla:)
      - {{RSFontAchievement|Faster, Pussycat! Kill! Kill!}}
      - (continue)
    - **Player:** Hola, gracias Gertrude.
  - [Choice]: cond=With a hellcat out:|¿Qué le pasó a mi gato?
    - **Player:** ¿Qué le pasó a mi gato?
    - **Gertrude:** Oh, Dios mío. Has estado dejando que se coma seres demoníacos, ¿no? No te preocupes, solo dale un trago de leche y estará como la lluvia.
  - [Choice]: cond=After Ratcatchers:|Habla sobre la misión 'Ratcatchers'.
    - **Gertrude:** ¿Alguna vez hablaste con esas personas de las que te hablé?
    - **Player:** Sí, gente extraña. Pero interesante de todos modos.

#### Durante las celebraciones del 25 Aniversario tarea con un seguidor de gatos

- **Gertrude:** Espero que estés cuidando bien a este lindo bebé.
- **Player:** ¡Claro que sí!
- **Gertrude:** Estaba hablando con tu gato.
- **Player:** Ah, claro.
- {{RSFontAchievement|Gertrude's Cat|Talk to Gertrude while you have a cat follower.}}
- ((Se muestra en una ventana emergente de finalización de tarea:))
  - {{Colour|#F0BE79| TAREA DEL 25 ANIVERSARIO |#181513}}
  - El gato de Gertrude
  - Habla con Gertrude mientras tengas un seguidor de gatos.
  - (continue)
- **Player:** Puedo asegurarles que estoy bien alimentado y recibo mucha atención.
- (Condition: Si se han completado todas las tareas:)
  - **Player:** Parece que he completado todo. ¡Será mejor que vaya a ver a Hans sobre esa recompensa!

### In New Varrock


#### Antes del regreso de mamá

- **Gertrude:** Los he perdido.<br>¡Los he perdido todos!
- [Menu]: Elige una opción:
  - [Choice]: ¿A quién has perdido?
    - **Gertrude:** Primero fue Fluffs, mi querido amigo felino. Llevaba casi una década ronroneando a mi lado.
    - **Gertrude:** No había nadie aquí para ayudar, así que envié a mis hijos mayores, Wilough y Shilop, a buscarla.
    - **Gertrude:** Ese fue el día en que llegó el demonio... mis pobres muchachos. Cuando el terror rojo irrumpió en el suelo de la plaza, fueron los primeros en ser capturados.
    - **Gertrude:**Después del... funeral, estaba muy molesto. No debería haber ido a la ciudad, no con el demonio todavía cerca, pero me sentía muy sola.
    - **Gertrude:** Solo salí de casa por un rato. Me aseguré de que mis hijos Philop y Kanel estuvieran bien alimentados y que la puerta estuviera bien cerrada.
    - **Gertrude:** Apenas había puesto un pie en la plaza cuando los muertos marcharon hacia Varrock. La guardia de la ciudad selló las puertas para intentar mantenerlos fuera.
    - **Gertrude:** No me dejaron volver por mis pequeños Philop y Kanel. Cuando las puertas cayeron y la batalla terminó, ya era demasiado tarde.
    - **Gertrude:** Mi casa era una ruina humeante y mis hijos no estaban por ningún lado.
    - **Gertrude:** Después de que el nigromante tomó el control, me mudé a este edificio, ya que no tenía otro lugar donde quedarme. Adopté uno de los perros callejeros, tratando de llenar el vacío de mi alma.
    - **Gertrude:** Lo amé y lo acaricié, pero ha cambiado, bendito sea. Intenta morderme y solo come carne cruda.
    - (Condition: Si el player ya le ha tomado la sardina a Dimies:)
      - **Gertrude:** ¡Y ahora mi pez mascota, mis pobres pequeños Dimies, también ha desaparecido! Es desgarrador...
      - (continue)
    - **Gertrude:** Ah, pero no quiero molestarte con los problemas de una vieja solterona tonta y su trágico pasado. No es que puedas hacer algo para ayudar. <br>¿Qué es lo que querías?
    - (initial)
  - [Choice]: ¿Estás vendiendo algo?
    - **Gertrude:** ¿Vendo?<br>Bueno, podría ofrecerte una comida caliente o un rico y delicioso pastel de chocolate. <br>Cocinar es mi manera de mantenerme ocupado hoy en día...
    - (opens=Gertrude's Food)
  - [Choice]: Adiós.
    - **Gertrude:** Oh... ¿te vas tan pronto? <br>Me encanta un poco de compañía. He estado tan solo...

#### Después del regreso de la momia

- **Gertrude:** Gracias por devolver a Fluffs a casa. ¡Ella me contó todo!
- [Menu]: Elige una opción:
  - [Choice]: ¿A quién has perdido?
    - **Gertrude:** Primero fue Fluffs, mi querido amigo felino. Llevaba casi una década ronroneando a mi lado.
    - **Gertrude:** No había nadie aquí para ayudar, así que envié a mis hijos mayores, Wilough y Shilop, a buscarla.
    - **Gertrude:** Ese fue el día en que llegó el demonio... mis pobres muchachos. Cuando el terror rojo irrumpió en el suelo de la plaza, fueron los primeros en ser capturados.
    - **Gertrude:**Después del... funeral, estaba muy molesto. No debería haber ido a la ciudad, no con el demonio todavía cerca, pero me sentía muy sola.
    - **Gertrude:** Solo salí de casa por un rato. Me aseguré de que mis hijos Philop y Kanel estuvieran bien alimentados y que la puerta estuviera bien cerrada.
    - **Gertrude:** Apenas había puesto un pie en la plaza cuando los muertos marcharon hacia Varrock. La guardia de la ciudad selló las puertas para intentar mantenerlos fuera.
    - **Gertrude:** No me dejaron volver por mis pequeños Philop y Kanel. Cuando las puertas cayeron y la batalla terminó, ya era demasiado tarde.
    - **Gertrude:** Mi casa era una ruina humeante y mis hijos no estaban por ningún lado.
    - **Gertrude:** Después de que el nigromante tomó el control, me mudé a este edificio, ya que no tenía otro lugar donde quedarme. Adopté uno de los perros callejeros, tratando de llenar el vacío de mi alma.
    - **Gertrude:** Lo amé y lo acaricié, pero ha cambiado, bendito sea. Intenta morderme y solo come carne cruda.
    - **Gertrude:** ¡Y ahora mi pez mascota, mis pobres pequeños Dimies, también ha desaparecido! Es desgarrador...
    - **Gertrude:** Ah, pero no quiero molestarte con los problemas de una vieja solterona tonta y su trágico pasado. Fluffs está en casa ahora y eso me ha animado.
    - (initial)
  - [Choice]: ¿Cómo es Fluffs?
    - **Gertrude:** ¡Oh, es como en los viejos tiempos! <br> ¡Estaremos juntos durante décadas!
    - **Gertrude:** Aunque a veces dice las cosas más extrañas: devorar almas y cosas así, pero...
    - **Gertrude:** ¡Ella también trajo a casa a sus gatitos! Han estado viviendo perdidos en Varrock y nunca lo supe. Están todos arriba.
    - **Gertrude:** Alguien se llevó mi pescado, mi pobre sardina, Dimies. Otra trágica pérdida...
    - **Gertrude:** Aunque es mejor. De todos modos, los gatos ya se lo habrían comido.
    - **Gertrude:** Y uno de los gatitos me regaló este extraño libro sobre gatos. Es muy interesante...
    - (initial)
  - [Choice]: ¿Estás vendiendo algo?
    - (arriba)
  - [Choice]: Adiós.
    - **Gertrude:** ¡Vuelve pronto!
