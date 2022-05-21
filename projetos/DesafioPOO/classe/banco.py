class Banco:
    def __init__(self):
        self._agencias = [8872, 1015]
        self._contas = []
        self._clientes = []

    def inserir_cliente(self, cliente):
        self._clientes.append(cliente)
        self._contas.append(cliente.conta)

    def autenticar(self, cliente):
        if cliente not in self._clientes:
            print("Cliente não encontrado")
            return False
        if cliente.conta.agencia not in self._agencias:
            print("Agência não localizada")
            return False
        if cliente.conta not in self._contas:
            print("Conta desconhecida")
            return False
        print("Validado com sucesso")
        return True
