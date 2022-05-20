class Banco:
    def __init__(self, nome_banco):
        self._nomeBanco = nome_banco
        self._agencias = [50, 320, 14, 8522]
        self._clientes = []
        self._contas = []

    def cadastro_de_cliente(self, cliente):
        self._clientes.append(cliente)

    def cadastro_de_conta(self, conta):
        self._contas.append(conta)

    def autenticar_cliente(self, cliente):
        if cliente not in self._clientes:
            print("Acesso negado! Cliente não encontrado")
            return False
        print("Cliente encontrado! Validando conta...")
        if cliente.conta not in self._contas:
            print("Acesso negado! Conta não encontrada no sistema.")
            return False
        if cliente.conta.agencia not in self._agencias:
            print("Acesso negado! Agência não encontrada")
            return False
        print("Validado com sucesso!")
        print("Operação realizada com sucesso")
        return True
