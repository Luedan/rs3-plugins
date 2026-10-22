# Badir the Snake Charmer

- **Original Wiki Page**: [Transcript:Badir the Snake Charmer](https://runescape.wiki/w/Transcript%3ABadir%20the%20Snake%20Charmer)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Disculpe...
- El encantador de serpientes te ignora. Tendrás que encontrar alguna manera de hacer que preste atención.
- '''¿Lanzar una moneda al bote del dinero?
  - [Choice]: Sí.
    - (removes=one coin)
    - [El encantador de serpientes sale de su trance y dirige toda su atención hacia ti.]
    - '''Selecciona una opción
      - [Choice]: Vaya, un encantador de serpientes. ¿Puedo intentarlo? ¿Por favor?
        - **Player:** Vaya, un encantador de serpientes. ¿Puedo intentarlo? ¿Puedo intentarlo? ¿Por favor?
        - ((If the player does not have a snake charm or snake basket in inventory:))
          - **Badir the Snake Charmer:** Si eso significa que me dejarás en paz, te daría mi súper kit inicial encantador de serpientes, completo con flauta y canasta.
          - (receives=snake charm and snake basket)
          - [El encantador de serpientes te regala una flauta encantadora de serpientes y una cesta.]
        - ((If the player already has a snake charm and snake basket in inventory:))
          - **Badir the Snake Charmer:** Bueno, ¿qué te detiene entonces? Tienes tu propia flauta encantadora de serpientes.
        - ((If the player has a snake basket in inventory but not a snake charm:))
          - **Badir the Snake Charmer:** Ah, veo que has perdido tu encantadora flauta. ¡Aquí tienes, ahora déjame en paz! Estás distrayendo a mis apostadores... erm, quiero decir, multitud.
          - (receives=snake charm)
        - ((If the player has a snake charm in inventory but not a snake basket:))
          - **Badir the Snake Charmer:** Ah, veo que has perdido tu cesta. ¡Aquí tienes, ahora déjame en paz! Estás arruinando el espectáculo.
          - (receives=snake basket)
      - [Choice]: Quiero hablarte sobre el encantador de animales.
        - **Player:** Quiero hablarte sobre el encantador de animales.
        - ((If the player has lost their music scroll and flute:))
          - **Player:** He perdido parte del equipo que me diste.
          - **Badir the Snake Charmer:** ¿Qué necesitas?
          - **Player:** Necesito una flauta nueva y algo de música.
          - **Badir the Snake Charmer:** Ahí lo tienes. Ahora, si no te importa, estoy ocupado tratando de encantar a esta serpiente.
          - (receives=music scroll)
          - (receives=Snake Charm)
        - ((If the player has lost their music scroll only))
          - **Player:** He perdido parte del equipo que me diste.
          - **Badir the Snake Charmer:** ¿Qué necesitas?
          - **Player:** Necesito más música.
          - **Badir the Snake Charmer:** Ahí lo tienes. Ahora, si no te importa, estoy ocupado tratando de encantar a esta serpiente.
          - (receives=music scroll)
        - ((If the player has lost their flute only))
          - **Player:** He perdido parte del equipo que me diste.
          - **Badir the Snake Charmer:** ¿Qué necesitas?
          - **Player:** Necesito otra flauta.
          - **Badir the Snake Charmer:** Ahí lo tienes. Ahora, si no te importa, estoy ocupado tratando de encantar a esta serpiente.
          - (receives=Snake Charm)
        - ((If the player has a music scroll and flute in their inventory:))
          - **Badir the Snake Charmer:** ¿Sí?
          - **Player:** ¿Puedes enseñarme algo más sobre el encantamiento de animales?
          - **Badir the Snake Charmer:** No, lo dudo. Creo que tus talentos se encuentran en otras áreas.
  - [Choice]: No.
    - (end)
