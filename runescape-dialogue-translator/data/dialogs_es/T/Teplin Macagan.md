# Teplin Macagan

- **Original Wiki Page**: [Transcript:Teplin Macagan](https://runescape.wiki/w/Transcript%3ATeplin%20Macagan)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué te trae a Oo'glog?
    - **Teplin Macagan:** Hay arenisca roja en esta zona, de la mejor calidad de todo el territorio y excelente para hacer frascos de pociones.
    - **Teplin Macagan:** Al principio, no parecía seguro aventurarse en una ciudad llena de ogresas, pero parece que Oo'glog se ha convertido en un lugar de vacaciones. Así que mi socio Rutmir y yo hemos venido aquí para ver qué podemos encontrar.
    - **Player:** ¿Me sería posible hacer estos frascos de pociones también?
    - **Teplin Macagan:** Necesitas hablar con Rutmir. Es el mejor enano artesano. Está al noreste de aquí. Quizás te deje usar su maravillosa máquina para fabricar vidrio.
  - [Choice]: ¿Puedes decantarme algunas pociones?
    - (below|Decant option)
  - [Choice]: Tengo que irme.
    - **Teplin Macagan:** Nos vemos luego.

### Decant option

- ((Lo siguiente se muestra en una interfaz titulada "Opciones de Decantación":))
  - [Choice]: Decantar matraces
    - (Condition: Si el player no tiene frascos viables de pociones para decantar:)
      - **Teplin Macagan:** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener 2 matraces que no estén completamente llenos!
    - (Condition: Si el player tiene matraces para decantar:)
      - **Teplin Macagan:** Veamos qué tienes. Decantaré sus frascos de poción nuevamente en 6 frascos dosificados. Puedo hacer uso de los frascos, así que los aceptaré como pago.
      - (Action: Teplin decanta tantas como puede hasta llenar frascos de 6 dosis)
      - **Teplin Macagan:** Aquí tienes. ¡Eso es lo mejor que puedo hacer! Si los matraces no se ven muy diferentes, los limpié.
  - [Choice]: Convertir viales en matraces
    - (Condition: Si el player no tiene matraces vacíos en backpack:)
      - **Teplin Macagan:** Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos. Puedes traérmelos anotados o sin anotaciones.
    - (Condition: Si el player tiene matraces vacíos en backpack:)
      - **Teplin Macagan:** Veamos qué tienes. Decantaré los viales de poción y todos los frascos hasta 4 dosis en frascos de 6 dosis. Tendrás que proporcionar los matraces vacíos tú mismo; no son baratos.
      - (Condition: Si el player tiene pociones para decantar en matraces:)
        - (Action: Teplin decanta tantas pociones como puede hasta llenar frascos de 6 dosis.)
        - **Teplin Macagan:** Aquí tienes. ¡Eso es lo mejor que puedo hacer!
      - (Condition: Si el player no tiene pociones para decantar:)
        - **Teplin Macagan:** ¡Lo siento, parece que no tienes nada en lo que pueda ayudarte! Asegúrate de tener las pociones correctas y algo de espacio libre en tu inventario y podré intentarlo de nuevo.
  - [Choice]: Convertir matraces en viales
    - (Condition: Si el player no tiene frascos viables de pociones para decantar:)
      - **Teplin Macagan:** Lo siento, parece que no tienes nada que pueda usar. ¡Asegúrate de tener al menos 1 matraz!
    - (Condition: Si el player tiene frascos de pociones para decantar en viales:)
      - **Teplin Macagan:** Por supuesto. Creo que puedo utilizar los matraces, así que te daré los viales gratis.
      - (Action: Teplin decanta tantas pociones como puede en viales marcados.)
      - **Teplin Macagan:** Ahí lo tienes, ¡eso es lo mejor que puedo hacer!
  - [Choice]: Cancelar
    - ((La interfaz se cierra.))
