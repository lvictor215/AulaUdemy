from classe import *


aluno = Estudante()

print("Nome do aluno:", aluno.nome)
aluno.nome = "Luiz"
print("Nome do aluno:", aluno.nome)
print("Idade do aluno:", aluno.idade)
aluno.idade = 25
print("Idade do aluno:", aluno.idade)
aluno.comendo = "Sushi"
aluno.comer()
aluno.comendo = None
aluno.comer()
