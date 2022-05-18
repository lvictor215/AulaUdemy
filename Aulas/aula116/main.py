class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)

print(r1 + r2)