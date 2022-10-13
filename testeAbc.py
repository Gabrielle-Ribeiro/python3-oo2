from collections.abc import MutableSequence


class MinhaListinhaMutavel(MutableSequence):
    pass


objetoValidado = MinhaListinhaMutavel()
# Vai acontecer um erro, pois a classe MinhaListinhaMutavel não
# implementa os métodos abstratos da superclasse.
print(objetoValidado)
