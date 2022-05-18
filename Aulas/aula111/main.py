from classes import *

c1 = Cliente("Luiz", 25, 100)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = ClienteVip("Maria", 35, 10000, 5, 10)
print(a1.nome)
a1.falar()
a1.comprar()
a1.SalaVip()
a1.printar()
