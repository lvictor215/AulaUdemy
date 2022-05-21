import re

class CalcIPv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor): raise ValueError('Ip Inválido!')
        self._ip = valor

    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return
        if not self._valida_ip(valor): raise ValueError('Máscara Inválida!')
        self._mascara = valor
        self._mascarabin = self._ip_to_bin(valor)

    @prefixo.setter
    def prefixo(self, valor):
        if not valor:
            return
        if not isinstance(valor, int):
            raise TypeError("Prefixo precisa ser inteiro")
        if valor > 32:
            raise TypeError("Prefixo precisa ter 32 bits.")
        self._prefixo = valor

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )
        if regexp.search(ip): return True

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]
        print(blocos_binarios)
        return ''.join(blocos_binarios)