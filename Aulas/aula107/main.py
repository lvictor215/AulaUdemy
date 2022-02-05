from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever


escritor = Escritor("Joaozinho")
caneta = Caneta("Bic")
can2 = Caneta("Faber Castell")
maquina = MaquinaDeEscrever()
escritor.ferramenta = can2
escritor.ferramenta.escrever()
print(escritor.nome)
print(caneta.marca)
maquina.escrever()
