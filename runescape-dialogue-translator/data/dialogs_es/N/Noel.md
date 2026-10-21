# Noel

- **Original Wiki Page**: [Transcript:Noel](https://runescape.wiki/w/Transcript%3ANoel)
- **Letter**: `N`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Talk to


#### Durante el período de intercambio

- [Menu]: Selecciona una opción
  - [Choice]: ¿Qué está pasando aquí?
    - **Player:** ¿Qué está pasando aquí?
    - **Noel:** Los Petes me han entregado oficialmente el papel de 'envoltorio oficial de material festivo'. ¡Estoy a cargo ahora!
    - **Noel:** Ya era hora de que me lo entregaran. Lo han hecho un verdadero desastre recientemente.
    - **Noel:** Hablando de eso, acabo de descubrir que lograron perder todo el papel de regalo navideño OTRA VEZ.
    - **Noel:** Y ahora le toca al viejo Noel resolver esto.
    - **Noel:** 'Ese es el problema: no hay posibilidad de que lo encuentre solo. Me vendría bien un poco de ayuda.
    - **Noel:** Te daré un regalo por cada 200 papeles de regalo navideños que encuentres y me los traigas.
    - [Obtendrás papel de regalo navideño a intervalos regulares mientras juegas.]
    - **Player:** ¡Suena bien! Yo te ayudaré.
    - **Noel:** Gracias.
    - (initial)
  - [Choice]: ¿Qué hay en los regalos?
    - (below|Present info)
  - [Choice]: Intercambia papel de regalo navideño.
    - (below|Exchange paper)
  - [Choice]: Adiós.
    - **Player:** ¡Adiós por ahora!
    - **Noel:** Nos vemos.

#### Después del período de intercambio pero antes del final del evento

- El evento ya terminó, pero aún puedes intercambiar cualquier papel que te quede hasta el final del 12 de enero.
- **¿Entregar papel de regalo navideño?**
  - [Choice]: Sí.
    - (below|Exchange paper)
  - [Choice]: No.
    - **Noel:** Nos vemos.

#### Después del final del evento

- El evento no está activo actualmente, por lo que no se puede cambiar ningún papel de regalo navideño.

### Exchange paper


#### Durante el evento


##### Sin al menos 200 papel de regalo navideño en el backpack o en la bolsa de billetes

- **Noel:** No puedo darte ningún regalo hasta que me tengas al menos 200 papeles de regalo navideños.

##### Con al menos 200 papeles de regalo navideños en el backpack o en la bolsa de billetes


##### Sin suficientes espacios libres en backpack

- **Noel:** Necesitas al menos [número] backpack espacios para tus regalos.

##### Con suficientes espacios libres en backpack

- (removes=multiples of 200 Christmas wrapping paper) (receives=one present for each set of 200 paper)
- Intercambias papel de regalo navideño [número] y recibes:
- (Condition: Si se recibieron regalos de Navidad blancos:)
  - [number] x {{Colour}}
  - (continue)
- (Condition: Si se recibieron regalos de Navidad azules:)
  - [number] x {{Colour}}
  - (continue)
- (Condition: Si se recibieron regalos de Navidad morados:)
  - [number] x {{Colour}}
  - (continue)
- (Condition: Si se recibieron regalos de Navidad dorados:)
  - [number] x {{Colour}}
  - (continue)
- (Condition: Si se recibieron los regalos de Navidad de Santa:)
  - [number] x {{Colour}}
  - (continue)
- (ventana emergente)
  - (Ventana emergente: intercambias papel de regalo navideño [número] y recibes:<br>[Each of the above lines that appeared])

#### Después del evento

- El evento no está activo actualmente, por lo que no se puede cambiar ningún papel de regalo navideño.

### Present info

- ((Lo siguiente se muestra en una interfaz titulada "Información actual":))
  - ¡Abre los regalos para obtener botín y tener la oportunidad de ganar premios especiales!
  - [[Archivo:Regalo de Navidad blanca (2025) detail.png
    - [Choice]: Información
      - (opens=White Christmas Present (2025))
      - (Condition: Al seleccionar "ATRÁS":)
        - (previous)
  - [[Archivo:Regalo de Navidad azul (2025) detail.png
    - [Choice]: Información
      - (opens=Blue Christmas Present (2025))
      - (Condition: Al seleccionar "ATRÁS":)
        - (previous)
  - [[Archivo:Regalo de Navidad morado (2025) detail.png
    - [Choice]: Información
      - (opens=Purple Christmas Present (2025))
      - (Condition: Al seleccionar "ATRÁS":)
        - (previous)
  - [[Archivo:Regalo de Navidad dorado (2025) detail.png
    - [Choice]: Información
      - (opens=Gold Christmas Present (2025))
      - (Condition: Al seleccionar "ATRÁS":)
        - (previous)
  - [[Archivo:Regalo de Navidad de Papá Noel (2025) detail.png
    - [Choice]: Información
      - (opens=Santa's Christmas Present (2025))
      - (Condition: Al seleccionar "ATRÁS":)
        - (previous)
