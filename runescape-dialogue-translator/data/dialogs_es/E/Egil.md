# Egil

- **Original Wiki Page**: [Transcript:Egil](https://runescape.wiki/w/Transcript%3AEgil)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|Dialogue for exchanging cannons and for unknown brackets of sword rating percentages}}

### Talk to

- **Egil:** Bienvenido al Taller de Artesanos. ¡Tenemos herrería normal en el frente y herrería funeraria en la parte trasera!
- **Egil:** Además, yo... mi primo de vez en cuando pasa por aquí y te entrega algunos planos de espada ceremoniales para que los completes y obtengas experiencia adicional.
- [Menu]: ¿Qué te gustaría decir?
  - [Choice]: ¿Qué es una espada ceremonial?
    - **Egil:** Una espada ceremonial distingue al portador de sus compañeros. Son artículos de belleza y artesanía preferidos por los oficiales y los muy ricos.
    - **Player:** ¿Supongo que son caros?
    - **Egil:** Así es. Utilizamos sólo el metal más puro para conseguir las espadas más maleables y perfectas. Cada hoja requiere una gran cantidad de mineral, que fundimos hasta obtener un metal puro y denso. ¡Pero si te damos algunos planos, te proporcionaremos todos los materiales para que puedas forjar libremente tu espada ceremonial!
    - (previous)
  - [Choice]: ¿Puedes mostrarme cómo hacer una espada ceremonial?
    - (Action: el player ingresa a una instancia del taller, donde se abre la interfaz de la espada ceremonial y comienza un tutorial.)
    - [Debes clavar la espada en el diseño de arriba.]
    - [Elija puntos a lo largo de la espada y golpéelos mientras se enfría. Una vez que la espada esté fría, ya no podrás usarla.]
    - (Action: Se realiza un golpe suave en la esquina superior derecha de la espada.)
    - [Hay diferentes puntos fuertes del "golpe".]
    - [pic=Martillo detail.png]
    - (Action: Se realiza un golpe fuerte en la esquina superior derecha de la espada.)
    - [pic=Martillo detail.png]
    - (Action: Se realiza un golpe medio en la esquina inferior derecha de la espada.)
    - [pic=Martillo detail.png]
    - (Action: Se realiza un golpe suave en la esquina inferior derecha de la espada.)
    - [pic=Martillo detail.png]
    - (Action: Se realiza un golpe cuidadoso en la esquina inferior derecha de la espada.)
    - [pic=Martillo detail.png]
    - **Egil:** Una vez que tu espada esté lo más cerca posible de los planos o se haya enfriado, habla conmigo.
    - (Action: Sten se acerca para enfrentar a Egil.)
    - **Egil:** Te recompensaré con experiencia adicional según lo cerca que te hayas mantenido del diseño.
    - (Action: La pantalla se vuelve negra y luego vuelve a aparecer; el player está de vuelta en el taller no instanciado.)
  - [Choice]: Can you rate my sword?|cond=Si el player tiene planos de espada ceremoniales en su backpack
    - (removes=the ceremonial sword plans)
    - ((Si la espada estuviera entre [unknown] y 99%:) <!-- lower bound is ≤ 88 -->
      - Tu espada recibe el [número]% de su experiencia potencial. Trabajo razonable.
    - ((For other ranges:))
      - {{Transcript missing}}
      - Tu espada recibe el [número]% de su experiencia potencial.
  - [Choice]: ¿Quién eres?
    - **Egil:** Soy Egil, especialista en espadas ceremoniales y, aparentemente, uno de los artesanos más veteranos del taller.
    - **Player:** ¿Aparentemente?
    - **Egil:** No tengo muchas acciones en títulos. Adornan el ego, pero son bastante poco prácticos.
    - (previous)
  - [Choice]: ¿Puedo cambiar mi cañón?
    - (Condition: If the player doesn't have a cannon:)
      - **Egil:** Me temo que no tienes ninguna mejora de cañón desbloqueada. Puedes desbloquear mejoras de cañones dorados y reales aquí en mi tienda, o diferentes actualizaciones a través de otros métodos que puedas descubrir en tus viajes.
      - (previous)
    - (Condition: Otherwise:)
      - [Menu]: Elige una opción:
        - [Choice]: Multicañón enano.
          - ((If the player did not bring their existing multicannon in their backpack:))
            - Debes traer un cañón múltiple dorado, real o de asedio para cambiarlo por un cañón múltiple enano normal.
            - **Egil:** ¡No me hagas perder el tiempo, no te daremos multicañones gratis! Necesitarás traer un cañón múltiple y lo convertiré.
            - (initial)
          - ((Otherwise:))
            - {{Transcript missing}}
        - [Choice]: Multicañón de oro.
          - ((If the player did not bring their existing multicannon in their backpack:))
            - Debes traer un cañón múltiple normal, real o de asedio para cambiarlo por un cañón múltiple enano dorado.
            - **Egil:** ¡No me hagas perder el tiempo, no te daremos multicañones gratis! Necesitarás traer un cañón múltiple y lo convertiré.
            - (initial)
          - ((Otherwise:))
            - {{Transcript missing}}
        - [Choice]: Royale multicannon.|cond=Si el player ha desbloqueado el cañón real:
          - ((If the player did not bring their existing multicannon in their backpack:))
            - Debes traer un cañón múltiple normal, dorado o de asedio para cambiarlo por un cañón múltiple enano real.
            - **Egil:** ¡No me hagas perder el tiempo, no te daremos multicañones gratis! Necesitarás traer un cañón múltiple y lo convertiré.
            - (initial)
          - ((Otherwise:))
            - {{Transcript missing}}
  - [Choice]: [More...]
    - [Menu]: ¿Qué te gustaría decir?
      - [Choice]: ¿Inyector de luminita?
        - **Player:** ¿Qué es un inyector de luminita?
        - **Egil:** Si lo activas en cualquier parte del taller, sobrecargará las tuberías dentro del taller, lo que hará que tú y todos los demás generen más progreso mientras forjan.
        - **Player:** Eso suena peligroso. ¿Cuánto dura?
        - **Egil:** ¡Ah, el taller puede soportarlo! Pero de vez en cuando podría reventar una tubería. Cada uno dura 5 minutos, pero puedes poner varios en cola para trabajar a la vez.
        - (Condition: If luminite injectors are active:)
          - **Egil:** De hecho, ¡hay uno activo ahora mismo! Caducará en [time given in minutes and seconds].
        - (initial)
      - [Choice]: ¿Hay alguna recompensa?
        - (opens=Artisans' Workshop Reward Shop)
      - [Choice]: Adiós.
        - (end)
      - [Choice]: [More...]
        - (initial)

### Rewards

- (opens=Artisans' Workshop Reward Shop)

### Change cannon

- (arriba2|cañón)
