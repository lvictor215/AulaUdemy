'''def saud(sauda="Olá", nome="Usuário"):
    print(f"{sauda}! {nome}.")


saud("Bem vindo", "Luiz")'''


'''def soma(n1=0, n2=0, n3=0):
    print(f"A soma dos valores é igual a: {n1+n2+n3}")


soma(1, 3, 5)'''


'''def aumento(atual, aumento):
    calculo1 = atual * (aumento / 100)
    calculo2 = atual + calculo1

    return calculo2


print(aumento(10850, 15))'''

def valide(num):

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return num


print(valide(15))