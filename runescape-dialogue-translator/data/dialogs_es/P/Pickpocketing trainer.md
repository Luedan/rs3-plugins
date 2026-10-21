# Pickpocketing trainer

- **Original Wiki Page**: [Transcript:Pickpocketing trainer](https://runescape.wiki/w/Transcript%3APickpocketing%20trainer)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Thieves' Guild


#### Hablando con él


##### Primera vez

- **Player:** Hola.
- **Pickpocketing trainer:** Ah, Player. Estoy dando clases sobre carteristas, si estás interesado.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Para qué sirven estos pañuelos?
    - **Player:** ¿Para qué sirven estos pañuelos?
    - **Pickpocketing trainer:** Oh, los usamos para realizar un seguimiento del régimen de entrenamiento de nuestros miembros. Los pañuelos azules te darán un punto, los rojos valen cuatro. Puedes reclamar una recompensa de cualquier trainer con tus puntos pañuelo.
    - (otro)
  - [Choice]: ¿Con qué frecuencia puedo hacer esto?
    - **Pickpocketing trainer:** La cantidad de puntos de pañuelo que puedes reclamar depende de tu dedicación al arte. Por el momento, puedes reclamar [número] puntos de pañuelo por semana en entrenamiento.
    - (otro)
  - [Choice]: ¿Qué actividades dan qué pañuelos?
    - **Player:** ¿Qué actividades dan qué pañuelos?
    - **Pickpocketing trainer:** Actualmente, nuestras zapatillas y cofres para carteristas llevan pañuelos azules. Esperamos expandirnos cuando tengamos más staff.
    - (otro)
  - [Choice]: Adiós por ahora.
    - ** Player:** Adiós por ahora.

##### Posteriormente

- **Player:** Hola.
- **Pickpocketing trainer:** Ah, Player. Estoy dando clases sobre carteristas, si estás interesado.
- [Menu]: Selecciona una opción
  - [Choice]: Sobre esos pañuelos...
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Para qué sirven estos pañuelos?
        - **Pickpocketing trainer:** Oh, los usamos para realizar un seguimiento del régimen de entrenamiento de nuestros miembros. Los pañuelos azules te darán un punto, los rojos valen cuatro. Puedes reclamar una recompensa de cualquier trainer con tus puntos pañuelo.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Con qué frecuencia puedo hacer esto?
            - **Pickpocketing trainer:** La cantidad de puntos de pañuelo que puedes reclamar depende de tu dedicación al arte. Por el momento, puedes reclamar [número] puntos de pañuelo por semana en entrenamiento.
            - (otro)
          - [Choice]: ¿Qué actividades dan qué pañuelos?
            - (Condition: Antes de Tiny Acorns:)
              - **Pickpocketing trainer:** Actualmente, nuestras zapatillas y cofres para carteristas llevan pañuelos azules. Esperamos expandirnos cuando tengamos más staff.
            - (Condition: Después de Tiny Acorns:)
              - **Pickpocketing trainer:** Nuestras zapatillas de carterismo, cajas fuertes y cofres fáciles llevan pañuelos azules; Los pañuelos rojos se pueden encontrar en las zapatillas deportivas y detrás de cerraduras más duras.
            - (otro)
          - [Choice]: Adiós por ahora.
            - ** Player:** Adiós por ahora.
      - [Choice]: ¿Cuantos puntos de pañuelo tengo?
        - (below|Check-points)
  - [Choice]: Por el momento no, gracias.
    - **Pickpocketing trainer:** Puedes intentarlo conmigo o con mis compañeros, aunque no tenemos nada más que pañuelos.
  - [Choice]: Entonces dame algunos consejos.
    - **Pickpocketing trainer:** Elegir un bolsillo es algo realmente sencillo.
    - **Pickpocketing trainer:** Actúa con indiferencia, mantén los dedos sueltos y asegúrate de que podrás recibir una paliza si te descubren.
    - **Pickpocketing trainer:** A la mayoría de las personas no les agrada que alguien pase la mano por sus pertenencias y te darán un buen golpe si te pillan haciéndolo.
    - ** Player:** Gracias por esa sorprendente revelación.
    - **Pickpocketing trainer:** Puedes intentarlo conmigo o con mis compañeros, aunque no tenemos nada más que pañuelos.

#### carterista


##### Fallando

- **Pickpocketing trainer:** {{RSChat|No, no, not like that.}}
- Intentas robarle el bolsillo al hombre.
- No logras robar el bolsillo del trainer.
- Has quedado atónito.

##### teniendo éxito

- Intentas robarle el bolsillo al hombre.
- Recuperas un pañuelo azul y se lo devuelves al trainer.
- (Condition: Si aún se pueden ganar puntos para la semana:)
  - [Ganas un punto de pañuelo.]
- (Condition: Si no se pueden ganar más puntos de pañuelo durante la semana:)
  - Has alcanzado el número máximo de puntos de pañuelo permitidos en tu nivel.

#### Puntos de control

- **Player:** ¿Cuántos puntos de pañuelo tengo?
- **Pickpocketing trainer:** Has recopilado [no hanky points yet/(number) hanky points]. Puedes reclamar la recompensa de hasta [número] puntos de pañuelo más esta semana.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Para qué son todos estos pañuelos?
    - (arriba)
  - [Choice]: Me gustaría reclamar una recompensa por mis puntos de pañuelo.
    - **Player:** ¡Me gustaría reclamar una recompensa por mis puntos de pañuelo!
    - (Condition: Sin puntos complicados que reclamar:)
      - **Pickpocketing trainer:** ¡No tienes puntos de pañuelo que reclamar! Prueba algunos de los ejercicios de entrenamiento del gremio.
    - (Condition: Con puntos de pañuelo para reclamar:)
      - **Pickpocketing trainer:** ¡Claro! Veamos ahora...
      - (receives=Thieving XP)
      - [Obtienes [número] Thieving XP. Te quedan 0 puntos y puedes entregar hasta [número] puntos más esta semana.]
    - (Condition: Habiendo reclamado el máximo de puntos del pañuelo de la semana:)
      - **Pickpocketing trainer:** Lo sentimos, has reclamado tantos puntos de pañuelo esta semana como puedas en tu nivel.
  - [Choice]: Adiós por ahora.
    - ** Player:** Adiós por ahora.
