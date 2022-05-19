class Arquivo:
    def __init__(self, arquivo, modo):
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()

#arquivo = open('abc.txt', 'w')
#arquivo.write('Alguma coisa')
#arquivo.close()

with open('abc.txt', 'w+') as arquivo:
    arquivo.write("Luiz Victor")