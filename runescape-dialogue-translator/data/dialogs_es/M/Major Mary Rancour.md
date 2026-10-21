# Major Mary Rancour

- **Original Wiki Page**: [Transcript:Major Mary Rancour](https://runescape.wiki/w/Transcript%3AMajor%20Mary%20Rancour)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Burthorpe

- [Menu]: Selecciona una opción
  - [Choice]: He perdido mi hacha del ejército enano.
    - (Condition: Sin ningún espacio en backpack:)
      - [Necesitas un espacio de inventario libre para recuperar el hacha del ejército enano.]
    - (Condition: Con al menos un espacio en backpack:)
      - (Condition: Con el hacha del ejército enano realmente perdida:)
        - **Major Mary Rancour:** Así que sí. Hay uno en las tiendas. ¿Te gustaría?
        - [Menu]: Selecciona una opción
          - [Choice]: si
            - [Dwarven army axe.]}}
            - [El hacha del ejército enano funciona como un hacha de acero. Al talar árboles normales, puedes obtener un nudo de madera, y al extraer cobre o estaño, una gema de lapislázuli, que puedes convertir en un broche de lapislázuli.]
            - [También te otorga +3 XP al extraer cobre y estaño, elaborar cuero suave y arcilla, cocinar, cazar vencejos carmesí y kebbits polares, cortar madera y hacer fuego normal y oak logs, y colocar puntas de flecha de bronce.]
          - [Choice]: No
            - (end)
      - (Condition: Con el hacha del ejército enano en backpack o banco:)
        - **Major Mary Rancour:** Según mis registros, todavía tienes un hacha del ejército enano. Quizás esté en tu banco.
  - [Choice]: ¡Debe haber algo de lucha que hacer!
    - **Major Mary Rancour:** Siempre hay trolls en la cueva del noroeste. Entra allí y mata a algunos si quieres.
  - [Choice]: cond=Historical:|(Vuelva a reproducir la escena de llegada de Burthorpe).
    - (Action: Reproduce la escena de llegada de Burthorpe.)
  - [Choice]: Necesito orientación.
    - (Condition: Históricamente:)
      - ((Se abre la interfaz para reproducir los tutoriales).
    - (Condition: Actualmente:)
      - (end)
  - [Choice]: Adiós.
    - (end)

#### Reproducir opción de escena de llegada (histórica)

- [Menu]: ¿Reproducir la escena de llegada de Burthorpe?
  - [Choice]: Sí.
    - (Action: Se repite la escena de llegada de Burthorpe.)
  - [Choice]: No.
    - (end)
