from traceback import print_tb


class algo:
    def __init__(self, algof):
        self.algof = algof

    def printar(self):
        print(f"Impresso {self.algof}")


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nome} está falando...")


class Cliente(Pessoa):

    def __init__(self, nome, idade, poderAquisitivo):
        Pessoa.__init__(self, nome, idade)
        self.poderAquisitivo = poderAquisitivo

    def comprar(self):
        print(f"{self.nome} de poder aquisitivo {self.poderAquisitivo} está comprando...")

    def falar(self):
        Pessoa.falar(self)


class ClienteVip(Cliente, algo):

    def __init__(self, nome, idade, poderAquisitivo, padrao, algof):
        Cliente.__init__(self, nome, idade, poderAquisitivo)
        algo.__init__(self, algof)
        self.padrao = padrao

    def falar(self):
        super().falar()
        print("Voz mais alta!")

    def SalaVip(self):
        print(f"{self.nome} está na sala VIP por ser {self.padrao} estrelas")
