class Pessoa:
    def __init__(self, nome=None, *filhos,  idade=None, peso=None, sexo=None):
        self.sexo = sexo
        self.peso = peso
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola!!!{id(self)}'


if __name__ == '__main__':
    josue = Pessoa(nome ='Josue')
    jose = Pessoa(josue, nome='Jose')

    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)

