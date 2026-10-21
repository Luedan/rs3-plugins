# Archmage Sedridor

- **Original Wiki Page**: [Transcript:Archmage Sedridor](https://runescape.wiki/w/Transcript%3AArchmage%20Sedridor)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Wizards' Tower


#### Habla con


##### Normalmente

- (Condition: Sin nivel 99 Magic y nivel 99 Runecrafting:)
  - **Archmage Sedridor:** Bienvenido, aventurero, al mundialmente famoso Wizards' Tower. ¿Le puedo ayudar en algo?
  - (continue)
- (Condition: Con nivel 99 Magic y nivel 99 Runecrafting:)
  - **Archmage Sedridor:** Bienvenido a la torre, archimago. ¿Le puedo ayudar en algo?
  - (continue)
- {{anchor|init-tower}}[Menú]: Elige una opción:
  - [Choice]: cond=With level 99 Magic and level 99 Runecrafting:|¿Acabas de llamarme 'archimago'?
    - **Archmage Sedridor:** De hecho, lo hice. El título normalmente está reservado para el líder de Wizards' Tower, pero a la luz de tu dominio tanto de Magic como de Runecrafting, creo que te has ganado el derecho a usarlo.
    - (El título 'Archimago' se desbloquea la primera vez que se utiliza esta opción de diálogo).
    - [Menu]: Selecciona una opción
      - [Choice]: (Establezca su título en 'Archimago'.)
        - Ahora otros te conocen como el Archimago Player.
        - **Archmage Sedridor:** ¿Hay algo más que pueda hacer por ti, Archimago?
        - (otro|torre-init)
      - [Choice]: (No cambies tu título).
        - (otro|torre-init)
  - [Choice]: cond=After Love Story:|A tus magos les fue bien contra el Wise Old Man.
    - **Archmage Sedridor:** Gracias. Debo admitir que habríamos perdido si Traiborn no hubiera ayudado. No tengo idea de qué convocó, pero ciertamente aterrorizó al Wise Old Man y a esa mujer.
  - [Choice]: ¿Puedes teletransportarme a la esencia rúnica?
    - **Archmage Sedridor:** {{RSChat|Seventior disthine molenko!}}
    - (Action: Archmage Sedridor teletransporta a el player a la mina Rune Essence.)
  - [Choice]: Cuéntame sobre el Wizards' Tower.
    - **Archmage Sedridor:** La torre es el mejor instituto de aprendizaje mágico en Misthalin, Asgarnia o Kandarin. El libro de hechizos del aventurero estándar y los imanes de teletransportación son productos de la investigación de los magos de las torres.
    - **Archmage Sedridor:** Lo más importante es que la torre guarda el secreto de la esencia rúnica, que permitió a la civilización humana prevalecer sobre los monstruos y bárbaros y marcó el comienzo de la Quinta Edad del mundo.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Puedes enseñarme magia?
        - **Archmage Sedridor:** ¡Ya conoces el libro de hechizos del aventurero! Para un aventurero como tú, la mejor manera de aprender es salir y practicar lanzar hechizos.
        - (otros|acerca de-las-opciones-de-la-torre-de-wizards)
      - [Choice]: ¿Cuáles son las ruinas que vi fuera de la torre?
        - **Archmage Sedridor:** Ah... son la reliquia de un capítulo triste en la historia de la torre.
        - **Archmage Sedridor:** Originalmente, los magos de la torre no estaban tan unidos como ahora. Había órdenes dedicadas a diferentes dioses: en particular Saradomin, dios de la bondad y el orden, y Zamorak, dios del mal y el caos.
        - **Archmage Sedridor:** Las órdenes trabajaron juntas durante setenta años, pero finalmente los magos zamorakianos traicionaron a los demás y quemaron la torre.
        - **Archmage Sedridor:** El archimago Perien reconstruyó la torre y prohibió a los magos zamorakianos unirse. La Torre reconstruida ha estado unida y en paz durante cien años.
        - (otros|acerca de-las-opciones-de-la-torre-de-wizards)
      - [Choice]: ¿El secreto de la esencia rúnica?
        - **Archmage Sedridor:** Sí, específicamente, el secreto del hechizo de teletransportación que nos permite alcanzarlo.
        - **Archmage Sedridor:** El descubrimiento de la esencia rúnica y la capacidad de hacer piedras rúnicas fue el mayor descubrimiento mágico en la historia de Gielinor. Permite a cualquiera producir efectos mágicos de forma fácil y fiable.
        - **Archmage Sedridor:** La esencia rúnica se encuentra en el norte helado, donde una vez descansó el Ojo de Saradomin. Los primeros magos llegaron hasta allí por una ardua ruta terrestre, pero finalmente descubrieron un hechizo para teletransportarse allí directamente.
        - **Archmage Sedridor:** Después de que los magos zamorakianos quemaran la torre hace cien años, el archimago Perien decidió mantener el hechizo en secreto en lugar de dejarlo caer en manos malvadas.
        - **Archmage Sedridor:** Lanzaremos el hechizo para cualquiera que consideremos digno de confianza, pero el hechizo en sí es un misterio interno de la torre y solo se enseña a personas seleccionadas.
        - (otros|acerca de-las-opciones-de-la-torre-de-wizards)
      - [Choice]: Otras preguntas...
        - (initial|init-tower)
      - [Choice]: Adiós.
        - (end)
  - [Choice]: Nada, gracias. Estoy viendo solamente.
    - (end)

##### Durante la tarea de celebraciones del 25 Aniversario

- **Player:** Hola, Archmage Sedridor. ¿Puedo hacer una pregunta sobre la red Lodestone?
- **Archmage Sedridor:** Por qué, por supuesto. ¿Cómo puedo ser de ayuda?
- **Player:** ¿Crees que las imanes han mejorado la vida de todos o les han quitado un poco de su magia?
- **Archmage Sedridor:** Hmm, una pregunta peculiar. ¡Son el colmo de la comodidad! Han hecho maravillas para el comercio mundial. Sin duda, han evitado a muchos ex caminantes innumerables lesiones en los pies.
- **Archmage Sedridor:** Ah, pero es cierto... ¿Cuándo uno se toma el tiempo para pasear casualmente estos días, para disfrutar de las vistas y los sonidos? ¿Qué maravillas nos perdemos cuando la comodidad está en primer plano...?
- {{RSFontAchievement|A Lode of Fun|Talk to Archmage Sedridor about the Lodestone Network.}}
- ((Se muestra en una ventana emergente de finalización de tarea:))
  - {{Colour|#F0BE79| TAREA DEL 25 ANIVERSARIO |#181513}}
  - Un montón de diversión
  - Hable con Archmage Sedridor sobre la red Lodestone.
  - (continue)
- **Archmage Sedridor:** De hecho, la vida debería ser algo "alterada", porque no puedes tener altibajos sin los bajos. Gracias por recordarme esto. Sabes qué, creo que saldré a caminar pronto.
- (Condition: Si se han completado todas las tareas:)
  - **Player:** Parece que he completado todo. ¡Será mejor que vaya a ver a Hans sobre esa recompensa!

#### Usando la caja de depósito con runa o esencia pura en backpack

- **Archmage Sedridor:** Lo sentimos, pero el uso de este cofre está prohibido mientras se lleva esencia.
- Sedridor no quiere que guardes esencia rúnica en la torre.

### At summer events

- **Archmage Sedridor:** Foreman George continúa impresionándome con sus diseños de castillos de arena; Me cuesta creer que no haya magia involucrada. Me encantaría ver un castillo de arena inspirado en la magia mientras esté aquí.
- **Player:** No eres muy sutil acerca de lo que quieres, ¿verdad?
