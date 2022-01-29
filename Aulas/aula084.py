def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        raise ZeroDivisionError("Erro de divisão")

print(divide(2, 1))
