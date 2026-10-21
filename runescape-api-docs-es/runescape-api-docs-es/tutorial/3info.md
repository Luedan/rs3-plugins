# 3. Recuperar Información del Juego

En este tutorial aprenderemos a consultar información directamente desde el motor del cliente, sin depender de fuentes externas que puedan estar desactualizadas.

---

## Objetivos
* Conocer la diferencia entre datos estáticos y datos dinámicos.
* Consultar definiciones estáticas de objetos y NPCs (`Config`).
* Leer información en tiempo real del jugador (`Player`) y de su inventario (`Inventory`).
* Mostrar estos datos en nuestra ventana de interfaz.

---

## Información Estática vs. Dinámica

| Tipo | Definición | Ejemplos |
| :--- | :--- | :--- |
| **Estática** | No cambia durante la partida; define cómo es un elemento en el juego. | Nombre de un objeto, descripción, estadísticas de un NPC, animaciones. |
| **Dinámica** | Cambia en cualquier momento según las acciones del jugador o del servidor. | Puntos de vida actuales, posición del jugador, objetos en la mochila. |

---

## 1. Consultar Información Estática: `ObjType` (Objetos)

Para obtener información sobre un objeto por su ID (por ejemplo, el Látigo abisal, ID `4151`):

```lua
local whipConfig = game.config.ObjType.Get(4151)

if whipConfig then
    print("Nombre del objeto:", whipConfig.name)
    print("Es comerciable:", whipConfig.tradeable)
end
```

---

## 2. Consultar Información Dinámica: El Jugador y su Inventario

### Obtener el Jugador Local (`Player.GetLocal()`)
```lua
local yo = game.Player.GetLocal()

if yo then
    print("Mi nombre:", yo.name)
    print("Nivel de combate:", yo.combatLevel)
    
    -- Posición en coordenadas de cuadrícula (Grid Units)
    local pos = yo.coordGrid
    print(string.format("Ubicación: [%d, %d, piso %d]", pos.x, pos.y, pos.plane))
end
```

### Consultar el Inventario (Mochila)
```lua
local inv = game.Inventory.Get(game.config.InvType.INVENTORY)

if inv then
    print("Espacios ocupados:", inv.size)
    for index, item in ipairs(inv:GetItems()) do
        local info = game.config.ObjType.Get(item.id)
        local nombre = info and info.name or "Desconocido"
        print(string.format("Casilla %d: %s x%d", index, nombre, item.count))
    end
end
```

---

## Integración con la Interfaz

Podemos unir lo aprendido en el tutorial anterior: un botón que al pulsarlo lea el nombre del jugador y lo muestre en una etiqueta de texto en pantalla:

```lua
local etiqueta = ui.Text.new()
etiqueta.text = "Pulsa el botón para leer datos"
etiqueta.x = 20
etiqueta.y = 80
panel:AddComponent(etiqueta)

boton:OnClick(function()
    local jugador = game.Player.GetLocal()
    if jugador then
        etiqueta.text = string.format("Jugador: %s (Nivel %d)", jugador.name, jugador.combatLevel)
    else
        etiqueta.text = "No conectado"
    end
end)
```

---

## Siguiente Tutorial
En lugar de presionar un botón manualmente, hagamos que el plugin reaccione automáticamente a lo que ocurre en el juego:  
➡️ **[4. Sistema de Eventos](4events.md)**
