---
name: Transcript healthcheck
description: >-
  Use this when a weekday transcript-healthcheck routine fires, or when auditing
  chat friction across same-account bots via ReadTranscript.
---
# Transcript healthcheck

Mine recent chat friction across bots on this account. Report only; never create skills, bots, or routines from the report alone.

## Window
- Prefer **since last successful run** of this healthcheck when that timestamp is known.
- Otherwise use the **last 24 hours**.

## Scope
1. List **same-account bots** currently active (this bot and peers). Skip deleted agents.
2. For each bot, page history with **ReadTranscript** (`agent_id`, `before`, reasonable `limit`). Do **not** read `/home/box/agent-data/agent-transcripts` or other on-disk transcript mirrors — they stay empty on server-side Grok Bot.
3. Skip `sand-subagent-` noise and pure automation plumbing that is not user-facing friction.

## What counts as friction
Actionable patterns only, for example:
- Repeated failed tool/auth loops the user had to push past
- Confusing ask-backs or wrong assumptions that wasted turns
- Missing skills or broken routine prompts that blocked a job
- Clear UX/process pain the user expressed

Ignore empty success noise and one-off trivial hiccups.

## Output
- If nothing actionable: **stay silent** (no filler status).
- If findings: hand the parent a short friction report. Each item must include a typed proposal: **skill** | **bot** | **routine**, with enough detail for the parent to ask the user before creating or changing anything.
- **Never** create or edit skills/bots/routines from this report by yourself.
