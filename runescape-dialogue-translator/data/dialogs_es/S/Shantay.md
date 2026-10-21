# Shantay

- **Original Wiki Page**: [Transcript:Shantay](https://runescape.wiki/w/Transcript%3AShantay)
- **Letter**: `S`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Standard dialogue


#### Diálogo por primera vez

- **Shantay:** Hola, effendi. Soy Shantay.
- *Si el player está en un mundo gratuito:*
  - (continue|free-to-play)
- *Si el player está en un mundo de miembros:*
  - **Shantay:** Veo que eres nuevo.
  - (continue|members)

#### Diálogo posterior

- *Si el player está en un mundo gratuito:*
  - **Shantay:** Hola, effendi. ¡Bienvenido al pase Shantay!
  - **SELECCIONA UNA OPCIÓN**
    - ¿Qué es este lugar?
      - (below|what-is-this-place)
    - Debo irme.
      - (below|going)
- *Si el player está en un mundo de miembros:*
  - **Shantay:** Hola, effendi.
  - **Shantay:** Por favor lea el cartel publicitario antes de adentrarse en el desierto. Le dará detalles sobre los peligros que puede enfrentar.
  - **SELECCIONA UNA OPCIÓN**
    - ¿Qué es este lugar?
      - **Player:** ¿Qué es este lugar?
      - **Shantay:** Este es el pase Shantay. Cuido esta zona con mis hombres. Soy responsable de mantener este pase abierto y reparado.
      - **Shantay:** Mis hombres y yo evitamos que los forajidos salgan del desierto. Y evitamos que los inexpertos mueran secamente en la arena. ¿Quién dirías que eres?
      - **SELECCIONA UNA OPCIÓN**
        - Definitivamente soy un forajido, ¡prepárate para morir!
          - **Player:** Definitivamente soy un forajido, ¡prepárate para morir!
          - **Shantay:** Jaja, muy gracioso... ¡Guardias, arresten a [him/her]!
          - *(Acción: Los guardias de Shantay te agarran y te encierran.)*
          - **Shantay:** Así es como tratamos a los alborotadores por aquí. Ahora, si pagas una multa, te liberaré. De lo contrario serás deportado a una cárcel de máxima seguridad en Port Sarim. ¡Elegir!
          - **¿QUÉ TE GUSTARÍA DECIR?**
            - Yo pagaré.
              - **Player:** Yo pagaré.
              - Shantay toma 5 coins y abre la puerta.
              - Se han eliminado 5 coins de tu bolsa de dinero.
            - ¡Deportame a Port Sarim!
              - **Player:** ¡Deportame a Port Sarim!
              - **Shantay:** ¡Espero que esto te enseñe una lección!
              - *(Acción: Eres teletransportado dentro de la celda de Prison Pete en la cárcel de Port Sarim)*
              - Te encuentras en una prisión.
            - Me quedaré aquí, gracias.
              - **Player:** Me quedaré aquí, gracias.
              - **Shantay:** Ah, es bueno que estés dispuesto a dedicar tiempo a reflexionar sobre tus fechorías.
        - Soy un poco inexperto.
          - **Player:** Soy un poco inexperto.
          - **Shantay:** ¿Puedo recomendarte que lleves al menos un odre de agua lleno al desierto? El sol calienta mucho y sin agua para beber puedes morir de sed. Veo que ya llevas un cuchillo en tu cinturón de herramientas. Si tus odres se están secando, puedes cortar los cactus que ves para reponerlos.
          - **SELECCIONA UNA OPCIÓN**
            - ¿Puedo ver lo que tienes para vender, por favor?
              - (below|sell)
            - Debo irme.
              - (below|going)
        - Er, tampoco, soy un aventurero.
          - **Player:** Er, tampoco, soy un aventurero.
          - **Shantay:** Bien, tengo lo ideal para el aventurero del desierto: ropa que te mantendrá fresco bajo el calor del sol. También vendo odres de agua, que te ayudarán a sobrevivir después de morir de sed. Y puedes utilizar el cofre del banco aquí. No es aconsejable viajar por el desierto con una armadura gruesa y pesada; sólo te deshidratarás más rápido.
          - **SELECCIONA UNA OPCIÓN**
            - ¿Puedo ver lo que tienes para vender, por favor?
              - (below|sell)
            - Debo irme.
              - (below|going)
    - ¿Puedo ver lo que tienes para vender, por favor?{{anchor|sell}}
      - **Player:** ¿Puedo ver lo que tienes para vender, por favor?
      - **Shantay:** ¡Absolutamente, effendi!
      - (opens=Shantay Pass Shop)
    - Debo irme.{{anchor|going}}
      - **Player:** Debo irme.
      - **Shantay:** Hasta luego...

### When trying to open the door after getting arrested

- **Shantay:** ¡Ajá, un alborotador! Ahora tienes una opción: si pagas una multa de 5 coins, te liberaré. De lo contrario serás deportado a una cárcel de máxima seguridad en Port Sarim.
- **¿QUÉ TE GUSTARÍA DECIR?**
  - Yo pagaré.
    - (arriba)
  - ¡Deportame a Port Sarim!
    - (arriba)
  - Me quedaré aquí, gracias.
    - (arriba)
