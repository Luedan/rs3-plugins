# Iffie

- **Original Wiki Page**: [Transcript:Iffie](https://runescape.wiki/w/Transcript%3AIffie)
- **Letter**: `I`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Varrock


#### Normalmente

- **Iffie:** ¡Hola, cariño! ¿Querías coleccionar un disfraz o hay algo más que pueda hacer por ti hoy?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: He venido por un disfraz.
    - **Iffie:** Quizás pueda encontrar tus disfraces fantasmales perdidos o tengo mi tienda de disfraces. ¿Cuál quieres?
    - [Menu]: Selecciona una opción
      - [Choice]: Uno de mis disfraces fantasmales.
        - ''(Se abre la interfaz de recuperación.)
      - [Choice]: Un disfraz de tu tienda.
        - **Iffie:** ¡Algunos de estos disfraces incluso vienen con un gesto gratis!
        - **Iffie:** Solo compra una pieza de los disfraces de mimo o zombi y te mostraré todos los movimientos relevantes.
        - (opens=Iffie's Random Costume Shop)
  - [Choice]: ¿No estás vendiendo nada?
    - **Player:** ¿No estás vendiendo nada?
    - **Iffie:** Ah, sí, pero solo disfraces. Thessalia vende otras prendas y gestiona el servicio makeover mage.
  - [Choice]: Sólo vine para charlar.
    - **Player:** Sólo vine para charlar.
    - **Iffie:** Oh, lo siento, ¡pero nunca terminaré de tejer si me detengo a charlar con cada joven [lad/lass] que deambula por la tienda!
    - **Iffie:** Deberías ir a ver a mi hermana, Elsie, arriba en la iglesia Varrock; ella siempre está lista para una buena charla.
  - [Choice]: cond=If the player is eligible for the classic cape:|Estoy aquí para hablar de lo que estás tejiendo.
    - **Player:** Estoy aquí para hablar de lo que estás tejiendo.
    - **Iffie:** ¿Esto? He estado tejiendo todo tipo de cosas, principalmente cosas que me recuerdan los buenos tiempos.
    - (Condition: Condition unknown:)
      - **Iffie:** Puede que seas más joven que yo, pero ¿quizás también quieras una capa que te recuerde a los viejos tiempos?
      - (continue)
    - (Condition: Condition unknown:)
      - **Iffie:** Y veo que eres un veterano de los viejos tiempos. ¿Te gustaría una capa que te recuerde los viejos tiempos?
      - (continue)
    - **Iffie:** Tejer tiene un precio: requiere bastante esfuerzo y materiales. ¿Te parece bien 50.000 coins, querida?
    - [Menu]: ¿Pagar 50.000 por una capa clásica?
      - [Choice]: ¡Me llevaré uno!
        - **Player:** ¡Me quedo con uno!
        - (Condition: If the player does not have enough coins:)
          - **Iffie:** Eso está bien, pero no tienes suficiente dinero para la capa.
        - (Condition: If the player does not have space in backpack:)
          - **Iffie:** Eso está bien, pero no tienes espacio en tu inventario para la capa y la capucha.
        - (Condition: If the player has enough coins:)
          - (removes=50,000 coins) (receives=classic cape and classic hood)
          - **Iffie:** Gracias. ¡Disfrutar!
      - [Choice]: No, gracias.
        - **Player:** No, gracias.

#### Durante la promoción Ghostweave

- **Iffie:** ¡Hola, cariño! ¿Querías coleccionar un disfraz o hay algo más que pueda hacer por ti hoy?
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Qué puedo hacer con el tejido fantasma?
    - **Iffie:** ¡Tejido fantasma! Hace mucho tiempo que no veo eso. Puedes hacer disfraces con él y puedes parecer un fantasma aterrador.
    - **Iffie:** Aunque se necesita bastante, cariño, dependiendo del disfraz que quieras.
    - **Iffie:** También puedes intercambiar tejido fantasma por chocolates especiales de Halloween que tienen efectos interesantes.
    - **Iffie:** Después del evento, puedes traerme cualquier tejido fantasma no utilizado y lo cambiaré por Crafting XP.
    - *(Durante la promoción principal:)*
      - **Iffie:** Quizás más adelante compre el tejido fantasma que te quede, pero deberías intentar hacer chocolates o disfraces con él ahora.
    - *(Después de la promoción principal :)*
      - *(Sin tejido fantasma en backpack :)*
        - **Iffie:** Te compraré los que te sobren o puedes convertirlos en chocolates tú mismo.
      - *(Con tejido fantasma en backpack :)*
        - **Iffie:** Ese tejido fantasma ya no durará mucho más. ¿Quieres venderme tu tejido fantasma de repuesto? Te daré 40 coins o un poco de capacitación en artesanía por cada pieza que tengas.
        - **Iffie:** También puedes intercambiar tejido fantasma por chocolates especiales de Halloween que tienen efectos interesantes.
        - [Menu]: ¿Vender tejido fantasma?
          - [Choice]: Vender todo ([N]) por oro [40N]
          - **Iffie:** Ahí tienes, querida. Eso es [40N] coins. No los gastes todos a la vez.
            - [40N] coins se han agregado a su bolsa de dinero.
          - [Choice]: Vender X por oro (40 cada uno)
            - *(Después de ingresar el monto:)*
              - **Iffie:** Ahí tienes, querida. Eso es [40N] coins. No los gastes todos a la vez.
              - [40N] coins se han agregado a su bolsa de dinero.
          - [Choice]: Vende todo ([N]) para obtener XP extra de [20N]
            - **Iffie:** Ahí tienes, querida. Estoy seguro de que serás mejor haciendo manualidades con un poco de práctica.
            - Has ganado puntos de experiencia adicionales [20N] en la habilidad Crafting.
          - [Choice]: Vende X para obtener Crafting XP extra (20 cada uno)
            - *(Después de ingresar el monto:)*
              - **Iffie:** Ahí tienes, querida. Estoy seguro de que serás mejor haciendo manualidades con un poco de práctica.
            - Has ganado puntos de experiencia adicionales [20N] en la habilidad Crafting.
          - [Choice]: no vender
            - **Iffie:** Está bien, querida, pero no durará mucho, así que decide pronto qué quieres hacer con él.
  - [Choice]: He venido por un disfraz.
    - (arriba)
  - [Choice]: ¿No estás vendiendo nada?
    - (arriba)
  - [Choice]: Sólo vine para charlar.
    - (arriba)

#### Realizar el gesto Muro de cristal con el traje de mimo equipado durante la tarea de celebración del 25.º aniversario

- **Iffie:** Oh, no esa tontería de Mime otra vez. ¿Cuántas veces tengo que copiarte antes de que me dejes solo?
- **Player:** Oh, espera, lo siento, no soy el Mime. Este no es algún tipo de evento aleatorio.
- **Iffie:** Oh, gracias a Dios. Todos estos extraños extraños aparecen, esperando que actuemos.
- **Iffie:** Supongo que ha pasado un tiempo desde que dejaron de venir. Al menos tenía alguien con quien hablar...
- {{RSFontAchievement|So Random|Perform the 'Glass Wall' emote while wearing the full Mime outfit inside of Thessalia's Fine Clothes in Varrock.}}
- ((Shown in a task completion pop-up:))
  - {{Colour|#F0BE79| TAREA DEL 25 ANIVERSARIO |#181513}}
  - tan aleatorio
  - Realiza el gesto 'Glass Wall' mientras usas el atuendo completo de Mime dentro de Fine Clothes de Thessalia en Varrock.
  - (continue)
- **Iffie:** Nunca sabes lo que te perderás hasta que desaparece.
- (Condition: If all the tasks have been completed:)
  - **Player:** Parece que he completado todo. ¡Será mejor que vaya a ver a Hans sobre esa recompensa!
