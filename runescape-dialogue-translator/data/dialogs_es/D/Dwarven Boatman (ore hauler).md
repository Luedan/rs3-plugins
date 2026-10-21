# Dwarven Boatman (ore hauler)

- **Original Wiki Page**: [Transcript:Dwarven Boatman (ore hauler)](https://runescape.wiki/w/Transcript%3ADwarven%20Boatman%20%28ore%20hauler%29)
- **Letter**: `D`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### First conversation

- **Player:** Hola. No creo haberte visto aquí antes.
- **Dwarven Boatman:** Oh, Dondakan me contrató recientemente. Necesita un barco para llevar todo su oro a la ciudad.
- **Player:** ¿La ciudad? ¿Puedes llevarme allí?
- **Dwarven Boatman:** Sólo hay espacio en mi barco para dos cosas... yo y el oro. Pero si quieres, puedo llevar tu mineral de oro a la ciudad y llevarlo al banco.
- **Player:** ¡Es un buen servicio! ¿Me costará algo?
- **Dwarven Boatman:** Sólo un poquito. Una pieza de mineral de oro por cada envío, y una pieza de mineral de oro por cada cinco piezas de mineral además de eso.
- **Player:** Entonces... si tuviera diez piezas de mineral, ¿cuánto tomarías?
- **Dwarven Boatman:** Serían tres piezas. Uno para el envío, dos para la carga. Siete piezas irían a tu cuenta bancaria. Entonces, ¿estás interesado?
  - *Si el player tiene exactamente un mineral de oro con ellos:*
    - (continue|anchor-one)
  - *Si el player tiene dos o más minerales de oro con ellos:*
    - (continue|anchor-two)
  - *Si el player no tiene ningún mineral de oro consigo:*
    - (continue|anchor-none)

### Subsequent conversations:

- **Dwarven Boatman:** ¿Tienes algún mineral de oro que quieras que lleve al banco de la ciudad?
- *Si el player tiene exactamente un mineral de oro con ellos: {{anchor|anchor-one}}*
  - **Player:** Bueno, tengo este pedazo de mineral...
  - **Dwarven Boatman:** Me temo que eso no te serviría de mucho. Mi tarifa mínima es una pieza de mineral de oro, no te quedaría nada.
- *Si el player tiene dos o más minerales de oro con ellos: {{anchor|anchor-two}}*
  - Seleccione una opción
    - Sí, por favor lleva mi oro a la ciudad.
      - **Player:** Sí, por favor lleva mi oro a la ciudad. Tengo [número] piezas de mineral aquí mismo.
      - **Dwarven Boatman:** Veamos, si llevo eso al banco por ti, me quedaría con [número] y llevaría [número] al banco por ti. ¿Suena justo?
      - Seleccione una opción
        - Sí.
          - **Player:** Sí, lo es.
          - **Dwarven Boatman:** ¡Excelente, ha sido bueno hacer negocios contigo! Los llevaré a la ciudad con mi próximo envío.
          - (Action: El Dwarven Boatman se lleva el oro de el player.)
        - No.
          - **Player:** No, eso es demasiado caro para mí.
    - No, me quedaré con esto yo mismo.
      - **Player:** No, me quedaré con estos yo mismo.
    - *Si el player tiene un Ring of charos (a) equipado:*
      - [Charm] Todo parece un poco caro, la verdad.
        - **Player:** Todo parece un poco caro, la verdad.
        - **Dwarven Boatman:** No lo sé... es solo lo que me dijo Dondakan, si alguien quisiera que le enviara su oro.
        - **Player:** Ahora hay mucho oro saliendo de esa roca, ¿seguramente puedes bajar un poco el precio?
        - **Dwarven Boatman:** Muy bien. Te diré una cosa, solo me quedaré con [número] y llevaré minerales [número] al banco para ti. ¿Trato?
        - Seleccione una opción
          - Sí.
            - **Player:** Sí, muy apreciado.
            - **Dwarven Boatman:** ¡Excelente, ha sido bueno hacer negocios contigo!
            - (Action: El Dwarven Boatman se lleva el oro de el player.)
          - No.
            - **Player:** No, me los quedaré yo mismo, gracias.
- *Si el player no tiene ningún mineral de oro con ellos:{{anchor|anchor-none}}*
  - **Player:** Me temo que no tengo ninguno.
