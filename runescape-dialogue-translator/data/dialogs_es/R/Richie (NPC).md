# Richie (NPC)

- **Original Wiki Page**: [Transcript:Richie (NPC)](https://runescape.wiki/w/Transcript%3ARichie%20%28NPC%29)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before contributing coins


#### Si el player tiene 0 coins con ellos

- No tienes coins para regalar.

#### Si el player tiene menos de 1.000.000 coins con ellos

- La urraca te ignora.

#### Si el player tiene entre 1.000.000 y 9.999.999 coins con ellos

- La urraca se interesa un poco por tu coins, pero sigue ignorándote.

#### Si el player tiene más de 10.000.000 coins con ellos

- **Richie:** ¡Buenos días! El conjunto de coins que tienes ahí tiene un aspecto bastante brillante.
- **Player:** ¿Estás mirando mi coins?
- [Mantienes tu coins frente a ti.]
- **Player:** Estos son mis coins ganados con tanto esfuerzo. He estado en muchas aventuras, ya ves.
- **Richie:** ¿Serías tan amable de compartir algunos conmigo?
- (continue|withgp)

### After contributing coins

- **Richie:** Buenos días Player. Es genial verte de nuevo.
- **Richie:** ¿Estás aquí para compartir más de tu riqueza?
- (Condition: Sin coins:)
  - No tienes coins para regalar.
- (Condición: Con coins :) {{anchor|withgp}}
  - ¿Cuántos coins te gustaría regalar?<br>Has ayudado a Richie a acumular una riqueza total de [número].<br><br>(0-[100,000,000 minus the already donated amount])<br>[input field]
  - (Condition: Introduciendo un importe positivo:)
    - (Condition: Si se ingresó un número superior a 100.000, se muestra lo siguiente en una interfaz titulada 'CONFIRMACIÓN':)
      - Estás a punto de regalar [número] coins.<br><br>¿Quieres continuar?
        - [Choice]: CANCELAR
          - (end)
        - [Choice]: bien
          - (continue)
    - (removes=coins)
    - **Richie:** Player, ¡me has ayudado a acumular una riqueza total de [número]!
    - (Condition: Si la suma total donada alcanzó 100.000.000 coins:)
      - **Richie:** Como sabes claramente cómo aumentar tu riqueza, ¡he decidido unirme a ti en tus aventuras!
      - (Action: Richie desaparece del Grand Exchange.)
      - Has desbloqueado la mascota: 'Richie'.
      - (ventana emergente)
        - {{popup|You have unlocked the pet:<br>'Richie'.|colour=#0f0}}
      - Puedes activar esto a través de la pestaña 'Mascotas' en la interfaz 'Personalizaciones'.
      - ¡Felicitaciones! Has completado: 'Richie': desbloquea la mascota Richie para que pueda ayudar a Richie a acumular riqueza en Grand Exchange. (100.000.000/100.000.000)
