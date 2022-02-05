class Estudante:

    def __init__(self, nome='Necessário Cadastro', idade='Necessário cadastro', comendo=False, alimento=None):
        self.__nome = nome
        self.__idade = idade
        self.__comendo = comendo
        self.__alimento = alimento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def comendo(self):
        return self.__comendo

    @comendo.setter
    def comendo(self, alimento=None):
        if alimento is not None:
            self.__comendo = True
            self.__alimento = alimento
        else:
            self.__comendo = False
            self.__alimento = None

    def comer(self):
        if self.__alimento is not None:
            print(f"{self.__nome} está comendo {self.__alimento}!")
        else:
            print(f"{self.__nome} não está comendo no momento")
