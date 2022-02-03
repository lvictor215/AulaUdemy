from funcoes import *

cnpj_digitado = ''
cnpj_calculado = []
cnpj_calculado2 = []
cnpj_final = []
valor = "6543298765432"
valor = list(valor)
total = 0


while True:
    cnpj_digitado = input('Digite o CNPJ: ')
    # cnpj_digitado = '42.968.415/0001-01'
    if len(cnpj_digitado) == 18 or len(cnpj_digitado) == 14:
        cnpj_digitado = converteCnpj(cnpj_digitado)
        if len(cnpj_digitado) == 14:
            break
        else:
            erro_cnpj()
    else:
        erro_cnpj()


for a, b, in enumerate(cnpj_digitado[:-2]):
    cnpj_calculado.append(int(valor[a+1]) * int(b))
    cnpj_final.append(int(b))

total = sum(cnpj_calculado)
total = 11 - total % 11
if total <= 9:
    cnpj_final.append(total)
else:
    cnpj_final.append(0)
cnpj_final = []
for a, b, in enumerate(cnpj_digitado[:-1]):
    cnpj_calculado2.append(int(valor[a]) * int(b))
    cnpj_final.append(int(b))

total = sum(cnpj_calculado2)
total = 11 - (total % 11)

if total <= 9:
    cnpj_final.append(total)
else:
    cnpj_final.append(0)


if cnpj_digitado == cnpj_final:
    print("O CNPJ digitado é Válido!")
else:
    print("O CNPJ digitado é Inválido")
print(f"CNPJ Válido é o {cnpj_final}")
print(cnpj_digitado)