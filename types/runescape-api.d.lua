---@meta
--- Declaraciones de tipos y autocompletado para RuneScape Client API (Lua 5.4.8)

--- ============================================================================
--- GLOBALES DEL MOTOR
--- ============================================================================

--- Imprime un mensaje en la consola de depuración de RuneScape.
---@param ... any
function print(...) end

--- Imprime un mensaje prefijado con el nombre de tu plugin en la consola.
---@param format string|any
---@param ... any
function log(format, ...) end

--- Ejecuta un comando en la consola interna del cliente del juego.
---@param command string
function ExecuteConsoleCommand(command) end

--- Función de ciclo de vida que el motor invoca cuando el plugin es desactivado o recargado.
--- Debe definirse a nivel global en tu main.lua.
function PluginShutdown() end

--- ============================================================================
--- CORE: PERSISTENT DB
--- ============================================================================

---@class PersistentDB
PersistentDB = {}

--- Obtiene un valor almacenado para la clave indicada.
---@param key string
---@return boolean|number|string|table|nil
function PersistentDB:Get(key) end

--- Obtiene un valor booleano almacenado.
---@param key string
---@return boolean|nil
function PersistentDB:GetBool(key) end

--- Obtiene un número entero almacenado.
---@param key string
---@return integer|nil
function PersistentDB:GetInt(key) end

--- Obtiene un número de punto flotante almacenado.
---@param key string
---@return number|nil
function PersistentDB:GetFloat(key) end

--- Obtiene una cadena de texto almacenada.
---@param key string
---@return string|nil
function PersistentDB:GetString(key) end

--- Obtiene una tabla/estructura serializada almacenada.
---@param key string
---@return table|nil
function PersistentDB:GetStructuredData(key) end

--- Almacena un valor asociado a una clave.
---@param key string
---@param value boolean|number|string|table
---@return boolean
function PersistentDB:Set(key, value) end

--- Almacena un valor booleano.
---@param key string
---@param value boolean
---@return boolean
function PersistentDB:SetBool(key, value) end

--- Almacena un número entero.
---@param key string
---@param value integer
---@return boolean
function PersistentDB:SetInt(key, value) end

--- Almacena un número flotante.
---@param key string
---@param value number
---@return boolean
function PersistentDB:SetFloat(key, value) end

--- Almacena una cadena de texto.
---@param key string
---@param value string
---@return boolean
function PersistentDB:SetString(key, value) end

--- Almacena una tabla serializable.
---@param key string
---@param value table
---@return boolean
function PersistentDB:SetStructuredData(key, value) end

--- Comprueba si existe una clave almacenada.
---@param key string
---@return boolean
function PersistentDB:CheckExists(key) end

--- Elimina una clave de la base de datos persistente.
---@param key string
---@return boolean
function PersistentDB:Delete(key) end

--- ============================================================================
--- CORE: PLUGIN
--- ============================================================================

---@class Plugin
Plugin = {
    resources = {},
    urls = {}
}

--- Comprueba si el plugin cuenta con un permiso específico otorgado.
---@param permission string
---@return boolean
function Plugin.HasPermission(permission) end

--- ============================================================================
--- SISTEMA DE EVENTOS
--- ============================================================================

---@class EventChannel
---@field Subscribe fun(referenceName: string, callback: fun(event: any): any)
---@field Unsubscribe fun(referenceName: string)

---@class EventContainer
---@field ServerLogic EventChannel
---@field Logic EventChannel
---@field ContentLayerReady EventChannel
---@field SettingsLayerReady EventChannel
---@field GameStateChanged EventChannel
---@field Draw EventChannel
---@field Logic EventChannel
---@field ServerLogic EventChannel
---@field InventoryUpdated EventChannel
---@field InventoryAdded EventChannel
---@field InventoryRemoved EventChannel
---@field ChatMessage EventChannel
---@field KeyDown EventChannel
---@field KeyUp EventChannel
---@field KeyTyped EventChannel
---@field EntityDraw EventChannel
---@field NPCEntityAdded EventChannel
---@field NPCEntityRemoved EventChannel
---@field PlayerEntityAdded EventChannel
---@field PlayerEntityRemoved EventChannel
---@field ObjStackEntityAdded EventChannel
---@field ObjStackEntityRemoved EventChannel
---@field WindowFocusChanged EventChannel
---@field WindowSizeChanged EventChannel
---@field MiniMenuOpened EventChannel
---@field MiniMenuClosed EventChannel
---@field MiniMenuReady EventChannel
---@field MiniMenuEntryAdded EventChannel
---@field MiniMenuEntrySelected EventChannel

---@type EventContainer
Event = {}

--- ============================================================================
--- GAME: JUGADOR Y ENTIDADES
--- ============================================================================

---@class CoordGrid
---@field x integer
---@field z integer
---@field level integer
---@field mapSquareX integer
---@field mapSquareZ integer
---@field localX integer
---@field localZ integer

---@class PlayerEntity
---@field isValid boolean
---@field displayName string
---@field coordGrid CoordGrid
---@field combatLevel integer
---@field currentHealth integer
---@field maxHealth integer

---@class Player
Player = {}

--- Comprueba si el personaje del jugador está disponible y conectado al mundo.
---@return boolean
function Player.IsAvailable() end

--- Devuelve la entidad del personaje del jugador local.
---@return PlayerEntity
function Player.GetEntity() end

--- Devuelve el nivel de combate del jugador.
---@return integer
function Player.GetCombatLevel() end

--- Devuelve el porcentaje de energía de correr actual (0 - 100).
---@return integer
function Player.GetRunEnergy() end

--- Devuelve el peso del jugador en kilogramos.
---@return integer
function Player.GetWeight() end

--- Devuelve el nivel de juego (incluyendo bonificaciones o penalizaciones).
---@param skill integer
---@return integer
function Player.GetLevelGameplay(skill) end

--- Devuelve el nivel basado en experiencia (limitado por F2P/P2P).
---@param skill integer
---@return integer
function Player.GetLevelCapped(skill) end

--- Devuelve el nivel no limitado según la XP real.
---@param skill integer
---@return integer
function Player.GetLevelUncapped(skill) end

--- Devuelve la XP acumulada en una habilidad.
---@param skill integer
---@return integer
function Player.GetXPUncapped(skill) end

---@class PlayerList
PlayerList = {}

--- Devuelve la entidad del propio jugador.
---@return PlayerEntity
function PlayerList.Self() end

--- ============================================================================
--- GAME: INVENTARIO
--- ============================================================================

---@class InvSlot
---@field id integer
---@field count integer

---@class Inv
---@field isValid boolean
---@field size integer
---@field GetSlot fun(self: Inv, index: integer): InvSlot?

---@class Inventory
Inventory = {}

--- Busca un contenedor de inventario según su ID o configuración.
---@param id integer
---@return Inv?
function Inventory.Find(id) end

--- ============================================================================
--- UI: COMPONENTES NATIVOS
--- ============================================================================

---@class ui_Component
---@field width integer
---@field height integer
---@field x integer
---@field y integer
---@field hidden boolean
---@field visible boolean (Solo lectura)
---@field visibleGlobal boolean (Solo lectura)
---@field stylesheetID integer?
---@field SetSize fun(self: ui_Component, width: integer, height: integer, parentPercentX: number?, parentPercentY: number?)
---@field SetPos fun(self: ui_Component, x: integer, y: integer, parentPercentX: number?, parentPercentY: number?, selfPercentX: number?, selfPercentY: number?)

---@class ui_Panel : ui_Component
---@field AddComponent fun(self: ui_Panel, child: ui_Component)

---@class ui_Button : ui_Component
---@field label string
---@field canToggle boolean
---@field isToggled boolean
---@field OnClick fun(self: ui_Button, callback: fun())
---@field Subscribe fun(self: ui_Button, hookId: integer, callback: fun(btn: ui_Button, toggled: boolean?))

---@class ui_Text : ui_Component
---@field content string
---@field colour any

---@class ui_Layer : ui_Component
---@class ui_Rectangle : ui_Component

---@class ui
ui = {
    Component = {},
    Panel = {},
    Button = {},
    Text = {},
    Layer = {},
    Rectangle = {},
    Interfaces = {}
}

---@class PrettyUISimpleView
---@field AddTitle fun(self: PrettyUISimpleView, text: string)
---@field AddText fun(self: PrettyUISimpleView, text: string)
---@field AddDivider fun(self: PrettyUISimpleView)
---@field AddSimpleButton fun(self: PrettyUISimpleView, options: table)
---@field AddCheckboxButton fun(self: PrettyUISimpleView, items: table, options: table)
---@field Destroy fun(self: PrettyUISimpleView)

---@class prettyui
prettyui = {
    SimpleView = {
        ---@param parent ui_Component
        ---@param opts { width: integer, height: integer }
        ---@return PrettyUISimpleView
        new = function(parent, opts) end
    }
}

--- ============================================================================
--- ENUMS COMUNES
--- ============================================================================

---@enum SkillType
SkillType = {
    ATTACK = 0,
    DEFENCE = 1,
    STRENGTH = 2,
    HITPOINTS = 3,
    RANGED = 4,
    PRAYER = 5,
    MAGIC = 6,
    COOKING = 7,
    WOODCUTTING = 8,
    FLETCHING = 9,
    FISHING = 10,
    FIREMAKING = 11,
    CRAFTING = 12,
    SMITHING = 13,
    MINING = 14,
    HERBLORE = 15,
    AGILITY = 16,
    THIEVING = 17,
    SLAYER = 18,
    FARMING = 19,
    RUNECRAFTING = 20,
    HUNTER = 21,
    CONSTRUCTION = 22,
    SUMMONING = 23,
    DUNGEONEERING = 24,
    DIVINATION = 25,
    INVENTION = 26,
    ARCHAEOLOGY = 27,
    NECROMANCY = 28
}

---@enum EntityType
EntityType = {
    PLAYER = 0,
    NPC = 1,
    LOC = 2,
    OBJ_STACK = 3
}

---@enum GameState
GameState = {
    STARTING = 0,
    LOGIN = 10,
    LOBBY = 20,
    GAME = 30
}

---@class id
id = {
    Component = {
        TOPLEVEL_V2__GAME_AREA = 0
    },
    Interface = {},
    StyleSheet = {},
    NPC = {}
}
