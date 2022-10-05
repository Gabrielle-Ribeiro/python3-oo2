class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
print(f'Filme: {vingadores.nome} - Ano: {vingadores.nome}'
      f'- Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Filme("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.nome = 'atlanta'
print(f'Filme: {atlanta.nome} - Ano: {atlanta.nome}'
      f'- Duração: {atlanta.duracao} - Likes: {atlanta.likes}')
