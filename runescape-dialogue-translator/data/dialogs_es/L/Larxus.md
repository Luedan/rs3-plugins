# Larxus

- **Original Wiki Page**: [Transcript:Larxus](https://runescape.wiki/w/Transcript%3ALarxus)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk-to


#### Antes de derrotar al Campeón Leprechaun

- (Condition: If the player has unclaimed reward lamps from a previous fight:)
  - (Condition: If the player does not have at least two free backpack spaces:)
    - **Larxus:** Tengo algunas lámparas para ti, pero en este momento tienes un inventario completo.
    - (continue)
  - (Condition: If the player has at least two free backpack spaces:)
    - **Larxus:** ¡Ah, ja! ¡Tengo algunas lámparas para ti!
    - (receives=constitution and slayer XP lamps)
    - (continue)
- (Condition: If the player has not defeated any champions:)
  - **Larxus:** ¡Bienvenido a la Arena de Campeones! Si alguna vez encuentras el pergamino de un campeón durante tus aventuras, aquí es donde tendrá lugar el duelo.
  - **Larxus:** Si quieres experimentar lo que es luchar contra un campeón, tengo un desafío informal que te presentó el Campeón Leprechaun.
  - **Larxus:** Las reglas de esta pelea son: No se permiten artículos. ¿Quieres aceptar el desafío?
  - [Menu]: Selecciona una opción
    - [Choice]: ¡Sí, déjame con él!
      - (Condition: If the player has any items equipped or in their backpack:)
        - **Larxus:** Creo que mencioné que no puedes llevar ningún objeto contigo para esta pelea.
      - (Condition: If the player does not have any items equipped or in their backpack:)
        - (Condition: If the player has a follower:)
          - **Larxus:** Lo siento, pero no voy a dejar que te enfrentes al Campeón Leprechaun con ese seguidor.
          - **Larxus:** ¡Este es un desafío entre tú y el campeón, no una pelea entre múltiples jugadores en la que todos están permitidos!
        - (Condition: If the player does not have a follower:)
          - **Larxus:** Debido a la naturaleza informal de este desafío, se llevará a cabo en la sala de capacitación. Tu retador te está esperando allí. Baja por la trampilla cuando estés listo.
    - [Choice]: No gracias, paso.
      - **Player:** No, gracias, paso.
      - (continue|main-dialogue)
- (Condition: If the player has defeated at least one champion:)
  - **Larxus:** El Campeón Leprechaun ha lanzado un desafío informal. Ha declarado que no se permitirán artículos para esta pelea. ¿Quieres aceptar el desafío?
  - (continuea|Leprechaun-Champion-challenge)

#### Después de derrotar al Campeón Leprechaun

- (Condition: If the player has unclaimed reward lamps from a previous fight:)
  - (Condition: If the player does not have at least two free backpack spaces:)
    - **Larxus:** Tengo algunas lámparas para ti, pero en este momento tienes un inventario completo.
    - (continue)
  - (Condition: If the player has at least two free backpack spaces:)
    - **Larxus:** ¡Ah, ja! ¡Tengo algunas lámparas para ti!
    - (receives=constitution and slayer XP lamps)
    - (continue)
- (Condition: If the player has been challenged by Leon d'Cour and has not defeated him:)
  - **Larxus:** Leon D'Cour{{Sic}} te ha lanzado un desafío. Ha declarado que no se permitirán artículos excepto los que estés usando. ¿Quieres aceptar el desafío?
  - [Menu]: Selecciona una opción
    - [Choice]: ¡Sí, déjame con él!
      - **Larxus:** Tu retador está listo. Baja por la trampilla cuando estés listo.
    - [Choice]: No gracias, paso.
      - **Player:** No, gracias, paso.
      - (continue|main-dialogue)
- (Condition: If the player has been challenged by Glophren and has not defeated him:)
  - **Larxus:** Glophren te ha lanzado un desafío. Ha declarado que sólo se permite Magic y que no puedes usar ningún escudo. ¿Quieres aceptar el desafío?
  - (continuea|champion-of-champions-challenge)
- (Condition: If the player has not claimed the calling beads after defeating any champion with a champion's scroll:)
  - **Larxus:** Los campeones desean felicitarte por tus logros en este campo.
  - (Condition: If the player does not have at least one free backpack space:)
    - **Larxus:** Lamentablemente, parece que no tienes espacio en el inventario para recibir la recompensa que tienen para ti. Lo guardaré aquí hasta que tengas espacio para él.
    - (continue)
  - (Condition: If the player has at least one free backpack space:)
    - **Larxus:** Les gustaría que tuvieras estas cuentas de llamada. Cuando se use, le llamarán a un portador de pancartas y mostrará sus logros en este campo.
    - **Larxus:** El banner mostrará el número total de pergaminos de campeones y Campeón de Campeones que has derrotado, o mostrará con orgullo una imagen de su raza individual.
    - **Larxus:** El portador del banner estará encantado de cambiar el banner cuando lo solicite.
    - (receives=calling beads)
    - [pic=Llamando cuentas detail.png]
    - (continue)
- (Condition: If the player has unclaimed rewards from defeating Glophren for the first time:)
  - (Condition: If the player has not claimed all four scrolls of knowledge:)
    - (receives=zero to four scrolls of knowledge)
    - (Condition: If the player does not have enough free backpack spaces for all unclaimed scrolls of knowledge:)
      - **Larxus:** Estas son algunas de las recompensas que obtuviste por derrotar al Gnome Champions{{Sic}} de campeones, Glophren. Te daré el resto cuando tengas algo de espacio libre en tu inventario para ello.
      - (continue)
    - (Condition: If the player has enough free backpack spaces for all unclaimed scrolls of knowledge:)
      - **Larxus:** Saludos. Aquí están las recompensas que obtuviste por derrotar al Gnome Champions{{Sic}} de campeones, Glophren.
      - (continue)
  - (Condition: If the player has not claimed the 50,000 coins:)
    - (receives=50,000 coins)
    - **Larxus:** Aquí también hay una recompensa en efectivo de 50 000 coins por derrotar al Gnome Champions{{Sic}} de campeones, Glophren.
    - (continue)
  - (Condition: If the player has already claimed all four scrolls of knowledge, does not have at least one free backpack space, and has all unused scrolls of knowledge in their backpack:)
    - **Larxus:** Saludos. Tengo algunas recompensas para ti por derrotar al Gnome Champions{{Sic}} de campeones, Glophren. Sin embargo, necesitará algo de espacio en su inventario.
    - (continue)
  - (continue|Is there something I can help you with?)
- **Larxus:** ¿Hay algo en lo que pueda ayudarte?
- [Menu]: Elige una opción:
  - [Choice]: ¡Deseo pelear contra los campeones!
    - (Condition: If the player has unclaimed reward lamps from a previous fight:)
      - (Condition: If the player does not have at least two free backpack spaces:)
        - **Larxus:** Lo siento, pero tienes un inventario completo y debes aceptar estas lámparas de recompensa antes de que pueda organizar otra pelea.
      - (Condition: If the player has at least two free backpack spaces:)
        - **Larxus:** Lo siento, debes aceptar estas lámparas de recompensa antes de que pueda emitir otra pelea.
        - (receives=constitution and slayer XP lamps)
    - (Condition: If the player does not have unclaimed reward lamps from a previous fight:)
      - ((Pick a champion interface opens.))
        - (Condition: If the player has already chosen a champion to fight:)
          - **Larxus:** Ya tienes un campeón esperándote.
        - (Condition: If the player chose the Leprechaun Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea no se te permiten artículos. ¿Aún quieres continuar?
        - (Condition: If the player chose the Imp Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea no puedes usar ningún ataque especial. ¿Aún quieres continuar?
        - (Condition: If the player chose the Goblin Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea solo puedes usar ataques Magic, no Melee o Ranged. ¿Aún quieres continuar?
        - (Condition: If the player chose the Skeleton Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea solo puedes usar ataques Ranged, no Melee o Magic. ¿Aún quieres continuar?
        - (Condition: If the player chose the Zombie Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea no puedes usar ningún ataque Magic. ¿Aún quieres continuar?
        - (Condition: If the player chose the Hobgoblin Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea no puedes usar ningún ataque cuerpo a cuerpo. ¿Aún quieres continuar?
        - (Condition: If the player chose the Giant Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea solo puedes usar ataques cuerpo a cuerpo, no Ranged o Magic. ¿Aún quieres continuar?
        - (Condition: If the player chose the Banshee Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea no puedes usar oraciones ni ataques cuerpo a cuerpo. ¿Aún quieres continuar?
        - (Condition: If the player chose the Ghoul Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea sólo puedes llevar armas y runas, no se permiten otros objetos. ¿Aún quieres continuar?
        - (Condition: If the player chose the Earth Warrior Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea no puedes usar ninguna oración. ¿Aún quieres continuar?
        - (Condition: If the player chose the Aberrant Spectre Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea deberás utilizar un arma de 2 manos. ¿Aún quieres continuar?
        - (Condition: If the player chose the Human Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea no se te permiten artículos {{Sic}} excepto los que llevas puestos. ¿Aún quieres continuar?
        - (Condition: If the player chose the Jogre Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea no puedes usar ningún ataque Ranged. ¿Aún quieres continuar?
        - (Condition: If the player chose the Mummy Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea no puedes usar nada que esté usado en tu ranura de mano secundaria. ¿Aún quieres continuar?
        - (Condition: If the player chose the Lesser Demon Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea no puedes traer armas ni armaduras. ¿Aún quieres continuar?
        - (Condition: If the player chose the Gnome Champion:)
          - **Larxus:** Entonces quieres aceptar el desafío, ¿eh? Bueno, existen algunas reglas específicas para estas peleas de campeones. Para esta pelea solo puedes usar ataques Magic y no puedes usar ningún escudo. ¿Aún quieres continuar?
      - [Menu]: Selecciona una opción
        - [Choice]: ¡Sí, déjame con él!
          - **Player:** ¡Sí, déjame hablar con él!
          - (Condition: If the player has a follower:)
            - **Larxus:** Lo siento, pero no voy a decepcionarte con ese seguidor.
            - **Larxus:** ¡Este es un desafío entre tú y el campeón, no una pelea entre múltiples jugadores en la que todos están permitidos!
            - (Condition: If the player has calling beads:)
              - **Larxus:** Eso también incluye este artículo: Cuentas de llamada.
          - (Condition: If the player does not have a follower:)
            - **Larxus:** Tu retador está listo. Baja por la trampilla cuando estés listo.
        - [Choice]: No gracias, paso.
          - **Player:** No, gracias, paso.
  - [Choice]: cond=If the player has a champion's scroll from a champion not yet defeated:|Me dieron un desafío. ¿Y ahora qué?
    - **Player:** Me dieron un desafío. ¿Y ahora qué?
    - **Larxus:** Bueno, pásalo aquí y te ayudaremos a empezar.
  - [Choice]: cond=If the player has defeated all the champions:|He derrotado a todos los campeones. ¿Y ahora qué?
    - **Player:** He derrotado a todos los campeones. ¿Y ahora qué?
    - **Larxus:** Puedes volver la semana que viene y luchar contra los campeones nuevamente, darles tiempo para curar sus heridas y su orgullo.
    - **Larxus:** Además, mantente atento. Es posible que surjan más campeones para poner a prueba tu temple en el futuro.
  - [Choice]: cond=If the player lost the calling beads:|He perdido mis cuentas de vocación.
    - **Player:** He perdido mis cuentas de llamada.
    - (Condition: If the player does not have at least one free backpack space:)
      - **Larxus:** Está bien. Te daré algunos más cuando tengas espacio en tu inventario para ellos.
    - (Condition: If the player has at least one free backpack space:)
      - **Larxus:** Está bien. Tómelos como reemplazos.
      - (receives=calling beads)
      - [pic=Llamando cuentas detail.png]
      - **Player:** Gracias.
  - [Choice]: ¿Qué es este lugar?
    - **Player:** ¿Qué es este lugar?
    - **Larxus:** Esta es la Arena de Campeones. Los campeones de varias razas lo utilizan para batirse en duelo con aquellos que consideran dignos de ese honor. ¿Algo más?
    - [Menu]: Elige una opción:
      - [Choice]: cond=If the player has a champion's scroll from a champion not yet defeated:|Me dieron un desafío. ¿Y ahora qué?
        - (above|I was given a challenge. What now?)
      - [Choice]: cond=If the player has defeated all the champions:|He derrotado a todos los campeones. ¿Y ahora qué?
        - (above|I've defeated all the champions. What now?)
      - [Choice]: Nada, gracias.
        - (below|Nothing, thanks.)
  - [Choice]: Nada, gracias.
    - **Player:** Nada, gracias.

### Fight


#### Antes de derrotar al Campeón Leprechaun

- (Condition: If the player has not defeated any champions:)
  - **Larxus:** ¡Bienvenido a la Arena de Campeones! Si alguna vez encuentras el pergamino de un campeón durante tus aventuras, aquí es donde tendrá lugar el duelo.
  - **Larxus:** Si quieres experimentar lo que es luchar contra un campeón, tengo un desafío informal que te presentó el Campeón Leprechaun.
  - **Larxus:** Las reglas de esta pelea son: No se permiten artículos. ¿Quieres aceptar el desafío?
  - [Menu]: Selecciona una opción
    - [Choice]: ¡Sí, déjame con él!
      - (Condition: If the player has any items equipped or in their backpack:)
        - **Larxus:** Creo que mencioné que no puedes llevar ningún objeto contigo para esta pelea.
      - (Condition: If the player does not have any items equipped or in their backpack:)
        - (Condition: If the player has a follower:)
          - **Larxus:** Lo siento, pero no voy a dejar que te enfrentes al Campeón Leprechaun con ese seguidor.
          - **Larxus:** ¡Este es un desafío entre tú y el campeón, no una pelea entre múltiples jugadores en la que todos están permitidos!
        - (Condition: If the player does not have a follower:)
          - **Larxus:** Debido a la naturaleza informal de este desafío, se llevará a cabo en la sala de capacitación. Tu retador te está esperando allí. Baja por la trampilla cuando estés listo.
    - [Choice]: No gracias, paso.
      - **Player:** No, gracias, paso.
      - (continuea|I wish to fight the champions!)
- (Condition: If the player has defeated at least one champion:)
  - **Larxus:** El Campeón Leprechaun ha lanzado un desafío informal. Ha declarado que no se permitirán artículos para esta pelea. ¿Quieres aceptar el desafío?
  - (continuea|Leprechaun-Champion-challenge-2)

#### Después de derrotar al Campeón Leprechaun

- (above|I wish to fight the champions!)

### Using a champion's scroll on Larxus

- (removes=the champion's scroll)
- (Condition: If the champion is not unlocked:)
  - **Larxus:** Ahora puedes desafiar a este campeón.
- (Condition: If the champion is already unlocked:)
  - **Larxus:** Ya has desbloqueado este campeón. El desafío es nulo.

### After defeating any champion

- (Condition: If the player does not have at least two free backpack spaces:)
  - Tienes lámparas no reclamadas de Larxus el mayordomo.
- (Condition: If the player has at least two free backpack spaces:)
  - (receives=constitution and slayer XP lamps)
  - Sientes que han entrado lámparas en tu bolso.

### After defeating any champion with 10+ unique champions defeated before defeating Leon d'Cour

- **Leon d'Cour:** Lo has hecho bien, valiente aventurero, pero ahora pondría a prueba tu temple. Puedes organizar la pelea con Larxus cuando quieras.

### After defeating any champion with 13+ unique champions defeated (including Leon d'Cour) before defeating Glophren

- **Glophren:** Tus habilidades son admirables, humano. Me gustaría poner a prueba tu temple ahora. Puedes organizar la pelea con Larxus cuando quieras.

### After defeating any champion with a champion's scroll before claiming the calling beads

- **Larxus:** ¡Felicitaciones! Los campeones y yo tenemos una recompensa para ti. Ven y habla conmigo para recogerlo.

### After defeating Glophren before collecting the rewards

- **Larxus:** También tengo algunas recompensas adicionales por tu victoria sobre el campeón Gnome. Ven y habla conmigo para recogerlos.

### Attempting to open the trapdoor


#### Antes de derrotar a todos los campeones.

- La trampilla está cerrada desde el interior. Puedes escuchar los sonidos ahogados de los golpes.
- **Larxus:** Esa es la sala de entrenamiento de los campeones. No puedo dejarte allí mientras entrenan.

#### Después de derrotar a todos los campeones.

- La trampilla está cerrada. Al otro lado todo está en silencio.
- **Larxus:** Esa era la sala de entrenamiento de los campeones, hasta que los derrotabas a todos.

### Attempting to open the champion statue

- **Larxus:** Debes organizar un desafío conmigo antes de ingresar a la arena.

### Attempting to climb-down the champion statue with a follower

- **Larxus:** Lo siento, pero no voy a decepcionarte con ese seguidor.
- **Larxus:** ¡Este es un desafío entre tú y el campeón, no una pelea entre múltiples jugadores en la que todos están permitidos!
- (Condition: If the player has calling beads:)
  - **Larxus:** Eso también incluye este artículo: Cuentas de llamada.

### Attempting to climb-down the champion statue with prohibited items


#### Campeón duende

- **Larxus:** Creo que mencioné que no puedes llevar ningún arma o armadura a este duelo.{{Sic}}

#### Campeón Demonio Menor

- **Larxus:** Creo que mencioné que no puedes llevar armas ni armaduras a este duelo.

#### Campeón necrófago

- **Larxus:** Creo que mencioné que solo puedes llevar armas o runas a este duelo.

#### Campeona de momias

- **Larxus:** Creo que mencioné que no puedes tener ningún objeto usado en tu ranura de mano izquierda en este duelo.

#### Campeón del espectro aberrante

- **Larxus:** Creo que mencioné que debes usar un arma de 2 manos en este duelo.

#### Leon de Cour

- **Larxus:** Creo que mencioné que no puedes llevar ningún objeto a este duelo, excepto los que llevas puesto.

#### Glophren

- **Larxus:** Creo que mencioné que no puedes aceptar ningún escudo.

### Attempting to use special attacks (including Ancient Magicks) during the fight with the Imp Champion

- **Larxus:** Creo que mencioné que no puedes usar ataques o habilidades especiales en este duelo.
- No puedes usar ataques o habilidades especiales en este duelo.
- ((Repeated in a pop-up:))
  - No puedes usar ataques o habilidades especiales en este duelo.

### Attempting to use melee or magic attacks during the fight with the Skeleton Champion

- **Larxus:** Creo que mencioné que solo puedes usar Ranged en este duelo.
- Sólo puedes usar Ranged en este duelo.
- ((Repeated in a pop-up:))
  - Sólo puedes usar Ranged en este duelo.

### Attempting to use melee or ranged attacks during the fight with the Goblin Champion and Glophren

- **Larxus:** Creo que mencioné que solo puedes usar Magic en este duelo.
- Sólo puedes usar Magic en este duelo.
- ((Repeated in a pop-up:))
  - Sólo puedes usar Magic en este duelo.

### Attempting to use melee attacks during the fight with the Hobgoblin and Banshee Champions

- **Larxus:** Creo que mencioné que no puedes usar el combate cuerpo a cuerpo en este duelo.
- No puedes utilizar el combate cuerpo a cuerpo en este duelo.
- ((Repeated in a pop-up:))
  - No puedes utilizar el combate cuerpo a cuerpo en este duelo.

### Attempting to use magic or ranged attacks during the fight with the Giant Champion

- **Larxus:** Creo que mencioné que solo puedes usar el combate cuerpo a cuerpo en este duelo.
- ¡Solo puedes usar combate cuerpo a cuerpo en este duelo!
- ((Repeated in a pop-up:))
  - ¡Solo puedes usar combate cuerpo a cuerpo en este duelo!

### Attempting to use magic attacks during the fight with the Zombie Champion

- **Larxus:** Creo que mencioné que no puedes usar Magic en este duelo.
- No puedes usar Magic en este duelo.
- ((Repeated in a pop-up:))
  - No puedes usar Magic en este duelo.

### Attempting to use ranged attacks during the fight with the Jogre Champion

- **Larxus:** Creo que mencioné que no puedes usar Ranged en este duelo.
- No puedes usar Ranged en este duelo.
- ((Repeated in a pop-up:))
  - No puedes usar Ranged en este duelo.

### Attempting to activate prayers or curses during the fight with the Earth Warrior and Banshee Champions

- **Larxus:** Creo que mencioné que no puedes usar Prayer en este duelo. ¡Eso también se aplica a las maldiciones!
- ¡No puedes usar [prayers/curses] en este duelo!

### Attempting to equip an item in the off-hand slot during the fight with the Mummy Champion

- Se supone que no debes tener nada que puedas usar en la ranura de tu escudo.
- ((Repeated in a pop-up:))
  - Se supone que no debes tener nada que puedas usar en la ranura de tu escudo.

### Attempting to equip a 1-handed weapon during the fight with the Aberrant Spectre Champion

- Sólo puedes usar un arma de 2 manos.
- ((Repeated in a pop-up:))
  - Sólo puedes usar un arma de 2 manos.

### Fighting Glophren

- (Condition: If the player is praying:)
  - ¡Glophren te arroja algo a los pies! Pierdes la concentración y dejas de orar.

### Attempting to teleport out of the Champions' Arena

- **Larxus:** Hay una escalera por una razón.
