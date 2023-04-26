def criarMulti(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criarMulti(2)
triplicar = criarMulti(3)
quadruplicar = criarMulti(4)
quintuplicar = criarMulti(5)


print(quadruplicar(3))