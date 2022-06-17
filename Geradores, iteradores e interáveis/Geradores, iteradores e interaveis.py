# '__iter__' Objeto interavel
# '__next__' Objeto interador
# Geradores são uma maneira simples de criar um objeto iterável sem a necessidade de construí-lo dentro de uma classe.

"""
lista = [0,1,2,3,4,5]
lista = iter(lista)
print(hasattr(lista, '__next__'))
"""
"""
import sys

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
"""

