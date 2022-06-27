from Dados import produtos, pessoas, lista
from functools import reduce

"""
#nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista]

print(lista)
print(list(nova_lista))
"""

"""
def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)
"""

"""
nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)
"""

"""
# Função filter

nova_lista = filter(lambda p: p['preco'] > 50,produtos)

for produto in nova_lista:
    print(produto)
"""

# Função Reduce

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)

soma_idades = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idades / len(pessoas))