# Thormac

- **Original Wiki Page**: [Transcript:Thormac](https://runescape.wiki/w/Transcript%3AThormac)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### After Scorpion Catcher

- **Thormac:** Gracias por rescatar a mis escorpiones.
- **SELECCIONA UNA OPCIÓN**
  - Está bien.
    - **Player:** Está bien.
  - Dijiste que encantarías mi battlestaff para mí.
    - **Player:** Dijiste que encantarías mi battlestaff para mí.
    - ((Si aún no ha completado las tareas difíciles de Seers' Village:))
      - **Thormac:** Sí, aunque los materiales te costarán 40.000 coins. ¿Qué tipo de staff querías encantador?
      - (continue)
    - ((Si ha completado las tareas difíciles de Seers' Village:))
      - **Thormac:** Sí. Normalmente te costaría 40.000 coins, pero, como te esforzaste en conocer la zona de los Videntes, te costará 27.000 coins. ¿Qué tipo de staff querías encantador?
      - (continue)
    - ((Se abre la interfaz battlestaff de Thormac.))
    - ((Después de hacer una selección:))
      - ((Si no tienes el battlestaff seleccionado contigo:))
        - No tienes el battlestaff correcto.
      - ((Si tienes el battlestaff seleccionado contigo:))
        - ((Si no tienes suficiente dinero contigo:))
          - Necesitas [27,000/40,000] coins para pagar Thormac.
        - ((Si tienes suficiente dinero contigo:))
          - ((Si el dinero a pagar está en su bolsa de dinero:))
            - [27,000/40,000] coins se han eliminado de su bolsa de dinero.
            - (continue)
          - (removes=coins and the battlestaff) (receives=corresponding mystic battlestaff)
          - Thormac encanta tus bastones de batalla.
  - ((Sólo si tienes un Armadyl battlestaff contigo:))
    - ¿Podrías encantar mi Armadyl battlestaff?
      - **Player:** ¿Podrías encantar mi Armadyl battlestaff?
      - **Thormac:** No sé de dónde sacaste esto, pero ya tiene mucho poder místico fluyendo a través de él. No creo que pueda hacerlo más místico.
