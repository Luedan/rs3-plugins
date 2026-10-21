# Gestión de Plugins

Esta guía explica cómo activar, desactivar, inspeccionar y recargar plugins en el cliente de RuneScape durante las etapas de desarrollo y pruebas.

---

## Comandos de Consola para Gestión

La consola de desarrollo se abre pulsando **`ALT` + `` ` ``** (tecla sobre Tab y bajo Esc).

### Lista de Plugins (`plist`)
Muestra todos los plugins encontrados en la carpeta `dev_plugins/`, indicando si están activados o desactivados:
```text
plist
```
Salida típica:
```text
Found 2 plugins
    mi-primer-plugin [ENABLED]
    calculadora-xp [DISABLED]
```

### Refrescar Archivos (`prf`)
Reescanea el disco en busca de nuevas carpetas o cambios de nombre en `dev_plugins/`:
```text
prf
```

### Encender un Plugin (`pon`)
Ejecuta el archivo `main.lua` del plugin y lo deja en estado activo:
```text
pon mi-primer-plugin
```

### Apagar un Plugin (`poff`)
Detiene el plugin, elimina sus componentes visuales asociados y desuscribe sus eventos:
```text
poff mi-primer-plugin
```

### Recargar un Plugin (`prl`)
Equivale a ejecutar `poff` seguido de `pon`. **Es el comando más utilizado durante el desarrollo**:
```text
prl mi-primer-plugin
```
Cada vez que edites tu código Lua en tu editor favorito (ej. VS Code), guarda el archivo y escribe `prl <nombre>` en la consola del juego para ver los cambios de inmediato.
