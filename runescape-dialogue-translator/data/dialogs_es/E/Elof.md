# Elof

- **Original Wiki Page**: [Transcript:Elof](https://runescape.wiki/w/Transcript%3AElof)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talking to Elof


#### Si habla con Elof sin un folleto del taller de Artisan con usted

- **Player:{{anchor|standard}}** Hola. ¿Qué haces aquí?
- **Elof:** Puedo intercambiar fichas de metal por ti, personalizar un conjunto de armadura de obra maestra recortada o agregar púas a tu armadura personalizada.<div id="Standard"></div>
- [Menu]: Selecciona una opción
  - [Choice]: Fichas metálicas
    - **Elof:** ¿Qué son las fichas de metal, te preguntarás? Bueno, hicimos un gran retiro de algunos de los artículos de herrería más antiguos, ¡debido a las peligrosas condiciones de herrería cuando fueron creados!
    - **Elof:** Como tal, hemos reemplazado los artículos con fichas del tipo de metal apropiado, que puedes comprarme si tienes alguna ficha.
    - [Menu]: ¿Alguna otra pregunta?
      - [Choice]: ¿Cómo puedo obtener más tokens?
        - **Elof:** No puedes obtener más tokens. Sólo hicimos el retiro una vez.
        - (previous)
      - [Choice]: ¿Puedo intercambiar estos tokens?
        - **Elof:** No, no puedes intercambiar estos tokens, pero puedes intercambiar los artículos que puedes obtener al intercambiar los tokens.
        - (previous)
      - [Choice]: ¿Qué pasa si quiero recuperar mis cosas viejas?
        - **Elof:** Deberías poder volver a comprar la mayoría de tus artículos con los tokens que hemos intercambiado por ti. Sin embargo, si no puedes, ahora deberías poder forjar tus objetos antiguos a un nivel mucho más bajo.
        - (previous)
      - [Choice]: Quiero intercambiar estos tokens.
        - **Elof:** ¿Qué tipo de tokens te gustaría intercambiar?
        - [Menu]: Selecciona una opción
          - [Choice]: Acero.
            - (opens=Steel item token exchange)
          - [Choice]: Mitril.
            - (opens=Mithril item token exchange)
          - [Choice]: Inflexible.
            - (opens=Adamant item token exchange)
          - [Choice]: Runa.
            - (opens=Rune item token exchange)
      - [Choice]: No.
        - (end)
    - [Choice]: Armadura maestra hecha a medida.
      - (below|custom)

#### Si habla con Elof con un folleto del taller de Artisan consigo

- **Elof:** Ah, veo que tienes un folleto del Taller de artesanos. ¡A cambio, tengo un paquete exclusivo de artículos de muestra para ti! ¡Necesitarás 11 espacios en tu backpack!
- [Menu]: ¿Canjear folleto?
  - [Choice]: Sí.
    - *(Si tienes suficiente espacio en tu backpack:)*
      - Elof arruga tu volante hasta convertirlo en una bola apretada y se lo mete en la boca. ¡Masticando pensativamente, te otorga una generosa variedad de suministros Mining y Smithing!
      - **Player:** ¡Guau, gracias!<br>¿Hay algo más que puedas darme?<!--It's split into two lines in one dialogue box as per in-game-->
      - (continuea|standard)
    - *(Si no tienes suficiente espacio en tu backpack:)*
      - **Elof:** ¡Vuelve con 11 espacios en tu backpack y te daré tus cosas gratis!
  - [Choice]: No.
    - (continuea|standard)

### "Metal token exchange" option

- **Elof:**¿Qué tipo de tokens te gustaría intercambiar?
- [Menu]: ¿Intercambiar qué tokens?
  - [Choice]: Acero.
    - (opens=Steel item token exchange)
  - [Choice]: Mitril.
    - (opens=Mithril item token exchange)
  - [Choice]: Inflexible.
    - (opens=Adamant item token exchange)
  - [Choice]: Runa.
    - (opens=Rune item token exchange)

### "Custom-fit Trimmed Masterwork" option

- **Elof:{{anchor|custom}}** Si tienes un juego de obras maestras recortadas totalmente equipado, puedo personalizarlo para ti. Si está aumentado, permanecerá aumentado y lo repararás de la misma manera que reparas una obra maestra recortada.
- **Player:** ¿Qué hace el ajuste personalizado?
- **Elof:** Se volverá intransferible.
- **Elof:** Se degradará un 50 % más lento, por lo que durará más.
- **Elof:** Tampoco se degradará nunca mientras estés en una tarea de cazador o segador.
- **Elof:** Pero el proceso es irreversible. Una vez hecha a medida, su obra maestra siempre estará hecha a medida.
- *(Si llevas un juego completo de obra maestra recortada:)*
  - [¿Estás seguro de que quieres personalizar tu armadura Trimmed Masterwork?<br />Este proceso los hará permanentemente intransferibles, hará que se degraden un 50% más lento y nunca se degradarán cuando estés en una tarea de cazador o segador.]
  - [Menu]: ¿Perfeccionar tu obra maestra recortada a la medida?
    - [Choice]: si
      - (removes=the equipped trimmed masterwork armour set) (receives=custom-fit trimmed masterwork armour set)
    - [Choice]: No
      - (end)
- *(Si no llevas un conjunto completo de obra maestra recortada:)*
  - [Debes llevar un juego completo de obra maestra recortada para poder personalizarlo.

### "Spiked Masterwork armour" option

- **Elof:** Hola. Puedo agregar o quitar púas de tu armadura maestra personalizada.
- [Menu]: ¿Quieres agregar o quitar púas de tu armadura?
  - [Choice]: Añadir
    - *(Si no tienes ninguna pieza de armadura maestra hecha a medida equipada:)*
      - [Debes llevar al menos una pieza de armadura elegible para que pueda modificarla.]
    - *(Si tienes equipadas piezas de armadura maestra hechas a medida:)*
      - [Menu]: ¿Estás seguro de que quieres agregar púas a tu armadura Masterwork personalizada? Este proceso te costará X barras gloriosas.
        - [Choice]: si
          - (removes=the equipped custom-fit trimmed masterwork armour set) (receives=custom-fit trimmed spiked masterwork armour set)
        - [Choice]: No
          - (end)
  - [Choice]: Quitar
    - *(Si no tienes ninguna pieza de armadura con púas equipada:)*
      - [Debes llevar al menos una pieza de armadura elegible para que pueda modificarla.]

### At Thalmund's forge

- ((Se ve una de las siguientes secuencias.))

#### Secuencia 1

- (Elof aparece en las puertas del norte).
- (Elof camina hacia los escombros en el sur).
- **Elof:** {{RSChat|Needs a clean.}}
- (Elof camina hacia la palanca.)
- **Elof:** {{RSChat|Smells like pie and slag.}}
- (Elof camina hacia la habitación con el yunque imcando y lo investiga.)
- (Elof camina hacia el horno.)
- **Elof:** {{RSChat|Impressive.}}
- (Elof camina hacia el estante de armas de los duendes, lo investiga y se teletransporta.)

#### Secuencia 2

- (Elof aparece en las puertas del norte).
- (Elof camina hacia los escombros en el sur).
- **Elof:** {{RSChat|What a mess!}}
- (Elof camina hacia la palanca.)
- **Elof:** {{RSChat|Hmmm...}}
- (Elof camina hacia la habitación con el yunque imcando y lo investiga.)
- (Elof camina hacia el horno.)
- **Elof:** {{RSChat|Not bad.}}
- (Elof camina hacia el estante de armas de los duendes, lo investiga y se teletransporta.)
