carrinho = list()

carrinho.append(('Produto 1', 3.0))
carrinho.append(('Produto 2', 2.2))
carrinho.append(('Produto 3', 1.1))
carrinho.append(('Produto 4', 3.2))
carrinho.append(('Produto 5', 15.3))
carrinho.append(('Produto 6', 1.5))
carrinho.append(('Produto 7', 25.0))

total = sum([float(x[1]) for x in carrinho])

print(f"O valor total do carrinho é: R$ {total:.2f}")
