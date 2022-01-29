

def aumento(vlr, aumento):

    vlr += vlr * (aumento / 100)
    return round(vlr, 2)

def reducao(vlr, reducao):
    vlr -= vlr * (reducao / 100)
    return round(vlr, 2)

