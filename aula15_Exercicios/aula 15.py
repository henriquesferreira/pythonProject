#1ºExercicio
"""
valor = input('Digite um numero inteiro: ')

if valor.isnumeric():
    valor = int(valor)
    if valor % 2 == 0:
         print("Seu numero é par")
    else:
        print("Seu numero é impar")
else:
    print("O que foi digitado não é um numero inteiro")
"""

#2ºExercicio
"""
horario = input("Que horas são? ")

if horario.isnumeric():
    horario = int(horario)
    if horario >= 0 and horario <= 11:
        print ("Bom dia")
    elif horario >= 12 and horario <= 17:
        print ("Boa tarde")
    elif horario >= 18 and horario <= 23:
        print("Boa noite")
else:
    print("O que foi digitado não é um numero inteiro")
"""

#3ºExercicio
nome = input("Qual seu primeiro nome? ")
qtd_caracteres = len(nome)

if  qtd_caracteres <= 4:
    print("Seu nome é curto")
elif qtd_caracteres == 5 or qtd_caracteres == 6:
    print("Seu nome é normal")
elif qtd_caracteres > 6:
    print("Seu nome é muito grande")
