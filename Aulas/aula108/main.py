from classes import *


carrinho = CarrinhoDeCompras()

p1 = Produto("Camiseta", 50)
p2 = Produto("Iphone", 10000)
p3 = Produto("Caneca", 15)
p4 = Produto("Notebook", 4500)
p5 = Produto("SSD", 250)


carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p5)

carrinho.lista_produto()

print(carrinho.soma_total())
