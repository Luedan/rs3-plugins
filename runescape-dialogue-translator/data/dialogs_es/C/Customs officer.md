# Customs officer

- **Original Wiki Page**: [Transcript:Customs officer](https://runescape.wiki/w/Transcript%3ACustoms%20officer)
- **Letter**: `C`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue


#### Antes del tesoro de Pirate

- **Customs officer:** ¿Puedo ayudarte?
- [Menu]: Selecciona una opción
  - [Choice]: ¿Puedo viajar en este barco?
    - **Player:** ¿Puedo viajar en este barco?
    - **Customs officer:** Debes que te registren antes de poder abordar.
    - [Menu]: Selecciona una opción
      - [Choice]: ¿Por qué?
        - **Player:** ¿Por qué?
        - **Customs officer:** Porque Asgarnia ha prohibido la importación de bebidas espirituosas.
        - (otro)
      - [Choice]: Busca, no tengo nada que ocultar.
        - **Player:** Busca, no tengo nada que ocultar.
        - ''(Si tienes ron Karamjan en tu inventario:) {{anchor|aha}}
          - **Customs officer:** Ajá, ¿tratamos de contrabandear ron, verdad?
          - **Player:** {{anchor|personaluse}}Umm... ¿es para uso personal?
          - (removes=Karamjan rum)
          - El customs officer confisca tu ron.
        - ''(Si tienes ron Karamjan en tu inventario y llevas un ring of Charos (a):)
          - **Customs officer:** Ajá, ¿tratamos de contrabandear ron, verdad?
          - [Menu]: Selecciona una opción
            - [Choice]: Umm... ¿es para uso personal?
              - (above|personaluse)
            - [Choice]: [Charm] Este no es el ron Karamjan que estás buscando.
              - **Player:** Este no es el ron Karamjan que estás buscando.
              - **Customs officer:** Este no es el ron Karamjan que buscamos.
              - **Player:** ¡Bueno, eso fue fácil!
              - Bailas de alegría...
              - ...y dejar caer accidentalmente el ron.
              - (removes=Karamjan rum)
              - **Player:** Maldita sea...
        - ''(Si no tienes ron Karamjan en tu inventario:)
          - **Customs officer:** Bueno, tienes algunas cosas raras, pero todo es legal. Ahora deberás pagar una tasa de embarque de 30 coins.
          - [Menu]: Seleccione una opción {{anchor|30coins}}
            - [Choice]: Bien.
              - **Player:** Vale.
              - ''(Si el player no tiene suficiente dinero:)
                - **Player:** Dios mío, parece que no tengo suficiente dinero.
                - No puedes permitirte eso.
              - ''(Si el player se ha ganado guantes Karamja:)
                - **Customs officer:** Espera un segundo, ¿no te ganaste los guantes Karamja? Pensé que te había visto ayudando en la isla. Puedes comprar a mitad de precio, amigo.
                - Pagas 15 coins y abordas el barco.
              - ''(Sin guantes Karamja :)
                - Pagas 30 coins y abordas el barco.
              - (Action: La pantalla aparece y desaparece, el player llega a Port Sarim)
              - El barco llega a Port Sarim.
            - [Choice]: Oh, no me molestaré entonces.
              - **Player:** Oh, entonces no me molestaré.
            - [Choice]: (*Si lleva un ring of Charos (a):*) [Charm] ¿O quizás podrías dejarme viajar gratis?
              - **Player:** ¿O quizás podrías dejarme viajar gratis?
              - **Customs officer:** Sí, tal vez podría. Bien, sube a bordo entonces.
              - (Action: La pantalla aparece y desaparece, el player llega a Port Sarim)
              - El barco llega a Port Sarim.
      - [Choice]: ¡No vas a poner tus manos sobre mis cosas!
        - **Player:** ¡No pondrás tus manos sobre mis cosas!
        - **Customs officer:** Entonces no subirás a este barco.
  - [Choice]: ¿Tiene Karamja costumbres inusuales entonces?
    - **Player:** ¿Tiene Karamja costumbres inusuales entonces?
    - **Customs officer:** No soy ese tipo de customs officer.

#### Después del tesoro de Pirate

- **Customs officer:** ¿Puedo ayudarte?
- Seleccione una opción
  - [Choice]: ¿Puedo viajar en este barco?
    - **Player:** ¿Puedo viajar en este barco?
    - ''(Si no tienes ron Karamjan en tu inventario:)
      - **Customs officer:** Oye, te conozco, trabajas en la plantación.
      - **Customs officer:** No creo que intentes contrabandear nada, sólo tienes que pagar una tarifa de embarque de 30 coins.
      - (continuea|30coins)
    - ''(Si tienes ron Karamjan en tu inventario:)
      - **Customs officer:** Inspección puntual. ¿No te importa?
      - **Customs officer:** Ajá, ¿intentas contrabandear ron, eh?
      - (continuea|aha)
  - [Choice]: ¿Tiene Karamja costumbres inusuales entonces?
    - (arriba)

### Pay fare

- *(Si has completado las tareas fáciles de Karamja pero no tienes 15 coins :)*
  - No puedes permitirte eso.
  - No tienes suficiente coins para pagar el pasaje. Necesitas 15 coins ya que te has ganado los guantes Karamja.
- ''(Sin las tareas fáciles de Karamja y sin 30 coins :)
  - No puedes permitirte eso.
  - No tienes suficientes coins para pagar el pasaje, necesitas 30.
- *(Si has completado las tareas fáciles de Karamja:)*
  - La oficial sonríe al reconocer que te has ganado guantes Karamja y te deja pasar a mitad de precio: 15 coins.
- ''(Sin las tareas fáciles de Karamja :)
  - Pagas 30 coins y abordas el barco.
- ''(Con ron Karamjan en inventario:)
  - **Customs officer:** Inspección puntual. ¿No te importa?
  - **Customs officer:** Ajá, ¿intentas contrabandear ron, eh?
  - (continuea|aha)
