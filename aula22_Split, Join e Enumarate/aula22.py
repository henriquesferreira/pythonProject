"""
Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumarate - Enumerar elementos da lista # list
strip - Tira espaços no começo e no final da frase
capitalize - Faça com que o primeiro caractere tenha maiúsculas e o restante em minúsculas.
"""

string = 'Bazuca é apelona no jogo'
lista = string.split(' ')
string2 = ','.join(lista)
matriz = [[1,'Cleitin'],[2,'joao']]

for num, nome in matriz:
    print(num, nome)


#for indice, valor in enumerate(lista):
 #   print(indice, valor)
