from pathlib import Path
agents=Path('templates/AGENTS.md').read_text();handoff=Path('templates/HANDOFF.md').read_text()
statuses=['IMPLEMENTED_AND_TESTED','IMPLEMENTED_NOT_EXTERNAL_VERIFIED','MOCK','BLOCKED_EXTERNAL','DEFERRED_BY_SCOPE','NOT_IMPLEMENTED']
for status in statuses:assert status in agents and status in handoff,status
for term in ['acceptance criteria','secret','regression','external']:
    assert term.lower() in agents.lower() or term.lower() in Path('docs/definition-of-done.md').read_text().lower()
print('STARTER_CONTRACT_PASS statuses=6')
