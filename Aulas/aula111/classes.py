from traceback import print_tb


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nome} está falando...")


class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nome} está comprando...")


class ClienteVip(Cliente):
    def falar(self):
        super().falar()
        print("Voz mais alta!")

    def SalaVip(self):
        print(f"{self.nome} está na sala VIP")
