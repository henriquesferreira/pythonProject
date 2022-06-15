#Função startswith: Verifica a primeira letra de uma string

nome = ['Cleitin', 'João zim']

for valor in nome:
    if valor.lower().startswith('c'):
        continue
    print(valor)
