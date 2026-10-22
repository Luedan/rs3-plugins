# Challenge Mistress Heriau

- **Original Wiki Page**: [Transcript:Challenge Mistress Heriau](https://runescape.wiki/w/Transcript%3AChallenge%20Mistress%20Heriau)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Prifddinas, after Plague's End

- **Challenge Mistress Heriau:** ¿Puedo ayudarte en algo?
- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Challenge Mistress Heriau:** Soy Heriau del Clan Cadarn, un descendiente directo de Baxtorian, el rey de antaño.
    - **Challenge Mistress Heriau:** Soy la maestra de desafíos a cargo de asignar desafíos y repartir recompensas. Están todos aquí en mi lista...
    - (initial)
  - [Choice]: Cuéntame sobre los desafíos diarios.
    - **Challenge Mistress Heriau:** Un desafío diario es un trabajo que hay que completar: cualquier cosa, desde forjar espadas hasta hornear patatas. Te asignamos tres desafíos por día.
    - Puedes ver todos los desafíos diarios en la pestaña Desafíos de la interfaz de Aventuras. Si has completado un desafío diario, también puedes reclamar tu recompensa desde allí, incluidos los cofres de recompensa semanales que hayas desbloqueado.
    - **Challenge Mistress Heriau:** Para completar un desafío diario, no tienes que darme los artículos que recolectas o produce. ¡Guárdalos para ti y úsalos o véndelos!
    - Si completas un desafío de combate, obtendrás una lámpara de XP que se puede usar en cualquier habilidad de combate. Si completas cualquier otro desafío, obtendrás XP en esa habilidad directamente. También recibirás una clave Treasure Hunter.
    - (initial)
  - [Choice]: Quiero alternar mis desafíos diarios activos.
    - ((Maxed challenge interface opens.))
  - [Choice]: He completado un desafío diario.
    - (Condition: Without any challenges to turn in:)
      - **Challenge Mistress Heriau:** No parece que hayas completado ningún desafío diario. Vuelve cuando hayas completado uno.
      - (initial)
    - (Condition: With challenges to turn in:)
      - **Challenge Mistress Heriau:** Ya lo has completado. ¡Bien hecho! Aquí está tu recompensa. ''(Se repite si hay más de un desafío completado)
      - **Challenge Mistress Heriau:** ¡Parece que eso es todo!
      - (initial)

#### Entrando al gremio Max por primera vez

- ¡Al ingresar al gremio Max por primera vez, desbloqueas el teletransporte del gremio Max en tu libro de habilidades!
- (pop-up)
  - (Pop-up: Upon entering the Max Guild for the first time, you unlock the Max guild teleport in your ability book!)
  - (continue)
- **Challenge Mistress Heriau:** ¡Oye, bienvenido a la torre del gremio Max! Debe haberte costado mucho trabajo llegar hasta aquí.
- (Condition: Without one free backpack space:)
  - **Challenge Mistress Heriau:** Tengo un regalo de bienvenida para ti; Lo guardaré hasta que tengas espacio para aceptarlo.
- (Condition: With one free backpack space:)
  - (receives=crystal acorn)
  - **Challenge Mistress Heriau:** Por favor, llévate esto como regalo de bienvenida.
  - [¡Challenge Mistress Heriau te entrega una bellota de cristal!]

### Turn in Challenges


#### Sin desafíos que entregar

- **Challenge Mistress Heriau:** No parece que hayas completado ningún desafío diario. Vuelve cuando hayas completado uno.

#### Con desafíos para entregar

- (ver|Sistema de desafíos#Reclamación de recompensas)
- **Challenge Mistress Heriau:** Ya lo has completado. ¡Bien hecho! Aquí está tu recompensa.
- **Challenge Mistress Heriau:** ¡Parece que eso es todo!

### Toggle Challenges

- (Se abre una interfaz "Seleccionar habilidades de desafío" con el siguiente contenido:)
  - Selecciona tus habilidades máximas para alternar si recibirás o no desafíos diarios para ellas.
  - (Las habilidades se muestran como íconos con las habilidades desactivadas con una cruz roja sobre ellos).
  - (Se muestra una casilla de verificación con la etiqueta "Bloquear desafíos en todas las habilidades de combate").
    - [Choice]: CONFIRMAR
      - (end)

### Historical dialogue


#### Liga Catalizador

- **Challenge Mistress Heriau:** ¿Puedo ayudarte en algo?
- **Challenge Mistress Heriau:** Soy Heriau del Clan Cadarn, un descendiente directo de Baxtorian, el rey de antaño.
- **Challenge Mistress Heriau:** Soy la maestra de desafíos a cargo de asignar desafíos y repartir recompensas. Están todos aquí en mi lista...

##### Entregar o alternar desafíos

- Los desafíos están deshabilitados en los mundos de League.
- (pop-up)
  - (Pop-up: Challenges are disabled on League worlds.|warning=yes)

#### Pase de héroe

- **Mission Mistress Heriau:** ¿Puedo ayudarte con algo?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Mission Mistress Heriau:** Soy Heriau del Clan Cadarn, un descendiente directo de Baxtorian, el rey de antaño.
    - **Mission Mistress Heriau:** Soy la Mission Mistress a cargo de crear y asignar misiones de Hero Pass.
    - (previous)
  - [Choice]: ¿Qué son las misiones de Hero Pass?
    - **Mission Mistress Heriau:** Las misiones de Hero Pass se asignan diaria y semanalmente. Ocasionalmente también podemos asignarle misiones adicionales.
    - **Mission Mistress Heriau:** Cada misión tiene uno u objetivos diferentes que debes completar. Una vez completado, puede reclamar recompensas por sus esfuerzos.
    - **Mission Mistress Heriau:** Aquí, echa un vistazo.
    - (opens=Hero Pass)
  - [Choice]: ¿Puedo ver mis misiones de Hero Pass?
    - (opens=Hero Pass)

#### Antes del 15 de noviembre de 2021

- **Challenge Mistress Heriau:** ¿Puedo ayudarte en algo?
- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Challenge Mistress Heriau:** Soy Heriau del Clan Cadarn, un descendiente directo de Baxtorian, el rey de antaño.
    - **Challenge Mistress Heriau:** Soy la maestra de desafíos a cargo de asignar desafíos y repartir recompensas. Están todos aquí en mi lista...
    - (initial)
  - [Choice]: Cuéntame sobre los desafíos diarios.
    - **Challenge Mistress Heriau:** Un desafío diario es un trabajo que hay que completar: cualquier cosa, desde forjar espadas hasta hornear patatas. Solo te asigno uno por día, pero obtienes una gran recompensa cuando lo completas. Puedes tener hasta cinco desafíos diarios a la vez.
    - Puedes ver todos los desafíos diarios en la pestaña Desafíos de la interfaz de Aventuras. Si has completado un desafío diario, también puedes reclamar tu recompensa desde allí.
    - **Challenge Mistress Heriau:** Para completar un desafío diario, no tienes que darme los artículos que recolectas o produce. Guárdelos para usted y úselos o véndalos.
    - Si completas un desafío de combate, obtendrás una lámpara de XP que se puede usar en cualquier habilidad de combate. Si completas cualquier otro desafío, obtendrás XP en esa habilidad directamente. También recibirás una clave Treasure Hunter.
    - (initial)
  - [Choice]: Quiero alternar mis desafíos diarios activos.
    - ((Maxed challenge interface opens.))
  - [Choice]: He completado un desafío diario.
    - (Condition: Without any challenges to turn in:)
      - **Challenge Mistress Heriau:** No parece que hayas completado ningún desafío diario. Vuelve cuando hayas completado uno.
      - (initial)
    - (Condition: With challenges to turn in:)
      - **Challenge Mistress Heriau:** Veamos este: [Name of Challenge]
      - **Challenge Mistress Heriau:** ¡Has completado ese! Bien hecho, aquí tienes tu recompensa. ''(Se repite si hay más de un desafío completado)
      - **Challenge Mistress Heriau:** ¡Parece que eso es todo!
      - (initial)
