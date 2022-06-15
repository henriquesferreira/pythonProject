"""
logged_user = False
msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar'

print (msg)
"""
"""
idade = 17
e_de_maior = (idade >= 18)
msg = 'Pode acesar' if e_de_maior else 'Não pode acessar'

print (msg)
"""

nome = input('Qual seu nome? ')
print (nome or 'Voce n digitou nada')