# Advanced pickpocketing trainer

- **Original Wiki Page**: [Transcript:Advanced pickpocketing trainer](https://runescape.wiki/w/Transcript%3AAdvanced%20pickpocketing%20trainer)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue


#### Sin blackjack equipado

- El trainer hace todo lo posible para centrarse en ti.
- ** Advanced pickpocketing trainer: ** Enseño 'Carteristas agresivos'. Necesitas estar mejor equipado antes de que pueda ayudarte. Consíguete una cachiporra.

#### Con un blackjack equipado

- El trainer hace todo lo posible para centrarse en ti.
- ** Advanced pickpocketing trainer: ** Un cosh es una herramienta fantástica, y eso no es una hipérbole. ¿Sabes cómo usarlo?
- [Menu]: Selecciona una opción
  - [Choice]: About those hankies...|cond=Si no es la primera vez:
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Para qué sirven estos pañuelos?
        - **Advanced pickpocketing trainer:** Oh, los usamos para realizar un seguimiento del régimen de entrenamiento de nuestros miembros. Los pañuelos azules te darán un punto, los rojos valen cuatro. Puedes reclamar una recompensa de cualquier trainer con tus puntos pañuelo.
        - [Menu]: Selecciona una opción
          - [Choice]: What are these handkerchiefs for?|cond=Sólo si no se seleccionó previamente:
            - (above|handkerchiefs-for)
          - [Choice]: ¿Con qué frecuencia puedo hacer esto?
            - **Advanced pickpocketing trainer:** La cantidad de puntos de pañuelo que puedes reclamar depende de tu dedicación al arte. Por el momento, puedes reclamar <number> puntos de pañuelo por semana en entrenamiento.
            - (Action: otro)
          - [Choice]: ¿Qué actividades dan qué pañuelos?
            - **Advanced pickpocketing trainer:** Nuestras zapatillas de carterismo, cajas fuertes y cofres fáciles llevan pañuelos azules; Los pañuelos rojos se pueden encontrar en las zapatillas deportivas y detrás de cerraduras más duras.
            - (Action: otro)
          - [Choice]: Adiós por ahora.
            - ** Player:** Adiós por ahora.
      - [Choice]: ¿Cuantos puntos de pañuelo tengo?
        - **Advanced pickpocketing trainer:** Has acumulado puntos de pañuelo <number>. Puedes reclamar la recompensa de hasta <number> puntos de pañuelo más esta semana.
      - [Choice]: Me gustaría reclamar una recompensa por mis puntos de pañuelo.
        - ''Si el player tiene puntos de pañuelo
          - **Advanced pickpocketing trainer:** Malvado, amigo. Vamos a configurarlo.
          - Obtienes <number> Thieving XP. Le quedan <number> puntos y puede entregar hasta <number> puntos más esta semana.
        - ''Si el player no tiene puntos de pañuelo
          - **Advanced pickpocketing trainer:** ¿Tú qué? No tienes puntos de pañuelo para entrar.
      - [Choice]: Adiós por ahora.
        - ** Player:** Adiós por ahora.
  - [Choice]: What are these handkerchiefs for?|cond=Sólo por primera vez:
    - ** Player:** ¿Para qué sirven estos pañuelos?
    - (above|handkerchiefs-for)
  - [Choice]: He tenido algo de experiencia, sí.
    - ** Player:** He tenido algo de experiencia, sí.
    - **Advanced pickpocketing trainer:{{anchor|ngabh}}** Puedes practicar conmigo si quieres, pero solo con un equipo de entrenamiento...
  - [Choice]: Recuérdame los puntos más finos, por favor.
    - ** Player:** ¿Recuérdame los puntos más finos, por favor?
    - **Advanced pickpocketing trainer:** Un blackjack, cosh o sap es una herramienta para abrir los bolsillos de las personas que vigilan mejor su billetera que el reverso de su propia moneda.
    - **Advanced pickpocketing trainer:** Primero debes sacarlos del alcance de las miradas indiscretas, luego simplemente darles un buen golpe justo aquí y caerán.
    - **Advanced pickpocketing trainer:** Entonces podrás ver qué tienen y que quizás quieras. ¿Entiendo?
    - ** Player:** Sí, eso fue bastante directo. Gracias.
    - (Action: continuar|ngabh)

### Blackjack dialogue


#### señuelo

''Uno de los siguientes diálogos se reproduce aleatoriamente:

##### Diálogo 1

- ** Player:** ¡Cuidado! ¡El tipo detrás de ti tiene un garrote!
- **Advanced pickpocketing trainer:** ¿Qué?

##### Diálogo 2

- ** Player:** ¡Detrás de ti! ¡Un mono de tres cabezas!
- **Advanced pickpocketing trainer:** ¿Qué?

##### Diálogo 3

- ** Player:** ¡Ese es el tercer ornitorrinco más grande que he visto en mi vida!
- **Advanced pickpocketing trainer:** ¿Qué?

##### Diálogo 4

- ** Player:** ¡Mira ALLÍ!
- **Advanced pickpocketing trainer:** ¿Qué?

##### Diálogo 5

- ** Player:** ¡Mira! ¡Un águila!
- **Advanced pickpocketing trainer:** ¿Qué?

##### Diálogo 6

- ** Player:** Tu cordón está desatado.
- **Advanced pickpocketing trainer:** ¿Qué?

##### Si está equipado un blackjack de madera

- ** Player:** Necesitaré un palo de entrenamiento para practicar mi técnica.

#### Nocaut

- **Advanced pickpocketing trainer:**{{RSChat|Blarg!}}
- Golpeas al trainer en la cabeza lo más cortésmente que puedas.
- **Advanced pickpocketing trainer:**{{RSChat|Anuvva bruise for me collection...}}

##### Sin atraer

- ** Player:** Primero necesito desviar su atención.

##### Sin nivel 40 Thieving

- Necesitas un nivel Thieving de al menos 40 para practicar el coshing.

#### Botín

- Vacías el bolsillo del hombre y le cubres con el pañuelo rojo.
- Ganas 4 puntos de pañuelo.

##### Sin ser noqueado

- Deberías noquearlo antes de intentar saquearlo.
