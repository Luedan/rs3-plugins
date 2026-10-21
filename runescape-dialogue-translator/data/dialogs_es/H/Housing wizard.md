# Housing wizard

- **Original Wiki Page**: [Transcript:Housing wizard](https://runescape.wiki/w/Transcript%3AHousing%20wizard)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Antes de completar No hay lugar como el hogar...

- ((Lo siguiente se muestra en una interfaz titulada "CONSTRUCCIÓN":))
  - 54px Debes completar el tutorial de Construction antes de poder utilizarlo.
  - Hable con Alfred Stonemason, al noroeste de Rimmington, para obtener más información.
    - [Choice]: bien
      - ((La interfaz se cierra y el diálogo continúa a continuación.))

#### Después de completar No hay lugar como el hogar...

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Mueve mi trama.
    - **Housing wizard:** Te teletransportaré a la granja y desde allí podrás elegir entre todos.
    - (Action: La pantalla se vuelve negra. el player ahora está dentro de la propiedad junto al portal de la propiedad.)
    - **Housing wizard:** Echa un vistazo a tus opciones. Cuando estés listo, simplemente toca el letrero numerado de la parcela cerca de la entrada.
  - [Choice]: Iniciar una granja.
    - [Menu]: Configuración de la granja
      - [Choice]: ¿Qué es una finca?
        - **Housing wizard:** Una granja es un espacio compartido donde tú y hasta cuatro personas más podéis construir juntos y explorar las parcelas de cada uno.
        - **Housing wizard:** Si eliges dejar una propiedad en el futuro, nunca perderás ningún progreso en tu parcela personal.
        - (initial)
      - [Choice]: Crear finca.
        - **Housing wizard:** ¡Genial! ¡Invita a algunos jugadores a tu grupo, luego ven a verme nuevamente y podremos finalizar tu propiedad!
        - [Haz clic derecho en los jugadores cercanos para invitarlos a tu granja.]
      - [Choice]: Nada por ahora.
        - (end)

#### El creador creando una granja

- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Establecer el nombre de la propiedad.
    - [Menu]: Ingrese el nombre de su propiedad deseada:
      - [0/20<br>[input field]<br>Los nombres solo pueden contener A-Z, a-z, 0-9 y espacios. Sin caracteres especiales, p. å, ä]
        - [Menu]: Confirme el nombre de su propiedad elegida:
          - [Choice]: [name]
            - Comprobando si el nombre de la propiedad está disponible.
            - (Ventana emergente: Comprobando si el nombre de la propiedad está disponible.|color=#00FF00)
            - [Menu]: ¿Crear una granja?
              - [Choice]: Crear propiedad: '[name]'.
                - Su propiedad ahora se está creando, esto puede tardar unos momentos.
                - Player se ha unido a su propiedad.
                - Su propiedad '[name]' se ha creado correctamente.
                - (Ventana emergente: Su propiedad '[name]' se ha creado correctamente.|color=#00FF00)
              - [Choice]: Cancelar.
                - (end)
          - [Choice]: Elija un nombre diferente.
            - (previous)
  - [Choice]: Finalizar la finca.
    - (above|enter-name)
  - [Choice]: Cancelar la creación de la propiedad.
    - [Menu]: ¿Está seguro de que desea abandonar el proceso de creación de vivienda?
      - [Choice]: Sí.
        - Ha abandonado el proceso de creación de propiedad.
        - (Ventana emergente: Has abandonado el proceso de creación de propiedad.|advertencia=yes)
      - [Choice]: No.
        - (end)
  - [Choice]: Nada por ahora.
    - (end)

#### Miembros fundadores creando una granja

- **Housing wizard:** Tu granja aún se está formando... ¿Qué te gustaría hacer?
- [Menu]: ¿Qué te gustaría hacer?
  - [Choice]: Dejar la creación de viviendas.
    - [Menu]: ¿Estás seguro de que quieres abandonar este grupo?
      - [Choice]: Sí.
        - Ha abandonado el proceso de creación de propiedad.
        - (Ventana emergente: Has abandonado el proceso de creación de propiedad.|advertencia=yes)
      - [Choice]: No.
        - (end)
  - [Choice]: Nada por ahora.
    - (end)

#### Creó una granja

- **Housing wizard:** ¡Excelente! Veo que estás instalado en una granja.
- (Condition: El intercambio está en curso:)
  - **Housing wizard:** Estás en el proceso de intercambiar una trama. ¿Quieres continuar?
  - [Menu]: Deja de intercambiar tramas.
    - [Choice]: Cancelar el intercambio de trama.
      - **Housing wizard:** Ordenado. Si quieres empezar a intercambiar parcelas con alguien de tu propiedad, vuelve a hablar conmigo.
      - (continue)
    - [Choice]: Continuar intercambiando tramas.
      - (end)
- [Menu]: ¿En qué puedo ayudarte?
  - [Choice]: Permutar parcela de finca.
    - Haz clic derecho en los jugadores cercanos para proponerles intercambiar parcelas con ellos.
    - Invitando a Player a intercambiar tramas.
    - (Ventana emergente: invitando a Player a intercambiar parcelas.|color=#00ff00)
    - (Condition: Player aceptó el intercambio:)
      - Ha intercambiado parcelas con éxito con Player. Su parcela se moverá la próxima vez que se genere su propiedad.
      - (Ventana emergente: Ha intercambiado parcelas exitosamente con Player. Su parcela se moverá la próxima vez que se genere su propiedad).
    - (Condition: Player rechazó el intercambio:)
      - Player ha rechazado su invitación.
      - (Ventana emergente: Player ha rechazado su invitación.|advertencia=yes)
  - [Choice]: Dejar la granja.
    - [Warning:]<br>Es posible que no puedas volver a unirte a esta propiedad si te vas.}}
    - [Menu]: ¿Estás seguro de que quieres irte?
      - [Choice]: Vete.
        - Su solicitud para abandonar su propiedad ya está en curso.
        - Has abandonado tu hogar.
        - (Ventana emergente: Has abandonado tu propiedad.|color=#00ff00)
      - [Choice]: Quédate.
        - (end)
  - [Choice]: Invita a un jugador.
  - [Choice]: Administración de fincas.
    - [Menu]: ¿Qué cambios en su hogar le gustaría hacer?
      - [Choice]: Patear a un miembro.
        - (Condition: Si hay un solo miembro:)
          - [can not] patéate.}}
          - [Choice]: Player 1
            - Player 1 ha sido eliminado de su propiedad.
          - [Choice]: Player 2
            - (arriba)
          - [Choice]: Player 3
            - (arriba)
          - [Choice]: Player 4
            - (arriba)
          - [Choice]: nadie
      - [Choice]: Cambiar dueño.
        - (Condition: Si hay un solo miembro:)
          - [can not] asignar otro propietario.}}
        - [Menu]: ¿A quién le gustaría asignar como nuevo propietario?
          - [Choice]: Player 1
            - Has cambiado correctamente de propietario a Player 1
            - (Ventana emergente: Ha cambiado correctamente el propietario a Player 1)
          - [Choice]: Player 2
            - (arriba)
          - [Choice]: Player 3
            - (arriba)
          - [Choice]: Player 4
            - (arriba)
          - [Choice]: nadie
            - (end)
      - [Choice]: Opciones anteriores.
        - (previous)
      - [Choice]: Nada por ahora.
        - (end)
  - [Choice]: Nada por ahora.
    - (end)

### Inviting player to join a homestead

- Invitando a Player a unirse a su granja.
- (Ventana emergente: Invitando a Player a unirse a su granja.|color=#00FF00)
- (Condition: Player aceptó la invitación:)
  - Player ha aceptado tu invitación.
  - (Ventana emergente: Player ha aceptado su invitación.|color=#00FF00)
- (Condition: Player rechazó la invitación:)
  - Player ha rechazado su invitación.
  - (Ventana emergente: Player ha rechazado su invitación.|advertencia=yes)

#### Ser invitado a unirse a una granja

- [Player] te invita a convertirte en miembro fundador de su granja.}}}}
  - [Choice]: Aceptar
    - ¡Te has unido a la creación de una granja!
    - (Ventana emergente: Player ha rechazado su invitación.|color=#00FF00)
  - [Choice]: Rechazar
    - (end)

### Being invited to swap plot

- [swap plots].}}}}
  - [Choice]: Aceptar
    - Ha intercambiado parcelas con éxito con Player. Su parcela se moverá la próxima vez que se genere su propiedad.
    - (Ventana emergente: Ha intercambiado parcelas exitosamente con Player. Su parcela se moverá la próxima vez que se genere su propiedad).
  - [Choice]: Rechazar
    - (end)

### Aborted the creation of a homestead

- La creación de la propiedad familiar finalizó porque el creador abandonó el grupo.
- (Ventana emergente: La creación de la propiedad familiar finalizó porque el creador abandonó el grupo.|advertencia=yes)

### When the owner finalising the creation

- Necesitas entre 2 y 5 jugadores para crear una granja.
- Te has unido a la granja: '[name]'.
- Su propiedad '[name]' se ha creado correctamente.
- (Ventana emergente: Su propiedad '[name]' se ha creado correctamente.|color=#00FF00)

### Entering house portal when swapping is in progress

- ¡Deberías terminar de intercambiar tu parcela antes de intentar acceder a una casa propiedad del jugador!

### Being kicked from a homestead

- Player ha sido eliminado de la propiedad.
