# Armoursmith

- **Original Wiki Page**: [Transcript:Armoursmith](https://runescape.wiki/w/Transcript%3AArmoursmith)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### First conversation

- **Armoursmith:** No está bien. Nada bueno.
- **Player:** ¿Qué no lo es?
- **Armoursmith:** Tu caparazón, no sirve.
- El armero mueve un martillo en dirección a tu estómago.
- **Armoursmith:** Los Airut lo aplastarán, sus perros lo desmenuzarán y el desierto lo cocinará.
- Seleccione una opción
  - ¿Cómo me sugieres que mejore mi caparazón?
    - **Armoursmith:** Mazcab es viejo, esconde muchos secretos, tengo fragmentos de estos secretos. Tráeme a Teci, los convertiré en un caparazón mejor para ti. Quizás encuentres tus propios secretos de Mazcab. Quizás formen un caparazón mejor que el mío. Hasta entonces, ven a mí.
    - (Action: continuar|iniciar)
  - Creo que mi caparazón funcionará bien, gracias.
    - **Player:** Creo que mi caparazón funcionará bien, gracias.

### Subsequent conversations

- *(Sin ninguna pieza Achto equipada:)*
  - **Armoursmith:** Todavía no es lo suficientemente bueno, humano.
  - *(Continúa a continuación.)*
- *(Con piezas Achto equipadas:)*
  - **Armoursmith:** Luce mucho mejor como humano.
  - *(Continúa a continuación.)*
- Seleccione una opción{{anchor|init}}
  - ¿Podrías hacerme una armadura?
    - (Action: opens=Recompensas de incursión)
  - ¿Dónde puedo encontrar a Teci?
    - **Armoursmith:** Teci se puede encontrar al derrotar a oponentes dignos en el área al norte de esta barrera.
    - (Action: inicial|inicio)
  - ¿Puedes imbuirme un anillo?
    - *(Como en los anillos de imbución.)*
  - Adiós.
    - (end)

### Imbuing rings

- **Armoursmith:** ¿Cuál quieres que imbuya?
- [Menu]: Selecciona una opción
  - [Choice]: Can you remove the enchantment from my item?|cond=Sólo con un anillo imbuido en backpack
    - **Player:** ¿Pueden eliminar el efecto de mi artículo?
    - **Armoursmith:** No hay problema. Sólo usa el anillo conmigo y veré qué puedo hacer.
  - [Choice]: Anillo de la fortuna (2500 Teci)
    - (continue)
  - [Choice]: Suerte de los enanos (7.500 Teci)
    - (continue)
  - [Choice]: Anillo de sello de Hazelmere (10,000 Teci)
    - (continue)
  - [Choice]: Más...
    - [Menu]: Selecciona una opción
      - [Choice]: Anillo de la Muerte (15.000 Teci)
        - (continue)
      - [Choice]: Anillo del cirujano de asilo (10.000 Teci)
        - (continue)
      - [Choice]: Atrás...
        - (previous)
- **Player:** [Chosen ring], por favor.
- (Condition: Si el player no tiene el anillo elegido en el inventario:)
  - **Player:** En realidad, no tengo ninguno de esos anillos conmigo.
- (Condition: Si el player no tiene el anillo elegido en el inventario pero no tiene suficiente Teci:)
  - **Player:** En realidad, no tengo tanto {{Sic|Teci}}
- (Condition: Si el player tiene el anillo elegido en el inventario y suficiente Teci:)
  - (removes=unimbued ring) (receives=imbued ring)
  - **Armoursmith:** Aquí tienes, humano, he imbuido la cáscara de tu dedo. Vuelve si quieres que elimine el efecto.

### Using an imbued ring

- [Menu]: ¿Quitar el encantamiento?
  - [Choice]: si
    - (Se elimina el encantamiento.)
    - **Armoursmith:** Ahí lo tienes.
  - [Choice]: No
    - (end)
