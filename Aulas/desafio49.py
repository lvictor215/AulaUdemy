cpf_user = input("Digite o número do cpf SEM PONTOS OU TRAÇOS: ")

validadorA = validadorB = 0

for a, b in enumerate(range(10, 1, -1)):
    validadorA += int(cpf_user[a]) * b

for c, d in enumerate(range(11, 1, -1)):
    validadorB += int(cpf_user[c]) * d

validadorA = 11 - (validadorA % 11)
validadorB = 11 - (validadorB % 11)

if validadorA > 9:
    validadorA = 0
if validadorB > 9:
    validadorB = 0
if validadorA == int(cpf_user[9]) and validadorB == int(cpf_user[10]):
    print("Validado com sucesso!")

else:
    print("Erro!")