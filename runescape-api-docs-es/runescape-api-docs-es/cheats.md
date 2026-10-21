# Comandos Cheat (Modo Desarrollador)

Esta página contiene la referencia oficial de comandos de prueba (cheats) disponibles exclusivamente en el entorno beta de desarrollo de la RuneScape Client API.

> **Advertencia**  
> Estos comandos no están disponibles en el juego en vivo y solo sirven para simular escenarios de prueba mientras desarrollas tu plugin.

---

## Lista de Comandos Principales

| Comando | Sintaxis | Descripción |
| :--- | :--- | :--- |
| **`tp`** | `tp <x> <y> [plano]` | Teletransporta al jugador a las coordenadas de cuadrícula especificadas. |
| **`tpto`** | `tpto <lugar>` | Teletransporta a un punto de interés por nombre (ej. `varrock`, `ge`). |
| **`give`** | `give <id> [cantidad]` | Añade el objeto con el ID indicado a la mochila del jugador. |
| **`empty`** | `empty` | Elimina todos los objetos del inventario. |
| **`sethp`** | `sethp <valor>` | Establece los puntos de salud actuales del jugador. |
| **`setstats`** | `setstats <nivel>` | Establece todas las habilidades al nivel indicado (ej. 1 o 99). |
| **`anim`** | `anim <id_animacion>` | Hace que el personaje reproduzca una animación específica. |
| **`spotanim`** | `spotanim <id>` | Reproduce un gráfico / efecto visual sobre el personaje. |
| **`camera`** | `camera reset` | Restaura los valores de orientación y distancia de la cámara. |

---

## Teletransportes con Nombre Comunes (`tpto`)

* `lumbridge`: Patio del castillo de Lumbridge.
* `varrock`: Plaza central de Varrock.
* `grandexchange` o `ge`: Centro del Grand Exchange.
* `falador`: Centro de Falador.
* `edgeville`: Banco de Edgeville.
* `prifddinas`: Centro de la ciudad élfica.
* `ar信用dougne`: Plaza del mercado de Ardougne.
* `burthorpe`: Zona de tutoriales y actividades en Burthorpe.

---

## Nombres de Inventarios Útiles (`InvType`)

* `INVENTORY`: Mochila del jugador (28 casillas).
* `EQUIPMENT`: Objetos equipados en el personaje (arma, armadura, capa, etc.).
* `BANK`: Objetos almacenados en el banco.
* `BEAST_OF_BURDEN`: Mochila de un familiar invocador.
