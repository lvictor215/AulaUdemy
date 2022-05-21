'''
Criar um programa que desmembre um ip, informando seus cálculos:

Repetir endereço com rede ex: 192.168.15.2/24
Repetir apenas o endereço ex: 192.168.15.2
Separar apenas o prefixo, ex: /24
Imprimir máscara de sub-rede: 255.255.255.0
Imprimir endereço IP da rede: 192.168.15.0/24
Imprimir o Broadcast da rede: 192.168.15.255
Imprimir o primeiro host tmb: 192.168.15.1
Imprimir ultimo host da rede: 192.168.15.254
Imprimir o range de IPS rede: 192.168.15.0 <-> 192.168.15.255
Imprimir o total de ips rede: 256 IPs
Imprimir total de ips em uso: 254 IPs


Passos:

128|64|32|16|8|4|2|1

Separar e transformar em binário
192.168.15.2
'''


def paraBinario(numero):
    binario = ''
    bin2 = ''
    while numero > 0:
        resto = numero % 2
        numero = int(numero / 2)
        binario += str(resto)
    for a in range(len(binario) - 1, 0, -1):
        bin2 += binario[a]
    return bin2


print(paraBinario(192))
