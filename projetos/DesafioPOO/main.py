from classe.banco import Banco
from classe.conta import ContaCorrente, ContaPoupanca
from classe.cliente import Cliente


c1 = Cliente("Luiz", 25)
c2 = Cliente("Luiza", 21)
c3 = Cliente("Marcelo", 51)
c4 = Cliente("Arielson", 28)

co1 = ContaCorrente(8872, 42407, 500, 500)
co2 = ContaPoupanca(8872, 333, 10000)
#Conta teste
co3 = ContaCorrente(10145, 312, 10000, 1000)

c1.inserir_conta(co1)
c4.inserir_conta(co3)

nubank = Banco()

nubank.inserir_cliente(c1)
nubank.inserir_cliente(c4)

if nubank.autenticar(c4):
    c4.conta.deposito(100000)
