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
        - ((Si el player no tiene un amuleto de serpiente o una canasta de serpientes en su inventario:))
          - **Badir the Snake Charmer:** Si eso significa que me dejarás en paz, te daría mi súper kit inicial encantador de serpientes, completo con flauta y canasta.
          - (receives=snake charm and snake basket)
          - [El encantador de serpientes te regala una flauta encantadora de serpientes y una cesta.]
        - ((Si el player ya tiene un amuleto de serpiente y una canasta de serpientes en su inventario:))
          - **Badir the Snake Charmer:** Bueno, ¿qué te detiene entonces? Tienes tu propia flauta encantadora de serpientes.
        - ((Si el player tiene una canasta de serpientes en su inventario pero no un amuleto de serpiente:))
          - **Badir the Snake Charmer:** Ah, veo que has perdido tu encantadora flauta. ¡Aquí tienes, ahora déjame en paz! Estás distrayendo a mis apostadores... erm, quiero decir, multitud.
          - (receives=snake charm)
        - ((Si el player tiene un amuleto de serpiente en su inventario pero no una canasta de serpientes:))
          - **Badir the Snake Charmer:** Ah, veo que has perdido tu cesta. ¡Aquí tienes, ahora déjame en paz! Estás arruinando el espectáculo.
          - (receives=snake basket)
      - [Choice]: Quiero hablarte sobre el encantador de animales.
        - **Player:** Quiero hablarte sobre el encantador de animales.
        - ((Si el player ha perdido su pergamino musical y su flauta:))
          - **Player:** He perdido parte del equipo que me diste.
          - **Badir the Snake Charmer:** ¿Qué necesitas?
          - **Player:** Necesito una flauta nueva y algo de música.
          - **Badir the Snake Charmer:** Ahí lo tienes. Ahora, si no te importa, estoy ocupado tratando de encantar a esta serpiente.
          - (receives=music scroll)
          - (receives=Snake Charm)
        - ((Si el player ha perdido solo su desplazamiento de música))
          - **Player:** He perdido parte del equipo que me diste.
          - **Badir the Snake Charmer:** ¿Qué necesitas?
          - **Player:** Necesito más música.
          - **Badir the Snake Charmer:** Ahí lo tienes. Ahora, si no te importa, estoy ocupado tratando de encantar a esta serpiente.
          - (receives=music scroll)
        - ((Si el player solo ha perdido su flauta))
          - **Player:** He perdido parte del equipo que me diste.
          - **Badir the Snake Charmer:** ¿Qué necesitas?
          - **Player:** Necesito otra flauta.
          - **Badir the Snake Charmer:** Ahí lo tienes. Ahora, si no te importa, estoy ocupado tratando de encantar a esta serpiente.
          - (receives=Snake Charm)
        - ((Si el player tiene un pergamino musical y una flauta en su inventario:))
          - **Badir the Snake Charmer:** ¿Sí?
          - **Player:** ¿Puedes enseñarme algo más sobre el encantamiento de animales?
          - **Badir the Snake Charmer:** No, lo dudo. Creo que tus talentos se encuentran en otras áreas.
  - [Choice]: No.
    - (end)
