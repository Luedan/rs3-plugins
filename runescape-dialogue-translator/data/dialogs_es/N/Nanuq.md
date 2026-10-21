# Nanuq

- **Original Wiki Page**: [Transcript:Nanuq](https://runescape.wiki/w/Transcript%3ANanuq)
- **Letter**: `N`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Missing dialogue for having 81 Summoning but before All Fired Up}}

### Talk-to


#### Antes de que todos se enciendan


##### Sin 81 Summoning

- **Nanuq:** Grrrrrrrrrrr. Groooowlioowlioooo!

##### Con 81 Summoning

- {{transcript missing}}

#### Después de todo entusiasmado


##### Sin 81 Summoning

- **Nanuq:** Grrrrrrrrrrr. Groooowlioowlioooo!

##### Con 81 Summoning

- **Nanuq:** Grrroooorgh. <br>(Hola, Player. ¿Qué puedo hacer por ti hoy?)
- [Menu]: Selecciona una opción
  - [Choice]: ¿Podrías cuidar esta baliza por mí?
    - **Player:** ¿Podrías cuidar esta baliza por mí?
    - (Condition: Si la baliza está apagada:)
      - **Nanuq:** Grrrrrrrrrrr. Groooowlioowlioooo! <br> (Por supuesto. Una vez que la baliza esté encendida, solo ten 5 logs conmigo y yo me encargaré del fuego tanto tiempo como pueda).
    - (Condition: Si la baliza está muriendo:)
      - **Nanuq:** ¡Gruooowlioowlioooo! (Bueno, podría, pero ya que estás aquí, es mejor que lo hagas tú mismo).
    - (Condition: Si la baliza no muere:)
      - (Condition: Si Nanuq no tiene cinco logs:)
        - (Condition: Si el player no tiene al menos cinco logs del mismo tipo:)
          - Debes darle al bombero cinco troncos del mismo tipo para la baliza.
          - **Nanuq:** Grrrrrrrrrrr. Groooowlioowlioooo! <br> (Me temo que no tiene suficiente registro del tipo correcto para que yo lo use).
        - (Condition: Si el player tiene al menos cinco logs del mismo tipo:)
          - (Condition: Si el mensaje de confirmación está habilitado:)
            - **Nanuq:** Grrr-arrrrg?<br>(Necesitaré cinco logs para poder atender el fuego. ¿Está bien?)
            - [Menu]: ¿Quieres darle cinco logs al fuego?
              - [Choice]: Sí.
                - (removes=five logs)
                - **Player:** Aquí tienes cinco logs para ti.
                - **Nanuq:** ¡Gruooowlioowlioooo!  <br>(¡Gracias! Usaré estos cinco logs para mantener la baliza encendida mientras estás fuera).
              - [Choice]: No.
                - **Player:** Creo que conservaré mi logs por ahora.
                - **Nanuq:** Raaaargh-groooool. <br> (Bueno, ya sabes dónde estoy si cambias de opinión).
              - [Choice]: Sí. Por favor, no me pidas confirmación en el futuro.
                - (above|talk-give-logs)
          - (Condition: Si el mensaje de confirmación está deshabilitado:)
            - (above|talk-give-logs)
      - (Condition: Si Nanuq tiene cinco logs:)
        - **Nanuq:** ¡Gruooowlioowlioooo! <br>(Por supuesto que lo haré, no te preocupes. Usaré el logs que ya me dejaste.
  - [Choice]: ¿Puedes hablarme de otras balizas?
    - **Player:** ¿Puedes hablarme de otras balizas?
    - **Nanuq:** Grrrroooorrg-gah. <br>(Sin duda.)
    - (Se abre la interfaz del mapa de estado de baliza All Fired Up (minijuego))
  - [Choice]: cond=If the player has not given a macaw pouch:|¿Es posible obtener información sobre balizas que están más alejadas?
    - **Player:** ¿Es posible obtener información sobre balizas que están más alejadas?
    - **Nanuq:** Grrroooorrgh.<br> (Puedo informarte sobre las balizas en cualquier dirección, hasta la primera que sale inclusive).
    - **Nanuq:** Grrrummmbberggrah. <br>(Por supuesto, una guacamaya tiene ojos mucho más agudos que yo. Si pudiera trabajar con esa guacamaya que tienes allí, podríamos contarte sobre toda la red de balizas).
    - **Player:** ¿Una guacamaya?
    - **Nanuq:** Grrrummmbble. <br>(Sí. Las guacamayas tienen la capacidad de volar muy alto en el aire y ver cosas que están mucho más lejos.}
    - **Nanuq:** Grrr-bah.<br> {También son muy inteligentes y pueden ser entrenados para proporcionar la información exacta necesaria para una descripción completa de la red de balizas).
    - ((Si el player tiene una bolsa de guacamayo en su backpack:))
      - **Nanuq:** Grrroooorrgh.<br> (Ahora que lo pienso, el guacamayo que tienes en el paquete sería perfecto).
      - (continue|macaw)
  - [Choice]: ¿Cómo estás?
    - **Player:** ¿Cómo te va?
    - **Nanuq:** Grrrrrrrrrrr. Groooowliowlioooo!<br> (Oo, ¿eres el bocadillo que pedí? Debo decir que estoy impresionado por la velocidad de las entregas en estos días).
    - **Player:** ¡No soy un bocadillo! Puedes sacar ese pensamiento de tu cabeza.
    - **Nanuq:** Raaaargh, grrrrrrowl groooo.<br> (Mis más sinceras disculpas, error mío).
  - [Choice]: ¡Ya terminé de hablar contigo!
    - **Player:** ¡Ya terminé de hablar contigo!
    - **Nanuq:** Grrroooorrgh. <br>(Adiós, entonces.)

##### Intentando agregar logs a la baliza antes de reparar el cortavientos

- **Nanuq:** Grrrrrrrrrrr. Groooowlioowlioooo! <br> (No me molestaría. Esa baliza no permanecerá encendida hasta que se repare el cortavientos).
- **Nanuq:** Rawwrrr grrrrowl. <br> (He estado tratando de masticar las fibras con los dientes, pero por alguna razón, eso parece empeorar las cosas).
- **Player:** Mmm. ¿Te vendría bien un poco de ayuda con eso?
- **Nanuq:** Grrrrrrrrrrumph...grr. <br> (Quizás un enfoque más peatonal sería suficiente. Sospecho que alguien con pulgares oponibles podría arreglarlo con una aguja y varios trozos de fibra de yute).
- **Nanuq:** ¿Grrrah? <br> (No tendrías tiempo para un poco de bricolaje, ¿verdad?)
- **Player:** Veré qué puedo hacer.
- **Nanuq:** Grrroooorrgh. <br>(Muchas gracias.)

### Using a macaw pouch on Nanuq


#### Antes de darle a Nanuq una bolsa de guacamaya{{Anchor|macaw}}

- [Menu]: ¿Quieres darle al fuego tierno tu guacamayo?
  - [Choice]: Sí.
    - (removes=a macaw pouch)
    - **Nanuq:** Raaaargh, genial grrrrrrrowl. <br> (Muchas gracias. Esto me ayudará a brindarle información más detallada sobre la red contra incendios).
  - [Choice]: No.
    - **Player:** Creo que me quedaré con mi guacamaya por ahora.
    - **Nanuq:** Raaaargh-groooool. <br> (Haz lo que quieras.)

#### Después de darle a Nanuq una bolsa de guacamaya

- **Player:** Ya le regalé una guacamaya; él no necesita otro.

### Using logs on Nanuq

- (Condition: Si la baliza está apagada:)
  - Aquí no hay fuego para que lo atienda el bombero.
- (Condition: Si la baliza está muriendo:)
  - **Player:** Ya que estoy aquí y el fuego de la baliza se está apagando, también podría cuidarlo yo mismo.
- (Condition: Si la baliza no muere:)
  - (Condition: Si Nanuq no tiene cinco logs:)
    - (Condition: Si el mensaje de confirmación está habilitado:)
      - [Menu]: ¿Quieres darle cinco logs al fuego?
        - [Choice]: Sí.
          - (Condition: Si el player no tiene al menos cinco logs del mismo tipo:)
            - El bombero necesita cinco troncos del mismo tipo para mantener este fuego.
          - (Condition: Si el player tiene al menos cinco logs del mismo tipo:)
            - (removes=five logs)
            - Le das al fuego tierno 5 [type] logs.
        - [Choice]: No.
          - **Player:** Creo que, después de todo, me quedaré con mi logs.
        - [Choice]: Sí. Por favor, no vuelvas a pedirme confirmación.
          - (above|use-give-logs)
    - (Condition: Si el mensaje de confirmación está deshabilitado:)
      - (above|use-give-logs)
  - (Condition: Si Nanuq tiene cinco logs:)
    - Ya saliste de logs con este ténder de fuego.

### Attempting to open the log storage chest without the elite Varrock tasks completed


#### Independientemente del nivel de Summoning

- **Nanuq:** ¡Oye! ¡Aléjate de eso! Hasta que no hayas demostrado que eres un verdadero aliado de Varrock, ¡no podrás usar eso!
- Debes reclamar la recompensa por las tareas del conjunto de élite en Varrock para usar este cofre.
