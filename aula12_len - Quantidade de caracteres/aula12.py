# Código len: Serve para saber a quantidade de caracteres de uma string

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitado foi {len(string1) + len(string2)}')