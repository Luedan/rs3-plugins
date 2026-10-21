# Skulgrimen

- **Original Wiki Page**: [Transcript:Skulgrimen](https://runescape.wiki/w/Transcript%3ASkulgrimen)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before The Fremennik Trials


#### Hablando con él

- **Player:** ¡Hola!
- **Skulgrimen:**Lo siento. No puedo vender armas a los extranjeros. No estaría bien. Contra nuestras creencias.

#### Intercambiándolo

- Sólo los Fremenniks pueden comprar armas y armaduras aquí.

### After The Fremennik Trials

- ((Tener al menos un trozo de concha de roca, fragmento o astilla en el backpack:))
  - **¿Sobre qué te gustaría preguntar?**
    - Armadura Roca Crab
      - **Player:** Hola. Tengo estos fragmentos de caparazón de cangrejo de roca y creo que podrías convertirlos en una armadura para mí...
      - **Skulgrimen:** No hay problema, [Fremennik name]. ¿Qué armadura quieres?
      - **Seleccione una opción**
        - Un buen timón
          - **Skulgrimen:** Costará 5000 coins. ¿Está bien?
          - **Seleccione una opción**
            - SI
              - ((Si falta uno o más componentes requeridos:))
                - **Skulgrimen:** Lo siento. Necesitas 1 trozo de piel de boca de daga oscura, 1 trozo de concha de roca y 5000 coins para hacer tu casco. Vuelve cuando lo tengas.
                - (end)
              - (removes=1 rock-shell chunk, 1 dagannoth hide, and 5,000 coins) (receives=rock-shell helm)
              - **Skulgrimen:** Ahí lo tienes. Buen timón. ¿Quieres otro?
              - **Seleccione una opción**
                - SI
                  - (continuea|helm)
                - NO
                  - (continuea|armour)
        - Armadura resistente
          - **Skulgrimen:** Costará 10.000 coins. ¿Está bien?
          - **Seleccione una opción**
            - SI
              - ((Si falta uno o más componentes requeridos:))
                - **Skulgrimen:** Disculpas. Necesitas 3 piezas de piel de boca de daga oscura, 1 fragmento de concha de roca y 10 000 coins para hacerte una armadura fuerte. Vuelve cuando lo tengas.
                - (end)
              - (removes=1 rock-shell shard, 3 dagannoth hides, and 10,000 coins) (receives=rock-shell plate)
              - **Skulgrimen:** Ahí lo tienes. Armadura robusta. ¿Necesitas otra pieza?
              - **Seleccione una opción**
                - SI
                  - (continuea|body)
                - NO
                  - (continuea|armour)
        - Potente armadura para las piernas
          - **Skulgrimen:** Costará 7500 coins. ¿Está bien?
          - **Seleccione una opción**
            - SI
              - ((Si falta uno o más componentes requeridos:))
                - **Skulgrimen:** Disculpas. Necesitas 2 piezas de piel de boca de daga oscura, 1 astilla de concha de roca y 7500 coins para hacerte una armadura para las piernas. Vuelve cuando lo tengas.
                - (end)
              - (removes=1 rock-shell splinter, 2 dagannoth hides, and 7,500 coins) (receives=rock-shell legs)
              - **Skulgrimen:** Ahí lo tienes. Armadura robusta. ¿Necesitas otra pieza?
              - **Seleccione una opción**
                - SI
                  - (continuea|legs)
                - NO
                  - (continuea|armour)
            - NO
              - (continuea|armour)
        - nada
          - **Player:** En realidad, no quiero nada.
          - **Skulgrimen:** Como desees.
    - Los juicios de Fremennik
      - (continue)
- **Skulgrimen:** Hola de nuevo, [Fremennik name]. ¿Vienes a ver qué hay a la venta?
- ((Condición desconocida:))
  - **Elige una opción:**
    - Muéstrame lo que tienes.
      - (opens=Skulgrimen's Battle Gear)
    - ¿Puedo preguntarte sobre V?
      - **Skulgrimen:** Mantendremos vivas sus historias, al menos su leyenda vivirá para siempre.
      - (end)
- (opens=Skulgrimen's Battle Gear)
