class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter

    @property
    def preco(self):
        return self._preco

    @property
    def nome(self):
        return self._nome

    # Setter

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = valor.upper()
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @nome.setter
    def nome(self, nomevlr):
        self._nome = nomevlr


p1 = Produto('Camiseta', 50)

p1.desconto(10)

print(p1.preco)

p2 = Produto('Caneca', 'r$15')
p2.desconto(10)
print(p2.preco)