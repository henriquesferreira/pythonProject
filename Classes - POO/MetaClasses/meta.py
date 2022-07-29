"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as "classes" que criam classes.
"""
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace:
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):
    attr_classe = 'Valor A'

class B(A):
    attr_classe = 'Valor B'

b = B()
print(b.attr_classe)

"""
Criando classes a partir da função type

class Pai:
    nome = 'Teste'

A = type(
    'A',
    (Pai,),
    {'attr': 'Olá Mundo!'}
)

a = A()
print(a.nome)
"""