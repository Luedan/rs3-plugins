# Charos

- **Original Wiki Page**: [Transcript:Charos](https://runescape.wiki/w/Transcript%3ACharos)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### House in Varrock

- Elige una opción:
  - ¿Vives aquí?
    - **Charos:** Bueno, técnicamente. He adquirido este edificio, pero no creo que sea todavía mi "hogar". Rara vez me quedo en un lugar el tiempo suficiente para llamarlo hogar. Los hogares te atan y siempre intento ser un espíritu más libre. Normalmente encuentro a alguien dispuesto a dejarme quedarme en su lujosa finca. Te sorprendería lo generosos que pueden ser los solitarios.
    - (previous|charos-contract-options)
  - ¿Hasta algo interesante?
    - ((Antes de completar Medidas desesperadas:))
      - **Charos:** Acabo de regresar al continente por un minuto y luego regresaré con Thok para perseguir a Kerapac.
      - **Charos:** Nadie me engaña así y se sale con la suya. Nadie.
      - (previous|charos-contract-options)
    - ((Después de completar Medidas desesperadas:))
      - **Charos:** En este momento solo quiero asegurarme de que este edificio se mantenga unido. Puede que sea una choza bastante monótona, pero tiene sus propios pequeños encantos.
      - (previous|charos-contract-options)
  - ((Si está en un construction contract para Charos:))
    - Hablemos de tu contrato.
      - Seleccione una opción
        - ¿Qué necesitas reparar?
          - **Charos:** Déjame ver, ahora mismo necesito que repares el siguiente pieces of furniture. [Furniture], [Furniture], [Furniture], [Furniture], [Furniture]
          - (previous|charos-contract-information)
        - ¿Qué materiales necesito?
          - **Charos:** Honestamente, no tengo idea. Construction no es lo mío. Pero el estate agent sí dejó una nota... ¡Ahaa! Aquí está, aparentemente necesitarás: Planks x [número], Steel nails x [número].
          - (previous|charos-contract-information)
        - [Anterior]
          - (initial|charos-contract-options)
  - [salir]
    - (end)

### At Glacor Front


#### Habla con

- ((La primera vez:))
  - **Charos (Cañón de Hielo):** Ah, Player. Me alegro de verte por aquí.
  - **Charos (Frost Cannon):** Tienes una manera de aparecer cuando las cosas se ponen difíciles.
  - **Charos (Frost Cannon):** Sin embargo, si no hay nada urgente, volveré a probar este Arch-Glacor en nudos ilusorios.
  - (continue)
- ((Después de la primera vez:))
  - **Charos (Frost Cannon):** ¡Hola de nuevo!
  - (continue)
- **ELIGE UNA OPCIÓN:**
  - ¿Cuál es tu papel aquí?
    - **Charos (Frost Cannon):** Estoy aquí para realizar interferencias.
    - **Charos (Frost Cannon):** El Arch-Glacor tiene un ataque de lo más desagradable: un rayo de energía helada de, francamente, una magnitud ridícula.
    - **Charos (Frost Cannon):** Es tosco, pero frustrantemente inevitable. Y ha estado matando impunemente a nuestros guerreros altamente entrenados.
    - **Charos (Frost Cannon):** Puedo evitar que Arch-Glacor acumule el poder para usar ese ataque, con un cóctel embriagador de trucos interceptores e ilusiones desviadoras.
    - **Charos (Frost Cannon):** También he estado proyectando canciones de remo de Fremennik en su mente. Es muy difícil cambiarlos una vez que están alojados.
  - ((Solo con la mecánica Frost Cannon desactivada:))
    - Tómate un descanso. Puedo manejar esto.
      - **Charos (Frost Cannon):** ¡Ahhh, ya era hora! Mis pies me están matando y me estoy quedando sin melodías irritantes y pegadizas para tararear.
      - Si Charos deja de canalizar su hechizo, Arch-Glacor utilizará su ataque inevitable. Necesitarás mitigar su daño para sobrevivir. ¿Está seguro?
      - **SELECCIONA UNA OPCIÓN**
        - Sí, adelante.
          - **Charos (Frost Cannon):** Muy bien. Ten cuidado de no morir.
          - La mecánica 'Frost Cannon' ahora está activa.
          - El Arch-Glacor ahora utilizará su inevitable ataque con rayo de hielo. Habla con Charos nuevamente para desactivar la mecánica.
        - En realidad, ¡espera!
          - **Charos (Frost Cannon):** Molesta. No supongas que podrías traerme agua con gas con una rodaja de lima, ¿verdad?
  - ((Solo con la mecánica Frost Cannon activada:))
    - ¿Podrías empezar a bloquear ese enorme ataque de nuevo?
      - **Charos (Frost Cannon):** No hay descanso para los malvados, ¿eh? O, de hecho, el endiabladamente guapo.
      - La mecánica 'Frost Cannon' ha sido desactivada.
      - Charos ahora impide que Arch-Glacor use su inevitable rayo de hielo. Habla con él nuevamente si deseas volver a habilitar la mecánica.

#### Mecánico de palanca


##### Con Frost Cannon desactivado

- La mecánica 'Frost Cannon' ahora está activa.

##### Con Frost Cannon activado

- La mecánica 'Frost Cannon' ha sido desactivada.
