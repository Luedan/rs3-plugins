local WidgetRequirement = require("src/requirements/widget")

local function norm(s)
  -- strip RS3 formatting tags (<col=..>, <p=N>, <br>, ...) before comparing
  s = tostring(s or ""):gsub("<[^>]*>", " ")
  return (s:gsub("%s+", " "):gsub("^ ", ""):gsub(" $", ""):lower())
end

---@class WidgetTextRequirement: WidgetRequirement
---@field substrings string[]
local WidgetTextRequirement = setmetatable({}, WidgetRequirement)
WidgetTextRequirement.__index = WidgetTextRequirement

---@generic T
---@param self T
---@param componentType "static" | "dynamic" | "interface"
---@param ids integer[]|DynamicEntry[]
---@param substrings string[]
---@param onlyVisible boolean?
---@param latch boolean?
---@return T
function WidgetTextRequirement:new(componentType, ids, substrings, onlyVisible, latch)
  local w = WidgetRequirement.new(self, componentType, ids, onlyVisible, latch)
  w.substrings = type(substrings) == "table" and substrings or {}

  return w
end

function WidgetTextRequirement:_check()
  if self.latch and self.seen then return true end

  local comps = self:getComponents()

  for _, c in ipairs(comps) do
    if self.onlyVisible and (c.hidden or not c.visible) then goto continue end

    ---ignore it since we are checking if text is available
    ---@diagnostic disable-next-line: undefined-field
    local txt = c.content or c.label --[[@as string?]]
    if not txt or txt == "" then goto continue end

    for _, s in ipairs(self.substrings) do
      if norm(txt):find(s:lower(), 1, true) then
        self.seen = true
        return true
      end
    end

    ::continue::
  end

  return false
end

return WidgetTextRequirement
