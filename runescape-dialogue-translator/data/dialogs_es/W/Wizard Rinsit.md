# Wizard Rinsit

- **Original Wiki Page**: [Transcript:Wizard Rinsit](https://runescape.wiki/w/Transcript%3AWizard%20Rinsit)
- **Letter**: `W`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### When talked to

- **Wizard Rinsit:** Hola, ¿qué puedo hacer por ti?
- [Menu]: Elija una opción:|anchor=Opciones-de-enjuague
  - [Choice]: ¿Qué haces en el Wizards' Tower?
    - **Wizard Rinsit:** Soy aprendiz en Wizards' Tower. Estoy aquí para compartir conocimientos sobre Runespan y ayudar a otros en sus viajes.
    - (previous|Rinsit-options)
  - [Choice]: ¿Qué vendes?
    - **Wizard Rinsit:** Puedes comprarme varias cosas que te ayudarán dentro de Runespan.
    - **Wizard Rinsit:** Tengo teletransportes de runesfera y mago amarillo que te permitirán moverte más fácilmente.
    - **Wizard Rinsit:** También puedo proporcionarte el traje de maestro creador de runas si estás preparado para ello.
    - **Wizard Rinsit:** Por último, tengo una variedad de tabletas de teletransportación de altares que pueden usarse para llevarte directamente al centro de las misteriosas ruinas que contienen altares de runas.
    - (previous|Rinsit-options)
  - [Choice]: ¿Puedo ver tu tienda?
    - (opens=Wizard Rinsit's Runecrafting Shop)
  - [Choice]: ¿Sabes si podría hacer una bolsa de esencias más grande?
    - **Player:** ¿Sabes si podría hacer una bolsa de esencias más grande?
    - **Wizard Rinsit:** ¡En teoría, sí!
    - (Condition: Without Runecrafting level 105:)
      - **Wizard Rinsit:** Sin embargo, no creo que sea algo de lo que alguien con tus habilidades sería capaz de hacer.
      - La creación de una bolsa expansiva requiere Runecrafting nivel 105.
    - [Menu]: Elija una opción:|anchor=Bolsa de enjuague
      - [Choice]: ¿Dónde podría hacerlo?
        - **Player:** ¿Dónde podría hacerlo?
        - **Wizard Rinsit:** ¡En un altar, por supuesto! Sólo algo así debería tener la energía vinculante para crear tal objeto.
        - (previous|Rinsit-pouch)
      - [Choice]: ¿Qué necesitaría para hacerlo?
        - **Player:** ¿Qué necesitaría para hacerlo?
        - **Wizard Rinsit:** Materiales potentes, eso es seguro.
        - **Wizard Rinsit:** Posiblemente podrías reutilizar una capucha Wicked como base de la bolsa. Resulta que tengo una capucha Hungry que podría venderte para ese propósito.
        - **Wizard Rinsit:** Por supuesto, probablemente también necesitarás el poder de otras bolsas de esencias.
        - **Wizard Rinsit:** Algo que aproveche la energía dimensional como esa definitivamente necesitaría una funda protectora de algún tipo, tal vez hecha de algún tipo de cuero resistente...
        - **Wizard Rinsit:** ¡Oh! También necesitarás una forma de cerrarlo. He oído hablar de un hilo mágico que se detectó al crear runas después de entrar directamente a las ruinas del altar, que podría funcionar.
        - (previous|Rinsit-pouch)
      - [Choice]: I lost some of the parts.|cond=Si alguna pieza falta o está destruida
        - (Condition: Without enough free backpack space for all the missing items:)
          - **Wizard Rinsit:** Encontré algunas cosas que quizás hayas extraviado, pero parece que no tienes espacio en tu backpack para llevarlas.
        - (Condition: With enough free backpack space for all the missing items:)
          - (receives=missing items)
          - **Wizard Rinsit:** He puesto algunas cosas que quizás hayas extraviado en tu backpack para ti.
          - (previous|Rinsit-pouch)
      - [Choice]: No importa.
        - (previous2|Rinsit-options)
  - [Choice]: Adiós.
    - (end)

### When directing portal


#### Si no se ha comprado la redirección del portal

- **Wizard Rinsit:** Puedo dirigir ese portal de allí para llevarte directamente al último piso de Runespan, sin embargo, no es una tarea fácil, te va a costar.
- Debes comprar la recompensa 'Redireccionamiento del portal' en la tienda de Wizard Rinsit antes de que pueda hacer esto.

#### Si se ha comprado la redirección del portal

- **Wizard Rinsit:** Puedo dirigir ese portal hacia allí para llevarte directamente al último piso de Runespan si eres un creador de runas experimentado.
- [Menu]: ¿A dónde le gustaría que se dirigiera el portal?
  - [Choice]: Runespan de nivel medio.
    - (Condition: If the portal is already directed there:)
      - **Wizard Rinsit:** Parece que el portal ya está dirigido a ese destino.
    - (Condition: If the portal is directed to high-level Runespan:)
      - **Wizard Rinsit:** ¡Ahí, todo redirigido para ti!
  - [Choice]: Runespan de alto nivel
    - (Condition: If the portal is already directed there:)
      - **Wizard Rinsit:** Parece que el portal ya está dirigido a ese destino.
    - (Condition: If the portal is directed to mid-level Runespan:)
      - **Wizard Rinsit:** ¡Ahí, todo redirigido para ti!

### When using the [[rusty chest]] on him


#### Antes del 13 de agosto de 2018


##### Primera vez

- **Player:** Me preguntaba si podrías echarle un vistazo a este cofre.
- **Wizard Rinsit:** ¿Qué tenemos aquí entonces? Hmm... Interesante, este cofre parece estar sellado por un candado mágico...
- **Player:** Esa es la razón por la que les traje esto. Seguí un mapa del tesoro y me llevó a este cofre, sin embargo, no tuve suerte para abrirlo.
- **Wizard Rinsit:** No te preocupes Player, ¡puedo quitar ese candado por ti! Desafortunadamente esto no va a ser tan fácil como pensaba. Necesitaré algo de tiempo para investigar esto; vuelva más tarde.

##### Si el cofre ya ha sido usado en él

- **Wizard Rinsit:** Todavía estoy buscando más información. Vuelve más tarde.

#### Después del 13 de agosto de 2018


##### Con el cofre cerrado

*Si has hablado con él antes*
- **Wizard Rinsit:** He pasado mucho tiempo investigando este tipo de cerradura. Entrégala y te la quitaré.
- (Action: Wizard Rinsit quita la cerradura del Rusty Chest)
- **Wizard Rinsit:** ¡Ahí estás Player! Siempre es agradable ver que el trabajo duro da sus frutos.
*Si hablas con él por primera vez*
- **Player:** Me preguntaba si podrías echarle un vistazo a este cofre.
- **Wizard Rinsit:** ¿Qué tenemos aquí entonces? Ah, sí, pasé mucho tiempo investigando este tipo de cerradura.
- **Player:** Esa es la razón por la que les traje esto. Seguí un mapa del tesoro y me llevó a este cofre, sin embargo, no tuve suerte para abrirlo.
- **Wizard Rinsit:** No te preocupes Player, ¡puedo quitar ese candado por ti!
- (Action: Wizard Rinsit quita la cerradura del Rusty Chest)
- **Wizard Rinsit:** ¡Ahí estás Player! Siempre es agradable ver que el trabajo duro da sus frutos.

##### Con el cofre abierto

- **Wizard Rinsit:** No estoy seguro de qué quieres que haga con eso, ¡ya te quité el candado!
- **Wizard Rinsit:** Ven a verme nuevamente si tienes algún otro problema.

### When using the [[ancient scroll]] on him

- **Wizard Rinsit:** Lamentablemente, esta no es mi área de especialización, por lo que no puedo ayudarte.
