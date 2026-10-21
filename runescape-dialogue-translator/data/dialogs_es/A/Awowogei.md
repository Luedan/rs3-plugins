# Awowogei

- **Original Wiki Page**: [Transcript:Awowogei](https://runescape.wiki/w/Transcript%3AAwowogei)
- **Letter**: `A`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Transcript npc|Awowogei}}

### After Monkey Madness


#### Como un mono karamjan

- **Rey Awowogei:** Todavía estamos reflexionando sobre tu propuesta... Te avisaremos cuando tengamos una respuesta...

#### Como cualquier otro mono

- **Rey Awowogei:** Hola extraño, ¿qué puedo hacer por ti?
- **Player:** Sólo estoy explorando.
- **Rey Awowogei:** Bueno, extraño, siéntete libre de explorar mi reino todo el tiempo que quieras.

### After Recipe for Disaster

- **Rey Awowogei:** Hola de nuevo, ¿hago algo por ti?
- **Player:** En realidad no, solo entro para saludar.
- **Rey Awowogei:** Bueno, disfruta del.

### Chimp ice dialogue (After Do No Evil)


#### Si el player no tiene un hielo de chimpancé en el inventario

- **Rey Awowogei:** ¿Tienes más helados de chimpancé?
- **Player:** No por mi cuenta.
- **Rey Awowogei:** Bueno, tráeme un poco más, después de todo, solo me has traído [número].

#### Si el player tiene un hielo de chimpancé en el inventario

- **Rey Awowogei:** *Sniff sniff* ¿Eso es hielo de chimpancé?
- **Player:** Sí, Su Majestad.
- **Rey Awowogei:** Tráeme más y verás prosperar tu colonia.
- Awowogei se lo traga.
- (removes=chimp ice)
- (Condition: Si es la entrega número 5, 10 o 15:)
  - **Rey Awowogei:** Tu colonia me ha sido de gran utilidad. ¡Haré construir una estatua en la colonia para celebrar tu éxito!
- (Condition: Si es la entrega número 25:)
  - **Rey Awowogei:** Tu colonia ha demostrado ser un activo valioso y necesitará protección. Enviaré a mi élite para protegerte.
  - ¡Felicitaciones! Has completado: 'Ice Ice Chimpy': completa 25 entregas de hielo de chimpancé. (25/25)
- (Condition: De lo contrario:)
  - (Condition: Si la recompensa son runas de muerte:)
    - (receives=30 to 50 death runes)
    - **Rey Awowogei:** Toma estas runas de muerte para solucionar tus problemas.
  - (Condition: Si la recompensa son runas de sangre:)
    - (receives=30 to 50 blood runes)
    - **Rey Awowogei:** Toma estas runas de sangre para solucionar tus problemas.
  - (Condition: Si la recompensa es un plátano:)
    - (receives=banana)
    - **Rey Awowogei:** Toma este plátano para solucionar tus problemas.
  - (Condition: Si la recompensa es un dragon scimitar:)
    - (receives=dragon scimitar)
    - **Rey Awowogei:** Toma este scimitar para solucionar tus problemas.

### Sandy Clue Scroll (historical)

- ((Sin espacio en backpack para ataúd:))
  - Necesitas más espacio en el inventario para recibir tu cofre de pistas.
- ((Con espacio en backpack:))
  - (removes=Sandy Clue Scroll and banana)
  - (Condition: Si el rastro continúa:)
    - (receives=Sandy Scroll box)
    - {{tbox|pic=Sandy Scroll box detail.png|You hand Awowogei a banana and he hands you a {{Sic|scrollbox}}... en silencio.}}
  - (Condition: Si el sendero termina:)
    - (receives=Sandy Casket and Sandy Casket (red))
    - {{tbox|pic=Sandy Casket detail.png|pic2=Sandy Casket (red) detail.png|You hand Awowogei a banana and he hands you a casket... silently.}}
