perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '5', 'b': '8', 'c': '3', 'd': '4',},
        'resposta_certa': 'd',
    },
    'Pegunta 2':{
        'pergunta': 'Quanto é 3*2?',
        'respostas': {'a': 6, 'b': 8, 'c': 3, 'd': 4,},
        'resposta_certa': 'a',
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