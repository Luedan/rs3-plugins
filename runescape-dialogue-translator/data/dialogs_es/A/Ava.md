# Ava

- **Original Wiki Page**: [Transcript:Ava](https://runescape.wiki/w/Transcript%3AAva)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Animal Magnetism


#### Hablando con ella

- *(Ver Transcripción: Magnetismo Animal)*

#### Opción comercial

- **Ava:** Hola, estoy ocupado con mi investigación. Vuelve en un momento, ¿podrías?

#### Comprar opción de dispositivo

- **Ava:** Lo siento, no puedo venderte ninguno de mis experimentos en este momento.

### After Animal Magnetism


#### Habla con

- **Ava:** Hola de nuevo; Estoy ocupado con mi investigación más reciente, así que no puedo chismorrear demasiado. ¿Busca información, una actualización, otro dispositivo o le gustaría ver mis productos a la venta?
- Seleccione una opción
  - Quisiera información por favor.
    - **Player:** Me gustaría información, por favor.
    - **Ava:** Sólo unos pocos datos antes de huir y perseguir cangrejos de roca o vacas.
    - **Ava:** En primer lugar, tu nuevo dispositivo no funcionará si llevas determinadas protecciones metálicas en el pecho.
    - **Ava:** La atracción magnética requerida para el funcionamiento provocaría retroalimentación, por lo que el dispositivo no permite equipar elementos incompatibles.
    - **Ava:** En segundo lugar, aunque el dispositivo está calibrado para atraer solo puntas de flecha, existe la posibilidad de que otros elementos magnéticamente activos sean atraídos.
    - **Ava:** La función de recuperación de flechas de los dispositivos es ligeramente diferente y se basa en un vínculo armónico entre las flechas y el imán del pollo. Por lo tanto, sólo recuperarás las flechas que hayas disparado tú y no las disparadas por personas cercanas.
    - **Ava:** También tendrás que moverte si quieres recolectar flechas, ya que la recolección de puntas de flecha perdidas hace mucho tiempo no funciona de otra manera.
    - **Ava:** Finalmente, el dispositivo solo funcionará cuando esté usado. Se desactiva automáticamente en otras circunstancias.
    - **Ava:** Me preocupaba lo que sucedería si lo colocaras en un banco en su estado activo, así que me aseguré de que solo funcione cuando lo tienes sobre tu espalda.
  - Parece que necesito un nuevo dispositivo.
    - **Player:** Necesito otro dispositivo para atraer flechas, por favor.
    - **Ava:** Bueno, por suerte para ti, tienen la costumbre de devolvérmelos cuando la gente los pierde, así que tengo algunos de repuesto. Parece que son gallinas perseguidoras.
    - **Ava:** Sin embargo, necesitaré 999 po para los gastos que implica devolverle la salud, la enfermedad o lo que sea a la pobre criatura.
    - **Player:** ¿Por qué 999?
    - **Ava:** Bueno, suena menos costoso que 1000. ¿Quieres ese reemplazo o no?
    - Seleccione una opción
      - Me parece bien.
        - **Player:** Me parece bien.
        - *Si el player tiene más de 999 po*
          - **Ava:** Aquí está tu dispositivo; Cuida bien tu pollo.
        - *Si el player tiene menos de 999 po*
          - **Ava:** Parece que no tienes suficiente dinero en efectivo; Aunque siempre puedes vender parte de tu equipo.
      - En realidad, preferiría no hacerlo.
        - **Player:** Preferiría no hacerlo, en realidad.
        - **Ava:** Tengo mejores cosas que hacer que irritarme contigo.
  - Me gustaría actualizar mi dispositivo, por favor.
    - **Player:** Me gustaría actualizar mi dispositivo, por favor.
    - *Si el player no tiene ningún dispositivo actualizable.*
      - **Ava:** Me temo que no tienes ningún dispositivo en tus maletas que pueda actualizar.
    - *Si el player tiene el atractor de Ava y 50 flechas de alcance, pero no 75 flechas de acero*
      - **Ava:** Me temo que necesito 75 flechas de acero para el proceso de actualización.
    - *Si el player tiene el atractor de Ava y 50 flechas a distancia y 75 flechas de acero*
      - **Ava:** Estás listo para actualizar. Tomaré 75 flechas de acero y el dispositivo viejo, si te parece bien.
      - Seleccione una opción
        - Me parece bien.
          - **Player:** Me parece bien.
          - **Ava:** Aquí está tu dispositivo actualizado; cuídalo bien.
        - En realidad, preferiría no hacerlo.
          - **Player:** Preferiría no hacerlo, en realidad.
          - **Ava:** Tengo mejores cosas que hacer que irritarme contigo.
  - Me gustaría ver tus cosas a la venta, por favor.
    - **Player:** Me gustaría ver tus cosas a la venta, por favor.
    - **Ava:** Aquí está mi tienda.
    - *(opens Ava's odds and ends store)*
  - Creo que simplemente me iré.
    - **Player:** Creo que simplemente me iré.
    - **Ava:** Gracias por la ayuda con mi cama; Nos vemos de nuevo.

#### Comprar dispositivo

- [Menu]: Me gustaría comprar:
  - [Choice]: el atractor
    - [Choice]: Sin 999 coins:
      - **Ava:** No dirijo una organización benéfica. Necesitas al menos 999 coins para comprar un nuevo atractor.
    - [Choice]: Con 999 coins:
      - (removes=999 coins)
      - (receives=Ava's attractor)
      - Se han eliminado 999 coins de su bolsa de dinero.
      - Compras un atractor nuevo por 999 coins.
  - [Choice]: el acumulador
    - (Condition: Sin 75 flechas de acero y 999 coins:)
      - **Ava:** No dirijo una organización benéfica. Necesitas al menos 999 coins y 75 flechas de acero para comprar un acumulador nuevo.
    - (Condition: Con 75 flechas de acero y 999 coins:)
      - (removes=999 coins and 75 steel arrows)
      - (receives=Ava's accumulator)
      - Se han eliminado 999 coins de su bolsa de dinero.
      - Compras un acumulador nuevo por 999 coins y 75 flechas.
  - [Choice]: The alerter|cond=Después de completar No hacer el mal
    - (Condition: Sin 75 flechas de acero y 999 coins:)
      - **Ava:** No dirijo una organización benéfica. Necesitas al menos 999 coins y 75 flechas de acero para comprar una nueva alerta.
    - (Condition: Con 75 flechas de acero y 999 coins:)
      - (removes=999 coins and 75 steel arrows)
      - (receives=Ava's alerter)
      - Se han eliminado 999 coins de su bolsa de dinero.
      - Compras un nuevo alertador por 999 coins y 75 flechas.

### Wearing the chicken outfit


#### Habla con

- **Ava:** ¿Qué llevas puesto en Gielinor?
- **Player:** Es mi traje de gallina. Salvé la Pascua y me la dieron como recompensa.
- **Ava:** No estás impresionando a nadie caminando así. ¿Por qué no vas...cruzas una calle o algo así?
