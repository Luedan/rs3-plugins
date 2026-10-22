# Chamber guardian

- **Original Wiki Page**: [Transcript:Chamber guardian](https://runescape.wiki/w/Transcript%3AChamber%20guardian)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Mage Arena


#### Antes de rezar ante una estatua

- **Player:** Hola amigo, Kolodion me envió.
- **Chamber guardian:** Sssshhh... los dioses están hablando. Puedo escuchar sus susurros.
- **Chamber guardian:** ¿Puedes oírlos aventurero? Te están llamando.
- **Player:** Erm... ¡vale!
- **Chamber guardian:** Ve a cantar ante la estatua del dios que más deseas representar en este mundo, serás recompensado.
- **Chamber guardian:** Una vez que hayas terminado, vuelve conmigo. Te proporcionaré un mago staff listo para la batalla.

##### Intentando cambiarlo antes de reclamar el staff gratis

- El guardián está profundamente concentrado.

#### Después de rezar ante una estatua, sin la capa en backpack

- **Player:** Hola.
- **Chamber guardian:** Hola aventurero, ¿has hecho tu elección?
- **Player:** Lo he hecho.
- **Chamber guardian:** Bien, bien, espero que hayas elegido bien. ¿Has sido recompensado con una capa de tu dios elegido?
- **Player:** Me temo que no lo tengo conmigo.
- **Chamber guardian:** Una vez que tengas tu capa, regresa conmigo y te proporcionaré un mago staff listo para la batalla.

#### Después de rezar ante una estatua, con la capa en backpack

- **Player:** Hola.
- **Chamber guardian:** Hola aventurero, ¿has hecho tu elección?
- **Player:** Lo he hecho.
- **Chamber guardian:** Bien, bien, espero que hayas elegido bien. Ahora les presentaré un staff mágico. Esto, junto con la capa que te otorgó el dios elegido, son todas las armas y armaduras que necesitarás aquí.
- (Condition: If the player prayed to Saradomin:)
  - (receives=Saradomin staff)
  - [El guardián te entrega un staff mágico adornado.]
  - (continue)
- (Condition: If the player prayed to Guthix:)
  - (receives=Guthix staff)
  - [El guardián te entrega un staff mágico adornado.]
  - (continue)
- (Condition: If the player prayed to Zamorak:)
  - (receives=Zamorak staff)
  - [El guardián te entrega un staff mágico adornado.]
  - (continue)
- {{RSFontAchievement|Mage Arena|Defeat Kolodion at the Mage Arena and collect a god staff.}}

#### Después de reclamar el staff gratis

- **Player:** Hola de nuevo.
- **Chamber guardian:** Hola aventurero, ¿estás buscando otro staff?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué tienes para ofrecer?
    - (opens=Mage Arena Staves)
  - [Choice]: No gracias.
    - **Player:** No, gracias.
    - **Chamber guardian:** Bueno, avísame si necesitas uno.
