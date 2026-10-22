# Cart conductor

- **Original Wiki Page**: [Transcript:Cart conductor](https://runescape.wiki/w/Transcript%3ACart%20conductor)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Dwarven Mine

- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Cart conductor:** Soy empleado de los carritos Keldagrim. Me aseguro de que los carros en esta área lleguen a tiempo y que la gente pague sus pasajes.
    - (initial)
  - [Choice]: ¿Dónde puedes llevarme?
    - **Player:** ¿A dónde puedes llevarme?
    - (Condition: Before gaining access to Keldagrim:)
      - **Cart conductor:** No creo que pueda llevarte a la ciudad de Keldagrim, humano. Quizás, cuando encuentres otro camino hacia la ciudad y hables con alguien importante allí, se te permitirá hacerlo.
      - (initial)
    - (Condition: After gaining access to Keldagrim:)
      - **Cart conductor:** Esta pista conduce directamente a Keldagrim. Sólo detente.
      - (initial)
  - [Choice]: Me gustaría comprar un billete.
    - **Player:** Me gustaría comprar un billete.
    - **Cart conductor:** No necesitas entrada. El Consorcio ha decidido conceder viajes gratuitos en carros mineros a todos los humanos.
  - [Choice]: Tengo que irme.
    - **Player:** Me tengo que ir.
    - **Cart conductor:** Solo recuerda, dondequiera que vayas, llegarás más rápido a través de los carritos Keldagrim.

### Under White Wolf Mountain

- [Menu]: Selecciona una opción
  - [Choice]: ¿Quién eres?
    - **Player:** ¿Quién eres?
    - **Cart conductor:** ¿Quiénooo? ¿Yo? Oh, me aseguro de que *hic* el tráfico de carritos proceda *hic* de forma ordenada. Moda. Sí.
    - (initial)
  - [Choice]: ¿Dónde puedes llevarme?
    - **Player:** ¿A dónde puedes llevarme?
    - (Condition: Before gaining access to Keldagrim:)
      - **Cart conductor:** Espera un segundo... ¡ESPERA un segundo! ¡Eres un humano! No creo que puedas usar los carritos.
      - **Cart conductor:** Tal vez si encuentras otra manera de entrar a la ciudad *hic*, tal vez puedas hablar con alguien y te dejará.
      - (initial)
    - (Condition: After gaining access to Keldagrim:)
      - **Cart conductor:** ¡Norte, norte, norte *hic* norte hasta Keldagrim!
      - (initial)
  - [Choice]: Me gustaría comprar un billete.
    - **Player:** Me gustaría comprar un billete.
    - **Cart conductor:** Un boleto para ehm...*hic* Keldagrim. Eso es 2... 3...*hic* ¡nada! ¡Es gratis!
    - **Cart conductor:** Es una nueva iniciativa económica...económica. Todos los humanos viajan a Keldagrim...¡gratis!
  - [Choice]: Tengo que irme.
    - **Player:** Me tengo que ir.
    - **Cart conductor:** Sólo recuerda, dondequiera que vayas... ehm... *hic* oh, olvídalo.

### In Keldagrim


#### Cerca de los carros de la mina.

- (Cuando se habla con cualquier cart conductor cerca de las vías del carro de la mina en Keldagrim. Cada cart conductor comienza con su propio saludo que no es exclusivo de ellos pero que nunca cambia, y continúa con el mismo diálogo :)
- (Condition: Talking to the green outfit near the tracks:)
  - **Cart conductor:** Entradas, entradas, ¡consigue tus entradas aquí!
  - (continue)
- (Condition: Talking to the red outfit:)
  - **Cart conductor:** ¿Puedo ayudarte en algo?
  - (continue)
- (Condition: Talking to the green outfit in waiting area:)
  - **Cart conductor:** ¿Sí [sir/m'am]? ¿Puedo ayudarte en algo?
  - (continue)
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué es este lugar?
    - **Player:** ¿Qué es este lugar?
    - (Condition: Talking to the conductors near the tracks:)
      - **Cart conductor:** Esta es la estación de carrito Keldagrim, humana.
      - (continue)
    - (Condition: Talking to the green outfit in waiting area:)
      - **Cart conductor:** Estás en la sala de espera principal de la estación de carritos Keldagrim.
      - (continue)
    - **Player:** ¿Estación de carro? ¿Qué pasa aquí entonces?
    - **Cart conductor:** Keldagrim es el centro de todo el tráfico del reino de los enanos. Casi todos los puestos avanzados enanos tienen vías de ferrocarril que conducen a Keldagrim, conectándolos para facilitar el viaje y el transporte de mercancías.
    - **Player:** ¡Increíble! ¿Y qué impulsa los carros? ¿Magic?
    - **Cart conductor:** Oh, no, no, los enanos no usamos magia. Todo esto está propulsado por máquinas de vapor, desarrolladas durante los últimos siglos después de que el Consorcio llegara al poder.
    - **Player:** Gracias por la información.
  - [Choice]: ¿Dónde puedes llevarme?
    - **Player:** ¿A dónde puedes llevarme?
    - **Cart conductor:** Veamos, podemos llevarte a las minas debajo de Ice Mountain y al Grand Exchange en Varrock.
    - (Condition: If the player has completed Fishing Contest:)
      - **Cart conductor:** Y como eres amigo de nuestros hermanos bajo White Wolf Mountain, también podríamos llevarte allí.
  - [Choice]: Me gustaría comprar un billete.
    - **Player:** Me gustaría comprar un billete.
    - **Cart conductor:** Oh, no necesitas un boleto. El Consorcio ha decidido conceder a los humanos viajes gratuitos en carros mineros hacia y desde Keldagrim.
  - [Choice]: Tengo que irme.
    - **Player:** Me tengo que ir.
    - **Cart conductor:** Solo recuerda, dondequiera que vayas, llegarás más rápido a través de los carritos Keldagrim.

##### Diálogo aéreo

- (Condition: Cart conductor wearing red outfit:)
  - **Cart conductor:** {{RSChat|White Wolf Mountain carts departing from all tracks!|colour=yellow|shadow=yes}}
  - **Cart conductor:** {{RSChat|Ice Mountain carts departing from all tracks!|colour=yellow|shadow=yes}}
  - **Cart conductor:** {{RSChat|Grand Exchange carts departing from all tracks!|colour=yellow|shadow=yes}}
  - **Cart conductor:** {{RSChat|Mind the cart!|colour=yellow|shadow=yes}}
  - **Cart conductor:** {{RSChat|Careful!|colour=yellow|shadow=yes}}
- (Condition: Cart conductors wearing green outfit:)
  - **Cart conductor:** {{RSChat|Tickets! Tickets!|colour=yellow|shadow=yes}}
  - **Cart conductor:** {{RSChat|Buy your tickets here!|colour=yellow|shadow=yes}}
  - **Cart conductor:** {{RSChat|Selling tickets!|colour=yellow|shadow=yes}}

#### El conductor de Keldagrim en reposo

- **Cart conductor:** ¿Qué quieres?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué es este lugar?
    - **Player:** ¿Qué es este lugar?
    - **Cart conductor:** ¿No ves que estoy teniendo un pequeño descanso?
    - **Player:** Ahora que lo mencionas, sí.
  - [Choice]: ¿Dónde puedes llevarme?
    - **Player:** ¿A dónde puedes llevarme?
    - **Cart conductor:** ¿No ves que estoy teniendo un pequeño descanso?
    - **Player:** Ahora que lo mencionas, sí.
  - [Choice]: Me gustaría comprar un billete.
    - **Player:** Me gustaría comprar un billete.
    - **Cart conductor:** ¿No ves que estoy teniendo un pequeño descanso?
    - **Player:** Ahora que lo mencionas, sí.
  - [Choice]: Tengo que irme.
    - **Player:** Me tengo que ir.
    - **Cart conductor:** Entonces, ¿por qué me hiciste perder el tiempo?

#### Pistas de fábrica de alto horno

- **Cart conductor:** ¡Fuera del camino, humano!
- **Player:** ¿Por qué? ¿Qué está pasando?
- **Cart conductor:** Hay tráfico importante por aquí y no quiero que ningún humano callejero me distraiga.
