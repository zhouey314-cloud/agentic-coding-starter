from pathlib import Path
agents=Path('templates/AGENTS.md').read_text();handoff=Path('templates/HANDOFF.md').read_text()
statuses=['IMPLEMENTED_AND_TESTED','IMPLEMENTED_NOT_EXTERNAL_VERIFIED','MOCK','BLOCKED_EXTERNAL','DEFERRED_BY_SCOPE','NOT_IMPLEMENTED']
for status in statuses:
    if status not in agents or status not in handoff:
        raise ValueError(f'Missing required status: {status}')
for term in ['acceptance criteria','secret','regression','external']:
    if term.lower() not in agents.lower() and term.lower() not in Path('docs/definition-of-done.md').read_text().lower():
        raise ValueError(f'Missing required term: {term}')
print('STARTER_CONTRACT_PASS statuses=6')
