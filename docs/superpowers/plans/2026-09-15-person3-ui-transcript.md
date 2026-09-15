# Person 3 UI & Transcript Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make the interactive chat visibly report artifact version, tool inputs, results/errors, and persist evidence-friendly transcripts.

**Architecture:** Keep the existing agent loop and transcript schema. Add a small pure formatter in `chat.py`, call it for every tool event, and test it with the standard library so verification works without a provider API key.

**Tech Stack:** Python 3.10+, `unittest`, existing provider/tool registry.

## Global Constraints

- Do not commit `.env`, API keys, real data, cache, or generated tickets.
- Keep all source under `starter_v0/`.
- Preserve the existing transcript JSON fields and artifact hash/version metadata.

---

### Task 1: Tool event display contract

**Files:**
- Create: `starter_v0/tests/test_chat.py`
- Modify: `starter_v0/chat.py`

**Interfaces:**
- Produces `format_tool_event(event) -> str`, a pure formatter containing the tool name, JSON input, and JSON result/error.

- [ ] Write a failing test asserting the formatter exposes tool name, input, result, and error text.
- [ ] Run `python -m unittest discover -s tests -v` from `starter_v0/` and confirm the new test fails because the formatter is absent.
- [ ] Implement the smallest formatter and route each tool event through it in the loop.
- [ ] Re-run the test suite and confirm it passes.
- [ ] Commit the focused UI change.

### Task 2: Offline end-to-end transcript check

**Files:**
- Modify: `starter_v0/tests/test_chat.py`

- [ ] Add a test for the existing `execute_tool_call` error shape and transcript serialization using a temporary directory.
- [ ] Run the test suite and confirm all tests pass.
- [ ] Run syntax compilation and a CLI smoke test with scripted `/exit` input; confirm the startup line includes the artifact version and the final transcript path.
- [ ] Inspect git diff and secret patterns before the final report.

### Task 3: Live-provider handoff

**Files:**
- Verify: `README.md`, `starter_v0/.env.example`, `starter_v0/chat.py`

- [ ] Verify the documented command for a real provider and record that it requires a locally supplied key.
- [ ] Do not create or commit a key; report the exact live-provider blocker if `.env` is absent.
