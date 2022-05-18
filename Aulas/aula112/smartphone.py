from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            warn = f"{self._nome} está desligado, impossível conectar."
            print(warn)
            self.log_error(warn)
            return

        if self._conectado:
            warn = f"{self._nome} já está conectado! Utilize apenas quando desconectado"
            print(warn)
            self.log_error(warn)
            return
        self._conectado = True
        info = f"{self._nome} obteve êxito na conexão!"
        print(info)
        self.log_info(info)

    def desconectar(self):
        if not self._ligado:
            warn = f"{self._nome} está desligado, não é necessário desconectar"
            print(warn)
            self.log_error(warn)
            return
        if not self._conectado:
            warn = f"{self._nome} já está desconectado, utilize apenas quando conectado!"
            print(warn)
            self.log_error(warn)
            return
        self._conectado = False
        info = f"{self._nome} obteve êxito na desconexão!"
        print(info)
        self.log_info(info)

    def ligar(self):
        if not self._ligado:
            super().ligar()
            info = f"Ligando {self._nome}..."
            print(info)
            self.log_info(info)
            return
        warn = f"{self._nome} já está ligado..."
        print(warn)
        self.log_error(warn)

    def desligar(self):
        if self._ligado:
            super().desligar()
            info = f"Desligando {self._nome}..."
            print(info)
            self.log_info(info)
            return
        warn = f"{self._nome} já está desligado..."
        print(warn)
        self.log_error(warn)
