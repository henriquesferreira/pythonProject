# add (adiciona), update (atualizada), clear, discard (remove)
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

l1 = ['Luiz', 'João', 'Maria']
l2 = ['João', 'Maria','Luiz','Luiz','Luiz','Luiz']

if set(l1) == set (l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')