frase = 'Cri5sdasa jjjbbfuhSDaatGEdcFGAeTRSDa'


def len2(msg):
    for a, b in enumerate(msg):
        a += 1
    return a


def upFrase(msg):
    nova_frase = ''
    for a in msg:
        if a == "a":
            a = 'A'
        elif a == "b":
            a = "B"
        elif a == "c":
            a = "C"
        elif a == "d":
            a = "D"
        elif a == "e":
            a = "E"
        elif a == "f":
            a = "F"
        elif a == "g":
            a = "g"
        elif a == "h":
            a = "H"
        elif a == "i":
            a = "I"
        elif a == "j":
            a = "J"
        elif a == "k":
            a = "K"
        elif a == "l":
            a = "L"
        elif a == "m":
            a = "M"
        elif a == "n":
            a = "N"
        elif a == "o":
            a = "O"
        elif a == "p":
            a = "P"
        elif a == "q":
            a = "Q"
        elif a == "r":
            a = "R"
        elif a == "s":
            a = "S"
        elif a == "t":
            a = "T"
        elif a == "u":
            a = "U"
        elif a == "v":
            a = "V"
        elif a == "w":
            a = "W"
        elif a == "x":
            a = "X"
        elif a == "y":
            a = "Y"
        elif a == "z":
            a = "Z"
            
        nova_frase += a
    return nova_frase

def lowFrase(msg):
    nova_frase = ''
    for a in msg:
        nova_frase += a.lower()
    return nova_frase

print(len2(frase))
print(len(frase))

print(upFrase(frase))
print(frase.upper())
