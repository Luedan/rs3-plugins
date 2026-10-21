local WidgetRequirement = require("src/requirements/widget")
local WidgetTextRequirement = require("src/requirements/widgettext")

---@class DialogRequirement: WidgetTextRequirement
---@field substrings string[]
local DialogRequirement = setmetatable({}, WidgetTextRequirement)
DialogRequirement.__index = DialogRequirement

DialogRequirement.DIALOG_IDS = {
  id.Component.CHAT_V2_LEFT__CHAT_TEXT,
  id.Component.CHAT_V2_RIGHT__CHAT_TEXT,
}

DialogRequirement.MESSAGE_IDS = { id.Interface.MESBOX_V2 }

---@generic T
---@param self T
---@param substrings string | string[]
---@param onlyVisible boolean?
---@param latch boolean?
---@return T
function DialogRequirement:new(substrings, onlyVisible, latch)
  substrings = type(substrings) == "table" and substrings or { substrings }

  local w = WidgetTextRequirement.new(self, "static", DialogRequirement.DIALOG_IDS, substrings, onlyVisible, latch)

  return w
end

---Text in the game's message box rather than in someone's mouth. Walks the interface instead of
---naming a component: the box is rebuilt per message and the text does not keep the same one.
---@generic T
---@param self T
---@param substrings string | string[]
---@param onlyVisible boolean?
---@param latch boolean?
---@return T
function DialogRequirement:message(substrings, onlyVisible, latch)
  substrings = type(substrings) == "table" and substrings or { substrings }

  return WidgetTextRequirement.new(self, "interface", DialogRequirement.MESSAGE_IDS, substrings, onlyVisible, latch)
end

---Use this to just check if a dialog is active, regardless which text is shown
---@generic T
---@param self T
---@param onlyVisible boolean?
---@param latch boolean?
---@return T
function DialogRequirement:active(onlyVisible, latch)
  local w = WidgetRequirement:new("static", DialogRequirement.DIALOG_IDS, onlyVisible, latch)
  return w
end

return DialogRequirement
