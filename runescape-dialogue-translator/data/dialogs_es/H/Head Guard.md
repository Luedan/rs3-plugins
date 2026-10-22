# Head Guard

- **Original Wiki Page**: [Transcript:Head Guard](https://runescape.wiki/w/Transcript%3AHead%20Guard)
- **Letter**: `H`
- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)

---

## Dialogue Transcript

{{Incomplete|missing dialogue for players with higher clan rank & citadels of other languages besides English}}

### Dialogue

- **Head Guard:** ¿Necesitas algo, [sir/ma'am]?
- [Menu]: Selecciona una opción
  - [Choice]: Me gustaría una capa de clan.
    - (Condition: If the player already has a clan cloak:)
      - **Head Guard:** ¡Ya te he regalado uno!
      - (previous)
    - (Condition: If the player does not have a clan cloak:)
      - **Head Guard:** Por supuesto. Aquí tiene.
      - El capitán te da una capa.
      - (receives=a clan cloak)
      - (previous)
  - [Choice]: Me gustaría un clan vexillum.
    - (Condition: If the player already has a clan vexillum:)
      - **Head Guard:** ¡Ya te he regalado uno!
      - (previous)
    - (Condition: If the player does not have a clan vexillum:)
      - **Head Guard:** Por supuesto. Aquí tiene.
      - El capitán te da un vexillum.
      - (receives=a clan vexillum)
      - (previous)
  - [Choice]: ¿Cómo cambio los permisos de mi clan?
    - **Head Guard:** Puedes acceder a la configuración de tu clan haciendo clic en la pestaña 'permisos' en la 'interfaz de configuración del clan', accesible desde la lista de clanes. Elija una clasificación de la lista de la izquierda y una categoría de la parte superior para ver qué permisos tiene cada clasificación y haga clic en una opción para activarla o desactivarla. Recuerde, sin embargo, que no puede alterar los permisos de ningún jugador de su propio rango o superior, y que a algunas opciones solo pueden acceder aquellos con acceso de administrador o superior. Además, la categoría de chat funciona ligeramente diferente a las demás, ya que estableces el rango mínimo para hablar o patear, en lugar de establecer permisos para cada rango individualmente. ¿Le gustaría saber más sobre una categoría específica?
    - [Menu]: Selecciona una opción
      - [Choice]: Administrador.
        - **Head Guard:** La categoría de administrador te permite cambiar los permisos para todas las acciones administrativas dentro de tu clan. Esto incluye reclutar, acceder a la ciudadela y torreón del clan, y liderar Guerras de clanes puntuadas.
        - (previous)
      - [Choice]: Eventos.
        - La categoría de eventos te permite cambiar los permisos relacionados con los eventos del clan. Esto incluye agregar avisos al tablero, iniciar una reunión, realizar una votación o iniciar un juego en el campo de batalla del clan. El acceso a los controles del salón de fiestas y del teatro también se controla desde la página de eventos.
        - (previous)
      - [Choice]: Ciudadela.
        - La categoría ciudadela le permite cambiar los permisos relacionados con las operaciones de construcción de la ciudadela. Esto incluye marcar edificios para mejorarlos o degradarlos y cambiar el diseño del campo de batalla del clan. Sin embargo, debes tener el rango de supervisor o superior para mover el tic de construcción.
        - (previous)
      - [Choice]: Habilidades.
        - La categoría de habilidades te permite cambiar los permisos relacionados con las habilidades dentro de la ciudadela del clan. Esto incluye cosas como establecer objetivos de recursos y cambiar el día del tick de compilación.
        - (previous)
      - [Choice]: Atrás.
        - (initial)
  - [Choice]: Me gustaría cambiar el idioma de mi ciudadela.
    - (Condition: If the clan citadel is affined to English servers:)
      - **Head Guard:** Tu ciudadela actualmente está vinculada a servidores de habla inglesa.
    - (Condition: If the clan citadel is affined to other language servers:)
      - {{Transcript missing}}
    - (Condition: If the player has permissions to change the language:)
      - {{Transcript missing}}
    - (Condition: If the player does not have permissions to change the language:)
      - **Head Guard:** Me temo que no tienes los permisos necesarios para eso, [sir/ma'am].
      - (previous)
  - [Choice]: Me gustaría cambiar la configuración de visibilidad del chat de mi ciudadela.
    - (Condition: If the player is the clan owner:)
      - {{Transcript missing}}
    - (Condition: If the player is not the clan owner:)
      - Sólo el propietario del clan puede cambiar esta configuración.
      - (end)
