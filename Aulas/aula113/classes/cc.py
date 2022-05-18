from classes.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    def sacar(self, valor):
        if self._saldo < valor:
            print("Saldo insuficiente")
            return
        self._saldo -= valor
        self.detalhes()
