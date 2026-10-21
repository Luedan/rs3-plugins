# Spirit tree

- **Original Wiki Page**: [Transcript:Spirit tree](https://runescape.wiki/w/Transcript%3ASpirit%20tree)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before unlocking the spirit tree


#### Hablando con eso

- El árbol no tiene ganas de hablar.

#### Intentando teletransportarse fuera del Tree Gnome Stronghold

- Debes haber completado Tree Gnome Village para hacer esto.

### After unlocking the spirit tree

- **Spirit tree:** Si eres amigo del pueblo gnomo, eres amigo mío. ¿Quieres viajar o estás aquí para preguntar sobre el árbol del mal?
- [Menu]: ¿Sobre qué te gustaría preguntar?
  - [Choice]: Viajar.
    - **Spirit tree:** Puedes viajar a los árboles relacionados conmigo. ¿Adónde deseas viajar, susurrador?
    - (opens=Spirit tree)
      - *(Al seleccionar un spirit tree válido:)*
        - Te sientes uno con el spirit tree.
        - (Action: el player es teletransportado al spirit tree seleccionado.)
  - [Choice]: Árbol malvado.
    - (Condition: Si actualmente hay un Árbol del Mal activo que fue asesinado recientemente:)
      - **Spirit tree:** La contaminación del árbol malvado no está actualmente en la tierra. No habrá un árbol malvado por mucho tiempo.
      - (continue)
    - (Condition: De lo contrario:)
      - **Spirit tree:** La contaminación del árbol malvado no está actualmente en la tierra. Habrá un árbol malvado en aproximadamente [número] hora [número] minutos.
      - (continue)
    - **Spirit tree:** Puedo ayudarte a encontrar el lugar donde aparecerá, pero mi conocimiento fuera del anima mundi es limitado.
    - **Spirit tree:** Se puede encontrar cerca de [location] *(Ver Evil Tree#Ubicaciones con sugerencias para obtener una lista de ubicaciones)*.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Qué es este 'árbol del mal'?
        - **Spirit tree:** Es una abominación de la naturaleza que debe ser destruida lo más rápido posible. No sabemos dónde aparecerá, pero, cuando aparezca, ¡debes acudir inmediatamente y ayudar!
      - [Choice]: Adiós.
        - **Spirit tree:** Adiós.
  - [Choice]: Nada.
    - **Player:** Nada, gracias.

#### Si hay un retoño extraño

- **Spirit tree:** Si eres amigo del pueblo gnomo, eres amigo mío. ¿Quieres viajar o estás interesado en el extraño retoño?
- [Menu]: ¿Sobre qué te gustaría preguntar?
  - [Choice]: Viajar.
    - **Spirit tree:** Puedes viajar a los árboles relacionados conmigo. ¿Adónde deseas viajar, susurrador?
    - (opens=Spirit tree)
      - *(Al seleccionar un spirit tree válido:)*
        - Te sientes uno con el spirit tree.
        - (Action: el player es teletransportado al spirit tree seleccionado.)
  - [Choice]: Extraño retoño.
    - **Spirit tree:** Puedo ayudarte a encontrar el extraño retoño, pero mi conocimiento fuera del anima mundi es limitado.
    - **Spirit tree:** Se puede encontrar en [location] *(Ver Evil Tree#Locations con sugerencias para una lista de ubicaciones)*.
  - [Choice]: Nada.
    - **Player:** Nada, gracias.

#### Si hay un árbol del mal activo

- **Spirit tree:** Si eres amigo del pueblo gnomo, eres amigo mío. ¿Quieres viajar o estás aquí para ayudar a acabar con el árbol malvado?
- [Menu]: ¿Sobre qué te gustaría preguntar?
  - [Choice]: Viajar.
    - **Spirit tree:** Puedes viajar a los árboles relacionados conmigo. ¿Adónde deseas viajar, susurrador?
    - (opens=Spirit tree)
      - *(Al seleccionar un spirit tree válido:)*
        - Te sientes uno con el spirit tree.
        - (Action: el player es teletransportado al spirit tree seleccionado.)
  - [Choice]: Árbol malvado.
    - **Spirit tree:{{anchor|evil-tree-teleport}}** ¿Quieres que te teletransporte directamente allí?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí, por favor.
        - (Action: el player es teletransportado a la ubicación del Árbol del Mal.)
      - [Choice]: ¿Qué es este 'árbol del mal'?
        - **Spirit tree:** Es una abominación de la naturaleza, que ha aparecido en [location]*(Ver Evil Tree#Locations con sugerencias para una lista de ubicaciones)*. ¡Deberías ir allí inmediatamente para ayudar!
        - (continuea|evil-tree-teleport)
      - [Choice]: He cambiado de opinión, quiero quedarme aquí.
        - **Spirit tree:** Haz lo que quieras.
  - [Choice]: Nada.
    - **Player:** Nada, gracias.
Categoría: Transcripciones de paisajes
