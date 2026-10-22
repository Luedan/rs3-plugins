# Hajedy

- **Original Wiki Page**: [Transcript:Hajedy](https://runescape.wiki/w/Transcript%3AHajedy)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before Shilo Village

- **Hajedy:** Solíamos realizar viajes en carrito hasta Shilo Village en el sur de Karamja. Desde la invasión zombie hemos tenido que parar. Murieron demasiadas personas.

### After Shilo Village

- **Hajedy:** Te ofrezco un paseo en carrito hasta Shilo Village si estás interesado. Costará 10 gold coins.
- [Menu]: Selecciona una opción
  - [Choice]: Sí por favor. Me gustaría ir a Shilo Village.
    - {{anchor|pay-fare}} (removes=10 coins)
    - (Action: La pantalla desaparece y aparece. el player aparece en Shilo Village.)
    - Te subes al carrito y el conductor insta a Theh Orses a seguir. Emprendes un viaje agotador a través de la jungla hasta Shilo Village.
    - Te sientes cansado por el viaje, pero al menos no tuviste que caminar tanta distancia.
  - [Choice]: No, gracias.
    - **Player:** No, gracias.

#### Tarifa de pago

- (above|pay-fare)

### Treasure Trails

- **Hajedy:** Bien hecho.
- (removes=the old clue scroll (medium))
- ((If the trail continues:))
  - (receives=a new clue scroll (medium))
  - [¡Hajedy te ha dado otro pergamino de pistas!]
- ((If the trail ends:))
  - (receives=reward casket (medium))
  - [¡Has encontrado un ataúd!]
