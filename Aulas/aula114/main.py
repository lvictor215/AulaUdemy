from classes.cp import ContaPoupanca
from classes.cc import ContaCorrente

c = ContaPoupanca(1001, 1511, 300)

c.depositar(50)
c.sacar(10)
c.sacar(300)
c.sacar(39)
c.sacar(2)


c2 = ContaCorrente(1002, 1000, 1000, 500)


c2.sacar(1010)
c2.sacar(90)
c2.sacar(300)
c2.sacar(150)
c2.depositar(300)
c2.depositar(100)
