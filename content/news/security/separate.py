import re

with open('_index.md') as f:
    md = f.read().split('\n')

startFlag = False
for i, l in enumerate(md):
    if l.startswith('####'):
        if startFlag:
            with open(''.join(date_i)+'.md', 'w') as f:
                f.write('\n'.join((
                    '---',
                    'title: '+title_i,
                    'date: '+('-').join(date_i),
                    'heading: notice',
                    '---',
                    '\n'.join(md[start_i+2:i])
                )))
            startFlag = False

        if not startFlag:
            start_i = i
            date_i = re.split('年|月|日', md[i+1])[0:3]
            date_i[1:2] = [f'{int(d):02d}' for d in date_i[1:2]]
            title_i = l[4:]
            startFlag = True

if startFlag:
    with open(''.join(date_i)+'.md', 'w') as f:
        f.write('\n'.join((
            '---',
            'title: '+title_i,
            'date: '+('-').join(date_i),
            'heading: notice',
            '---',
            '\n'.join(md[start_i+2:i])
        )))
    startFlag = False
