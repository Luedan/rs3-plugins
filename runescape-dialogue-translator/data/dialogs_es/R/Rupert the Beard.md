# Rupert the Beard

- **Original Wiki Page**: [Transcript:Rupert the Beard](https://runescape.wiki/w/Transcript%3ARupert%20the%20Beard)
- **Letter**: `R`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### At the tower north of Falador


#### Antes de Grim Tales (se requieren 58 Thieving)

- **Player:** ¡Hola!
- **Tubo de drenaje:** ¡Yo digo! ¿De dónde vino esa voz en Gielinor?
- **Player:** ¡Hola! ¿Puedes oírme?
- **Tubo de drenaje:** Por qué sí. Sí puedo. Mi palabra. ¿Es ese... es ese uno de los dioses? ¿Quizás Guthix? ¿Saradomin?
- **Player:** No, no. Yo no soy ninguno de los dos.
- **Tubo de drenaje:** ¡Egad! No eres...Zamorak...¿verdad? Quiero decir, uh... con su perdón, por supuesto, mi Señor. ¡Sin ánimo de ofender!
- **Player:** ¡Ja, ja! ¡No, te estoy hablando a través del tubo! Estoy al pie de tu torre.
- **Tubo de drenaje:** Oh. ¡Ah, claro! Oh sí. ¡Qué inteligente! ¡Excelente idea! ¿Cómo pensaste en eso? ¡Buen espectáculo, viejo frijol!
- **Player:** ¿Quién eres?
- **Tubo de drenaje:** Rupert the Beard. A sus ordenes, fruta vieja.
- **Player:** Rupert the Beard?
- **Tubo de drenaje:** Sí, nabo viejo. A causa de mi barbilla maravillosamente larga, ¿sabes?
- **Player:** Entonces, ¿qué estás haciendo exactamente ahí arriba? ¿Y por qué hablas tan raro?
- **Tubo de drenaje:** ¿Qué estoy haciendo? Bueno, supongo que estoy estancado en una cuestión de hablar. ¡Dios mío, sí! Estoy estancado. Y hablo en el discurso del Rey, te lo haré saber.
- **Player:** ¿En serio? ¿Qué rey?
- **Tubo de drenaje:** ¿Cuál K...? ¡Vaya, EL Rey, viejo! ¡EL Rey! En mi opinión sólo vale la pena mencionar uno.
- **Player:** Ya veo. Bueno, ¿hay algo que pueda hacer para ayudarte ahí arriba?
- **Tubo de drenaje:** Hmmm. No, no, no se me ocurre nada en este momento. Estoy un poco estancado. Déjame saber si tienes alguna idea.
- **Player:** ¡Haré lo mejor que pueda!

#### Después de cuentos sombríos

- **Player:** Hola, Ruperto.
- **Rupert the Beard:** ¡Hola de nuevo, viejo pastel de queso! Es maravilloso verte.
- **Player:** ¿Cómo van las investigaciones?
- **Rupert the Beard:** ¡Gracias a que me liberaste, muy bien! Tengo mucho más que hacer por supuesto, pero ahora soy libre y puedo continuar donde lo dejé.
- **Player:** ¡Es una gran noticia!
- (Condition: If the player has lost their dwarven helmet:)
  - **Player:** Ummm...
  - **Rupert the Beard:** ¿Cuál es el problema, viejo pelusa del ombligo?
  - **Player:** Perdí ese casco que me diste.
  - **Rupert the Beard:** Ya veo. Bueno, puede que tengas suerte. Recientemente hice otro para reemplazarlo. Supongo que podrías tenerlo por 60.000 de oro. En cuanto a los materiales, ya lo entiendes.
  - [Menu]: Selecciona una opción
    - [Choice]: Ok, eso suena justo.
      - **Player:** Ok, eso suena justo.
      - (Condition: Without space in backpack:)
        - **Rupert the Beard:** Mmm. Parece que primero necesitarás más espacio en tu inventario, viejo saltador. Vuelve a verme de nuevo cuando hayas hecho espacio.
        - **Player:** Vale.
      - (Condition: With less than 60,000 coins:)
        - No puedes permitirte eso.
        - **Rupert the Beard:** Mmm. Parece que no tienes suficiente, vieja papilla. Vuelve a verme otra vez cuando tengas un poco más de oro contigo.
        - **Player:** Vale.
      - (Condition: With 60,000 coins:)
        - (removes=60,000 coins) (receives=dwarven helmet)
        - **Rupert the Beard:** ¡Ahí estás! Espero que esto te sirva lo suficiente, repollo viejo.
        - **Player:**¡Gracias, Rupert!
    - [Choice]: No creo que pueda permitirme eso, lo siento.
      - **Player:**No creo que pueda permitirme eso, lo siento.
      - **Rupert the Beard:** ¡No hay problema! Vuelvan a verme si cambian de opinión, viejos ligueros.
