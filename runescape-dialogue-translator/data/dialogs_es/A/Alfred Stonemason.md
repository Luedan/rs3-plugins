# Alfred Stonemason

- **Original Wiki Page**: [Transcript:Alfred Stonemason](https://runescape.wiki/w/Transcript%3AAlfred%20Stonemason)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Transcript npc|Alfred Stonemason}}

### Before There's No Place Like Home...

- (ver|No hay lugar como el hogar...#Hablando con Alfred Stonemason)

### After There's No Place Like Home...

- **Alfred Stonemason:** ¡Espero que te lleves bien con tu viaje a la vivienda! <br>Recuerda que si alguna vez necesitas un repaso sobre cómo funcionan las cosas, puedes hojear la guía Construction.
- **Alfred Stonemason:** ¿Quieres uno?
- [Menu]: ¿Llevar una guía de construcción?
  - [Choice]: ¡Me llevaré uno!
    - (Condition: Sin espacio en backpack:)
      - **Alfred Stonemason:** Libera algo de espacio en tu backpack y te daré uno.
    - (Condition: Con espacio en backpack:)
      - (receives=construction guide)
      - **Alfred Stonemason:** ¡Aquí tienes!
  - [Choice]: No gracias.
    - (end)

### Historical dialogue prior to 13 July 2026


#### Si el player aún no tiene casa

- **Alfred Stonemason:** ¿Necesitas ayuda de Construction?
- [Menu]: Elige una opción:
  - [Choice]: Dime cómo puedo conseguir mi propia casa.
    - **Alfred Stonemason:** Mira, estaban estos magos, cierto, y necesitaban más espacio para vivir. Entonces descubrieron una manera de hacerlo para que las cosas no ocupen espacio.
    - **Alfred Stonemason:** Ni yo mismo lo entiendo, pero ahora todos pueden tener sus propios dos acres y todo es fácilmente accesible desde aquí.
    - **Alfred Stonemason:** Sí, un lugar donde colgar el sombrero. Tus raíces. Tu castillo. Una casa propia.
    - **Alfred Stonemason:** Una hermosa casa mágica aquí mismo en Rimmington te costará solo 1000 coins. Siempre puedes mover el portal a otro lugar más adelante si lo deseas. ''(Nota: Alfred dice 'Taverley' en lugar de 'Rimmington' en su voz en off).
    - ((Lo siguiente se muestra en una interfaz titulada "Comprar una casa":))
      - [Choice]: Cancelar
        - **Alfred Stonemason:** Bueno, ¡disfruta de tu caja de cartón propiedad del jugador, o de donde sea que vayas a dormir esta noche!
        - (previous)
      - [Choice]: bien
        - (Condition: Si el player no tiene 1000 coins:)
          - No puedes permitirte eso.
          - Necesitas 1000 coins para comprar una casa.
          - (ventana emergente)
            - (Ventana emergente: necesita 1000 coins para comprar una casa.|advertencia=yes)
        - (Condition: Si el player tiene 1000 coins:)
          - (removes=1,000 coins)
          - {{RSFontAchievement|Unreal Estate, Man|Buy a house of your own.}}
          - **Alfred Stonemason:** ¡Genial! ¡Continúa por ese gran portal morado que hay allí y podrás empezar a añadir habitaciones a la casa! De hecho, tengo una guía al respecto aquí en alguna parte.
          - (Condition: Si el player no tiene espacio en backpack:)
            - Tu backpack está lleno. Puedes reclamar la guía de construcción desde un estate agent.
            - (ventana emergente)
              - (Ventana emergente: Tu backpack está lleno. Puedes reclamar la guía de construcción de un estate agent.|warning=yes)
          - (Condition: Si el player tiene espacio en backpack:)
            - (receives=construction guide)
            - [Este libro te ayudará a empezar a construir tu casa.]
  - [Choice]: Necesito materiales de construcción.
    - (opens=Alfred Stonemason's Construction Shop)

#### Si el player ya posee una casa

- **Alfred Stonemason:** ¿Necesitas ayuda de Construction?
- [Menu]: Elige una opción:
  - [Choice]: Necesito materiales de construcción.
    - (opens=Alfred Stonemason's Construction Shop)
  - [Choice]: Cuéntame sobre la casa que tengo.
    - **Alfred Stonemason:** Mira, estaban estos magos, cierto, y necesitaban más espacio para vivir. Entonces descubrieron una manera de hacerlo para que las cosas no ocupen espacio.
    - **Alfred Stonemason:** Ni yo mismo lo entiendo, pero ahora todos pueden tener sus propios dos acres y todo es fácilmente accesible desde aquí.
    - **Alfred Stonemason:** Sí, un lugar donde colgar el sombrero. Tus raíces. Tu castillo. Una casa propia.
    - (previous)
  - [Choice]: ¿Puedes redecorar mi casa, por favor?
    - **Alfred Stonemason:** ¡Ciertamente puedo! Puedo hacerlo por ti en un santiamén. ¿Qué estilo buscabas?
    - ((Lo siguiente se muestra en una interfaz titulada "SELECCIONE UNA OPCIÓN":))
    - ¿Qué parte de tu casa quieres redecorar?
      - [Choice]: casa
        - ((Lo siguiente se muestra en una interfaz titulada "SELECCIONE UNA OPCIÓN":))
        - ¿Qué estilo de casa quieres?
          - [Choice]: Madera básica (2,500 coins) ''(Estilo original)
            - (abajo2|zxz)
          - [Choice]: Piedra básica (5000 coins) ''(Requiere nivel 10 Construction)
            - (abajo2|zxz)
          - [Choice]: Piedra encalada (7,500 coins) ''(Requiere nivel 20 Construction)
            - (abajo2|zxz)
          - [Choice]: Madera estilo Fremennik (10,000 coins) ''(Requiere nivel 30 Construction)
            - (abajo2|zxz)
          - [Choice]: Madera tropical (15,000 coins) ''(Requiere nivel 40 Construction)
            - (abajo2|zxz)
          - [Choice]: Piedra elegante (25,000 coins) ''(Requiere nivel 50 Construction)
            - (abajo2|zxz)
          - [Choice]: Piedra oscura (gratis) ''(Completa la misión 'Historia de amor')
            - (abajo2|zxz)
          - [Choice]: Atrás
            - (previous)
      - [Choice]: Terrenos
        - ((Lo siguiente se muestra en una interfaz titulada "SELECCIONE UNA OPCIÓN":))
        - Que terreno quieres??
          - [Choice]: Hierba áspera (5,000 coins) ''(Estilo original)
            - (abajo2|zxz)
          - [Choice]: Desierto (7,500 coins) ''(Requiere nivel 20 Construction)
            - (abajo2|zxz)
          - [Choice]: Tierra estéril (10,000 coins) ''(Requiere nivel 30 Construction)
            - (abajo2|zxz)
          - [Choice]: Hierba cortada (15,000 coins) ''(Requiere nivel 40 Construction)
            - (abajo2|zxz)
          - [Choice]: Tundra (100,000 coins) ''(Requiere nivel 70 Construction)
            - (abajo2|zxz)
          - [Choice]: Atrás
            - (previous)
      - [Choice]: mazmorra
        - ((Lo siguiente se muestra en una interfaz titulada "SELECCIONE UNA OPCIÓN":))
        - ¿Qué estilo de mazmorra quieres?
          - [Choice]: Piedra en bruto (2.500 coins) ''(Estilo original)
            - (abajo2|zxz)
          - [Choice]: Piedra lisa (5,000 coins)''(Requiere nivel 10 Construction)
            - (abajo2|zxz)
          - [Choice]: Mazmorra del desierto (7,500 coins) ''(Requiere nivel 20 Construction)
            - (abajo2|zxz)
          - [Choice]: Mina de montaña (10,000 coins) ''(Requiere nivel 30 Construction)
            - (abajo2|zxz)
          - [Choice]: Cueva tropical (15,000 coins) ''(Requiere nivel 40 Construction)
            - (abajo2|zxz)
          - [Choice]: Bloques de piedra (25,000 coins) ''(Requiere nivel 50 Construction)
            - (abajo2|zxz)
          - [Choice]: Atrás
            - (previous)
      - [Choice]: Iluminación
        - ((Lo siguiente se muestra en una interfaz titulada "SELECCIONE UNA OPCIÓN":))
        - ¿Qué iluminación quieres?
          - [Choice]: Diurno (5000 coins) ''(estilo original)
            - (abajo2|zxz)
          - [Choice]: Anochecer (1,500,000 coins)''(Requiere nivel 75 Construction)
            - (abajo2|zxz)
          - [Choice]: Noche (250.000 coins) ''(Requiere nivel 85 Construction)
            - (abajo2|zxz)
          - [Choice]: Atrás
            - (previous)
  - [Choice]: ¿Puedes mudar mi casa por favor?
    - ((Lo siguiente se muestra en una interfaz titulada "SELECCIONE UNA OPCIÓN":))
    - ¿A dónde te gustaría trasladar tu casa?
      - [Choice]: Rimmington (5,000) ''(Área original)
        - (abajo2|xzx)
      - [Choice]: Taverley (5,000) ''(Requiere nivel 1 Construction)
        - (abajo2|xzx)
      - [Choice]: Pollnivneach (7,500) ''(Requiere nivel 20 Construction)
        - (abajo2|xzx)
      - [Choice]: Rellekka (10,000) ''(Requiere nivel 30 Construction)
        - (abajo2|xzx)
      - [Choice]: Brimhaven (15,000) ''(Requiere nivel 40 Construction)
        - (abajo2|xzx)
      - [Choice]: Yanille (25,000) ''(Requiere nivel 50 Construction)
        - (abajo2|xzx)
      - [Choice]: Menaphos (50,000) ''(Requiere nivel 50 Construction)
        - (abajo2|xzx)
      - [Choice]: Otot (Mazcab) (50,000) ''(Requiere nivel 60 Construction)
        - (abajo2|xzx)
      - [Choice]: Prifddinas (50,000) ''(Requiere nivel 75 Construction)
        - (abajo2|xzx)

#### Al elegir una opción de redecoración {{anchor|zxz}}


##### Sin suficiente dinero

- Necesita [número] coins.
- (ventana emergente)
  - (Ventana emergente: necesita [número] coins.|advertencia=yes)

##### Sin el requisito de nivel Construction

- Necesitas el nivel [número] Construction para usar ese estilo.
- (ventana emergente)
  - (Ventana emergente: requiere el nivel [número] Construction para usar ese estilo.|advertencia=yes)

##### Seleccionando piedra oscura sin Love Story completada

- Primero debes completar la misión 'Historia de amor'.
- (ventana emergente)
  - (Ventana emergente: primero debes completar la misión 'Historia de amor'.|advertencia=yes)

##### Seleccionando piedra oscura con Love Story completada

- **Alfred Stonemason:** Ah, ¿conoces a Zenevivia? Señora con clase, eso.<br>Muy bien. La redecoración está hecha.
- ((Regresa a la interfaz "SELECCIONAR UNA OPCIÓN".))

##### Eligiendo la misma opción que la actual

- ¡Tu [house/grounds/dungeon/lighting] ya tiene ese estilo!
- (ventana emergente)
  - (Ventana emergente: ¡Tu [house/grounds/dungeon/lighting] ya tiene ese estilo!|advertencia=yes)

##### De lo contrario

- (removes=coins)
- **Alfred Stonemason:** Buena elección.<br>Muy bien. La redecoración está hecha.
- ((Regresa a la interfaz "SELECCIONAR UNA OPCIÓN".))

#### Al elegir una opción de ubicación{{anchor|xzx}}


##### Sin suficiente dinero

- Necesita [número] coins para trasladar su casa allí.
- (ventana emergente)
  - (Ventana emergente: Necesita [número] coins para mudar su casa allí.|advertencia=yes)

##### Sin el requisito de nivel Construction

- Necesitas el nivel [número] Construction para trasladar tu casa allí.
- (ventana emergente)
  - (Ventana emergente: Necesitas el nivel [número] Construction para trasladar tu casa allí.|advertencia=yes)

##### Eligiendo la misma opción que la actual

- ¡Tu casa ya está ahí!
- (ventana emergente)
  - (Ventana emergente: ¡Tu casa ya está ahí!|advertencia=yes)

##### De lo contrario

- (removes=coins)
- Su casa ha sido trasladada a [location].
