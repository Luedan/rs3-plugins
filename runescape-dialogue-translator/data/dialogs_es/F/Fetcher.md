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
    - ((Si el player no tiene botín que recolectar, Lil' Tuzzy que verificar o no ha realizado incursiones anteriormente:))
      - **Fetcher:** Lo siento humano, no pude encontrar nada para ti.
    - ((Si el player tiene botín:))
      - ((Si el botín aún no ha sido revisado:))
        - **Fetcher:** ¡He encontrado algo para ti!
        - (continue)
      - ((Si se ha revisado el botín pero aún no se ha solucionado todo:))
        - **Fetcher:** Parece que no terminaste de clasificar los últimos elementos que te encontré. Échale un vistazo.
        - (continue)
      - ((Lo siguiente se muestra en una interfaz titulada "SELECCIONE UNA OPCIÓN:))
        - ¿Qué debo buscar?
          - ((Solo con botín Beastmaster Durzag disponible:))
            - Recoge el botín de Beastmaster Durzag.
              - (Se abre la interfaz del Cofre de recompensas).
                - ((Después de cerrar la interfaz sin habernos ocupado de todo el botín:))
                  - {{Contrast|c=#003366|t=WARNING:}} Si cierras sesión, los artículos del cofre de recompensas se moverán a tu inventario o banco. Si ambos lugares están llenos, perderás los artículos.
          - ((Solo con botín Yakamaru disponible:))
            - Recoge el botín de Yakamaru.
              - (Se abre la interfaz del Cofre de recompensas).
                - ((Después de cerrar la interfaz sin habernos ocupado de todo el botín:))
                  - {{Contrast|c=#003366|t=WARNING:}} Si cierras sesión, los artículos del cofre de recompensas se moverán a tu inventario o banco. Si ambos lugares están llenos, perderás los artículos.
          - Volveré más tarde.
            - {{Transcript missing}}
    - ((No poder saquear a Lil' Tuzzy durante el cierre patronal:))
      - **Fetcher:** Lo siento humano, no pude encontrar a Lil' Tuzzy por ningún lado.
    - ((Saquear con éxito a Lil' Tuzzy durante el cierre patronal:))
      - **Fetcher:** Oye, encontré algo para ti.
    - ((Activador desconocido:))
      - **Fetcher:** ¡Veré si puedo encontrar algo de botín para ti!
      - **Fetcher:** No. No pude encontrar nada.
  - [Choice]: Muéstrame mi bloqueo de incursión actual.
    - (below|View lock)
  - [Choice]: ¿Pueden restablecer automáticamente mi bloqueo de incursión?
    - **Fetcher:** Eso debería ser posible humano.
    - (Condition: Si a Fetcher no se le pidió previamente que restableciera automáticamente el bloqueo de incursiones:)
      - [Menu]: ¿Restablecer automáticamente el bloqueo de tus incursiones?
        - [Choice]: si
          - (end)
        - [Choice]: No
          - (end)
    - (Condition: Si Fetcher ya estaba restableciendo automáticamente el bloqueo de incursiones:)
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
- ((Sólo si el reinicio está habilitado:))
  - REINICIAR
    - Solo puedes restablecer la incursión de Mazcab una vez cada 48 horas. ¡Asegúrate de que deseas restablecer tu progreso antes de continuar!
      - CANCELAR
        - ((Regresa a la interfaz de Mazcab Raid Lock sin cambios.))
      - CONFIRMAR
        - El progreso de tu incursión se ha reiniciado.
        - ((Regresa a la interfaz de Mazcab Raid Lock con los fondos cambiados a verde y el botón de reinicio desactivado.))
- ((Al pasar el cursor sobre el botón de reinicio deshabilitado:))
  - El progreso del jefe solo se puede restablecer una vez cada 48 horas.
