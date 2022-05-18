class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('Erro de sistema')


try:
    testar()
except TaErradoError as error:
    print(f"Erro: {error}")