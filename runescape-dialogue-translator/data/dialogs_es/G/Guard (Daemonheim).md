# Guard (Daemonheim)

- **Original Wiki Page**: [Transcript:Guard (Daemonheim)](https://runescape.wiki/w/Transcript%3AGuard%20%28Daemonheim%29)
- **Letter**: `G`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Player:** Hola.
- **Guardia:** ¿Podemos ayudarte en algo?
- ¿Qué te gustaría decir?{{anchor|init}}
  - ¿Puedo pasar por la puerta?
    - **Player:** ¿Puedo pasar por la puerta?
    - **Guardia:** Si quieres te dejaremos pasar al Wilderness. Ten en cuenta que otros jugadores podrían atacarte allí y no se te permitirá atravesar la puerta mientras estés en combate.
    - ¿Qué te gustaría decir?
      - No tengo miedo.
        - **Player:** No tengo miedo.
        - **Guardia:** Tu discurso es valiente. Viaja hacia el suroeste y deberías llegar a la ciudad de Varrock, si no mueres primero. Ahora bien, ¿podemos ayudarte en algo más?
        - ¿Qué te gustaría decir?{{anchor|second-opts}}
          - ¿Qué estás haciendo aquí?
            - (below|role)
          - ¿Hay alguna otra manera de salir de aquí?
            - **Player:** ¿Hay alguna otra manera de salir de aquí?
            - **Guardia:** Oh, sí. Vuelve a subir la colina hasta el campamento y luego dirígete hacia el este hasta los muelles. Hay un ferry que te llevará al sur, a las llamadas tierras civilizadas. Es mucho más seguro que intentar caminar por Wilderness. Ahora bien, ¿podemos ayudarte en algo más?
            - (initial|init)
          - No gracias.
            - **Player:** No, gracias.
      - Olvídalo, no voy a pasar por ahí.
        - **Player:** Olvídalo, no voy a pasar por ahí.
        - **Guardia:** Eso es sabio. Ahora bien, ¿podemos ayudarte en algo más?
        - (continuea|second-opts)
  - ¿Qué haces aquí?{{anchor|role}}
    - **Player:** ¿Qué haces aquí?
    - **Guardia:** Estamos protegiendo esta entrada contra los feroces luchadores que deambulan por Wilderness.
    - **Player:** Buena suerte con eso.
    - **Guardia:** Gracias. Ahora bien, ¿podemos ayudarte en algo más?
    - (continuea|second-opts)
  - No gracias.
    - **Player:** No, gracias.

### Attempting to enter the Wilderness

- **Guardia:** Puedes ingresar al Wilderness, si quieres, pero no puedes regresar por aquí si estás en combate.
- ¿Pasar por la puerta?
  - Sí, entiendo las restricciones.
    - (Action: el player pasa junto al guardia y entra en Wilderness.)
  - No, me quedaré aquí.
    - ((The player walks one square back.))
    - **Player:** No, me quedaré aquí.
