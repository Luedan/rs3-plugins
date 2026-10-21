# Challenge Mistress Fara

- **Original Wiki Page**: [Transcript:Challenge Mistress Fara](https://runescape.wiki/w/Transcript%3AChallenge%20Mistress%20Fara)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Burthorpe

(Uno de los siguientes saludos se reproduce al azar:)
- (Saludo 1 :)
  - **Challenge Mistress Fara:** ¿Tienes algo para mí, frijol?
  - (continue)
- (Saludo 2 :)
  - **Challenge Mistress Fara:** ¡Oye, estiramiento! ¿Tienes algo para mí?
  - (continue)
- (Saludo 3 :)
  - **Challenge Mistress Fara:** Oye, ¿cómo está el clima allí arriba?
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Challenge Mistress Fara:** El nombre es Fara, orgullosa gnoma y extraordinaria coleccionista.
    - **Challenge Mistress Fara:** Soy la Challenge Mistress encargada de asignar desafíos y repartir recompensas. Están todos aquí en mi lista...
    - (initial)
  - [Choice]: Cuéntame sobre los desafíos diarios.
    - **Challenge Mistress Fara:** Un desafío diario es un trabajo que hay que completar: cualquier cosa, desde forjar espadas hasta hornear patatas. Te asignamos tres desafíos por día.
    - Puedes ver todos los desafíos diarios en la pestaña Desafíos de la interfaz de Aventuras. Si has completado un desafío diario, también puedes reclamar tu recompensa desde allí, incluidos los cofres de recompensa semanales que hayas desbloqueado.
    - **Challenge Mistress Fara:** Para completar un desafío diario, no tienes que darme los artículos que recolectas o produce. Guárdelos para usted y úselos o véndalos.
    - Si completas un desafío de combate, obtendrás una lámpara de XP que se puede usar en cualquier habilidad de combate. Si completas cualquier otro desafío, obtendrás XP en esa habilidad directamente.
    - (Condition: Si el player se ha ganado un bebé troll:)
      - **Player:** Una cosa más. ¿Puedo reclamar a mi bebé troll?
      - **Challenge Mistress Fara:** Corporal Keymans cuida a tu bebé troll por ti. Está en el campo de entrenamiento de la guardia imperial al noreste de nosotros.
      - (continue)
    - (initial)
  - [Choice]: Quiero alternar mis desafíos diarios activos.
    - ((Se abre la interfaz de desafío al máximo.))
  - [Choice]: He completado un desafío diario.
    - (Condition: Sin ningún desafío para entregar:)
      - **Challenge Mistress Fara:** No parece que hayas completado ningún desafío diario. Vuelve cuando hayas completado uno.
      - (initial)
    - (Condition: Con desafíos para entregar:)
      - **Challenge Mistress Fara:** ¡Has completado ese! Bien hecho, aquí tienes tu recompensa. ''(Se repite si hay más de un desafío completado)
      - **Challenge Mistress Fara:** ¡Parece que eso es todo!
      - (initial)

#### Senderos del tesoro

- (removes=the old clue scroll (easy))
- ((Si el rastro continúa:))
  - (receives=a new clue scroll (easy))
  - [Challenge Mistress Fara te ha dado tu siguiente pergamino de pistas.]
  - (continue)
- ((Si el sendero termina:))
  - (receives=reward casket (easy))
  - [¡Has encontrado un ataúd!]
  - (continue)
- **Challenge Mistress Fara:** ¡Cosas increíbles!

### Turn in Challenges


#### Sin desafíos que entregar

- **Challenge Mistress Fara:** No parece que hayas completado ningún desafío diario. Vuelve cuando hayas completado uno.

#### Con desafíos para entregar

- (ver|Sistema de desafíos#Reclamación de recompensas)
- **Challenge Mistress Fara:** Ya lo has completado. ¡Bien hecho! Aquí está tu recompensa.
- **Challenge Mistress Fara:** ¡Parece que eso es todo!

### Toggle Challenges

- (Se abre una interfaz "Seleccionar habilidades de desafío" con el siguiente contenido:)
  - Selecciona tus habilidades máximas para alternar si recibirás o no desafíos diarios para ellas.
  - (Las habilidades se muestran como íconos con las habilidades desactivadas con una cruz roja sobre ellos).
  - (Se muestra una casilla de verificación con la etiqueta "Bloquear desafíos en todas las habilidades de combate").
    - [Choice]: CONFIRMAR
      - (end)

### Historical dialogue


#### Liga Catalizador y Liga Equilibrio

(Uno de los siguientes saludos se reproduce al azar:)
- (Saludo 1 :)
  - **Challenge Mistress Fara:** ¿Tienes algo para mí, frijol?
  - (continue)
- (Saludo 2 :)
  - **Challenge Mistress Fara:** ¡Oye, estiramiento! ¿Tienes algo para mí?
  - (continue)
- (Saludo 3 :)
  - **Challenge Mistress Fara:** Oye, ¿cómo está el clima allí arriba?
  - (continue)
- **Challenge Mistress Fara:** El nombre es Fara, orgullosa gnoma y extraordinaria coleccionista.
- **Challenge Mistress Fara:** Soy la Challenge Mistress encargada de asignar desafíos y repartir recompensas. Están todos aquí en mi lista...

##### Entregar o alternar desafíos

- Los desafíos están deshabilitados en los mundos de League.
- (ventana emergente)
  - (Ventana emergente: Los desafíos están deshabilitados en los mundos de League.|advertencia=yes)

#### Pase de héroe

(Uno de los siguientes saludos se reproduce al azar:)
- (Saludo 1 :)
  - **Misionera Fara:** ¿Tienes algo para mí, frijol?
  - (continue)
- (Saludo 2 :)
  - **Mission Mistress Fara:** ¡Oye, estiramiento! ¿Tienes algo para mí?
  - (continue)
- (Saludo 3 :)
  - **Mission Mistress Fara:** Oye, ¿cómo está el clima allí arriba?
  - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Mission Mistress Fara:** El nombre es Fara, orgullosa gnoma y extraordinaria coleccionista.
    - **Mission Mistress Fara:** Soy la Mission Mistress a cargo de crear y asignar misiones de Hero Pass.
    - (previous)
  - [Choice]: ¿Qué son las misiones de Hero Pass?
    - **Mission Mistress Fara:** Las misiones Hero Pass se asignan diaria y semanalmente. Ocasionalmente también podemos asignarle misiones adicionales.
    - **Mission Mistress Fara:** Cada misión tiene uno u objetivos diferentes que debes completar. Una vez completado, puede reclamar recompensas por sus esfuerzos.
    - **Mission Mistress Fara:** Aquí, echa un vistazo.
    - (opens=Hero Pass)
  - [Choice]: ¿Puedo ver mis misiones de Hero Pass?
    - (opens=Hero Pass)

#### Antes de 2019

''Uno de los siguientes saludos se reproduce al azar:
- *Saludo 1: *
  - **Challenge Mistress Fara:** ¿Tienes algo para mí, frijol?
  - (continue)
- *Saludo 2: *
  - **Challenge Mistress Fara:** ¡Oye, estiramiento! ¿Tienes algo para mí?
  - (continue)
- *Saludo 3:*
  - **Challenge Mistress Fara:** Oye, ¿cómo está el clima allí arriba?
  - (continue)
  - [Choice]: He completado un desafío.
    - (Condition: Sin ningún desafío para entregar:)
      - **Challenge Mistress Fara:** No parece que hayas completado ningún desafío diario. Vuelve cuando hayas completado uno.
      - (initial)
    - (Condition: Con desafíos para entregar:)
      - **Challenge Mistress Fara:** Veamos este: [Name of Challenge]
      - **Challenge Mistress Fara:** ¡Has completado ese! Bien hecho, aquí tienes tu recompensa.
      - **Challenge Mistress Fara:** ¡Parece que eso es todo!
  - [Choice]: ¿Quién eres?
    - **Challenge Mistress Fara:** El nombre es Fara, orgullosa gnoma y extraordinaria coleccionista.
    - **Challenge Mistress Fara:** Soy la maestra de desafíos a cargo de asignar desafíos y repartir recompensas. Están todos aquí en mi lista...
    - (initial)
  - [Choice]: Cuéntame sobre los desafíos.
    - **Challenge Mistress Fara:** Bueno, un desafío es un trabajo que hay que completar: cualquier cosa, desde forjar espadas hasta hornear patatas.
    - **Challenge Mistress Fara:** Esos son sólo para tu propio desarrollo. No tienes que entregar nada y no te daré ninguna recompensa. Son simplemente una buena manera de saber qué hacer a continuación.
    - Puedes ver todos los desafíos disponibles en la pestaña Desafíos de la interfaz de Aventuras.
    - **Challenge Mistress Fara:** Si estás interesado en las recompensas, que parece que sí, necesitarás un desafío diario.
    - (initial)
  - [Choice]: Cuéntame sobre los desafíos diarios.
    - **Challenge Mistress Fara:** Los desafíos diarios son bastante especiales. Solo te asigno uno por día, pero obtienes una gran recompensa cuando lo completas.
    - Puedes ver todos los desafíos diarios en la pestaña Desafíos de la interfaz de Aventuras.
    - **Challenge Mistress Fara:** Puedes tener hasta cinco desafíos diarios a la vez. Después de eso, los nuevos eliminan a los viejos de su lista.
    - **Challenge Mistress Fara:** Los diarios funcionan igual que los desafíos normales, ¡pero tendrás que darme todo lo que recolectes o produzcas al final para que pueda agregarlo a mi colección!
    - **Challenge Mistress Fara:** No te preocupes, te compensaré con una recompensa. Tengo todo tipo de cosas útiles aquí, así que haré todo lo posible para que sea un comercio justo que cubra sus costos.
    - **Challenge Mistress Fara:** También tengo un montón de lámparas viejas por ahí. ¡Ustedes, los tipos aventureros, parecen volverse locos por esas cosas viejas!
    - **Challenge Mistress Fara:** Te daré una de estas lámparas por cada desafío diario que completes.
    - Si completas un desafío de combate, obtendrás una lámpara de XP que se puede usar en cualquier habilidad de combate. Si completas cualquier otro desafío, obtendrás XP en esa habilidad directamente.
    - Cada día recibirás un nuevo Desafío Diario. {{color|#7E0700|Si ya tienes cinco desafíos diarios, ¡el más antiguo desaparecerá!}}
    - (initial)
  - [Choice]: Adiós.
    - (end)

#### Antes del 15 de noviembre de 2021

''Uno de los siguientes saludos se reproduce al azar:
- *Saludo 1: *
  - **Challenge Mistress Fara:** ¿Tienes algo para mí, frijol?
  - (continue)
- *Saludo 2: *
  - **Challenge Mistress Fara:** ¡Oye, estiramiento! ¿Tienes algo para mí?
  - (continue)
- *Saludo 3:*
  - **Challenge Mistress Fara:** Oye, ¿cómo está el clima allí arriba?
  - (continue)
- [Menu]: Elige una opción:
  - [Choice]: ¿Quién eres?
    - **Challenge Mistress Fara:** El nombre es Fara, orgullosa gnoma y extraordinaria coleccionista.
    - **Challenge Mistress Fara:** Soy la Challenge Mistress encargada de asignar desafíos y repartir recompensas. Están todos aquí en mi lista...
    - (initial)
  - [Choice]: Cuéntame sobre los desafíos diarios.
    - **Challenge Mistress Fara:** Un desafío diario es un trabajo que hay que completar: cualquier cosa, desde forjar espadas hasta hornear patatas. Solo te asigno uno por día, pero obtienes una gran recompensa cuando lo completas. Puedes tener hasta cinco desafíos diarios a la vez.
    - Puedes ver todos los desafíos diarios en la pestaña Desafíos de la interfaz de Aventuras. Si has completado un desafío diario, también puedes reclamar tu recompensa desde allí.
    - **Challenge Mistress Fara:** Para completar un desafío diario, no tienes que darme los artículos que recolectas o produce. Guárdelos para usted y úselos o véndalos.
    - Si completas un desafío de combate, obtendrás una lámpara de XP que se puede usar en cualquier habilidad de combate. Si completas cualquier otro desafío, obtendrás XP en esa habilidad directamente. **También recibirás una clave Treasure Hunter. (Esta oración se omite para los jugadores gratuitos)**
    - (Condition: Si el player se ha ganado un bebé troll:)
      - **Player:** Una cosa más. ¿Puedo reclamar a mi bebé troll?
      - **Challenge Mistress Fara:** Corporal Keymans cuida a tu bebé troll por ti. Está en el campo de entrenamiento de la guardia imperial al noreste de nosotros.
      - (continue)
    - (initial)
  - [Choice]: Quiero alternar mis desafíos diarios activos.
    - ((Se abre la interfaz de desafío al máximo.))
  - [Choice]: He completado un desafío diario.
    - (Condition: Sin ningún desafío para entregar:)
      - **Challenge Mistress Fara:** No parece que hayas completado ningún desafío diario. Vuelve cuando hayas completado uno.
      - (initial)
    - (Condition: Con desafíos para entregar:)
      - **Challenge Mistress Fara:** Veamos este: [Name of Challenge]
      - **Challenge Mistress Fara:** ¡Has completado ese! Bien hecho, aquí tienes tu recompensa. ''(Se repite si hay más de un desafío completado)
      - **Challenge Mistress Fara:** ¡Parece que eso es todo!
      - (initial)
