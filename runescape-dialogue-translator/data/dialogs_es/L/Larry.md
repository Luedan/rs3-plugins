# Larry

- **Original Wiki Page**: [Transcript:Larry](https://runescape.wiki/w/Transcript%3ALarry)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Ardougne Zoo


#### Antes de hablar con Larry sobre Penguin Hide and Seek

- [Menu]: Quiero hablar con Larry sobre:
  - [Choice]: Frío War
    - (Condition: Without level 10 Hunter:)
      - [Debes tener el nivel 10 Hunter para comenzar esta misión.]
    - (Condition: With level 10 Hunter:)
      - [Debes tener el nivel 30 Agility para comenzar esta misión.]
      - **Larry:** Estoy buscando un aventurero experimentado y tú no lo eres. Vuelve cuando seas más capaz.
    - (Condition: With level 30 Agility:)
      - [Debes tener el nivel 34 Construction para comenzar esta misión.]
      - **Larry:** Estoy buscando un aventurero experimentado y tú no lo eres. Vuelve cuando seas más capaz.
  - [Choice]: El escondite del pingüino
    - **Larry:** ¿Qué quieres?
    - **Player:** Uh, solo quería preguntar-
    - **Larry:** ¡SHHHHHHH! Están escuchando. Mantén la voz baja.
    - **Player:** *susurra* ¿Quién escucha?
    - **Larry:** No importa.
    - **Larry:** ¿Eres del tipo curioso? ¿Estás dispuesto a hacer una expedición por mí?
    - **Player:** ¿Qué tendría que hacer en esta expedición?
    - **Larry:** El zoológico me ha concedido permiso para estudiar pingüinos en el extranjero. Según tengo entendido, hay muchos pingüinos repartidos por todo el mundo.
    - **Player:** ¿Por qué quieres encontrar pingüinos en todo el mundo?
    - **Larry:** Necesito ver si están organis-, quiero decir, si están migrando o algo así.
    - **Player:** ¿Crees que están organizados? ¡Son sólo pingüinos!
    - **Larry:** ¡No los subestimes! ¡Son inteligentes, astutos y ESCUCHAN! Sé que están tramando algo.
    - **Larry:** Por eso estoy reclutando valientes aventureros para que encuentren a estos pingüinos y me cuenten su ubicación.
    - **Player:** Bueno, no creo que estén organizados, pero sí viajo por todo el mundo. Podría ayudarte a encontrarlos. ¿Qué necesito hacer?
    - **Larry:** Siempre que veas un pingüino, espíalo. Están bien entrenados y cambiarán de posición cada semana, así que mantén los ojos bien abiertos.
    - **Larry:** Te daré un dispositivo que puede rastrear a los pingüinos espías y ofrecerte pistas sobre sus ubicaciones. Los pingüinos valen entre 1 y 3 Penguin Points dependiendo de lo difíciles que sean de encontrar.
    - **Larry:** Infórmate aquí y te recompensaré por tus esfuerzos.
    - **Player:** Genial, comenzaré de inmediato.
    - (Condition: Without space in backpack:)
      - **Larry:** Necesito darte un dispositivo pero no tienes espacio. Ven y habla conmigo una vez que hayas hecho espacio, o puedes reclamar uno en la tienda.
    - (Condition: With space in backpack:)
      - **Larry:** Espera, ahí. Toma este dispositivo.
      - (receives=penguin spy device)
      - [Larry te entrega un dispositivo espía para pingüinos.]
      - **Larry:** Deberías llevar este dispositivo para espiar a los pingüinos. Debería resultarte útil ya que tiene una serie de funciones útiles que te ayudarán en tu misión.
      - **Larry:** Primero, proporcionará pistas sobre todas las ubicaciones de los pingüinos. No puede localizarlo con exactitud, pero debería brindarle el área general para comenzar su búsqueda.
      - **Larry:** Una vez que estés en el área, puedes iniciar un escaneo que buscará en tus inmediaciones e identificará los pingüinos cercanos.
      - **Larry:** A medida que veas más pingüinos, te ofreceré una actualización del rango de escaneo y una nueva función de descarga que congelará a los pingüinos en su lugar.

#### Después de hablar con Larry sobre Penguin Hide and Seek

- [Menu]: Quiero hablar con Larry sobre:
  - [Choice]: Frío War
    - (arriba)
  - [Choice]: El escondite del pingüino
    - **Larry:** ¿Tienes noticias? ¿Has encontrado más?
    - (Condition: If the player is receiving the penguin spy device for the first time:)
      - **Larry:** Deberías llevar este dispositivo para espiar a los pingüinos. Debería resultarte útil ya que tiene una serie de funciones útiles que te ayudarán en tu misión.
      - **Larry:** Primero, proporcionará pistas sobre todas las ubicaciones de los pingüinos. No puede localizarlo con exactitud, pero debería brindarle el área general para comenzar su búsqueda.
      - **Larry:** Una vez que estés en el área, puedes iniciar un escaneo que buscará en tus inmediaciones e identificará los pingüinos cercanos.
      - **Larry:** A medida que veas más pingüinos, te ofreceré una actualización del rango de escaneo y una nueva función de descarga que congelará a los pingüinos en su lugar.
      - (Condition: Without space in backpack:)
        - **Larry:** Parece que tu backpack está lleno. No te preocupes, guardaré esto por ti. Después de todo, ¡nunca se sabe de dónde podría venir el próximo pingüino!
        - (continue|standard)
      - (Condition: With space in backpack:)
        - (receives=penguin spy device)
        - [Larry te entrega un dispositivo espía para pingüinos.]
        - (continue|standard)
    - (Condition: If the player has lost the penguin spy device:)
      - **Larry:** ¡Espera! ¿Dónde está tu dispositivo espía? ¿Cayó en manos enemigas?
      - **Player:** Sólo me di vuelta por un segundo...
      - **Larry:** Tienes suerte de que sean tan fáciles de hacer. Sólo un poco de papel de aluminio y listo.
      - (Condition: Without space in backpack:)
        - **Larry:** Parece que tu backpack está lleno. No te preocupes, guardaré esto por ti. Después de todo, ¡nunca se sabe de dónde podría venir el próximo pingüino!
        - (continue|standard)
      - (Condition: With space in backpack:)
        - (receives=penguin spy device)
        - [Larry te entrega un dispositivo espía para pingüinos.]
        - (continue|standard)
    - [Menu]: Selecciona una opción
      - [Choice]: He encontrado más pingüinos.
        - **Player:** He encontrado más pingüinos.
        - **Larry:** ¿Más? Se están propagando muy rápido.
        - (Condition: First time after spying on a penguin:)
          - **Player:** ¡Eso no es todo! ¡Descubrí que hay pingüinos agentes secretos que también han comenzado a aparecer en Gielinor!
          - **Larry:** ¡Galletas de gambas! ¿Seguramente no? Escuché los susurros pero nunca creí que ya hubieran llegado a esta etapa.
          - **Player:** ¿Qué debemos hacer al respecto?
          - **Larry:** Sigamos rastreándolos por ahora. Al final tendrán que cometer un error.
          - **Player:** Por el hielo, ¿verdad?
          - **Larry:** ¡Esto no es motivo de risa, Player! ¡Presta atención o quién sabe qué te puede pasar!
          - **Player:** Lo siento. Enfoque total a partir de ahora.
          - (continue)
        - **Player:** Encontré [número] pingüino[s] esta semana.
        - (Condition: With points to spend:)
          - **Larry:** ¡Genial! Tienes puntos [número] para gastar. Quizás deberías pensar en reclamar tu recompensa.
          - (continue)
        - (Condition: Without points to spend:)
          - **Larry:** Has encontrado muchos espías. Pero no tienes puntos de pingüino ahorrados. ¡Sigue buscando!
          - (continue)
        - [Menu]: Selecciona una opción
          - [Choice]: Tengo problemas para encontrar los pingüinos, ¿puedo darme una pista?
            - (below|hint)
          - [Choice]: ¿Qué necesito hacer de nuevo?
            - (below|explain-again)
          - [Choice]: No importa.
            - (below|nevermind)
      - [Choice]: Tengo problemas para encontrar a los pingüinos; ¿Puedo tener una pista? {{anchor|hint}}
        - **Player:** Tengo problemas para encontrar a los pingüinos; ¿Puedo tener una pista?
        - ((One of the following is shown, depending on the location of the penguins:))
          - **Larry:** He oído que hay un pingüino ubicado alrededor de un pueblo entre una gran torre y la mansión de vampyre.
          - **Larry:** He oído que hay un pingüino ubicado alrededor de Ardougne.
          - **Larry:** He oído que hay un pingüino ubicado alrededor de Feldip Hills, cerca de Gu'Tanoth.
          - **Larry:** He oído que hay un pingüino ubicado alrededor de la región Al Kharid, al norte del paso Shantay.
          - **Larry:** He oído que hay un pingüino ubicado alrededor de la región de Ice Mountain.
          - **Larry:** He oído que hay un pingüino ubicado entre los Fremenniks y los Bárbaros.
          - **Larry:** He oído que hay un pingüino ubicado en lo profundo de la jungla.
          - **Larry:** He oído que hay un pingüino ubicado al este del Mage Training Arena.
          - **Larry:** He oído que hay un pingüino ubicado en una ciudad de plagas en el desierto.
          - **Larry:** He oído que hay un pingüino ubicado en un pueblo de druidas.
          - **Larry:** He oído que hay un pingüino ubicado en Falador o sus alrededores.
          - **Larry:** He oído que hay un pingüino ubicado al este del reino de Kandarin.
          - **Larry:** He oído que hay un pingüino ubicado en el reino de las hadas.
          - **Larry:** He oído que hay un pingüino ubicado en los páramos helados.
          - **Larry:** He oído que hay un pingüino ubicado en el norte del reino de Misthalin.
          - **Larry:** He oído que hay un pingüino ubicado en el sur del reino de Misthalin.
          - **Larry:** He oído que hay un pingüino ubicado en el norte de Kharidian desert.
          - **Larry:** He oído que hay un pingüino ubicado en el sur de Kharidian desert.
          - **Larry:** He oído que hay un pingüino ubicado en el oeste del reino de Kandarin.
          - **Larry:** He oído que hay un pingüino ubicado en wilderness.
          - **Larry:** He oído que hay un pingüino ubicado cerca de un gran árbol rodeado de gente baja.
          - **Larry:** He oído que hay un pingüino ubicado cerca de una montaña de lobos.
          - **Larry:** He oído que hay un pingüino ubicado cerca de un pantano contaminado.
          - **Larry:** He oído que hay un pingüino ubicado cerca de un pueblo de hombres lobo.
          - **Larry:** He oído que hay un pingüino ubicado cerca de unos ogros en South Feldip Hills.
          - **Larry:** He oído que hay un pingüino ubicado cerca del Barbarian Outpost.
          - **Larry:** He oído que hay un pingüino ubicado cerca de las abejas y el lino.
          - **Larry:** He oído que hay un pingüino ubicado cerca del Castillo de Arturo.
          - **Larry:** He oído que hay un pingüino ubicado cerca de la ciudad de los fantasmas.
          - **Larry:** He oído que hay un pingüino ubicado cerca de la costa, al este de Ardougne.
          - **Larry:** He oído que hay un pingüino ubicado cerca de la isla de Dragontooth.
          - **Larry:** He oído que hay un pingüino ubicado cerca de los de orejas puntiagudas.
          - **Larry:** He oído que hay un pingüino ubicado cerca de Port Sarim.
          - **Larry:** He oído que hay un pingüino ubicado cerca de los saltamontes.
          - **Larry:** He oído que hay un pingüino ubicado al norte de Ardougne.
          - **Larry:** He oído que hay un pingüino ubicado en una gran isla en forma de media luna.
          - **Larry:** He oído que hay un pingüino ubicado en una isla, etc.
          - **Larry:** He oído que hay un pingüino ubicado en islas donde los hermanos se pelean.
          - **Larry:** He oído que hay un pingüino ubicado en algún lugar donde no se puede detectar.
          - **Larry:** He oído que hay un pingüino ubicado en algún lugar de Gielinor.
          - **Larry:** He oído que hay un pingüino ubicado al sur de Ardougne.
          - **Larry:** He oído que hay un pingüino ubicado al oeste de Ardougne, en las colinas.
          - **Larry:** He oído que hay un pingüino ubicado al oeste de Varrock.
          - **Larry:** He oído que hay un pingüino ubicado donde habitan los contrabandistas de plátanos.
          - **Larry:** He oído que hay un pingüino ubicado donde gobiernan los chupasangres.
          - **Larry:** He oído que hay un pingüino ubicado donde vuelan las águilas.
          - **Larry:** He oído que hay un pingüino ubicado donde los pescadores colonizan.
          - **Larry:** He oído que hay un pingüino ubicado donde gobiernan los monos.
          - **Larry:** He oído que hay un pingüino ubicado donde no pueden ir armas.
          - **Larry:** He oído que hay un pingüino ubicado donde los piratas se sienten en su mayoría inofensivos.
          - **Larry:** He oído que hay un pingüino ubicado donde habitan los duendes de ojos grandes.
          - **Larry:** He oído que hay un pingüino ubicado donde los enanos cavan profundamente.
          - **Larry:** He oído que hay un pingüino ubicado donde el Fremennik 'heim' y busca.
          - **Larry:** He oído que hay un pingüino ubicado donde entrena la Guardia Imperial.
          - **Larry:** He oído que hay un pingüino ubicado donde estudian los magos.
      - [Choice]: Quiero reclamar mi recompensa.
        - (opens=Spy Club)
      - [Choice]: ¿Qué necesito hacer de nuevo?{{anchor|explain-again}}
        - **Player:** ¿Qué debo hacer de nuevo?
        - **Larry:** ¿No estabas escuchando la primera vez? Bien, lo explicaré de nuevo, pero esta vez presta atención.
        - **Larry:** Hay espías por todas partes. Estoy reclutando valientes aventureros para encontrar a estos pingüinos y contarme su ubicación.
        - **Larry:** Siempre que veas un pingüino, espíalo. Están bien entrenados y cambiarán de posición cada semana, así que mantén los ojos bien abiertos.
        - **Larry:** Te di un dispositivo que puede rastrear a los pingüinos espías y ofrecerte pistas sobre su ubicación. Los pingüinos valen entre 1 y 3 Penguin Points dependiendo de lo difíciles que sean de encontrar.
        - **Larry:** Infórmate aquí y te recompensaré por tus esfuerzos.
        - (Condition: If Lunar Diplomacy is not completed:)
          - **Larry:** Una última cosa. Si alguna vez descubres un lugar llamado Lunar Isle, es posible que obtengas acceso a un hechizo que te ayudará a ponerte en contacto conmigo desde cualquier parte del mundo. No puedo decir más sobre eso, puede que haya espías cerca.
      - [Choice]: No importa.{{anchor|nevermind}}
        - **Player:** No importa.
        - **Larry:** BIEN. Sea así.

#### Hora del esmoquin


##### Antes del resfriado War

- **Larry:** No puedo hablar de eso ahora.

##### Después del resfriado War

- **Larry:** No puedo hacer eso ahora.

#### Esconder y buscar


##### Antes de hablar con Larry sobre Penguin Hide and Seek

- **Larry:** ¿Qué quieres?
- (above|shhhh)

##### Después de hablar con Larry sobre Penguin Hide and Seek

- ((Spy Club reward interface opens.))
