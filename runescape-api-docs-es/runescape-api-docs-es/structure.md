# Estructura del Plugin

Este documento describe la organización de carpetas y archivos requerida para empaquetar un plugin listo para desarrollo y publicación.

---

## Estructura de Directorios

Un plugin típico se compone de los siguientes archivos:

```text
nombre-del-plugin/
├── plugin.json         -- Manifiesto con metadatos del plugin (Obligatorio)
├── main.lua            -- Punto de entrada del código en Lua (Obligatorio)
├── icon.png            -- Icono representativo de 64x64 o 128x128 píxeles
├── README.md           -- Descripción para la tienda de Mod.io
└── modules/            -- Módulos Lua secundarios importables (Opcional)
    ├── ui_view.lua
    └── helpers.lua
```

---

## El Manifiesto (`plugin.json`)

El archivo `plugin.json` debe contener metadatos válidos en formato JSON.

### Ejemplo Completo
```json
{
    "name": "RuneMetrics Local",
    "version": "1.0.0",
    "description": "Calcula experiencia ganada por hora y muestra estadísticas en pantalla.",
    "contactEmailAddress": "desarrollador@ejemplo.com",
    "permissions": [
        "http",
        "persistent_db"
    ],
    "dependencies": {}
}
```

### Campos del Manifiesto

| Campo | Tipo | Requerido | Descripción |
| :--- | :--- | :--- | :--- |
| **`name`** | String | Sí | Nombre público del plugin. |
| **`version`** | String | Sí | Versión en formato semántico (ej. `1.0.0`). |
| **`description`** | String | Recomendado | Breve resumen de lo que hace el plugin. |
| **`contactEmailAddress`** | String | Sí | Correo electrónico de contacto del desarrollador. |
| **`permissions`** | Array | No | Lista de permisos especiales requeridos (ej. `http`). |

---

## Permisos (`permissions`)

Por motivos de seguridad, ciertas capacidades de la API requieren declaración explícita en `plugin.json`:

* **`http`**: Necesario si el plugin realiza peticiones web externas mediante `core.Http`.
* **`persistent_db`**: Acceso al almacenamiento local de datos con `core.PersistentDB`.

Si tu plugin intenta usar una función que requiere un permiso no declarado, el motor de RuneScape bloqueará la llamada y registrará un error en la consola.
