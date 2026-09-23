# Project agent instructions

## Scope

Describe the product, exact repository root, owners and data classification. Preserve existing user changes.

## Definition of Done

1. Record acceptance criteria before implementation.
2. Explain architecture and dependencies before broad edits.
3. Run relevant deterministic tests.
4. For AI behavior, preserve a baseline, Golden Set, regression cases and release gate.
5. Check tracked files and Git history for credentials and private data.
6. Verify real external integrations on their actual platform when available.
7. Report each feature with a truthful status and link evidence.

## Allowed statuses

IMPLEMENTED_AND_TESTED
IMPLEMENTED_NOT_EXTERNAL_VERIFIED
MOCK
BLOCKED_EXTERNAL
DEFERRED_BY_SCOPE
NOT_IMPLEMENTED

## Guardrails

No fabricated users, revenue, customers, model quality or production deployment. Do not auto-send or publish without the project's explicit workflow authorization. Keep secrets out of source control.
