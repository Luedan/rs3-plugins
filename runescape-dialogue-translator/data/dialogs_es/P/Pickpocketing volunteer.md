# Pickpocketing volunteer

- **Original Wiki Page**: [Transcript:Pickpocketing volunteer](https://runescape.wiki/w/Transcript%3APickpocketing%20volunteer)
- **Letter**: `P`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### In the Thieves' Guild


#### Hablando con él o ella

- **Pickpocketing volunteer:** ¡Muy bien! Estoy aquí para que practiques el viejo dippetydoodah. Si quieres saber más, habla con trainer.

#### carterista


##### Fallando

- **Pickpocketing volunteer:** {{RSChat|Spotted you.}}
- Intenta robarle el bolsillo al voluntario.
- No logras robarle el bolsillo al miembro de staff.
- Has quedado atónito.

##### teniendo éxito

- Intenta robarle el bolsillo al voluntario.
- Recuperas un pañuelo azul y se lo devuelves al miembro de staff.
- (Condition: Si aún se pueden ganar puntos para la semana:)
  - [Ganas un punto de pañuelo.]
- (Condition: Si no se pueden ganar más puntos de pañuelo durante la semana:)
  - Has alcanzado el número máximo de puntos de pañuelo permitidos en tu nivel.

#### Puntos de control

- **Player:** ¿Cuántos puntos de pañuelo tengo?
- **Pickpocketing volunteer:** Has recopilado [no hanky points yet/(number) hanky points]. Puedes reclamar la recompensa de hasta [número] puntos de pañuelo más esta semana.
- [Menu]: Selecciona una opción
  - [Choice]: ¿Para qué son todos estos pañuelos?
    - (arriba)
  - [Choice]: Me gustaría reclamar una recompensa por mis puntos de pañuelo.
    - **Player:** ¡Me gustaría reclamar una recompensa por mis puntos de pañuelo!
    - (Condition: Sin puntos complicados que reclamar:)
      - **Pickpocketing volunteer:** ¡No tienes puntos de pañuelo que reclamar! Prueba algunos de los ejercicios de entrenamiento del gremio.
    - (Condition: Con puntos de pañuelo para reclamar:)
      - **Pickpocketing volunteer:** ¡Claro! Veamos ahora...
      - (receives=Thieving XP)
      - [Obtienes [número] Thieving XP. Te quedan 0 puntos y puedes entregar hasta [número] puntos más esta semana.]
    - (Condition: Habiendo reclamado el máximo de puntos del pañuelo de la semana:)
      - **Pickpocketing volunteer:** Lo sentimos, has reclamado tantos puntos de pañuelo esta semana como puedas en tu nivel.
  - [Choice]: Adiós por ahora.
    - ** Player:** Adiós por ahora.
