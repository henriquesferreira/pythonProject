# Função: (continue) pula os codigos posteriores no laço de repetição
# Função: (break) termina o laço de repetição atual

"""
n = 0

while n <= 10:
    print(n)
    n += 1 # n = n + 1
"""

#While / Else
"""
cont = 1
acumulador = 1

while cont <= 10:
    print(cont, acumulador)

    acumulador = acumulador + cont
    cont += 1
else:
    print("Cheguei no else")
"""

#Interando strings com while

frase = 'Vou ali comprar açai'
tamanho = len(frase)
cont = 0

while cont < tamanho:
    print(frase[cont])
    cont += 1