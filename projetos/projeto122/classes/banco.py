from abc import ABC, abstractmethod
from classes.pessoa import Cliente
from classes.contas import ContaCorrente, ContaPoupanca


class Banco(Cliente, ):
    def __init__(self, codigo, nome):
        self._codigo = codigo
        self._nome = nome

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @nome.setter
    def nome(self, nome):
        self._nome = nome
