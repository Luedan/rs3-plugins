# Trader Crewmember

- **Original Wiki Page**: [Transcript:Trader Crewmember](https://runescape.wiki/w/Transcript%3ATrader%20Crewmember)
- **Letter**: `T`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue

- **Trader Crewmember:** ¿Puedo ayudarte?
- [Menu]: Elige una opción:
  - [Choice]: Sí, ¿quién eres?
    - **Player:** Sí, ¿quién eres?
    - **Trader Crewmember:** Soy uno de los miembros del equipo de Trader Stan; Todos somos parte de la flota más grande de buques mercantes y de vela que jamás haya navegado por los siete mares.
    - **Trader Crewmember:** Si quieres llegar a un puerto rápidamente, puedes alquilar uno de nuestros barcos para que te lleve allí, si el precio es correcto...
    - **Player:** Entonces, ¿adónde puedo ir exactamente con sus barcos?
    - **Trader Crewmember:** Llevamos barcos desde Port Phasmatys hasta Port Tyras, parando en Port Sarim, Catherby, Brimhaven, Karamja, el Astillero, Oo'glog y Port Khazard.
    - **Trader Crewmember:** Quizás también atraquemos en Mos Le'Harmless de vez en cuando, si entiendes lo que quiero decir...
    - **Player:** Vaya, son muchos puertos. ¿Supongo que tienes algunas cosas exóticas para intercambiar?
    - **Trader Crewmember:** ¡Por supuesto que sí! Tenemos acceso a artículos comprados y vendidos en todo el mundo.
    - **Trader Crewmember:** ¿Te gustaría echar un vistazo?
    - [Menu]: Selecciona una opción
      - [Choice]: si
        - **Player:** Sí.
        - (opens=Trader Stan's Trading Post)
      - [Choice]: No
        - **Player:** No.
        - **Trader Crewmember:** Bueno, está bien. ¿Te gustaría alquilar un barco?
        - [Menu]: Selecciona una opción
          - [Choice]: Sí, me gustaría alquilar un barco.
            - (below|charter)
          - [Choice]: No.
            - (end)
      - [Choice]: ¿No es complicado navegar con esa ropa?
        - **Player:** ¿No es complicado navegar con esa ropa?
        - **Trader Crewmember:** ¿Difícil? ¡Complicado!
        - **Trader Crewmember:** Con todo crédito, Trader Stan es un gran empleador, pero insiste en que usemos lo último en alta costura incluso cuando navegamos.
        - **Trader Crewmember:** ¿Tienes la más mínima idea de lo complicado que es navegar con este material?
        - **Trader Crewmember:** Algunos de nosotros intentamos rasgarlo y argumentamos que era demasiado frágil para usarlo en un barco, pero él simplemente lo había encantado para volver a coserlo solo.
        - **Trader Crewmember:** Es difícil odiarlo cuando sabemos cuánto gasta en este equipo, pero si me caigo por la borda debido a este atuendo una vez más, lo dejaré.
        - **Player:** Vaya, eso es un poco duro.
  - [Choice]: Habla de barcos chárter. {{anchor|charter}}
    - (Condition: Si el player tiene la confirmación desactivada:)
      - [Menu]: Elige una opción:
        - [Choice]: Alquilar un barco
          - (abajo)
        - [Choice]: Confirmar pagos
          - **Player:** ¿Podrías avisarme de nuevo antes de viajar en tus barcos chárter?
          - **Trader Crewmember:** Ciertamente Player, le he informado al resto de tripulantes para comprobar que estás seguro de que quieres viajar en el futuro.
          - **Trader Crewmember:** ¿Hubo algo más?
          - **Player:** Sí, me gustaría alquilar un barco.
          - **Trader Crewmember:** Por supuesto señor, ¿adónde le gustaría ir?
          - ((Se abre la interfaz de destino de Charter Ship.))
    - (Condition: De lo contrario:)
      - **Player:** Sí, me gustaría alquilar un barco.
      - **Trader Crewmember:** Por supuesto [sir/madam], ¿adónde te gustaría ir?
      - (Condition: Si el player tiene sábana:)
        - **Trader Crewmember:** Lo sentimos, somos un barco de lavandería, tendrás que dejar esas sábanas sucias.
        - **Player:** ¿Me dejarías traerlo si te dijera que es una manta de seguridad?
        - **Trader Crewmember:** No, entonces simplemente nos burlaríamos de ti.
        - **Player:** Ah, ya veo.
      - (Condition: Si el player tiene una sábana cubierta de baba:)
        - **Trader Crewmember:** ¿Esa tu sábana está cubierta de baba sucia?
        - **Player:** Puedo decir con toda honestidad que no lo es.
        - **Trader Crewmember:** Bueno, a quien pertenezca, ¡no vendrá en este barco!
      - (Condition: De lo contrario:)
        - ((Se abre la interfaz de destino de Charter Ship.))
