from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @conta.setter
    def conta(self, conta):
        self._conta = conta

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def deposito(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Apenas valores numéricos são permitidos aqui...")
        self._saldo += valor
        print(f"Importância de R$ {float(valor):.2f} foi depositada com sucesso")
        self.resumo()

    def resumo(self):
        print("=" * 30)
        print(f"Agência: {self._agencia}")
        print(f"Conta: {self._conta}")
        print(f"Saldo atual: R$ {float(self._saldo):.2f}")
        print("=" * 30)

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo=0):
        super().__init__(agencia, conta, saldo)
        print("Criada nova conta poupança")

    def sacar(self, valor):
        if valor > self._saldo:
            print("Impossível, o valor a ser sacado excede o valor em conta.")
            self.resumo()
            return
        print("Sacado com sucesso!")
        self._saldo -= valor
        self.resumo()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
        print("Criada nova conta corrente")

    def sacar(self, valor):
        if valor > (self._saldo + self._limite):
            print(f"Impossível, o valor a ser sacado excede o valor "
                  f"em conta + LIS.\nLIS ATUAL: R$ {float(self._limite):.2f}")
            self.resumo()
            return
        self._saldo -= valor
        self.resumo()
