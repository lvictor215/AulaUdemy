def inteiro(msg):
    while True:
        escolha = input(msg)

        try:
            escolha = int(escolha)
        except ValueError as error:
            print("Por favor, apenas digite números")
            # print(error)
        else:
            return escolha


def menu(lista):
    print("=" * 50)
    print("Escolha a opção desejada dentre as opções abaixo:")
    for a, b in enumerate(lista):
        print(f'[{a + 1}] {b}')
    print("=" * 50)
    return inteiro("Opção: ")


def adicionar(tarefa, lista=None):
    if lista is None:
        lista = []
    lista.append(tarefa)
    return lista


def listar(lista):
    if type(lista) is not list:
        print("Lista de tarefas vazia, Adicione novas tarefas! =)")
    else:
        for a, b in enumerate(lista):
            print(f"[{a + 1}] {b}")