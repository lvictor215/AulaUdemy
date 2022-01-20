def m(msg=''):
    print(msg)


num = input("Digite um número para saber se é par ou impar ")
m()
m()

if num != '':

    if num.isnumeric():

        num = int(num)

    else:
        m()
        m("Por favor, digite apenas números inteiros!")
        m()

if isinstance(num, int):
    print(f" O número {num} é ", end='')
    if (num % 2) == 0:
        m("Par")
    else:
        m("Impar")

m()
m()


hora = input("Digite apenas os digitos da hora ")

if hora != '':
    if hora.isnumeric():
        hora = int(hora)
        if not (00 <= hora <= 23):
            m("Favor digitar apenas números no intervalo entre 00 e 23")
            hora = str(hora)
    else:
        m("Favor digitar apenas números inteiros")

if isinstance(hora, int):
    if hora <= 11:
        m("Bom dia!")
    elif hora <= 17:
        m("Boa tarde!")
    else:
        m("Boa noite!")

nome = input("Digite seu nome: ")

if len(nome) <= 4:
    m("Seu nome é muito curto")
elif len(nome) <= 6:
    m("Seu nome é normal")
else:
    m("Seu nome é muito grande")
