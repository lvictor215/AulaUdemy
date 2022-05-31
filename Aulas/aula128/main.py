class MinhaLista:

    def __init__(self):
        self.__itens = []
        self.__index = 0

    def add(self, valor):
        self.__itens.append(valor)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__itens[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__itens})'

    def __getitem__(self, index):
        return self.__itens[index]

    def __setitem__(self, index, valor):
        if index >= len(self.__itens):
            self.__itens.append(valor)
        self.__itens[index] = valor

    def __delitem__(self, key):
        del self.__itens[key]


if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('Luiz')
    lista.add('Maria')

    lista[0] = "Victor"
    lista[2] = "Luiz"
    print(lista)

    del lista[2]

    print(lista)

    # for valor in lista:
    #     print(valor)
