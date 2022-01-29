#Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.

def oi():
    return('=' * 50)


def mnd(func):
    return func()


print(mnd(oi))
#Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a função1 executar duas funções que recebam um número diferente de argumentos.


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def oi(nome):
    return f'Oi, {nome}'


def saudacao(nome, saudaca):
    return f'{saudaca}, {nome}'


executando = mestre(saudacao, 'Luiz', 'Bem vindo')

print(executando)