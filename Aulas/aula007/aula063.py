perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '5', 'b': '8', 'c': '3', 'd': '4', },
        'resposta_certa': 'd',
    },
    'Pegunta 2': {
        'pergunta': 'Quanto é 3*2?',
        'respostas': {'a': 6, 'b': 8, 'c': 3, 'd': 4, },
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 7+8?',
        'respostas': {'a': '18', 'b': '15', 'c': '13', 'd': '14', },
        'resposta_certa': 'b',
    },
    'Pegunta 4': {
        'pergunta': 'Quanto é 3*4?',
        'respostas': {'a': 3, 'b': 11, 'c': 12, 'd': 14, },
        'resposta_certa': 'c',
    },
}

for a, b in perguntas.items():
    print(f'Pergunta: {b["pergunta"]}')

    for c, d in b['respostas'].items():
        print(f'[{c}] {d}')

    resposta = input("Digite a resposta: ").lower().strip()[0]
    if resposta == b['resposta_certa']:
        print("Parabéns, você acertou")
    else:
        print("Que pena, você errou!")
    print()
    print()
