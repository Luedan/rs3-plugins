# Farmer Blinkin

- **Original Wiki Page**: [Transcript:Farmer Blinkin](https://runescape.wiki/w/Transcript%3AFarmer%20Blinkin)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

- **Farmer Blinkin:** '¡Hola! Bienvenido a la granja de Winkin. ¿Qué puedo hacer por ti?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué es este lugar?
    - **Player:** ¿Qué es este lugar?
    - **Farmer Blinkin:** ¡Ja! Ya te lo dije, es Winkin's Farm. Aquí es donde cultivamos las mágicas raíces de ogle para el resto del mundo.
    - **Player:** Entonces, ¿qué puedo hacer aquí?
    - **Farmer Blinkin:** Puedes mejorar tu habilidad Farming obteniendo algunas banderas mías o de Mrs. Winkin, adentro. Luego, dirígete a los campos y marca dónde crees que se plantan plantas.
    - **Player:** ¿Es eso todo?
    - **Farmer Blinkin:** ¡Para nada! Hay más. Cuando hayas colocado banderas de yar, los granjeros las recogerán y te darán puntos. Puedes canjear estos puntos por semillas o experiencia en la tienda del interior.
    - **Player:** ¡Está bien, eso suena genial! Entonces empezaré a plantar.
    - **Farmer Blinkin:** Sí, pero ten cuidado donde plantas las banderas. Si no hay ninguna planta bajo la bandera de yar, el granjero se la quedará y le costará un centavo comprar más.
    - **Player:** Ya veo. Gracias por la ayuda.
    - **Farmer Blinkin:** Adiós, por ahora. Si tengo que decir 'bandera' una vez más, os lo digo...
  - [Choice]: ¿Tienes alguna bandera?
    - **Player:** ¿Tienes alguna bandera?
    - **Farmer Blinkin:** Déjame comprobarlo.
    - (Condition: If it is the first time:)
      - **Farmer Blinkin:** Arr, un nuevo, ¿eh? Sí, siempre es bueno ver una cara nueva por estos lares. Ahora, normalmente cobramos por las banderas, ya que muchas se pierden, pero puedes configurar la primera de forma gratuita.
      - **Player:** ¡Vaya, gracias!
      - **Farmer Blinkin:** Ahora, recuerda: si plantas las banderas en cualquier lugar antiguo que no tenga semillas, perderás tu bandera, y no es barato comprármelas a mí o a Mrs. Winkin. De todos modos, aquí está tu primer lote.
      - (receives=10 flags)
      - **Player:** ¡Muchas gracias! Entonces me voy.
      - **Farmer Blinkin:** Adiós.
    - (Condition: If the player can claim free flags:)
      - **Farmer Blinkin:** ¡Ah! Lo primero es lo primero. Uno de los muchachos de la granja te dejó algunas banderas. Puedes recuperarlos. Aquí tienes.
    - (Condition: If the player can buy flags:)
      - **Farmer Blinkin:** Righty-ho! Puedes tener un total de 10 banderas. Conseguir un juego completo de banderas te costará [número] piezas de oro. ¿Te gustaría comprar estas banderas?
      - [Menu]: Selecciona una opción
        - [Choice]: Sí, por favor.
          - **Player:** Sí, por favor.
          - [número] coins se han eliminado de su bolsa de dinero.
          - **Farmer Blinkin:** Aquí tienes, entonces.
        - [Choice]: No, gracias.
          - **Player:** No, gracias.
          - **Farmer Blinkin:** ¡Así es! Nos vemos.
    - (Condition: If the player has 10 flags (either before talking to Farmer Blinkin or by claiming/buying flags):)
      - **Farmer Blinkin:** Parece que ya tienes todas las banderas que necesitas ahora. No necesitas comprar más.
  - [Choice]: ¿Dónde está el señor Winkin?
    - **Player:** ¿Dónde está el Sr. Winkin?
    - **Farmer Blinkin:** ¿Granjero Winkin? Bueno, lo último que oí es que iba al mercado con una nueva carga de Ogleroots.
    - **Player:** ¿Ogleroots?
    - **Farmer Blinkin:** ¡Sí! Los hacemos crecer mucho aquí en el corral. Los desenterramos y los vendemos a muchos.
    - **Player:** ¿Mi suerte?
    - **Farmer Blinkin:** ¡Sí! Humanos.
    - **Player:** Ah, ya veo. ¡Gracias!
    - **Farmer Blinkin:** ¡Adiós!
