class A:
    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self):
        print('Eu sou o INIT')


a = A()

