from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta=None):
        super().__init__(nome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta):
        self._conta = conta

