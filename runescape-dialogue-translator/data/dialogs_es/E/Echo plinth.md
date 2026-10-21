# Echo plinth

- **Original Wiki Page**: [Transcript:Echo plinth](https://runescape.wiki/w/Transcript%3AEcho%20plinth)
- **Letter**: `E`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript


### Check

- (Condition: Si el pedestal está vacío:)
  - {{tselect|SELECCIÓN DE ECO
    - Los engramas deben cargarse y entregarse a Orla antes de que puedas mostrar su eco en un pedestal.
    - No es necesario mostrar ecos para ningún efecto beneficioso pasivo.
    - Seleccione un eco para mostrar aquí:
    - *(Se muestran 12 cuadros de engrama. Si el engrama se ha entregado, el cuadro contiene su nombre y una casilla de verificación. Si el engrama ya se ha colocado en un pedestal, el cuadro está atenuado y la casilla de verificación está marcada. Si el engrama no se ha entregado, el cuadro está atenuado y contiene el texto '[Uncharged]' y una casilla de verificación llena con un '?'.)*}}
    - [Choice]: [Clicking any engram that isn't greyed out]
      - (Acción: aparece un eco del engrama seleccionado en el pedestal cuando el player lo invoca con una animación Divination que dura indefinidamente).
    - [Choice]: CANCELAR
      - ((La interfaz se cierra.))
  - (Condición: información sobre herramientas al pasar el cursor sobre un cuadro de engrama:) <!-- in order of appearance in the interface -->
    - Naragi: {{Interface tooltip|Found within the memory of a long-dead world.}}
    - Espada mayor: {{Interface tooltip|Found on the docks of an island devoid of pests.}}
    - Fairy: {{Interface tooltip|Found where the Fairy Queen is seated.}}
    - Gnome: {{Interface tooltip|Found at a dead end in a maze of gnomes.}}
    - Puerta mundial: {{Interface tooltip|Found near the Gate on this world.}}
    - Druida: {{Interface tooltip|Found where you can mix cakes near a stone circle.}}
    - Piedra de Jas: {{Interface tooltip|Found where a bug guards the impact from a fist.}}{{fact|Is this different if Fiara dies during The World Wakes?}}
    - Sheep: {{Interface tooltip|Found in a pen protected by 'The Thing'.}}
    - Hora: {{Interface tooltip|Found where an elven queen rests eternal.}}
    - Espada de los Edictos: {{Interface tooltip|Found where a sharp reminder stands for all to see.}}
    - Guardianes de Guthix: {{Interface tooltip|Found where stories hold back tears of loss.}}
    - Elemento de equilibrio: {{Interface tooltip|Found among druidic standing stones.}}
- (Condition: Si el pedestal tiene eco:)
  - [Menu]: ¿Qué te gustaría hacer?
    - [Choice]: Habla con el eco.
      - ((Vea las transcripciones de Balance Elemental, Druida, Elder Sword, Fairy, Gnome, Guardian of Guthix, Naragi, Time, Sheep, Stone of Jas, Sword of Edicts, World Gate.))
    - [Choice]: Vuelva a colorear este eco.{{fact|Does this show before prestiging?}}
      - [Menu]: ¿Qué color?
        - [Choice]: Azul.
          - (Action: El eco se vuelve azul.)
        - [Choice]: Green.|cond=Después del prestigio 1:
          - (Action: El eco se vuelve verde.)
        - [Choice]: Gold.|cond=Después del prestigio 2:
          - (Action: El eco se vuelve dorado.)
    - [Choice]: Limpia este pedestal.
      - (Action: El eco desaparece del pedestal.)
