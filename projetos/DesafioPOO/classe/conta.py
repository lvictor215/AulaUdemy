from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self._agencia = agencia
        self._conta = conta
        self._saldo = float(saldo)

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    def deposito(self, valor):
        if not isinstance(valor, (int, float)):
            print("=" * 30)
            print("Valor precisa ser numérico")
            print("=" * 30)
            return False
        print("=" * 30)
        print("Operação realizada com sucesso!")
        print("=" * 30)
        self._saldo += float(valor)
        self.resumo()
        return True

    def resumo(self):
        print("=" * 30)
        print(f"Agência: {self._agencia}")
        print(f"Conta: {self._conta}")
        print(f"Saldo atual: R$ {self._saldo:.2f}")
        print("=" * 30)

    @abstractmethod
    def saque(self, valor):
        pass


class ContaPoupanca(Conta):
    def saque(self, valor):
        if self._saldo < valor:
            print("=" * 30)
            print("Saldo insuficiente!")
            print("=" * 30)
            return False
        self._saldo -= valor
        print("=" * 30)
        print("Operação realizada com sucesso!")
        print("=" * 30)
        self.resumo()
        return True


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=200):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    def saque(self, valor):
        if (self._saldo + self._limite) < valor:
            print("Saldo insuficiente!")
            return False
        self._saldo -= valor
        print("Operação realizada com sucesso!")
        self.resumo()
        return True