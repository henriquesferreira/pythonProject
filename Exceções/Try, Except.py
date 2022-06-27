try:
    a = {}
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('Seu codigo foi executado com sucesso')
    print(a)
finally:
    print('Finalmente')

print('Bora continuar...')