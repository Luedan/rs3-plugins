# Quartermaster (Clan Citadels)

- **Original Wiki Page**: [Transcript:Quartermaster (Clan Citadels)](https://runescape.wiki/w/Transcript%3AQuartermaster%20%28Clan%20Citadels%29)
- **Letter**: `Q`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Needs dialogue for updating the job list and changing the build tick}}

### In the Clan Citadel


#### Hablando con él

- **Intendente:** ¡Buenos días! ¿Cómo puedo ayudar?
- [Menu]: Elige una opción:
  - [Choice]: ¿Qué haces aquí?
    - **Intendente:** Soy el intendente de tu clan. Llevo un registro de los trabajos que tú o tus compañeros de clan habéis marcado para realizar dentro de la ciudadela; los recursos que se necesitarán; y si puede cumplir con ese requisito.
    - **Intendente:** También soy capaz de alterar el día en el que se modifican tus edificios y los recursos utilizados, y puedo otorgar experiencia adicional.
    - [Menu]: Selecciona una opción
      - [Choice]: Cuéntame más sobre la lista de trabajos.
        - **Intendente:** En la lista de trabajos verás todas las solicitudes de degradación, cuotas de mantenimiento y mejoras pendientes para la ciudadela de tu clan. Los trabajos de mantenimiento permanecerán mientras tengas un edificio en tu ciudadela que requiera mantenimiento; los demás se eliminan cuando se llevan a cabo.
        - **Intendente:** Puede hacer clic en los trabajos de la lista para ver más información sobre sus costos y los recursos disponibles para realizar esos trabajos, y cualquier advertencia relacionada con trabajos que actualmente tienen requisitos insuficientes o no cumplidos.
        - **Intendente:** Si tienes los permisos de acceso necesarios de los oficiales de tu clan, puedes modificar la lista arrastrando trabajos para reordenarlos o cancelar trabajos de degradación o mejora.
        - **Intendente:** También puedes pasar de los trabajos de actualización a la interfaz de construcción para realizar modificaciones si es necesario, pero, francamente, esa es más área del artesano que mía.
        - [Menu]: ¿Quieres abrir la lista ahora?
          - [Choice]: si
            - *(Se abre la interfaz de lista de trabajos)*
          - [Choice]: No
            - (end)
      - [Choice]: Cuéntame cómo mover el tick de compilación.
        - El propietario, diputado o supervisor de un clan puede mover la marca de construcción a un día de la semana y a una hora del día más adecuada para la actividad de su clan. Sólo háblame al respecto y configuraré tu tick de compilación para que venza exactamente una semana a partir de ese momento.
        - **Intendente:** Debo advertirle, sin embargo, que hacerlo le costará una semana de mantenimiento por adelantado. Se te permitirá hacerlo sólo una vez por semana y no podrás mover la garrapata al mismo día en el que ya cae.
        - **Intendente:** Mover la marca de compilación tampoco llevará a cabo ningún trabajo de actualización o degradación que hayas enumerado.
        - [Menu]: ¿Desea mover el tick de compilación?
          - [Choice]: si
            - (Condition: If clan rank is high enough:)
              - {{Transcript missing}}
            - (Condition: If clan rank is not high enough:)
              - Tu rango no es lo suficientemente alto como para cambiar el día de construcción/mantenimiento de tu clan.
          - [Choice]: No
            - (end)
      - [Choice]: Acerca de los aumentos de experiencia...
        - (Condition: If the player has been in the clan for less than 1 week, and received bonus experience within 1 week:)
          - **Intendente:** Me temo que te he dado experiencia hace poco y como eres nuevo en el clan no puedo darte más hasta al menos hasta dentro de un día.
        - (Condition: If the player has already received bonus experience for the current build cycle:)
          - **Intendente:** Ya te he dado algo de experiencia; No podré darte más hasta después del próximo ciclo de construcción.
        - (Condition: If the player has not yet received bonus experience for the current build cycle:)
          - [Menu]: Selecciona una opción
            - [Choice]: ¿Puedes darme alguna experiencia?
              - **Intendente:** A medida que trabajes para tu clan, reuniendo los recursos que necesitamos para construir y mantener la Fortaleza, progresarás para obtener un aumento de experiencia. Podrás utilizar la experiencia adicional tanto aquí en la ciudadela como en el resto del mundo.
              - **Intendente:** Debo advertirles que solo puedo ofrecer un bono por semana.
              - **Intendente:** Ahora, veamos...
              - (Condition: If the player has not yet gathered enough resources for the current build cycle:)
                - **Intendente:** Nuestros registros muestran que no ha trabajado para nosotros esta semana.
              - (Condition: If the player has not yet gathered enough resources for the current build cycle:)
                - **Intendente:** Sí; has trabajado suficiente para ganar experiencia. ¿En qué habilidad te gustaría hacerlo?
                - ((Skill selection interface opens.))
            - [Choice]: ¿Cómo puedo ganar experiencia extra?
              - **Intendente:** Obtener el impulso es simplemente cuestión de trabajar en cualquiera de nuestros edificios de recolección de recursos, desde el árbol Woodcutting hasta la arboleda Summoning. Una vez que hayas reunido lo suficiente, reparte como quieras entre las parcelas disponibles para el clan, puedo otorgarte el bono.
              - (previous)
            - [Choice]: Estoy aquí para un impulso de experiencia.
              - (Condition: If the player has not yet gathered enough resources for the current build cycle:)
                - **Intendente:** Lo siento mucho. Necesitarás trabajar más antes de que pueda brindarte experiencia.
              - (Condition: If the player has not yet gathered enough resources for the current build cycle:)
                - **Intendente:** Sí; has trabajado suficiente para ganar experiencia. ¿En qué habilidad te gustaría hacerlo?
                - ((Skill selection interface opens.))
  - [Choice]: Me gustaría consultar la lista de trabajos.
    - *(Se abre la interfaz de lista de trabajos)*
  - [Choice]: Me gustaría mover el tick de construcción del clan.
    - (Condition: If clan rank is high enough:)
      - {{Transcript missing}}
    - (Condition: If clan rank is high enough:)
      - Tu rango no es lo suficientemente alto como para cambiar el día de construcción/mantenimiento de tu clan.
  - [Choice]: Acerca de la experiencia adicional...
    - (above|bxp)
  - [Choice]: ¿Puedes venderme algunos potenciadores de la Ciudadela del clan?
    - **Intendente:** ¡Por supuesto! ¿Cuantos quieres?
    - [Menu]: ¿Cuántos te gustaría comprar?
      - [Choice]: Uno.
        - (La interfaz de compra se abre para Clan Citadel Booster (x1) por 100 RuneCoins)
      - [Choice]: Tres.
        - (Se abre la interfaz de compra para Clan Citadel Booster (x3) por 250 RuneCoins)
      - [Choice]: Seis.
        - (Se abre la interfaz de compra para Clan Citadel Booster (x6) por 450 RuneCoins)
      - [Choice]: Ninguno, cambié de opinión.
        - (end)

#### Mover opción de marca

- (above|move)

#### Opción de reclamar XP

- (above|claim)
