from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(selfself, msg):pass


class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()

b.fala('um assunto')
c.fala('outro assunto')