#Função values: Permite acessar os valores de um dicionario
#Função keys: Permite acessar as chaves de um dicionario
#Função items: Permite acessar todo o conteudo de um dicionario

"""
d1 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla'
}

print('str' in d1)
print('str' in d1.keys())
print('valor' in d1.values())

for k, v in d1.items():
    print(k, v)
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {  'a': '1',  'b': '4',   'c': '5', },
        'resposta_certa' : 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2?',
        'respostas': {  'a': '4',  'b': '10',   'c': '6', },
        'resposta_certa' : 'c',
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")

    print("Respostas: ")
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input("Sua resposta:")

    if resposta_usuario == pv['resposta_certa']:
        print('EHHHHH!!! Você acertou!!!')
        respostas_certas += 1
    else:
        print('IXXIII!!! Você ERROU!!!')

    print()