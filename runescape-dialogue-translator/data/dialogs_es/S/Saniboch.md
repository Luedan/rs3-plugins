# Saniboch

- **Original Wiki Page**: [Transcript:Saniboch](https://runescape.wiki/w/Transcript%3ASaniboch)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At Brimhaven Dungeon entrance


#### Intentando entrar sin pagar

- **Saniboch:** ¡No puedes entrar sin pagar!

#### Hablando con Saniboch

- **Saniboch:** Buenos días para ti, bwana.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Puedo pasar por esa puerta por favor?
    - **Player:** ¿Puedo pasar por esa puerta, por favor?
    - (Condition: Con el conjunto de tareas Karamja completado:)
      - **Saniboch:** Puedes participar gratis ya que has demostrado que eres amigo de Karamja.
    - (Condition: De lo contrario:)
      - **Saniboch:** Por supuesto, pero primero debo cobrarte la suma de 875 coins.
      - (Condition: Si no tienes suficiente dinero contigo:)
        - **Player:** No tengo el dinero encima en este momento.
        - **Saniboch:** Bueno, esta es una mazmorra para los aventureros más ricos y exigentes, vete con tu gentuza.
        - **Player:** Pero ni siquiera tienes ropa, ¿cómo puedes llamar en serio a alguien gentuza?
        - **Saniboch:** Humph.
      - (Condition: Si tienes suficiente dinero contigo:)
        - [Menu]: Selecciona una opción
          - [Choice]: Bien, aquí está 875 coins.
            - **Player:** Ok, aquí está 875 coins.
            - [Le das Saniboch 875 coins.]
            - Pagas Saniboch 875 coins.
            - (removes=875 coins)
            - **Saniboch:** Muchas gracias. Ahora puedes pasar la puerta. ¡Que tu muerte sea gloriosa!
          - [Choice]: No importa.
            - **Player:** No importa.
          - [Choice]: ¿Por qué vale la pena el costo de la entrada?
            - **Player:** ¿Por qué vale la pena el costo de la entrada?
            - **Saniboch:** Conduce a una enorme y temible mazmorra, poblada por gigantes y perros extraños. Los aventureros vienen de todas partes para explorar sus profundidades.
            - **Saniboch:** No sé qué hay más profundo en mí, porque mis habilidades de agilidad y corte de madera son inadecuadas, pero escucho hablar de peligros aún mayores en lo más profundo.
  - [Choice]: ¿A dónde conduce esta extraña entrada?
    - **Player:** ¿A dónde conduce esta extraña entrada?
    - **Saniboch:** A una enorme y temible mazmorra, poblada por gigantes y perros extraños. Los aventureros vienen de todas partes para explorar sus profundidades.
    - **Saniboch:** No sé qué hay más profundo en mí, porque mis habilidades de agilidad y corte de madera son inadecuadas.
  - [Choice]: Buen día para ti también.
    - **Player:** Buenos días para ti también.
  - [Choice]: Estoy impresionado, ese árbol está creciendo en ese cobertizo.
    - **Player:** Estoy impresionado, ese árbol está creciendo en ese cobertizo.
    - **Saniboch:** Mi empleador me dice que es un tipo de árbol poco común llamado árbol Fyburglars.

#### Pagar

- (Condition: Sin haber completado el conjunto de tareas difíciles de Karamja:)
  - [Le das Saniboch 875 coins.]
  - Pagas Saniboch 875 coins.
  - (removes=875 coins)
  - **Saniboch:** Muchas gracias. Ahora puedes pasar la puerta. ¡Que tu muerte sea gloriosa!
- (Condition: Con el conjunto de tareas Karamja completado:)
  - **Saniboch:** Puedes participar gratis ya que has demostrado que eres amigo de Karamja.
