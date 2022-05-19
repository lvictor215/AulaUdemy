'''
EM PYTHON TUDO É OBJETO: Incluindo classes.
Metaclasses são as "Classes" que criam classes.
type é uma metaclasse (!!!???)
'''


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    def b_fala(self):
        print("Oi")


b = B();