
def converteCnpj(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace('/', '')
    cnpj = list(cnpj)
    cnpj = converteIntLista(cnpj)
    return cnpj


def erro_cnpj():
    print("Por favor, digite um cnpj válido!")


def converteIntLista(cnpj):
    listaint = []
    for a in cnpj:
        listaint.append(int(a))
    return listaint