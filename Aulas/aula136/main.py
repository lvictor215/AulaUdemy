from dados import *
import json

dados_json = json.dumps(clientes_dicionario, indent=4)
print(dados_json)
lista = json.loads(dados_json)
print(type(lista))
