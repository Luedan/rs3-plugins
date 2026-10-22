# Fizzy Bunny

- **Original Wiki Page**: [Transcript:Fizzy Bunny](https://runescape.wiki/w/Transcript%3AFizzy%20Bunny)
- **Letter**: `F`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Con el título de "el Huevo" antes de haber desbloqueado su variante "Agrietado"

- **Fizzy Bunny:** Es un título interesante... Yo era el mismo hasta que mi amigo, el Makeover Mage, me ayudó.
- ¡Has desbloqueado el color 'Agrietado' para el título 'el Huevo'!
- ((Repeated in a pop-up:))
  - ¡Has desbloqueado el color 'Agrietado' para el título 'el Huevo'!
  - (continue)
- **Fizzy Bunny:** Déjame ponerle algunos colores nuevos a ese título, tal vez te sirvan.

#### Diálogo estándar

- **Fizzy Bunny:** ¡Bien conocido, Player!
- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué está pasando aquí?
    - **Player:** ¿Qué está pasando aquí?
    - **Fizzy Bunny:** Estaba supervisando la creación de unas deliciosas estatuillas, inspiradas en un servidor, ¡cuando tuve una revelación deliciosa!
    - **Fizzy Bunny:** ¡Coamancia! ¡Delicias de chocolate animadas! ¡No sólo es un sabroso manjar, sino también un juguete emocionante!
    - **Fizzy Bunny:** Desafortunadamente, la confianza de un compañero del que busqué ayuda me desvió; Parece que estaba mintiendo un poco sobre su experiencia, ¡y ahora los conejitos están sueltos!
    - **Fizzy Bunny:** Han comenzado a habitar madrigueras de chocolate cercanas, y cada pocos minutos los sinvergüenzas parecen aparecer en un lugar diferente.
    - **Fizzy Bunny:** Si logras localizarlos, me encantaría ofrecerte fichas de primavera a cambio de las que me devuelvas.
    - (previous)
  - [Choice]: Tengo algo para ti.
    - (Condition: Without chocolate rabbits:)
      - **Fizzy Bunny:** ¿Me estás tomando el pelo? ¡No tienes conejos! Vuelve cuando tengas algo para mí.
    - (Condition: With chocolate rabbits:)
      - (Condition: With at least 30,000 spring tokens:)
        - [Menu]: No recibirás ningún token Spring por esto. ¿Entregar de todos modos?
          - [Choice]: Sí.
            - (removes=all chocolate rabbits in backpack)
            - Ha alcanzado el límite flexible del token Spring de 30 000. Debes gastar algunas fichas en la tienda de Gummy antes de poder ganar más.
            - (pop-up)
              - (Pop-up: You have reached the Spring token soft cap of 30,000. You need to spend some tokens in Gummy's store before you can earn more.|warning=yes)
              - (continue)
          - [Choice]: No.
            - (end)
      - (Condition: With less than 30,000 spring tokens:)
        - (removes=all chocolate rabbits in backpack)
        - Se ha agregado lo siguiente a su bolsa de divisas: [número] x tokens Spring
        - (continue)
      - **Fizzy Bunny:** ¡Trabajo increíble, Player! ¡Toma esto como pago y vuelve a salir, inmediatamente!
  - [Choice]: Adiós.
    - **Player:** Adiós, Fizzy.
    - **Fizzy Bunny:** ¡Vuelve pronto! ¡Con tantos conejos de chocolate como puedas sostener!

### Hand in

- (above|I've got something for you)
