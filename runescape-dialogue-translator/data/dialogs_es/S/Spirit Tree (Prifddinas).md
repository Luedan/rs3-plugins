# Spirit Tree (Prifddinas)

- **Original Wiki Page**: [Transcript:Spirit Tree (Prifddinas)](https://runescape.wiki/w/Transcript%3ASpirit%20Tree%20%28Prifddinas%29)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Prifddinas, after Plague's End


#### Hablando con el Spirit Tree

- **Spirit Tree:** Hola, susurrador de árboles. He estado solo mucho tiempo, pero es bueno ser parte de Anima Mundi una vez más.
  - (Condition: Si el player aún no ha vuelto a conectar el Spirit Tree a todos sus hermanos:)
    - **Spirit Tree:** Puedo escuchar a mis hermanos claramente... pero no a todos. Me pregunto, ¿podrías ayudarme a reconectarme con todos ellos?
      - (Condition: Si el player aún no ha ayudado a Incomitatus:)
        - **Spirit Tree:** El árbol al sur en Poison Wastes suena preocupado.
        - (continue)
      - (Condition: Si el player aún no ha plantado un Spirit tree en Port Sarim:)
        - **Spirit Tree:** No puedo sentir a mis hermanos en Port Sarim.
        - (continue)
      - (Condition: Si el player aún no ha plantado un Spirit tree en Etceteria:)
        - **Spirit Tree:** No puedo sentir a mis hermanos en Etceteria.
        - (continue)
      - (Condition: Si el player aún no ha plantado un Spirit tree en Brimhaven:)
        - **Spirit Tree:** No puedo sentir a mis hermanos en Brimhaven.
        - (continue)
      - (Condition: Si el player aún no ha plantado un Spirit tree en Manor Farm:)
        - **Spirit Tree:** No puedo sentir a mis hermanos en Manor Farm.
        - (continue)
      - (Condition: Si el player tiene un Spirit tree en crecimiento:)
        - **Spirit Tree:** Siento que mis hermanos en [location] están regresando.
      - (Condition: Si el player tiene un Spirit tree que ha crecido completamente pero aún no se ha comprobado su salud:)
        - **Spirit Tree:** Mis hermanos en [location] son cercanos. Quizás deberías ir a verlos.
        - (continue)
    - **Spirit Tree:** Si pudieras encontrar una manera de devolverme a estos hermanos, te estaría muy agradecido. Le dejé una pequeña recompensa a nuestro amigo gnomo si logras esto.
    - (continue|standard)
  - (Condition: Si es la primera vez que habla después de que todos los árboles Spirit hayan vuelto a crecer:)
    - **Spirit Tree:** No... espera... ¡Puedo escucharlos a todos otra vez! ¡Gracias, susurrador de árboles, gracias! Le pedí a nuestro amigo gnomo que te recompensara por tus esfuerzos.
    - (continue|standard)

#### Después de que todos los árboles espirituales hayan sido conectados


##### Si no existe el Árbol del Mal

- **Spirit tree:{{anchor|standard}}** Si eres amigo del pueblo gnomo, eres amigo mío. ¿Quieres viajar o estás aquí para preguntar sobre el árbol del mal?
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

##### Si hay un retoño extraño

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

##### Si hay un árbol del mal activo

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
