class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getArea(self):
        return self.x * self.y

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other):
        a1 = self.getArea()
        a2 = other.getArea()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.getArea()
        a2 = other.getArea()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        a1 = self.getArea()
        a2 = other.getArea()

        if a1 == a2:
            return True
        else:
            return False


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)

r3 = r2 + r1
print(r2 > r1)
