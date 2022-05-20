from classes.banco import Banco
from classes.cliente import Cliente
from classes.conta import ContaCorrente, ContaPoupanca

banco = Banco("Nubank")

cliente1 = Cliente("Luiz", 25)
cliente2 = Cliente("Maria", 18)
cliente3 = Cliente("João", 50)

conta1 = ContaPoupanca(8522, 1996)
conta2 = ContaCorrente(14, 2005)
conta3 = ContaPoupanca(1212, 254138, 100)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.cadastro_de_cliente(cliente2)
banco.cadastro_de_conta(cliente2.conta)

if banco.autenticar_cliente(cliente1):
    cliente1.conta.sacar(20)
