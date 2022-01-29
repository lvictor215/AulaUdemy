import math

PI = math.pi


def dobra_lista(lis):
    return [x * 2 for x in lis]


def multiplica(lis):
    z = 1
    for x in lis:
        z *= x
    return z


if __name__ == '__main__':
    lista = [x for x in range(1, 6)]

    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
