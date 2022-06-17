"""
v1 = 0
v2 = 10

while v1 <= 10 and v2 >= 0:
    print(v1,v2)
    v1 += 1
    v2 -= 1
"""
"""
for v1, v2 in enumerate(range(10, 0, -1)):
    print(v1, v2)
"""

"""
cpf = "16899535009"
novo_cpf = cpf[:-2]
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

if cpf == novo_cpf:
    print("Válido")
else:
    print ("Invalido")
"""