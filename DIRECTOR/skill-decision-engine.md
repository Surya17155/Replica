# Skill Decision Engine.Md

Version: 2.0 / @Surya17155

## Overview
This is the core routing shim for the design system. It determines which design skills to load for any given request based on domain tags, skill catalog data, and active fingerprints.

---

## Triggers

The engine is triggered when:
1. A new user request arrives (chat/input layer)
2. The request is non-trivial
3. The agent does not already have a confirmed skill-catalog response for this session

---

## Protocol

1. Tag the request with domain labels
2. Query the skill-catalog
3. Retrieve any active skill fingerprints
4. Assign the request to a primary skill and 0-1 secondary skill
5. Return a structured response

---

## Assignment Rules

1. Exact match on domain tag
2. Semantic match on domain tag
3. Recent usage - fingerprint history
4. Framework recommendation

Response includes: assigned primary skill, assigned secondary skills with ratinale, relevant skill groups, tag summary.