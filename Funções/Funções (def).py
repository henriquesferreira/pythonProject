"""
def saudacao(saudacao, nome):
    print(saudacao, nome)

saudacao("Bom dia", 'Cleiton')
"""

"""
def soma(n1,n2,n3):
    print (n1+n2+n3)

soma(1,2,3)
"""

"""
def soma(n1, p):
    s = n1 * (p / 100)
    return s + n1

print(soma(50, 10))
"""

"""
def funcao(n1):

    if n1 % 5 == 0 and n1 % 3 == 0:
        return 'FizzBuzz'
    if n1 % 5 == 0:
        return 'buzz'
    if n1 % 3 == 0:
        return 'fizz'
    
    return n1

print(funcao(10))
"""

"""
def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Henrique', sobrenome='Sousa')
"""


def mestre(func, *args, **kwargs):
    return func( *args, **kwargs)

def func1(nome):
    return f'Oi {nome}'

def func2(nome, saudacao):
    return f'{saudacao}, {nome}'

palavra = mestre(func1, 'Luiz')
palavra2 = mestre(func2, 'Luiz','Bom dia')
print (palavra)
print (palavra2)