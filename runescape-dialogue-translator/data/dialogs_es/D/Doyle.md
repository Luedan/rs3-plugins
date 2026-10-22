# Doyle

- **Original Wiki Page**: [Transcript:Doyle](https://runescape.wiki/w/Transcript%3ADoyle)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Antes de chicos y muñecas.

- **Doyle:** ¡Argh! Estoy demasiado asustado. Déjame en paz.

#### Durante chicos y muñecas

- (ver|Chicos y muñecos)

#### Después de completar Chicos y Muñecas

- **Player:** Hola, Doyle. Entonces, ¿cómo funciona esto del pedido de calabazas?
- (Condition: Without harvest list:)
  - (Condition: Without free backpack space:)
    - **Doyle:** Si estás aquí para ayudar, ¡haz algo de espacio y te daré la lista de pedidos más reciente de Dolly!
    - (continue)
  - (Condition: With free backpack space:)
    - (receives=harvest list)
    - **Doyle:** Oye, si estás aquí para ayudar, ¡aquí tienes el último pedido de Dolly para que lo completes!
    - (continue)
- **Doyle:** Todo lo que tienes que hacer es cosechar calabazas de los huertos frente a mí y depositarlas en el carro de cosecha que está aquí.
- **Doyle:** Puedes entregar partes del pedido sobre la marcha o esperar hasta que hayas cosechado todo el pedido.
- **Doyle:** ¡Obtendrás una buena experiencia cuando se complete el pedido y una bonificación si lo haces todo de una vez!
- **Player:** ¿Esos cuervos todavía te molestan?
- **Doyle:** Lo son: cada vez que se cosecha una calabaza, se abalanzan en busca de semillas. ¡Sus ojos son más grandes que sus barrigas!
- **Doyle:** Puedes ahuyentarlos con bastante facilidad, pero es un trabajo duro uno a la vez.
- **Doyle:** Puedo asustarlos a todos a la vez, pero cada vez que lo hago necesitaré un minuto para recuperarme.
- **Doyle:** Sin embargo, una vez que un cuervo ha sido ahuyentado de un huerto, crecerá una nueva calabaza en él. Entonces hay que hacerlo.
- **Player:** Suena bastante simple: cosecha calabazas, ahuyenta a los cuervos y completa el pedido de Dolly poniendo calabazas en el carrito de cosecha.
- **Player:** ¿Algo más que deba saber?
- **Doyle:** ¡Oh, sí! Hay un contenedor de abono en la esquina opuesta al carro de cosecha. Puedes tirar a la basura las calabazas que no quieras allí. Podría ayudar a hacer espacio para otros diferentes, o simplemente cuando hayas terminado el día.
- **Doyle:** Además, puedes obtener cosas aleatorias de Halloween mientras cosechas, pero obtendrás la experiencia principalmente al completar pedidos.
- (Condition: With "Talk to" as the default option:)
  - [También puedes configurar la opción de clic izquierdo de Doyle para que sea más fácil ahuyentar a todos los cuervos.]

### Scare all crows


#### Si el susto de Doyle no está en tiempo de reutilización

- {{Trandom}}
  - Doyle: ¡FUERA USTEDES, RATAS CON ALAS!
  - Doyle: ¡VAYAMOS, LOROS EMO!
  - Doyle: ¡MOLESA A ALGUIEN MÁS, Aspirantes A CUERVOS!
  - Doyle: ¡PIÉRDENSE, URRACAS HOMOCROMÁTICAS!
  - Doyle: ¡DÉJENNOS EN SOLA, PATOS MUCKY!
  - Doyle: ¡DEJEN DE COMER SEMILLAS, ALCANTOS!
  - Doyle: ¡LOS PÁJAROS TONTOS TIENEN QUE IRSE!

#### Si el susto de Doyle está en tiempo de reutilización

- **Doyle:** Dame un minuto para volver a mentalizarme...

### Configure

- [Menu]: Seleccione la opción de clic izquierdo
  - [Choice]: Habla con.
    - (Action: La primera opción en Doyle se convierte en "Hablar con".)
  - [Choice]: Asusta a todos los cuervos.
    - (Action: La primera opción en Doyle se convierte en "Asustar a todos los cuervos".)

### When Doyle is ready to scare more crows

- Doyle: ¡Estoy listo para asustar a más cuervos!
- (ventana emergente)
  - {{Popup|Doyle: I'm ready to scare more crows!|colour=#FF6600}}
