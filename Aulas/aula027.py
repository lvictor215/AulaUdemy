usuario = input('Digite o seu usuário: ')
qtd_caracteres = len(usuario)

print(f"Usuário {usuario} tem {qtd_caracteres} caracteres")

if qtd_caracteres < 8:
    print("Quantidade de caracteres mínimos (8)")
    print("FALHA")
else:
    print("Cadastro aprovado!")
