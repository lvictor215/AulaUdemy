from classe.banco import Banco
from classe.conta import ContaCorrente, ContaPoupanca
from classe.cliente import Cliente


c1 = Cliente("Luiz", 25)
c2 = Cliente("Luiza", 21)
c3 = Cliente("Marcelo", 51)
co1 = ContaCorrente(8872, 42407, 500, 500)
co2 = ContaPoupanca(8872, 333, 10000)

c3.inserir_conta(co2)
c1.inserir_conta(co1)

nubank = Banco()

nubank.inserir_cliente(c1)
nubank.inserir_cliente(c3)

if nubank.autenticar(c3):
    c3.conta.deposito(100000)
