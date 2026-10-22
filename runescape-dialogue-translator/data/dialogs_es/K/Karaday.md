# Karaday

- **Original Wiki Page**: [Transcript:Karaday](https://runescape.wiki/w/Transcript%3AKaraday)
- **Letter**: `K`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Tai Bwo Wannai, after Jungle Potion

- **Karaday:** Hola... gracias por ayudar a Trufitus a comunicarse con los dioses Bwana. Hemos podido regresar al pueblo gracias a vuestra ayuda.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué haces aquí?
    - **Player:** ¿Qué haces aquí?
    - **Karaday:** Oh, soy pescador de profesión y a veces ayudo a mi padre, Safta Doc.
    - (initial)
  - [Choice]: ¿Hay algo interesante que hacer aquí?
    - **Player:** ¿Hay algo interesante que hacer aquí?
    - {{Trandom}}
      - (Diálogo 1 :)
        - **Karaday:** Bwana, si alguien más me hace esa pregunta hoy, ¡explotaré! ¡Ve y pregúntale a Murcaily!
      - (Diálogo 2 :)
        - **Karaday:** Solo estoy disfrutando del sol, Bwana. Intente preguntarle a Murcaily.
      - (Diálogo 3 :)
        - **Karaday:** Bueno, creo que hay trabajo por hacer... tal vez Murcaily pueda ayudarte. Por lo general, atiende el bosquecillo de madera al este de la cabaña de Trufitus.
      - (Diálogo 4 :)
        - **Karaday:** Lo siento Bwana, ya estoy ocupado, ¿por qué no vas y hablas con Murcaily? Está en alguna parte del pueblo.
  - [Choice]: cond=With Tai Bwo Wannai Cleanup started|He estado trabajando en el pueblo.
    - (Condition: With unclaimed Tai Bwo Wannai favour:)
      - **Karaday:** Oye, te he visto trabajando en el pueblo. Has estado haciendo un muy buen trabajo aquí para nosotros. Déjame darte algo por tu molestia.
      - (receives=trading sticks)
    - (Condition: Without unclaimed Tai Bwo Wannai favour:)
      - **Karaday:** Ya te he dado algunos palitos de intercambio y no tengo ninguno más en este momento. ¿Por qué no vas y hablas con algunos de los otros aldeanos y consigues algunas contribuciones?
  - [Choice]: Bien, gracias.
    - **Player:** Vale, gracias.

#### Ocasionalmente con favor no reclamado

- **Karaday:** Oye, te he visto trabajando en el pueblo. Has estado haciendo un muy buen trabajo aquí para nosotros. Déjame darte algo por tu molestia.
- (receives=trading sticks)
- Obtienes palos comerciales [número]. El favor restante asciende a [percentage].

#### Con una máscara tribal equipada.

- {{Trandom}}
  - (Diálogo 1 :)
    - **Karaday:** Ahhhhhhhh - ¡Aléjate de mí, bestia!
    - (continue)
  - (Diálogo 2 :)
    - **Karaday:** ¡Ahhhhhhhh!
    - (continue)
  - (Diálogo 3 :)
    - **Karaday:** Ahhhhhhhh - ¡Es un monstruo!
    - (continue)
  - (Diálogo 4 :)
    - **Karaday:** ¡Waahhhhh! - ¡Es una bestia malvada que viene a comerse mi alma!
    - (continue)
- **Player:** ¿Cuál es el problema? ¡Oh, estoy usando esta gran máscara aterradora! Será mejor que me lo quite antes de empezar a hablar con los nativos.
