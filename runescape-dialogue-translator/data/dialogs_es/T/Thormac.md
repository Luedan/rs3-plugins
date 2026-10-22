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
    - ((If you have't yet completed the Seers' Village Hard Tasks:))
      - **Thormac:** Sí, aunque los materiales te costarán 40.000 coins. ¿Qué tipo de staff querías encantador?
      - (continue)
    - ((If you have completed the Seers' Village Hard Tasks:))
      - **Thormac:** Sí. Normalmente te costaría 40.000 coins, pero, como te esforzaste en conocer la zona de los Videntes, te costará 27.000 coins. ¿Qué tipo de staff querías encantador?
      - (continue)
    - ((Thormac's battlestaff interface opens.))
    - ((After making a selection:))
      - ((If you don't have the selected battlestaff with you:))
        - No tienes el battlestaff correcto.
      - ((If you have the selected battlestaff with you:))
        - ((If you don't have sufficient money with you:))
          - Necesitas [27,000/40,000] coins para pagar Thormac.
        - ((If you have sufficient money with you:))
          - ((If money to be paid is in your money pouch:))
            - [27,000/40,000] coins se han eliminado de su bolsa de dinero.
            - (continue)
          - (removes=coins and the battlestaff) (receives=corresponding mystic battlestaff)
          - Thormac encanta tus bastones de batalla.
  - ((Only if you have an Armadyl battlestaff with you:))
    - ¿Podrías encantar mi Armadyl battlestaff?
      - **Player:** ¿Podrías encantar mi Armadyl battlestaff?
      - **Thormac:** No sé de dónde sacaste esto, pero ya tiene mucho poder místico fluyendo a través de él. No creo que pueda hacerlo más místico.
