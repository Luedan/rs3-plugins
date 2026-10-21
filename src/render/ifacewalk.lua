-- Walk the components of a loaded interface.
local M = {}

local function safe(fn)
  local ok, v = pcall(fn)
  if ok then return v end
end

local function recurse(node, visit, depth, budget)
  if node == nil or depth > budget.maxDepth or budget.n <= 0 then return end
  for _, method in ipairs({ "IterateDynamicComponents", "IterateStaticComponents" }) do
    pcall(function()
      node[method](node, function(child, visible)
        if budget.n <= 0 then return true end
        budget.n = budget.n - 1
        visit(child, node, visible, depth)
        recurse(child, visit, depth + 1, budget)
        return budget.n <= 0
      end)
    end)
  end
end

function M.walk(ifaceId, visit, opts)
  opts = opts or {}
  local iface = safe(function() return ui.Interfaces:GetInterface(ifaceId) end)
  if iface == nil then return false end
  local budget = { n = opts.maxComps or 1200, maxDepth = opts.maxDepth or 10 }
  local maxStatic = opts.maxStatic or 400
  for sid = 0, maxStatic do
    if budget.n <= 0 then break end
    local comp = safe(function() return iface:GetComponent(sid) end)
    if comp ~= nil then
      budget.n = budget.n - 1
      visit(comp, nil, true, 0)
      recurse(comp, visit, 1, budget)
    end
  end
  return true
end

return M
