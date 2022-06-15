"""
:s - Tetxto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_f = 1.2543
print(f"{num_f:.2f}")

num_1 = 1
print(f"{num_1:0>10}")

nome = "cleiton"
print(nome.lower()) # tudo minusculo
print(nome.upper()) # tudo maiusculo
print(nome.title()) # primeiras letras maiusculas