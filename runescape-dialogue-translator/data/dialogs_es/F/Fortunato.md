# Fortunato

- **Original Wiki Page**: [Transcript:Fortunato](https://runescape.wiki/w/Transcript%3AFortunato)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Draynor Village

- **Fortunato:** ¿Puedo ayudarte en algo?
- [Menu]: Elige una opción:
  - [Choice]: Sí, ¿qué estás vendiendo?
    - **Player:** Sí, ¿qué estás vendiendo?{{anchor|shop}}
    - (opens=Fortunato's Fine Wine)
  - [Choice]: cond=After Rag and Bone Man:|Hablando de Rag and Bone Man.
    - **Fortunato:** Oh, has vuelto.
    - **Fortunato:** Por favor, no tengo más vinagre. Dame un poco de tiempo, te lo ruego.
    - **Player:** Hoy no buscaba vinagre.
    - **Fortunato:** Oh, maravilloso.
    - **Fortunato:** Pronto tendré algunos si 'él' los necesita.
    - **Fortunato:** Mientras tanto, ¿puedo interesarte en algo más?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí.
        - (above|shop)
      - [Choice]: No.
        - **Player:** No.
        - **Fortunato:** Bueno, dejaré algo especial a un lado para ti.
        - **Player:** Gracias.
  - [Choice]: cond=On free-to-play worlds, or before Rag and Bone Man:|Comerciante de vinos, ¿eh?
    - **Fortunato:** Sí, efectivamente. Los mejores vinos de Misthalin.
    - **Fortunato:** ¿Te importaría echar un vistazo a mis productos?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí.
        - (above|shop)
      - [Choice]: No por el momento.
        - (below|ragamuffin)
  - [Choice]: cond=Before Vampyre Slayer:|¿Puedes hablarme de Draynor Village?
    - **Fortunato:** El pueblo es bastante antiguo, pero el mercado es una incorporación bastante reciente. Hasta hace poco estábamos haciendo bastante buen negocio.
    - **Player:** ¿Qué pasó?
    - **Fortunato:** Los aldeanos comenzaron a sufrir ataques misteriosos. Algunos dicen que es un vampyre, pero a mí no me convence.
    - (initial)
  - [Choice]: cond=After Vampyre Slayer:|Habla de Vampyre Slayer.
    - **Fortunato:** Bien hecho matando a ese vampyre. Sin duda, el negocio ha mejorado desde que cesaron los ataques.
    - **Player:** Encantado de poder ayudar.
    - (initial)
  - [Choice]: No por el momento.
    - **Player:** No por el momento.{{anchor|ragamuffin}}
    - **Fortunato:** Entonces sigue adelante, asqueroso canalla, ¡tengo clientes a quienes atender!

#### Usando botellas de vino vacías en Fortunato

- **Fortunato:** ¡Ah! Compro botellas de vino si quieres entregármelas todas.
- (removes=all empty wine bottles) (receives=2 coins per bottle)

#### Ser atrapado mientras intentaba robar en su puesto

- **Fortunato:** {{RSChat|Hey! Get your hands off there!}}

#### Intercambiar o hablar con él después de robar en su puesto

- **Fortunato:**{{RSChat|shadow=yes|colour=yellow|You're the thief who stole from me!}}
- **Fortunato:**{{RSChat|shadow=yes|colour=yellow|Guards, guards!}}

#### Diálogo histórico

- **Fortunato:** ¿Puedo ayudarte en algo?
- [Menu]: Elige una opción:
  - [Choice]: Sí, ¿qué estás vendiendo?
    - (above|shop)
  - [Choice]: cond=After Rag and Bone Man:|Hablando de Rag and Bone Man.
    - (arriba)
  - [Choice]: cond=On free-to-play worlds, or before Rag and Bone Man:|Comerciante de vinos, ¿eh?
    - (arriba)
  - [Choice]: ¿Puedes hablarme de Draynor Village?
    - **Fortunato:** El pueblo es bastante antiguo, pero el mercado es una incorporación bastante reciente. Hasta hace poco estábamos haciendo bastante buen negocio.
    - **Player:** ¿Qué pasó?
    - (Condition: Durante la Batalla de Lumbridge:)
      - **Fortunato:** ¡Saradomin y Zamorak han decidido tener una gran pelea cerca! ¡Es terrible para los negocios!
      - (continue|zxc)
    - (Condition: Después de la Batalla de Lumbridge:)
      - **Fortunato:** Bueno, no hace mucho hubo una batalla justo afuera de Draynor, ¡entre Saradomin y Zamorak! Todavía puedes ver el campo de batalla.
      - (continue|zxc)
    - (Condition: Antes de Vampyre Slayer:)
      - **Fortunato:** Además de eso, comenzaron a ocurrir ataques misteriosos a los aldeanos. Algunos dicen que es un vampyre, pero a mí no me convence.
      - (continue|cxz)
    - (Condition: Después de Vampyre Slayer:)
      - **Fortunato:** Si sumas eso al vampyre que eliminaste, ¡no obtendrás cifras de ventas felices!
      - (continue|cxz)
    - **Fortunato:** ¿Quizás pueda interesarte un poco de vino?
    - [Menu]: Selecciona una opción
      - [Choice]: Sí.
        - (above|shop)
      - [Choice]: No por el momento.
        - (above|ragamuffin)
