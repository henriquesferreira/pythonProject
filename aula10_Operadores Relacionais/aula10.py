"""
Operadores Relacionais
== > >= < <= !=
"""

nome = input("Qual seu nome?")
idade = input("Qual seu idade?")

idade = int(idade)

#Limite para pegar empréstimo
idade_menor = 20 # muito jovem
idade_maior = 30 # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f"{nome} pode pegar o empréstimo.")
else:
    print(f"{nome} NÃO pode pegar o empréstimo.")