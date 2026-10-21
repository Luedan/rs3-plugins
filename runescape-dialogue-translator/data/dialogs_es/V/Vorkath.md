# Vorkath

- **Original Wiki Page**: [Transcript:Vorkath](https://runescape.wiki/w/Transcript%3AVorkath)
- **Letter**: `V`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### City of Um


#### Enfoque

- (Condition: Si el player no tiene el anillo de Zorgoth o el anillo del alma de Zorgoth y tiene espacio libre en backpack:)
  - (Condition: Sin haber mejorado el anillo:)
    - (receives=Zorgoth's ring)
    - [Vorkath te devuelve el anillo y vuelve a dormir.]
    - (continue)
  - (Condition: Habiendo mejorado el anillo:)
    - (receives=Zorgoth's soul ring)
    - [Vorkath le devuelve su anillo actualizado y vuelve a dormir.]
    - (continue)
- (Condition: Si el player no tiene The Shadow Realm y Zorgoth's Journal en su backpack:)
  - (Condition: Sin Tiny Zemouregal ni Vorki convocados:)
    - Vorkath está ocupado teniendo un largo y agradable descanso.
    - ((Repetido en una ventana emergente:))
      - Vorkath está ocupado teniendo un largo y agradable descanso.
  - (Condition: Con Tiny Zemouregal convocado:)
    - **Tiny Zemouregal:** ¡GRAN DRAGÓN!
    - **Vorkath:** ...
    - **Tiny Zemouregal:** ¡GRAN DRAGÓN ARRIBA! ¡ VOLAMOS!
    - **Player:** No creo que Vorkath quiera hacer eso nunca más.
    - **Tiny Zemouregal:** ¡QUÉMALO TODO, DRAGÓN!
    - **Vorkath:** (Vorkath lo ignora y vuelve a dormir.)
  - (Condition: Con Vorki convocado:)
    - **Vorki:** ¡Mira, Player! ¡Soy yo!
    - **Vorkath:** ...
    - **Vorki:** ¡Soy GRANDE para mí!
    - **Vorki:** Voy a ser así de grande algún día.
    - **Vorki:** ¡Y TE COMERÉ, Player!
    - **Vorkath:** ...
    - **Player:** Si tú lo dices, pequeño.
- (Condition: Si el player tiene The Shadow Realm y Zorgoth's Journal en su backpack:)
  - **Player:** ¿Qué te pasa, Vorkath?<br/>¿No puedes dormir?
  - **Vorkath:** *ruidos tristes de dragón*
  - (Action: el player abre El Reino de las Sombras.)
  - [Recuperas un libro sobre el reino de las sombras de tu backpack y lo abres en la primera página.]
  - **Player:** Ejem. 'En mis expediciones de investigación al continente, he pasado algún tiempo estudiando a los hechiceros del imperio del dios vacío...'
  - (Action: La pantalla se vuelve negra y luego se desvanece.)
  - **Player:** 'Habiendo alcanzado incluso Gielinor, no sé qué, si es que hay algo, puede impedir que llene el universo por completo.'
  - **Vorkath:** *ruidos de dragón asustado*
  - **Player:** Quizás no sea el material ideal para la hora de dormir.<br/>Probemos con otro.
  - (Action: el player abre el Diario de Zorgoth.)
  - **Player:** Adventure, Inc. presenta 'Zorgoth's Journal', escrito por Zorgoth y narrado por Player.
  - **Player:** 'Desprecio a los humanos. Su población se extiende por todos los mundos que toco...'
  - **Vorkath:** *ruidos de dragón enojado*
  - **Player:** ...¡no es lo que dice este libro!<br/>Éste trata sobre...
  - **Player:** Eh...
  - **Player:** Se trata de un dragón muy valiente, que tuvo todo tipo de aventuras...
  - (Action: La pantalla se vuelve negra y luego se desvanece.)
  - **Player:** '...¡y todos vivieron felices para siempre!'
  - [Cierras el libro y observas con una sonrisa que Vorkath ahora ronca pacíficamente.]
  - (Condition: Si es la primera vez que lees las dos historias de Vorkath:)
    - {{RSFontAchievement|Soft Dragon, Warm Dragon|Read two bedtime stories to Vorkath.}}

#### mascota

- (Action: el player mascotas Vorkath.)
- ((Al azar se puede mostrar lo siguiente:))
  - ¡Mira, perro!
  - ((Repetido en una ventana emergente:))
    - ¡Mira, perro!

#### Usando un corazón de piedra negra en Vorkath

- **Vorkath:** (Vorkath te gruñe y muestra sus dientes fantasmales).
