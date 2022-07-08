from random import randint

class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Métodos de instancias
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Métodos de classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Métodos estaticos
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
print(p1.idade)
print(Pessoa.gera_id())
print(p1.gera_id())
