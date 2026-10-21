# Harmony pillar farmer

- **Original Wiki Page**: [Transcript:Harmony pillar farmer](https://runescape.wiki/w/Transcript%3AHarmony%20pillar%20farmer)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Harmony pillar farmer:** ¡Bienvenido al hogar de los mayores secretos del Clan Meilyr para hacer pociones!
- **Harmony pillar farmer:** Compartimos conocimientos libremente entre nosotros. Los forasteros, sin embargo, deben comerciar.
- (Condition: Sólo la primera vez:)
  - **Harmony pillar farmer:** Antes de continuar, tenemos algunos de nuestros propios conocimientos para compartir con usted.
  - **Harmony pillar farmer:** Dentro de las antiguas tierras (tu gente se refiere a ellas como Daemonheim), el conocimiento del pasado de nuestro clan permanece fuera de nuestro alcance.
  - **Harmony pillar farmer:** Nuestro clan ha adquirido recientemente los medios para traducir la antigua lengua élfica. Si encuentra algo que parezca coincidir con esto en sus viajes, tráiganoslo y compartiremos este conocimiento.
  - [El comerciante proporciona un diario, que contendrá automáticamente todo lo que encuentre en Daemonheim.]
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: ¿Tienes algo para vender?
    - **Granjero:** Sí, puedo proporcionar semillas para cultivar musgo de armonía o recetas para pociones combinadas.
    - [Menu]: Selecciona una opción
      - [Choice]: Semillas, por favor.
        - (opens= Meilyr Clan Store)
      - [Choice]: Recetas, por favor.
        - (opens= Recipe Shop)
      - [Choice]: Me gustaría preguntar algo más.
        - (previous)
      - [Choice]: Adiós.
        - (end)
  - [Choice]: ¿Qué puedes decirme sobre estos pilares?
    - **Harmony pillar farmer:** El funcionamiento interno de los pilares de la armonía es un misterio. Nuestra investigación indica que funcionan con las habilidades de quien planta una semilla de musgo de armonía, que puedo proporcionarle... por un precio.
    - **Harmony pillar farmer:** La habilidad con la que se relaciona un pilar cambia cada día, o cuando está completamente saciado y cosechado. Una vez que se coloca una semilla, es irrevocable y debes terminar la cosecha antes de que cambie.
    - **Harmony pillar farmer:** El musgo no crecerá con el tiempo. Sólo a medida que crezcas, crecerá.
    - <span style="display: inline-block; text-align: center;">Los pilares de armonía no crecen como los parches agrícolas normales.<br><br>Debes ganar 50 000 XP en la habilidad con la que estás en sintonía para avanzar en una etapa de crecimiento. Un pilar tiene 4 etapas de crecimiento.</span>
    - (previous)
  - [Choice]: How much harmony moss have I harvested?|cond=Después de haber preguntado sobre los pilares al menos una vez antes:
    - (Condition: Si es menor o igual a 50 musgo:)
      - **Harmony pillar farmer:** Hmm, ¿cuál era el nombre? Ah... sí. Ahí vamos. Según mis cuentas, has cosechado [número] unidades.
    - (Condition: Si hay más de 50 musgo:)
      - **Harmony pillar farmer:** ¡Has cosechado mucho! Dejé de contar cuando llegaste a las 50 unidades.
    - (previous)
  - [Choice]: Adiós.
    - (end)

### Interacting for the first time after reaching level 99 in all skills

- **Harmony pillar farmer:** El clan Meilyr respeta a quienes dominan todo lo que se puede dominar. Estas pociones se ofrecen a quienes logran tales hazañas.
- (receives= perfect juju agility potion, perfect juju dungeoneering potion, perfect juju farming potion, perfect juju herblore potion, perfect juju mining potion, perfect juju prayer potion, perfect juju smithing potion and perfect juju woodcutting potion)
