# Locks and traps trainer

- **Original Wiki Page**: [Transcript:Locks and traps trainer](https://runescape.wiki/w/Transcript%3ALocks%20and%20traps%20trainer)
- **Letter**: `L`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript



### In the Thieves' Guild


#### Diálogo por primera vez

- **Player:** ¿Qué puedes enseñarme?
- **Locks and traps trainer:** Soy el locks and traps trainer. ¿Necesitas algún consejo?
- [Menu]: Selecciona una opción
  - [Choice]: Sobre esos pañuelos...
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Para qué sirven estos pañuelos?
        - **Player:** ¿Para qué sirven estos pañuelos?
        - **Locks and traps trainer:** Oh, los usamos para realizar un seguimiento del régimen de entrenamiento de nuestros miembros. Los pañuelos azules te darán un punto, los rojos valen cuatro. Puedes reclamar una recompensa de cualquier trainer con tus puntos pañuelo.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Con qué frecuencia puedo hacer esto?
            - **Player:** ¿Con qué frecuencia puedo hacer esto?
            - **Locks and traps trainer:** La cantidad de puntos de pañuelo que puedes reclamar depende de tu dedicación al arte. Por el momento, puedes reclamar <number> puntos de pañuelo por semana en entrenamiento.
            - [Menu]: Selecciona una opción
              - [Choice]: ¿Para qué sirven estos pañuelos?
                - (arriba)
              - [Choice]: ¿Qué actividades dan qué pañuelos?
                - (abajo)
              - [Choice]: Adiós por ahora.
                - **Player:** Adiós por ahora.
      - [Choice]: ¿Qué actividades dan qué pañuelos?
        - **Player:** ¿Qué actividades dan qué pañuelos?
        - (Condition: Having completed only Buyers and Cellars:)
          - **Locks and traps trainer:** Actualmente, nuestras zapatillas y cofres para carteristas llevan pañuelos azules. Esperamos expandirnos cuando tengamos más staff.
          - (continue)
        - (Condition: After completing subsequent capers:)
          - **Locks and traps trainer:** Nuestras zapatillas de carterismo, cajas fuertes y cofres fáciles llevan pañuelos azules; Los pañuelos rojos se pueden encontrar en las zapatillas deportivas y detrás de cerraduras más duras.
          - (continue)
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Para qué sirven estos pañuelos?
            - (arriba)
          - [Choice]: ¿Con qué frecuencia puedo hacer esto?
            - (arriba)
          - [Choice]: Adiós por ahora.
            - **Player:** Adiós por ahora.
  - [Choice]: Está bien, gracias.
    - **Player:** Está bien, gracias.
    - **Locks and traps trainer:** Siéntete libre de practicar en mis arcas; las del sur son ejemplos de esclusas más complejas.
  - [Choice]: Siempre estoy feliz de aprender.
    - **Player:** Siempre estoy feliz de aprender.
    - **Locks and traps trainer:** Te encontrarás con bastantes puertas y cofres en todo el mundo, y la gente tiende a cerrarlos con llave.
    - **Locks and traps trainer:** Sin embargo, con un poco de habilidad y, a veces, algunas herramientas especializadas, puedes abrirlas y desarmar los gatillos de las trampas que sostienen.
    - **Locks and traps trainer:** Si algo parece sospechoso, examínelo de cerca antes de tocarlo.
    - **Player:** ¿Herramientas especializadas?
    - **Locks and traps trainer:** Algunas cerraduras son más complejas que otras; los más complicados necesitan una ganzúa. Puedes comprar uno en la tienda si pierdes el tuyo o se rompe.
    - **Player:** Otro misterio desbloqueado. Gracias.
    - **Locks and traps trainer:** Siéntete libre de practicar en mis arcas; las del sur son ejemplos de esclusas más complejas.

#### Diálogo posterior

- **Player:** ¿Qué puedes enseñarme?
- **Locks and traps trainer:** Soy el locks and traps trainer. ¿Necesitas algún consejo?
- [Menu]: Selecciona una opción
  - [Choice]: Sobre esos pañuelos...
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Para qué sirven estos pañuelos?
        - (arriba)
      - [Choice]: ¿Cuantos puntos de pañuelo tengo?
        - **Player:** ¿Cuántos puntos de pañuelo tengo?
        - **Locks and traps trainer:** Has recopilado [no hanky points yet/(number) hanky points]. Puedes reclamar la recompensa de hasta [número] puntos de pañuelo más esta semana.
        - [Menu]: Selecciona una opción
          - [Choice]: ¿Para qué sirven estos pañuelos?
            - (arriba)
          - [Choice]: Me gustaría reclamar una recompensa por mis puntos de pañuelo.
            - **Player:** Me gustaría reclamar una recompensa por mis puntos de pañuelo.
            - (Condition: With no hanky points to claim:)
              - **Locks and traps trainer:** ¡No tienes puntos de pañuelo que reclamar! Prueba algunos de los ejercicios de entrenamiento del gremio.
            - (Condition: With hanky points to claim:)
              - **Locks and traps trainer:** ¡Claro! Veamos ahora...
              - (receives=Thieving XP)
              - Obtienes <number> Thieving XP. Le quedan <number> puntos y puede entregar hasta <number> puntos más esta semana.
            - (Condition: Having claimed the maximum hanky points for the week:)
              - **Locks and traps trainer:** Lo sentimos, has reclamado tantos puntos de pañuelo esta semana como puedas en tu nivel.
          - [Choice]: Adiós por ahora.
            - **Player:** Adiós por ahora.
      - [Choice]: Me gustaría reclamar una recompensa por mis puntos de pañuelo.
        - (arriba)
      - [Choice]: Adiós por ahora.
        - **Player:** Adiós por ahora.
  - [Choice]: Está bien, gracias.
    - (arriba)
  - [Choice]: Siempre estoy feliz de aprender.
    - (arriba)

#### Puntos de control

- (above|claim)
