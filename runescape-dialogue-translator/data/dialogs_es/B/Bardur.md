# Bardur

- **Original Wiki Page**: [Transcript:Bardur](https://runescape.wiki/w/Transcript%3ABardur)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to

- (Condition: If the player's Fremennik name is Bardur:)
  - (Condition: If the player is male:)
    - **Bardur:** ¡Ah, Bardur mi hermano de nombre! ¡Qué suerte que nos encontremos aquí así!
  - (Condition: If the player is female:)
    - **Bardur:** ¡Ah, Bardur, mi hermana de nombre! ¡Qué suerte que nos encontremos aquí así!
- **Player:** Hola, Bardur. ¿Te estás divirtiendo?
- **Bardur:** ¡He estado aquí todo el día, masacrando a los engendros de boca de daga para que ninguno pase!
- **Bardur:** ¡El brazo de mi espada se cansa y la sangre de mis enemigos cuelga pesadamente de mi ropa!
- **Bardur:** ¡¡¡POR CLARO QUE ME ESTOY DIVERTIENDO!!!
- **Player:** ¿Puedes contarme algo sobre las cuevas de aquí abajo?
- **Bardur:** ¡Sí, eso puedo [Fremennik name]! ¡Allá se encuentra la guarida de los Reyes Boca de Daga, las tres bestias legendarias!
- **Bardur:** ¡Entreno mis habilidades aquí sobre su loque, para prepararme para la lucha que se avecina!
- **Player:** Bien, gracias Bardur. ¿Tienes algo de comida contigo?
- **Bardur:** Ah, ¿no viniste preparado [Fremennik name]?
- **Bardur:** ¡No tengo nada de sobra, pero mi equipo se debilita bajo el ataque de los engendros de boca de daga!
- **Bardur:** Te cambiaré un tiburón finamente cocido si tienes un reemplazo para mi yelmo, mi escudo o mi espada...
- (Condition: If the player does not have a Fremennik blade, Fremennik shield, or Fremennik helm:)
  - **Player:** Lo siento, no tengo nada que busques...
- (Condition: If the player has a Fremennik blade, Fremennik shield, or Fremennik helm:)
  - **Bardur:** Dame cualquier equipo que quieras intercambiar y te pagaré un tiburón por ello.

### Using a Fremennik blade, Fremennik shield, or Fremennik helm on Bardur

- **Bardur:** ¡Ah, justo lo que estaba buscando! ¿Quieres cambiarme eso por un tiburón cocido?
- [Menu]: ¿Comerciar con Bardur?
  - [Choice]: SI
    - (receives=one shark)
    - **Bardur:** ¡Ah, esto me servirá como respaldo! Mi agradecimiento a ti [Fremennik name], ¡confío en que algún día cantaremos juntos canciones de gloriosas batallas en el largo salón de Rellekka!
  - [Choice]: NO
    - **Bardur:** Como desees, [Fremennik name] Mis armas me han durado tanto tiempo, mantendré mi confianza en ellas todavía.
