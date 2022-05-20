from classes.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta=None):
        super().__init__(nome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta

    def inserir_conta(self, conta):
        self._conta = conta
