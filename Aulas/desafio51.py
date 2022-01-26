from random import randint

cpf = randint(100000000, 999999999)
cpf_user = str(cpf)

validadorA = validadorB = 0

for a, b in enumerate(range(10, 1, -1)):
    validadorA += int(cpf_user[a]) * b

validadorA = 11 - (validadorA % 11)
if validadorA > 9:
    validadorA = 0
cpf_user += str(validadorA)

for c, d in enumerate(range(11, 1, -1)):
    validadorB += int(cpf_user[c]) * d
validadorB = 11 - (validadorB % 11)
if validadorB > 9:
    validadorB = 0
cpf_user += str(validadorB)


if validadorA == int(cpf_user[9]) and validadorB == int(cpf_user[10]):
    print("Gerado com sucesso!")
    print(cpf_user)

else:
    print("Erro!")
    print(cpf_user)