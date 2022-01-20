nome = input("Digite o nome de usuário: ")
senha = input("Digite sua senha: ")

user = 'luiz'
senh = '12345'


if nome == user and senha == senh:
    print(f'Bem vindo, {nome}!')
else:
    print('Dados incorretos, verifique o nome e execute o programa novamente!')
