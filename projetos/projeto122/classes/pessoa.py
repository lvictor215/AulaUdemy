from abc import ABC
from classes.contas import ContaCorrente, ContaPoupanca


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


class Cliente(Pessoa, ContaCorrente, ContaPoupanca):
    def __init__(self, nome, idade, banco, agencia, conta, saldo, tipo_de_conta=1, limite=100):
        Pessoa.__init__(self, nome, idade)
        self._banco = banco

        if tipo_de_conta == 1:
            ContaPoupanca.__init__(self, agencia, conta, saldo)
        elif tipo_de_conta == 2:
            ContaCorrente.__init__(self, agencia, conta, saldo, limite)

