# Murky Matt (runes)

- **Original Wiki Page**: [Transcript:Murky Matt (runes)](https://runescape.wiki/w/Transcript%3AMurky%20Matt%20%28runes%29)
- **Letter**: `M`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Before doing the Grand Exchange tutorial

- **Player:** Hola.
- **Murky Matt (runas):{{anchor|arr}}** Arrrr, muchacho, hablaría contigo, pero ¿puedo pedirte que hables con Brugsen Bursen o Grand Exchange Tutor cerca de la entrada? Brugsen os dará una gran y saqueadora lección sobre el Grand Exchange y el Tutor una explicación mucho más breve y sencilla.

#### Opción de runas de información

- (arriba2|arr)

#### Opción de combinación

- **Murky Matt (runas):** Arrrr, muchacho, debo pedirte que primero aprendas un poco sobre Grand Exchange. Brugsen os dará una gran y saqueadora lección, o el Tutor puede ofreceros una explicación mucho más breve y sencilla.

### After doing the Grand Exchange tutorial

- **Player:** ¡Un pirata!
- **Murky Matt (runas):** Arrrr, ¿cómo adivinarías eso, [me-lad/me-lady]?
- **Player:** Estás bromeando, ¿verdad?
- **Murky Matt (runas):** ¡No! Ahora bien, ¿qué es lo que queréis? Puedo contarte todo sobre los precios de las runas, o tal vez podría combinar los cargos de tus joyas de teletransporte.
- [Menu]: Elige una opción:
  - [Choice]: ¿Qué hace un pirata aquí?
    - **Player:** ¿Qué hace un pirata aquí?
    - **Murky Matt (runas):** ¡Por mi piel llena de ampollas marinas, podría pedirte lo mismo!
    - **Player:** Pero... ¿No soy un pirata?
    - **Murky Matt (runas):** ¿No? ¿Entonces qué es ese olor? ¡El olor de alguien que pasó demasiado tiempo en el mar sin bañarse!
    - **Player:** Creo que probablemente seas tú.
    - **Murky Matt (runas):** ¡Jar, ja, ja!
    - **Murky Matt (runas):** ¡Tenemos un marinero de tierra severo aquí! Bueno, déjame decirte que estoy aquí para el Grand Exchange. ¡Voy a cobrar mi botín!
    - **Player:** ¿No quieres simplemente venderlo en una tienda o canjeárselo a alguien específico?
    - **Murky Matt (runas):** ¡Por mis huesos golpeados por las olas! ¡No cuando puedo vender a todo el mundo desde este mismo lugar!
    - (Condition: If Lunar Diplomacy has not been completed:)
      - (initial)
    - (Condition: If Lunar Diplomacy has been completed:)
      - **Player:** ¡Ustedes, los piratas, no son más que problemas! ¡Vaya, una vez viajé a Lunar Isle con un grupo de tu tipo y pasé días navegando en círculos!
      - **Murky Matt (runas):** ¡Entonces debes conocerme hermano! ¡Murky Pat!
      - **Player:** Mmmm. No estoy tan seguro de recordarlo.
      - **Murky Matt (runas):** Bueno, seguro que estará en ese barco. Y recuerdo que me habló de un tipo como tú, mezclado con maldiciones y grumetes.
      - **Player:** ¡Sí! ¡Ese era yo!
      - **Murky Matt (runas):** Seguro que serás un personaje diferente.
      - (initial)
  - [Choice]: Cuéntame sobre los precios de las runas.
    - **Player:** Cuéntame sobre los precios de las runas.
    - ((Guide Prices: Runes opens up.))
  - [Choice]: Combina las cargas de mis joyas de teletransporte, por favor.{{anchor|combine}}
    - **Player:** Combina los cargos de mis joyas de teletransporte, por favor.
      - (Condition: If there is nothing to combine:)
        - **Murky Matt (runas):** Arrr, no hay nada en tu inventario que pueda combinar.
      - (Condition: If the player's backpack is empty:)
        - **Murky Matt (runas):** ¡Arrr! ¡Tus bolsillos están tan vacíos como un barco fantasma en un exorcismo!
      - (Condition: With jewellery to combine:)
        - (Las joyas en backpack tienen sus cargos combinados).
        - **Murky Matt (runas):** Arrr, todo listo.
        - **Player:** ¡Gracias!
  - [Choice]: ¡Tengo que ir a limpiar algunas cubiertas! ¡Yarr!
    - **Player:** ¡Tengo que irme, ejem, a limpiar algunas cubiertas! ¡Yarr!
    - **Murky Matt (runas):** ¡Aplaza tu discurso allí mismo! Dejemos de lado esta alusión despectiva y un tanto estrecha de miras de que todos los que viajan por mar sólo se preocupan de lavar las cubiertas, cuidar de los loros y beber ron. Te haré saber que un pirata es mucho más de lo que parece.
    - **Player:** ¡Sí, sí, capitán!
    - **Murky Matt (runas):** ...
    - **Player:** ¡Oh, vamos! ¡Relájate!

#### Opción de combinación

- (above|combine)

#### Opción de runas de información

- ((Guide Prices: Runes opens up.))

### Overhead dialogue

{{Trandom}}
- **Murky Matt (runas):** {{RSChat|Sure be a busy place, today.}}
- **Murky Matt (runas):** {{RSChat|Yarrr! I'm gonna be rich, I tell ye!}}
- **Murky Matt (runas):** {{RSChat|I'm lovin' this Grand Exchange! Arrr!}}
- **Murky Matt (runas):** {{RSChat|Arrr! Another good sale!}}
- **Murky Matt (runas):** {{RSChat|No! Me prices, they be goin' down!}}
