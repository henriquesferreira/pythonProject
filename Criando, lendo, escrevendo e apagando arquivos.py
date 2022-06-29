"""
with open('abc.txt', 'w+') as file:
    file.write('Outra linha\n')
    file.seek(0)
    print(file.read())
"""

import os, json
#os.remove('abc.txt')

d1 = {
    'Pessoa 1' : {
        'nome': 'Rose',
        'idade': 30,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    }
}

d1_json = json.dumps(d1, indent=True)

with open('abs.json', 'w+') as file:
    file.write(d1_json)