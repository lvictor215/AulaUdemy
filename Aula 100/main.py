from random import randint

class empresa:
    ano_atual = 2022

    def __init__(self, nome, funcionarios, idade):
        self.nome = nome
        self.funcionarios = funcionarios
        self.idade = idade

    def get_ano_criacao(self):
        print(f"O ano de criação é {self.ano_atual - self.idade}")

    @classmethod
    def por_ano_nascimento(clss, nome, funcionarios, ano_criacao):
        idade = clss.ano_atual - ano_criacao
        return clss(nome, funcionarios, idade)

    @staticmethod
    def getId():
        rand = randint(10000, 19999)
        return rand


emp1 = empresa.por_ano_nascimento("LPTech", 1, 2020)

emp1.get_ano_criacao()
print(emp1.idade)

print(emp1.getId())
