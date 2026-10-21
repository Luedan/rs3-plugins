# Ogre boat

- **Original Wiki Page**: [Transcript:Ogre boat](https://runescape.wiki/w/Transcript%3AOgre%20boat)
- **Letter**: `O`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At the Feldip Hills

- **Bugs:** Dad dice que puedes llevarte a Karamja con nosotros si quieres. ¡Pero primero nos das dos mordiscos!
- [Menu]: Selecciona una opción
  - [Choice]: Sí, por favor, te llevaré a Karamja.
    - (Condition: Si el player no tiene dos chompies:)
      - **Ogre boat:** No tienes mordiscos... ¡ni viajes en barco!
    - (Condition: Si el player tiene pago suficiente:)
    - (removes=two cooked chompies)
      - (Action: Player se transporta al oeste de Tai Bwo Wannai.)
      - El tronco apenas apto para navegar llega a la playa de Karamja.
  - [Choice]: No gracias.
    - **Player:** No, gracias.

### At Karamja

- **Bugs:** Dad dice que puedes regresar con nosotros si quieres. ¡Pero primero nos das dos herbies glug-glugs!
- [Menu]: Selecciona una opción
  - [Choice]: Sí, por favor, me llevarán de regreso.
    - (Condition: Si el player lleva ron Karamjan:)
      - **Bugs:** Dad dice que no traerás cosas divertidas... cosas malas hasta que nos metemos en grandes males.
    - (Condition: Si el player no tiene dos hierba de serpiente limpia o dos carteras de pícaro limpias:)
      - **Ogre boat:** No tienes herbies glug-glugs... ¡ni viajes en barco!
    - (Condition: Si el player tiene pago suficiente:)
      - (removes=two herbs)
      - Entregas dos hierbas y aceptas que Fycie y Bugs te lleven en el barco improvisado.
      - (Action: Player es transportado al este de Feldip Hills.)
      - El tronco apenas apto para navegar llega a Feldip Hills.
  - [Choice]: What are 'glug-glugs herbies'?|cond=Si no se seleccionó previamente la opción:
    - **Bugs:** ¡Glug-glugs herbies! ¡Sabes! ¡El herbie ladrón o el herbie serpiente!
    - **Player:** Espera, ¿te refieres al bolso del pícaro o a la hierba de serpiente?
    - ¡Sí! ¡Demín! Ahora papá dice que puedes regresar con el uso si quieres. ¡Pero primero nos das dos herbies!
    - (initial)
  - [Choice]: What herbies did you want again?|cond=Si previamente seleccionó la opción anterior:
    - (arriba)
  - [Choice]: No gracias.
    - **Player:** No, gracias.
