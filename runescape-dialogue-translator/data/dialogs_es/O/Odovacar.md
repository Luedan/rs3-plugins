# Odovacar

- **Original Wiki Page**: [Transcript:Odovacar](https://runescape.wiki/w/Transcript%3AOdovacar)
- **Letter**: `O`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

- *Si el player está en el mosaico directamente al norte, este, sur u oeste de Odovacar:*
  - **Odovacar:** ¡Bien conocido, compañero aventurero! ¿Le puedo ayudar en algo?
- *Si el player no está en el mosaico directamente al norte, este, sur u oeste de Odovacar:*
  - **Odovacar:** Buenos días. ¿Cómo puedo ayudarte?
- *Si el player tiene artículos que puede recolectar de Grand Exchange:*
  - **Odovacar:** Antes de continuar, debo informarle que tiene artículos listos para ser recogidos en Grand Exchange.
- **¿Qué te gustaría decir?**
  - *Si el player está en el mosaico directamente al norte, este, sur u oeste de Odovacar:*
    - ¿Quién eres?
      - **Odovacar:** Qué terriblemente grosero de mi parte, mi querido [chap/lady]. Mi nombre es Odovacar y trabajo para esa excelente empresa, el Banco de Gielinor.
      - **¿Qué te gustaría decir?**
        - Si trabajas en el banco, ¿qué haces aquí?
          - **Odovacar:** Como parte de nuestro servicio continuo para brindarle a usted, el cliente, una experiencia bancaria absolutamente de clase mundial, estamos investigando la opción de abrir una cadena de bancos ambulantes. Estos le brindarán a usted, nuestro estimado cliente, la conveniencia de contar con instalaciones bancarias que le serán de máxima utilidad. ¡Como aquí!
          - **Player:** ¿Eh?
          - **Odovacar:** Soy el primero de una nueva generación de banqueros viajeros que recorrerán las zonas peligrosas del mundo para brindarle a usted, el valioso cliente, un banco cuando más lo necesita.
          - **Player:** ¿Entonces puedo acceder a mi cuenta bancaria simplemente hablando contigo?
          - **Odovacar:** Absolutamente correcto, querido [sir/lady]. Debo advertirle, sin embargo, que debido a los gastos generales significativamente mayores de una empresa como esta, hay un pequeño cargo bancario de 100 po cada vez que desea acceder a su cuenta.
          - **¿Qué te gustaría decir?**
            - Suena justo; Aquí está el dinero. ¿Puedo acceder a mi cuenta ahora?
              - (below|access-bank)
            - Déjame abrir mi cuenta y luego te pagaré.
              - **Odovacar:** No es que no confíe en ti, viejo [chap/girl], pero como dice el viejo refrán, "el dinero está antes que los amigos".
            - ¡Eso es absurdo! ¡No estoy pagando para retirar mi propio dinero!
              - **Odovacar:** Lamento oír eso, [sir/madam]. Si debes reconsiderarlo, porque creo que este servicio ofrece una excelente relación calidad-precio, no dudes en contactarme.
        - Me gustaría acceder a mi cuenta bancaria, por favor.
          - (below|access-bank)
        - Me gustaría verificar la configuración de mi PIN.
          - (opens=Bank PIN)
  - Me gustaría acceder a mi cuenta bancaria, por favor.
    - *Si el player tiene al menos 100 coins:*
      - *Si el player está en el mosaico directamente al norte, este, sur u oeste de Odovacar:*
        - (Action: Pagas 100 coins para utilizar el banco viajero.)
      - (opens=Bank)
    - *Si el player no tiene al menos 100 coins:*
      - **Odovacar:** Me temo que no tienes los fondos necesarios contigo en este momento, por lo que no puedo permitirte acceder a tu cuenta. Por favor, vuelve cuando tengas 100 de oro para cubrir la tarifa.
  - Me gustaría verificar la configuración de mi PIN.
    - (opens=Bank PIN)
  - Me gustaría ver mi caja de colección.
    - (opens=Collection box)
  - *Si el player no está en el mosaico directamente al norte, este, sur u oeste de Odovacar:*
    - ¿Qué es este lugar?
      - **Odovacar:** Esta es una sucursal del Banco de Gielinor. Disponemos de sucursales en muchas localidades.
      - **¿Qué te gustaría decir?**
        - ¿Y tú qué haces?
          - **Odovacar:** Nos ocuparemos de tus artículos y de tu dinero. Deje sus objetos de valor con nosotros si desea mantenerlos seguros.
        - ¿No te llamaban antes el Banco de Varrock?
          - **Odovacar:** Sí, lo hicimos, pero la gente seguía entrando a nuestras sucursales fuera de Varrock y diciéndonos que nuestros carteles estaban equivocados. Actuaron como si no supiéramos en qué ciudad estábamos o algo así.
