# Benny

- **Original Wiki Page**: [Transcript:Benny](https://runescape.wiki/w/Transcript%3ABenny)
- **Letter**: `B`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In Varrock

- **Seleccione una opción**
  - [Choice]: ¿Puedo darme un periódico, por favor?
    - **Player:** ¿Me puedes dar un periódico, por favor?
    - **Benny:** Por supuesto, [Guv/Missus]. Serán 50 piezas de oro, por favor.
    - **Seleccione una opción**
      - [Choice]: Claro, aquí tienes. {{anchor|buy}}
        - (Condition: If the player does not have enough money:)
          - No puedes permitirte eso.
          - **Player:** Dios mío, parece que no tengo suficiente dinero conmigo.
          - **Benny:** Bueno, sin efectivo ni papel. Vive en la ignorancia.
        - (Condition: If the player has enough money:)
          - (removes=50 coins) (receives=newspaper)
          - {{RSFontAchievement|Read All About It}}
      - [Choice]: Uh, no gracias, he cambiado de opinión.
        - **Player:** No, gracias.
        - **Benny:** Ok, haz lo que quieras. Hay muchos más peces en el mar.
  - [Choice]: ¿Cuanto cuesta un papel?
    - **Player:** ¿Cuánto cuesta un artículo?
    - **Benny:** ¡Solo 50 piezas de oro! ¡Una auténtica ganga! ¿Quieres uno?
    - **Seleccione una opción** {{anchor|yesno}}
      - [Choice]: Sí, por favor.
        - **Player:** Sí, por favor.
        - (continuea|buy)
      - [Choice]: No, gracias.
        - (arriba)
  - [Choice]: Varrock Herald? Nunca he oído hablar de eso.
    - **Player:** Varrock Herald? Nunca he oído hablar de eso.
    - **Benny:** Para los analfabetos entre nosotros, lo aclararé. El Varrock Herald es un periódico nuevo. Es editado, impreso y publicado por mí, Benny Gutenberg, y cada edición promete cautivar al lector con cautivantes
    - **Benny:** ¡material! Ahora, ¿puedo interesarte en comprar uno por sólo 50 de oro?
    - (continuea|yesno)
  - [Choice]: ¿Algo interesante ahí dentro?
    - **Player:** ¿Hay algo interesante ahí?
    - **Benny:** Por supuesto que sí, amigo. ¡Lleno de ideas que invitan a la reflexión, entrevistas polémicas y escándalos de celebridades! ¡Una lectura excelente y todo por sólo 50 coins! ¿Quieres uno?
    - (continuea|yesno)

#### Diálogo aéreo

- **Benny:** {{RSChat|Varrock Herald, on sale here!}}
- **Benny:** {{RSChat|Get your Varrock Herald here!}}
- **Benny:** {{RSChat|Extra! Extra! Read all about it!}}

### In New Varrock

- **Seleccione una opción**
  - [Choice]: ¿Puedo darme un periódico, por favor?
    - **Benny:**5 de tus mejores zemomarks.
    - **Seleccione una opción**
      - [Choice]: Claro, aquí tienes.
        - (Condition: If the player does not have five zemomarks:)
          - **Player:** Me temo que no tengo suficiente dinero conmigo.
          - **Benny:** ¡Sin efectivo, sin heraldo! <br>I no reparte folletos gratis, jefe.
          - (initial)
        - (Condition: If the player has five zemomarks:)
          - (removes=five zemomarks) (receives=Newspaper (New Varrock))
          - [Benny te vende una copia del Nuevo Varrock Herald.]
          - (initial)
      - [Choice]: Uh, no gracias, he cambiado de opinión.
        - **Benny:**Haz lo que quieras. Hay muchos más peces en el mar.
        - (initial)
  - [Choice]: ¿Cuanto cuesta un papel?
    - **Benny:**¡Solo 5 zemomarks! Eso hoy en día ni siquiera te daría un trago de lengua. <br>¿Quieres uno?
    - (initial)
  - [Choice]: ¿Nuevo Varrock Herald? Nunca he oído hablar de eso.
    - **Benny:** Permítame aclararlo, jefe.
    - **Benny:**El nuevo Varrock Herald es un periódico nuevo. Está editado, impreso y publicado por mí mismo, Benny Gutenburg...
    - **Benny:**...bajo la muy apreciada dirección de la Comisión de Correcciones y Publicaciones de Zemouregal.
    - **Benny:** ¡Cada edición promete cautivar a {{Sic}} con material cautivador y educativo! <br>Ahora, ¿puedo interesarte por uno por sólo 5 zemomarks?
    - (initial)
  - [Choice]: ¿Algo interesante ahí dentro?
    - **Benny:** Por supuesto que sí, amigo. ¡Lleno de ideas que invitan a la reflexión, entrevistas polémicas y escándalos de celebridades!
    - **Benny:** ¡Un cambio de página, todo por solo 5 zemomarks! ¿Quieres uno? ¿Quizás dos?
    - (initial)
  - [Choice]: No interesado.
    - **Benny:**Bien. Permanecer ignorante de la actualidad. No tengo piel en la nariz.

#### Diálogo aéreo

- **Benny:** {{RSChat|New Varrock Herald! Only 5 zemomarks!}}
- **Benny:** {{RSChat|Get your New Varrock Herald!}}
- **Benny:** {{RSChat|Selling V Herald 5zm!}}
- **Benny:** {{RSChat|Read all about it!}}
- **Benny:** {{RSChat|Come on guys, I'm on commission here!}}
