nome = 'Cleitin'
idade = 15
altura = 1.7
peso = 59
imc = peso / (altura * altura)

#print(nome, "tem", idade, "anos e seu IMC é", imc)
print(f" {nome} tem {idade} anos e seu IMC é {imc:.2f}")
print(" {} tem {} anos e seu IMC é {:.2f}".format(nome, idade, imc))
print(" {n} tem {i} anos e seu IMC é {im:.2f}".format(n=nome, i=idade, im=imc))