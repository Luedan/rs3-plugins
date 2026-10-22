# Fetcher

- **Original Wiki Page**: [Transcript:Fetcher](https://runescape.wiki/w/Transcript%3AFetcher)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Outdated|Dailyscape overhaul that removed raid lockout mechanic}}

### Standard dialogue

- **Fetcher:** Es peligroso ir más allá de este punto humano. Déjame ayudarte a prepararte.
- [Menu]: Elige una opción:
  - [Choice]: ¿Puedes traer algún botín que me haya perdido?
    - ((If the player has no loot to collect, Lil' Tuzzy to check, or hasn't previously done Raids:))
      - **Fetcher:** Lo siento humano, no pude encontrar nada para ti.
    - ((If the player has loot:))
      - ((If the loot hasn't been checked yet:))
        - **Fetcher:** ¡He encontrado algo para ti!
        - (continue)
      - ((If the loot has been checked but not all of it has been dealt with yet:))
        - **Fetcher:** Parece que no terminaste de clasificar los últimos elementos que te encontré. Échale un vistazo.
        - (continue)
      - ((The following is shown in an interface titled "SELECT AN OPTION:))
        - ¿Qué debo buscar?
          - ((Only with Beastmaster Durzag loot available:))
            - Recoge el botín de Beastmaster Durzag.
              - (Se abre la interfaz del Cofre de recompensas).
                - ((After closing the interface without having dealt with all the loot:))
                  - {{Contrast|c=#003366|t=WARNING:}} Si cierras sesión, los artículos del cofre de recompensas se moverán a tu inventario o banco. Si ambos lugares están llenos, perderás los artículos.
          - ((Only with Yakamaru loot available:))
            - Recoge el botín de Yakamaru.
              - (Se abre la interfaz del Cofre de recompensas).
                - ((After closing the interface without having dealt with all the loot:))
                  - {{Contrast|c=#003366|t=WARNING:}} Si cierras sesión, los artículos del cofre de recompensas se moverán a tu inventario o banco. Si ambos lugares están llenos, perderás los artículos.
          - Volveré más tarde.
            - {{Transcript missing}}
    - ((Failing to loot Lil' Tuzzy while on lockout:))
      - **Fetcher:** Lo siento humano, no pude encontrar a Lil' Tuzzy por ningún lado.
    - ((Successfully looting Lil' Tuzzy while on lockout:))
      - **Fetcher:** Oye, encontré algo para ti.
    - ((Unknown trigger:))
      - **Fetcher:** ¡Veré si puedo encontrar algo de botín para ti!
      - **Fetcher:** No. No pude encontrar nada.
  - [Choice]: Muéstrame mi bloqueo de incursión actual.
    - (below|View lock)
  - [Choice]: ¿Pueden restablecer automáticamente mi bloqueo de incursión?
    - **Fetcher:** Eso debería ser posible humano.
    - (Condition: If Fetcher wasn't previously asked to automatically reset raids lockout:)
      - [Menu]: ¿Restablecer automáticamente el bloqueo de tus incursiones?
        - [Choice]: si
          - (end)
        - [Choice]: No
          - (end)
    - (Condition: If Fetcher was already automatically resetting raids lockout:)
      - **Fetcher:** Parece que ya lo estoy haciendo por ti humano. ¿Quieres que me detenga?
      - [Menu]: Detener automáticamente {{Sic|reseting your raids lockout?}}
        - [Choice]: si
          - (end)
        - [Choice]: No
          - (end)
  - [Choice]: cond=If the player has the maximum goebie reputation and is carrying burial charms:|¿Pagarías a cualquier Teci por estos amuletos funerarios?
    - **Fetcher:{{anchor|exchange}}** Si no necesitas tus amuletos, estaría dispuesto a cambiarlos por una pequeña cantidad de Teci. ¿Estás interesado?
    - [Menu]: ¿Intercambiar [#] charm[s] por [#] Teci?
      - [Choice]: Sí.
        - (removes=all burial charms)
        - (receives=the corresponding amount of Teci)
      - [Choice]: No.
        - **Fetcher:** Muy bien, humano.
  - [Choice]: Adiós.
    - (end)

### Using a burial charm on Fetcher


#### Sin máxima reputación

- **Fetcher:** No puedo hacer nada con ese humano. Quizás si fueras un poco más conocido podría hacer un intercambio.

#### Con máxima reputación

- (continuea|exchange)

### Collect loot

- (above|loot)

### View lock

- (Se abre una interfaz titulada Mazcab Raid Lock, con "BEASTMASTER DURZAG" y "YAKAMARU" mostrados en fondo verde o rojo, dependiendo de si el botín está disponible o no. El botón "RESET" está habilitado o deshabilitado).
- ((Only if the reset is enabled:))
  - REINICIAR
    - Solo puedes restablecer la incursión de Mazcab una vez cada 48 horas. ¡Asegúrate de que deseas restablecer tu progreso antes de continuar!
      - CANCELAR
        - ((Returns to the Mazcab Raid Lock interface without changes.))
      - CONFIRMAR
        - El progreso de tu incursión se ha reiniciado.
        - ((Returns to the Mazcab Raid Lock interface with the backgrounds changed to green and reset button disabled.))
- ((When hovering over the disabled reset button:))
  - El progreso del jefe solo se puede restablecer una vez cada 48 horas.
