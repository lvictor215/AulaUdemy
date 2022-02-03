from uteis import *

options = [
            'Adicionar nova tarefa',
            'Listar todas as tarefas',
            'Desfazer última adição',
            'Repetir última adição',
            'Sair do sistema'
           ]

tarefas = None
historico = None
ultimaPalavra = ''

while True:
    print("Bem vindo ao sistema de anotações!")

    escolha = menu(options)

    if escolha == 5:
        print("Encerrando com segurança...")
        break

    elif escolha == 1:
        print("Digite o texto a ser adicionado:")
        ultimaPalavra = tarefa = input("-->")
        tarefas = adicionar(tarefa, tarefas)
        historico = GravarHistorico(1, historico)

    elif escolha == 2:
        listar(tarefas)

    elif escolha == 3:
        if historico[-1] == 1 or historico[-1] == 4:
            tarefas.pop()
            historico = GravarHistorico(3, historico)
        elif escolha == 3:
            tarefas.append(ultimaPalavra)
            historico = GravarHistorico(2, historico)

    elif escolha == 4:
        if historico[-1] == 3:
            tarefas.append(ultimaPalavra)
            historico = GravarHistorico(4, historico)
        elif historico[-1] == 2:
            tarefas.pop()
            historico = GravarHistorico(3, historico)
        else:
            print('Só é possível refazer quando desfez alguma operação')

    else:
        print('Favor, digitar uma opção válida!')

