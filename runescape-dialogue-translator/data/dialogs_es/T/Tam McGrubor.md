# Tam McGrubor

- **Original Wiki Page**: [Transcript:Tam McGrubor](https://runescape.wiki/w/Transcript%3ATam%20McGrubor)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Burthorpe


#### En mundos gratuitos

- **Tam McGrubor:** Hola. ¡Gracias por parar!
- **Tam McGrubor:** Déjame contarte lo que tengo aquí.
- **Player:** ¿Son esas capuchas?
- **Tam McGrubor:** No sólo capuchas. ¡Estos son matones malvados! Los llamo así porque son geniales y también se ven un poco malvados.
- **Tam McGrubor:** No solo lucirás como un mago serio en uno de estos, sino que también podrás usar sus poderes mágicos para ayudarte a lanzar hechizos.
- **Player:** ¿Qué poderes mágicos?
- **Tam McGrubor:** Puede crear runas y esencias rúnicas gratuitas para lanzar hechizos y, ocasionalmente, puede teletransportarte a las misteriosas ruinas donde se crean las runas.
- [Inicie sesión en un mundo de miembros para reclamar su malvado capó gratis.]

#### En los mundos de los miembros, sin capucha malvada en backpack

- **Tam McGrubor:** Hola. ¡Gracias por parar!
- {{anchor|fix-up}}**Tam McGrubor:** Entonces, ¿puedo arreglarte con uno de estos malvados matones?
- [Menu]: Selecciona una opción
  - [Choice]: Sí, por favor.
    - (Condition: Without space in backpack:)
      - [Necesitas un espacio en tu inventario para la campana.]
    - (Condition: With space in backpack:)
      - (receives=wicked hood)
      - [Tam te entrega una capucha malvada.]
    - (continue|second-set-options)
  - [Choice]: ¿Qué hace?
    - (below|what-does-it-do)
  - [Choice]: No gracias.
    - (end)

#### En los mundos de los miembros, con una capucha malvada en backpack

- **Tam McGrubor:** Hola. ¡Gracias por parar!
- {{anchor|second-set-options}}[Menú]: Seleccione una opción
  - [Choice]: ¿Puedo conseguir otra capucha?
    - **Tam McGrubor:** ¡Ya tienes uno! Si alguna vez pierdes el tuyo, ven y lo reemplazaré.
    - **Player:** Está bien.
  - [Choice]: ¿Cómo funciona esta capucha?
    - {{anchor|what-does-it-do}}**Tam McGrubor:** Es una capucha elegante para Runecrafting. Puede conjurar runas y esencias rúnicas, teletransportarte a altares de creación de runas y desbloquear el acceso a ellos.
    - **Tam McGrubor:** Lo más importante que debes recordar es que si quieres usar una habilidad asociada a una runa en particular, primero debes desbloquear ese tipo de runa para tu capucha.
    - [Menu]: Selecciona una opción
      - [Choice]: What runes can I get from the hood?|cond=Si no se seleccionó previamente:
        - **Tam McGrubor:** Una vez al día, el capó puede crear una pila de runas de cualquier tipo que el capó haya desbloqueado. ¡Solo alcanza y sácalos!
        - **Player:** ¿Una vez al día?
        - **Tam McGrubor:** Tiene que recargarse.
        - (previous)
      - [Choice]: How much rune essence can I get?|cond=Si no se seleccionó previamente:
        - **Tam McGrubor:** ¡Cien finas piezas de esencia rúnica cada día!
        - **Player:** No tengo espacio para tanta esencia a la vez.
        - **Tam McGrubor:** No te preocupes. Producirá todo lo que tenga espacio y luego podrá producir más una vez que tenga espacio.
        - (previous)
      - [Choice]: What's this about teleporting?|cond=Si no se seleccionó previamente:
        - **Tam McGrubor:** La capucha puede teletransportarte a cualquiera de los altares de creación de runas, siempre y cuando hayas desbloqueado la runa correspondiente.
        - **Tam McGrubor:** Sin embargo, solo obtienes dos teletransportes por día. Dos en total, no dos por altar.
        - (previous)
      - [Choice]: How do I unlock a rune?|cond=Si no se seleccionó previamente:
        - **Tam McGrubor:** Necesitas encontrar el tipo correcto de talismán e introducirlo en el capó. Una vez que hagas eso, ese tipo de runa se desbloqueará permanentemente para el capó.
        - **Tam McGrubor:** El capó comienza con las runas de aire y mente ya desbloqueadas. Otros talismanes vienen de todas partes.
        - **Tam McGrubor:** A veces los monstruos los tendrán, o es posible que puedas comprárselos a otros aventureros.
        - (previous)
      - [Choice]: Eso es todo lo que quiero preguntar.
        - (Condition: If players don't currently have a wicked hood:)
          - (above|fix-up)
        - (Condition: If players have a wicked hood:)
          - (previous)
  - [Choice]: Adiós.
    - (end)
