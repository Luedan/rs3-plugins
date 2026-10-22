# Plank maker

- **Original Wiki Page**: [Transcript:Plank maker](https://runescape.wiki/w/Transcript%3APlank%20maker)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Buy plank


#### Antes de comenzar No hay lugar como el hogar...

- ((The following is shown in an interface titled "CONSTRUCTION":))
  - 54px Debes completar el tutorial de Construction antes de poder utilizarlo.
  - Hable con Alfred Stonemason, al noroeste de Rimmington, para obtener más información.
    - [Choice]: bien
      - ((The interface closes.))

#### Durante No hay lugar como el hogar...

- (ver|No hay lugar como el hogar...)

#### Después de completar No hay lugar como el hogar...


##### Sin ningún logs adecuado en backpack

- (Se muestra en una ventana emergente:)
  - (Pop-up: You are not carrying any logs to cut into planks.|colour=#EBE0BC)

##### Con logs adecuado en backpack

- ((The following is shown in an interface titled "SAWMILL":))
- Elige una tabla para hacer.
  - [Choice]: Tablón<br>Coste cada uno: 100 x coins
    - (abajo2|Al elegir una opción)
  - [Choice]: Tablón de roble<br>Coste cada uno: 250 x coins
    - (abajo2|Al elegir una opción)
  - [Choice]: Tablón de sauce<br>Coste cada uno: 250 x coins
    - (abajo2|Al elegir una opción)
  - [Choice]: Tablón de teca<br>Coste cada unidad: 500 x coins
    - (abajo2|Al elegir una opción)
  - [Choice]: Tablón de arce<br>Coste cada uno: 250 x coins
    - (abajo2|Al elegir una opción)
  - [Choice]: Plancha Acadia<br>Costo cada uno: 500 x coins
    - (abajo2|Al elegir una opción)
  - [Choice]: Tablón de caoba<br>Coste cada uno: 1.500 x coins
    - (abajo2|Al elegir una opción)
  - [Choice]: Más
    - Elige una tabla para hacer.
      - [Choice]: Tablón de tejo<br>Coste cada uno: 2000 x coins
        - (abajo2|Al elegir una opción)
      - [Choice]: Plancha Magic<br>Coste cada una: 3.500 x coins
        - (abajo2|Al elegir una opción)
      - [Choice]: Tablón de anciano<br>Coste cada uno: 5,000 x coins
        - (abajo2|Al elegir una opción)
      - [Choice]: Más
        - (previous)

##### Al elegir una opción

- {{Tinput|How many [type] logs would you like to make into planks? (0 - [number])<br>Cost each: [number])}}
- ((After entering a positive amount:))
  - (Condition: Without sufficient money:)
    - No puedes darte el lujo de hacer tantos planks.
    - ((Repeated in a pop-up:))
      - (Pop-up: You cannot afford to make that many planks.|colour=#EBE0BC)
  - (Condition: With sufficient money:)
    - (removes=coins) (receives=planks)

### Talk to


#### Antes de comenzar No hay lugar como el hogar...

- ((The following is shown in an interface titled "CONSTRUCTION":))
  - 54px Debes completar el tutorial de Construction antes de poder utilizarlo.
  - Hable con Alfred Stonemason, al noroeste de Rimmington, para obtener más información.
    - [Choice]: bien
      - ((The interface closes.))

#### Durante No hay lugar como el hogar...

- (ver|No hay lugar como el hogar...)

#### Después de completar No hay lugar como el hogar...

- **Plank maker:** Hola. ¿Quieres que te haga un poco de planks?
- [Menu]: Elige una opción:
  - [Choice]: Planks, por favor.
    - **Plank maker:** ¿Qué tipo de planks quieres?
    - (continue|Buy plank option)
  - [Choice]: ¿Qué tipo de planks puedes hacer?
    - **Plank maker:** Puedo hacer planks con madera, roble, teca y caoba. No hago planks con otras maderas porque no sirven para hacer furniture.
    - **Plank maker:** La madera y el roble están por todas partes, pero la teca y la caoba solo se pueden encontrar en unos pocos lugares como Karamja y Etceteria.
  - (initial)
  - [Choice]: Nada, gracias.
    - **Player:** Nada, gracias.
    - **Plank maker:** Bueno, vuelve cuando quieras. ¡No puedes conseguir planks de buena calidad en ningún otro lugar que no sea aquí!

### Trade


#### Antes de comenzar No hay lugar como el hogar...

- ((The following is shown in an interface titled "CONSTRUCTION":))
  - 54px Debes completar el tutorial de Construction antes de poder utilizarlo.
  - Hable con Alfred Stonemason, al noroeste de Rimmington, para obtener más información.
    - [Choice]: bien
      - ((The interface closes.))

#### Durante No hay lugar como el hogar...

- (ver|No hay lugar como el hogar...)

#### Después de completar No hay lugar como el hogar...

- (opens=Sawmill Co. - A 'G.H.A' Subsidiary)
