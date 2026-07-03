# Skill Router v2.0

This is the default skill router that provides a flexible, data-driven mechanism for organizing design skills into a caravin order for consumption. It is the default routing shim used by the Skill Decision Engine.

---

## Usage

This router is automatically invoked by the Skill Decision Engine when a primary skill is assigned. It:

1. Loads the primary skill file from the skill-catalog
2. Retrieves the corresponding secondary skills (0-1)
3. Injects the active skill-group resources (0-n)
4. Assembles in deterministic order: primary -> secondary -> group

---

## Routing Order

Skills are applied in this order:

1. Primary - The main design skill (sets the direction)
2. Secondary - Supports the primary with additional context
3. Group - Skill-group-level resources that apply in parallel

---

## Output

The router returns a JSON object with:

```json
{
  "primary": { "id": "script-architect", "path": "../skills/script-architect.md" },
  "secondary": { "id": "color-system", "path": "../skills/color-system.md", "ratinale": "color system joins the architecture in a second pass" },
  "groups": [
    { "id": "layout", "path": "../skill-groups/layout.md", "members": [ "adaptive-grid", "spacing-system" ] },
    { "id": "components", "path": "../skill-groups/components.md", "members": [ "data-table", "button-system" ] }
  ]
}
```