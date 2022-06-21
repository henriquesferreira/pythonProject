"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo horizonte', 'Salvador', 'Monte belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice,
    cidades,
    estados
)

for indice, cidade, estado in cidades_estados:
    print( indice, cidade, estado)
"""

#Exercicio
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for menos que a outra, a soma só vai considerar o tamanho sa menor.
"""

lista_a = [1,2,3,6]
lista_b = [9,5,8]
lista_soma = [x + y for x,y in zip(lista_a, lista_b)]
print(lista_soma)

"""
soma = []
for i in range(len(lista_b)):
    soma.append(lista_a[i] + lista_b[i])
print(soma)
"""

"""
soma = []
for i, _ in enumerate(lista_b):
    soma.append(lista_a[i] + lista_b[i])
print(soma)
"""