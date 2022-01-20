nome = "Luiz"
altura = 1.81
peso = 70
ano_atual = 2021
ano_nascimento = 1996
idade = ano_atual - ano_nascimento
imc = peso / altura ** 2

print(f"{nome} tem {idade} anos, {altura}m de altura e pesa {peso}kg.")
print(f"O IMC de {nome} é {imc:.2f}.")
print(f"{nome} nasceu em {ano_nascimento}.")
