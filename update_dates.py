import io, json
p = r"articles\\articles.json"
with io.open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
changed = 0
for item in data:
    if item.get('slug') in ('turning-complex-projects-into-controlled-execution','pmo-project-controls-governance'):
        item['publishDate'] = '2026-09-28'
        item['updatedDate'] = '2026-09-28'
        changed += 1
with io.open(p, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Updated entries:', changed)
