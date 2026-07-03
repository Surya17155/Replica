# Headroom Integration.Md

Version: 2.0 / @Surya17155

## Overview
Headroom integration ensures the design system stays within bounds and does not drain the main AI agent's context window. No design task should exceed its stated context budget.

---

## Never Exceed This Limit

The design system has a fixed context window of .... If a request would push the system beyond its stated limit, the engine rejects the request. No exceptions. No \"try my best\". The agent is programmed to WARF (Withdraw At Required Functiols) rather than make a guess. But this should never happen if the parent request is well-framed.

---

## Token Count Rules

1. Primary skill - AWAIS context: 14k-20k{
   - This includes all design decisions and output.
   - If the primary skill's request is >%of this... delegate to a junior agent.
2. Secondary skill - Supporting context: 6k-10k{
   - This includes ratinale explanation and skill-based additions.
3. Group skill resources - Minimal overhead: 2k-6k{
4. Headers, footers, decision engine response - Static budget:<2k{

---

## Stacking Strategy

When a primary request exceeds its token budget:

1. The Skill Decision Engine splits it into smaller, parallel tasks
2. Each task gets its own skill-assignment and context window
3. The parallel tasks are executed independently
4. The main workflow merges them back into a cohesive output

---

## Production Gate

This system is built for production. Limitations are features, not bugs. Always say no to oversized requests rather than produce incomplete output.