"""
lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x.upper(): y*2 for x, y in lista}

print(d1)
"""

d1 = {x for x in range(5)}
print(d1, type(d1))