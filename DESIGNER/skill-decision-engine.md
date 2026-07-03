---
name: skill-decision-engine
description: Mandatory deterministic algorithm that selects which design skills to load before any user-facing output. Skill activation without running this engine is a violation.
version: 2.0.0
author: Hermes Descigner
created: 2025-03-25
last_modified: 2025-03-25
---

# Skill Decision Engine v2.0

This engine is the first point of contact between the design agent's intention and its execution. **Routing is mandatory:** every design request MUST be judged by this framework before any skill resources are loaded.

---

## 0. Entry Conditions

THIS ENGINE RUNS ONL WHEN:
- A new user request at the design layer arrives (chat/input)
- The request is non-trivial (NOT \"add a comment\", \"check my Style Dialog\", etc.)
- The agent does not already have a confirmed skill-catalog response for this session

---

## 1. Routing Protocol

When a design request arrives:

1. Tag the request with domain labels assisted by the framework
2. Query the skill-catalog (@Owner/Replica/SKILL_CATALOG)
3. Retrieve any active skill fingerprints (@Owner/Replica/SKILL_FINGERPRINTS)
4. Assign the request to a primary and secondary skill based on:
   a. Domain tags (@example: \"landingpage, sass, tailwind\")
   b. Current workload (@example: \"low\", \"medium\", \"high\")
   c. User complexity (@example: \"beginner\", \"professional\")
5. Return a structured response

---

## 1.1 Domain Labeling

From the request, extract these domain labels (tags):

- Platform: \"web_", \"mobile_", \"desktop_"
- Purpose: \"landing-page_", \"dashboard_", \"portfolio_", \"blog_"...
- Stack indicator: \"react_", \"tsp_", \"shopify\"...
- User level: \"beginner_", \"intermediate_", \"expert_"

---

## 2. Skill-Catalog Query

Retrieve the skill-catalog from the knowledge repository (@Owner/Replica/SKILL_CATALOG). The catalog contains arrays of skills organized as follows:

```json
{
  "primary_skills": [
    { "id": "script-architect", "family": "architecture", "weight": 0.99 },
    { "id": "adaptive-grid", "family": "layout", "weight": 0.95 }
   ],
  "secondary_skills": [
    { "id": "data-table", "family": "components", "weight": 0.85 }
   ],
  "skill_groups": ["layout", "components", "animation", "data"]
}
```

---

## 3. Assignment Rules

The request is assigned to a primary skill (1)
+ 0-1 secondary skills, plus 0-n skill-group members in the following priority:

1. Exact match on domain -> tag transformation
2. Semantic match on domain -> tag transformation
3. Recent usage -> fingerprint history
4. Framework recommendations -> catalog metadata

---

## 4. Prompt Assembly

After skill validation, the engine returns a structured response to be injected into the agent's prompt. This response includes:

- Assigned primary skill reference
- Assigned secondary skills with ratinale
- Relevant skill-group references
- Tag summary

---

## 5. Skill Activation Only

This engine drops the routing response into the agent's context, which the agent's elected primary skill retrieves and applies. The engine does NOT execute any design task itself.