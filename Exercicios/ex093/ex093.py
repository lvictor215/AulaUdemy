from uteis import *

options = ['Adicionar nova tarefa', 'Listar todas as tarefas', 'Desfazer última adição', 'Repetir última adição', 'Sair do sistema']
tarefas = None

while True:
    print("Bem vindo ao sistema de anotações!")

    escolha = menu(options)

    if escolha == 5:
        print("Encerrando com segurança...")
        break

    elif escolha == 1:
        print("Digite o texto a ser adicionado:")
        tarefa = input("-->")
        tarefas = adicionar(tarefa, tarefas)

    elif escolha == 2:
        listar(tarefas)

    elif escolha == 3:
        pass

    elif escolha == 4:
        pass

    else:
        print('Favor, digitar uma opção válida!')

