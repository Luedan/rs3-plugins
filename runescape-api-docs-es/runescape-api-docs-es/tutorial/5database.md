# 5. Base de Datos Persistente

Hasta ahora, cualquier variable almacenada en Lua se pierde en cuanto el plugin se recarga o el juego se cierra. En este tutorial aprenderás a usar **`core.PersistentDB`** para guardar configuraciones, contadores o estadísticas permanentemente en el disco.

---

## Objetivos
* Almacenar datos persistentes con clave-valor.
* Leer datos almacenados al inicializar el plugin.
* Manejar tipos de datos admitidos (cadenas, números, booleanos, tablas).
* Gestionar valores por defecto cuando no existe un dato previo.

---

## Uso de `core.PersistentDB`

Cada plugin tiene su propio espacio aislado en la base de datos local SQLite administrada por el cliente. No hay riesgo de colisión con otros plugins.

### Guardar Datos (`Set`)
```lua
-- Guardar datos simples
core.PersistentDB.Set("conteo_clics", 42)
core.PersistentDB.Set("usuario_activo", true)
core.PersistentDB.Set("color_favorito", "dorado")

-- Guardar tablas / estructuras (se serializan automáticamente)
local opciones = {
    mostrarMinimapa = true,
    alertaSonido = false,
    umbralSalud = 50
}
core.PersistentDB.Set("ajustes", opciones)
```

### Leer Datos (`Get`)
```lua
-- Obtener un valor; si no existe, devuelve nil
local clics = core.PersistentDB.Get("conteo_clics") or 0
print("Total clics registrados:", clics)

local ajustes = core.PersistentDB.Get("ajustes")
if ajustes then
    print("Umbral de salud configurado:", ajustes.umbralSalud)
end
```

### Eliminar Datos (`Delete`)
```lua
core.PersistentDB.Delete("conteo_clics")
```

---

## Ejemplo Práctico: Contador Persistente

Un plugin simple que recuerda cuántas veces has pulsado el botón en todas tus sesiones:

```lua
local ventana = ui.Interface.new("ContadorPersistente")
local panel = ui.Panel.new()
ventana:AddComponent(panel)

-- Recuperamos el conteo previo o arrancamos en 0
local totalClics = core.PersistentDB.Get("total_clics") or 0

local texto = ui.Text.new()
texto.text = "Clics totales: " .. totalClics
panel:AddComponent(texto)

local boton = ui.Button.new()
boton.text = "+1 Clic"
boton:OnClick(function()
    totalClics = totalClics + 1
    texto.text = "Clics totales: " .. totalClics
    
    -- Guardamos inmediatamente en la base de datos
    core.PersistentDB.Set("total_clics", totalClics)
end)
panel:AddComponent(boton)
```

---

## Siguiente Tutorial
Herramientas avanzadas de prueba en el entorno de desarrollo:  
➡️ **[6. Comandos Cheat de Desarrollador](6cheats.md)**
