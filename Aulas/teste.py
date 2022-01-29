'''import time


def gera():
    r = []
    for n in range(1001):
        r.append(n)
        time.sleep(0.001)
    return r


g = gera()

for v in g:
    print(v)
'''


'''
Zip - Unindo iteráveis
Zip_longest - Itertools
'''
'''from itertools import count'''

##Código

'''indices = count()
cidades = ['Salvador', 'Belo Horizonte', 'São Paulo', 'Rio de Janeiro']
estados = ['BA', 'MG', 'SP', 'RJ']


cidades_estados = zip(
    indices,
    estados,
    cidades
)

for indice, estado, cidade in cidades_estados:
    print(f"ID: {indice} | {estado} - {cidade}")'''


# Aula COUNT


# from itertools import count
#
# contador = count(step=0.1)
#
# for x in contador:
#     print(round(x, 2))
#
#     if x >= 9.9:
#         break
#
#
#
# from itertools import combinations, permutations, product
#
# pessoa = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']
#
# for x, y in product(pessoa, repeat=2):
#     print(x, y)
# print()
#
# for x, y in combinations(pessoa, 2):
#     print(x, y)
# print()
#
# for x, y in permutations(pessoa, 2):
#     print(x, y)

# from itertools import groupby, tee
#
# alunos = [
#     {'nome': 'Luiz', 'nota': 'A'},
#     {'nome': 'Letícia', 'nota': 'B'},
#     {'nome': 'Fabrício', 'nota': 'A'},
#     {'nome': 'Rosemary', 'nota': 'C'},
#     {'nome': 'Joana', 'nota': 'D'},
#     {'nome': 'João', 'nota': 'A'},
#     {'nome': 'Eduardo', 'nota': 'B'},
#     {'nome': 'André', 'nota': 'C'},
#     {'nome': 'Anderson', 'nota': 'B'},
# ]
#
# ordena = lambda item: item['nota']
#
# alunos.sort(key=ordena)
#
# alunos_agrupados = groupby(alunos, ordena)
#
# for aluno, b in alunos_agrupados:
#     al1, al2 = tee(b)
#     contador = 0
#     print(f'Nota: {aluno}')
#
#     for alu in al1:
#         print(f'{alu["nome"]}, com nota {alu["nota"]}')
#
#     print(f'{len(list(al2))} Alunos tiraram a nota {aluno}')
