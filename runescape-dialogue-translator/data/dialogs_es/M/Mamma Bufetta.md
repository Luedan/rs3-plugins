# Mamma Bufetta

- **Original Wiki Page**: [Transcript:Mamma Bufetta](https://runescape.wiki/w/Transcript%3AMamma%20Bufetta)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Tai Bwo Wannai, after Jungle Potion

- **Mamma Bufetta:** Hola... gracias por ayudar a Trufitus a comunicarse con los dioses Bwana. Hemos podido regresar al pueblo gracias a vuestra ayuda.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué haces aquí?
    - **Player:** ¿Qué haces aquí?
    - **Mamma Bufetta:** He estado cocinando algunas arañas asadas... ¿Puedo mostrarte cómo hacerlas si quieres?
    - [Menu]: Selecciona una opción
      - [Choice]: Errrr... ¡qué asco, arañas asadas, eso suena asqueroso!
        - **Player:** Errrr... ¡qué asco, arañas asadas, eso suena asqueroso!
        - **Mamma Bufetta:** Bueno, puedes hacerlo amigo mío, ¡pero tengo que decirte que están deliciosos!
        - **Mamma Bufetta:** ¡Mmmm, mmm, mmmmmm!
      - [Choice]: Mmmm, supongo que podría considerarse un manjar, entonces, ¿sí, por favor?
        - **Player:** Hmm, supongo que podría considerarse un manjar, así que ¿sí, por favor?
        - **Mamma Bufetta:** Ok, amigo mío, ¡simplemente necesitas un palo adecuado para ensartar el cadáver de la araña y luego asarlo al fuego!
        - **Player:** ¿Qué tipo de palo y dónde puedo conseguirlo?
        - **Mamma Bufetta:** Bueno, prefiero usar un palo para brocheta, puedes hacer uno con un palo de paja usando un machete. O, si estás atascado, siempre puedes usar el eje de una flecha, aunque tienden a ser inútiles una vez que hayas terminado de comerte la araña.
        - **Player:** ¡Vale, gracias!
      - [Choice]: Me gustaría hacer otra pregunta.
        - (initial)
      - [Choice]: Lo siento, tengo que irme.
        - **Player:** Lo siento, tengo que irme.
    - (initial)
  - [Choice]: ¿Hay algo interesante que hacer aquí?
    - **Player:** ¿Hay algo interesante que hacer aquí?
    - {{Trandom}}
      - (Diálogo 1 :)
        - **Mamma Bufetta:** Bwana, si alguien más me hace esa pregunta hoy, ¡explotaré! ¡Ve y pregúntale a Murcaily!
      - (Diálogo 2 :)
        - **Mamma Bufetta:** Solo estoy disfrutando del sol, Bwana. Intente preguntarle a Murcaily.
      - (Diálogo 3 :)
        - **Mamma Bufetta:** Bueno, creo que hay trabajo por hacer... tal vez Murcaily pueda ayudarte. Por lo general, atiende el bosquecillo de madera al este de la cabaña de Trufitus.
      - (Diálogo 4 :)
        - **Mamma Bufetta:** Lo siento Bwana, ya estoy ocupado, ¿por qué no vas y hablas con Murcaily? Está en alguna parte del pueblo.
  - [Choice]: cond=With Tai Bwo Wannai Cleanup started|He estado trabajando en el pueblo.
    - (Condition: With unclaimed Tai Bwo Wannai favour:)
      - **Mamma Bufetta:** Oye, te he visto trabajando en el pueblo. Has estado haciendo un muy buen trabajo aquí para nosotros. Déjame darte algo por tu molestia.
      - (receives=trading sticks)
    - (Condition: Without unclaimed Tai Bwo Wannai favour:)
      - **Mamma Bufetta:** Ya te he dado algunos palitos de intercambio y no tengo ninguno más en este momento. ¿Por qué no vas y hablas con algunos de los otros aldeanos y consigues algunas contribuciones?
  - [Choice]: Bien, gracias.
    - **Player:** Vale, gracias.

#### Ocasionalmente con favor no reclamado

- **Mamma Bufetta:** Oye, te he visto trabajando en el pueblo. Has estado haciendo un muy buen trabajo aquí para nosotros. Déjame darte algo por tu molestia.
- (receives=trading sticks)
- Obtienes palos comerciales [número]. El favor restante asciende a [percentage].

#### Con una máscara tribal equipada.

- {{Trandom}}
  - (Diálogo 1 :)
    - **Mamma Bufetta:** Ahhhhhhhh - ¡Aléjate de mí, bestia!
    - (continue)
  - (Diálogo 2 :)
    - **Mamma Bufetta:** ¡Ahhhhhhhh!
    - (continue)
  - (Diálogo 3 :)
    - **Mamma Bufetta:** Ahhhhhhhh - ¡Es un monstruo!
    - (continue)
  - (Diálogo 4 :)
    - **Mamma Bufetta:** ¡Waahhhhh! - ¡Es una bestia malvada que viene a comerse mi alma!
    - (continue)
- **Player:** ¿Cuál es el problema? ¡Oh, estoy usando esta gran máscara aterradora! Será mejor que me lo quite antes de empezar a hablar con los nativos.
