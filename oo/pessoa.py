class Pessoa:
    def __init__(self, *filhos, nome=None,  idade=None, peso=None, sexo=None):
        self.sexo = sexo
        self.peso = peso
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola!!!{id(self)}'


if __name__ == '__main__':
    josue = Pessoa(nome = 'Josue')
    jose = Pessoa(josue, nome= 'Josue')

    print(Pessoa.cumprimentar(jose))
    print(id(jose))
    print(jose.cumprimentar())
    print(jose.nome)
    print(jose.idade)
    for filho in jose.filhos:
        print(filho.nome)


