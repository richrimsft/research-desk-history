---
name: Routine healthcheck
description: >-
  Use this when a Monday routine-healthcheck fires, or when auditing
  scheduled/event routines for waste, overlap, or broken prompts.
---
# Routine healthcheck

Audit routines across same-account bots for token waste, bad cadence, and broken prompts. Report only; never edit routines until the user approves.

## Scope
1. List active same-account bots and each bot’s current routines (authoritative list from the runtime, not a local folder).
2. Skip deleted agents with no remaining routines.

## Flags worth proposing
- Too-frequent schedules with repeated empty/no-op runs
- Quiet-hours or weekend fires that do not match the user’s real hours (unless the user explicitly wanted them)
- Prompts that point at missing skills, dead paths, or obsolete tools
- Duplicate monitors that cover the same job
- Auth-dependent routines that keep failing the same way

## Clean
Routines that look correctly scoped and quiet-when-empty need no mention.

## Output
- If nothing worth changing: **stay silent**.
- If findings: hand the parent a short list (bot, routine id/name, flag, suggested fix). Ask the user before any create/update/pause/delete.
