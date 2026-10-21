# Civilian

- **Original Wiki Page**: [Transcript:Civilian](https://runescape.wiki/w/Transcript%3ACivilian)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### After Plague City, before Plague's End


#### Mientras no uses el equipo Mourner completo


##### Civilian #1 (pelo largo con pantalones verdes)

- **Player:** Hola.
- **Civilian:** Buenos días, viajero.
- **Player:** ¿Qué estás haciendo?
- **Civilian:** ¡Persiguiendo ratones como siempre! Es todo lo que parece hacer hoy en día.
- **Player:** ¿Debes perder mucho tiempo?
- **Civilian:** Sí, pero ¿qué puedes hacer? ¡No es que haya muchos gatos por aquí!
- (Condition: Con el Witch's cat en backpack:)
  - **Player:** Tengo un gato... ¡mira!
  - **Civilian:** Hmmm... no parece que haya visto la luz del día en años. ¡Eso no atrapará ningún ratón!
- (Condition: Con un gatito o gato seguidor, o en backpack:)
  - (continue|Cat sale dialogue)
- (Condition: De lo contrario:)
  - **Player:** No, tienes razón, no ves muchos por ahí.

##### Civilian #2 (calvo con la parte superior verde)

- **Player:** Hola.
- **Civilian:** Estoy un poco ocupado para hablar ahora, lo siento.
- **Player:** ¿Por qué? ¿Qué estás haciendo?
- **Civilian:** ¡Intentando matar a estos ratones! ¡Lo que realmente necesito es un gato!
- (Condition: Con el Witch's cat en backpack:)
  - (above|daylight)
- (Condition: Con un gatito o gato seguidor, o en backpack:)
  - (continue|Cat sale dialogue)
- (Condition: De lo contrario:)
  - (above|notmany)

##### Civilian #3 (cabello rubio con pantalón rojo)

- **Player:** Hola.
- **Civilian:** Oh, hola. Lo siento, estoy un poco agotado.
- **Player:** ¿Día ocupado?
- **Civilian:** ¡Oh, son esos ratones! ¡Están por todas partes! Lo que realmente necesito es un gato, pero hoy en día es difícil conseguirlos.
- (Condition: Con el Witch's cat en backpack:)
  - (above|daylight)
- (Condition: Con un gatito o gato seguidor, o en backpack:)
  - (continue|Cat sale dialogue)
- (Condition: De lo contrario:)
  - (above|notmany)

#### Mientras usas el equipo Mourner completo

- **Player:** Hola.
- **Civilian:** Si ustedes, los dolientes, realmente quieren ayudar, ¿por qué no hacen algo con estos ratones?

### After Plague's End


#### Mientras no uses el equipo Mourner completo


##### Civilian #1 (pelo largo con pantalones verdes)

- **Player:** Hola.
- **Civilian:** Buenos días para ti, [hero/heroine] de Ardougne.
- (continuea)

##### Civilian #2 (calvo con la parte superior verde)

- (arriba)

##### Civilian #3 (cabello rubio con pantalón rojo)

- (arriba)

#### Mientras usas el equipo Mourner completo

- **Player:** Hola.
- **Civilian:** Uf, un Mourner. Me alegra que Player finalmente te haya delatado.

### Cat sale dialogue

- [Menu]: Selecciona una opción
  - [Choice]: cond=With a kitten follower, or in backpack|Tengo un gatito que podría vender.
    - **Player:** Tengo un gatito que podría vender.
    - **Civilian:** De verdad, echemos un vistazo.
    - Presentas el gatito.
    - **Civilian:** ¡Ja!  La cosita no cazará ningún ratón. Necesito un gato adulto.
  - [Choice]: cond=With a cat follower, or in backpack|Tengo un gato que podría vender.
    - **Player:** Tengo un gato que podría vender.
    - **Civilian:** No lo dices. ¿Es eso todo?
    - **Player:** ¡Saluda a un verdadero asesino de ratones!
    - **Civilian:** Hmmm, nada mal, nada mal. Parece que es uno animado.
    - **Player:** Erm... más o menos...
    - **Civilian:** No tengo mucho dinero, ¡pero sí tengo estos!
    - [El campesino te muestra un saco de runas de muerte.]
    - (Condition: Sin los logros fáciles de Ardougne:)
      - **Civilian:** Los enanos nos los traen de la mina. Te diré una cosa, te daré 100 runas de muerte para el gato.
      - (continue)
    - (Condition: Con los sencillos logros de Ardougne:)
      - **Civilian:** Los enanos nos los traen de la mina. Te diré una cosa, como has estado explorando mucho alrededor de Ardougne, te daré 200 runas de muerte para el gato.
      - (continue)
    - [Menu]: Selecciona una opción
      - [Choice]: No, no me voy a despedir por eso.
        - **Player:** No, no me voy a despedir por eso.
        - **Civilian:** Bueno, ¡no te doy más!
      - [Choice]: Bien, entonces tienes un trato.
        - **Player:** Bien, entonces, tienes un trato.
        - **Civilian:** ¡Genial! Entrega el gato y te daré las runas.
  - [Choice]: No, no son fáciles de conseguir.
    - **Player:** No, no es fácil conseguirlos.

#### Usar un gato contra el civil

- (removes=cat) (receives=100 or 200 death runes)
- [Entregas el gato. Recibirás runas de muerte [100/200].]
- **Civilian:** Genial, ¡gracias por eso!
- **Player:** Está bien. Cuidarse.

#### Usar un gatito contra el civil

- **Civilian:** Ese gatito no es lo suficientemente grande; Vuelve cuando sea más grande.
