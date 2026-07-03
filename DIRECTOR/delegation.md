# Delegation.Md

Version: 2.0 / @Surya17155

## Overview
Delegation manages junior agent roles in the design system. It defines how and when tasks are assigned based on complexity, domain, and agent capacity.

---

## Delegation Triggers

The Skill Decision Engine delegates to a junior agent when:

1. The request falls below a predefined complexity threshold
2. The primary skill can be applied without supervision
3. The assigned secondary skill ratinale reaches a confidence threshold

---

## Agent Roles

|Responsibility|Description|Trigger|
|---------------|--------------|---------|
|Primary Designer|Full design execution|All requests|
|Secondary Support|Specialized skill application|Assigned by decision engine|

---

## Junior Agent Response Model

When delegating, the supervisor provides:
1. Exact skill reference (@.d/routing)
2. No-estimate completion time - returns when done
3. Status reporting on completion
4. Production-ready deliverable
