# Gatekeeper

- **Original Wiki Page**: [Transcript:Gatekeeper](https://runescape.wiki/w/Transcript%3AGatekeeper)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At the entrance to Zanaris Market area


#### Antes de A Fairy Tale III - Batalla en Ork's Rift


##### Habla con

- **Player:** ¿Qué pasó con el old man que solía ser el portero?
- **Gatekeeper:** ¿Te refieres a mi padre? Se jubiló. Me he hecho cargo del negocio familiar.
- **Player:** ¿Tu padre? ¡Pero no te pareces en nada a él!
- **Gatekeeper:** No. Afortunadamente para mí, heredé mi buena apariencia de mi madre.

##### Interactuando con la puerta

- (Condition: If the player has any kind of sacks:)
  - **Gatekeeper:** Lo sentimos, no podemos permitirle traer esos sacos al mercado por razones de seguridad.<!--Always plural "sacks".-->
- (Condition: Without any kind of sacks:)
  - **Gatekeeper:** No puedes pasar por esta puerta sin pagar el impuesto comercial.
  - **Player:** ¿A cuánto asciende el impuesto?
  - **Gatekeeper:** El costo es de un diamante.
  - [Menu]: Selecciona una opción
    - [Choice]: Está bien...
      - **Player:** Está bien...
      - (Condition: Without a diamond:)
        - **Player:** ...pero...
        - **Player:** No he traído mis diamantes conmigo.
        - **Gatekeeper:** Sin impuestos, sin entrada.
      - (Condition: With a diamond:)
        - (removes=diamond)
        - Le das un diamante al portero.
        - (Action: el player entra por la puerta mágica.)
    - [Choice]: ¿Un diamante? ¿Estás loco?
      - **Player:** ¿Un diamante? ¿Estás loco?
      - **Gatekeeper:** Para nada. Esas son las reglas.
    - [Choice]: No he traído mis diamantes conmigo.
      - **Player:** No he traído mis diamantes conmigo.
      - **Gatekeeper:** Sin impuestos, sin entrada.
    - [Choice]: ¿Qué haces con todos los diamantes que obtienes?
      - **Player:** ¿Qué haces con todos los diamantes que obtienes?
      - **Gatekeeper:** ¿Has oído hablar alguna vez de las luces de hadas? Bueno, ¿cómo crees que los hacemos? Primero recolectamos un montón de gemas y luego conseguimos que una araña las haga tejer en una larga red, encendemos las joyas imbuyendo a cada una de ellas con un poco de magia.
      - **Player:** ¿Entonces me estás diciendo que las luces de hadas están hechas de gemas?
      - **Gatekeeper:** Así es, ¿de qué otra manera podríamos hacer que centelleen tan bellamente?

#### Después de A Fairy Tale III - Batalla en Ork's Rift


##### Habla con

- **Gatekeeper:** Muchas gracias por salvar a Zanaris del padrino de Fairy y sus orkos.
- **Gatekeeper:** Siéntete libre de entrar y salir del mercado cuando quieras; No podríamos cobrarle ni un diamante después de todo lo que ha hecho por nosotros.
- [Menu]: Selecciona una opción
  - [Choice]: Pues, gracias.
    - **Player:** Bueno, gracias.
    - **Gatekeeper:** No, gracias.
  - [Choice]: ¿Qué pasó con el old man que solía ser el portero?
    - (above|inherited)

##### Interactuando con la puerta

- (Condition: If the player has any kind of sacks:)
  - **Gatekeeper:** Lo sentimos, no podemos permitirle traer esos sacos al mercado por razones de seguridad.<!--Always plural "sacks".-->

##### Usando el certificado de Nuff en ellos

- (Condition: Before studying the certificate:)
  - [Le muestra el certificado al portero.]
  - **Player:** ¿Sabes lo que significan estas extrañas marcas?
  - **Gatekeeper:** ¿Que has estado garabateando? Si no te importa, tengo un trabajo que hacer. Por favor deja de distraerme.
- (Condition: After studying the certificate:)
  - [Le muestra el certificado al portero.]
  - **Player:** ¿Sabes lo que significan estas extrañas marcas?
  - **Gatekeeper:** No, no lo hago y estoy intentando trabajar aquí. Por favor deja de distraerme.

### Near the entrance to the Tanglefoot's lair


#### Habla con


##### Durante A Fairy Tale I - Dolores de crecimiento

- **Player:** ¿Qué haces hasta aquí? ¿No deberías estar en la puerta del mercado?
- **Gatekeeper:** Sí, ese es mi lugar habitual, pero el Padrino dijo que debería estar aquí, así que aquí estoy.

##### Después de A Fairy Tale I - Dolores de crecimiento

- **Gatekeeper:** Hola, ¿acabas de llegar de las puertas del mercado? ¿Mis hermanos están haciendo bien su trabajo? ¡Me preocupa que empiecen a permitir que la gente entre al mercado de forma gratuita sin que yo esté allí para supervisarlos!

#### Entrando a la arboleda


##### Antes de obtener tijeras de podar mágicas durante A Fairy Tale I - Dolores de crecimiento

- **Guardián de la puerta:** Me temo que a nadie se le permite entrar ahí, órdenes del jefe.

##### Después de obtener tijeras de podar mágicas durante A Fairy Tale I - Growing Pains

- **Guardián de la puerta:** He recibido órdenes de dejarte pasar si quieres. Buena suerte.

##### Después de derrotar a Tanglefoot

- **Guardián de la puerta:** Ten cuidado ahí dentro, todavía hay algunos de esos bebés Tanglefootii por ahí.
- (Action: el player aparece en la arboleda.)
- (Condition: During A Fairy Tale I, if the Queen's secateurs have been lost:)
  - (receives=Queen's secateurs)
  - [¡Encontrarás las tijeras de podar de Fairy Queen!]
