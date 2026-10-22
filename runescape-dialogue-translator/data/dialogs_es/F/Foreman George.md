# Foreman George

- **Original Wiki Page**: [Transcript:Foreman George](https://runescape.wiki/w/Transcript%3AForeman%20George)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Lumbridge Rebuildathon

- (ver | Lumbridge Rebuildathon)

### Summer events


#### Recibiendo a los invitados


##### Archmage Sedridor

- **Foreman George:** {{RSChat|Wizard Sedridor! Come to see the Wizards' Sandtower?}}

##### Duke Horacio

- **Foreman George:** {{RSChat|Kind of you to visit, Duke Horacio. Want to see the Lumbridge Sandcastle?}}

##### Ozan

- **Foreman George:** {{RSChat|Welcome Ozan! Would you like to see the Sand Pyramid?}}

##### Sally the Grand Exchange clerk

- **Foreman George:** {{RSChat|Sally, let me show you the Sand Exchange!}}

#### Cuando hablamos

- **Foreman George:** ¡Bienvenido a mi nuevo maratón de reconstrucción!
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué necesito hacer aquí?
    - **Foreman George:** Realmente simple. Elige un castillo de arena que quieras ayudar a construir y empieza a trabajar en él.
    - **Foreman George:** Tengo en mente a algunos dignatarios visitantes, así que vale la pena intentar impresionarlos mientras están aquí para obtener una mejor recompensa.
    - **Foreman George:** Es un trabajo muy caliente, así que si tienes demasiado calor quizás quieras buscar un helado para refrescarte.
    - (previous)
  - [Choice]: ¿Qué obtengo por ayudar?
    - **Foreman George:** Directamente al grano, ¿eh?
    - **Foreman George:** Ayúdame a construir estos castillos de arena y obtendrás algo de XP Construction. Si toma nota del dignatario visitante, obtendrá una recompensa mayor por impresionarlo con su trabajo.
    - (previous)
  - [Choice]: ¿Quién eres?
    - **Foreman George:** Mi nombre es George y soy el capataz de este proyecto.
    - **Foreman George:** Un pequeño cambio con respecto a mi trabajo anterior: ayudar a reconstruir Lumbridge después de la batalla, pero esto parece ser igual de desafiante.
    - **Player:** ¿En serio? Parecen castillos de arena. ¿Qué tan difícil puede ser construirlos?
    - **Foreman George:** ¿Estás cuestionando mis habilidades de construcción?
    - **Foreman George:** Digamos que son más avanzados que un castillo de arena normal. Yo tengo los planos, tú solo concéntrate en el edificio.
    - (previous)
  - [Choice]: Hablaremos más tarde.
    - (end)

#### Con el pergamino de pistas Sandy (histórico)

- **Foreman George:** Alguien te dejó esto en una de las esculturas de arena.
- (Condition: Receiving a scroll box:)
  - (removes=Sandy Clue Scroll) (receives=Sandy Scroll box)
  - [scrollbox].}}
- (Condition: Receiving caskets:)
  - (Condition: Without free space in backpack:)
    - Necesitas 1 espacio libre en tu backpack para recibir tus cofres de pistas.
  - (Condition: With free space in backpack:)
    - (removes=Sandy Clue Scroll) (receives=Sandy Casket and its red version)
    - [¡Te entregan un ataúd!]
