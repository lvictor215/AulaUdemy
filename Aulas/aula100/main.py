class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano(cls, nome, ano):
        idade = cls.ano_atual - ano
        return cls(nome, idade)


p1 = Pessoa.por_ano('Luiz', 1996)

print(p1.idade)