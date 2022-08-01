"""
Exercicio com Abstração, Herança, Encapsulamento e Polimorfismo.
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

"""

from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('Joao', 23)

conta1 = ContaPoupanca(1111, 25467, 0)
conta2 = ContaCorrente(2222, 13432, 0)
conta3 = ContaPoupanca(1212, 75608, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_clientes(cliente1)
banco.inserir_conta(conta1)


if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado')

print('################################')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(40)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado')