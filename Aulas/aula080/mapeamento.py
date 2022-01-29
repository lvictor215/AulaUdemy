from aula080 import produtos, pessoas, lista
from itertools import tee

from functools import reduce

# nova_lista = map(lambda x: round(x['preco'] * 30, 2), produtos)
#
# v1, v2 = tee(nova_lista)
#
# for preco in v1:
#     print(f'R$ {preco:.2f}')
#
# print('-' * 15)
# print(f'R$ {sum(v2):.2f}')
#
#
# nomes = map(lambda n: n['nome'], pessoas)
#
# for pessoa in nomes:
#     print(pessoa)
#
# nova_lista = filter(lambda x: x['preco'] > 20, produtos)
#
#
# for a in nova_lista:
#     print(a)


somalista = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)

print(somalista / len(pessoas))
