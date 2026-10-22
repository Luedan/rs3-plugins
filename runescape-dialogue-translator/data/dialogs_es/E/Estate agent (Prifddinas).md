# Estate agent (Prifddinas)

- **Original Wiki Page**: [Transcript:Estate agent (Prifddinas)](https://runescape.wiki/w/Transcript%3AEstate%20agent%20%28Prifddinas%29)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Antes de completar No hay lugar como el hogar...

- **Estate agent:** Si lo que buscas es una casa, querrás dirigirte a Rimmington y charlar con estate agent allí.

#### Después de completar No hay lugar como el hogar...

- {{Transcript missing}}

### Redecorate


#### Antes de completar No hay lugar como el hogar...

- **Estate agent:** Si lo que buscas es una casa, querrás dirigirte a Rimmington y charlar con estate agent allí.

#### Después de completar No hay lugar como el hogar...

- {{Transcript missing}}

### Contracts

- [Menu]: Elige una opción:
  - [Choice]: cond=Without a contract|Quiero un nuevo contrato.
    - (Condition: Without free backpack space:)
      - **Estate agent:** Necesitará algo de espacio en su backpack para un contrato.
    - (Condition: With free backpack space:)
      - (receives=Construction contract)
      - Te entregan un Construction contract.
      - **Estate agent:** Aquí tienes, esto acaba de llegar para [character] en [location].
      - **Player:** ¡Gracias! Veré qué puedo hacer.
  - [Choice]: cond=With a contract|¿Cuál es mi contrato actual?
    - **Estate agent:** Parece que estás ayudando a [character] en [location].
    - (Condition: If the Construction contract has been lost:)
      - (Condition: Without free backpack space:)
        - **Estate agent:** Necesitará algo de espacio en su backpack para un contrato.
      - (Condition: With free backpack space:)
        - (receives=Construction contract)
        - Te entregan un Construction contract.
  - [Choice]: Háblame de contracts
    - **Estate agent:** Hay muchos propietarios alrededor de Gielinor que tienen dificultades para mantenerse al día con las reparaciones de forma regular.
    - **Estate agent:** Ahora mismo existe una oportunidad de mercado para poner en práctica sus habilidades de construcción y ayudarlos.
    - **Estate agent:** Nosotros, los agentes inmobiliarios, podemos proporcionarle un contrato. Este contrato le indicará quién necesita ayuda y qué necesita reparación.
    - **Estate agent:** Todo lo que necesitas hacer es ir y reparar todos los furniture rotos.
    - **Estate agent:** Puedes utilizar materiales básicos para un trabajo de reparación más económico pero más lento. O puede utilizar materiales más caros para una devolución más rápida y más experiencia.
    - **Estate agent:** Elijas lo que elijas, obtendrás una gran cantidad de experiencia una vez que hayas reparado todos los pieces of furniture que necesitan reparación.
    - **Estate agent:** También te recompensaremos con créditos de contrato, que puedes canjear desde cualquier estate agent por recompensas variadas.
    - (previous|Contracts)
  - [Choice]: cond=If the player has lost their plank box|He perdido mi caja de tablones.
    - **Player:** He perdido mi caja de tablones.
    - **Estate agent:** No te preocupes, tengo otro por ahí.
    - (Condition: Without free backpack space:)
      - **Estate agent:** Vuelve cuando tengas algo de espacio libre en tu backpack.
    - (Condition: With free backpack space:)
      - (receives=plank box)
      - **Estate agent:** Pero intenta no perder este.
  - [Choice]: ¿Tienes algo que pueda comprar?
    - (opens=Estate Agents Shop)
  - [Choice]: [Leave]
    - (end)

### Shop

- (opens=Estate Agents Shop)
