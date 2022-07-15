from classes import *

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

c1= Cliente('Luiz', 45)
c1.falar()
c1.comprar()

a1 = Aluno('Cleiton', 21)
a1.falar()
a1.estudar()

p1 = Pessoa('Luiz', 43)
p1.falar()